# JAVA OPENAPI: Image (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/magicdraw/mdprofiles/Image.html
- source_path: `com/nomagic/uml2/ext/magicdraw/mdprofiles/Image.html`
- source_sha256: `089b17f2d087458ce9ee5e6c5f4e74519784ddb9df4e9aa9831e4d5b8a8a8b01`
- captured_utc: `2026-07-14T16:56:20.277735+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.mdprofiles](package-summary.html)

## Interface Image

All Superinterfaces:
`[BaseElement](../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceImageextends [Element](../classes/mdkernel/Element.html)

begin-user-doc 
 A representation of the model object '***Image***'.
 end-user-doc 
begin-model-doc 
 Physical definition of a graphical image.
 end-model-doc 
The following features are supported:
 [`*Content*`](#getContent())
[`*Format*`](#getFormat())
[`*Location*`](#getLocation())
[`*stereotype Of Icon*`](#get_stereotypeOfIcon())

See Also:
[`UMLPackage.getImage()`](../metadata/UMLPackage.html#getImage())
Model:
annotation="MOF package='mdprofiles'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Stereotype](Stereotype.html)`
`[get_stereotypeOfIcon](#get_stereotypeOfIcon())()`
Returns the value of the '***stereotype Of Icon***' container reference.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getContent](#getContent())()`
Returns the value of the '***Content***' attribute.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFormat](#getFormat())()`
Returns the value of the '***Format***' attribute.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLocation](#getLocation())()`
Returns the value of the '***Location***' attribute.
`void`
`[set_stereotypeOfIcon](#set_stereotypeOfIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Stereotype](Stereotype.html) value)`
Sets the value of the '[`*stereotype Of Icon*`](#get_stereotypeOfIcon())' container reference.
`void`
`[setContent](#setContent(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Content*`](#getContent())' attribute.
`void`
`[setFormat](#setFormat(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Format*`](#getFormat())' attribute.
`void`
`[setLocation](#setLocation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Location*`](#getLocation())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../base/ModelObject.html)
`[get_representationText](../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../base/ModelObject.html#set_representationText(java.lang.String))`
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
getContent
@CheckForNull[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getContent()
Returns the value of the '***Content***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This contains the serialization of the image according to the format. The value could represent a bitmap, image such as a GIF file, or drawing 'instructions'
 using a standard such as Scalable Vector Graphic (SVG) (which is XML based).
 end-model-doc
Returns:
the value of the '*Content*' attribute.
See Also:
[`setContent(String)`](#setContent(java.lang.String))
[`UMLPackage.getImage_Content()`](../metadata/UMLPackage.html#getImage_Content())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"
Generated:
setContent
void setContent(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Content*`](#getContent())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Content*' attribute.
See Also:
[`getContent()`](#getContent())
Generated:
getLocation
@CheckForNull[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLocation()
Returns the value of the '***Location***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This contains a location that can be used by a tool to locate the image as an alternative to embedding it in the stereotype.
 end-model-doc
Returns:
the value of the '*Location*' attribute.
See Also:
[`setLocation(String)`](#setLocation(java.lang.String))
[`UMLPackage.getImage_Location()`](../metadata/UMLPackage.html#getImage_Location())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"
Generated:
setLocation
void setLocation(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Location*`](#getLocation())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Location*' attribute.
See Also:
[`getLocation()`](#getLocation())
Generated:
getFormat
@CheckForNull[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFormat()
Returns the value of the '***Format***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This indicates the format of the content, which is how the string content should be interpreted. The following values are reserved: SVG, GIF, PNG, JPG, WMF, EMF,
 BMP. In addition the prefix 'MIME: ' is also reserved. This option can be used as an alternative to express the reserved values above, for example "SVG" could
 instead be expressed as "MIME: image/svg+xml".
 end-model-doc
Returns:
the value of the '*Format*' attribute.
See Also:
[`setFormat(String)`](#setFormat(java.lang.String))
[`UMLPackage.getImage_Format()`](../metadata/UMLPackage.html#getImage_Format())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"
Generated:
setFormat
void setFormat(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Format*`](#getFormat())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Format*' attribute.
See Also:
[`getFormat()`](#getFormat())
Generated:
get_stereotypeOfIcon
@CheckForNull[Stereotype](Stereotype.html) get_stereotypeOfIcon()
Returns the value of the '***stereotype Of Icon***' container reference.
 It is bidirectional and its opposite is '[`*Icon*`](Stereotype.html#getIcon())'.
 begin-user-doc 
If the meaning of the '*stereotype Of Icon*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*stereotype Of Icon*' container reference.
See Also:
[`set_stereotypeOfIcon(Stereotype)`](#set_stereotypeOfIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
[`UMLPackage.getImage__stereotypeOfIcon()`](../metadata/UMLPackage.html#getImage__stereotypeOfIcon())
[`Stereotype.getIcon()`](Stereotype.html#getIcon())
Model:
opposite="icon" transient="false" ordered="false"
Generated:
set_stereotypeOfIcon
void set_stereotypeOfIcon(@CheckForNull
 [Stereotype](Stereotype.html) value)
Sets the value of the '[`*stereotype Of Icon*`](#get_stereotypeOfIcon())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*stereotype Of Icon*' container reference.
See Also:
[`get_stereotypeOfIcon()`](#get_stereotypeOfIcon())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.mdprofiles</a></div>
<h1 class="title" title="Interface Image">Interface Image</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Image</span><span class="extends-implements">
extends <a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Image</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 Physical definition of a graphical image.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getContent()"><code><em>Content</em></code></a></li>
<li><a href="#getFormat()"><code><em>Format</em></code></a></li>
<li><a href="#getLocation()"><code><em>Location</em></code></a></li>
<li><a href="#get_stereotypeOfIcon()"><code><em>stereotype Of Icon</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../metadata/UMLPackage.html#getImage()"><code>UMLPackage.getImage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='mdprofiles'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_stereotypeOfIcon()">get_stereotypeOfIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>stereotype Of Icon</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContent()">getContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Content</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFormat()">getFormat</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Format</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLocation()">getLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Location</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_stereotypeOfIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">set_stereotypeOfIcon</a><wbr/>(<a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_stereotypeOfIcon()"><code><em>stereotype Of Icon</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setContent(java.lang.String)">setContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getContent()"><code><em>Content</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFormat(java.lang.String)">setFormat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getFormat()"><code><em>Format</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setLocation(java.lang.String)">setLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getLocation()"><code><em>Location</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
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
<section class="detail" id="getContent()">
<h3>getContent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getContent</span>()</div>
<div class="block">Returns the value of the '<em><b>Content</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This contains the serialization of the image according to the format. The value could represent a bitmap, image such as a GIF file, or drawing 'instructions'
 using a standard such as Scalable Vector Graphic (SVG) (which is XML based).
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Content</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setContent(java.lang.String)"><code>setContent(String)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getImage_Content()"><code>UMLPackage.getImage_Content()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContent(java.lang.String)">
<h3>setContent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setContent</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getContent()"><code><em>Content</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Content</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getContent()"><code>getContent()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocation()">
<h3>getLocation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLocation</span>()</div>
<div class="block">Returns the value of the '<em><b>Location</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This contains a location that can be used by a tool to locate the image as an alternative to embedding it in the stereotype.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Location</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setLocation(java.lang.String)"><code>setLocation(String)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getImage_Location()"><code>UMLPackage.getImage_Location()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocation(java.lang.String)">
<h3>setLocation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setLocation</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getLocation()"><code><em>Location</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Location</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getLocation()"><code>getLocation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFormat()">
<h3>getFormat</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFormat</span>()</div>
<div class="block">Returns the value of the '<em><b>Format</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This indicates the format of the content, which is how the string content should be interpreted. The following values are reserved: SVG, GIF, PNG, JPG, WMF, EMF,
 BMP. In addition the prefix 'MIME: ' is also reserved. This option can be used as an alternative to express the reserved values above, for example "SVG" could
 instead be expressed as "MIME: image/svg+xml".
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Format</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setFormat(java.lang.String)"><code>setFormat(String)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getImage_Format()"><code>UMLPackage.getImage_Format()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFormat(java.lang.String)">
<h3>setFormat</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFormat</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getFormat()"><code><em>Format</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Format</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getFormat()"><code>getFormat()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_stereotypeOfIcon()">
<h3>get_stereotypeOfIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">get_stereotypeOfIcon</span>()</div>
<div class="block">Returns the value of the '<em><b>stereotype Of Icon</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Stereotype.html#getIcon()"><code><em>Icon</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>stereotype Of Icon</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>stereotype Of Icon</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_stereotypeOfIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>set_stereotypeOfIcon(Stereotype)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getImage__stereotypeOfIcon()"><code>UMLPackage.getImage__stereotypeOfIcon()</code></a></li>
<li><a href="Stereotype.html#getIcon()"><code>Stereotype.getIcon()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="icon" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_stereotypeOfIcon(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>set_stereotypeOfIcon</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_stereotypeOfIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_stereotypeOfIcon()"><code><em>stereotype Of Icon</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>stereotype Of Icon</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_stereotypeOfIcon()"><code>get_stereotypeOfIcon()</code></a></li>
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
