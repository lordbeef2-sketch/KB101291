# JAVA OPENAPI: KerMLLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/libraries/standard/KerMLLibrary.html
- source_path: `com/dassault_systemes/modeler/kerml/libraries/standard/KerMLLibrary.html`
- source_sha256: `38257e70cbeca9b6dc908b26d2c215ec8110a68b436e5414b07ca215a5aeead4`
- captured_utc: `2026-07-14T16:44:46.052817+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.libraries.standard](package-summary.html)

## Class KerMLLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../AbstractLibrary.html)
com.dassault_systemes.modeler.kerml.libraries.standard.KerMLLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classKerMLLibrary
extends [AbstractLibrary](../AbstractLibrary.html)

Provides typed access to elements from the KerML standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[KerMLLibrary.BehaviorMetaclass](KerMLLibrary.BehaviorMetaclass.html)`
Type wrapper for the BehaviorMetaclass library element.
`static class`
`[KerMLLibrary.ClassifierMetaclass](KerMLLibrary.ClassifierMetaclass.html)`
Type wrapper for the ClassifierMetaclass library element.
`static class`
`[KerMLLibrary.ClassMetaclass](KerMLLibrary.ClassMetaclass.html)`
Type wrapper for the ClassMetaclass library element.
`static class`
`[KerMLLibrary.CommentMetaclass](KerMLLibrary.CommentMetaclass.html)`
Type wrapper for the CommentMetaclass library element.
`static class`
`[KerMLLibrary.ConnectorMetaclass](KerMLLibrary.ConnectorMetaclass.html)`
Type wrapper for the ConnectorMetaclass library element.
`static class`
`[KerMLLibrary.DataTypeMetaclass](KerMLLibrary.DataTypeMetaclass.html)`
Type wrapper for the DataTypeMetaclass library element.
`static class`
`[KerMLLibrary.DependencyMetaclass](KerMLLibrary.DependencyMetaclass.html)`
Type wrapper for the DependencyMetaclass library element.
`static class`
`[KerMLLibrary.ElementMetaclass](KerMLLibrary.ElementMetaclass.html)`
Type wrapper for the ElementMetaclass library element.
`static class`
`[KerMLLibrary.ExpressionMetaclass](KerMLLibrary.ExpressionMetaclass.html)`
Type wrapper for the ExpressionMetaclass library element.
`static class`
`[KerMLLibrary.FeatureMetaclass](KerMLLibrary.FeatureMetaclass.html)`
Type wrapper for the FeatureMetaclass library element.
`static class`
`[KerMLLibrary.FeatureReferenceExpressionMetaclass](KerMLLibrary.FeatureReferenceExpressionMetaclass.html)`
Type wrapper for the FeatureReferenceExpressionMetaclass library element.
`static class`
`[KerMLLibrary.FunctionMetaclass](KerMLLibrary.FunctionMetaclass.html)`
Type wrapper for the FunctionMetaclass library element.
`static class`
`[KerMLLibrary.InteractionMetaclass](KerMLLibrary.InteractionMetaclass.html)`
Type wrapper for the InteractionMetaclass library element.
`static class`
`[KerMLLibrary.InvocationExpressionMetaclass](KerMLLibrary.InvocationExpressionMetaclass.html)`
Type wrapper for the InvocationExpressionMetaclass library element.
`static class`
`[KerMLLibrary.LibraryPackageMetaclass](KerMLLibrary.LibraryPackageMetaclass.html)`
Type wrapper for the LibraryPackageMetaclass library element.
`static class`
`[KerMLLibrary.LiteralBooleanMetaclass](KerMLLibrary.LiteralBooleanMetaclass.html)`
Type wrapper for the LiteralBooleanMetaclass library element.
`static class`
`[KerMLLibrary.LiteralExpressionMetaclass](KerMLLibrary.LiteralExpressionMetaclass.html)`
Type wrapper for the LiteralExpressionMetaclass library element.
`static class`
`[KerMLLibrary.LiteralIntegerMetaclass](KerMLLibrary.LiteralIntegerMetaclass.html)`
Type wrapper for the LiteralIntegerMetaclass library element.
`static class`
`[KerMLLibrary.LiteralRationalMetaclass](KerMLLibrary.LiteralRationalMetaclass.html)`
Type wrapper for the LiteralRationalMetaclass library element.
`static class`
`[KerMLLibrary.LiteralStringMetaclass](KerMLLibrary.LiteralStringMetaclass.html)`
Type wrapper for the LiteralStringMetaclass library element.
`static class`
`[KerMLLibrary.MultiplicityMetaclass](KerMLLibrary.MultiplicityMetaclass.html)`
Type wrapper for the MultiplicityMetaclass library element.
`static class`
`[KerMLLibrary.NamespaceMetaclass](KerMLLibrary.NamespaceMetaclass.html)`
Type wrapper for the NamespaceMetaclass library element.
`static class`
`[KerMLLibrary.NullExpressionMetaclass](KerMLLibrary.NullExpressionMetaclass.html)`
Type wrapper for the NullExpressionMetaclass library element.
`static class`
`[KerMLLibrary.PackageMetaclass](KerMLLibrary.PackageMetaclass.html)`
Type wrapper for the PackageMetaclass library element.
`static class`
`[KerMLLibrary.RelationshipMetaclass](KerMLLibrary.RelationshipMetaclass.html)`
Type wrapper for the RelationshipMetaclass library element.
`static class`
`[KerMLLibrary.SubclassificationMetaclass](KerMLLibrary.SubclassificationMetaclass.html)`
Type wrapper for the SubclassificationMetaclass library element.
`static class`
`[KerMLLibrary.TypeMetaclass](KerMLLibrary.TypeMetaclass.html)`
Type wrapper for the TypeMetaclass library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[KerMLLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a KerMLLibrary for the given project.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[KerMLLibrary.BehaviorMetaclass](KerMLLibrary.BehaviorMetaclass.html)`
`[Behavior](#Behavior())()`
Returns the wrapper for the Behavior library element.
`[KerMLLibrary.ClassMetaclass](KerMLLibrary.ClassMetaclass.html)`
`[Class](#Class())()`
Returns the wrapper for the Class library element.
`[KerMLLibrary.ClassifierMetaclass](KerMLLibrary.ClassifierMetaclass.html)`
`[Classifier](#Classifier())()`
Returns the wrapper for the Classifier library element.
`[KerMLLibrary.CommentMetaclass](KerMLLibrary.CommentMetaclass.html)`
`[Comment](#Comment())()`
Returns the wrapper for the Comment library element.
`[KerMLLibrary.ConnectorMetaclass](KerMLLibrary.ConnectorMetaclass.html)`
`[Connector](#Connector())()`
Returns the wrapper for the Connector library element.
`[KerMLLibrary.DataTypeMetaclass](KerMLLibrary.DataTypeMetaclass.html)`
`[DataType](#DataType())()`
Returns the wrapper for the DataType library element.
`[KerMLLibrary.DependencyMetaclass](KerMLLibrary.DependencyMetaclass.html)`
`[Dependency](#Dependency())()`
Returns the wrapper for the Dependency library element.
`[KerMLLibrary.ElementMetaclass](KerMLLibrary.ElementMetaclass.html)`
`[Element](#Element())()`
Returns the wrapper for the Element library element.
`[KerMLLibrary.ExpressionMetaclass](KerMLLibrary.ExpressionMetaclass.html)`
`[Expression](#Expression())()`
Returns the wrapper for the Expression library element.
`[KerMLLibrary.FeatureMetaclass](KerMLLibrary.FeatureMetaclass.html)`
`[Feature](#Feature())()`
Returns the wrapper for the Feature library element.
`[KerMLLibrary.FeatureReferenceExpressionMetaclass](KerMLLibrary.FeatureReferenceExpressionMetaclass.html)`
`[FeatureReferenceExpression](#FeatureReferenceExpression())()`
Returns the wrapper for the FeatureReferenceExpression library element.
`[KerMLLibrary.FunctionMetaclass](KerMLLibrary.FunctionMetaclass.html)`
`[Function](#Function())()`
Returns the wrapper for the Function library element.
`static [KerMLLibrary](KerMLLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the KerMLLibrary instance for the project that owns the given element.
`static [KerMLLibrary](KerMLLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the KerMLLibrary instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns the type wrappers exposed by this library.
`[KerMLLibrary.InteractionMetaclass](KerMLLibrary.InteractionMetaclass.html)`
`[Interaction](#Interaction())()`
Returns the wrapper for the Interaction library element.
`[KerMLLibrary.InvocationExpressionMetaclass](KerMLLibrary.InvocationExpressionMetaclass.html)`
`[InvocationExpression](#InvocationExpression())()`
Returns the wrapper for the InvocationExpression library element.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is treated as semantic.
`[KerMLLibrary.LibraryPackageMetaclass](KerMLLibrary.LibraryPackageMetaclass.html)`
`[LibraryPackage](#LibraryPackage())()`
Returns the wrapper for the LibraryPackage library element.
`[KerMLLibrary.LiteralBooleanMetaclass](KerMLLibrary.LiteralBooleanMetaclass.html)`
`[LiteralBoolean](#LiteralBoolean())()`
Returns the wrapper for the LiteralBoolean library element.
`[KerMLLibrary.LiteralExpressionMetaclass](KerMLLibrary.LiteralExpressionMetaclass.html)`
`[LiteralExpression](#LiteralExpression())()`
Returns the wrapper for the LiteralExpression library element.
`[KerMLLibrary.LiteralIntegerMetaclass](KerMLLibrary.LiteralIntegerMetaclass.html)`
`[LiteralInteger](#LiteralInteger())()`
Returns the wrapper for the LiteralInteger library element.
`[KerMLLibrary.LiteralRationalMetaclass](KerMLLibrary.LiteralRationalMetaclass.html)`
`[LiteralRational](#LiteralRational())()`
Returns the wrapper for the LiteralRational library element.
`[KerMLLibrary.LiteralStringMetaclass](KerMLLibrary.LiteralStringMetaclass.html)`
`[LiteralString](#LiteralString())()`
Returns the wrapper for the LiteralString library element.
`[KerMLLibrary.MultiplicityMetaclass](KerMLLibrary.MultiplicityMetaclass.html)`
`[Multiplicity](#Multiplicity())()`
Returns the wrapper for the Multiplicity library element.
`[KerMLLibrary.NamespaceMetaclass](KerMLLibrary.NamespaceMetaclass.html)`
`[Namespace](#Namespace())()`
Returns the wrapper for the Namespace library element.
`[KerMLLibrary.NullExpressionMetaclass](KerMLLibrary.NullExpressionMetaclass.html)`
`[NullExpression](#NullExpression())()`
Returns the wrapper for the NullExpression library element.
`[KerMLLibrary.PackageMetaclass](KerMLLibrary.PackageMetaclass.html)`
`[Package](#Package())()`
Returns the wrapper for the Package library element.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the library packages exposed by this wrapper.
`[KerMLLibrary.RelationshipMetaclass](KerMLLibrary.RelationshipMetaclass.html)`
`[Relationship](#Relationship())()`
Returns the wrapper for the Relationship library element.
`[KerMLLibrary.SubclassificationMetaclass](KerMLLibrary.SubclassificationMetaclass.html)`
`[Subclassification](#Subclassification())()`
Returns the wrapper for the Subclassification library element.
`[KerMLLibrary.TypeMetaclass](KerMLLibrary.TypeMetaclass.html)`
`[Type](#Type())()`
Returns the wrapper for the Type library element.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../AbstractLibrary.html)
`[findFunctionInLibrary](../AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../AbstractLibrary.html#getLibraryPackages()), [getNamespace](../AbstractLibrary.html#getNamespace()), [initialized](../AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
KerMLLibrary
public KerMLLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a KerMLLibrary for the given project.
Parameters:
`project` - the project that provides access to the library model elements
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [KerMLLibrary](KerMLLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the KerMLLibrary instance for the given project.
Parameters:
`project` - the project whose library instance is requested
Returns:
the library instance for the project
getInstance
public static [KerMLLibrary](KerMLLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the KerMLLibrary instance for the project that owns the given element.
Parameters:
`element` - the element whose owning project is used to resolve the library instance
Returns:
the library instance associated with the element project
isSemantic
public boolean isSemantic()
Returns whether this library is treated as semantic.
Specified by:
`[isSemantic](../AbstractLibrary.html#isSemantic())` in class `[AbstractLibrary](../AbstractLibrary.html)`
Returns:
`true` if this library is semantic
packagesNames
protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> packagesNames()
Returns the names of the library packages exposed by this wrapper.
Specified by:
`[packagesNames](../AbstractLibrary.html#packagesNames())` in class `[AbstractLibrary](../AbstractLibrary.html)`
Returns:
package names that belong to this library
Comment
public [KerMLLibrary.CommentMetaclass](KerMLLibrary.CommentMetaclass.html) Comment()
Returns the wrapper for the Comment library element.
Returns:
the wrapper for the Comment element
Dependency
public [KerMLLibrary.DependencyMetaclass](KerMLLibrary.DependencyMetaclass.html) Dependency()
Returns the wrapper for the Dependency library element.
Returns:
the wrapper for the Dependency element
Element
public [KerMLLibrary.ElementMetaclass](KerMLLibrary.ElementMetaclass.html) Element()
Returns the wrapper for the Element library element.
Returns:
the wrapper for the Element element
Namespace
public [KerMLLibrary.NamespaceMetaclass](KerMLLibrary.NamespaceMetaclass.html) Namespace()
Returns the wrapper for the Namespace library element.
Returns:
the wrapper for the Namespace element
Relationship
public [KerMLLibrary.RelationshipMetaclass](KerMLLibrary.RelationshipMetaclass.html) Relationship()
Returns the wrapper for the Relationship library element.
Returns:
the wrapper for the Relationship element
Classifier
public [KerMLLibrary.ClassifierMetaclass](KerMLLibrary.ClassifierMetaclass.html) Classifier()
Returns the wrapper for the Classifier library element.
Returns:
the wrapper for the Classifier element
Feature
public [KerMLLibrary.FeatureMetaclass](KerMLLibrary.FeatureMetaclass.html) Feature()
Returns the wrapper for the Feature library element.
Returns:
the wrapper for the Feature element
Multiplicity
public [KerMLLibrary.MultiplicityMetaclass](KerMLLibrary.MultiplicityMetaclass.html) Multiplicity()
Returns the wrapper for the Multiplicity library element.
Returns:
the wrapper for the Multiplicity element
Subclassification
public [KerMLLibrary.SubclassificationMetaclass](KerMLLibrary.SubclassificationMetaclass.html) Subclassification()
Returns the wrapper for the Subclassification library element.
Returns:
the wrapper for the Subclassification element
Type
public [KerMLLibrary.TypeMetaclass](KerMLLibrary.TypeMetaclass.html) Type()
Returns the wrapper for the Type library element.
Returns:
the wrapper for the Type element
Behavior
public [KerMLLibrary.BehaviorMetaclass](KerMLLibrary.BehaviorMetaclass.html) Behavior()
Returns the wrapper for the Behavior library element.
Returns:
the wrapper for the Behavior element
Class
public [KerMLLibrary.ClassMetaclass](KerMLLibrary.ClassMetaclass.html) Class()
Returns the wrapper for the Class library element.
Returns:
the wrapper for the Class element
Connector
public [KerMLLibrary.ConnectorMetaclass](KerMLLibrary.ConnectorMetaclass.html) Connector()
Returns the wrapper for the Connector library element.
Returns:
the wrapper for the Connector element
DataType
public [KerMLLibrary.DataTypeMetaclass](KerMLLibrary.DataTypeMetaclass.html) DataType()
Returns the wrapper for the DataType library element.
Returns:
the wrapper for the DataType element
Expression
public [KerMLLibrary.ExpressionMetaclass](KerMLLibrary.ExpressionMetaclass.html) Expression()
Returns the wrapper for the Expression library element.
Returns:
the wrapper for the Expression element
FeatureReferenceExpression
public [KerMLLibrary.FeatureReferenceExpressionMetaclass](KerMLLibrary.FeatureReferenceExpressionMetaclass.html) FeatureReferenceExpression()
Returns the wrapper for the FeatureReferenceExpression library element.
Returns:
the wrapper for the FeatureReferenceExpression element
Function
public [KerMLLibrary.FunctionMetaclass](KerMLLibrary.FunctionMetaclass.html) Function()
Returns the wrapper for the Function library element.
Returns:
the wrapper for the Function element
Interaction
public [KerMLLibrary.InteractionMetaclass](KerMLLibrary.InteractionMetaclass.html) Interaction()
Returns the wrapper for the Interaction library element.
Returns:
the wrapper for the Interaction element
InvocationExpression
public [KerMLLibrary.InvocationExpressionMetaclass](KerMLLibrary.InvocationExpressionMetaclass.html) InvocationExpression()
Returns the wrapper for the InvocationExpression library element.
Returns:
the wrapper for the InvocationExpression element
LibraryPackage
public [KerMLLibrary.LibraryPackageMetaclass](KerMLLibrary.LibraryPackageMetaclass.html) LibraryPackage()
Returns the wrapper for the LibraryPackage library element.
Returns:
the wrapper for the LibraryPackage element
LiteralBoolean
public [KerMLLibrary.LiteralBooleanMetaclass](KerMLLibrary.LiteralBooleanMetaclass.html) LiteralBoolean()
Returns the wrapper for the LiteralBoolean library element.
Returns:
the wrapper for the LiteralBoolean element
LiteralExpression
public [KerMLLibrary.LiteralExpressionMetaclass](KerMLLibrary.LiteralExpressionMetaclass.html) LiteralExpression()
Returns the wrapper for the LiteralExpression library element.
Returns:
the wrapper for the LiteralExpression element
LiteralInteger
public [KerMLLibrary.LiteralIntegerMetaclass](KerMLLibrary.LiteralIntegerMetaclass.html) LiteralInteger()
Returns the wrapper for the LiteralInteger library element.
Returns:
the wrapper for the LiteralInteger element
LiteralRational
public [KerMLLibrary.LiteralRationalMetaclass](KerMLLibrary.LiteralRationalMetaclass.html) LiteralRational()
Returns the wrapper for the LiteralRational library element.
Returns:
the wrapper for the LiteralRational element
LiteralString
public [KerMLLibrary.LiteralStringMetaclass](KerMLLibrary.LiteralStringMetaclass.html) LiteralString()
Returns the wrapper for the LiteralString library element.
Returns:
the wrapper for the LiteralString element
NullExpression
public [KerMLLibrary.NullExpressionMetaclass](KerMLLibrary.NullExpressionMetaclass.html) NullExpression()
Returns the wrapper for the NullExpression library element.
Returns:
the wrapper for the NullExpression element
Package
public [KerMLLibrary.PackageMetaclass](KerMLLibrary.PackageMetaclass.html) Package()
Returns the wrapper for the Package library element.
Returns:
the wrapper for the Package element
getTypeWrappers
protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper> getTypeWrappers()
Returns the type wrappers exposed by this library.
Specified by:
`[getTypeWrappers](../AbstractLibrary.html#getTypeWrappers())` in class `[AbstractLibrary](../AbstractLibrary.html)`
Returns:
type wrappers managed by this library

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.libraries.standard</a></div>
<h1 class="title" title="Class KerMLLibrary">Class KerMLLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.libraries.standard.KerMLLibrary</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">KerMLLibrary</span>
<span class="extends-implements">extends <a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Provides typed access to elements from the KerML standard library.</div>
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
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.BehaviorMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.BehaviorMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the BehaviorMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.ClassifierMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ClassifierMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the ClassifierMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.ClassMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ClassMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the ClassMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.CommentMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.CommentMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the CommentMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.ConnectorMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ConnectorMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the ConnectorMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.DataTypeMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.DataTypeMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the DataTypeMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.DependencyMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.DependencyMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the DependencyMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.ElementMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ElementMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the ElementMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.ExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ExpressionMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the ExpressionMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.FeatureMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FeatureMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the FeatureMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.FeatureReferenceExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FeatureReferenceExpressionMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the FeatureReferenceExpressionMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.FunctionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FunctionMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the FunctionMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.InteractionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.InteractionMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the InteractionMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.InvocationExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.InvocationExpressionMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the InvocationExpressionMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.LibraryPackageMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LibraryPackageMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the LibraryPackageMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.LiteralBooleanMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralBooleanMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the LiteralBooleanMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.LiteralExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralExpressionMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the LiteralExpressionMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.LiteralIntegerMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralIntegerMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the LiteralIntegerMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.LiteralRationalMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralRationalMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the LiteralRationalMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.LiteralStringMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralStringMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the LiteralStringMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.MultiplicityMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.MultiplicityMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the MultiplicityMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.NamespaceMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.NamespaceMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the NamespaceMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.NullExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.NullExpressionMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the NullExpressionMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.PackageMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.PackageMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the PackageMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.RelationshipMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.RelationshipMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the RelationshipMetaclass library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="KerMLLibrary.SubclassificationMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.SubclassificationMetaclass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the SubclassificationMetaclass library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="KerMLLibrary.TypeMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.TypeMetaclass</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the TypeMetaclass library element.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">KerMLLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a KerMLLibrary for the given project.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.BehaviorMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.BehaviorMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Behavior()">Behavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Behavior library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.ClassMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ClassMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Class()">Class</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Class library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.ClassifierMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ClassifierMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Classifier()">Classifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Classifier library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.CommentMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.CommentMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Comment()">Comment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Comment library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.ConnectorMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ConnectorMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Connector()">Connector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Connector library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.DataTypeMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.DataTypeMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#DataType()">DataType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the DataType library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.DependencyMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.DependencyMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Dependency()">Dependency</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Dependency library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.ElementMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ElementMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Element()">Element</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Element library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.ExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ExpressionMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Expression()">Expression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Expression library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.FeatureMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FeatureMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Feature()">Feature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Feature library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.FeatureReferenceExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FeatureReferenceExpressionMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#FeatureReferenceExpression()">FeatureReferenceExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the FeatureReferenceExpression library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.FunctionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FunctionMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Function()">Function</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Function library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="KerMLLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the KerMLLibrary instance for the project that owns the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="KerMLLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the KerMLLibrary instance for the given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the type wrappers exposed by this library.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.InteractionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.InteractionMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Interaction()">Interaction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Interaction library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.InvocationExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.InvocationExpressionMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#InvocationExpression()">InvocationExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the InvocationExpression library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is treated as semantic.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.LibraryPackageMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LibraryPackageMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LibraryPackage()">LibraryPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LibraryPackage library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.LiteralBooleanMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralBooleanMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LiteralBoolean()">LiteralBoolean</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LiteralBoolean library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.LiteralExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralExpressionMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LiteralExpression()">LiteralExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LiteralExpression library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.LiteralIntegerMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralIntegerMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LiteralInteger()">LiteralInteger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LiteralInteger library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.LiteralRationalMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralRationalMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LiteralRational()">LiteralRational</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LiteralRational library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.LiteralStringMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralStringMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LiteralString()">LiteralString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LiteralString library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.MultiplicityMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.MultiplicityMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Multiplicity()">Multiplicity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Multiplicity library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.NamespaceMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.NamespaceMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Namespace()">Namespace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Namespace library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.NullExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.NullExpressionMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#NullExpression()">NullExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the NullExpression library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.PackageMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.PackageMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Package()">Package</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Package library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the library packages exposed by this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.RelationshipMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.RelationshipMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Relationship()">Relationship</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Relationship library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.SubclassificationMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.SubclassificationMetaclass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Subclassification()">Subclassification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Subclassification library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="KerMLLibrary.TypeMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.TypeMetaclass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Type()">Type</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Type library element.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary">Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.<a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></h3>
<code><a href="../AbstractLibrary.html#findFunctionInLibrary(java.lang.String)">findFunctionInLibrary</a>, <a href="../AbstractLibrary.html#findLibraryPackage(java.lang.String)">findLibraryPackage</a>, <a href="../AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)">findPackage</a>, <a href="../AbstractLibrary.html#getLibraryPackages()">getLibraryPackages</a>, <a href="../AbstractLibrary.html#getNamespace()">getNamespace</a>, <a href="../AbstractLibrary.html#initialized()">initialized</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>KerMLLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">KerMLLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a KerMLLibrary for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project that provides access to the library model elements</dd>
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
<section class="detail" id="getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="KerMLLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the KerMLLibrary instance for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project whose library instance is requested</dd>
<dt>Returns:</dt>
<dd>the library instance for the project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="KerMLLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the KerMLLibrary instance for the project that owns the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element whose owning project is used to resolve the library instance</dd>
<dt>Returns:</dt>
<dd>the library instance associated with the element project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSemantic()">
<h3>isSemantic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSemantic</span>()</div>
<div class="block">Returns whether this library is treated as semantic.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractLibrary.html#isSemantic()">isSemantic</a></code> in class <code><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if this library is semantic</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="packagesNames()">
<h3>packagesNames</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">packagesNames</span>()</div>
<div class="block">Returns the names of the library packages exposed by this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractLibrary.html#packagesNames()">packagesNames</a></code> in class <code><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>package names that belong to this library</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Comment()">
<h3>Comment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.CommentMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.CommentMetaclass</a></span> <span class="element-name">Comment</span>()</div>
<div class="block">Returns the wrapper for the Comment library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Comment element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Dependency()">
<h3>Dependency</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.DependencyMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.DependencyMetaclass</a></span> <span class="element-name">Dependency</span>()</div>
<div class="block">Returns the wrapper for the Dependency library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Dependency element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Element()">
<h3>Element</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.ElementMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ElementMetaclass</a></span> <span class="element-name">Element</span>()</div>
<div class="block">Returns the wrapper for the Element library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Element element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Namespace()">
<h3>Namespace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.NamespaceMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.NamespaceMetaclass</a></span> <span class="element-name">Namespace</span>()</div>
<div class="block">Returns the wrapper for the Namespace library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Namespace element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Relationship()">
<h3>Relationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.RelationshipMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.RelationshipMetaclass</a></span> <span class="element-name">Relationship</span>()</div>
<div class="block">Returns the wrapper for the Relationship library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Relationship element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Classifier()">
<h3>Classifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.ClassifierMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ClassifierMetaclass</a></span> <span class="element-name">Classifier</span>()</div>
<div class="block">Returns the wrapper for the Classifier library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Classifier element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Feature()">
<h3>Feature</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.FeatureMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FeatureMetaclass</a></span> <span class="element-name">Feature</span>()</div>
<div class="block">Returns the wrapper for the Feature library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Feature element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Multiplicity()">
<h3>Multiplicity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.MultiplicityMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.MultiplicityMetaclass</a></span> <span class="element-name">Multiplicity</span>()</div>
<div class="block">Returns the wrapper for the Multiplicity library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Multiplicity element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Subclassification()">
<h3>Subclassification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.SubclassificationMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.SubclassificationMetaclass</a></span> <span class="element-name">Subclassification</span>()</div>
<div class="block">Returns the wrapper for the Subclassification library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Subclassification element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Type()">
<h3>Type</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.TypeMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.TypeMetaclass</a></span> <span class="element-name">Type</span>()</div>
<div class="block">Returns the wrapper for the Type library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Type element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Behavior()">
<h3>Behavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.BehaviorMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.BehaviorMetaclass</a></span> <span class="element-name">Behavior</span>()</div>
<div class="block">Returns the wrapper for the Behavior library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Behavior element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Class()">
<h3>Class</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.ClassMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ClassMetaclass</a></span> <span class="element-name">Class</span>()</div>
<div class="block">Returns the wrapper for the Class library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Class element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Connector()">
<h3>Connector</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.ConnectorMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ConnectorMetaclass</a></span> <span class="element-name">Connector</span>()</div>
<div class="block">Returns the wrapper for the Connector library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Connector element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DataType()">
<h3>DataType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.DataTypeMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.DataTypeMetaclass</a></span> <span class="element-name">DataType</span>()</div>
<div class="block">Returns the wrapper for the DataType library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the DataType element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Expression()">
<h3>Expression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.ExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.ExpressionMetaclass</a></span> <span class="element-name">Expression</span>()</div>
<div class="block">Returns the wrapper for the Expression library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Expression element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FeatureReferenceExpression()">
<h3>FeatureReferenceExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.FeatureReferenceExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FeatureReferenceExpressionMetaclass</a></span> <span class="element-name">FeatureReferenceExpression</span>()</div>
<div class="block">Returns the wrapper for the FeatureReferenceExpression library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the FeatureReferenceExpression element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Function()">
<h3>Function</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.FunctionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.FunctionMetaclass</a></span> <span class="element-name">Function</span>()</div>
<div class="block">Returns the wrapper for the Function library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Function element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Interaction()">
<h3>Interaction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.InteractionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.InteractionMetaclass</a></span> <span class="element-name">Interaction</span>()</div>
<div class="block">Returns the wrapper for the Interaction library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Interaction element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="InvocationExpression()">
<h3>InvocationExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.InvocationExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.InvocationExpressionMetaclass</a></span> <span class="element-name">InvocationExpression</span>()</div>
<div class="block">Returns the wrapper for the InvocationExpression library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the InvocationExpression element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LibraryPackage()">
<h3>LibraryPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.LibraryPackageMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LibraryPackageMetaclass</a></span> <span class="element-name">LibraryPackage</span>()</div>
<div class="block">Returns the wrapper for the LibraryPackage library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LibraryPackage element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LiteralBoolean()">
<h3>LiteralBoolean</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.LiteralBooleanMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralBooleanMetaclass</a></span> <span class="element-name">LiteralBoolean</span>()</div>
<div class="block">Returns the wrapper for the LiteralBoolean library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LiteralBoolean element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LiteralExpression()">
<h3>LiteralExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.LiteralExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralExpressionMetaclass</a></span> <span class="element-name">LiteralExpression</span>()</div>
<div class="block">Returns the wrapper for the LiteralExpression library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LiteralExpression element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LiteralInteger()">
<h3>LiteralInteger</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.LiteralIntegerMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralIntegerMetaclass</a></span> <span class="element-name">LiteralInteger</span>()</div>
<div class="block">Returns the wrapper for the LiteralInteger library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LiteralInteger element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LiteralRational()">
<h3>LiteralRational</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.LiteralRationalMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralRationalMetaclass</a></span> <span class="element-name">LiteralRational</span>()</div>
<div class="block">Returns the wrapper for the LiteralRational library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LiteralRational element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LiteralString()">
<h3>LiteralString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.LiteralStringMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.LiteralStringMetaclass</a></span> <span class="element-name">LiteralString</span>()</div>
<div class="block">Returns the wrapper for the LiteralString library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LiteralString element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NullExpression()">
<h3>NullExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.NullExpressionMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.NullExpressionMetaclass</a></span> <span class="element-name">NullExpression</span>()</div>
<div class="block">Returns the wrapper for the NullExpression library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the NullExpression element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Package()">
<h3>Package</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="KerMLLibrary.PackageMetaclass.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">KerMLLibrary.PackageMetaclass</a></span> <span class="element-name">Package</span>()</div>
<div class="block">Returns the wrapper for the Package library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Package element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeWrappers()">
<h3>getTypeWrappers</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</span> <span class="element-name">getTypeWrappers</span>()</div>
<div class="block">Returns the type wrappers exposed by this library.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractLibrary.html#getTypeWrappers()">getTypeWrappers</a></code> in class <code><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>type wrappers managed by this library</dd>
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
