# JAVA OPENAPI: Clause (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/Clause.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/Clause.html`
- source_sha256: `b1eda66c2b66672c4788ce2220875c3e3e4d63a992f6d1761cb0a84c78685841`
- captured_utc: `2026-07-14T16:52:47.610352+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities](package-summary.html)

## Interface Clause

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceClauseextends [Element](../../classes/mdkernel/Element.html)

begin-user-doc 
 A representation of the model object '***Clause***'.
 end-user-doc 
begin-model-doc 
 A Clause is an Element that represents a single branch of a ConditionalNode, including a test and a body section. The body section is executed only if (but not
 necessarily if) the test section evaluates to true.
 end-model-doc 
The following features are supported:
 [`*Body*`](#getBody())
[`*Body Output*`](#getBodyOutput())
[`*Decider*`](#getDecider())
[`*Predecessor Clause*`](#getPredecessorClause())
[`*Successor Clause*`](#getSuccessorClause())
[`*Test*`](#getTest())
[`*conditional Node Of Clause*`](#get_conditionalNodeOfClause())

See Also:
[`UMLPackage.getClause()`](../../metadata/UMLPackage.html#getClause())
Model:
annotation="MOF package='activities.mdstructuredactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ConditionalNode](ConditionalNode.html)`
`[get_conditionalNodeOfClause](#get_conditionalNodeOfClause())()`
Returns the value of the '***conditional Node Of Clause***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExecutableNode](ExecutableNode.html)>`
`[getBody](#getBody())()`
Returns the value of the '***Body***' reference list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[OutputPin](../../actions/mdbasicactions/OutputPin.html)>`
`[getBodyOutput](#getBodyOutput())()`
Returns the value of the '***Body Output***' reference list.
`[OutputPin](../../actions/mdbasicactions/OutputPin.html)`
`[getDecider](#getDecider())()`
Returns the value of the '***Decider***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Clause](Clause.html)>`
`[getPredecessorClause](#getPredecessorClause())()`
Returns the value of the '***Predecessor Clause***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Clause](Clause.html)>`
`[getSuccessorClause](#getSuccessorClause())()`
Returns the value of the '***Successor Clause***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExecutableNode](ExecutableNode.html)>`
`[getTest](#getTest())()`
Returns the value of the '***Test***' reference list.
`boolean`
`[hasBody](#hasBody())()`

`boolean`
`[hasBodyOutput](#hasBodyOutput())()`

`boolean`
`[hasPredecessorClause](#hasPredecessorClause())()`

`boolean`
`[hasSuccessorClause](#hasSuccessorClause())()`

`boolean`
`[hasTest](#hasTest())()`

`void`
`[set_conditionalNodeOfClause](#set_conditionalNodeOfClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode))([ConditionalNode](ConditionalNode.html) value)`
Sets the value of the
 '[`*conditional Node Of Clause*`](#get_conditionalNodeOfClause())' container
 reference.
`void`
`[setDecider](#setDecider(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin))([OutputPin](../../actions/mdbasicactions/OutputPin.html) value)`
Sets the value of the '[`*Decider*`](#getDecider())' reference.
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
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
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
getTest
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExecutableNode](ExecutableNode.html)> getTest()
Returns the value of the '***Test***' reference list.
 The list contents are of type [`ExecutableNode`](ExecutableNode.html).
 It is bidirectional and its opposite is
 '[`*clause Of Test*`](ExecutableNode.html#get_clauseOfTest())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of ExecutableNodes that are executed in order to provide a test result for the Clause.
 end-model-doc
Returns:
the value of the '*Test*' reference list.
See Also:
[`UMLPackage.getClause_Test()`](../../metadata/UMLPackage.html#getClause_Test())
[`ExecutableNode.get_clauseOfTest()`](ExecutableNode.html#get_clauseOfTest())
Model:
opposite="_clauseOfTest" required="true" ordered="false"
Generated:
getBody
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExecutableNode](ExecutableNode.html)> getBody()
Returns the value of the '***Body***' reference list.
 The list contents are of type [`ExecutableNode`](ExecutableNode.html).
 It is bidirectional and its opposite is
 '[`*clause Of Body*`](ExecutableNode.html#get_clauseOfBody())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The set of ExecutableNodes that are executed if the test evaluates to true and the Clause is chosen over other Clauses within the ConditionalNode that also have
 tests that evaluate to true.
 end-model-doc
Returns:
the value of the '*Body*' reference list.
See Also:
[`UMLPackage.getClause_Body()`](../../metadata/UMLPackage.html#getClause_Body())
[`ExecutableNode.get_clauseOfBody()`](ExecutableNode.html#get_clauseOfBody())
Model:
opposite="_clauseOfBody" ordered="false"
Generated:
getPredecessorClause
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Clause](Clause.html)> getPredecessorClause()
Returns the value of the '***Predecessor Clause***' reference list.
 The list contents are of type [`Clause`](Clause.html).
 It is bidirectional and its opposite is
 '[`*Successor Clause*`](#getSuccessorClause())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A set of Clauses whose tests must all evaluate to false before this Clause can evaluate its test.
 end-model-doc
Returns:
the value of the '*Predecessor Clause*' reference list.
See Also:
[`UMLPackage.getClause_PredecessorClause()`](../../metadata/UMLPackage.html#getClause_PredecessorClause())
[`getSuccessorClause()`](#getSuccessorClause())
Model:
opposite="successorClause" ordered="false"
Generated:
getSuccessorClause
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Clause](Clause.html)> getSuccessorClause()
Returns the value of the '***Successor Clause***' reference list.
 The list contents are of type [`Clause`](Clause.html).
 It is bidirectional and its opposite is
 '[`*Predecessor Clause*`](#getPredecessorClause())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A set of Clauses that may not evaluate their tests unless the test for this Clause evaluates to false.
 end-model-doc
Returns:
the value of the '*Successor Clause*' reference list.
See Also:
[`UMLPackage.getClause_SuccessorClause()`](../../metadata/UMLPackage.html#getClause_SuccessorClause())
[`getPredecessorClause()`](#getPredecessorClause())
Model:
opposite="predecessorClause" ordered="false"
Generated:
getBodyOutput
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[OutputPin](../../actions/mdbasicactions/OutputPin.html)> getBodyOutput()
Returns the value of the '***Body Output***' reference list.
 The list contents are of type [`OutputPin`](../../actions/mdbasicactions/OutputPin.html).
 It is bidirectional and its opposite is
 '[`*clause Of Body Output*`](../../actions/mdbasicactions/OutputPin.html#get_clauseOfBodyOutput())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The OutputPins on Actions within the body section whose values are moved to the result OutputPins of the containing ConditionalNode after execution of the body.
 end-model-doc
Returns:
the value of the '*Body Output*' reference list.
See Also:
[`UMLPackage.getClause_BodyOutput()`](../../metadata/UMLPackage.html#getClause_BodyOutput())
[`OutputPin.get_clauseOfBodyOutput()`](../../actions/mdbasicactions/OutputPin.html#get_clauseOfBodyOutput())
Model:
opposite="_clauseOfBodyOutput"
Generated:
get_conditionalNodeOfClause
@CheckForNull[ConditionalNode](ConditionalNode.html) get_conditionalNodeOfClause()
Returns the value of the '***conditional Node Of Clause***' container reference.
 It is bidirectional and its opposite is '[`*Clause*`](ConditionalNode.html#getClause())'.
 begin-user-doc 
If the meaning of the '*conditional Node Of Clause*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*conditional Node Of Clause*' container reference.
See Also:
[`set_conditionalNodeOfClause(ConditionalNode)`](#set_conditionalNodeOfClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode))
[`UMLPackage.getClause__conditionalNodeOfClause()`](../../metadata/UMLPackage.html#getClause__conditionalNodeOfClause())
[`ConditionalNode.getClause()`](ConditionalNode.html#getClause())
Model:
opposite="clause" required="true" transient="false" ordered="false"
Generated:
set_conditionalNodeOfClause
void set_conditionalNodeOfClause(@CheckForNull
 [ConditionalNode](ConditionalNode.html) value)
Sets the value of the
 '[`*conditional Node Of Clause*`](#get_conditionalNodeOfClause())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*conditional Node Of Clause*' container reference.
See Also:
[`get_conditionalNodeOfClause()`](#get_conditionalNodeOfClause())
Generated:
getDecider
@CheckForNull[OutputPin](../../actions/mdbasicactions/OutputPin.html) getDecider()
Returns the value of the '***Decider***' reference.
 It is bidirectional and its opposite is '[`*clause Of Decider*`](../../actions/mdbasicactions/OutputPin.html#get_clauseOfDecider())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An OutputPin on an Action in the test section whose Boolean value determines the result of the test.
 end-model-doc
Returns:
the value of the '*Decider*' reference.
See Also:
[`setDecider(OutputPin)`](#setDecider(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin))
[`UMLPackage.getClause_Decider()`](../../metadata/UMLPackage.html#getClause_Decider())
[`OutputPin.get_clauseOfDecider()`](../../actions/mdbasicactions/OutputPin.html#get_clauseOfDecider())
Model:
opposite="_clauseOfDecider" required="true" ordered="false"
Generated:
setDecider
void setDecider(@CheckForNull
 [OutputPin](../../actions/mdbasicactions/OutputPin.html) value)
Sets the value of the '[`*Decider*`](#getDecider())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Decider*' reference.
See Also:
[`getDecider()`](#getDecider())
Generated:
hasTest
boolean hasTest()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasBody
boolean hasBody()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPredecessorClause
boolean hasPredecessorClause()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasSuccessorClause
boolean hasSuccessorClause()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasBodyOutput
boolean hasBodyOutput()
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
<h1 class="title" title="Interface Clause">Interface Clause</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Clause</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Clause</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Clause is an Element that represents a single branch of a ConditionalNode, including a test and a body section. The body section is executed only if (but not
 necessarily if) the test section evaluates to true.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getBody()"><code><em>Body</em></code></a></li>
<li><a href="#getBodyOutput()"><code><em>Body Output</em></code></a></li>
<li><a href="#getDecider()"><code><em>Decider</em></code></a></li>
<li><a href="#getPredecessorClause()"><code><em>Predecessor Clause</em></code></a></li>
<li><a href="#getSuccessorClause()"><code><em>Successor Clause</em></code></a></li>
<li><a href="#getTest()"><code><em>Test</em></code></a></li>
<li><a href="#get_conditionalNodeOfClause()"><code><em>conditional Node Of Clause</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getClause()"><code>UMLPackage.getClause()</code></a></li>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_conditionalNodeOfClause()">get_conditionalNodeOfClause</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>conditional Node Of Clause</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBody()">getBody</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Body</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBodyOutput()">getBodyOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Body Output</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDecider()">getDecider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Decider</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPredecessorClause()">getPredecessorClause</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Predecessor Clause</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSuccessorClause()">getSuccessorClause</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Successor Clause</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTest()">getTest</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Test</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasBody()">hasBody</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasBodyOutput()">hasBodyOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPredecessorClause()">hasPredecessorClause</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasSuccessorClause()">hasSuccessorClause</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasTest()">hasTest</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_conditionalNodeOfClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)">set_conditionalNodeOfClause</a><wbr/>(<a href="ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_conditionalNodeOfClause()"><code><em>conditional Node Of Clause</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDecider(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)">setDecider</a><wbr/>(<a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDecider()"><code><em>Decider</em></code></a>' reference.</div>
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
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
<section class="detail" id="getTest()">
<h3>getTest</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a>&gt;</span> <span class="element-name">getTest</span>()</div>
<div class="block">Returns the value of the '<em><b>Test</b></em>' reference list.
 The list contents are of type <a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a>.
 It is bidirectional and its opposite is
 '<a href="ExecutableNode.html#get_clauseOfTest()"><code><em>clause Of Test</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of ExecutableNodes that are executed in order to provide a test result for the Clause.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Test</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getClause_Test()"><code>UMLPackage.getClause_Test()</code></a></li>
<li><a href="ExecutableNode.html#get_clauseOfTest()"><code>ExecutableNode.get_clauseOfTest()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_clauseOfTest" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBody()">
<h3>getBody</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a>&gt;</span> <span class="element-name">getBody</span>()</div>
<div class="block">Returns the value of the '<em><b>Body</b></em>' reference list.
 The list contents are of type <a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a>.
 It is bidirectional and its opposite is
 '<a href="ExecutableNode.html#get_clauseOfBody()"><code><em>clause Of Body</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The set of ExecutableNodes that are executed if the test evaluates to true and the Clause is chosen over other Clauses within the ConditionalNode that also have
 tests that evaluate to true.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Body</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getClause_Body()"><code>UMLPackage.getClause_Body()</code></a></li>
<li><a href="ExecutableNode.html#get_clauseOfBody()"><code>ExecutableNode.get_clauseOfBody()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_clauseOfBody" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPredecessorClause()">
<h3>getPredecessorClause</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a>&gt;</span> <span class="element-name">getPredecessorClause</span>()</div>
<div class="block">Returns the value of the '<em><b>Predecessor Clause</b></em>' reference list.
 The list contents are of type <a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getSuccessorClause()"><code><em>Successor Clause</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A set of Clauses whose tests must all evaluate to false before this Clause can evaluate its test.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Predecessor Clause</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getClause_PredecessorClause()"><code>UMLPackage.getClause_PredecessorClause()</code></a></li>
<li><a href="#getSuccessorClause()"><code>getSuccessorClause()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="successorClause" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuccessorClause()">
<h3>getSuccessorClause</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a>&gt;</span> <span class="element-name">getSuccessorClause</span>()</div>
<div class="block">Returns the value of the '<em><b>Successor Clause</b></em>' reference list.
 The list contents are of type <a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getPredecessorClause()"><code><em>Predecessor Clause</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A set of Clauses that may not evaluate their tests unless the test for this Clause evaluates to false.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Successor Clause</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getClause_SuccessorClause()"><code>UMLPackage.getClause_SuccessorClause()</code></a></li>
<li><a href="#getPredecessorClause()"><code>getPredecessorClause()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="predecessorClause" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBodyOutput()">
<h3>getBodyOutput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a>&gt;</span> <span class="element-name">getBodyOutput</span>()</div>
<div class="block">Returns the value of the '<em><b>Body Output</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../actions/mdbasicactions/OutputPin.html#get_clauseOfBodyOutput()"><code><em>clause Of Body Output</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The OutputPins on Actions within the body section whose values are moved to the result OutputPins of the containing ConditionalNode after execution of the body.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Body Output</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getClause_BodyOutput()"><code>UMLPackage.getClause_BodyOutput()</code></a></li>
<li><a href="../../actions/mdbasicactions/OutputPin.html#get_clauseOfBodyOutput()"><code>OutputPin.get_clauseOfBodyOutput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_clauseOfBodyOutput"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_conditionalNodeOfClause()">
<h3>get_conditionalNodeOfClause</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></span> <span class="element-name">get_conditionalNodeOfClause</span>()</div>
<div class="block">Returns the value of the '<em><b>conditional Node Of Clause</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="ConditionalNode.html#getClause()"><code><em>Clause</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>conditional Node Of Clause</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>conditional Node Of Clause</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_conditionalNodeOfClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)"><code>set_conditionalNodeOfClause(ConditionalNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClause__conditionalNodeOfClause()"><code>UMLPackage.getClause__conditionalNodeOfClause()</code></a></li>
<li><a href="ConditionalNode.html#getClause()"><code>ConditionalNode.getClause()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="clause" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_conditionalNodeOfClause(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)">
<h3>set_conditionalNodeOfClause</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_conditionalNodeOfClause</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_conditionalNodeOfClause()"><code><em>conditional Node Of Clause</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>conditional Node Of Clause</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_conditionalNodeOfClause()"><code>get_conditionalNodeOfClause()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDecider()">
<h3>getDecider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></span> <span class="element-name">getDecider</span>()</div>
<div class="block">Returns the value of the '<em><b>Decider</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/OutputPin.html#get_clauseOfDecider()"><code><em>clause Of Decider</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An OutputPin on an Action in the test section whose Boolean value determines the result of the test.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Decider</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setDecider(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)"><code>setDecider(OutputPin)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getClause_Decider()"><code>UMLPackage.getClause_Decider()</code></a></li>
<li><a href="../../actions/mdbasicactions/OutputPin.html#get_clauseOfDecider()"><code>OutputPin.get_clauseOfDecider()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_clauseOfDecider" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDecider(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)">
<h3>setDecider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDecider</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDecider()"><code><em>Decider</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Decider</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getDecider()"><code>getDecider()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasTest()">
<h3>hasTest</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasTest</span>()
         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasBody()">
<h3>hasBody</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasBody</span>()
         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPredecessorClause()">
<h3>hasPredecessorClause</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPredecessorClause</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSuccessorClause()">
<h3>hasSuccessorClause</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasSuccessorClause</span>()
                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasBodyOutput()">
<h3>hasBodyOutput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasBodyOutput</span>()
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
