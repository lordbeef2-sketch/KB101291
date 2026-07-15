# JAVA OPENAPI: FilterSettings (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/dependencymatrix/persistence/FilterSettings.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/persistence/FilterSettings.html`
- source_sha256: `7f40b4cd503d84ab618a70387ef986f5a89d83acb0adeca865180326ed4588c4`
- captured_utc: `2026-07-14T16:51:17.302149+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.persistence](package-summary.html)

## Class FilterSettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.persistence.FilterSettings

All Implemented Interfaces:
`com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`

@OpenApiAllpublic abstract classFilterSettings
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings

Provides generic ability to access row or column filter settings.
 
 Settings are stored directly in the Dependency Matrix diagram element, and retrieved directly

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FilterSettings](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Initializes access to the filter settings element
`[FilterSettings](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) filterStereotype)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static <T> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T>`
`[castList](#castList(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) listValue)`
Checks if provided list is not EmptyList.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getAdditionalElements](#getAdditionalElements())()`
Additional scope elements setting
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getElementTypes](#getElementTypes())()`
Element types for rows/columns
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementTypesTagName](#getElementTypesTagName())()`
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
`protected [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getFilterStereotype](#getFilterStereotype())()`

`protected [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getMatrixElement](#getMatrixElement())()`

`[Project](../../core/Project.html)`
`[getProject](#getProject())()`
Project of these settings
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getPropertyFilter](#getPropertyFilter())()`
Dependency Matrix Property filter property
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPropertyFilterTagName](#getPropertyFilterTagName())()`
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getQueryExpression](#getQueryExpression())()`

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getQueryTagName](#getQueryTagName())()`
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRemovedElements](#getRemovedElements())()`
Dependency matrix removed element property
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemovedElementsTagName](#getRemovedElementsTagName())()`
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getScope](#getScope())()`
Deprecated.
use com.nomagic.magicdraw.dependencymatrix.persistence.FilterSettings#getScopeRoots()
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getScopeDefinedTagName](#getScopeDefinedTagName())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getScopeRoots](#getScopeRoots())()`
Root elements of the scope.
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getScopeTagName](#getScopeTagName())()`
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTypesIncludeCustomTypes](#getTypesIncludeCustomTypes())()`
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTypesIncludeSubtypes](#getTypesIncludeSubtypes())()`
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
`boolean`
`[isElementTypesDefined](#isElementTypesDefined())()`

`boolean`
`[isIncludeAdditionalContent](#isIncludeAdditionalContent())()`

`boolean`
`[isRemoveChildrenOfRemovedElements](#isRemoveChildrenOfRemovedElements())()`
Indicates if children of removed elements should be removed too.
`boolean`
`[isScopeDefined](#isScopeDefined())()`

`boolean`
`[isTypesIncludeCustomTypes](#isTypesIncludeCustomTypes())()`
Include custom types element filter property
`boolean`
`[isTypesIncludeSubtypes](#isTypesIncludeSubtypes())()`
Include subtypes element filter property
`void`
`[setConvertedElementTypes](#setConvertedElementTypes(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> types)`
Converts element types and saves them as the diagram setting
`void`
`[setElementTypes](#setElementTypes(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> types)`
Set element types for diagram
`void`
`[setIncludeAdditionalContent](#setIncludeAdditionalContent(boolean))(boolean includeAdditionalContent)`

`void`
`[setPropertyFilter](#setPropertyFilter(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> propertyFilter)`
Dependency Matrix Property filter property
`void`
`[setQueryExpression](#setQueryExpression(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) expression)`

`void`
`[setRemovedElements](#setRemovedElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> removedElements)`
update Dependency matrix removed element property
`void`
`[setScope](#setScope(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)`
Dependency matrix scope property
`void`
`[setScopeDefined](#setScopeDefined(boolean))(boolean confirmed)`
Set scope confirmation flag
`void`
`[setTypesIncludeCustomTypes](#setTypesIncludeCustomTypes(boolean))(boolean includeCustomTypes)`
Include subtypes element filter property
`void`
`[setTypesIncludeSubtypes](#setTypesIncludeSubtypes(boolean))(boolean includeSubtypes)`
Include subtypes element filter property
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings
`getName`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FilterSettings
public FilterSettings([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Initializes access to the filter settings element
Parameters:
`diagram` - matrix diagram
FilterSettings
public FilterSettings([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) filterStereotype)
 ============ METHOD DETAIL ========== 
Method Details
castList
public static <T> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> castList([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) listValue)
Checks if provided list is not EmptyList. If so - returns new list. Otherwise - returns the same list
Parameters:
`listValue` - checked list
Returns:
list or new list
getElementTypes
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getElementTypes()
Element types for rows/columns
Specified by:
`getElementTypes` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
ist of metaclass or stereotype instance
isElementTypesDefined
public boolean isElementTypesDefined()
Specified by:
`isElementTypesDefined` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
when true and getElementTypes() is empty, means that elements of any type can be in the scope.
 when false and getElementTypes() is empty, means that no types are accepted so the scope is empty
setElementTypes
public void setElementTypes([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> types)
Set element types for diagram
Parameters:
`types` - list of metaclass or stereotype instance
setConvertedElementTypes
public void setConvertedElementTypes([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> types)
Converts element types and saves them as the diagram setting
Parameters:
`types` - element types
getScopeRoots
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getScopeRoots()
Description copied from interface: `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Root elements of the scope. Those elements and their children can be included into the scope
Specified by:
`getScopeRoots` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
scope root elements, used when collecting all elements in the scope
getScope
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getScope()
Deprecated.
use com.nomagic.magicdraw.dependencymatrix.persistence.FilterSettings#getScopeRoots()
setScope
public void setScope([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)
Dependency matrix scope property
Parameters:
`scope` - scope element collection
getRemovedElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRemovedElements()
Dependency matrix removed element property
Specified by:
`getRemovedElements` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
element removed from the scope
isRemoveChildrenOfRemovedElements
public boolean isRemoveChildrenOfRemovedElements()
Description copied from interface: `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Indicates if children of removed elements should be removed too.
Specified by:
`isRemoveChildrenOfRemovedElements` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
true if children of removed elements should be removed.
setRemovedElements
public void setRemovedElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> removedElements)
update Dependency matrix removed element property
Parameters:
`removedElements` - element removed from the scope
isTypesIncludeSubtypes
public boolean isTypesIncludeSubtypes()
Include subtypes element filter property
Specified by:
`isTypesIncludeSubtypes` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
true if all subtypes should be accepted
setTypesIncludeSubtypes
public void setTypesIncludeSubtypes(boolean includeSubtypes)
Include subtypes element filter property
Parameters:
`includeSubtypes` - if all subtypes should be accepted
isTypesIncludeCustomTypes
public boolean isTypesIncludeCustomTypes()
Include custom types element filter property
Specified by:
`isTypesIncludeCustomTypes` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
true if all subtypes should be accepted
setTypesIncludeCustomTypes
public void setTypesIncludeCustomTypes(boolean includeCustomTypes)
Include subtypes element filter property
Parameters:
`includeCustomTypes` - if all custom types should be accepted
getPropertyFilter
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getPropertyFilter()
Dependency Matrix Property filter property
Specified by:
`getPropertyFilter` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
property filter values
setPropertyFilter
public void setPropertyFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> propertyFilter)
Dependency Matrix Property filter property
Parameters:
`propertyFilter` - property filter values
setQueryExpression
public void setQueryExpression(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) expression)
Parameters:
`expression` - query string expression
getElementTypesTagName
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementTypesTagName()
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
Returns:
tag name
getScopeTagName
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getScopeTagName()
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
Returns:
tag name
getRemovedElementsTagName
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemovedElementsTagName()
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
Returns:
tag name
getTypesIncludeSubtypes
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTypesIncludeSubtypes()
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
Returns:
tag name
getTypesIncludeCustomTypes
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTypesIncludeCustomTypes()
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
Returns:
tag name
getPropertyFilterTagName
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPropertyFilterTagName()
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
Returns:
tag name
getScopeDefinedTagName
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getScopeDefinedTagName()
getQueryTagName
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getQueryTagName()
Stereotype tag name of the dependency matrix filter stereotype, used to get the property value
Returns:
tag name
getFilterStereotype
protected [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getFilterStereotype()
getMatrixElement
protected [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) getMatrixElement()
getProject
public [Project](../../core/Project.html) getProject()
Description copied from interface: `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Project of these settings
Specified by:
`getProject` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
project
setScopeDefined
public void setScopeDefined(boolean confirmed)
Set scope confirmation flag
Parameters:
`confirmed` - flag value
isScopeDefined
public boolean isScopeDefined()
Specified by:
`isScopeDefined` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
true if scope is defined. If scope is empty and defined, it means whole project.
setIncludeAdditionalContent
public void setIncludeAdditionalContent(boolean includeAdditionalContent)
isIncludeAdditionalContent
public boolean isIncludeAdditionalContent()
Specified by:
`isIncludeAdditionalContent` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
true if it should retrieve additional content when collecting elements.
getQueryExpression
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getQueryExpression()
Specified by:
`getQueryExpression` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
getAdditionalElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getAdditionalElements()
Description copied from interface: `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Additional scope elements setting
Specified by:
`getAdditionalElements` in interface `com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings`
Returns:
additionally added elements to the scope

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.persistence</a></div>
<h1 class="title" title="Class FilterSettings">Class FilterSettings</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.persistence.FilterSettings</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">FilterSettings</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</span></div>
<div class="block">Provides generic ability to access row or column filter settings.
 <p></p>
 Settings are stored directly in the Dependency Matrix diagram element, and retrieved directly</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">FilterSettings</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color">
<div class="block">Initializes access to the filter settings element</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">FilterSettings</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> filterStereotype)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#castList(java.util.List)">castList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> listValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if provided list is not EmptyList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalElements()">getAdditionalElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Additional scope elements setting</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementTypes()">getElementTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Element types for rows/columns</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementTypesTagName()">getElementTypesTagName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilterStereotype()">getFilterStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMatrixElement()">getMatrixElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Project of these settings</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyFilter()">getPropertyFilter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency Matrix Property filter property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPropertyFilterTagName()">getPropertyFilterTagName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQueryExpression()">getQueryExpression</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getQueryTagName()">getQueryTagName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemovedElements()">getRemovedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency matrix removed element property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRemovedElementsTagName()">getRemovedElementsTagName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getScope()">getScope</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use com.nomagic.magicdraw.dependencymatrix.persistence.FilterSettings#getScopeRoots()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getScopeDefinedTagName()">getScopeDefinedTagName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getScopeRoots()">getScopeRoots</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Root elements of the scope.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getScopeTagName()">getScopeTagName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTypesIncludeCustomTypes()">getTypesIncludeCustomTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTypesIncludeSubtypes()">getTypesIncludeSubtypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementTypesDefined()">isElementTypesDefined</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIncludeAdditionalContent()">isIncludeAdditionalContent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemoveChildrenOfRemovedElements()">isRemoveChildrenOfRemovedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if children of removed elements should be removed too.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isScopeDefined()">isScopeDefined</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypesIncludeCustomTypes()">isTypesIncludeCustomTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Include custom types element filter property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypesIncludeSubtypes()">isTypesIncludeSubtypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Include subtypes element filter property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConvertedElementTypes(java.util.List)">setConvertedElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts element types and saves them as the diagram setting</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElementTypes(java.util.List)">setElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; types)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set element types for diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIncludeAdditionalContent(boolean)">setIncludeAdditionalContent</a><wbr/>(boolean includeAdditionalContent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyFilter(java.util.List)">setPropertyFilter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyFilter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency Matrix Property filter property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setQueryExpression(java.lang.String)">setQueryExpression</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRemovedElements(java.util.Collection)">setRemovedElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; removedElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update Dependency matrix removed element property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setScope(java.util.Collection)">setScope</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency matrix scope property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setScopeDefined(boolean)">setScopeDefined</a><wbr/>(boolean confirmed)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set scope confirmation flag</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTypesIncludeCustomTypes(boolean)">setTypesIncludeCustomTypes</a><wbr/>(boolean includeCustomTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Include subtypes element filter property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTypesIncludeSubtypes(boolean)">setTypesIncludeSubtypes</a><wbr/>(boolean includeSubtypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Include subtypes element filter property</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings">Methods inherited from interface com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</h3>
<code>getName</code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>FilterSettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FilterSettings</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Initializes access to the filter settings element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - matrix diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>FilterSettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FilterSettings</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> filterStereotype)</span></div>
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
<section class="detail" id="castList(java.util.List)">
<h3>castList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">castList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> listValue)</span></div>
<div class="block">Checks if provided list is not EmptyList. If so - returns new list. Otherwise - returns the same list</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listValue</code> - checked list</dd>
<dt>Returns:</dt>
<dd>list or new list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementTypes()">
<h3>getElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElementTypes</span>()</div>
<div class="block">Element types for rows/columns</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getElementTypes</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>ist of metaclass or stereotype instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementTypesDefined()">
<h3>isElementTypesDefined</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementTypesDefined</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isElementTypesDefined</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>when true and getElementTypes() is empty, means that elements of any type can be in the scope.
 when false and getElementTypes() is empty, means that no types are accepted so the scope is empty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElementTypes(java.util.List)">
<h3>setElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElementTypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; types)</span></div>
<div class="block">Set element types for diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>types</code> - list of metaclass or stereotype instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConvertedElementTypes(java.util.List)">
<h3>setConvertedElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConvertedElementTypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; types)</span></div>
<div class="block">Converts element types and saves them as the diagram setting</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>types</code> - element types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScopeRoots()">
<h3>getScopeRoots</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getScopeRoots</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></span></div>
<div class="block">Root elements of the scope. Those elements and their children can be included into the scope</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getScopeRoots</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>scope root elements, used when collecting all elements in the scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScope()">
<h3>getScope</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getScope</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use com.nomagic.magicdraw.dependencymatrix.persistence.FilterSettings#getScopeRoots()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="setScope(java.util.Collection)">
<h3>setScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setScope</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</span></div>
<div class="block">Dependency matrix scope property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scope</code> - scope element collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemovedElements()">
<h3>getRemovedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRemovedElements</span>()</div>
<div class="block">Dependency matrix removed element property</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getRemovedElements</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>element removed from the scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemoveChildrenOfRemovedElements()">
<h3>isRemoveChildrenOfRemovedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemoveChildrenOfRemovedElements</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></span></div>
<div class="block">Indicates if children of removed elements should be removed too.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isRemoveChildrenOfRemovedElements</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>true if children of removed elements should be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRemovedElements(java.util.Collection)">
<h3>setRemovedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRemovedElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; removedElements)</span></div>
<div class="block">update Dependency matrix removed element property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>removedElements</code> - element removed from the scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypesIncludeSubtypes()">
<h3>isTypesIncludeSubtypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypesIncludeSubtypes</span>()</div>
<div class="block">Include subtypes element filter property</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isTypesIncludeSubtypes</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>true if all subtypes should be accepted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTypesIncludeSubtypes(boolean)">
<h3>setTypesIncludeSubtypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTypesIncludeSubtypes</span><wbr/><span class="parameters">(boolean includeSubtypes)</span></div>
<div class="block">Include subtypes element filter property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includeSubtypes</code> - if all subtypes should be accepted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypesIncludeCustomTypes()">
<h3>isTypesIncludeCustomTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypesIncludeCustomTypes</span>()</div>
<div class="block">Include custom types element filter property</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isTypesIncludeCustomTypes</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>true if all subtypes should be accepted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTypesIncludeCustomTypes(boolean)">
<h3>setTypesIncludeCustomTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTypesIncludeCustomTypes</span><wbr/><span class="parameters">(boolean includeCustomTypes)</span></div>
<div class="block">Include subtypes element filter property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includeCustomTypes</code> - if all custom types should be accepted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyFilter()">
<h3>getPropertyFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getPropertyFilter</span>()</div>
<div class="block">Dependency Matrix Property filter property</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getPropertyFilter</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>property filter values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertyFilter(java.util.List)">
<h3>setPropertyFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertyFilter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyFilter)</span></div>
<div class="block">Dependency Matrix Property filter property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyFilter</code> - property filter values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setQueryExpression(java.lang.String)">
<h3>setQueryExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setQueryExpression</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - query string expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementTypesTagName()">
<h3>getElementTypesTagName</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementTypesTagName</span>()</div>
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tag name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScopeTagName()">
<h3>getScopeTagName</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getScopeTagName</span>()</div>
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tag name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemovedElementsTagName()">
<h3>getRemovedElementsTagName</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemovedElementsTagName</span>()</div>
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tag name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypesIncludeSubtypes()">
<h3>getTypesIncludeSubtypes</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTypesIncludeSubtypes</span>()</div>
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tag name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypesIncludeCustomTypes()">
<h3>getTypesIncludeCustomTypes</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTypesIncludeCustomTypes</span>()</div>
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tag name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyFilterTagName()">
<h3>getPropertyFilterTagName</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyFilterTagName</span>()</div>
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tag name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScopeDefinedTagName()">
<h3>getScopeDefinedTagName</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getScopeDefinedTagName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getQueryTagName()">
<h3>getQueryTagName</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQueryTagName</span>()</div>
<div class="block">Stereotype tag name of the dependency matrix filter stereotype, used to get the property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tag name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFilterStereotype()">
<h3>getFilterStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFilterStereotype</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMatrixElement()">
<h3>getMatrixElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">getMatrixElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></span></div>
<div class="block">Project of these settings</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getProject</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setScopeDefined(boolean)">
<h3>setScopeDefined</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setScopeDefined</span><wbr/><span class="parameters">(boolean confirmed)</span></div>
<div class="block">Set scope confirmation flag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>confirmed</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isScopeDefined()">
<h3>isScopeDefined</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isScopeDefined</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isScopeDefined</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>true if scope is defined. If scope is empty and defined, it means whole project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIncludeAdditionalContent(boolean)">
<h3>setIncludeAdditionalContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIncludeAdditionalContent</span><wbr/><span class="parameters">(boolean includeAdditionalContent)</span></div>
</section>
</li>
<li>
<section class="detail" id="isIncludeAdditionalContent()">
<h3>isIncludeAdditionalContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIncludeAdditionalContent</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isIncludeAdditionalContent</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>true if it should retrieve additional content when collecting elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQueryExpression()">
<h3>getQueryExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQueryExpression</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getQueryExpression</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdditionalElements()">
<h3>getAdditionalElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getAdditionalElements</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></span></div>
<div class="block">Additional scope elements setting</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getAdditionalElements</code> in interface <code>com.nomagic.magicdraw.ui.diagrams.scope.ScopeSettings</code></dd>
<dt>Returns:</dt>
<dd>additionally added elements to the scope</dd>
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
