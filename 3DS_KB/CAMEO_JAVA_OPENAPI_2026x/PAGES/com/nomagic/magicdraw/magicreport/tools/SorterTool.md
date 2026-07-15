# JAVA OPENAPI: SorterTool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/magicreport/tools/SorterTool.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/SorterTool.html`
- source_sha256: `ade166d04dbda722b03da71d6ad7638637150e71faf3c0e6fdf1c0c205300a1c`
- captured_utc: `2026-07-14T16:57:59.257549+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class SorterTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../../magicreport/engine/Tool.html)
[com.nomagic.magicreport.engine.tools.SortTool](../../../magicreport/engine/tools/SortTool.html)
com.nomagic.magicdraw.magicreport.tools.SorterTool

All Implemented Interfaces:
`[ITool](../../../magicreport/engine/ITool.html)`, `[IVariable](../../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classSorterTool
extends [SortTool](../../../magicreport/engine/tools/SortTool.html)

The sort tool specific for MagicDraw.

Since:
Jun 13, 2008
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.SorterTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.tools.[SortTool](../../../magicreport/engine/tools/SortTool.html)
`[SortTool.AscendingSort](../../../magicreport/engine/tools/SortTool.AscendingSort.html), [SortTool.DescendingSort](../../../magicreport/engine/tools/SortTool.DescendingSort.html), [SortTool.FirstNumberAscendingSort](../../../magicreport/engine/tools/SortTool.FirstNumberAscendingSort.html), [SortTool.FirstNumberDescendingSort](../../../magicreport/engine/tools/SortTool.FirstNumberDescendingSort.html), [SortTool.HumanAscendingSort](../../../magicreport/engine/tools/SortTool.HumanAscendingSort.html), [SortTool.HumanDescendingSort](../../../magicreport/engine/tools/SortTool.HumanDescendingSort.html)`
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Contains a context name.
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[context](../../../magicreport/engine/Tool.html#context), [properties](../../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[VOID](../../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SorterTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[containmentTreeSort](#containmentTreeSort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`
Sorter for sorting elements that they would look same as in browser tree.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getBlankValue](#getBlankValue())()`
Return the value for blank field.
`protected [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(java.lang.Object,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Look up a object value by property name.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[humanSort](#humanSort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`
Sort function for template report.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[tagSort](#tagSort(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Sort element by tag name of specific stereotype.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[tagSort](#tagSort(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 boolean forceNumber)`
Sort element by tag name of specific stereotype.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[tagSort](#tagSort(java.util.Collection,java.lang.String,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Sort element by tag name of specific stereotype name.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[tagSort](#tagSort(java.util.Collection,java.lang.String,java.lang.String,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 boolean forceNumber)`
Sort element by tag name of specific stereotype name.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[treeSort](#treeSort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`
Special sorting function with human order for containment tree elements, which says to split the text to be
 sorted into numeric and non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
Methods inherited from class com.nomagic.magicreport.engine.tools.[SortTool](../../../magicreport/engine/tools/SortTool.html)
`[defaultSort](../../../magicreport/engine/tools/SortTool.html#defaultSort(java.util.Collection)), [getNextToken](../../../magicreport/engine/tools/SortTool.html#getNextToken(java.lang.String,int,int)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,boolean)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String,boolean)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String,boolean)), [isForceNumber](../../../magicreport/engine/tools/SortTool.html#isForceNumber()), [setForceNumber](../../../magicreport/engine/tools/SortTool.html#setForceNumber(boolean)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String,boolean)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String,boolean)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.lang.String)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection,java.lang.String)), [sortByLocale](../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String)), [sortByLocale](../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String,java.lang.String))`
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[clone](../../../magicreport/engine/Tool.html#clone()), [getContext](../../../magicreport/engine/Tool.html#getContext()), [getProperties](../../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[clearTool](../../../magicreport/engine/ITool.html#clearTool())`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
Contains a context name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.SorterTool.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SorterTool
public SorterTool()
 ============ METHOD DETAIL ========== 
Method Details
setProperties
public void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties. Override current properties will not affect with the engine.
Specified by:
`[setProperties](../../../magicreport/engine/ITool.html#setProperties(java.util.Properties))` in interface `[ITool](../../../magicreport/engine/ITool.html)`
Overrides:
`[setProperties](../../../magicreport/engine/Tool.html#setProperties(java.util.Properties))` in class `[Tool](../../../magicreport/engine/Tool.html)`
Parameters:
`properties` - template engine properties
getBlankValue
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getBlankValue()
Return the value for blank field.
Returns:
value for blank field
sort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)
Sort function for template report. Context name of this class is "sorter". Public functions of this class
 are able to access via template by using `$sorter`
For example:

 <code>
 #foreach ($rel in $sorter.sort($package))
 $rel.name
 #end
 </code>
This method will sort object in collection by default MagicDraw model ordering ('name' when input is a
 collection of NamedElement).
Overrides:
`[sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection))` in class `[SortTool](../../../magicreport/engine/tools/SortTool.html)`
Parameters:
`collection` - collection to be sort
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"
 This method will sort object in collection by default MagicDraw model ordering. ('name' when input is a
 collection of NamedElement).
Overrides:
`[humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection))` in class `[SortTool](../../../magicreport/engine/tools/SortTool.html)`
Parameters:
`collection` - collection collection to be sort
Returns:
sorted collection
tagSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) tagSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
Sort element by tag name of specific stereotype.
Parameters:
`collection` - elements to be sorted
`stereotype` - specific stereotype
`tagName` - tagName
Returns:
sorted collection
tagSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) tagSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
Sort element by tag name of specific stereotype name.
Parameters:
`collection` - elements to be sorted
`stereotypeName` - specific stereotype name
`tagName` - tagName
Returns:
sorted collection
tagSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) tagSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 boolean forceNumber)
Sort element by tag name of specific stereotype.
Parameters:
`collection` - elements to be sorted
`stereotype` - specific stereotype
`tagName` - tagName
`forceNumber` - try to compare by number
Returns:
sorted collection
tagSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) tagSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stereotypeName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 boolean forceNumber)
Sort element by tag name of specific stereotype name.
Parameters:
`collection` - elements to be sorted
`stereotypeName` - specific stereotype name
`tagName` - tagName
`forceNumber` - try to compare by number
Returns:
sorted collection
treeSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) treeSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)
Special sorting function with human order for containment tree elements, which says to split the text to be
 sorted into numeric and non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
 This makes "foo10" sort after "foo2"
 This method will sort object in collection by default MagicDraw model ordering. ('name' when input is a
 collection of NamedElement).
Parameters:
`collection` - collection collection to be sort
Returns:
sorted collection
containmentTreeSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) containmentTreeSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)
Sorter for sorting elements that they would look same as in browser tree.
Parameters:
`collection` - collection collection to be sort
Returns:
sorted collection
getValue
protected [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Look up a object value by property name.
Overrides:
`[getValue](../../../magicreport/engine/tools/SortTool.html#getValue(java.lang.Object,java.lang.String))` in class `[SortTool](../../../magicreport/engine/tools/SortTool.html)`
Parameters:
`object` - target object.
`propertyName` - property name
Returns:
the value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class SorterTool">Class SorterTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance"><a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">com.nomagic.magicreport.engine.tools.SortTool</a>
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.SorterTool</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SorterTool</span>
<span class="extends-implements">extends <a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></span></div>
<div class="block">The sort tool specific for MagicDraw.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 13, 2008</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.SorterTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.tools.SortTool">Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.tools.<a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></h2>
<code><a href="../../../magicreport/engine/tools/SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.DescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.DescendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.FirstNumberAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.FirstNumberAscendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.FirstNumberDescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.FirstNumberDescendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.HumanDescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanDescendingSort</a></code></div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains a context name.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#context">context</a>, <a href="../../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SorterTool</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#containmentTreeSort(java.util.Collection)">containmentTreeSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sorter for sorting elements that they would look same as in browser tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBlankValue()">getBlankValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the value for blank field.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(java.lang.Object,java.lang.String)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up a object value by property name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function for template report.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#tagSort(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">tagSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort element by tag name of specific stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#tagSort(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">tagSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean forceNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort element by tag name of specific stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#tagSort(java.util.Collection,java.lang.String,java.lang.String)">tagSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort element by tag name of specific stereotype name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#tagSort(java.util.Collection,java.lang.String,java.lang.String,boolean)">tagSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean forceNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort element by tag name of specific stereotype name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#treeSort(java.util.Collection)">treeSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order for containment tree elements, which says to split the text to be
 sorted into numeric and non-numeric chunks, then sort so that the numeric chunks are treated as numbers.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.tools.SortTool">Methods inherited from class com.nomagic.magicreport.engine.tools.<a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></h3>
<code><a href="../../../magicreport/engine/tools/SortTool.html#defaultSort(java.util.Collection)">defaultSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#getNextToken(java.lang.String,int,int)">getNextToken</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,boolean)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String,boolean)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#isForceNumber()">isForceNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#setForceNumber(boolean)">setForceNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String,boolean)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.lang.String)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection,java.lang.String)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String)">sortByLocale</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String,java.lang.String)">sortByLocale</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<section class="detail" id="CONTEXT_NAME">
<h3>CONTEXT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTEXT_NAME</span></div>
<div class="block">Contains a context name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.SorterTool.CONTEXT_NAME">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>SorterTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SorterTool</span>()</div>
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
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties. Override current properties will not affect with the engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../magicreport/engine/ITool.html#setProperties(java.util.Properties)">setProperties</a></code> in interface <code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code> in class <code><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>properties</code> - template engine properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBlankValue()">
<h3>getBlankValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getBlankValue</span>()</div>
<div class="block">Return the value for blank field.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value for blank field</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
<div class="block">Sort function for template report. Context name of this class is "sorter". Public functions of this class
 are able to access via template by using <code>$sorter</code>
<p>
 For example:

 <pre>
 &lt;code&gt;
    #foreach ($rel in $sorter.sort($package))
       $rel.name
    #end
 &lt;/code&gt;
 </pre>
</p>
<p>
 This method will sort object in collection by default MagicDraw model ordering ('name' when input is a
 collection of NamedElement).
 </p></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection)">sort</a></code> in class <code><a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"
 <p>
 This method will sort object in collection by default MagicDraw model ordering. ('name' when input is a
 collection of NamedElement).
 </p></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection)">humanSort</a></code> in class <code><a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="tagSort(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">
<h3>tagSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">tagSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Sort element by tag name of specific stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - elements to be sorted</dd>
<dd><code>stereotype</code> - specific stereotype</dd>
<dd><code>tagName</code> - tagName</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="tagSort(java.util.Collection,java.lang.String,java.lang.String)">
<h3>tagSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">tagSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Sort element by tag name of specific stereotype name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - elements to be sorted</dd>
<dd><code>stereotypeName</code> - specific stereotype name</dd>
<dd><code>tagName</code> - tagName</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="tagSort(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,boolean)">
<h3>tagSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">tagSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean forceNumber)</span></div>
<div class="block">Sort element by tag name of specific stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - elements to be sorted</dd>
<dd><code>stereotype</code> - specific stereotype</dd>
<dd><code>tagName</code> - tagName</dd>
<dd><code>forceNumber</code> - try to compare by number</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="tagSort(java.util.Collection,java.lang.String,java.lang.String,boolean)">
<h3>tagSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">tagSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 boolean forceNumber)</span></div>
<div class="block">Sort element by tag name of specific stereotype name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - elements to be sorted</dd>
<dd><code>stereotypeName</code> - specific stereotype name</dd>
<dd><code>tagName</code> - tagName</dd>
<dd><code>forceNumber</code> - try to compare by number</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="treeSort(java.util.Collection)">
<h3>treeSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">treeSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
<div class="block">Special sorting function with human order for containment tree elements, which says to split the text to be
 sorted into numeric and non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
 This makes "foo10" sort after "foo2"
 <p>
 This method will sort object in collection by default MagicDraw model ordering. ('name' when input is a
 collection of NamedElement).
 </p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containmentTreeSort(java.util.Collection)">
<h3>containmentTreeSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">containmentTreeSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
<div class="block">Sorter for sorting elements that they would look same as in browser tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(java.lang.Object,java.lang.String)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Look up a object value by property name.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../magicreport/engine/tools/SortTool.html#getValue(java.lang.Object,java.lang.String)">getValue</a></code> in class <code><a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>object</code> - target object.</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>the value.</dd>
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
