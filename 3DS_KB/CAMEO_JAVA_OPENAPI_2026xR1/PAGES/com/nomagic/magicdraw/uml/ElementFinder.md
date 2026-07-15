# JAVA OPENAPI: ElementFinder (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/ElementFinder.html
- source_path: `com/nomagic/magicdraw/uml/ElementFinder.html`
- source_sha256: `84d4a600d1b43110e978042c73553d128dcf5c2621fc9258f96389ea3f0dabaf`
- captured_utc: `2026-07-14T16:46:04.714862+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class ElementFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.ElementFinder

@OpenApiAll
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public classElementFinder
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Deprecated.
use [`Finder`](Finder.html)
This class is used for searching of some element in the model structure with given name.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementFinder](#%3Cinit%3E())()`
Deprecated.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Deprecated.
use [`Finder.byName()`](Finder.html#byName())
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren)`
Deprecated.
use [`Finder.byNameRecursively()`](Finder.html#byNameRecursively()) or [`Finder.byName()`](Finder.html#byName())
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren,
 boolean checkRoot)`
Deprecated.
use [`Finder.byNameRecursively()`](Finder.html#byNameRecursively()) or [`Finder.byName()`](Finder.html#byName())
`static void`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String,java.util.Collection,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) results,
 boolean searchInChildren)`
Deprecated.
use [`Finder.byNameAllRecursively()`](Finder.html#byNameAllRecursively()) or [`Finder.byNameAll()`](Finder.html#byNameAll())
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Deprecated.
use [`Finder.byName()`](Finder.html#byName())
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren)`
Deprecated.
use [`Finder.byName()`](Finder.html#byName()) or [`Finder.byNameRecursively()`](Finder.html#byNameRecursively())
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren,
 boolean checkRoot)`
Deprecated.
use [`Finder.byNameRecursively()`](Finder.html#byNameRecursively()) or [`Finder.byName()`](Finder.html#byName())
`static void`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,java.util.Collection,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) results,
 boolean searchInChildren)`
Deprecated.
use [`Finder.byNameAllRecursively()`](Finder.html#byNameAllRecursively()) or [`Finder.byNameAll()`](Finder.html#byNameAll())
`static void`
`[find](#find(java.util.Collection,java.lang.String,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) children,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) results)`
Deprecated.
use [`Finder.byName()`](Finder.html#byName())
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[getChildren](#getChildren(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 boolean checkParent)`
Deprecated.
use [`Finder.byType()`](Finder.html#byType())
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[getChildren](#getChildren(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 boolean recursively,
 boolean checkParent)`
Deprecated.
use [`Finder.byType()`](Finder.html#byType()) or [`Finder.byTypeRecursively()`](Finder.html#byTypeRecursively())
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementFinder
public ElementFinder()
Deprecated.
 ============ METHOD DETAIL ========== 
Method Details
find
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Deprecated.
use [`Finder.byName()`](Finder.html#byName())
Find element.
Parameters:
`root` - Root element.
`type` - Type of element.
`name` - Element name.
Returns:
Element.
find
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Deprecated.
use [`Finder.byName()`](Finder.html#byName())
Find element.
Parameters:
`root` - Root element.
`type` - Elements type list.
`name` - Element name.
Returns:
Element.
find
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren)
Deprecated.
use [`Finder.byName()`](Finder.html#byName()) or [`Finder.byNameRecursively()`](Finder.html#byNameRecursively())
Find element.
Parameters:
`root` - Root element.
`type` - Type of element.
`name` - Element name.
`searchInChildren` - Is search in children?
Returns:
Element.
find
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren)
Deprecated.
use [`Finder.byNameRecursively()`](Finder.html#byNameRecursively()) or [`Finder.byName()`](Finder.html#byName())
Find element.
Parameters:
`root` - Root element.
`type` - Element type list.
`name` - Element name.
`searchInChildren` - Is search in children?
Returns:
Element.
find
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren,
 boolean checkRoot)
Deprecated.
use [`Finder.byNameRecursively()`](Finder.html#byNameRecursively()) or [`Finder.byName()`](Finder.html#byName())
Find Element.
Parameters:
`root` - Root element.
`type` - Type of element.
`name` - Element name
`searchInChildren` - Is search in children?
`checkRoot` - Check with root element.
Returns:
Element.
find
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean searchInChildren,
 boolean checkRoot)
Deprecated.
use [`Finder.byNameRecursively()`](Finder.html#byNameRecursively()) or [`Finder.byName()`](Finder.html#byName())
Find Element
Parameters:
`root` - Root element.
`type` - Element type list.
`name` - Element name
`searchInChildren` - Is search in children?
`checkRoot` - Check with root element.
Returns:
Element.
find
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static void find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) results,
 boolean searchInChildren)
Deprecated.
use [`Finder.byNameAllRecursively()`](Finder.html#byNameAllRecursively()) or [`Finder.byNameAll()`](Finder.html#byNameAll())
Find Element.
Parameters:
`root` - Root Element.
`type` - Type of element.
`name` - Element name.
`results` - The matched element.
`searchInChildren` - Is search in children?
find
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static void find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) results,
 boolean searchInChildren)
Deprecated.
use [`Finder.byNameAllRecursively()`](Finder.html#byNameAllRecursively()) or [`Finder.byNameAll()`](Finder.html#byNameAll())
Find Element.
Parameters:
`root` - Root Element.
`type` - Element type list.
`name` - Element name.
`results` - The matched element.
`searchInChildren` - Is search in children?
find
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static void find([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) children,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) results)
Deprecated.
use [`Finder.byName()`](Finder.html#byName())
Find Element.
Parameters:
`children` - children
`name` - Element name.
`results` - The matched element.
getChildren
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) getChildren([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 boolean checkParent)
Deprecated.
use [`Finder.byType()`](Finder.html#byType())
Use this method if you don`t want to search recursively.
 It checks if parent has owned elements if yes checks if elements are specified type
 if yes adds them.
 If needs checks parent and adds it to list.
Parameters:
`parent` - Root Element.
`type` - Element type list.
`checkParent` - is need to check parent?
Returns:
Collection of elements.
getChildren
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) getChildren([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] type,
 boolean recursively,
 boolean checkParent)
Deprecated.
use [`Finder.byType()`](Finder.html#byType()) or [`Finder.byTypeRecursively()`](Finder.html#byTypeRecursively())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class ElementFinder">Class ElementFinder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.ElementFinder</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementFinder</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html" title="class in com.nomagic.magicdraw.uml"><code>Finder</code></a></div>
</div>
<div class="block">This class is used for searching of some element in the model structure with given name.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementFinder</a>()</code></div>
<div class="col-last even-row-color">
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a> or <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String,boolean,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren,
 boolean checkRoot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a> or <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,java.lang.String,java.util.Collection,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results,
 boolean searchInChildren)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameAllRecursively()"><code>Finder.byNameAllRecursively()</code></a> or <a href="Finder.html#byNameAll()"><code>Finder.byNameAll()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a> or <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,boolean,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren,
 boolean checkRoot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a> or <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,java.util.Collection,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results,
 boolean searchInChildren)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameAllRecursively()"><code>Finder.byNameAllRecursively()</code></a> or <a href="Finder.html#byNameAll()"><code>Finder.byNameAll()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.String,java.util.Collection)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> children,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getChildren(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean)">getChildren</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean checkParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byType()"><code>Finder.byType()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getChildren(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean,boolean)">getChildren</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean recursively,
 boolean checkParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byType()"><code>Finder.byType()</code></a> or <a href="Finder.html#byTypeRecursively()"><code>Finder.byTypeRecursively()</code></a></div>
</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>ElementFinder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementFinder</span>()</div>
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
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
<div class="block">Find element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root element.</dd>
<dd><code>type</code> - Type of element.</dd>
<dd><code>name</code> - Element name.</dd>
<dt>Returns:</dt>
<dd>Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],java.lang.String)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
<div class="block">Find element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root element.</dd>
<dd><code>type</code> - Elements type list.</dd>
<dd><code>name</code> - Element name.</dd>
<dt>Returns:</dt>
<dd>Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a> or <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a></div>
</div>
<div class="block">Find element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root element.</dd>
<dd><code>type</code> - Type of element.</dd>
<dd><code>name</code> - Element name.</dd>
<dd><code>searchInChildren</code> - Is search in children?</dd>
<dt>Returns:</dt>
<dd>Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],java.lang.String,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a> or <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
<div class="block">Find element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root element.</dd>
<dd><code>type</code> - Element type list.</dd>
<dd><code>name</code> - Element name.</dd>
<dd><code>searchInChildren</code> - Is search in children?</dd>
<dt>Returns:</dt>
<dd>Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,boolean,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren,
 boolean checkRoot)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a> or <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
<div class="block">Find Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root element.</dd>
<dd><code>type</code> - Type of element.</dd>
<dd><code>name</code> - Element name</dd>
<dd><code>searchInChildren</code> - Is search in children?</dd>
<dd><code>checkRoot</code> - Check with root element.</dd>
<dt>Returns:</dt>
<dd>Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],java.lang.String,boolean,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean searchInChildren,
 boolean checkRoot)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameRecursively()"><code>Finder.byNameRecursively()</code></a> or <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
<div class="block">Find Element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root element.</dd>
<dd><code>type</code> - Element type list.</dd>
<dd><code>name</code> - Element name</dd>
<dd><code>searchInChildren</code> - Is search in children?</dd>
<dd><code>checkRoot</code> - Check with root element.</dd>
<dt>Returns:</dt>
<dd>Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,java.lang.String,java.util.Collection,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results,
 boolean searchInChildren)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameAllRecursively()"><code>Finder.byNameAllRecursively()</code></a> or <a href="Finder.html#byNameAll()"><code>Finder.byNameAll()</code></a></div>
</div>
<div class="block">Find Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root Element.</dd>
<dd><code>type</code> - Type of element.</dd>
<dd><code>name</code> - Element name.</dd>
<dd><code>results</code> - The matched element.</dd>
<dd><code>searchInChildren</code> - Is search in children?</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],java.lang.String,java.util.Collection,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results,
 boolean searchInChildren)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byNameAllRecursively()"><code>Finder.byNameAllRecursively()</code></a> or <a href="Finder.html#byNameAll()"><code>Finder.byNameAll()</code></a></div>
</div>
<div class="block">Find Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - Root Element.</dd>
<dd><code>type</code> - Element type list.</dd>
<dd><code>name</code> - Element name.</dd>
<dd><code>results</code> - The matched element.</dd>
<dd><code>searchInChildren</code> - Is search in children?</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.String,java.util.Collection)">
<h3>find</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> children,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> results)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byName()"><code>Finder.byName()</code></a></div>
</div>
<div class="block">Find Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>children</code> - children</dd>
<dd><code>name</code> - Element name.</dd>
<dd><code>results</code> - The matched element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildren(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],boolean)">
<h3>getChildren</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getChildren</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean checkParent)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byType()"><code>Finder.byType()</code></a></div>
</div>
<div class="block">Use this method if you don`t want to search recursively.
 It checks if parent has owned elements if yes checks if elements are specified type
 if yes adds them.
 If needs checks parent and adds it to list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - Root Element.</dd>
<dd><code>type</code> - Element type list.</dd>
<dd><code>checkParent</code> - is need to check parent?</dd>
<dt>Returns:</dt>
<dd>Collection of elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildren(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],boolean,boolean)">
<h3>getChildren</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getChildren</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean recursively,
 boolean checkParent)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Finder.html#byType()"><code>Finder.byType()</code></a> or <a href="Finder.html#byTypeRecursively()"><code>Finder.byTypeRecursively()</code></a></div>
</div>
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
