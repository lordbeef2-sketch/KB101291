# JAVA OPENAPI: StereotypeByProfileCache (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/helpers/StereotypeByProfileCache.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/StereotypeByProfileCache.html`
- source_sha256: `a6480443d22431709aac652c06027bf2522d84aa587a36bec4b9f7b006c5c725`
- captured_utc: `2026-07-14T16:56:16.107689+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class StereotypeByProfileCache

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[Project](../../../../magicdraw/core/Project.html)>
com.nomagic.magicdraw.core.project.service.ProjectService
com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApiAllpublic abstract classStereotypeByProfileCache
extends com.nomagic.magicdraw.core.project.service.ProjectService

Deprecated.
Profile should extend [`ProfileImplementation`](../../../../profiles/ProfileImplementation.html). Re-generate the profile class using
 "Generate Profile Class Implementation" action from the Development Tools plugin

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`protected static class`
`[StereotypeByProfileCache.AbstractElementWrapper](StereotypeByProfileCache.AbstractElementWrapper.html)<[ELEMENT](StereotypeByProfileCache.AbstractElementWrapper.html) extends [Element](../../magicdraw/classes/mdkernel/Element.html)>`
Deprecated.
`protected static class`
`[StereotypeByProfileCache.AbstractEnumerationWrapper](StereotypeByProfileCache.AbstractEnumerationWrapper.html)`
Deprecated.
`protected static class`
`[StereotypeByProfileCache.AbstractStereotypeWrapper](StereotypeByProfileCache.AbstractStereotypeWrapper.html)`
Deprecated.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[StereotypeByProfileCache](#%3Cinit%3E(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../../../magicdraw/core/Project.html) prj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)`
Deprecated.
`protected`
`[StereotypeByProfileCache](#%3Cinit%3E(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String))([Project](../../../../magicdraw/core/Project.html) prj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileURI)`
Deprecated.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected void`
`[clearCache](#clearCache())()`
Deprecated.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[StereotypeByProfileCache.AbstractElementWrapper](StereotypeByProfileCache.AbstractElementWrapper.html)>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`
Deprecated.
Generated method for getting all stereotype wrappers contained within this profile.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`
Deprecated.
Generated method for getting all stereotypes contained within this profile.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)>`
`[getAllStereotypes](#getAllStereotypes())()`
Deprecated.
Gets all stereotypes contained within this profile.
`[DataType](../../magicdraw/classes/mdkernel/DataType.html)`
`[getDataType](#getDataType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Deprecated.
`protected static <S extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService,
T extends [Project](../../../../magicdraw/core/Project.html)> 
S`
`[getInternalInstance](#getInternalInstance(java.lang.Class,T))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<S> key,
 T project)`
Deprecated.
This is only used for backwards compatibility with previously used `AbstractProjectService`
 

`return getOrCreateInstance(MyProfile.class, MyProfile::new, project);`
 

 or
 

`getOrCreateInstanceWithNullSupport(MyProfile.class, MyProfile::new, project);`
 

 should be used in place of this
`[Profile](../../magicdraw/mdprofiles/Profile.html)`
`[getProfile](#getProfile())()`
Deprecated.
`[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Deprecated.
`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Deprecated.
Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype).
`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Deprecated.
Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype).
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StereotypeByProfileCache
protected StereotypeByProfileCache([Project](../../../../magicdraw/core/Project.html) prj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName)
Deprecated.
StereotypeByProfileCache
protected StereotypeByProfileCache([Project](../../../../magicdraw/core/Project.html) prj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) profileURI)
Deprecated.
 ============ METHOD DETAIL ========== 
Method Details
getInternalInstance
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)protected static <S extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService,
T extends [Project](../../../../magicdraw/core/Project.html)>
S getInternalInstance([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<S> key,
 @CheckForNull
 T project)
Deprecated.
This is only used for backwards compatibility with previously used `AbstractProjectService`
 

`return getOrCreateInstance(MyProfile.class, MyProfile::new, project);`
 

 or
 

`getOrCreateInstanceWithNullSupport(MyProfile.class, MyProfile::new, project);`
 

 should be used in place of this
getStereotype
@CheckForNullpublic [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getStereotype([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Deprecated.
getDataType
@CheckForNullpublic [DataType](../../magicdraw/classes/mdkernel/DataType.html) getDataType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Deprecated.
getProfile
@CheckForNullpublic [Profile](../../magicdraw/mdprofiles/Profile.html) getProfile()
Deprecated.
getAllStereotypes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> getAllStereotypes()
Deprecated.
Gets all stereotypes contained within this profile.
Returns:
unmodifiable collection containing all stereotypes within this profile.
generatedGetAllStereotypes
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()
Deprecated.
Generated method for getting all stereotypes contained within this profile.
Returns:
gets all stereotypes contained within this profile.
generatedGetAllElementWrappers
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[StereotypeByProfileCache.AbstractElementWrapper](StereotypeByProfileCache.AbstractElementWrapper.html)> generatedGetAllElementWrappers()
Deprecated.
Generated method for getting all stereotype wrappers contained within this profile.
Returns:
gets all stereotype wrappers contained within this profile.
isTypeOf
public boolean isTypeOf([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Deprecated.
Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype). Caches value of this check
Parameters:
`element` - element
`stereotypeName` - stereotype
Returns:
true if element has assigned given stereotype
clearCache
protected void clearCache()
Deprecated.
isTypeOf
public boolean isTypeOf([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Deprecated.
Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype). Caches value of this check
Parameters:
`element` - element
`stereotype` - stereotype
Returns:
true if element has assigned given stereotype

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class StereotypeByProfileCache">Class StereotypeByProfileCache</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.core.project.service.ProjectService
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.StereotypeByProfileCache</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">StereotypeByProfileCache</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.project.service.ProjectService</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Profile should extend <a href="../../../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles"><code>ProfileImplementation</code></a>. Re-generate the profile class using
 "Generate Profile Class Implementation" action from the Development Tools plugin</div>
</div>
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
<div class="col-first even-row-color"><code>protected static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StereotypeByProfileCache.AbstractElementWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractElementWrapper</a>&lt;<a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="type parameter in StereotypeByProfileCache.AbstractElementWrapper">ELEMENT</a> extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="StereotypeByProfileCache.AbstractEnumerationWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractEnumerationWrapper</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StereotypeByProfileCache.AbstractStereotypeWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractStereotypeWrapper</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project,java.lang.String)">StereotypeByProfileCache</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String)">StereotypeByProfileCache</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileURI)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#clearCache()">clearCache</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractElementWrapper</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getAllStereotypes()">getAllStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Gets all stereotypes contained within this profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDataType(java.lang.String)">getDataType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>protected static &lt;S extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService,<wbr/>
T extends <a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;<br/>S</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInternalInstance(java.lang.Class,T)">getInternalInstance</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;S&gt; key,
 T project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">This is only used for backwards compatibility with previously used <code>AbstractProjectService</code>
<br/>
<code>return getOrCreateInstance(MyProfile.class, MyProfile::new, project);</code>
<br/>
 or
 <br/>
<code>getOrCreateInstanceWithNullSupport(MyProfile.class, MyProfile::new, project);</code>
<br/>
 should be used in place of this</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getProfile()">getProfile</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotype(java.lang.String)">getStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isTypeOf</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isTypeOf</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype).</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>StereotypeByProfileCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">StereotypeByProfileCache</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String)">
<h3>StereotypeByProfileCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">StereotypeByProfileCache</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> profileURI)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
<section class="detail" id="getInternalInstance(java.lang.Class,T)">
<h3 id="getInternalInstance(java.lang.Class,com.nomagic.magicdraw.core.Project)">getInternalInstance</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">protected static</span> <span class="type-parameters-long">&lt;S extends com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService,<wbr/>
T extends <a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;</span>
<span class="return-type">S</span> <span class="element-name">getInternalInstance</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;S&gt; key,
 @CheckForNull
 T project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">This is only used for backwards compatibility with previously used <code>AbstractProjectService</code>
<br/>
<code>return getOrCreateInstance(MyProfile.class, MyProfile::new, project);</code>
<br/>
 or
 <br/>
<code>getOrCreateInstanceWithNullSupport(MyProfile.class, MyProfile::new, project);</code>
<br/>
 should be used in place of this</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getStereotype(java.lang.String)">
<h3>getStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getDataType(java.lang.String)">
<h3>getDataType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></span> <span class="element-name">getDataType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getProfile()">
<h3>getProfile</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">getProfile</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getAllStereotypes()">
<h3>getAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getAllStereotypes</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Gets all stereotypes contained within this profile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>unmodifiable collection containing all stereotypes within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>gets all stereotypes contained within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="StereotypeByProfileCache.AbstractElementWrapper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">StereotypeByProfileCache.AbstractElementWrapper</a>&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>gets all stereotype wrappers contained within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype). Caches value of this check</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotypeName</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>true if element has assigned given stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCache()">
<h3>clearCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clearCache</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if given Element is type of given Stereotype (has assigned stereotype or some derived stereotype). Caches value of this check</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>true if element has assigned given stereotype</dd>
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
