# JAVA OPENAPI: MagicDrawProfile.DerivedPropertySpecificationStereotype (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/MagicDrawProfile.DerivedPropertySpecificationStereotype.html
- source_path: `com/nomagic/uml2/MagicDrawProfile.DerivedPropertySpecificationStereotype.html`
- source_sha256: `c07293c49dff125c1ee32544803189e2990caeb397457e8a4759e24828cd1a5b`
- captured_utc: `2026-07-14T16:56:10.801631+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2](package-summary.html)

## Class MagicDrawProfile.DerivedPropertySpecificationStereotype

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)
com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype

Enclosing class:
[MagicDrawProfile](MagicDrawProfile.html)

public static classMagicDrawProfile.DerivedPropertySpecificationStereotype
extends [ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXPRESSION](#EXPRESSION)`
List of different types of criteria how to gather dependent elements: Simple (UML Relation, Property or Tag); Meta Chain, OCL and Binary.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ISREADONLY](#ISREADONLY)`
If True, property is read only without ability to create target element.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEREOTYPE_NAME](#STEREOTYPE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALUESETTER](#VALUESETTER)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[DerivedPropertySpecificationStereotype](#%3Cinit%3E(com.nomagic.uml2.MagicDrawProfile))([MagicDrawProfile](MagicDrawProfile.html) profile)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addExpression](#addExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`protected void`
`[clear](#clear())()`

`void`
`[clearExpression](#clearExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearIsReadOnly](#clearIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearValueSetter](#clearValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getExpression](#getExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getExpressionProperty](#getExpressionProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getIsReadOnlyProperty](#getIsReadOnlyProperty())()`

`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Returns stereotype for this wrapper.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValueSetter](#getValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getValueSetterProperty](#getValueSetterProperty())()`

`boolean`
`[is](#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Checks if stereotype of this wrapper is applied to given element.
`static boolean`
`[isInstance](#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isIsReadOnly](#isIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[removeExpression](#removeExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[setExpression](#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> value)`

`void`
`[setIsReadOnly](#setIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setValueSetter](#setValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)
`[apply](../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getElement](../profiles/ProfileImplementation.StereotypeWrapper.html#getElement(com.nomagic.profiles.ProfileCache,java.lang.String)), [getTagByName](../profiles/ProfileImplementation.StereotypeWrapper.html#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [isDerivedStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isSameOrDerivedStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [toBoolean](../profiles/ProfileImplementation.StereotypeWrapper.html#toBoolean(java.lang.Object)), [toDouble](../profiles/ProfileImplementation.StereotypeWrapper.html#toDouble(java.lang.Object)), [toInteger](../profiles/ProfileImplementation.StereotypeWrapper.html#toInteger(java.lang.Object)), [toString](../profiles/ProfileImplementation.StereotypeWrapper.html#toString(java.lang.Object)), [unApply](../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STEREOTYPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.STEREOTYPE_NAME)
EXPRESSION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXPRESSION
List of different types of criteria how to gather dependent elements: Simple (UML Relation, Property or Tag); Meta Chain, OCL and Binary. If several criterion are defined results is union of all of them.
 Expression can be used in Derived Property Specification, Dependency Matrix, Dependency Map.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.EXPRESSION)
ISREADONLY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ISREADONLY
If True, property is read only without ability to create target element. If False Property is read / write with ability to create value according to defined expressions.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.ISREADONLY)
VALUESETTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALUESETTER
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.VALUESETTER)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DerivedPropertySpecificationStereotype
protected DerivedPropertySpecificationStereotype([MagicDrawProfile](MagicDrawProfile.html) profile)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())`
Returns stereotype for this wrapper.
Specified by:
`[getStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())` in class `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)`
Returns:
stereotype
getExpressionProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getExpressionProperty()
getIsReadOnlyProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getIsReadOnlyProperty()
getValueSetterProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getValueSetterProperty()
setExpression
public void setExpression([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> value)
clearExpression
public void clearExpression([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
addExpression
public void addExpression([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
removeExpression
public void removeExpression([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
getExpression
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getExpression([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setIsReadOnly
public void setIsReadOnly([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearIsReadOnly
public void clearIsReadOnly([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isIsReadOnly
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isIsReadOnly([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setValueSetter
public void setValueSetter([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearValueSetter
public void clearValueSetter([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getValueSetter
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValueSetter([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
clear
protected void clear()
is
public boolean is(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Checks if stereotype of this wrapper is applied to given element.
Specified by:
`[is](../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))` in class `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)`
Parameters:
`element` - element
Returns:
true if stereotype of this wrapper is applied to given element
isInstance
public static boolean isInstance(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2</a></div>
<h1 class="title" title="Class MagicDrawProfile.DerivedPropertySpecificationStereotype">Class MagicDrawProfile.DerivedPropertySpecificationStereotype</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation.StereotypeWrapper</a>
<div class="inheritance">com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">MagicDrawProfile.DerivedPropertySpecificationStereotype</span>
<span class="extends-implements">extends <a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXPRESSION">EXPRESSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of different types of criteria how to gather dependent elements: Simple (UML Relation, Property or Tag); Meta Chain, OCL and Binary.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ISREADONLY">ISREADONLY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If True, property is read only without ability to create target element.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STEREOTYPE_NAME">STEREOTYPE_NAME</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VALUESETTER">VALUESETTER</a></code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.MagicDrawProfile)">DerivedPropertySpecificationStereotype</a><wbr/>(<a href="MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a> profile)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">addExpression</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearExpression</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearIsReadOnly</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearValueSetter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getExpression</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExpressionProperty()">getExpressionProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIsReadOnlyProperty()">getIsReadOnlyProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype for this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getValueSetter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSetterProperty()">getValueSetterProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if stereotype of this wrapper is applied to given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstance</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isIsReadOnly</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">removeExpression</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setExpression</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setIsReadOnly</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setValueSetter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation.StereotypeWrapper">Methods inherited from class com.nomagic.profiles.<a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></h3>
<code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">apply</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getElement(com.nomagic.profiles.ProfileCache,java.lang.String)">getElement</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getTagByName</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isDerivedStereotype</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isSameOrDerivedStereotype</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toBoolean(java.lang.Object)">toBoolean</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toDouble(java.lang.Object)">toDouble</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toInteger(java.lang.Object)">toInteger</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toString(java.lang.Object)">toString</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">unApply</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="STEREOTYPE_NAME">
<h3>STEREOTYPE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEREOTYPE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXPRESSION">
<h3>EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXPRESSION</span></div>
<div class="block">List of different types of criteria how to gather dependent elements: Simple (UML Relation, Property or Tag); Meta Chain, OCL and Binary. If several criterion are defined results is union of all of them.
 <p>
 Expression can be used in Derived Property Specification, Dependency Matrix, Dependency Map.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ISREADONLY">
<h3>ISREADONLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ISREADONLY</span></div>
<div class="block">If True, property is read only without ability to create target element. If False Property is read / write with ability to create value according to defined expressions.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.ISREADONLY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUESETTER">
<h3>VALUESETTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALUESETTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.DerivedPropertySpecificationStereotype.VALUESETTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.MagicDrawProfile)">
<h3>DerivedPropertySpecificationStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">DerivedPropertySpecificationStereotype</span><wbr/><span class="parameters">(<a href="MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a> profile)</span></div>
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
<section class="detail" id="getStereotype()">
<h3>getStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Returns stereotype for this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">getStereotype</a></code> in class <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpressionProperty()">
<h3>getExpressionProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getExpressionProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getIsReadOnlyProperty()">
<h3>getIsReadOnlyProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getIsReadOnlyProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getValueSetterProperty()">
<h3>getValueSetterProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getValueSetterProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExpression</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearExpression</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>addExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addExpression</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>removeExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeExpression</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getExpression</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getExpression</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setIsReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIsReadOnly</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearIsReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearIsReadOnly</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isIsReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isIsReadOnly</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isIsReadOnly</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setValueSetter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValueSetter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearValueSetter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearValueSetter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getValueSetter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getValueSetter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueSetter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
</section>
</li>
<li>
<section class="detail" id="is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>is</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">is</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Checks if stereotype of this wrapper is applied to given element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a></code> in class <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if stereotype of this wrapper is applied to given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
