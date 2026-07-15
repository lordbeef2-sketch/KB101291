# JAVA OPENAPI: DisplayPathElements.DisplayPathOptions (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/DisplayPathElements.DisplayPathOptions.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DisplayPathElements.DisplayPathOptions.html`
- source_sha256: `9cbea868353d0910455cb3312a1c3392a3227a6ed1553e80f278ac43b4dce4fd`
- captured_utc: `2026-07-14T16:55:55.893463+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class DisplayPathElements.DisplayPathOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.DisplayPathElements.DisplayPathOptions

Enclosing class:
[DisplayPathElements](DisplayPathElements.html)

public static final classDisplayPathElements.DisplayPathOptions
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Display path elements options

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DisplayPathOptions](#%3Cinit%3E())()`
Default options.
`[DisplayPathOptions](#%3Cinit%3E(boolean,boolean,boolean,boolean))(boolean displayRelationships,
 boolean createTrees,
 boolean displayContainmentLinks,
 boolean displayNoteAnchors)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<com.dassault_systemes.modeler.foundation.model.ModelElement>`
`[getElementFilter](#getElementFilter())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[getOnlyBetweenThese](#getOnlyBetweenThese())()`

`com.nomagic.utils.TriFunction<com.dassault_systemes.modeler.foundation.model.ModelElement,[PresentationElement](PresentationElement.html),[PresentationElement](PresentationElement.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)>`
`[getRelationshipFilter](#getRelationshipFilter())()`

`boolean`
`[isCreateTrees](#isCreateTrees())()`

`boolean`
`[isDisplayContainmentLinks](#isDisplayContainmentLinks())()`

`boolean`
`[isDisplayNoteAnchors](#isDisplayNoteAnchors())()`

`boolean`
`[isDisplayPathsToSelf](#isDisplayPathsToSelf())()`

`boolean`
`[isDisplayRelationships](#isDisplayRelationships())()`

`void`
`[setCreateTrees](#setCreateTrees(boolean))(boolean createTrees)`
Display trees
`void`
`[setDisplayContainmentLinks](#setDisplayContainmentLinks(boolean))(boolean displayContainmentLinks)`
Display Containment links
`void`
`[setDisplayNoteAnchors](#setDisplayNoteAnchors(boolean))(boolean displayNoteAnchors)`
Display Note Anchors
`void`
`[setDisplayPathsToSelf](#setDisplayPathsToSelf(boolean))(boolean displayPathsToSelf)`
Display paths to self
`void`
`[setDisplayRelationships](#setDisplayRelationships(boolean))(boolean displayRelationships)`
Display Relationships (all connected Relationships in the model)
`void`
`[setElementFilter](#setElementFilter(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<com.dassault_systemes.modeler.foundation.model.ModelElement> elementFilter)`
Set filter for model elements
`void`
`[setOnlyBetweenThese](#setOnlyBetweenThese(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> onlyBetweenThese)`
Display paths only among given symbols.
`void`
`[setRelationshipFilter](#setRelationshipFilter(com.nomagic.utils.TriFunction))(com.nomagic.utils.TriFunction<com.dassault_systemes.modeler.foundation.model.ModelElement,[PresentationElement](PresentationElement.html),[PresentationElement](PresentationElement.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> relationshipFilter)`
Set Relationships filter
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DisplayPathOptions
public DisplayPathOptions()
Default options. Trees, containment links and note anchors will be displayed
DisplayPathOptions
public DisplayPathOptions(boolean displayRelationships,
 boolean createTrees,
 boolean displayContainmentLinks,
 boolean displayNoteAnchors)
Constructor
Parameters:
`createTrees` - create trees for Generalizations, InterfaceRealizations
`displayContainmentLinks` - display Containment links
`displayNoteAnchors` - display Note Anchors
 ============ METHOD DETAIL ========== 
Method Details
isDisplayRelationships
public boolean isDisplayRelationships()
Returns:
true if relationships should be displayed
setDisplayRelationships
public void setDisplayRelationships(boolean displayRelationships)
Display Relationships (all connected Relationships in the model)
Parameters:
`displayRelationships` - value
isCreateTrees
public boolean isCreateTrees()
Returns:
true if trees should be displayed
setCreateTrees
public void setCreateTrees(boolean createTrees)
Display trees
Parameters:
`createTrees` - flag
isDisplayContainmentLinks
public boolean isDisplayContainmentLinks()
Returns:
true if containment links should be displayed
setDisplayContainmentLinks
public void setDisplayContainmentLinks(boolean displayContainmentLinks)
Display Containment links
Parameters:
`displayContainmentLinks` - value
isDisplayNoteAnchors
public boolean isDisplayNoteAnchors()
Returns:
true if note anchors should be displayed
setDisplayNoteAnchors
public void setDisplayNoteAnchors(boolean displayNoteAnchors)
Display Note Anchors
Parameters:
`displayNoteAnchors` - value
getOnlyBetweenThese
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> getOnlyBetweenThese()
Returns:
paths will be created only among given symbols. If null, paths will be created among any symbols in the diagram
setOnlyBetweenThese
public void setOnlyBetweenThese(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> onlyBetweenThese)
Display paths only among given symbols.
Parameters:
`onlyBetweenThese` - paths will be created only among given symbols. If null, paths will be created among any symbols in the diagram
isDisplayPathsToSelf
public boolean isDisplayPathsToSelf()
Returns:
true if paths to self should be displayed
setDisplayPathsToSelf
public void setDisplayPathsToSelf(boolean displayPathsToSelf)
Display paths to self
Parameters:
`displayPathsToSelf` - value
setElementFilter
public void setElementFilter(@CheckForNull
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<com.dassault_systemes.modeler.foundation.model.ModelElement> elementFilter)
Set filter for model elements
Parameters:
`elementFilter` - predicate
getElementFilter
@CheckForNullpublic [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<com.dassault_systemes.modeler.foundation.model.ModelElement> getElementFilter()
Returns:
filter for elements
setRelationshipFilter
public void setRelationshipFilter(com.nomagic.utils.TriFunction<com.dassault_systemes.modeler.foundation.model.ModelElement,[PresentationElement](PresentationElement.html),[PresentationElement](PresentationElement.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> relationshipFilter)
Set Relationships filter
Parameters:
`relationshipFilter` - triFunction
getRelationshipFilter
public com.nomagic.utils.TriFunction<com.dassault_systemes.modeler.foundation.model.ModelElement,[PresentationElement](PresentationElement.html),[PresentationElement](PresentationElement.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> getRelationshipFilter()
Returns:
filter for relationships

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class DisplayPathElements.DisplayPathOptions">Class DisplayPathElements.DisplayPathOptions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.DisplayPathElements.DisplayPathOptions</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="DisplayPathElements.html" title="class in com.nomagic.magicdraw.uml.symbols">DisplayPathElements</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">DisplayPathElements.DisplayPathOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Display path elements options</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DisplayPathOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default options.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean,boolean,boolean,boolean)">DisplayPathOptions</a><wbr/>(boolean displayRelationships,
 boolean createTrees,
 boolean displayContainmentLinks,
 boolean displayNoteAnchors)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementFilter()">getElementFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOnlyBetweenThese()">getOnlyBetweenThese</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.utils.TriFunction&lt;com.dassault_systemes.modeler.foundation.model.ModelElement,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipFilter()">getRelationshipFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateTrees()">isCreateTrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayContainmentLinks()">isDisplayContainmentLinks</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayNoteAnchors()">isDisplayNoteAnchors</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayPathsToSelf()">isDisplayPathsToSelf</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayRelationships()">isDisplayRelationships</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateTrees(boolean)">setCreateTrees</a><wbr/>(boolean createTrees)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display trees</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayContainmentLinks(boolean)">setDisplayContainmentLinks</a><wbr/>(boolean displayContainmentLinks)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display Containment links</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayNoteAnchors(boolean)">setDisplayNoteAnchors</a><wbr/>(boolean displayNoteAnchors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display Note Anchors</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayPathsToSelf(boolean)">setDisplayPathsToSelf</a><wbr/>(boolean displayPathsToSelf)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display paths to self</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayRelationships(boolean)">setDisplayRelationships</a><wbr/>(boolean displayRelationships)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display Relationships (all connected Relationships in the model)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElementFilter(java.util.function.Predicate)">setElementFilter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt; elementFilter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set filter for model elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOnlyBetweenThese(java.util.Collection)">setOnlyBetweenThese</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; onlyBetweenThese)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display paths only among given symbols.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRelationshipFilter(com.nomagic.utils.TriFunction)">setRelationshipFilter</a><wbr/>(com.nomagic.utils.TriFunction&lt;com.dassault_systemes.modeler.foundation.model.ModelElement,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; relationshipFilter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Relationships filter</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>DisplayPathOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DisplayPathOptions</span>()</div>
<div class="block">Default options. Trees, containment links and note anchors will be displayed</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean,boolean,boolean,boolean)">
<h3>DisplayPathOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DisplayPathOptions</span><wbr/><span class="parameters">(boolean displayRelationships,
 boolean createTrees,
 boolean displayContainmentLinks,
 boolean displayNoteAnchors)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>createTrees</code> - create trees for Generalizations, InterfaceRealizations</dd>
<dd><code>displayContainmentLinks</code> - display Containment links</dd>
<dd><code>displayNoteAnchors</code> - display Note Anchors</dd>
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
<section class="detail" id="isDisplayRelationships()">
<h3>isDisplayRelationships</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayRelationships</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if relationships should be displayed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayRelationships(boolean)">
<h3>setDisplayRelationships</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayRelationships</span><wbr/><span class="parameters">(boolean displayRelationships)</span></div>
<div class="block">Display Relationships (all connected Relationships in the model)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayRelationships</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateTrees()">
<h3>isCreateTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateTrees</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if trees should be displayed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateTrees(boolean)">
<h3>setCreateTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateTrees</span><wbr/><span class="parameters">(boolean createTrees)</span></div>
<div class="block">Display trees</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>createTrees</code> - flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayContainmentLinks()">
<h3>isDisplayContainmentLinks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayContainmentLinks</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if containment links should be displayed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayContainmentLinks(boolean)">
<h3>setDisplayContainmentLinks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayContainmentLinks</span><wbr/><span class="parameters">(boolean displayContainmentLinks)</span></div>
<div class="block">Display Containment links</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayContainmentLinks</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayNoteAnchors()">
<h3>isDisplayNoteAnchors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayNoteAnchors</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if note anchors should be displayed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayNoteAnchors(boolean)">
<h3>setDisplayNoteAnchors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayNoteAnchors</span><wbr/><span class="parameters">(boolean displayNoteAnchors)</span></div>
<div class="block">Display Note Anchors</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayNoteAnchors</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOnlyBetweenThese()">
<h3>getOnlyBetweenThese</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getOnlyBetweenThese</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>paths will be created only among given symbols. If null, paths will be created among any symbols in the diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOnlyBetweenThese(java.util.Collection)">
<h3>setOnlyBetweenThese</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOnlyBetweenThese</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; onlyBetweenThese)</span></div>
<div class="block">Display paths only among given symbols.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>onlyBetweenThese</code> - paths will be created only among given symbols. If null, paths will be created among any symbols in the diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayPathsToSelf()">
<h3>isDisplayPathsToSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayPathsToSelf</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if paths to self should be displayed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayPathsToSelf(boolean)">
<h3>setDisplayPathsToSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayPathsToSelf</span><wbr/><span class="parameters">(boolean displayPathsToSelf)</span></div>
<div class="block">Display paths to self</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayPathsToSelf</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElementFilter(java.util.function.Predicate)">
<h3>setElementFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElementFilter</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt; elementFilter)</span></div>
<div class="block">Set filter for model elements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementFilter</code> - predicate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementFilter()">
<h3>getElementFilter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</span> <span class="element-name">getElementFilter</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>filter for elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRelationshipFilter(com.nomagic.utils.TriFunction)">
<h3>setRelationshipFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRelationshipFilter</span><wbr/><span class="parameters">(com.nomagic.utils.TriFunction&lt;com.dassault_systemes.modeler.foundation.model.ModelElement,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; relationshipFilter)</span></div>
<div class="block">Set Relationships filter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationshipFilter</code> - triFunction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationshipFilter()">
<h3>getRelationshipFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.utils.TriFunction&lt;com.dassault_systemes.modeler.foundation.model.ModelElement,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</span> <span class="element-name">getRelationshipFilter</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>filter for relationships</dd>
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
