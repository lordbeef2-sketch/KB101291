# JAVA OPENAPI: SelectElementTypes (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/dialogs/SelectElementTypes.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/SelectElementTypes.html`
- source_sha256: `649ea6e94d2aa98bed0789e00218be87bef6d832057af577cf1a67bfe8f86aa0`
- captured_utc: `2026-07-14T16:58:25.347149+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs](package-summary.html)

## Class SelectElementTypes

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dialogs.SelectElementTypes

@OpenApiAllpublic classSelectElementTypes
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Element types for element(s) selection dialog.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[create](#create)`
The types (metaclasses) of elements or stereotypes that can be created in the select element
 dialog.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[display](#display)`
The types (metaclasses) of elements that should be displayed in the select element dialog.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[restricted](#restricted)`
The types (metaclasses) of elements or stereotypes that restricts the element selection.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[select](#select)`
The types (metaclasses) of elements that can be selected in the select element dialog.
`boolean`
`[usedAsTypes](#usedAsTypes)`
The result will be used as "type", so possible elements should be filtered by DSL engine doNotSuggestAsType flag.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SelectElementTypes](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean))([ElementListProperty](../../properties/ElementListProperty.html) property,
 boolean creatable)`

`[SelectElementTypes](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean,boolean))([ElementListProperty](../../properties/ElementListProperty.html) property,
 boolean creatable,
 boolean appendOwnersToCreatable)`

`[SelectElementTypes](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean))([ElementProperty](../../properties/ElementProperty.html) property,
 boolean creatable)`

`[SelectElementTypes](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean,boolean))([ElementProperty](../../properties/ElementProperty.html) property,
 boolean creatable,
 boolean appendOwnersToCreatable)`

`[SelectElementTypes](#%3Cinit%3E(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select)`

`[SelectElementTypes](#%3Cinit%3E(java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`

`[SelectElementTypes](#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create)`
Constructor.
`[SelectElementTypes](#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create,
 boolean appendOwnersToCreatable)`
Constructor.
`[SelectElementTypes](#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted)`
Constructor.
`[SelectElementTypes](#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection,java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 boolean appendOwnersToCreatable)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [SelectElementTypes](SelectElementTypes.html)`
`[create](#create(com.nomagic.magicdraw.properties.Property,boolean))([Property](../../properties/Property.html) property,
 boolean creatable)`
An utility method to create an instance for given property.
`static [SelectElementTypes](SelectElementTypes.html)`
`[create](#create(com.nomagic.magicdraw.properties.Property,boolean,boolean))([Property](../../properties/Property.html) property,
 boolean creatable,
 boolean appendOwnersToCreatable)`
An utility method to create an instance for given property.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[getRestricted](#getRestricted())()`

`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[getSelect](#getSelect())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
display
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display
The types (metaclasses) of elements that should be displayed in the select element dialog.
select
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select
The types (metaclasses) of elements that can be selected in the select element dialog.
create
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create
The types (metaclasses) of elements or stereotypes that can be created in the select element
 dialog. Stereotype means that element with the applied stereotype will be created.
restricted
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted
The types (metaclasses) of elements or stereotypes that restricts the element selection. If
 the restricted element is stereotype - only element that has applied this stereotype can be
 selected.
usedAsTypes
public boolean usedAsTypes
The result will be used as "type", so possible elements should be filtered by DSL engine doNotSuggestAsType flag.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SelectElementTypes
public SelectElementTypes([ElementProperty](../../properties/ElementProperty.html) property,
 boolean creatable)
SelectElementTypes
public SelectElementTypes([ElementProperty](../../properties/ElementProperty.html) property,
 boolean creatable,
 boolean appendOwnersToCreatable)
SelectElementTypes
public SelectElementTypes([ElementListProperty](../../properties/ElementListProperty.html) property,
 boolean creatable)
SelectElementTypes
public SelectElementTypes([ElementListProperty](../../properties/ElementListProperty.html) property,
 boolean creatable,
 boolean appendOwnersToCreatable)
SelectElementTypes
public SelectElementTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select)
SelectElementTypes
public SelectElementTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 @CheckForNull
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
SelectElementTypes
public SelectElementTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create)
Constructor.
Parameters:
`display` - [`display`](#display) value.
`select` - [`select`](#select) value.
`create` - [`create`](#create) value.
SelectElementTypes
public SelectElementTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create,
 boolean appendOwnersToCreatable)
Constructor.
Parameters:
`display` - [`display`](#display) value.
`select` - [`select`](#select) value.
`create` - [`create`](#create) value.
`appendOwnersToCreatable` - true if possible owners should be added into creatable metaclasses
SelectElementTypes
public SelectElementTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted)
Constructor.
Parameters:
`display` - [`display`](#display) value.
`select` - [`select`](#select) value.
`create` - [`create`](#create) value.
`restricted` - [`restricted`](#restricted) value.
SelectElementTypes
public SelectElementTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) display,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) select,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) create,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 boolean appendOwnersToCreatable)
Constructor.
Parameters:
`display` - [`display`](#display) value.
`select` - [`select`](#select) value.
`create` - [`create`](#create) value.
`restricted` - [`restricted`](#restricted) value.
`appendOwnersToCreatable` - true if possible owners should be added into creatable metaclasses
 ============ METHOD DETAIL ========== 
Method Details
getSelect
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) getSelect()
getRestricted
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) getRestricted()
create
@CheckForNullpublic static [SelectElementTypes](SelectElementTypes.html) create([Property](../../properties/Property.html) property,
 boolean creatable)
An utility method to create an instance for given property.
Parameters:
`property` - the given property
`creatable` - true if elements must be allowed to create
Returns:
a new instance in case property is ElementProperty or Element ListProperty or null
See Also:
[`SelectElementTypes(com.nomagic.magicdraw.properties.ElementProperty, boolean)`](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean))
[`SelectElementTypes(com.nomagic.magicdraw.properties.ElementListProperty, boolean)`](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean))
create
@CheckForNullpublic static [SelectElementTypes](SelectElementTypes.html) create([Property](../../properties/Property.html) property,
 boolean creatable,
 boolean appendOwnersToCreatable)
An utility method to create an instance for given property.
Parameters:
`property` - the given property
`creatable` - true if elements must be allowed to create
`appendOwnersToCreatable` - true if possible owners should be added into creatable metaclasses
Returns:
a new instance in case property is ElementProperty or Element ListProperty or null
See Also:
[`SelectElementTypes(com.nomagic.magicdraw.properties.ElementProperty, boolean)`](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean))
[`SelectElementTypes(com.nomagic.magicdraw.properties.ElementListProperty, boolean)`](#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs</a></div>
<h1 class="title" title="Class SelectElementTypes">Class SelectElementTypes</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.SelectElementTypes</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SelectElementTypes</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Element types for element(s) selection dialog.</div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#create">create</a></code></div>
<div class="col-last even-row-color">
<div class="block">The types (metaclasses) of elements or stereotypes that can be created in the select element
 dialog.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#display">display</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The types (metaclasses) of elements that should be displayed in the select element dialog.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restricted">restricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The types (metaclasses) of elements or stereotypes that restricts the element selection.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#select">select</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The types (metaclasses) of elements that can be selected in the select element dialog.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#usedAsTypes">usedAsTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">The result will be used as "type", so possible elements should be filtered by DSL engine doNotSuggestAsType flag.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean)">SelectElementTypes</a><wbr/>(<a href="../../properties/ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> property,
 boolean creatable)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean,boolean)">SelectElementTypes</a><wbr/>(<a href="../../properties/ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> property,
 boolean creatable,
 boolean appendOwnersToCreatable)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean)">SelectElementTypes</a><wbr/>(<a href="../../properties/ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> property,
 boolean creatable)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean,boolean)">SelectElementTypes</a><wbr/>(<a href="../../properties/ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> property,
 boolean creatable,
 boolean appendOwnersToCreatable)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection)">SelectElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">SelectElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection)">SelectElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection,boolean)">SelectElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create,
 boolean appendOwnersToCreatable)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection,java.util.Collection)">SelectElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Collection,java.util.Collection,boolean)">SelectElementTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 boolean appendOwnersToCreatable)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.nomagic.magicdraw.properties.Property,boolean)">create</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean creatable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">An utility method to create an instance for given property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.nomagic.magicdraw.properties.Property,boolean,boolean)">create</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean creatable,
 boolean appendOwnersToCreatable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">An utility method to create an instance for given property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRestricted()">getRestricted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelect()">getSelect</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="display">
<h3>display</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">display</span></div>
<div class="block">The types (metaclasses) of elements that should be displayed in the select element dialog.</div>
</section>
</li>
<li>
<section class="detail" id="select">
<h3>select</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">select</span></div>
<div class="block">The types (metaclasses) of elements that can be selected in the select element dialog.</div>
</section>
</li>
<li>
<section class="detail" id="create">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">create</span></div>
<div class="block">The types (metaclasses) of elements or stereotypes that can be created in the select element
 dialog. Stereotype means that element with the applied stereotype will be created.</div>
</section>
</li>
<li>
<section class="detail" id="restricted">
<h3>restricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">restricted</span></div>
<div class="block">The types (metaclasses) of elements or stereotypes that restricts the element selection. If
 the restricted element is stereotype - only element that has applied this stereotype can be
 selected.</div>
</section>
</li>
<li>
<section class="detail" id="usedAsTypes">
<h3>usedAsTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">usedAsTypes</span></div>
<div class="block">The result will be used as "type", so possible elements should be filtered by DSL engine doNotSuggestAsType flag.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.ElementProperty,boolean)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(<a href="../../properties/ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> property,
 boolean creatable)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.ElementProperty,boolean,boolean)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(<a href="../../properties/ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> property,
 boolean creatable,
 boolean appendOwnersToCreatable)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.ElementListProperty,boolean)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(<a href="../../properties/ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> property,
 boolean creatable)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.ElementListProperty,boolean,boolean)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(<a href="../../properties/ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> property,
 boolean creatable,
 boolean appendOwnersToCreatable)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection,java.util.Collection)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>display</code> - <a href="#display"><code>display</code></a> value.</dd>
<dd><code>select</code> - <a href="#select"><code>select</code></a> value.</dd>
<dd><code>create</code> - <a href="#create"><code>create</code></a> value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection,java.util.Collection,boolean)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create,
 boolean appendOwnersToCreatable)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>display</code> - <a href="#display"><code>display</code></a> value.</dd>
<dd><code>select</code> - <a href="#select"><code>select</code></a> value.</dd>
<dd><code>create</code> - <a href="#create"><code>create</code></a> value.</dd>
<dd><code>appendOwnersToCreatable</code> - true if possible owners should be added into creatable metaclasses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection,java.util.Collection,java.util.Collection)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>display</code> - <a href="#display"><code>display</code></a> value.</dd>
<dd><code>select</code> - <a href="#select"><code>select</code></a> value.</dd>
<dd><code>create</code> - <a href="#create"><code>create</code></a> value.</dd>
<dd><code>restricted</code> - <a href="#restricted"><code>restricted</code></a> value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection,java.util.Collection,java.util.Collection,boolean)">
<h3>SelectElementTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SelectElementTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> display,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> select,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> create,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 boolean appendOwnersToCreatable)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>display</code> - <a href="#display"><code>display</code></a> value.</dd>
<dd><code>select</code> - <a href="#select"><code>select</code></a> value.</dd>
<dd><code>create</code> - <a href="#create"><code>create</code></a> value.</dd>
<dd><code>restricted</code> - <a href="#restricted"><code>restricted</code></a> value.</dd>
<dd><code>appendOwnersToCreatable</code> - true if possible owners should be added into creatable metaclasses</dd>
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
<section class="detail" id="getSelect()">
<h3>getSelect</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getSelect</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRestricted()">
<h3>getRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getRestricted</span>()</div>
</section>
</li>
<li>
<section class="detail" id="create(com.nomagic.magicdraw.properties.Property,boolean)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean creatable)</span></div>
<div class="block">An utility method to create an instance for given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - the given property</dd>
<dd><code>creatable</code> - true if elements must be allowed to create</dd>
<dt>Returns:</dt>
<dd>a new instance in case property is ElementProperty or Element ListProperty or null</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean)"><code>SelectElementTypes(com.nomagic.magicdraw.properties.ElementProperty, boolean)</code></a></li>
<li><a href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean)"><code>SelectElementTypes(com.nomagic.magicdraw.properties.ElementListProperty, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(com.nomagic.magicdraw.properties.Property,boolean,boolean)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean creatable,
 boolean appendOwnersToCreatable)</span></div>
<div class="block">An utility method to create an instance for given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - the given property</dd>
<dd><code>creatable</code> - true if elements must be allowed to create</dd>
<dd><code>appendOwnersToCreatable</code> - true if possible owners should be added into creatable metaclasses</dd>
<dt>Returns:</dt>
<dd>a new instance in case property is ElementProperty or Element ListProperty or null</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementProperty,boolean)"><code>SelectElementTypes(com.nomagic.magicdraw.properties.ElementProperty, boolean)</code></a></li>
<li><a href="#%3Cinit%3E(com.nomagic.magicdraw.properties.ElementListProperty,boolean)"><code>SelectElementTypes(com.nomagic.magicdraw.properties.ElementListProperty, boolean)</code></a></li>
</ul>
</dd>
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
