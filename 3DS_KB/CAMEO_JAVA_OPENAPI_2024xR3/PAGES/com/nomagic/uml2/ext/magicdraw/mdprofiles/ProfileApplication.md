# JAVA OPENAPI: ProfileApplication (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/mdprofiles/ProfileApplication.html
- source_path: `com/nomagic/uml2/ext/magicdraw/mdprofiles/ProfileApplication.html`
- source_sha256: `d1684f002a93d52a7b2dd973d204eb81e7ed5664d2cb44a88de84efd09e7db81`
- captured_utc: `2026-07-14T16:56:25.470797+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.mdprofiles](package-summary.html)

## Interface ProfileApplication

All Superinterfaces:
`[BaseElement](../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[DirectedRelationship](../classes/mdkernel/DirectedRelationship.html)`, `[Element](../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[Relationship](../classes/mdkernel/Relationship.html)`

public interfaceProfileApplicationextends [DirectedRelationship](../classes/mdkernel/DirectedRelationship.html)

begin-user-doc 
 A representation of the model object '***Profile Application***'.
 end-user-doc 
begin-model-doc 
 A profile application is used to show which profiles have been applied to a package.
 end-model-doc 
The following features are supported:
 [`*Applied Profile*`](#getAppliedProfile())
[`*Strict*`](#isStrict())
[`*Applying Package*`](#getApplyingPackage())

See Also:
[`UMLPackage.getProfileApplication()`](../metadata/UMLPackage.html#getProfileApplication())
Model:
annotation="MOF package='mdprofiles'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Profile](Profile.html)`
`[getAppliedProfile](#getAppliedProfile())()`
Returns the value of the '***Applied Profile***' reference.
`[Package](../classes/mdkernel/Package.html)`
`[getApplyingPackage](#getApplyingPackage())()`
Returns the value of the '***Applying Package***' container reference.
`boolean`
`[isStrict](#isStrict())()`
Returns the value of the '***Strict***' attribute.
`void`
`[setAppliedProfile](#setAppliedProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Profile](Profile.html) value)`
Sets the value of the '[`*Applied Profile*`](#getAppliedProfile())' reference.
`void`
`[setApplyingPackage](#setApplyingPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../classes/mdkernel/Package.html) value)`
Sets the value of the '[`*Applying Package*`](#getApplyingPackage())' container reference.
`void`
`[setStrict](#setStrict(boolean))(boolean value)`
Sets the value of the '[`*Strict*`](#isStrict())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[DirectedRelationship](../classes/mdkernel/DirectedRelationship.html)
`[getSource](../classes/mdkernel/DirectedRelationship.html#getSource()), [getTarget](../classes/mdkernel/DirectedRelationship.html#getTarget()), [hasSource](../classes/mdkernel/DirectedRelationship.html#hasSource()), [hasTarget](../classes/mdkernel/DirectedRelationship.html#hasTarget())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Relationship](../classes/mdkernel/Relationship.html)
`[get_abstraction](../classes/mdkernel/Relationship.html#get_abstraction()), [getRelatedElement](../classes/mdkernel/Relationship.html#getRelatedElement()), [has_abstraction](../classes/mdkernel/Relationship.html#has_abstraction()), [hasRelatedElement](../classes/mdkernel/Relationship.html#hasRelatedElement())`

============ METHOD DETAIL ========== 
Method Details
getAppliedProfile
@CheckForNull[Profile](Profile.html) getAppliedProfile()
Returns the value of the '***Applied Profile***' reference.
 It is bidirectional and its opposite is
 '[`*profile Application Of Applied Profile*`](Profile.html#get_profileApplicationOfAppliedProfile())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Profiles that are applied to a Package through this ProfileApplication.
 end-model-doc
Returns:
the value of the '*Applied Profile*' reference.
See Also:
[`setAppliedProfile(Profile)`](#setAppliedProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))
[`UMLPackage.getProfileApplication_AppliedProfile()`](../metadata/UMLPackage.html#getProfileApplication_AppliedProfile())
[`Profile.get_profileApplicationOfAppliedProfile()`](Profile.html#get_profileApplicationOfAppliedProfile())
Model:
opposite="_profileApplicationOfAppliedProfile" required="true" ordered="false"
Generated:
setAppliedProfile
void setAppliedProfile(@CheckForNull
 [Profile](Profile.html) value)
Sets the value of the '[`*Applied Profile*`](#getAppliedProfile())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Applied Profile*' reference.
See Also:
[`getAppliedProfile()`](#getAppliedProfile())
Generated:
isStrict
boolean isStrict()
Returns the value of the '***Strict***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies that the Profile filtering rules for the metaclasses of the referenced metamodel shall be strictly applied.
 end-model-doc
Returns:
the value of the '*Strict*' attribute.
See Also:
[`setStrict(boolean)`](#setStrict(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProfileApplication_Strict()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setStrict
void setStrict(boolean value)
Sets the value of the '[`*Strict*`](#isStrict())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Strict*' attribute.
See Also:
[`isStrict()`](#isStrict())
Generated:
getApplyingPackage
@CheckForNull[Package](../classes/mdkernel/Package.html) getApplyingPackage()
Returns the value of the '***Applying Package***' container reference.
 It is bidirectional and its opposite is '[`*Profile Application*`](../classes/mdkernel/Package.html#getProfileApplication())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The package that owns the profile application.
 end-model-doc
Returns:
the value of the '*Applying Package*' container reference.
See Also:
[`setApplyingPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)`](#setApplyingPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))
[`UMLPackage.getProfileApplication_ApplyingPackage()`](../metadata/UMLPackage.html#getProfileApplication_ApplyingPackage())
[`Package.getProfileApplication()`](../classes/mdkernel/Package.html#getProfileApplication())
Model:
opposite="profileApplication" required="true" transient="false" ordered="false"
Generated:
setApplyingPackage
void setApplyingPackage(@CheckForNull
 [Package](../classes/mdkernel/Package.html) value)
Sets the value of the '[`*Applying Package*`](#getApplyingPackage())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Applying Package*' container reference.
See Also:
[`getApplyingPackage()`](#getApplyingPackage())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.mdprofiles</a></div>
<h1 class="title" title="Interface ProfileApplication">Interface ProfileApplication</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></code>, <code><a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ProfileApplication</span><span class="extends-implements">
extends <a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Profile Application</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A profile application is used to show which profiles have been applied to a package.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getAppliedProfile()"><code><em>Applied Profile</em></code></a></li>
<li><a href="#isStrict()"><code><em>Strict</em></code></a></li>
<li><a href="#getApplyingPackage()"><code><em>Applying Package</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../metadata/UMLPackage.html#getProfileApplication()"><code>UMLPackage.getProfileApplication()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAppliedProfile()">getAppliedProfile</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Applied Profile</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getApplyingPackage()">getApplyingPackage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Applying Package</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isStrict()">isStrict</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Strict</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAppliedProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">setAppliedProfile</a><wbr/>(<a href="Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getAppliedProfile()"><code><em>Applied Profile</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setApplyingPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setApplyingPackage</a><wbr/>(<a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getApplyingPackage()"><code><em>Applying Package</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setStrict(boolean)">setStrict</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isStrict()"><code><em>Strict</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#atInsert()">atInsert</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a>, <a href="../../../../magicdraw/uml/BaseElement.html#clone()">clone</a>, <a href="../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a>, <a href="../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></h3>
<code><a href="../classes/mdkernel/DirectedRelationship.html#getSource()">getSource</a>, <a href="../classes/mdkernel/DirectedRelationship.html#getTarget()">getTarget</a>, <a href="../classes/mdkernel/DirectedRelationship.html#hasSource()">hasSource</a>, <a href="../classes/mdkernel/DirectedRelationship.html#hasTarget()">hasTarget</a></code></div>
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
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
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
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></h3>
<code><a href="../classes/mdkernel/Relationship.html#get_abstraction()">get_abstraction</a>, <a href="../classes/mdkernel/Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="../classes/mdkernel/Relationship.html#has_abstraction()">has_abstraction</a>, <a href="../classes/mdkernel/Relationship.html#hasRelatedElement()">hasRelatedElement</a></code></div>
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
<section class="detail" id="getAppliedProfile()">
<h3>getAppliedProfile</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">getAppliedProfile</span>()</div>
<div class="block">Returns the value of the '<em><b>Applied Profile</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="Profile.html#get_profileApplicationOfAppliedProfile()"><code><em>profile Application Of Applied Profile</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Profiles that are applied to a Package through this ProfileApplication.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Applied Profile</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setAppliedProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)"><code>setAppliedProfile(Profile)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getProfileApplication_AppliedProfile()"><code>UMLPackage.getProfileApplication_AppliedProfile()</code></a></li>
<li><a href="Profile.html#get_profileApplicationOfAppliedProfile()"><code>Profile.get_profileApplicationOfAppliedProfile()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_profileApplicationOfAppliedProfile" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAppliedProfile(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>setAppliedProfile</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAppliedProfile</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getAppliedProfile()"><code><em>Applied Profile</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Applied Profile</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getAppliedProfile()"><code>getAppliedProfile()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStrict()">
<h3>isStrict</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isStrict</span>()</div>
<div class="block">Returns the value of the '<em><b>Strict</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies that the Profile filtering rules for the metaclasses of the referenced metamodel shall be strictly applied.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Strict</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setStrict(boolean)"><code>setStrict(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getProfileApplication_Strict()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStrict(boolean)">
<h3>setStrict</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setStrict</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isStrict()"><code><em>Strict</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Strict</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isStrict()"><code>isStrict()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApplyingPackage()">
<h3>getApplyingPackage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getApplyingPackage</span>()</div>
<div class="block">Returns the value of the '<em><b>Applying Package</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../classes/mdkernel/Package.html#getProfileApplication()"><code><em>Profile Application</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The package that owns the profile application.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Applying Package</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setApplyingPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)"><code>setApplyingPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getProfileApplication_ApplyingPackage()"><code>UMLPackage.getProfileApplication_ApplyingPackage()</code></a></li>
<li><a href="../classes/mdkernel/Package.html#getProfileApplication()"><code>Package.getProfileApplication()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="profileApplication" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplyingPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>setApplyingPackage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setApplyingPackage</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getApplyingPackage()"><code><em>Applying Package</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Applying Package</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getApplyingPackage()"><code>getApplyingPackage()</code></a></li>
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
