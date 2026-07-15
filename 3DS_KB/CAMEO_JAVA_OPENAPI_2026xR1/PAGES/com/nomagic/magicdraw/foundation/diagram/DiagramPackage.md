# JAVA OPENAPI: DiagramPackage (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/foundation/diagram/DiagramPackage.html
- source_path: `com/nomagic/magicdraw/foundation/diagram/DiagramPackage.html`
- source_sha256: `aff608d2a7cf27a1e671a35e9d3b7e8d06d99a061ac9c8862ed954e1598d0655`
- captured_utc: `2026-07-14T16:45:37.019494+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation.diagram](package-summary.html)

## Interface DiagramPackage

All Superinterfaces:
`org.eclipse.emf.ecore.EModelElement`, `org.eclipse.emf.ecore.ENamedElement`, `org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.ecore.EPackage`, `org.eclipse.emf.common.notify.Notifier`

public interfaceDiagramPackageextends org.eclipse.emf.ecore.EPackage

begin-user-doc 
 The **Package** for the model.
 It contains accessors for the meta objects to represent
 each class,
each feature of each class,
each enum,
and each data type
 end-user-doc

See Also:
[`DiagramFactory`](DiagramFactory.html)
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
`[DiagramPackage.Literals](DiagramPackage.Literals.html)`
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
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT)`
The meta object id for the '`*Abstract Diagram Representation Object*`' class.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS)`
The feature id for the '***Diagram Contents***' containment reference.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES)`
The feature id for the '***Diagram Properties***' attribute.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID)`
The feature id for the '***Diagram Style ID***' attribute.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID)`
The feature id for the '***ID***' attribute.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET)`
The feature id for the '***Initial Frame Size Set***' attribute.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE)`
The feature id for the '***Required Feature***' attribute.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE)`
The feature id for the '***Type***' attribute.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE)`
The feature id for the '***Uml Type***' attribute.
`static final int`
`[ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT](#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT)`
The number of structural features of the '*Abstract Diagram Representation Object*' class.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR](#DIAGRAM_CONTENTS_DESCRIPTOR)`
The meta object id for the '`*Contents Descriptor*`' class.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT](#DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT)`
The feature id for the '***Binary Object***' containment reference.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH](#DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH)`
The feature id for the '***Content Hash***' attribute.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME](#DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME)`
The feature id for the '***Exporter Name***' attribute.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION](#DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION)`
The feature id for the '***Exporter Version***' attribute.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION](#DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION)`
The feature id for the '***Representation***' container reference.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS](#DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS)`
The feature id for the '***Used Elements***' attribute list.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS](#DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS)`
The feature id for the '***Used Objects***' reference list.
`static final int`
`[DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT](#DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT)`
The number of structural features of the '*Contents Descriptor*' class.
`static final [DiagramPackage](DiagramPackage.html)`
`[eINSTANCE](#eINSTANCE)`
The singleton instance of the package.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[eNAME](#eNAME)`
The package name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[eNS_PREFIX](#eNS_PREFIX)`
The package namespace name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[eNS_URI](#eNS_URI)`
The package namespace URI.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf.ecore.EClass`
`[getAbstractDiagramRepresentationObject](#getAbstractDiagramRepresentationObject())()`
Returns the meta object for class '[`*Abstract Diagram Representation Object*`](AbstractDiagramRepresentationObject.html)'.
`org.eclipse.emf.ecore.EReference`
`[getAbstractDiagramRepresentationObject_DiagramContents](#getAbstractDiagramRepresentationObject_DiagramContents())()`
Returns the meta object for the containment reference '[`*Diagram Contents*`](AbstractDiagramRepresentationObject.html#getDiagramContents())'.
`org.eclipse.emf.ecore.EAttribute`
`[getAbstractDiagramRepresentationObject_DiagramProperties](#getAbstractDiagramRepresentationObject_DiagramProperties())()`
Returns the meta object for the attribute '[`*Diagram Properties*`](AbstractDiagramRepresentationObject.html#getDiagramProperties())'.
`org.eclipse.emf.ecore.EAttribute`
`[getAbstractDiagramRepresentationObject_DiagramStyleID](#getAbstractDiagramRepresentationObject_DiagramStyleID())()`
Returns the meta object for the attribute '[`*Diagram Style ID*`](AbstractDiagramRepresentationObject.html#getDiagramStyleID())'.
`org.eclipse.emf.ecore.EAttribute`
`[getAbstractDiagramRepresentationObject_ID](#getAbstractDiagramRepresentationObject_ID())()`
Returns the meta object for the attribute '[`*ID*`](AbstractDiagramRepresentationObject.html#getID())'.
`org.eclipse.emf.ecore.EAttribute`
`[getAbstractDiagramRepresentationObject_InitialFrameSizeSet](#getAbstractDiagramRepresentationObject_InitialFrameSizeSet())()`
Returns the meta object for the attribute '[`*Initial Frame Size Set*`](AbstractDiagramRepresentationObject.html#isInitialFrameSizeSet())'.
`org.eclipse.emf.ecore.EAttribute`
`[getAbstractDiagramRepresentationObject_RequiredFeature](#getAbstractDiagramRepresentationObject_RequiredFeature())()`
Returns the meta object for the attribute '[`*Required Feature*`](AbstractDiagramRepresentationObject.html#getRequiredFeature())'.
`org.eclipse.emf.ecore.EAttribute`
`[getAbstractDiagramRepresentationObject_Type](#getAbstractDiagramRepresentationObject_Type())()`
Returns the meta object for the attribute '[`*Type*`](AbstractDiagramRepresentationObject.html#getType())'.
`org.eclipse.emf.ecore.EAttribute`
`[getAbstractDiagramRepresentationObject_UmlType](#getAbstractDiagramRepresentationObject_UmlType())()`
Returns the meta object for the attribute '[`*Uml Type*`](AbstractDiagramRepresentationObject.html#getUmlType())'.
`org.eclipse.emf.ecore.EClass`
`[getDiagramContentsDescriptor](#getDiagramContentsDescriptor())()`
Returns the meta object for class '[`*Contents Descriptor*`](DiagramContentsDescriptor.html)'.
`org.eclipse.emf.ecore.EReference`
`[getDiagramContentsDescriptor_BinaryObject](#getDiagramContentsDescriptor_BinaryObject())()`
Returns the meta object for the containment reference '[`*Binary Object*`](DiagramContentsDescriptor.html#getBinaryObject())'.
`org.eclipse.emf.ecore.EAttribute`
`[getDiagramContentsDescriptor_ContentHash](#getDiagramContentsDescriptor_ContentHash())()`
Returns the meta object for the attribute '[`*Content Hash*`](DiagramContentsDescriptor.html#getContentHash())'.
`org.eclipse.emf.ecore.EAttribute`
`[getDiagramContentsDescriptor_ExporterName](#getDiagramContentsDescriptor_ExporterName())()`
Returns the meta object for the attribute '[`*Exporter Name*`](DiagramContentsDescriptor.html#getExporterName())'.
`org.eclipse.emf.ecore.EAttribute`
`[getDiagramContentsDescriptor_ExporterVersion](#getDiagramContentsDescriptor_ExporterVersion())()`
Returns the meta object for the attribute '[`*Exporter Version*`](DiagramContentsDescriptor.html#getExporterVersion())'.
`org.eclipse.emf.ecore.EReference`
`[getDiagramContentsDescriptor_Representation](#getDiagramContentsDescriptor_Representation())()`
Returns the meta object for the container reference '[`*Representation*`](DiagramContentsDescriptor.html#getRepresentation())'.
`org.eclipse.emf.ecore.EAttribute`
`[getDiagramContentsDescriptor_UsedElements](#getDiagramContentsDescriptor_UsedElements())()`
Returns the meta object for the attribute list '[`*Used Elements*`](DiagramContentsDescriptor.html#getUsedElements())'.
`org.eclipse.emf.ecore.EReference`
`[getDiagramContentsDescriptor_UsedObjects](#getDiagramContentsDescriptor_UsedObjects())()`
Returns the meta object for the reference list '[`*Used Objects*`](DiagramContentsDescriptor.html#getUsedObjects())'.
`[DiagramFactory](DiagramFactory.html)`
`[getDiagramFactory](#getDiagramFactory())()`
Returns the factory that creates the instances of the model.
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
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) eNAME
The package name.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.eNAME)
Generated:
eNS_URI
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) eNS_URI
The package namespace URI.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.eNS_URI)
Generated:
eNS_PREFIX
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) eNS_PREFIX
The package namespace name.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.eNS_PREFIX)
Generated:
eINSTANCE
static final [DiagramPackage](DiagramPackage.html) eINSTANCE
The singleton instance of the package.
 begin-user-doc 
 end-user-doc
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT
The meta object id for the '`*Abstract Diagram Representation Object*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`AbstractDiagramRepresentationObjectImpl`
`DiagramPackageImpl.getAbstractDiagramRepresentationObject()`
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID
The feature id for the '***ID***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE
The feature id for the '***Type***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE
The feature id for the '***Uml Type***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES
The feature id for the '***Diagram Properties***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET
The feature id for the '***Initial Frame Size Set***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE
The feature id for the '***Required Feature***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS
The feature id for the '***Diagram Contents***' containment reference.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID
The feature id for the '***Diagram Style ID***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID)
Generated:
ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT
static final int ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT
The number of structural features of the '*Abstract Diagram Representation Object*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR
static final int DIAGRAM_CONTENTS_DESCRIPTOR
The meta object id for the '`*Contents Descriptor*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`DiagramContentsDescriptorImpl`
`DiagramPackageImpl.getDiagramContentsDescriptor()`
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION
static final int DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION
The feature id for the '***Representation***' container reference.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME
static final int DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME
The feature id for the '***Exporter Name***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION
static final int DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION
The feature id for the '***Exporter Version***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS
static final int DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS
The feature id for the '***Used Elements***' attribute list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT
static final int DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT
The feature id for the '***Binary Object***' containment reference.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH
static final int DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH
The feature id for the '***Content Hash***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS
static final int DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS
The feature id for the '***Used Objects***' reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS)
Generated:
DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT
static final int DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT
The number of structural features of the '*Contents Descriptor*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT)
Generated:
 ============ METHOD DETAIL ========== 
Method Details
getAbstractDiagramRepresentationObject
org.eclipse.emf.ecore.EClass getAbstractDiagramRepresentationObject()
Returns the meta object for class '[`*Abstract Diagram Representation Object*`](AbstractDiagramRepresentationObject.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Abstract Diagram Representation Object*'.
See Also:
[`AbstractDiagramRepresentationObject`](AbstractDiagramRepresentationObject.html)
Generated:
getAbstractDiagramRepresentationObject_ID
org.eclipse.emf.ecore.EAttribute getAbstractDiagramRepresentationObject_ID()
Returns the meta object for the attribute '[`*ID*`](AbstractDiagramRepresentationObject.html#getID())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*ID*'.
See Also:
[`AbstractDiagramRepresentationObject.getID()`](AbstractDiagramRepresentationObject.html#getID())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getAbstractDiagramRepresentationObject_Type
org.eclipse.emf.ecore.EAttribute getAbstractDiagramRepresentationObject_Type()
Returns the meta object for the attribute '[`*Type*`](AbstractDiagramRepresentationObject.html#getType())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Type*'.
See Also:
[`AbstractDiagramRepresentationObject.getType()`](AbstractDiagramRepresentationObject.html#getType())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getAbstractDiagramRepresentationObject_UmlType
org.eclipse.emf.ecore.EAttribute getAbstractDiagramRepresentationObject_UmlType()
Returns the meta object for the attribute '[`*Uml Type*`](AbstractDiagramRepresentationObject.html#getUmlType())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Uml Type*'.
See Also:
[`AbstractDiagramRepresentationObject.getUmlType()`](AbstractDiagramRepresentationObject.html#getUmlType())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getAbstractDiagramRepresentationObject_DiagramProperties
org.eclipse.emf.ecore.EAttribute getAbstractDiagramRepresentationObject_DiagramProperties()
Returns the meta object for the attribute '[`*Diagram Properties*`](AbstractDiagramRepresentationObject.html#getDiagramProperties())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Diagram Properties*'.
See Also:
[`AbstractDiagramRepresentationObject.getDiagramProperties()`](AbstractDiagramRepresentationObject.html#getDiagramProperties())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getAbstractDiagramRepresentationObject_InitialFrameSizeSet
org.eclipse.emf.ecore.EAttribute getAbstractDiagramRepresentationObject_InitialFrameSizeSet()
Returns the meta object for the attribute '[`*Initial Frame Size Set*`](AbstractDiagramRepresentationObject.html#isInitialFrameSizeSet())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Initial Frame Size Set*'.
See Also:
[`AbstractDiagramRepresentationObject.isInitialFrameSizeSet()`](AbstractDiagramRepresentationObject.html#isInitialFrameSizeSet())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getAbstractDiagramRepresentationObject_RequiredFeature
org.eclipse.emf.ecore.EAttribute getAbstractDiagramRepresentationObject_RequiredFeature()
Returns the meta object for the attribute '[`*Required Feature*`](AbstractDiagramRepresentationObject.html#getRequiredFeature())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Required Feature*'.
See Also:
[`AbstractDiagramRepresentationObject.getRequiredFeature()`](AbstractDiagramRepresentationObject.html#getRequiredFeature())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getAbstractDiagramRepresentationObject_DiagramContents
org.eclipse.emf.ecore.EReference getAbstractDiagramRepresentationObject_DiagramContents()
Returns the meta object for the containment reference '[`*Diagram Contents*`](AbstractDiagramRepresentationObject.html#getDiagramContents())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the containment reference '*Diagram Contents*'.
See Also:
[`AbstractDiagramRepresentationObject.getDiagramContents()`](AbstractDiagramRepresentationObject.html#getDiagramContents())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getAbstractDiagramRepresentationObject_DiagramStyleID
org.eclipse.emf.ecore.EAttribute getAbstractDiagramRepresentationObject_DiagramStyleID()
Returns the meta object for the attribute '[`*Diagram Style ID*`](AbstractDiagramRepresentationObject.html#getDiagramStyleID())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Diagram Style ID*'.
See Also:
[`AbstractDiagramRepresentationObject.getDiagramStyleID()`](AbstractDiagramRepresentationObject.html#getDiagramStyleID())
[`getAbstractDiagramRepresentationObject()`](#getAbstractDiagramRepresentationObject())
Generated:
getDiagramContentsDescriptor
org.eclipse.emf.ecore.EClass getDiagramContentsDescriptor()
Returns the meta object for class '[`*Contents Descriptor*`](DiagramContentsDescriptor.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Contents Descriptor*'.
See Also:
[`DiagramContentsDescriptor`](DiagramContentsDescriptor.html)
Generated:
getDiagramContentsDescriptor_Representation
org.eclipse.emf.ecore.EReference getDiagramContentsDescriptor_Representation()
Returns the meta object for the container reference '[`*Representation*`](DiagramContentsDescriptor.html#getRepresentation())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the container reference '*Representation*'.
See Also:
[`DiagramContentsDescriptor.getRepresentation()`](DiagramContentsDescriptor.html#getRepresentation())
[`getDiagramContentsDescriptor()`](#getDiagramContentsDescriptor())
Generated:
getDiagramContentsDescriptor_ExporterName
org.eclipse.emf.ecore.EAttribute getDiagramContentsDescriptor_ExporterName()
Returns the meta object for the attribute '[`*Exporter Name*`](DiagramContentsDescriptor.html#getExporterName())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Exporter Name*'.
See Also:
[`DiagramContentsDescriptor.getExporterName()`](DiagramContentsDescriptor.html#getExporterName())
[`getDiagramContentsDescriptor()`](#getDiagramContentsDescriptor())
Generated:
getDiagramContentsDescriptor_ExporterVersion
org.eclipse.emf.ecore.EAttribute getDiagramContentsDescriptor_ExporterVersion()
Returns the meta object for the attribute '[`*Exporter Version*`](DiagramContentsDescriptor.html#getExporterVersion())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Exporter Version*'.
See Also:
[`DiagramContentsDescriptor.getExporterVersion()`](DiagramContentsDescriptor.html#getExporterVersion())
[`getDiagramContentsDescriptor()`](#getDiagramContentsDescriptor())
Generated:
getDiagramContentsDescriptor_UsedElements
org.eclipse.emf.ecore.EAttribute getDiagramContentsDescriptor_UsedElements()
Returns the meta object for the attribute list '[`*Used Elements*`](DiagramContentsDescriptor.html#getUsedElements())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute list '*Used Elements*'.
See Also:
[`DiagramContentsDescriptor.getUsedElements()`](DiagramContentsDescriptor.html#getUsedElements())
[`getDiagramContentsDescriptor()`](#getDiagramContentsDescriptor())
Generated:
getDiagramContentsDescriptor_BinaryObject
org.eclipse.emf.ecore.EReference getDiagramContentsDescriptor_BinaryObject()
Returns the meta object for the containment reference '[`*Binary Object*`](DiagramContentsDescriptor.html#getBinaryObject())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the containment reference '*Binary Object*'.
See Also:
[`DiagramContentsDescriptor.getBinaryObject()`](DiagramContentsDescriptor.html#getBinaryObject())
[`getDiagramContentsDescriptor()`](#getDiagramContentsDescriptor())
Generated:
getDiagramContentsDescriptor_ContentHash
org.eclipse.emf.ecore.EAttribute getDiagramContentsDescriptor_ContentHash()
Returns the meta object for the attribute '[`*Content Hash*`](DiagramContentsDescriptor.html#getContentHash())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Content Hash*'.
See Also:
[`DiagramContentsDescriptor.getContentHash()`](DiagramContentsDescriptor.html#getContentHash())
[`getDiagramContentsDescriptor()`](#getDiagramContentsDescriptor())
Generated:
getDiagramContentsDescriptor_UsedObjects
org.eclipse.emf.ecore.EReference getDiagramContentsDescriptor_UsedObjects()
Returns the meta object for the reference list '[`*Used Objects*`](DiagramContentsDescriptor.html#getUsedObjects())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the reference list '*Used Objects*'.
See Also:
[`DiagramContentsDescriptor.getUsedObjects()`](DiagramContentsDescriptor.html#getUsedObjects())
[`getDiagramContentsDescriptor()`](#getDiagramContentsDescriptor())
Generated:
getDiagramFactory
[DiagramFactory](DiagramFactory.html) getDiagramFactory()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation.diagram</a></div>
<h1 class="title" title="Interface DiagramPackage">Interface DiagramPackage</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EModelElement</code>, <code>org.eclipse.emf.ecore.ENamedElement</code>, <code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.ecore.EPackage</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramPackage</span><span class="extends-implements">
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
<ul class="tag-list">
<li><a href="DiagramFactory.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code>DiagramFactory</code></a></li>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="DiagramPackage.Literals.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramPackage.Literals</a></code></div>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<code><em>Abstract Diagram Representation Object</em></code>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Diagram Contents</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Diagram Properties</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Diagram Style ID</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>ID</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Initial Frame Size Set</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Required Feature</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Type</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Uml Type</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of structural features of the '<em>Abstract Diagram Representation Object</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR">DIAGRAM_CONTENTS_DESCRIPTOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<code><em>Contents Descriptor</em></code>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT">DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Binary Object</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH">DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Content Hash</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME">DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Exporter Name</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION">DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Exporter Version</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION">DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Representation</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS">DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Used Elements</b></em>' attribute list.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS">DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Used Objects</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT">DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>Contents Descriptor</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramPackage</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#eINSTANCE">eINSTANCE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The singleton instance of the package.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eNAME">eNAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">The package name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#eNS_PREFIX">eNS_PREFIX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The package namespace name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eNS_URI">eNS_URI</a></code></div>
<div class="col-last even-row-color">
<div class="block">The package namespace URI.</div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject()">getAbstractDiagramRepresentationObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Abstract Diagram Representation Object</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_DiagramContents()">getAbstractDiagramRepresentationObject_DiagramContents</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the containment reference '<a href="AbstractDiagramRepresentationObject.html#getDiagramContents()"><code><em>Diagram Contents</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_DiagramProperties()">getAbstractDiagramRepresentationObject_DiagramProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getDiagramProperties()"><code><em>Diagram Properties</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_DiagramStyleID()">getAbstractDiagramRepresentationObject_DiagramStyleID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getDiagramStyleID()"><code><em>Diagram Style ID</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_ID()">getAbstractDiagramRepresentationObject_ID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getID()"><code><em>ID</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_InitialFrameSizeSet()">getAbstractDiagramRepresentationObject_InitialFrameSizeSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#isInitialFrameSizeSet()"><code><em>Initial Frame Size Set</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_RequiredFeature()">getAbstractDiagramRepresentationObject_RequiredFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getRequiredFeature()"><code><em>Required Feature</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_Type()">getAbstractDiagramRepresentationObject_Type</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getType()"><code><em>Type</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAbstractDiagramRepresentationObject_UmlType()">getAbstractDiagramRepresentationObject_UmlType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getUmlType()"><code><em>Uml Type</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor()">getDiagramContentsDescriptor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Contents Descriptor</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor_BinaryObject()">getDiagramContentsDescriptor_BinaryObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the containment reference '<a href="DiagramContentsDescriptor.html#getBinaryObject()"><code><em>Binary Object</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor_ContentHash()">getDiagramContentsDescriptor_ContentHash</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="DiagramContentsDescriptor.html#getContentHash()"><code><em>Content Hash</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor_ExporterName()">getDiagramContentsDescriptor_ExporterName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="DiagramContentsDescriptor.html#getExporterName()"><code><em>Exporter Name</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor_ExporterVersion()">getDiagramContentsDescriptor_ExporterVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="DiagramContentsDescriptor.html#getExporterVersion()"><code><em>Exporter Version</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor_Representation()">getDiagramContentsDescriptor_Representation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the container reference '<a href="DiagramContentsDescriptor.html#getRepresentation()"><code><em>Representation</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor_UsedElements()">getDiagramContentsDescriptor_UsedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute list '<a href="DiagramContentsDescriptor.html#getUsedElements()"><code><em>Used Elements</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContentsDescriptor_UsedObjects()">getDiagramContentsDescriptor_UsedObjects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the reference list '<a href="DiagramContentsDescriptor.html#getUsedObjects()"><code><em>Used Objects</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="DiagramFactory.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramFactory</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramFactory()">getDiagramFactory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the factory that creates the instances of the model.</div>
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
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNAME</span></div>
<div class="block">The package name.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.eNAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eNS_URI">
<h3>eNS_URI</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNS_URI</span></div>
<div class="block">The package namespace URI.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.eNS_URI">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eNS_PREFIX">
<h3>eNS_PREFIX</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNS_PREFIX</span></div>
<div class="block">The package namespace name.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.eNS_PREFIX">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eINSTANCE">
<h3>eINSTANCE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a href="DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramPackage</a></span> <span class="element-name">eINSTANCE</span></div>
<div class="block">The singleton instance of the package.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT</span></div>
<div class="block">The meta object id for the '<code><em>Abstract Diagram Representation Object</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>AbstractDiagramRepresentationObjectImpl</code></li>
<li><code>DiagramPackageImpl.getAbstractDiagramRepresentationObject()</code></li>
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID</span></div>
<div class="block">The feature id for the '<em><b>ID</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__ID">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE</span></div>
<div class="block">The feature id for the '<em><b>Type</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__TYPE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE</span></div>
<div class="block">The feature id for the '<em><b>Uml Type</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__UML_TYPE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES</span></div>
<div class="block">The feature id for the '<em><b>Diagram Properties</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET</span></div>
<div class="block">The feature id for the '<em><b>Initial Frame Size Set</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__INITIAL_FRAME_SIZE_SET">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE</span></div>
<div class="block">The feature id for the '<em><b>Required Feature</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__REQUIRED_FEATURE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS</span></div>
<div class="block">The feature id for the '<em><b>Diagram Contents</b></em>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_CONTENTS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID</span></div>
<div class="block">The feature id for the '<em><b>Diagram Style ID</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT__DIAGRAM_STYLE_ID">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT">
<h3>ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Abstract Diagram Representation Object</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.ABSTRACT_DIAGRAM_REPRESENTATION_OBJECT_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR</span></div>
<div class="block">The meta object id for the '<code><em>Contents Descriptor</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>DiagramContentsDescriptorImpl</code></li>
<li><code>DiagramPackageImpl.getDiagramContentsDescriptor()</code></li>
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION</span></div>
<div class="block">The feature id for the '<em><b>Representation</b></em>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__REPRESENTATION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME</span></div>
<div class="block">The feature id for the '<em><b>Exporter Name</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_NAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION</span></div>
<div class="block">The feature id for the '<em><b>Exporter Version</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__EXPORTER_VERSION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS</span></div>
<div class="block">The feature id for the '<em><b>Used Elements</b></em>' attribute list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__USED_ELEMENTS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT</span></div>
<div class="block">The feature id for the '<em><b>Binary Object</b></em>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__BINARY_OBJECT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH</span></div>
<div class="block">The feature id for the '<em><b>Content Hash</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__CONTENT_HASH">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS</span></div>
<div class="block">The feature id for the '<em><b>Used Objects</b></em>' reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR__USED_OBJECTS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT">
<h3>DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Contents Descriptor</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.foundation.diagram.DiagramPackage.DIAGRAM_CONTENTS_DESCRIPTOR_FEATURE_COUNT">Constant Field Values</a></li>
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
<section class="detail" id="getAbstractDiagramRepresentationObject()">
<h3>getAbstractDiagramRepresentationObject</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getAbstractDiagramRepresentationObject</span>()</div>
<div class="block">Returns the meta object for class '<a href="AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Abstract Diagram Representation Object</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Abstract Diagram Representation Object</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code>AbstractDiagramRepresentationObject</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_ID()">
<h3>getAbstractDiagramRepresentationObject_ID</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getAbstractDiagramRepresentationObject_ID</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getID()"><code><em>ID</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>ID</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#getID()"><code>AbstractDiagramRepresentationObject.getID()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_Type()">
<h3>getAbstractDiagramRepresentationObject_Type</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getAbstractDiagramRepresentationObject_Type</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getType()"><code><em>Type</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Type</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#getType()"><code>AbstractDiagramRepresentationObject.getType()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_UmlType()">
<h3>getAbstractDiagramRepresentationObject_UmlType</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getAbstractDiagramRepresentationObject_UmlType</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getUmlType()"><code><em>Uml Type</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Uml Type</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#getUmlType()"><code>AbstractDiagramRepresentationObject.getUmlType()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_DiagramProperties()">
<h3>getAbstractDiagramRepresentationObject_DiagramProperties</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getAbstractDiagramRepresentationObject_DiagramProperties</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getDiagramProperties()"><code><em>Diagram Properties</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Diagram Properties</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#getDiagramProperties()"><code>AbstractDiagramRepresentationObject.getDiagramProperties()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_InitialFrameSizeSet()">
<h3>getAbstractDiagramRepresentationObject_InitialFrameSizeSet</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getAbstractDiagramRepresentationObject_InitialFrameSizeSet</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#isInitialFrameSizeSet()"><code><em>Initial Frame Size Set</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Initial Frame Size Set</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#isInitialFrameSizeSet()"><code>AbstractDiagramRepresentationObject.isInitialFrameSizeSet()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_RequiredFeature()">
<h3>getAbstractDiagramRepresentationObject_RequiredFeature</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getAbstractDiagramRepresentationObject_RequiredFeature</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getRequiredFeature()"><code><em>Required Feature</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Required Feature</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#getRequiredFeature()"><code>AbstractDiagramRepresentationObject.getRequiredFeature()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_DiagramContents()">
<h3>getAbstractDiagramRepresentationObject_DiagramContents</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getAbstractDiagramRepresentationObject_DiagramContents</span>()</div>
<div class="block">Returns the meta object for the containment reference '<a href="AbstractDiagramRepresentationObject.html#getDiagramContents()"><code><em>Diagram Contents</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the containment reference '<em>Diagram Contents</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#getDiagramContents()"><code>AbstractDiagramRepresentationObject.getDiagramContents()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramRepresentationObject_DiagramStyleID()">
<h3>getAbstractDiagramRepresentationObject_DiagramStyleID</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getAbstractDiagramRepresentationObject_DiagramStyleID</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="AbstractDiagramRepresentationObject.html#getDiagramStyleID()"><code><em>Diagram Style ID</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Diagram Style ID</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="AbstractDiagramRepresentationObject.html#getDiagramStyleID()"><code>AbstractDiagramRepresentationObject.getDiagramStyleID()</code></a></li>
<li><a href="#getAbstractDiagramRepresentationObject()"><code>getAbstractDiagramRepresentationObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor()">
<h3>getDiagramContentsDescriptor</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getDiagramContentsDescriptor</span>()</div>
<div class="block">Returns the meta object for class '<a href="DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Contents Descriptor</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Contents Descriptor</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code>DiagramContentsDescriptor</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor_Representation()">
<h3>getDiagramContentsDescriptor_Representation</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getDiagramContentsDescriptor_Representation</span>()</div>
<div class="block">Returns the meta object for the container reference '<a href="DiagramContentsDescriptor.html#getRepresentation()"><code><em>Representation</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the container reference '<em>Representation</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramContentsDescriptor.html#getRepresentation()"><code>DiagramContentsDescriptor.getRepresentation()</code></a></li>
<li><a href="#getDiagramContentsDescriptor()"><code>getDiagramContentsDescriptor()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor_ExporterName()">
<h3>getDiagramContentsDescriptor_ExporterName</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getDiagramContentsDescriptor_ExporterName</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="DiagramContentsDescriptor.html#getExporterName()"><code><em>Exporter Name</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Exporter Name</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramContentsDescriptor.html#getExporterName()"><code>DiagramContentsDescriptor.getExporterName()</code></a></li>
<li><a href="#getDiagramContentsDescriptor()"><code>getDiagramContentsDescriptor()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor_ExporterVersion()">
<h3>getDiagramContentsDescriptor_ExporterVersion</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getDiagramContentsDescriptor_ExporterVersion</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="DiagramContentsDescriptor.html#getExporterVersion()"><code><em>Exporter Version</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Exporter Version</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramContentsDescriptor.html#getExporterVersion()"><code>DiagramContentsDescriptor.getExporterVersion()</code></a></li>
<li><a href="#getDiagramContentsDescriptor()"><code>getDiagramContentsDescriptor()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor_UsedElements()">
<h3>getDiagramContentsDescriptor_UsedElements</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getDiagramContentsDescriptor_UsedElements</span>()</div>
<div class="block">Returns the meta object for the attribute list '<a href="DiagramContentsDescriptor.html#getUsedElements()"><code><em>Used Elements</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute list '<em>Used Elements</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramContentsDescriptor.html#getUsedElements()"><code>DiagramContentsDescriptor.getUsedElements()</code></a></li>
<li><a href="#getDiagramContentsDescriptor()"><code>getDiagramContentsDescriptor()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor_BinaryObject()">
<h3>getDiagramContentsDescriptor_BinaryObject</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getDiagramContentsDescriptor_BinaryObject</span>()</div>
<div class="block">Returns the meta object for the containment reference '<a href="DiagramContentsDescriptor.html#getBinaryObject()"><code><em>Binary Object</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the containment reference '<em>Binary Object</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramContentsDescriptor.html#getBinaryObject()"><code>DiagramContentsDescriptor.getBinaryObject()</code></a></li>
<li><a href="#getDiagramContentsDescriptor()"><code>getDiagramContentsDescriptor()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor_ContentHash()">
<h3>getDiagramContentsDescriptor_ContentHash</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getDiagramContentsDescriptor_ContentHash</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="DiagramContentsDescriptor.html#getContentHash()"><code><em>Content Hash</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Content Hash</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramContentsDescriptor.html#getContentHash()"><code>DiagramContentsDescriptor.getContentHash()</code></a></li>
<li><a href="#getDiagramContentsDescriptor()"><code>getDiagramContentsDescriptor()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContentsDescriptor_UsedObjects()">
<h3>getDiagramContentsDescriptor_UsedObjects</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getDiagramContentsDescriptor_UsedObjects</span>()</div>
<div class="block">Returns the meta object for the reference list '<a href="DiagramContentsDescriptor.html#getUsedObjects()"><code><em>Used Objects</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the reference list '<em>Used Objects</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramContentsDescriptor.html#getUsedObjects()"><code>DiagramContentsDescriptor.getUsedObjects()</code></a></li>
<li><a href="#getDiagramContentsDescriptor()"><code>getDiagramContentsDescriptor()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramFactory()">
<h3>getDiagramFactory</h3>
<div class="member-signature"><span class="return-type"><a href="DiagramFactory.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramFactory</a></span> <span class="element-name">getDiagramFactory</span>()</div>
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
