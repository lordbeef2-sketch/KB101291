# JAVA OPENAPI: LinkEndCreationData (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html
- source_path: `com/nomagic/uml2/ext/magicdraw/actions/mdintermediateactions/LinkEndCreationData.html`
- source_sha256: `febd4769e288f1ebf64ef66e29783f2889ebe622a966ad02b36c588cf1bb0a46`
- captured_utc: `2026-07-14T16:56:18.447716+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions](package-summary.html)

## Interface LinkEndCreationData

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[LinkEndData](LinkEndData.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceLinkEndCreationDataextends [LinkEndData](LinkEndData.html)

begin-user-doc 
 A representation of the model object '***Link End Creation Data***'.
 end-user-doc 
begin-model-doc 
 LinkEndCreationData is LinkEndData used to provide values for one end of a link to be created by a CreateLinkAction.
 end-model-doc 
The following features are supported:
 [`*Insert At*`](#getInsertAt())
[`*Replace All*`](#isReplaceAll())
[`*create Link Action Of End Data*`](#get_createLinkActionOfEndData())

See Also:
[`UMLPackage.getLinkEndCreationData()`](../../metadata/UMLPackage.html#getLinkEndCreationData())
Model:
annotation="MOF package='actions.mdintermediateactions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[CreateLinkAction](CreateLinkAction.html)`
`[get_createLinkActionOfEndData](#get_createLinkActionOfEndData())()`
Returns the value of the '***create Link Action Of End Data***' container reference.
`[InputPin](../mdbasicactions/InputPin.html)`
`[getInsertAt](#getInsertAt())()`
Returns the value of the '***Insert At***' reference.
`boolean`
`[isReplaceAll](#isReplaceAll())()`
Returns the value of the '***Replace All***' attribute.
`void`
`[set_createLinkActionOfEndData](#set_createLinkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction))([CreateLinkAction](CreateLinkAction.html) value)`
Sets the value of the '[`*create Link
 Action Of End Data*`](#get_createLinkActionOfEndData())' container reference.
`void`
`[setInsertAt](#setInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin))([InputPin](../mdbasicactions/InputPin.html) value)`
Sets the value of the '[`*Insert At*`](#getInsertAt())' reference.
`void`
`[setReplaceAll](#setReplaceAll(boolean))(boolean value)`
Sets the value of the '[`*Replace All*`](#isReplaceAll())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.[LinkEndData](LinkEndData.html)
`[get_linkActionOfEndData](LinkEndData.html#get_linkActionOfEndData()), [getEnd](LinkEndData.html#getEnd()), [getQualifier](LinkEndData.html#getQualifier()), [getValue](LinkEndData.html#getValue()), [hasQualifier](LinkEndData.html#hasQualifier()), [set_linkActionOfEndData](LinkEndData.html#set_linkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)), [setEnd](LinkEndData.html#setEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [setValue](LinkEndData.html#setValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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
getInsertAt
@CheckForNull[InputPin](../mdbasicactions/InputPin.html) getInsertAt()
Returns the value of the '***Insert At***' reference.
 It is bidirectional and its opposite is
 '[`*link End Creation Data Of Insert At*`](../mdbasicactions/InputPin.html#get_linkEndCreationDataOfInsertAt())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 For ordered Association ends, the InputPin that provides the position where the new link should be inserted or where an existing link should be moved to. The
 type of the insertAt InputPin is UnlimitedNatural, but the input cannot be zero. It is omitted for Association ends that are not ordered.
 end-model-doc
Returns:
the value of the '*Insert At*' reference.
See Also:
[`setInsertAt(InputPin)`](#setInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin))
[`UMLPackage.getLinkEndCreationData_InsertAt()`](../../metadata/UMLPackage.html#getLinkEndCreationData_InsertAt())
[`InputPin.get_linkEndCreationDataOfInsertAt()`](../mdbasicactions/InputPin.html#get_linkEndCreationDataOfInsertAt())
Model:
opposite="_linkEndCreationDataOfInsertAt" ordered="false"
Generated:
setInsertAt
void setInsertAt(@CheckForNull
 [InputPin](../mdbasicactions/InputPin.html) value)
Sets the value of the '[`*Insert At*`](#getInsertAt())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Insert At*' reference.
See Also:
[`getInsertAt()`](#getInsertAt())
Generated:
isReplaceAll
boolean isReplaceAll()
Returns the value of the '***Replace All***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether the existing links emanating from the object on this end should be destroyed before creating a new link.
 end-model-doc
Returns:
the value of the '*Replace All*' attribute.
See Also:
[`setReplaceAll(boolean)`](#setReplaceAll(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getLinkEndCreationData_ReplaceAll()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setReplaceAll
void setReplaceAll(boolean value)
Sets the value of the '[`*Replace All*`](#isReplaceAll())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Replace All*' attribute.
See Also:
[`isReplaceAll()`](#isReplaceAll())
Generated:
get_createLinkActionOfEndData
@CheckForNull[CreateLinkAction](CreateLinkAction.html) get_createLinkActionOfEndData()
Returns the value of the '***create Link Action Of End Data***' container reference.
 It is bidirectional and its opposite is '[`*End Data*`](CreateLinkAction.html#getEndData())'.
 begin-user-doc 
If the meaning of the '*create Link Action Of End Data*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*create Link Action Of End Data*' container reference.
See Also:
[`set_createLinkActionOfEndData(CreateLinkAction)`](#set_createLinkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction))
[`UMLPackage.getLinkEndCreationData__createLinkActionOfEndData()`](../../metadata/UMLPackage.html#getLinkEndCreationData__createLinkActionOfEndData())
[`CreateLinkAction.getEndData()`](CreateLinkAction.html#getEndData())
Model:
opposite="endData" required="true" volatile="true" ordered="false"
Generated:
set_createLinkActionOfEndData
void set_createLinkActionOfEndData(@CheckForNull
 [CreateLinkAction](CreateLinkAction.html) value)
Sets the value of the '[`*create Link
 Action Of End Data*`](#get_createLinkActionOfEndData())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*create Link Action Of End Data*' container reference.
See Also:
[`get_createLinkActionOfEndData()`](#get_createLinkActionOfEndData())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions</a></div>
<h1 class="title" title="Interface LinkEndCreationData">Interface LinkEndCreationData</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">LinkEndCreationData</span><span class="extends-implements">
extends <a href="LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Link End Creation Data</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 LinkEndCreationData is LinkEndData used to provide values for one end of a link to be created by a CreateLinkAction.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getInsertAt()"><code><em>Insert At</em></code></a></li>
<li><a href="#isReplaceAll()"><code><em>Replace All</em></code></a></li>
<li><a href="#get_createLinkActionOfEndData()"><code><em>create Link Action Of End Data</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getLinkEndCreationData()"><code>UMLPackage.getLinkEndCreationData()</code></a></li>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_createLinkActionOfEndData()">get_createLinkActionOfEndData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>create Link Action Of End Data</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInsertAt()">getInsertAt</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Insert At</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isReplaceAll()">isReplaceAll</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Replace All</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_createLinkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction)">set_createLinkActionOfEndData</a><wbr/>(<a href="CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_createLinkActionOfEndData()"><code><em>create Link
 Action Of End Data</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)">setInsertAt</a><wbr/>(<a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getInsertAt()"><code><em>Insert At</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setReplaceAll(boolean)">setReplaceAll</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isReplaceAll()"><code><em>Replace All</em></code></a>' attribute.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.<a href="LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></h3>
<code><a href="LinkEndData.html#get_linkActionOfEndData()">get_linkActionOfEndData</a>, <a href="LinkEndData.html#getEnd()">getEnd</a>, <a href="LinkEndData.html#getQualifier()">getQualifier</a>, <a href="LinkEndData.html#getValue()">getValue</a>, <a href="LinkEndData.html#hasQualifier()">hasQualifier</a>, <a href="LinkEndData.html#set_linkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)">set_linkActionOfEndData</a>, <a href="LinkEndData.html#setEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setEnd</a>, <a href="LinkEndData.html#setValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)">setValue</a></code></div>
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
<section class="detail" id="getInsertAt()">
<h3>getInsertAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></span> <span class="element-name">getInsertAt</span>()</div>
<div class="block">Returns the value of the '<em><b>Insert At</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../mdbasicactions/InputPin.html#get_linkEndCreationDataOfInsertAt()"><code><em>link End Creation Data Of Insert At</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 For ordered Association ends, the InputPin that provides the position where the new link should be inserted or where an existing link should be moved to. The
 type of the insertAt InputPin is UnlimitedNatural, but the input cannot be zero. It is omitted for Association ends that are not ordered.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Insert At</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)"><code>setInsertAt(InputPin)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLinkEndCreationData_InsertAt()"><code>UMLPackage.getLinkEndCreationData_InsertAt()</code></a></li>
<li><a href="../mdbasicactions/InputPin.html#get_linkEndCreationDataOfInsertAt()"><code>InputPin.get_linkEndCreationDataOfInsertAt()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_linkEndCreationDataOfInsertAt" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InputPin)">
<h3>setInsertAt</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInsertAt</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getInsertAt()"><code><em>Insert At</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Insert At</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getInsertAt()"><code>getInsertAt()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReplaceAll()">
<h3>isReplaceAll</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isReplaceAll</span>()</div>
<div class="block">Returns the value of the '<em><b>Replace All</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether the existing links emanating from the object on this end should be destroyed before creating a new link.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Replace All</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setReplaceAll(boolean)"><code>setReplaceAll(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getLinkEndCreationData_ReplaceAll()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReplaceAll(boolean)">
<h3>setReplaceAll</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setReplaceAll</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isReplaceAll()"><code><em>Replace All</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Replace All</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isReplaceAll()"><code>isReplaceAll()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_createLinkActionOfEndData()">
<h3>get_createLinkActionOfEndData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></span> <span class="element-name">get_createLinkActionOfEndData</span>()</div>
<div class="block">Returns the value of the '<em><b>create Link Action Of End Data</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="CreateLinkAction.html#getEndData()"><code><em>End Data</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>create Link Action Of End Data</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>create Link Action Of End Data</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_createLinkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction)"><code>set_createLinkActionOfEndData(CreateLinkAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLinkEndCreationData__createLinkActionOfEndData()"><code>UMLPackage.getLinkEndCreationData__createLinkActionOfEndData()</code></a></li>
<li><a href="CreateLinkAction.html#getEndData()"><code>CreateLinkAction.getEndData()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="endData" required="true" volatile="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_createLinkActionOfEndData(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateLinkAction)">
<h3>set_createLinkActionOfEndData</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_createLinkActionOfEndData</span><wbr/><span class="parameters">(@CheckForNull
 <a href="CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_createLinkActionOfEndData()"><code><em>create Link
 Action Of End Data</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>create Link Action Of End Data</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_createLinkActionOfEndData()"><code>get_createLinkActionOfEndData()</code></a></li>
</ul>
</dd>
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
