# JAVA OPENAPI: MultiplicityElement (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html`
- source_sha256: `e1a448da4d3e7b0b4b8dbff60b41d80352cde698f7a827863f5b20a1b42625cf`
- captured_utc: `2026-07-14T16:53:01.087507+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface MultiplicityElement

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[ActionInputPin](../../actions/mdstructuredactions/ActionInputPin.html)`, `[ConnectorEnd](../../compositestructures/mdinternalstructures/ConnectorEnd.html)`, `[ExtensionEnd](../../mdprofiles/ExtensionEnd.html)`, `[InputPin](../../actions/mdbasicactions/InputPin.html)`, `[OutputPin](../../actions/mdbasicactions/OutputPin.html)`, `[Parameter](Parameter.html)`, `[Pin](../../actions/mdbasicactions/Pin.html)`, `[Port](../../compositestructures/mdports/Port.html)`, `[Property](Property.html)`, `[StructuralFeature](StructuralFeature.html)`, `[ValuePin](../../actions/mdbasicactions/ValuePin.html)`, `[Variable](../../activities/mdstructuredactivities/Variable.html)`

public interfaceMultiplicityElementextends [Element](Element.html)

begin-user-doc 
 A representation of the model object '***Multiplicity Element***'.
 end-user-doc 
begin-model-doc 
 A multiplicity is a definition of an inclusive interval of non-negative integers beginning with a lower bound and ending with a (possibly infinite) upper bound. A
 MultiplicityElement embeds this information to specify the allowable cardinalities for an instantiation of the Element.
 end-model-doc 
The following features are supported:
 [`*Ordered*`](#isOrdered())
[`*Unique*`](#isUnique())
[`*Lower*`](#getLower())
[`*Lower Value*`](#getLowerValue())
[`*Upper Value*`](#getUpperValue())
[`*Upper*`](#getUpper())

See Also:
[`UMLPackage.getMultiplicityElement()`](../../metadata/UMLPackage.html#getMultiplicityElement())
Model:
abstract="true"
 annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`int`
`[getLower](#getLower())()`
Returns the value of the '***Lower***' attribute.
`[ValueSpecification](ValueSpecification.html)`
`[getLowerValue](#getLowerValue())()`
Returns the value of the '***Lower Value***' containment reference.
`int`
`[getUpper](#getUpper())()`
Returns the value of the '***Upper***' attribute.
`[ValueSpecification](ValueSpecification.html)`
`[getUpperValue](#getUpperValue())()`
Returns the value of the '***Upper Value***' containment reference.
`boolean`
`[isOrdered](#isOrdered())()`
Returns the value of the '***Ordered***' attribute.
`boolean`
`[isUnique](#isUnique())()`
Returns the value of the '***Unique***' attribute.
`void`
`[setLowerValue](#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](ValueSpecification.html) value)`
Sets the value of the '[`*Lower Value*`](#getLowerValue())' containment reference.
`void`
`[setOrdered](#setOrdered(boolean))(boolean value)`
Sets the value of the '[`*Ordered*`](#isOrdered())' attribute.
`void`
`[setUnique](#setUnique(boolean))(boolean value)`
Sets the value of the '[`*Unique*`](#isUnique())' attribute.
`void`
`[setUpperValue](#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](ValueSpecification.html) value)`
Sets the value of the '[`*Upper Value*`](#getUpperValue())' containment reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
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
isOrdered
boolean isOrdered()
Returns the value of the '***Ordered***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 For a multivalued multiplicity, this attribute specifies whether the values in an instantiation of this MultiplicityElement are sequentially ordered.
 end-model-doc
Returns:
the value of the '*Ordered*' attribute.
See Also:
[`setOrdered(boolean)`](#setOrdered(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getMultiplicityElement_Ordered()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setOrdered
void setOrdered(boolean value)
Sets the value of the '[`*Ordered*`](#isOrdered())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Ordered*' attribute.
See Also:
[`isOrdered()`](#isOrdered())
Generated:
isUnique
boolean isUnique()
Returns the value of the '***Unique***' attribute.
 The default value is `"true"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 For a multivalued multiplicity, this attributes specifies whether the values in an instantiation of this MultiplicityElement are unique.
 end-model-doc
Returns:
the value of the '*Unique*' attribute.
See Also:
[`setUnique(boolean)`](#setUnique(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getMultiplicityElement_Unique()`
Model:
default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setUnique
void setUnique(boolean value)
Sets the value of the '[`*Unique*`](#isUnique())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Unique*' attribute.
See Also:
[`isUnique()`](#isUnique())
Generated:
getUpper
int getUpper()
Returns the value of the '***Upper***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The upper bound of the multiplicity interval.
 end-model-doc
Returns:
the value of the '*Upper*' attribute.
See Also:
[`UMLPackage.getMultiplicityElement_Upper()`](../../metadata/UMLPackage.html#getMultiplicityElement_Upper())
Model:
dataType="com.nomagic.uml2.ext.magicdraw.UnlimitedNatural" required="true" transient="true" changeable="false" volatile="true" derived="true"
 ordered="false"
Generated:
getLower
int getLower()
Returns the value of the '***Lower***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The lower bound of the multiplicity interval.
 end-model-doc
Returns:
the value of the '*Lower*' attribute.
See Also:
[`UMLPackage.getMultiplicityElement_Lower()`](../../metadata/UMLPackage.html#getMultiplicityElement_Lower())
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Integer" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getUpperValue
@CheckForNull[ValueSpecification](ValueSpecification.html) getUpperValue()
Returns the value of the '***Upper Value***' containment reference.
 It is bidirectional and its opposite is '[`*Owning Upper*`](ValueSpecification.html#getOwningUpper())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The specification of the upper bound for this multiplicity.
 end-model-doc
Returns:
the value of the '*Upper Value*' containment reference.
See Also:
[`setUpperValue(ValueSpecification)`](#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getMultiplicityElement_UpperValue()`](../../metadata/UMLPackage.html#getMultiplicityElement_UpperValue())
[`ValueSpecification.getOwningUpper()`](ValueSpecification.html#getOwningUpper())
Model:
opposite="owningUpper" containment="true" resolveProxies="true" ordered="false"
Generated:
setUpperValue
void setUpperValue(@CheckForNull
 [ValueSpecification](ValueSpecification.html) value)
Sets the value of the '[`*Upper Value*`](#getUpperValue())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Upper Value*' containment reference.
See Also:
[`getUpperValue()`](#getUpperValue())
Generated:
getLowerValue
@CheckForNull[ValueSpecification](ValueSpecification.html) getLowerValue()
Returns the value of the '***Lower Value***' containment reference.
 It is bidirectional and its opposite is '[`*Owning Lower*`](ValueSpecification.html#getOwningLower())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The specification of the lower bound for this multiplicity.
 end-model-doc
Returns:
the value of the '*Lower Value*' containment reference.
See Also:
[`setLowerValue(ValueSpecification)`](#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getMultiplicityElement_LowerValue()`](../../metadata/UMLPackage.html#getMultiplicityElement_LowerValue())
[`ValueSpecification.getOwningLower()`](ValueSpecification.html#getOwningLower())
Model:
opposite="owningLower" containment="true" resolveProxies="true" ordered="false"
Generated:
setLowerValue
void setLowerValue(@CheckForNull
 [ValueSpecification](ValueSpecification.html) value)
Sets the value of the '[`*Lower Value*`](#getLowerValue())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Lower Value*' containment reference.
See Also:
[`getLowerValue()`](#getLowerValue())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface MultiplicityElement">Interface MultiplicityElement</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code>, <code><a href="../../compositestructures/mdinternalstructures/ConnectorEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectorEnd</a></code>, <code><a href="../../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code>, <code><a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code>, <code><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code>, <code><a href="../../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code>, <code><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code>, <code><a href="../../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MultiplicityElement</span><span class="extends-implements">
extends <a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Multiplicity Element</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A multiplicity is a definition of an inclusive interval of non-negative integers beginning with a lower bound and ending with a (possibly infinite) upper bound. A
 MultiplicityElement embeds this information to specify the allowable cardinalities for an instantiation of the Element.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#isOrdered()"><code><em>Ordered</em></code></a></li>
<li><a href="#isUnique()"><code><em>Unique</em></code></a></li>
<li><a href="#getLower()"><code><em>Lower</em></code></a></li>
<li><a href="#getLowerValue()"><code><em>Lower Value</em></code></a></li>
<li><a href="#getUpperValue()"><code><em>Upper Value</em></code></a></li>
<li><a href="#getUpper()"><code><em>Upper</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getMultiplicityElement()"><code>UMLPackage.getMultiplicityElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='classes.mdkernel'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLower()">getLower</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Lower</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLowerValue()">getLowerValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Lower Value</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUpper()">getUpper</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Upper</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUpperValue()">getUpperValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Upper Value</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOrdered()">isOrdered</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Ordered</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isUnique()">isUnique</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Unique</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setLowerValue</a><wbr/>(<a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getLowerValue()"><code><em>Lower Value</em></code></a>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOrdered(boolean)">setOrdered</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isOrdered()"><code><em>Ordered</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUnique(boolean)">setUnique</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isUnique()"><code><em>Unique</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setUpperValue</a><wbr/>(<a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getUpperValue()"><code><em>Upper Value</em></code></a>' containment reference.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<section class="detail" id="isOrdered()">
<h3>isOrdered</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOrdered</span>()</div>
<div class="block">Returns the value of the '<em><b>Ordered</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 For a multivalued multiplicity, this attribute specifies whether the values in an instantiation of this MultiplicityElement are sequentially ordered.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Ordered</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOrdered(boolean)"><code>setOrdered(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getMultiplicityElement_Ordered()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOrdered(boolean)">
<h3>setOrdered</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOrdered</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isOrdered()"><code><em>Ordered</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Ordered</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isOrdered()"><code>isOrdered()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUnique()">
<h3>isUnique</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isUnique</span>()</div>
<div class="block">Returns the value of the '<em><b>Unique</b></em>' attribute.
 The default value is <code>"true"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 For a multivalued multiplicity, this attributes specifies whether the values in an instantiation of this MultiplicityElement are unique.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Unique</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setUnique(boolean)"><code>setUnique(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getMultiplicityElement_Unique()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUnique(boolean)">
<h3>setUnique</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUnique</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isUnique()"><code><em>Unique</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Unique</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isUnique()"><code>isUnique()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUpper()">
<h3>getUpper</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getUpper</span>()</div>
<div class="block">Returns the value of the '<em><b>Upper</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The upper bound of the multiplicity interval.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Upper</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getMultiplicityElement_Upper()"><code>UMLPackage.getMultiplicityElement_Upper()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.UnlimitedNatural" required="true" transient="true" changeable="false" volatile="true" derived="true"
 ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLower()">
<h3>getLower</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getLower</span>()</div>
<div class="block">Returns the value of the '<em><b>Lower</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The lower bound of the multiplicity interval.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Lower</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getMultiplicityElement_Lower()"><code>UMLPackage.getMultiplicityElement_Lower()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Integer" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUpperValue()">
<h3>getUpperValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getUpperValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Upper Value</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="ValueSpecification.html#getOwningUpper()"><code><em>Owning Upper</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The specification of the upper bound for this multiplicity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Upper Value</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setUpperValue(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMultiplicityElement_UpperValue()"><code>UMLPackage.getMultiplicityElement_UpperValue()</code></a></li>
<li><a href="ValueSpecification.html#getOwningUpper()"><code>ValueSpecification.getOwningUpper()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningUpper" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setUpperValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUpperValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getUpperValue()"><code><em>Upper Value</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Upper Value</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getUpperValue()"><code>getUpperValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLowerValue()">
<h3>getLowerValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getLowerValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Lower Value</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="ValueSpecification.html#getOwningLower()"><code><em>Owning Lower</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The specification of the lower bound for this multiplicity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Lower Value</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setLowerValue(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMultiplicityElement_LowerValue()"><code>UMLPackage.getMultiplicityElement_LowerValue()</code></a></li>
<li><a href="ValueSpecification.html#getOwningLower()"><code>ValueSpecification.getOwningLower()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningLower" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setLowerValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setLowerValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getLowerValue()"><code><em>Lower Value</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Lower Value</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getLowerValue()"><code>getLowerValue()</code></a></li>
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
