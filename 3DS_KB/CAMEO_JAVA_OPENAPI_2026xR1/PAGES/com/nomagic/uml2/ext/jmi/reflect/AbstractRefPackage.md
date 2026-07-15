# JAVA OPENAPI: AbstractRefPackage (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/jmi/reflect/AbstractRefPackage.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/AbstractRefPackage.html`
- source_sha256: `eabae98d83adfa5e67601d30e94a06315ad0e4413b940a0953b1223fa10930c4`
- captured_utc: `2026-07-14T16:46:22.953105+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Class AbstractRefPackage

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage

All Implemented Interfaces:
`com.nomagic.uml2.ext.jmi.MapOwner`, `[AbstractRefBaseObject](AbstractRefBaseObject.html)`, `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefPackage`

Direct Known Subclasses:
`[AbstractRepository](AbstractRepository.html)`, `[EcoreRefPackage](EcoreRefPackage.html)`

public abstract classAbstractRefPackage
extends com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
implements javax.jmi.reflect.RefPackage

The RefPackage interface is an abstraction for accessing a collection of
 objects and their associations. The interface provides an operation to access
 the meta object description for the package, and operations to access the
 package instance's class proxy objects and its association objects

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`mMetaObject, repository`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractRefPackage](#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository))([AbstractRepository](AbstractRepository.html) repository)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addAssociation](#addAssociation(java.lang.String,javax.jmi.reflect.RefAssociation))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 javax.jmi.reflect.RefAssociation assoc)`

`void`
`[addClass](#addClass(java.lang.String,javax.jmi.reflect.RefClass))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 javax.jmi.reflect.RefClass clazz)`

`void`
`[addPackage](#addPackage(java.lang.String,javax.jmi.reflect.RefBaseObject))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 javax.jmi.reflect.RefBaseObject pack)`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)`
`[getMetaObjects](#getMetaObjects())()`

`void`
`[internalError](#internalError(java.lang.String,javax.jmi.reflect.InvalidCallException))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string,
 javax.jmi.reflect.InvalidCallException ex)`

`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[refAllAssociations](#refAllAssociations())()`
The refAllAssociation operation returns all associations directly contained by this package.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[refAllClasses](#refAllClasses())()`
The refAllClasses operation returns all class proxies directly contained by this package.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[refAllPackages](#refAllPackages())()`
Returns a (possible empty) collection of RefPackages directly contained
 by this package.
`javax.jmi.reflect.RefAssociation`
`[refAssociation](#refAssociation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) associationName)`
The association (or associationName ) parameter should designate the (M2)
 association whose association object is to be returned.
`javax.jmi.reflect.RefAssociation`
`[refAssociation](#refAssociation(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject association)`

`javax.jmi.reflect.RefClass`
`[refClass](#refClass(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) className)`
The type (or className ) parameter should designate the class whose class
 proxy object is to be returned.
`javax.jmi.reflect.RefClass`
`[refClass](#refClass(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject type)`

`javax.jmi.reflect.RefStruct`
`[refCreateStruct](#refCreateStruct(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) structName,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) args)`
The refCreateStruct operation creates an instance of a struct data type
 defined by the metaobject structType (or structName ) whose attribute
 values are specified by the ordered collection args .
`javax.jmi.reflect.RefStruct`
`[refCreateStruct](#refCreateStruct(javax.jmi.reflect.RefObject,java.util.List))(javax.jmi.reflect.RefObject structType,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) name)`

`void`
`[refDelete](#refDelete())()`
The "refDelete" operation destroys this package, including the objects it contains directly or transitively.
`javax.jmi.reflect.RefEnum`
`[refGetEnum](#refGetEnum(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) enumName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) args)`
The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
`javax.jmi.reflect.RefEnum`
`[refGetEnum](#refGetEnum(javax.jmi.reflect.RefObject,java.lang.String))(javax.jmi.reflect.RefObject enumType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) args)`

`javax.jmi.reflect.RefPackage`
`[refPackage](#refPackage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) nestedPackageName)`
The "nestedPackage" (or nestedPackageName ) parameter should designate
 the package whose package object is to be returned.
`javax.jmi.reflect.RefPackage`
`[refPackage](#refPackage(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject nestedPackage)`

`void`
`[removeClass](#removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass))(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass clazz)`

`void`
`[removePackage](#removePackage(javax.jmi.reflect.RefBaseObject))(javax.jmi.reflect.RefBaseObject pack)`
Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`getRepository, mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractRefPackage
public AbstractRefPackage(@CheckForNull
 [AbstractRepository](AbstractRepository.html) repository)
Parameters:
`repository` -
 ============ METHOD DETAIL ========== 
Method Details
addAssociation
public void addAssociation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 javax.jmi.reflect.RefAssociation assoc)
Parameters:
`name` -
`assoc` -
refAllAssociations
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) refAllAssociations()
The refAllAssociation operation returns all associations directly contained by this package.
 Returns a (possible empty) collection of RefAssociations directly contained by this package.
Specified by:
`refAllAssociations` in interface `javax.jmi.reflect.RefPackage`
refAllClasses
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) refAllClasses()
The refAllClasses operation returns all class proxies directly contained by this package.
 Returns a (possible empty) collection of RefClasses directly contained by this package.
Specified by:
`refAllClasses` in interface `javax.jmi.reflect.RefPackage`
refAssociation
public javax.jmi.reflect.RefAssociation refAssociation(javax.jmi.reflect.RefObject association)
Specified by:
`refAssociation` in interface `javax.jmi.reflect.RefPackage`
refAssociation
public javax.jmi.reflect.RefAssociation refAssociation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) associationName)
The association (or associationName ) parameter should designate the (M2)
 association whose association object is to be returned. The
 refAssociation operations return an association object for a given
 association. specific analog: get () return type:
 RefAssociation isQuery: yes parameters: RefObject association (or String
 associationName) exceptions: JmiException (InvalidCallException,
 InvalidNameException)
Specified by:
`refAssociation` in interface `javax.jmi.reflect.RefPackage`
refClass
public javax.jmi.reflect.RefClass refClass(javax.jmi.reflect.RefObject type)
Specified by:
`refClass` in interface `javax.jmi.reflect.RefPackage`
refClass
public javax.jmi.reflect.RefClass refClass([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) className)
The type (or className ) parameter should designate the class whose class
 proxy object is to be returned. InvalidCallException is raised if the
 type parameter does not designate a valid class. InvalidNameException is
 raised when the className does not denote a valid class name. The
 refClass operations return the class proxy object for a given class.
 specific analog: get () return type: RefClass isQuery: yes
 parameters: RefObject type (or String className) exceptions: JmiException
 (InvalidCallException, InvalidNameException)
Specified by:
`refClass` in interface `javax.jmi.reflect.RefPackage`
refCreateStruct
public javax.jmi.reflect.RefStruct refCreateStruct(javax.jmi.reflect.RefObject structType,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) name)
Specified by:
`refCreateStruct` in interface `javax.jmi.reflect.RefPackage`
refCreateStruct
public javax.jmi.reflect.RefStruct refCreateStruct([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) structName,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) args)
The refCreateStruct operation creates an instance of a struct data type
 defined by the metaobject structType (or structName ) whose attribute
 values are specified by the ordered collection args . The members of the
 args list correspond 1-to-1 to the parameters for the specific create
 operation. They must be encoded as per Generation Rules for Parameters on
 page 56. InvalidCallException is raised if the structType parameter does
 not designate a struct type. InvalidNameException is raised when the
 structName does not denote a valid struct name. This refCreateStruct
 operations create a new instance of a struct data type. specific analog:
 create (...); return type: RefStruct parameters: RefObject
 structType (or String structName), List args exceptions: JmiException
 (WrongSizeException, TypeMismatchException, InvalidObjectException,
 InvalidCallException, InvalidNameException,
 java.lang.NullPointerException)
Specified by:
`refCreateStruct` in interface `javax.jmi.reflect.RefPackage`
refDelete
public void refDelete()
The "refDelete" operation destroys this package, including the objects it contains directly or transitively.
 Deletion of an outermost package causes all objects within its extent to be deleted.
Specified by:
`refDelete` in interface `javax.jmi.reflect.RefPackage`
refGetEnum
public javax.jmi.reflect.RefEnum refGetEnum(javax.jmi.reflect.RefObject enumType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) args)
Specified by:
`refGetEnum` in interface `javax.jmi.reflect.RefPackage`
refGetEnum
public javax.jmi.reflect.RefEnum refGetEnum([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) enumName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) args)
The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
 Note that the type of enumeration is defined by the meta object that owns
 the metaLiteral object. InvalidCallException is raised if the enumType
 parameter does not designate a valid enumeration. InvalidNameException is
 raised when the enumName does not denote a valid enum name. This
 refGetEnum returns the enumeration object representing the enumeration
 literal. specific analog: none. return type: RefEnum parameters:
 RefObject enumType (or String enumName ) String literalName exceptions:
 JmiException (TypeMismatchException, InvalidCallException,
 InvalidNameException, java.lang.NullPointerException)
Specified by:
`refGetEnum` in interface `javax.jmi.reflect.RefPackage`
refPackage
public javax.jmi.reflect.RefPackage refPackage(javax.jmi.reflect.RefObject nestedPackage)
Specified by:
`refPackage` in interface `javax.jmi.reflect.RefPackage`
refPackage
public javax.jmi.reflect.RefPackage refPackage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) nestedPackageName)
The "nestedPackage" (or nestedPackageName ) parameter should designate
 the package whose package object is to be returned. It must either be
 nested within the package for this package object, or imported with
 isCluster set to true. InvalidCallException is raised if the
 nestedPackage parameter does not designate a valid package.
 InvalidNameException is raised when the nestedPackageName does not denote
 a valid nested package name. The refPackage operations return a package
 object for a nested or clustered package. specific analog: get
 () return type: RefPackage isQuery: yes parameters:
 RefObject nestedPackage (or String nestedPackageName) exceptions:
 JmiException (InvalidCallException, InvalidNameException)
Specified by:
`refPackage` in interface `javax.jmi.reflect.RefPackage`
internalError
public void internalError([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string,
 javax.jmi.reflect.InvalidCallException ex)
Parameters:
`string` -
`ex` -
getMetaObjects
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html) getMetaObjects()
Returns:
addClass
public void addClass([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 javax.jmi.reflect.RefClass clazz)
Parameters:
`name` -
`clazz` -
removeClass
public void removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass clazz)
addPackage
public void addPackage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 javax.jmi.reflect.RefBaseObject pack)
Parameters:
`string` -
`basicBehaviorsPackage2` -
removePackage
public void removePackage(javax.jmi.reflect.RefBaseObject pack)
refAllPackages
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) refAllPackages()
Returns a (possible empty) collection of RefPackages directly contained
 by this package. 
 The Collection returned from this operation is an
 immutable collection. The refAllPackages
 operation returns all packages directly contained or clustered by this
 package. specific analog: None return type: Collection of RefPackages
 isQuery: yes parameters: None exceptions: JmiException
Specified by:
`refAllPackages` in interface `javax.jmi.reflect.RefPackage`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Class AbstractRefPackage">Class AbstractRefPackage</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.uml2.ext.jmi.MapOwner</code>, <code><a href="AbstractRefBaseObject.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRefBaseObject</a></code>, <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code>, <code><a href="EcoreRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">EcoreRefPackage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractRefPackage</span>
<span class="extends-implements">extends com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
implements javax.jmi.reflect.RefPackage</span></div>
<div class="block">The RefPackage interface is an abstraction for accessing a collection of
 objects and their associations. The interface provides an operation to access
 the meta object description for the package, and operations to access the
 package instance's class proxy objects and its association objects</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>mMetaObject, repository</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">AbstractRefPackage</a><wbr/>(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAssociation(java.lang.String,javax.jmi.reflect.RefAssociation)">addAssociation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 javax.jmi.reflect.RefAssociation assoc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addClass(java.lang.String,javax.jmi.reflect.RefClass)">addClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 javax.jmi.reflect.RefClass clazz)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPackage(java.lang.String,javax.jmi.reflect.RefBaseObject)">addPackage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 javax.jmi.reflect.RefBaseObject pack)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaObjects()">getMetaObjects</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalError(java.lang.String,javax.jmi.reflect.InvalidCallException)">internalError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 javax.jmi.reflect.InvalidCallException ex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refAllAssociations()">refAllAssociations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The  refAllAssociation  operation returns all associations directly contained by this package.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refAllClasses()">refAllClasses</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The  refAllClasses  operation returns all class proxies directly contained by this package.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refAllPackages()">refAllPackages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a (possible empty) collection of RefPackages directly contained
 by this package.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefAssociation</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refAssociation(java.lang.String)">refAssociation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> associationName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The association (or associationName ) parameter should designate the (M2)
 association whose association object is to be returned.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefAssociation</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refAssociation(javax.jmi.reflect.RefObject)">refAssociation</a><wbr/>(javax.jmi.reflect.RefObject association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refClass(java.lang.String)">refClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> className)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The type (or className ) parameter should designate the class whose class
 proxy object is to be returned.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refClass(javax.jmi.reflect.RefObject)">refClass</a><wbr/>(javax.jmi.reflect.RefObject type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefStruct</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refCreateStruct(java.lang.String,java.util.List)">refCreateStruct</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> structName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> args)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The refCreateStruct operation creates an instance of a struct data type
 defined by the metaobject structType (or structName ) whose attribute
 values are specified by the ordered collection args .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefStruct</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refCreateStruct(javax.jmi.reflect.RefObject,java.util.List)">refCreateStruct</a><wbr/>(javax.jmi.reflect.RefObject structType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refDelete()">refDelete</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The "refDelete" operation destroys this package, including the objects it contains directly or transitively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefEnum</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refGetEnum(java.lang.String,java.lang.String)">refGetEnum</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> enumName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> args)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefEnum</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refGetEnum(javax.jmi.reflect.RefObject,java.lang.String)">refGetEnum</a><wbr/>(javax.jmi.reflect.RefObject enumType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> args)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefPackage</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refPackage(java.lang.String)">refPackage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> nestedPackageName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The "nestedPackage" (or nestedPackageName ) parameter should designate
 the package whose package object is to be returned.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefPackage</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refPackage(javax.jmi.reflect.RefObject)">refPackage</a><wbr/>(javax.jmi.reflect.RefObject nestedPackage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass)">removeClass</a><wbr/>(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass clazz)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePackage(javax.jmi.reflect.RefBaseObject)">removePackage</a><wbr/>(javax.jmi.reflect.RefBaseObject pack)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>getRepository, mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">
<h3>AbstractRefPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractRefPackage</span><wbr/><span class="parameters">(@CheckForNull
 <a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>repository</code> - </dd>
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
<section class="detail" id="addAssociation(java.lang.String,javax.jmi.reflect.RefAssociation)">
<h3>addAssociation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAssociation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 javax.jmi.reflect.RefAssociation assoc)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - </dd>
<dd><code>assoc</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refAllAssociations()">
<h3>refAllAssociations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">refAllAssociations</span>()</div>
<div class="block">The  refAllAssociation  operation returns all associations directly contained by this package.
 Returns a (possible empty) collection of RefAssociations directly contained by this package.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refAllAssociations</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refAllClasses()">
<h3>refAllClasses</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">refAllClasses</span>()</div>
<div class="block">The  refAllClasses  operation returns all class proxies directly contained by this package.
 Returns a (possible empty) collection of RefClasses directly contained by this package.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refAllClasses</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refAssociation(javax.jmi.reflect.RefObject)">
<h3>refAssociation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefAssociation</span> <span class="element-name">refAssociation</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject association)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refAssociation</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refAssociation(java.lang.String)">
<h3>refAssociation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefAssociation</span> <span class="element-name">refAssociation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> associationName)</span></div>
<div class="block">The association (or associationName ) parameter should designate the (M2)
 association whose association object is to be returned. The
 refAssociation operations return an association object for a given
 association. specific analog: get <associationname>() return type:
 RefAssociation isQuery: yes parameters: RefObject association (or String
 associationName) exceptions: JmiException (InvalidCallException,
 InvalidNameException)</associationname></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refAssociation</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refClass(javax.jmi.reflect.RefObject)">
<h3>refClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefClass</span> <span class="element-name">refClass</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject type)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refClass</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refClass(java.lang.String)">
<h3>refClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefClass</span> <span class="element-name">refClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> className)</span></div>
<div class="block">The type (or className ) parameter should designate the class whose class
 proxy object is to be returned. InvalidCallException is raised if the
 type parameter does not designate a valid class. InvalidNameException is
 raised when the className does not denote a valid class name. The
 refClass operations return the class proxy object for a given class.
 specific analog: get <classname>() return type: RefClass isQuery: yes
 parameters: RefObject type (or String className) exceptions: JmiException
 (InvalidCallException, InvalidNameException)</classname></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refClass</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refCreateStruct(javax.jmi.reflect.RefObject,java.util.List)">
<h3>refCreateStruct</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefStruct</span> <span class="element-name">refCreateStruct</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject structType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> name)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refCreateStruct</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refCreateStruct(java.lang.String,java.util.List)">
<h3>refCreateStruct</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefStruct</span> <span class="element-name">refCreateStruct</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> structName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> args)</span></div>
<div class="block">The refCreateStruct operation creates an instance of a struct data type
 defined by the metaobject structType (or structName ) whose attribute
 values are specified by the ordered collection args . The members of the
 args list correspond 1-to-1 to the parameters for the specific create
 operation. They must be encoded as per Generation Rules for Parameters on
 page 56. InvalidCallException is raised if the structType parameter does
 not designate a struct type. InvalidNameException is raised when the
 structName does not denote a valid struct name. This refCreateStruct
 operations create a new instance of a struct data type. specific analog:
 create <struct>(...); return type: RefStruct parameters: RefObject
 structType (or String structName), List args exceptions: JmiException
 (WrongSizeException, TypeMismatchException, InvalidObjectException,
 InvalidCallException, InvalidNameException,
 java.lang.NullPointerException)</struct></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refCreateStruct</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refDelete()">
<h3>refDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">refDelete</span>()</div>
<div class="block">The "refDelete" operation destroys this package, including the objects it contains directly or transitively.
 Deletion of an outermost package causes all objects within its extent to be deleted.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refDelete</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refGetEnum(javax.jmi.reflect.RefObject,java.lang.String)">
<h3>refGetEnum</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefEnum</span> <span class="element-name">refGetEnum</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject enumType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> args)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refGetEnum</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refGetEnum(java.lang.String,java.lang.String)">
<h3>refGetEnum</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefEnum</span> <span class="element-name">refGetEnum</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> enumName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> args)</span></div>
<div class="block">The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
 Note that the type of enumeration is defined by the meta object that owns
 the metaLiteral object. InvalidCallException is raised if the enumType
 parameter does not designate a valid enumeration. InvalidNameException is
 raised when the enumName does not denote a valid enum name. This
 refGetEnum returns the enumeration object representing the enumeration
 literal. specific analog: none. return type: RefEnum parameters:
 RefObject enumType (or String enumName ) String literalName exceptions:
 JmiException (TypeMismatchException, InvalidCallException,
 InvalidNameException, java.lang.NullPointerException)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refGetEnum</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refPackage(javax.jmi.reflect.RefObject)">
<h3>refPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefPackage</span> <span class="element-name">refPackage</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject nestedPackage)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refPackage</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refPackage(java.lang.String)">
<h3>refPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefPackage</span> <span class="element-name">refPackage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> nestedPackageName)</span></div>
<div class="block">The "nestedPackage" (or nestedPackageName ) parameter should designate
 the package whose package object is to be returned. It must either be
 nested within the package for this package object, or imported with
 isCluster set to true. InvalidCallException is raised if the
 nestedPackage parameter does not designate a valid package.
 InvalidNameException is raised when the nestedPackageName does not denote
 a valid nested package name. The refPackage operations return a package
 object for a nested or clustered package. specific analog: get
 <packagename>() return type: RefPackage isQuery: yes parameters:
 RefObject nestedPackage (or String nestedPackageName) exceptions:
 JmiException (InvalidCallException, InvalidNameException)</packagename></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refPackage</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalError(java.lang.String,javax.jmi.reflect.InvalidCallException)">
<h3>internalError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 javax.jmi.reflect.InvalidCallException ex)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - </dd>
<dd><code>ex</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaObjects()">
<h3>getMetaObjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getMetaObjects</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="addClass(java.lang.String,javax.jmi.reflect.RefClass)">
<h3>addClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 javax.jmi.reflect.RefClass clazz)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - </dd>
<dd><code>clazz</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass)">
<h3>removeClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeClass</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass clazz)</span></div>
</section>
</li>
<li>
<section class="detail" id="addPackage(java.lang.String,javax.jmi.reflect.RefBaseObject)">
<h3>addPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPackage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 javax.jmi.reflect.RefBaseObject pack)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - </dd>
<dd><code>basicBehaviorsPackage2</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePackage(javax.jmi.reflect.RefBaseObject)">
<h3>removePackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePackage</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject pack)</span></div>
</section>
</li>
<li>
<section class="detail" id="refAllPackages()">
<h3>refAllPackages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">refAllPackages</span>()</div>
<div class="block">Returns a (possible empty) collection of RefPackages directly contained
 by this package. 
 The Collection returned from this operation is an
 immutable collection. The refAllPackages
 operation returns all packages directly contained or clustered by this
 package. specific analog: None return type: Collection of RefPackages
 isQuery: yes parameters: None exceptions: JmiException</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refAllPackages</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
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
