# JAVA OPENAPI: LinkEndData (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndData.html
- source_path: `com/nomagic/uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndData.html`
- source_sha256: `765caaf870201b634b4680a81376e3502cb25969cd5de8720d3f47365445c93a`
- captured_utc: `2026-07-14T16:52:44.174306+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions](package-summary.html)

## Interface LinkEndData

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[LinkEndCreationData](LinkEndCreationData.html)`, `[LinkEndDestructionData](LinkEndDestructionData.html)`

public interfaceLinkEndDataextends [Element](../../classes/mdkernel/Element.html)

begin-user-doc 
 A representation of the model object '***Link End Data***'.
 end-user-doc 
begin-model-doc 
 LinkEndData is an Element that identifies on end of a link to be read or written by a LinkAction. As a link (that is not a link object) cannot be passed as a
 runtime value to or from an Action, it is instead identified by its end objects and qualifier values, if any. A LinkEndData instance provides these values for a
 single Association end.
 end-model-doc 
The following features are supported:
 [`*End*`](#getEnd())
[`*Qualifier*`](#getQualifier())
[`*Value*`](#getValue())
[`*link Action Of End Data*`](#get_linkActionOfEndData())

See Also:
[`UMLPackage.getLinkEndData()`](../../metadata/UMLPackage.html#getLinkEndData())
Model:
annotation="MOF package='actions.mdintermediateactions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[LinkAction](LinkAction.html)`
`[get_linkActionOfEndData](#get_linkActionOfEndData())()`
Returns the value of the '***link Action Of End Data***' container reference.
`[Property](../../classes/mdkernel/Property.html)`
`[getEnd](#getEnd())()`
Returns the value of the '***End***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[QualifierValue](../mdcompleteactions/QualifierValue.html)>`
`[getQualifier](#getQualifier())()`
Returns the value of the '***Qualifier***' containment reference list.
`[InputPin](../mdbasicactions/InputPin.html)`
`[getValue](#getValue())()`
Returns the value of the '***Value***' reference.
`boolean`
`[hasQualifier](#hasQualifier())()`

`void`
`[set_linkActionOfEndData](#set_linkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction))([LinkAction](LinkAction.html) value)`
Sets the value of the '[`*link Action Of End Data*`](#get_linkActionOfEndData())'
 container reference.
`void`
`[setEnd](#setEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../classes/mdkernel/Property.html) value)`
Sets the value of the '[`*End*`](#getEnd())' reference.
`void`
`[setValue](#setValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin))([InputPin](../mdbasicactions/InputPin.html) value)`
Sets the value of the '[`*Value*`](#getValue())' reference.
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
getValue
@CheckForNull[InputPin](../mdbasicactions/InputPin.html) getValue()
Returns the value of the '***Value***' reference.
 It is bidirectional and its opposite is
 '[`*link End Data Of Value*`](../mdbasicactions/InputPin.html#get_linkEndDataOfValue())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The InputPin that provides the specified value for the given end. This InputPin is omitted if the LinkEndData specifies the "open" end for a ReadLinkAction.
 end-model-doc
Returns:
the value of the '*Value*' reference.
See Also:
[`setValue(InputPin)`](#setValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin))
[`UMLPackage.getLinkEndData_Value()`](../../metadata/UMLPackage.html#getLinkEndData_Value())
[`InputPin.get_linkEndDataOfValue()`](../mdbasicactions/InputPin.html#get_linkEndDataOfValue())
Model:
opposite="_linkEndDataOfValue" ordered="false"
Generated:
setValue
void setValue(@CheckForNull
 [InputPin](../mdbasicactions/InputPin.html) value)
Sets the value of the '[`*Value*`](#getValue())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Value*' reference.
See Also:
[`getValue()`](#getValue())
Generated:
getEnd
@CheckForNull[Property](../../classes/mdkernel/Property.html) getEnd()
Returns the value of the '***End***' reference.
 It is bidirectional and its opposite is '[`*link End Data Of End*`](../../classes/mdkernel/Property.html#get_linkEndDataOfEnd())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Association end for which this LinkEndData specifies values.
 end-model-doc
Returns:
the value of the '*End*' reference.
See Also:
[`setEnd(Property)`](#setEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))
[`UMLPackage.getLinkEndData_End()`](../../metadata/UMLPackage.html#getLinkEndData_End())
[`Property.get_linkEndDataOfEnd()`](../../classes/mdkernel/Property.html#get_linkEndDataOfEnd())
Model:
opposite="_linkEndDataOfEnd" required="true" ordered="false"
Generated:
setEnd
void setEnd(@CheckForNull
 [Property](../../classes/mdkernel/Property.html) value)
Sets the value of the '[`*End*`](#getEnd())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*End*' reference.
See Also:
[`getEnd()`](#getEnd())
Generated:
get_linkActionOfEndData
@CheckForNull[LinkAction](LinkAction.html) get_linkActionOfEndData()
Returns the value of the '***link Action Of End Data***' container reference.
 It is bidirectional and its opposite is '[`*End Data*`](LinkAction.html#getEndData())'.
 begin-user-doc 
If the meaning of the '*link Action Of End Data*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*link Action Of End Data*' container reference.
See Also:
[`set_linkActionOfEndData(LinkAction)`](#set_linkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction))
[`UMLPackage.getLinkEndData__linkActionOfEndData()`](../../metadata/UMLPackage.html#getLinkEndData__linkActionOfEndData())
[`LinkAction.getEndData()`](LinkAction.html#getEndData())
Model:
opposite="endData" required="true" transient="false" ordered="false"
Generated:
set_linkActionOfEndData
void set_linkActionOfEndData(@CheckForNull
 [LinkAction](LinkAction.html) value)
Sets the value of the '[`*link Action Of End Data*`](#get_linkActionOfEndData())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*link Action Of End Data*' container reference.
See Also:
[`get_linkActionOfEndData()`](#get_linkActionOfEndData())
Generated:
getQualifier
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[QualifierValue](../mdcompleteactions/QualifierValue.html)> getQualifier()
Returns the value of the '***Qualifier***' containment reference list.
 The list contents are of type [`QualifierValue`](../mdcompleteactions/QualifierValue.html).
 It is bidirectional and its opposite is
 '[`*link End Data Of Qualifier*`](../mdcompleteactions/QualifierValue.html#get_linkEndDataOfQualifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A set of QualifierValues used to provide values for the qualifiers of the end.
 end-model-doc
Returns:
the value of the '*Qualifier*' containment reference list.
See Also:
[`UMLPackage.getLinkEndData_Qualifier()`](../../metadata/UMLPackage.html#getLinkEndData_Qualifier())
[`QualifierValue.get_linkEndDataOfQualifier()`](../mdcompleteactions/QualifierValue.html#get_linkEndDataOfQualifier())
Model:
opposite="_linkEndDataOfQualifier" containment="true" resolveProxies="true" ordered="false"
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions</a></div>
<h1 class="title" title="Interface LinkEndData">Interface LinkEndData</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></code>, <code><a href="LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">LinkEndData</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Link End Data</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 LinkEndData is an Element that identifies on end of a link to be read or written by a LinkAction. As a link (that is not a link object) cannot be passed as a
 runtime value to or from an Action, it is instead identified by its end objects and qualifier values, if any. A LinkEndData instance provides these values for a
 single Association end.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getEnd()"><code><em>End</em></code></a></li>
<li><a href="#getQualifier()"><code><em>Qualifier</em></code></a></li>
<li><a href="#getValue()"><code><em>Value</em></code></a></li>
<li><a href="#get_linkActionOfEndData()"><code><em>link Action Of End Data</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getLinkEndData()"><code>UMLPackage.getLinkEndData()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='actions.mdintermediateactions'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_linkActionOfEndData()">get_linkActionOfEndData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>link Action Of End Data</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEnd()">getEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>End</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getQualifier()">getQualifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Qualifier</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Value</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasQualifier()">hasQualifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_linkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)">set_linkActionOfEndData</a><wbr/>(<a href="LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_linkActionOfEndData()"><code><em>link Action Of End Data</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setEnd</a><wbr/>(<a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getEnd()"><code><em>End</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)">setValue</a><wbr/>(<a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getValue()"><code><em>Value</em></code></a>' reference.</div>
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
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></span> <span class="element-name">getValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Value</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../mdbasicactions/InputPin.html#get_linkEndDataOfValue()"><code><em>link End Data Of Value</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The InputPin that provides the specified value for the given end. This InputPin is omitted if the LinkEndData specifies the "open" end for a ReadLinkAction.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Value</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)"><code>setValue(InputPin)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLinkEndData_Value()"><code>UMLPackage.getLinkEndData_Value()</code></a></li>
<li><a href="../mdbasicactions/InputPin.html#get_linkEndDataOfValue()"><code>InputPin.get_linkEndDataOfValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_linkEndDataOfValue" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)">
<h3>setValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getValue()"><code><em>Value</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Value</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getValue()"><code>getValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnd()">
<h3>getEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getEnd</span>()</div>
<div class="block">Returns the value of the '<em><b>End</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/Property.html#get_linkEndDataOfEnd()"><code><em>link End Data Of End</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Association end for which this LinkEndData specifies values.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>End</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)"><code>setEnd(Property)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLinkEndData_End()"><code>UMLPackage.getLinkEndData_End()</code></a></li>
<li><a href="../../classes/mdkernel/Property.html#get_linkEndDataOfEnd()"><code>Property.get_linkEndDataOfEnd()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_linkEndDataOfEnd" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>setEnd</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEnd</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getEnd()"><code><em>End</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>End</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getEnd()"><code>getEnd()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_linkActionOfEndData()">
<h3>get_linkActionOfEndData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></span> <span class="element-name">get_linkActionOfEndData</span>()</div>
<div class="block">Returns the value of the '<em><b>link Action Of End Data</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="LinkAction.html#getEndData()"><code><em>End Data</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>link Action Of End Data</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>link Action Of End Data</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_linkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)"><code>set_linkActionOfEndData(LinkAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLinkEndData__linkActionOfEndData()"><code>UMLPackage.getLinkEndData__linkActionOfEndData()</code></a></li>
<li><a href="LinkAction.html#getEndData()"><code>LinkAction.getEndData()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="endData" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_linkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)">
<h3>set_linkActionOfEndData</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_linkActionOfEndData</span><wbr/><span class="parameters">(@CheckForNull
 <a href="LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_linkActionOfEndData()"><code><em>link Action Of End Data</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>link Action Of End Data</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_linkActionOfEndData()"><code>get_linkActionOfEndData()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifier()">
<h3>getQualifier</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a>&gt;</span> <span class="element-name">getQualifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Qualifier</b></em>' containment reference list.
 The list contents are of type <a href="../mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>QualifierValue</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdcompleteactions/QualifierValue.html#get_linkEndDataOfQualifier()"><code><em>link End Data Of Qualifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A set of QualifierValues used to provide values for the qualifiers of the end.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Qualifier</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getLinkEndData_Qualifier()"><code>UMLPackage.getLinkEndData_Qualifier()</code></a></li>
<li><a href="../mdcompleteactions/QualifierValue.html#get_linkEndDataOfQualifier()"><code>QualifierValue.get_linkEndDataOfQualifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_linkEndDataOfQualifier" containment="true" resolveProxies="true" ordered="false"</dd>
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
