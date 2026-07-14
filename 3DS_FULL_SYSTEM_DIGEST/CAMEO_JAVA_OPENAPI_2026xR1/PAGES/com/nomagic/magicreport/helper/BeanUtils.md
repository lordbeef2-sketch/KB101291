# JAVA OPENAPI: BeanUtils (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/helper/BeanUtils.html
- source_path: `com/nomagic/magicreport/helper/BeanUtils.html`
- source_sha256: `93f03ec9a634be675b2b057dff1f89abb9b7d2777e2b2dcbe11626263718bbe3`
- captured_utc: `2026-07-14T16:46:14.533995+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.helper](package-summary.html)

## Class BeanUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.helper.BeanUtils

@OpenApiAllpublic final classBeanUtils
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

This class consists exclusively of static methods that operate java bean object.
 

 The methods of this class all throw a NullPointerException if the bean or class objects provided to them are
 null.

Since:
Dec 20, 2005 3:24:36 PM
Version:
1.2 October 13, 2006

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[findField](#findField(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) methodName)`
Return field name from getter or setter method name.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[findGetter](#findGetter(java.lang.reflect.Field))([Field](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html) field)`
Return getter name from given field.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[findGetter](#findGetter(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)`
Return getter name from given field name.
`static [Method](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html)`
`[findGetter](#findGetter(java.lang.String,java.lang.Class))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> beanClass)`
Return getter Method from given bean class and field name.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[findSetter](#findSetter(java.lang.reflect.Field))([Field](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html) field)`
Return setter name from given field.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[findSetter](#findSetter(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)`
Return setter name from given field name.
`static [Method](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html)`
`[findSetter](#findSetter(java.lang.String,java.lang.Class,java.lang.Class))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> beanClass,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> parameterType)`
Return setter name from given field name.
`static [Field](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html)`
`[getDeclaredField](#getDeclaredField(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)`
Returns a `Field` object that reflects the specified declared field of the class represented by
 this `Class` object or super of this class.This method perform recursive until field was found or
 no super class was retrieved.
`static [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getProperty](#getProperty(java.lang.Object,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bean,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property)`
Invoke and return property value of `bean`.
`static void`
`[setProperty](#setProperty(java.lang.Object,java.lang.String,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bean,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Invoke and set the property value of `bean`.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getProperty
public static [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getProperty([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bean,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property)
Invoke and return property value of `bean`. e.g. `return bean.[get]Property();`
Parameters:
`bean` - Object Bean
`property` - property name
Returns:
property value of given bean
setProperty
public static void setProperty([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bean,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Invoke and set the property value of `bean`. e.g. `bean.[set]Property(value);`
Parameters:
`bean` - Object being set
`property` - property name
`value` - setting value
Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if `bean` or `value` is null
findGetter
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) findGetter([Field](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html) field)
Return getter name from given field.
Parameters:
`field` - `Field`
Returns:
getter name
findSetter
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) findSetter([Field](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html) field)
Return setter name from given field.
Parameters:
`field` - `Field`
Returns:
setter name
findGetter
public static [Method](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html) findGetter([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> beanClass)
 throws [NoSuchMethodException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html)
Return getter Method from given bean class and field name.
Parameters:
`fieldName` - field name
`beanClass` - bean class
Returns:
getter method
Throws:
`[NoSuchMethodException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html)` - if a getter method is not found
findSetter
public static [Method](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html) findSetter([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> beanClass,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> parameterType)
 throws [NoSuchMethodException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html)
Return setter name from given field name.
Parameters:
`fieldName` - field name
`beanClass` - bean class
`parameterType` - a parameter
Returns:
setter method
Throws:
`[NoSuchMethodException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html)` - if a getter method is not found
findGetter
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) findGetter([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)
Return getter name from given field name.
Parameters:
`fieldName` - field name
Returns:
getter name
findSetter
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) findSetter([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)
Return setter name from given field name.
Parameters:
`fieldName` - field name
Returns:
setter name
findField
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) findField([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) methodName)
Return field name from getter or setter method name.
Parameters:
`methodName` - getter or setter name
Returns:
field name of this getter or setter.
getDeclaredField
public static [Field](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html) getDeclaredField([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)
 throws [NoSuchFieldException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchFieldException.html)
Returns a `Field` object that reflects the specified declared field of the class represented by
 this `Class` object or super of this class.This method perform recursive until field was found or
 no super class was retrieved.
Parameters:
`clazz` - original Class
`fieldName` - the name of the field
Returns:
the `Field` object for the specified field in this class
Throws:
`[NoSuchFieldException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchFieldException.html)` - when no such field found

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.helper</a></div>
<h1 class="title" title="Class BeanUtils">Class BeanUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.helper.BeanUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">BeanUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">This class consists exclusively of static methods that operate java bean object.
 <br/>
 The methods of this class all throw a NullPointerException if the bean or class objects provided to them are
 null.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Dec 20, 2005 3:24:36 PM</dd>
<dt>Version:</dt>
<dd>1.2 October 13, 2006</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findField(java.lang.String)">findField</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> methodName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return field name from getter or setter method name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findGetter(java.lang.reflect.Field)">findGetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html" title="class or interface in java.lang.reflect">Field</a> field)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return getter name from given field.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findGetter(java.lang.String)">findGetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return getter name from given field name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html" title="class or interface in java.lang.reflect">Method</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findGetter(java.lang.String,java.lang.Class)">findGetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; beanClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return getter Method from given bean class and field name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findSetter(java.lang.reflect.Field)">findSetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html" title="class or interface in java.lang.reflect">Field</a> field)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return setter name from given field.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findSetter(java.lang.String)">findSetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return setter name from given field name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html" title="class or interface in java.lang.reflect">Method</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findSetter(java.lang.String,java.lang.Class,java.lang.Class)">findSetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; beanClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; parameterType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return setter name from given field name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html" title="class or interface in java.lang.reflect">Field</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeclaredField(java.lang.Class,java.lang.String)">getDeclaredField</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a <code>Field</code> object that reflects the specified declared field of the class represented by
 this <code>Class</code> object or super of this class.This method perform recursive until field was found or
 no super class was retrieved.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.Object,java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bean,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Invoke and return property value of <code>bean</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperty(java.lang.Object,java.lang.String,java.lang.Object)">setProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bean,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Invoke and set the property value of <code>bean</code>.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getProperty(java.lang.Object,java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bean,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property)</span></div>
<div class="block">Invoke and return property value of <code>bean</code>. e.g. <code>return bean.[get]Property();</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bean</code> - Object Bean</dd>
<dd><code>property</code> - property name</dd>
<dt>Returns:</dt>
<dd>property value of given bean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperty(java.lang.Object,java.lang.String,java.lang.Object)">
<h3>setProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bean,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Invoke and set the property value of <code>bean</code>. e.g. <code>bean.[set]Property(value);</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bean</code> - Object being set</dd>
<dd><code>property</code> - property name</dd>
<dd><code>value</code> - setting value</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if <code>bean</code> or <code>value</code> is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findGetter(java.lang.reflect.Field)">
<h3>findGetter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">findGetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html" title="class or interface in java.lang.reflect">Field</a> field)</span></div>
<div class="block">Return getter name from given field.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>field</code> - <code>Field</code></dd>
<dt>Returns:</dt>
<dd>getter name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findSetter(java.lang.reflect.Field)">
<h3>findSetter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">findSetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html" title="class or interface in java.lang.reflect">Field</a> field)</span></div>
<div class="block">Return setter name from given field.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>field</code> - <code>Field</code></dd>
<dt>Returns:</dt>
<dd>setter name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findGetter(java.lang.String,java.lang.Class)">
<h3>findGetter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html" title="class or interface in java.lang.reflect">Method</a></span> <span class="element-name">findGetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; beanClass)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html" title="class or interface in java.lang">NoSuchMethodException</a></span></div>
<div class="block">Return getter Method from given bean class and field name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fieldName</code> - field name</dd>
<dd><code>beanClass</code> - bean class</dd>
<dt>Returns:</dt>
<dd>getter method</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html" title="class or interface in java.lang">NoSuchMethodException</a></code> - if a getter method is not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findSetter(java.lang.String,java.lang.Class,java.lang.Class)">
<h3>findSetter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Method.html" title="class or interface in java.lang.reflect">Method</a></span> <span class="element-name">findSetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; beanClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; parameterType)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html" title="class or interface in java.lang">NoSuchMethodException</a></span></div>
<div class="block">Return setter name from given field name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fieldName</code> - field name</dd>
<dd><code>beanClass</code> - bean class</dd>
<dd><code>parameterType</code> - a parameter</dd>
<dt>Returns:</dt>
<dd>setter method</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchMethodException.html" title="class or interface in java.lang">NoSuchMethodException</a></code> - if a getter method is not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findGetter(java.lang.String)">
<h3>findGetter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">findGetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</span></div>
<div class="block">Return getter name from given field name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fieldName</code> - field name</dd>
<dt>Returns:</dt>
<dd>getter name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findSetter(java.lang.String)">
<h3>findSetter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">findSetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</span></div>
<div class="block">Return setter name from given field name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fieldName</code> - field name</dd>
<dt>Returns:</dt>
<dd>setter name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findField(java.lang.String)">
<h3>findField</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">findField</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> methodName)</span></div>
<div class="block">Return field name from getter or setter method name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>methodName</code> - getter or setter name</dd>
<dt>Returns:</dt>
<dd>field name of this getter or setter.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeclaredField(java.lang.Class,java.lang.String)">
<h3>getDeclaredField</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Field.html" title="class or interface in java.lang.reflect">Field</a></span> <span class="element-name">getDeclaredField</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchFieldException.html" title="class or interface in java.lang">NoSuchFieldException</a></span></div>
<div class="block">Returns a <code>Field</code> object that reflects the specified declared field of the class represented by
 this <code>Class</code> object or super of this class.This method perform recursive until field was found or
 no super class was retrieved.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - original Class</dd>
<dd><code>fieldName</code> - the name of the field</dd>
<dt>Returns:</dt>
<dd>the <code>Field</code> object for the specified field in this class</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NoSuchFieldException.html" title="class or interface in java.lang">NoSuchFieldException</a></code> - when no such field found</dd>
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
