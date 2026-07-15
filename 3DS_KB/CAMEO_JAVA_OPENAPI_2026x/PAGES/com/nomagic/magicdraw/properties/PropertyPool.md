# JAVA OPENAPI: PropertyPool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/properties/PropertyPool.html
- source_path: `com/nomagic/magicdraw/properties/PropertyPool.html`
- source_sha256: `83116e20bc3a579a577f4c4e4abaecae826b1fdacafbbf8b4785e4346f6bef18`
- captured_utc: `2026-07-14T16:58:00.627566+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class PropertyPool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.properties.PropertyPool

@OpenApiAllpublic classPropertyPool
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
This is a pool of the properties. Use this pool if you do not want to create a lot of instance of properties
 with the same ID and value.
 Be careful with changing the value of property taken from this pool. Property is mutable object!!!

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PropertyPool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [BooleanProperty](BooleanProperty.html)`
`[getBooleanProperty](#getBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty))([BooleanProperty](BooleanProperty.html) p)`
Returns shared instance of boolean property with the same id and value as given property.
`static [BooleanProperty](BooleanProperty.html)`
`[getBooleanProperty](#getBooleanProperty(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 boolean value)`
Returns shared instance of boolean property with the given id and value.
`static [BooleanProperty](BooleanProperty.html)`
`[getBooleanProperty](#getBooleanProperty(java.lang.String,boolean,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 boolean value,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)`
Returns shared instance of boolean property with the given id and value.
`static [ChoiceProperty](ChoiceProperty.html)`
`[getChoiceProperty](#getChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty))([ChoiceProperty](ChoiceProperty.html) p)`
Returns shared instance of choice property with the same id and value as given property.
`static [ChoiceProperty](ChoiceProperty.html)`
`[getChoiceProperty](#getChoiceProperty(java.lang.String,java.lang.Object,java.util.List))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) possibleValues)`
Returns shared instance of choice property with the given id, value and possible values for selection
`static [ChoiceProperty](ChoiceProperty.html)`
`[getChoiceProperty](#getChoiceProperty(java.lang.String,java.lang.Object,java.util.List,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) possibleValues,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)`
Returns shared instance of choice property with the given id, group, value and possible values for selection
`static [ColorProperty](ColorProperty.html)`
`[getColorProperty](#getColorProperty(com.nomagic.magicdraw.properties.ColorProperty))([ColorProperty](ColorProperty.html) p)`
Returns shared instance of color property with the same id and value as given property.
`static [ColorProperty](ColorProperty.html)`
`[getColorProperty](#getColorProperty(java.lang.String,java.awt.Color))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) value)`
Returns shared instance of color property with the given id and value.
`static [ColorProperty](ColorProperty.html)`
`[getColorProperty](#getColorProperty(java.lang.String,java.awt.Color,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) value,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)`
Returns shared instance of color property with the given id and value.
`static [FontProperty](FontProperty.html)`
`[getFontProperty](#getFontProperty(com.nomagic.magicdraw.properties.FontProperty))([FontProperty](FontProperty.html) p)`
Returns shared instance of font property with the same id and value as given property.
`static [FontProperty](FontProperty.html)`
`[getFontProperty](#getFontProperty(java.lang.String,java.awt.Font))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) value)`
Returns shared instance of font property with the given id and value.
`static [FontProperty](FontProperty.html)`
`[getFontProperty](#getFontProperty(java.lang.String,java.awt.Font,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) value,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)`
Returns shared instance of font property with the given id and value.
`static [Property](Property.html)`
`[getProperty](#getProperty(com.nomagic.magicdraw.properties.Property))([Property](Property.html) property)`
Returns shared instance of given property.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PropertyPool
public PropertyPool()
 ============ METHOD DETAIL ========== 
Method Details
getBooleanProperty
public static [BooleanProperty](BooleanProperty.html) getBooleanProperty([BooleanProperty](BooleanProperty.html) p)
Returns shared instance of boolean property with the same id and value as given property.
Parameters:
`p` - the given property.
Returns:
shared instance.
getBooleanProperty
public static [BooleanProperty](BooleanProperty.html) getBooleanProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 boolean value)
Returns shared instance of boolean property with the given id and value.
Parameters:
`id` - the property id.
`value` - the given value of the property.
Returns:
shared instance.
getBooleanProperty
public static [BooleanProperty](BooleanProperty.html) getBooleanProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 boolean value,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)
Returns shared instance of boolean property with the given id and value.
Parameters:
`id` - the property id.
`value` - the given value of the property.
`group` - property group
Returns:
shared instance
getColorProperty
public static [ColorProperty](ColorProperty.html) getColorProperty([ColorProperty](ColorProperty.html) p)
Returns shared instance of color property with the same id and value as given property.
Parameters:
`p` - the given property.
Returns:
shared instance.
getColorProperty
public static [ColorProperty](ColorProperty.html) getColorProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) value)
Returns shared instance of color property with the given id and value.
Parameters:
`id` - the property id.
`value` - the given value of the property.
Returns:
shared instance.
getColorProperty
public static [ColorProperty](ColorProperty.html) getColorProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) value,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)
Returns shared instance of color property with the given id and value.
Parameters:
`id` - the property id.
`value` - the given value of the property.
`group` - property group
Returns:
shared instance
getFontProperty
public static [FontProperty](FontProperty.html) getFontProperty([FontProperty](FontProperty.html) p)
Returns shared instance of font property with the same id and value as given property.
Parameters:
`p` - the given property.
Returns:
shared instance.
getFontProperty
public static [FontProperty](FontProperty.html) getFontProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) value)
Returns shared instance of font property with the given id and value.
Parameters:
`id` - the property id.
`value` - the given value of the property.
Returns:
shared instance.
getFontProperty
public static [FontProperty](FontProperty.html) getFontProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) value,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)
Returns shared instance of font property with the given id and value.
Parameters:
`id` - the property id.
`value` - the given value of the property.
`group` - property group
Returns:
shared instance
getChoiceProperty
public static [ChoiceProperty](ChoiceProperty.html) getChoiceProperty([ChoiceProperty](ChoiceProperty.html) p)
Returns shared instance of choice property with the same id and value as given property.
Parameters:
`p` - the given property.
Returns:
shared instance.
getChoiceProperty
public static [ChoiceProperty](ChoiceProperty.html) getChoiceProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) possibleValues)
Returns shared instance of choice property with the given id, value and possible values for selection
Parameters:
`id` - the property id.
`value` - the given value of the property.
Returns:
shared instance.
getChoiceProperty
public static [ChoiceProperty](ChoiceProperty.html) getChoiceProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) possibleValues,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) group)
Returns shared instance of choice property with the given id, group, value and possible values for selection
Parameters:
`id` - the property id.
`value` - the given value of the property.
`group` - property group
Returns:
shared instance
getProperty
public static [Property](Property.html) getProperty([Property](Property.html) property)
Returns shared instance of given property. If this pool can not create shared instance,
 return given property.
Parameters:
`property` - the given property.
Returns:
cached property

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class PropertyPool">Class PropertyPool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.properties.PropertyPool</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PropertyPool</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">This is a pool of the properties. Use this pool if you do not want to create a lot of instance of properties
 with the same ID and value.
 <p>
 Be careful with changing the value of property taken from this pool. Property is mutable object!!!</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PropertyPool</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty)">getBooleanProperty</a><wbr/>(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> p)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of boolean property with the same id and value as given property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBooleanProperty(java.lang.String,boolean)">getBooleanProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of boolean property with the given id and value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBooleanProperty(java.lang.String,boolean,java.lang.String)">getBooleanProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of boolean property with the given id and value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty)">getChoiceProperty</a><wbr/>(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of choice property with the same id and value as given property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getChoiceProperty(java.lang.String,java.lang.Object,java.util.List)">getChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> possibleValues)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of choice property with the given id, value and possible values for selection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getChoiceProperty(java.lang.String,java.lang.Object,java.util.List,java.lang.String)">getChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> possibleValues,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of choice property with the given id, group, value and possible values for selection</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColorProperty(com.nomagic.magicdraw.properties.ColorProperty)">getColorProperty</a><wbr/>(<a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a> p)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of color property with the same id and value as given property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColorProperty(java.lang.String,java.awt.Color)">getColorProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of color property with the given id and value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColorProperty(java.lang.String,java.awt.Color,java.lang.String)">getColorProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of color property with the given id and value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFontProperty(com.nomagic.magicdraw.properties.FontProperty)">getFontProperty</a><wbr/>(<a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of font property with the same id and value as given property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFontProperty(java.lang.String,java.awt.Font)">getFontProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of font property with the given id and value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFontProperty(java.lang.String,java.awt.Font,java.lang.String)">getFontProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of font property with the given id and value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(com.nomagic.magicdraw.properties.Property)">getProperty</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of given property.</div>
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
<h3>PropertyPool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyPool</span>()</div>
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
<section class="detail" id="getBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty)">
<h3>getBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></span> <span class="element-name">getBooleanProperty</span><wbr/><span class="parameters">(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> p)</span></div>
<div class="block">Returns shared instance of boolean property with the same id and value as given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - the given property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBooleanProperty(java.lang.String,boolean)">
<h3>getBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></span> <span class="element-name">getBooleanProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean value)</span></div>
<div class="block">Returns shared instance of boolean property with the given id and value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBooleanProperty(java.lang.String,boolean,java.lang.String)">
<h3>getBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></span> <span class="element-name">getBooleanProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Returns shared instance of boolean property with the given id and value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dd><code>group</code> - property group</dd>
<dt>Returns:</dt>
<dd>shared instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColorProperty(com.nomagic.magicdraw.properties.ColorProperty)">
<h3>getColorProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></span> <span class="element-name">getColorProperty</span><wbr/><span class="parameters">(<a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a> p)</span></div>
<div class="block">Returns shared instance of color property with the same id and value as given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - the given property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColorProperty(java.lang.String,java.awt.Color)">
<h3>getColorProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></span> <span class="element-name">getColorProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> value)</span></div>
<div class="block">Returns shared instance of color property with the given id and value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColorProperty(java.lang.String,java.awt.Color,java.lang.String)">
<h3>getColorProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></span> <span class="element-name">getColorProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Returns shared instance of color property with the given id and value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dd><code>group</code> - property group</dd>
<dt>Returns:</dt>
<dd>shared instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFontProperty(com.nomagic.magicdraw.properties.FontProperty)">
<h3>getFontProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></span> <span class="element-name">getFontProperty</span><wbr/><span class="parameters">(<a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a> p)</span></div>
<div class="block">Returns shared instance of font property with the same id and value as given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - the given property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFontProperty(java.lang.String,java.awt.Font)">
<h3>getFontProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></span> <span class="element-name">getFontProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> value)</span></div>
<div class="block">Returns shared instance of font property with the given id and value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFontProperty(java.lang.String,java.awt.Font,java.lang.String)">
<h3>getFontProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></span> <span class="element-name">getFontProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Returns shared instance of font property with the given id and value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dd><code>group</code> - property group</dd>
<dt>Returns:</dt>
<dd>shared instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty)">
<h3>getChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></span> <span class="element-name">getChoiceProperty</span><wbr/><span class="parameters">(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> p)</span></div>
<div class="block">Returns shared instance of choice property with the same id and value as given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - the given property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChoiceProperty(java.lang.String,java.lang.Object,java.util.List)">
<h3>getChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></span> <span class="element-name">getChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> possibleValues)</span></div>
<div class="block">Returns shared instance of choice property with the given id, value and possible values for selection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dt>Returns:</dt>
<dd>shared instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChoiceProperty(java.lang.String,java.lang.Object,java.util.List,java.lang.String)">
<h3>getChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></span> <span class="element-name">getChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> possibleValues,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Returns shared instance of choice property with the given id, group, value and possible values for selection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property id.</dd>
<dd><code>value</code> - the given value of the property.</dd>
<dd><code>group</code> - property group</dd>
<dt>Returns:</dt>
<dd>shared instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(com.nomagic.magicdraw.properties.Property)">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block">Returns shared instance of given property. If this pool can not create shared instance,
 return given property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - the given property.</dd>
<dt>Returns:</dt>
<dd>cached property</dd>
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
