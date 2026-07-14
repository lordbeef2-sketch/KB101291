# JAVA OPENAPI: MDFoundationPackage (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/foundation/MDFoundationPackage.html
- source_path: `com/nomagic/magicdraw/foundation/MDFoundationPackage.html`
- source_sha256: `fbc257ec262bc87f013655d2c57e9c10a86d938b05494d97de8d86438e5712c0`
- captured_utc: `2026-07-14T16:51:22.154215+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation](package-summary.html)

## Interface MDFoundationPackage

All Superinterfaces:
`org.eclipse.emf.ecore.EModelElement`, `org.eclipse.emf.ecore.ENamedElement`, `org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.ecore.EPackage`, `org.eclipse.emf.common.notify.Notifier`

public interfaceMDFoundationPackageextends org.eclipse.emf.ecore.EPackage

begin-user-doc 
 The **Package** for the model.
 It contains accessors for the meta objects to represent
 each class,
each feature of each class,
each enum,
and each data type
 end-user-doc

See Also:
[`MDFoundationFactory`](MDFoundationFactory.html)
Model:
kind="package"
Generated:

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static interface`
`[MDFoundationPackage.Literals](MDFoundationPackage.Literals.html)`
Defines literals for the meta objects that represent
 
 each class,
 each feature of each class,
 each enum,
 and each data type
 
 end-user-doc
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [MDFoundationPackage](MDFoundationPackage.html)`
`[eINSTANCE](#eINSTANCE)`
The singleton instance of the package.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[eNAME](#eNAME)`
The package name.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[eNS_PREFIX](#eNS_PREFIX)`
The package namespace name.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[eNS_URI](#eNS_URI)`
The package namespace URI.
`static final int`
`[MD_EXTENSION](#MD_EXTENSION)`
The meta object id for the '`*MD Extension*`' class.
`static final int`
`[MD_EXTENSION__CONTENTS](#MD_EXTENSION__CONTENTS)`
The feature id for the '***Contents***' containment reference list.
`static final int`
`[MD_EXTENSION__DETAILS](#MD_EXTENSION__DETAILS)`
The feature id for the '***Details***' map.
`static final int`
`[MD_EXTENSION__ELEMENT](#MD_EXTENSION__ELEMENT)`
The feature id for the '***Element***' container reference.
`static final int`
`[MD_EXTENSION__REFERENCES](#MD_EXTENSION__REFERENCES)`
The feature id for the '***References***' reference list.
`static final int`
`[MD_EXTENSION__SOURCE](#MD_EXTENSION__SOURCE)`
The feature id for the '***Source***' attribute.
`static final int`
`[MD_EXTENSION_FEATURE_COUNT](#MD_EXTENSION_FEATURE_COUNT)`
The number of structural features of the '*MD Extension*' class.
`static final int`
`[MD_OBJECT](#MD_OBJECT)`
The meta object id for the '`*MD Object*`' class.
`static final int`
`[MD_OBJECT__ID](#MD_OBJECT__ID)`
The feature id for the '***ID***' attribute.
`static final int`
`[MD_OBJECT__MD_EXTENSIONS](#MD_OBJECT__MD_EXTENSIONS)`
The feature id for the '***Md Extensions***' containment reference list.
`static final int`
`[MD_OBJECT_FEATURE_COUNT](#MD_OBJECT_FEATURE_COUNT)`
The number of structural features of the '*MD Object*' class.
`static final int`
`[STRING_TO_STRING_MAP_ENTRY](#STRING_TO_STRING_MAP_ENTRY)`
The meta object id for the '`*String To String Map Entry*`' class.
`static final int`
`[STRING_TO_STRING_MAP_ENTRY__KEY](#STRING_TO_STRING_MAP_ENTRY__KEY)`
The feature id for the '***Key***' attribute.
`static final int`
`[STRING_TO_STRING_MAP_ENTRY__VALUE](#STRING_TO_STRING_MAP_ENTRY__VALUE)`
The feature id for the '***Value***' attribute.
`static final int`
`[STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT](#STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT)`
The number of structural features of the '*String To String Map Entry*' class.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf.ecore.EClass`
`[getMDExtension](#getMDExtension())()`
Returns the meta object for class '[`*MD Extension*`](MDExtension.html)'.
`org.eclipse.emf.ecore.EReference`
`[getMDExtension_Contents](#getMDExtension_Contents())()`
Returns the meta object for the containment reference list '[`*Contents*`](MDExtension.html#getContents())'.
`org.eclipse.emf.ecore.EReference`
`[getMDExtension_Details](#getMDExtension_Details())()`
Returns the meta object for the map '[`*Details*`](MDExtension.html#getDetails())'.
`org.eclipse.emf.ecore.EReference`
`[getMDExtension_Element](#getMDExtension_Element())()`
Returns the meta object for the container reference '[`*Element*`](MDExtension.html#getElement())'.
`org.eclipse.emf.ecore.EReference`
`[getMDExtension_References](#getMDExtension_References())()`
Returns the meta object for the reference list '[`*References*`](MDExtension.html#getReferences())'.
`org.eclipse.emf.ecore.EAttribute`
`[getMDExtension_Source](#getMDExtension_Source())()`
Returns the meta object for the attribute '[`*Source*`](MDExtension.html#getSource())'.
`[MDFoundationFactory](MDFoundationFactory.html)`
`[getMDFoundationFactory](#getMDFoundationFactory())()`
Returns the factory that creates the instances of the model.
`org.eclipse.emf.ecore.EClass`
`[getMDObject](#getMDObject())()`
Returns the meta object for class '[`*MD Object*`](MDObject.html)'.
`org.eclipse.emf.ecore.EAttribute`
`[getMDObject_ID](#getMDObject_ID())()`
Returns the meta object for the attribute '[`*ID*`](MDObject.html#getID())'.
`org.eclipse.emf.ecore.EReference`
`[getMDObject_MdExtensions](#getMDObject_MdExtensions())()`
Returns the meta object for the containment reference list '[`*Md Extensions*`](MDObject.html#getMdExtensions())'.
`org.eclipse.emf.ecore.EClass`
`[getStringToStringMapEntry](#getStringToStringMapEntry())()`
Returns the meta object for class '[`*String To String Map Entry*`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)'.
`org.eclipse.emf.ecore.EAttribute`
`[getStringToStringMapEntry_Key](#getStringToStringMapEntry_Key())()`
Returns the meta object for the attribute '[`*Key*`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)'.
`org.eclipse.emf.ecore.EAttribute`
`[getStringToStringMapEntry_Value](#getStringToStringMapEntry_Value())()`
Returns the meta object for the attribute '[`*Value*`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)'.
Methods inherited from interface org.eclipse.emf.ecore.EModelElement
`getEAnnotation, getEAnnotations`
Methods inherited from interface org.eclipse.emf.ecore.ENamedElement
`getName, setName`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface org.eclipse.emf.ecore.EPackage
`getEClassifier, getEClassifiers, getEFactoryInstance, getESubpackages, getESuperPackage, getNsPrefix, getNsURI, setEFactoryInstance, setNsPrefix, setNsURI`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ FIELD DETAIL =========== 
Field Details
eNAME
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) eNAME
The package name.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.eNAME)
Generated:
eNS_URI
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) eNS_URI
The package namespace URI.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.eNS_URI)
Generated:
eNS_PREFIX
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) eNS_PREFIX
The package namespace name.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.eNS_PREFIX)
Generated:
eINSTANCE
static final [MDFoundationPackage](MDFoundationPackage.html) eINSTANCE
The singleton instance of the package.
 begin-user-doc 
 end-user-doc
Generated:
MD_OBJECT
static final int MD_OBJECT
The meta object id for the '`*MD Object*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`MDObjectImpl`
`MDFoundationPackageImpl.getMDObject()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT)
Generated:
MD_OBJECT__ID
static final int MD_OBJECT__ID
The feature id for the '***ID***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT__ID)
Generated:
MD_OBJECT__MD_EXTENSIONS
static final int MD_OBJECT__MD_EXTENSIONS
The feature id for the '***Md Extensions***' containment reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT__MD_EXTENSIONS)
Generated:
MD_OBJECT_FEATURE_COUNT
static final int MD_OBJECT_FEATURE_COUNT
The number of structural features of the '*MD Object*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT_FEATURE_COUNT)
Generated:
MD_EXTENSION
static final int MD_EXTENSION
The meta object id for the '`*MD Extension*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`MDExtensionImpl`
`MDFoundationPackageImpl.getMDExtension()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION)
Generated:
MD_EXTENSION__SOURCE
static final int MD_EXTENSION__SOURCE
The feature id for the '***Source***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__SOURCE)
Generated:
MD_EXTENSION__CONTENTS
static final int MD_EXTENSION__CONTENTS
The feature id for the '***Contents***' containment reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__CONTENTS)
Generated:
MD_EXTENSION__REFERENCES
static final int MD_EXTENSION__REFERENCES
The feature id for the '***References***' reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__REFERENCES)
Generated:
MD_EXTENSION__ELEMENT
static final int MD_EXTENSION__ELEMENT
The feature id for the '***Element***' container reference.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__ELEMENT)
Generated:
MD_EXTENSION__DETAILS
static final int MD_EXTENSION__DETAILS
The feature id for the '***Details***' map.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__DETAILS)
Generated:
MD_EXTENSION_FEATURE_COUNT
static final int MD_EXTENSION_FEATURE_COUNT
The number of structural features of the '*MD Extension*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION_FEATURE_COUNT)
Generated:
STRING_TO_STRING_MAP_ENTRY
static final int STRING_TO_STRING_MAP_ENTRY
The meta object id for the '`*String To String Map Entry*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`StringToStringMapEntryImpl`
`MDFoundationPackageImpl.getStringToStringMapEntry()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY)
Generated:
STRING_TO_STRING_MAP_ENTRY__KEY
static final int STRING_TO_STRING_MAP_ENTRY__KEY
The feature id for the '***Key***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY__KEY)
Generated:
STRING_TO_STRING_MAP_ENTRY__VALUE
static final int STRING_TO_STRING_MAP_ENTRY__VALUE
The feature id for the '***Value***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY__VALUE)
Generated:
STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT
static final int STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT
The number of structural features of the '*String To String Map Entry*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT)
Generated:
 ============ METHOD DETAIL ========== 
Method Details
getMDObject
org.eclipse.emf.ecore.EClass getMDObject()
Returns the meta object for class '[`*MD Object*`](MDObject.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*MD Object*'.
See Also:
[`MDObject`](MDObject.html)
Generated:
getMDObject_ID
org.eclipse.emf.ecore.EAttribute getMDObject_ID()
Returns the meta object for the attribute '[`*ID*`](MDObject.html#getID())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*ID*'.
See Also:
[`MDObject.getID()`](MDObject.html#getID())
[`getMDObject()`](#getMDObject())
Generated:
getMDObject_MdExtensions
org.eclipse.emf.ecore.EReference getMDObject_MdExtensions()
Returns the meta object for the containment reference list '[`*Md Extensions*`](MDObject.html#getMdExtensions())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the containment reference list '*Md Extensions*'.
See Also:
[`MDObject.getMdExtensions()`](MDObject.html#getMdExtensions())
[`getMDObject()`](#getMDObject())
Generated:
getMDExtension
org.eclipse.emf.ecore.EClass getMDExtension()
Returns the meta object for class '[`*MD Extension*`](MDExtension.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*MD Extension*'.
See Also:
[`MDExtension`](MDExtension.html)
Generated:
getMDExtension_Source
org.eclipse.emf.ecore.EAttribute getMDExtension_Source()
Returns the meta object for the attribute '[`*Source*`](MDExtension.html#getSource())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Source*'.
See Also:
[`MDExtension.getSource()`](MDExtension.html#getSource())
[`getMDExtension()`](#getMDExtension())
Generated:
getMDExtension_Contents
org.eclipse.emf.ecore.EReference getMDExtension_Contents()
Returns the meta object for the containment reference list '[`*Contents*`](MDExtension.html#getContents())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the containment reference list '*Contents*'.
See Also:
[`MDExtension.getContents()`](MDExtension.html#getContents())
[`getMDExtension()`](#getMDExtension())
Generated:
getMDExtension_References
org.eclipse.emf.ecore.EReference getMDExtension_References()
Returns the meta object for the reference list '[`*References*`](MDExtension.html#getReferences())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the reference list '*References*'.
See Also:
[`MDExtension.getReferences()`](MDExtension.html#getReferences())
[`getMDExtension()`](#getMDExtension())
Generated:
getMDExtension_Element
org.eclipse.emf.ecore.EReference getMDExtension_Element()
Returns the meta object for the container reference '[`*Element*`](MDExtension.html#getElement())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the container reference '*Element*'.
See Also:
[`MDExtension.getElement()`](MDExtension.html#getElement())
[`getMDExtension()`](#getMDExtension())
Generated:
getMDExtension_Details
org.eclipse.emf.ecore.EReference getMDExtension_Details()
Returns the meta object for the map '[`*Details*`](MDExtension.html#getDetails())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the map '*Details*'.
See Also:
[`MDExtension.getDetails()`](MDExtension.html#getDetails())
[`getMDExtension()`](#getMDExtension())
Generated:
getStringToStringMapEntry
org.eclipse.emf.ecore.EClass getStringToStringMapEntry()
Returns the meta object for class '[`*String To String Map Entry*`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*String To String Map Entry*'.
See Also:
[`Map.Entry`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)
Model:
keyDataType="org.eclipse.emf.ecore.EString"
 valueDataType="org.eclipse.emf.ecore.EString"
Generated:
getStringToStringMapEntry_Key
org.eclipse.emf.ecore.EAttribute getStringToStringMapEntry_Key()
Returns the meta object for the attribute '[`*Key*`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Key*'.
See Also:
[`Map.Entry`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)
[`getStringToStringMapEntry()`](#getStringToStringMapEntry())
Generated:
getStringToStringMapEntry_Value
org.eclipse.emf.ecore.EAttribute getStringToStringMapEntry_Value()
Returns the meta object for the attribute '[`*Value*`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Value*'.
See Also:
[`Map.Entry`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html)
[`getStringToStringMapEntry()`](#getStringToStringMapEntry())
Generated:
getMDFoundationFactory
[MDFoundationFactory](MDFoundationFactory.html) getMDFoundationFactory()
Returns the factory that creates the instances of the model.
 begin-user-doc 
 end-user-doc
Returns:
the factory that creates the instances of the model.
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation</a></div>
<h1 class="title" title="Interface MDFoundationPackage">Interface MDFoundationPackage</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EModelElement</code>, <code>org.eclipse.emf.ecore.ENamedElement</code>, <code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.ecore.EPackage</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MDFoundationPackage</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EPackage</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Package</b> for the model.
 It contains accessors for the meta objects to represent
 <ul>
<li>each class,</li>
<li>each feature of each class,</li>
<li>each enum,</li>
<li>and each data type</li>
</ul>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDFoundationFactory.html" title="interface in com.nomagic.magicdraw.foundation"><code>MDFoundationFactory</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>kind="package"</dd>
<dt>Generated:</dt>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MDFoundationPackage.Literals.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationPackage.Literals</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines literals for the meta objects that represent
 
   each class,
   each feature of each class,
   each enum,
   and each data type
 
 <!-- end-user-doc --></div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a href="MDFoundationPackage.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationPackage</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eINSTANCE">eINSTANCE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The singleton instance of the package.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#eNAME">eNAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The package name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eNS_PREFIX">eNS_PREFIX</a></code></div>
<div class="col-last even-row-color">
<div class="block">The package namespace name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#eNS_URI">eNS_URI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The package namespace URI.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_EXTENSION">MD_EXTENSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<code><em>MD Extension</em></code>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MD_EXTENSION__CONTENTS">MD_EXTENSION__CONTENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Contents</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_EXTENSION__DETAILS">MD_EXTENSION__DETAILS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Details</b></em>' map.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MD_EXTENSION__ELEMENT">MD_EXTENSION__ELEMENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Element</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_EXTENSION__REFERENCES">MD_EXTENSION__REFERENCES</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>References</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MD_EXTENSION__SOURCE">MD_EXTENSION__SOURCE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Source</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_EXTENSION_FEATURE_COUNT">MD_EXTENSION_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>MD Extension</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MD_OBJECT">MD_OBJECT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<code><em>MD Object</em></code>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_OBJECT__ID">MD_OBJECT__ID</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>ID</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MD_OBJECT__MD_EXTENSIONS">MD_OBJECT__MD_EXTENSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Md Extensions</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_OBJECT_FEATURE_COUNT">MD_OBJECT_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>MD Object</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STRING_TO_STRING_MAP_ENTRY">STRING_TO_STRING_MAP_ENTRY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<code><em>String To String Map Entry</em></code>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STRING_TO_STRING_MAP_ENTRY__KEY">STRING_TO_STRING_MAP_ENTRY__KEY</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Key</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STRING_TO_STRING_MAP_ENTRY__VALUE">STRING_TO_STRING_MAP_ENTRY__VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Value</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT">STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>String To String Map Entry</em>' class.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDExtension()">getMDExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="MDExtension.html" title="interface in com.nomagic.magicdraw.foundation"><code><em>MD Extension</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDExtension_Contents()">getMDExtension_Contents</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the containment reference list '<a href="MDExtension.html#getContents()"><code><em>Contents</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDExtension_Details()">getMDExtension_Details</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the map '<a href="MDExtension.html#getDetails()"><code><em>Details</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDExtension_Element()">getMDExtension_Element</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the container reference '<a href="MDExtension.html#getElement()"><code><em>Element</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDExtension_References()">getMDExtension_References</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the reference list '<a href="MDExtension.html#getReferences()"><code><em>References</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDExtension_Source()">getMDExtension_Source</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="MDExtension.html#getSource()"><code><em>Source</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MDFoundationFactory.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationFactory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDFoundationFactory()">getMDFoundationFactory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the factory that creates the instances of the model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDObject()">getMDObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="MDObject.html" title="interface in com.nomagic.magicdraw.foundation"><code><em>MD Object</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDObject_ID()">getMDObject_ID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="MDObject.html#getID()"><code><em>ID</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDObject_MdExtensions()">getMDObject_MdExtensions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the containment reference list '<a href="MDObject.html#getMdExtensions()"><code><em>Md Extensions</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStringToStringMapEntry()">getStringToStringMapEntry</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>String To String Map Entry</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStringToStringMapEntry_Key()">getStringToStringMapEntry_Key</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Key</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStringToStringMapEntry_Value()">getStringToStringMapEntry_Value</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Value</em></code></a>'.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EModelElement">Methods inherited from interface org.eclipse.emf.ecore.EModelElement</h3>
<code>getEAnnotation, getEAnnotations</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.ENamedElement">Methods inherited from interface org.eclipse.emf.ecore.ENamedElement</h3>
<code>getName, setName</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EPackage">Methods inherited from interface org.eclipse.emf.ecore.EPackage</h3>
<code>getEClassifier, getEClassifiers, getEFactoryInstance, getESubpackages, getESuperPackage, getNsPrefix, getNsURI, setEFactoryInstance, setNsPrefix, setNsURI</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="eNAME">
<h3>eNAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNAME</span></div>
<div class="block">The package name.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.eNAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eNS_URI">
<h3>eNS_URI</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNS_URI</span></div>
<div class="block">The package namespace URI.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.eNS_URI">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eNS_PREFIX">
<h3>eNS_PREFIX</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNS_PREFIX</span></div>
<div class="block">The package namespace name.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.eNS_PREFIX">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eINSTANCE">
<h3>eINSTANCE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a href="MDFoundationPackage.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationPackage</a></span> <span class="element-name">eINSTANCE</span></div>
<div class="block">The singleton instance of the package.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_OBJECT">
<h3>MD_OBJECT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_OBJECT</span></div>
<div class="block">The meta object id for the '<code><em>MD Object</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>MDObjectImpl</code></li>
<li><code>MDFoundationPackageImpl.getMDObject()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_OBJECT__ID">
<h3>MD_OBJECT__ID</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_OBJECT__ID</span></div>
<div class="block">The feature id for the '<em><b>ID</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT__ID">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_OBJECT__MD_EXTENSIONS">
<h3>MD_OBJECT__MD_EXTENSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_OBJECT__MD_EXTENSIONS</span></div>
<div class="block">The feature id for the '<em><b>Md Extensions</b></em>' containment reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT__MD_EXTENSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_OBJECT_FEATURE_COUNT">
<h3>MD_OBJECT_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_OBJECT_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>MD Object</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_OBJECT_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_EXTENSION">
<h3>MD_EXTENSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_EXTENSION</span></div>
<div class="block">The meta object id for the '<code><em>MD Extension</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>MDExtensionImpl</code></li>
<li><code>MDFoundationPackageImpl.getMDExtension()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_EXTENSION__SOURCE">
<h3>MD_EXTENSION__SOURCE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_EXTENSION__SOURCE</span></div>
<div class="block">The feature id for the '<em><b>Source</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__SOURCE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_EXTENSION__CONTENTS">
<h3>MD_EXTENSION__CONTENTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_EXTENSION__CONTENTS</span></div>
<div class="block">The feature id for the '<em><b>Contents</b></em>' containment reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__CONTENTS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_EXTENSION__REFERENCES">
<h3>MD_EXTENSION__REFERENCES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_EXTENSION__REFERENCES</span></div>
<div class="block">The feature id for the '<em><b>References</b></em>' reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__REFERENCES">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_EXTENSION__ELEMENT">
<h3>MD_EXTENSION__ELEMENT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_EXTENSION__ELEMENT</span></div>
<div class="block">The feature id for the '<em><b>Element</b></em>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__ELEMENT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_EXTENSION__DETAILS">
<h3>MD_EXTENSION__DETAILS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_EXTENSION__DETAILS</span></div>
<div class="block">The feature id for the '<em><b>Details</b></em>' map.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION__DETAILS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_EXTENSION_FEATURE_COUNT">
<h3>MD_EXTENSION_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MD_EXTENSION_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>MD Extension</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.MD_EXTENSION_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_STRING_MAP_ENTRY">
<h3>STRING_TO_STRING_MAP_ENTRY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_STRING_MAP_ENTRY</span></div>
<div class="block">The meta object id for the '<code><em>String To String Map Entry</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>StringToStringMapEntryImpl</code></li>
<li><code>MDFoundationPackageImpl.getStringToStringMapEntry()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_STRING_MAP_ENTRY__KEY">
<h3>STRING_TO_STRING_MAP_ENTRY__KEY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_STRING_MAP_ENTRY__KEY</span></div>
<div class="block">The feature id for the '<em><b>Key</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY__KEY">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_STRING_MAP_ENTRY__VALUE">
<h3>STRING_TO_STRING_MAP_ENTRY__VALUE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_STRING_MAP_ENTRY__VALUE</span></div>
<div class="block">The feature id for the '<em><b>Value</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY__VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT">
<h3>STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>String To String Map Entry</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.foundation.MDFoundationPackage.STRING_TO_STRING_MAP_ENTRY_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getMDObject()">
<h3>getMDObject</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getMDObject</span>()</div>
<div class="block">Returns the meta object for class '<a href="MDObject.html" title="interface in com.nomagic.magicdraw.foundation"><code><em>MD Object</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>MD Object</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDObject.html" title="interface in com.nomagic.magicdraw.foundation"><code>MDObject</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDObject_ID()">
<h3>getMDObject_ID</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getMDObject_ID</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="MDObject.html#getID()"><code><em>ID</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>ID</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDObject.html#getID()"><code>MDObject.getID()</code></a></li>
<li><a href="#getMDObject()"><code>getMDObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDObject_MdExtensions()">
<h3>getMDObject_MdExtensions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getMDObject_MdExtensions</span>()</div>
<div class="block">Returns the meta object for the containment reference list '<a href="MDObject.html#getMdExtensions()"><code><em>Md Extensions</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the containment reference list '<em>Md Extensions</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDObject.html#getMdExtensions()"><code>MDObject.getMdExtensions()</code></a></li>
<li><a href="#getMDObject()"><code>getMDObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDExtension()">
<h3>getMDExtension</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getMDExtension</span>()</div>
<div class="block">Returns the meta object for class '<a href="MDExtension.html" title="interface in com.nomagic.magicdraw.foundation"><code><em>MD Extension</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>MD Extension</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDExtension.html" title="interface in com.nomagic.magicdraw.foundation"><code>MDExtension</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDExtension_Source()">
<h3>getMDExtension_Source</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getMDExtension_Source</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="MDExtension.html#getSource()"><code><em>Source</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Source</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDExtension.html#getSource()"><code>MDExtension.getSource()</code></a></li>
<li><a href="#getMDExtension()"><code>getMDExtension()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDExtension_Contents()">
<h3>getMDExtension_Contents</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getMDExtension_Contents</span>()</div>
<div class="block">Returns the meta object for the containment reference list '<a href="MDExtension.html#getContents()"><code><em>Contents</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the containment reference list '<em>Contents</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDExtension.html#getContents()"><code>MDExtension.getContents()</code></a></li>
<li><a href="#getMDExtension()"><code>getMDExtension()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDExtension_References()">
<h3>getMDExtension_References</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getMDExtension_References</span>()</div>
<div class="block">Returns the meta object for the reference list '<a href="MDExtension.html#getReferences()"><code><em>References</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the reference list '<em>References</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDExtension.html#getReferences()"><code>MDExtension.getReferences()</code></a></li>
<li><a href="#getMDExtension()"><code>getMDExtension()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDExtension_Element()">
<h3>getMDExtension_Element</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getMDExtension_Element</span>()</div>
<div class="block">Returns the meta object for the container reference '<a href="MDExtension.html#getElement()"><code><em>Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the container reference '<em>Element</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDExtension.html#getElement()"><code>MDExtension.getElement()</code></a></li>
<li><a href="#getMDExtension()"><code>getMDExtension()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDExtension_Details()">
<h3>getMDExtension_Details</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getMDExtension_Details</span>()</div>
<div class="block">Returns the meta object for the map '<a href="MDExtension.html#getDetails()"><code><em>Details</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the map '<em>Details</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDExtension.html#getDetails()"><code>MDExtension.getDetails()</code></a></li>
<li><a href="#getMDExtension()"><code>getMDExtension()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringToStringMapEntry()">
<h3>getStringToStringMapEntry</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getStringToStringMapEntry</span>()</div>
<div class="block">Returns the meta object for class '<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>String To String Map Entry</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>String To String Map Entry</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code>Map.Entry</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>keyDataType="org.eclipse.emf.ecore.EString"
        valueDataType="org.eclipse.emf.ecore.EString"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringToStringMapEntry_Key()">
<h3>getStringToStringMapEntry_Key</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getStringToStringMapEntry_Key</span>()</div>
<div class="block">Returns the meta object for the attribute '<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Key</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Key</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code>Map.Entry</code></a></li>
<li><a href="#getStringToStringMapEntry()"><code>getStringToStringMapEntry()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringToStringMapEntry_Value()">
<h3>getStringToStringMapEntry_Value</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getStringToStringMapEntry_Value</span>()</div>
<div class="block">Returns the meta object for the attribute '<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Value</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code>Map.Entry</code></a></li>
<li><a href="#getStringToStringMapEntry()"><code>getStringToStringMapEntry()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDFoundationFactory()">
<h3>getMDFoundationFactory</h3>
<div class="member-signature"><span class="return-type"><a href="MDFoundationFactory.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationFactory</a></span> <span class="element-name">getMDFoundationFactory</span>()</div>
<div class="block">Returns the factory that creates the instances of the model.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the factory that creates the instances of the model.</dd>
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
