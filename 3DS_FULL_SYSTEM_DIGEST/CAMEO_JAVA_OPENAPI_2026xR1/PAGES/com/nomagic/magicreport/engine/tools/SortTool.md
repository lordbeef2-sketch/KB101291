# JAVA OPENAPI: SortTool (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/tools/SortTool.html
- source_path: `com/nomagic/magicreport/engine/tools/SortTool.html`
- source_sha256: `415795519cc4468d1eb81b83964183893e80975187a1fd13b44d60296a51494d`
- captured_utc: `2026-07-14T16:46:13.003974+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Class SortTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../Tool.html)
com.nomagic.magicreport.engine.tools.SortTool

All Implemented Interfaces:
`[ITool](../ITool.html)`, `[IVariable](../../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[SorterTool](../../../magicdraw/magicreport/tools/SorterTool.html)`, `[SortTable](../../../reportwizard/tools/dialog/SortTable.html)`

@OpenApiAllpublic classSortTool
extends [Tool](../Tool.html)

This class is use to sort the collection in template report.

Since:
Jul 13, 2007
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`protected static class`
`[SortTool.AscendingSort](SortTool.AscendingSort.html)`
sort Collection in ascending
`protected static class`
`[SortTool.DescendingSort](SortTool.DescendingSort.html)`
sort Collection in descending
`protected static class`
`[SortTool.FirstNumberAscendingSort](SortTool.FirstNumberAscendingSort.html)`
sort Collection in first number ascending
`protected static class`
`[SortTool.FirstNumberDescendingSort](SortTool.FirstNumberDescendingSort.html)`
sort Collection in first number descending
`protected static class`
`[SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)`
Sort Collection in ascending.
`protected static class`
`[SortTool.HumanDescendingSort](SortTool.HumanDescendingSort.html)`
sort Collection in descending.
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[ITool.HTMLString](../ITool.HTMLString.html), [ITool.RetainedString](../ITool.RetainedString.html), [ITool.Void](../ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Contains a context name.
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../Tool.html)
`[context](../Tool.html#context), [properties](../Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[VOID](../ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SortTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[defaultSort](#defaultSort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`

`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNextToken](#getNextToken(java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str,
 int offset,
 int len)`
Return a next token of string from starting offset.
`protected [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(java.lang.Object,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Look up a object value by property name.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[humanSort](#humanSort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection)`
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[humanSort](#humanSort(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 boolean isCaseInsensitive)`
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[humanSort](#humanSort(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[humanSort](#humanSort(java.util.Collection,java.lang.String,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 boolean isCaseInsensitive)`
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[humanSort](#humanSort(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)`
Special sorting function with human order.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[humanSort](#humanSort(java.util.Collection,java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction)`
Special sorting function with human order.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[humanSort](#humanSort(java.util.Collection,java.util.Collection,java.lang.String,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction,
 boolean isCaseInsensitive)`
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.
`boolean`
`[isForceNumber](#isForceNumber())()`

`void`
`[setForceNumber](#setForceNumber(boolean))(boolean forceNumber)`

`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`
Sort function for template report.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Sort function for template report.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection,java.lang.String,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 boolean isCaseInsensitive)`
Sort function for template report.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)`
Sort function for template report.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection,java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction)`
Sort function for template report.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection,java.util.Collection,java.lang.String,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction,
 boolean isCaseInsensitive)`
Sort function for template report.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[sortByFirstNumber](#sortByFirstNumber(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection)`
Sort function with special text ordering.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[sortByFirstNumber](#sortByFirstNumber(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Sort function with special text ordering.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[sortByFirstNumber](#sortByFirstNumber(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)`
Sort function with special text ordering.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[sortByFirstNumber](#sortByFirstNumber(java.util.Collection,java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction)`
Sort function with special text ordering.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[sortByLocale](#sortByLocale(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locale)`
Sort the given collection by specified country code.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[sortByLocale](#sortByLocale(java.util.Collection,java.lang.String,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locale)`
Sort the given collection by specified country code.
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../Tool.html)
`[clone](../Tool.html#clone()), [getContext](../Tool.html#getContext()), [getProperties](../Tool.html#getProperties()), [getProperty](../Tool.html#getProperty(java.lang.String)), [getProperty](../Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../Tool.html#notifyObservers(java.lang.Object)), [setContext](../Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[clearTool](../ITool.html#clearTool())`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
Contains a context name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.SortTool.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SortTool
public SortTool()
 ============ METHOD DETAIL ========== 
Method Details
isForceNumber
public boolean isForceNumber()
setForceNumber
public void setForceNumber(boolean forceNumber)
defaultSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) defaultSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)
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
$package is collection to sort
Parameters:
`collection` - collection collection to be sort
Returns:
sorted collection
sort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Sort function for template report. Context name of this class is "sorter". Public functions of this class
 are able to access via template by using `$sorter`. This function will sort case-insensitive by default
 

 For example:
 
 <code>
 #foreach ($rel in $sorter.sort($package, "name:desc"))
 $rel.name
 #end
 </code>
$package is collection to sort
"name:desc" separate by ":" in 2 part
first part to identify the property name to sorting
second part is option to identify type of sorting.
if type of sorting is not identified, the default value is ascending
Parameters:
`collection` - collection to be sort
`propertyName` - identify property name to sorting and type of sorting
Returns:
sorted collection
sort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)
Sort function for template report.
Parameters:
`collection` - collection to be sort
`propertyNames` - collection of property name to sorting
Returns:
sorted collection
sort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction)
Sort function for template report.
Parameters:
`collection` - collection to be sort
`propertyNames` - collection of property name to sorting
`direction` - type of sorting
Returns:
sorted collection
sort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 boolean isCaseInsensitive)
Sort function for template report. Context name of this class is "sorter". Public functions of this class
 are able to access via template by using `$sorter`
 

 For example:
 
 <code>
 #foreach ($rel in $sorter.sort($package, "name:desc"))
 $rel.name
 #end
 </code>
$package is collection to sort
"name:desc" separate by ":" in 2 part
first part to identify the property name to sorting
second part is option to identify type of sorting.
if type of sorting is not identified, the default value is ascending
Parameters:
`collection` - collection to be sort
`propertyName` - identify property name to sorting and type of sorting
`isCaseInsensitive` - true to compare case-insensitive
Returns:
sorted collection
sort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction,
 boolean isCaseInsensitive)
Sort function for template report.
Parameters:
`collection` - collection to be sort
`direction` - type of sorting (asc, desc)
`isCaseInsensitive` - true to compare case-insensitive
`propertyName` - property name to sorting and type of sorting
Returns:
sorted collection
sortByLocale
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> sortByLocale([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locale)
Sort the given collection by specified country code.
 For example:
 
 <code>
 #foreach ($rel in $sorter.sortByLocale($package, "DE"))
 $rel.name
 #end
 </code>
$package is collection to sort
"DE" is the country argument for GERMANY (ISO Country Code)
 Note: This method performs sorting by attribute "name" of each element by default.
Parameters:
`collection` - collection collection to be sort
`locale` - identified country name
Returns:
sorted collection
sortByLocale
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> sortByLocale([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locale)
Sort the given collection by specified country code.
 For example:
 
 <code>
 #foreach ($rel in $sorter.sortByLocale($package, "DE"))
 $rel.name
 #end
 </code>
$package is collection to sort
"DE" is the country argument for GERMANY (ISO Country Code)
Parameters:
`collection` - collection collection to be sort
`propertyName` - identify property name to sorting
`locale` - identified country name
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection)
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"
Parameters:
`collection` - collection collection to be sort
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 boolean isCaseInsensitive)
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"
Parameters:
`collection` - collection collection to be sort
`isCaseInsensitive` - true to sort case-insensitive
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"
Parameters:
`collection` - collection collection to be sort
`propertyName` - property name to sorting and type of sorting
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)
Special sorting function with human order.
Parameters:
`collection` - collection collection to be sort
`propertyNames` - collection of property name to sorting
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction)
Special sorting function with human order.
Parameters:
`collection` - collection collection to be sort
`propertyNames` - collection of property name to sorting
`direction` - type of sorting (asc, desc)
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 boolean isCaseInsensitive)
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"
Parameters:
`collection` - collection collection to be sort
`propertyName` - identify property name to sorting and type of sorting
`isCaseInsensitive` - true to sort case-insensitive
Returns:
sorted collection
humanSort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> humanSort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction,
 boolean isCaseInsensitive)
Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"
Parameters:
`collection` - collection collection to be sort
`propertyNames` - collection of property name to sorting
`direction` - type of sorting (asc, desc)
`isCaseInsensitive` - true to sort case-insensitive
Returns:
sorted collection
sortByFirstNumber
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> sortByFirstNumber([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection)
Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.
 For example:
 
 <code>
 ["1abc", "2abc", "a1bc", "a2bc"]
 </code>
 
 The output order will be:
 
 <code>
 ["1abc", "a1bc", "2abc", "a2bc"]
 </code>
Parameters:
`collection` - collection collection to be sort
Returns:
sorted collection
sortByFirstNumber
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> sortByFirstNumber([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)
Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.
Parameters:
`propertyNames` - collection of property name
Returns:
sorted collection
sortByFirstNumber
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> sortByFirstNumber([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.
 For example:
 
 <code>
 ["1abc", "2abc", "a1bc", "a2bc"]
 </code>
 
 The output order will be:
 
 <code>
 ["1abc", "a1bc", "2abc", "a2bc"]
 </code>
Parameters:
`collection` - collection to be sort
`propertyName` - identify property name to sorting and type of sorting
Returns:
sorted collection
sortByFirstNumber
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> sortByFirstNumber([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) direction)
Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.
Parameters:
`collection` - collection to be sort
`propertyNames` - collection of property name to be sort
Returns:
sorted collection
getNextToken
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNextToken([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str,
 int offset,
 int len)
Return a next token of string from starting offset.
Parameters:
`str` - input string
`offset` - starting offset
`len` - string length
Returns:
next token.
getValue
protected [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Look up a object value by property name.
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Class SortTool">Class SortTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.magicreport.engine.tools.SortTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../../magicdraw/magicreport/tools/SorterTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">SorterTool</a></code>, <code><a href="../../../reportwizard/tools/dialog/SortTable.html" title="class in com.nomagic.reportwizard.tools.dialog">SortTable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SortTool</span>
<span class="extends-implements">extends <a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">This class is use to sort the collection in template report.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jul 13, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool">Serialized Form</a></li>
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
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a></code></div>
<div class="col-last even-row-color">
<div class="block">sort Collection in ascending</div>
</div>
<div class="col-first odd-row-color"><code>protected static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SortTool.DescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.DescendingSort</a></code></div>
<div class="col-last odd-row-color">
<div class="block">sort Collection in descending</div>
</div>
<div class="col-first even-row-color"><code>protected static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SortTool.FirstNumberAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.FirstNumberAscendingSort</a></code></div>
<div class="col-last even-row-color">
<div class="block">sort Collection in first number ascending</div>
</div>
<div class="col-first odd-row-color"><code>protected static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SortTool.FirstNumberDescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.FirstNumberDescendingSort</a></code></div>
<div class="col-last odd-row-color">
<div class="block">sort Collection in first number descending</div>
</div>
<div class="col-first even-row-color"><code>protected static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></code></div>
<div class="col-last even-row-color">
<div class="block">Sort Collection in ascending.</div>
</div>
<div class="col-first odd-row-color"><code>protected static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SortTool.HumanDescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanDescendingSort</a></code></div>
<div class="col-last odd-row-color">
<div class="block">sort Collection in descending.</div>
</div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
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
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../Tool.html#context">context</a>, <a href="../Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SortTool</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#defaultSort(java.util.Collection)">defaultSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNextToken(java.lang.String,int,int)">getNextToken</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 int offset,
 int len)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a next token of string from starting offset.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(java.lang.Object,java.lang.String)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up a object value by property name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection,boolean)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 boolean isCaseInsensitive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection,java.lang.String)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection,java.lang.String,boolean)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean isCaseInsensitive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection,java.util.Collection)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection,java.util.Collection,java.lang.String)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#humanSort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">humanSort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction,
 boolean isCaseInsensitive)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isForceNumber()">isForceNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setForceNumber(boolean)">setForceNumber</a><wbr/>(boolean forceNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function for template report.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection,java.lang.String)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function for template report.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection,java.lang.String,boolean)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean isCaseInsensitive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function for template report.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection,java.util.Collection)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function for template report.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection,java.util.Collection,java.lang.String)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function for template report.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction,
 boolean isCaseInsensitive)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function for template report.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortByFirstNumber(java.util.Collection)">sortByFirstNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function with special text ordering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortByFirstNumber(java.util.Collection,java.lang.String)">sortByFirstNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function with special text ordering.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortByFirstNumber(java.util.Collection,java.util.Collection)">sortByFirstNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function with special text ordering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortByFirstNumber(java.util.Collection,java.util.Collection,java.lang.String)">sortByFirstNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort function with special text ordering.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortByLocale(java.util.Collection,java.lang.String)">sortByLocale</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locale)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort the given collection by specified country code.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortByLocale(java.util.Collection,java.lang.String,java.lang.String)">sortByLocale</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locale)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sort the given collection by specified country code.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../Tool.html#clone()">clone</a>, <a href="../Tool.html#getContext()">getContext</a>, <a href="../Tool.html#getProperties()">getProperties</a>, <a href="../Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../ITool.html#clearTool()">clearTool</a></code></div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.SortTool.CONTEXT_NAME">Constant Field Values</a></li>
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
<h3>SortTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SortTool</span>()</div>
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
<section class="detail" id="isForceNumber()">
<h3>isForceNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isForceNumber</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setForceNumber(boolean)">
<h3>setForceNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setForceNumber</span><wbr/><span class="parameters">(boolean forceNumber)</span></div>
</section>
</li>
<li>
<section class="detail" id="defaultSort(java.util.Collection)">
<h3>defaultSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">defaultSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
<div class="block">Sort function for template report. Context name of this class is "sorter". Public functions of this class
 are able to access via template by using <code>$sorter</code>
<br/>
 For example:
 
 <pre>
 &lt;code&gt;
    #foreach ($rel in $sorter.sort($package))
       $rel.name
    #end
 &lt;/code&gt;
 </pre>
<ul>
<li>$package is collection to sort</li>
</ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection,java.lang.String)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Sort function for template report. Context name of this class is "sorter". Public functions of this class
 are able to access via template by using <code>$sorter</code>. This function will sort case-insensitive by default
 <br/>
 For example:
 
 <pre>
 &lt;code&gt;
    #foreach ($rel in $sorter.sort($package, "name:desc"))
       $rel.name
    #end
 &lt;/code&gt;
 </pre>
<ul>
<li>$package is collection to sort</li>
<li>"name:desc" separate by ":" in 2 part</li>
<li>first part to identify the property name to sorting</li>
<li>second part is option to identify type of sorting.</li>
<li>if type of sorting is not identified, the default value is ascending</li>
</ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dd><code>propertyName</code> - identify property name to sorting and type of sorting</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection,java.util.Collection)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</span></div>
<div class="block">Sort function for template report.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dd><code>propertyNames</code> - collection of property name to sorting</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection,java.util.Collection,java.lang.String)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction)</span></div>
<div class="block">Sort function for template report.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dd><code>propertyNames</code> - collection of property name to sorting</dd>
<dd><code>direction</code> - type of sorting</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection,java.lang.String,boolean)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean isCaseInsensitive)</span></div>
<div class="block">Sort function for template report. Context name of this class is "sorter". Public functions of this class
 are able to access via template by using <code>$sorter</code>
<br/>
 For example:
 
 <pre>
 &lt;code&gt;
    #foreach ($rel in $sorter.sort($package, "name:desc"))
       $rel.name
    #end
 &lt;/code&gt;
 </pre>
<ul>
<li>$package is collection to sort</li>
<li>"name:desc" separate by ":" in 2 part</li>
<li>first part to identify the property name to sorting</li>
<li>second part is option to identify type of sorting.</li>
<li>if type of sorting is not identified, the default value is ascending</li>
</ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dd><code>propertyName</code> - identify property name to sorting and type of sorting</dd>
<dd><code>isCaseInsensitive</code> - true to compare case-insensitive</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction,
 boolean isCaseInsensitive)</span></div>
<div class="block">Sort function for template report.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dd><code>direction</code> - type of sorting (asc, desc)</dd>
<dd><code>isCaseInsensitive</code> - true to compare case-insensitive</dd>
<dd><code>propertyName</code> - property name to sorting and type of sorting</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortByLocale(java.util.Collection,java.lang.String)">
<h3>sortByLocale</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">sortByLocale</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locale)</span></div>
<div class="block">Sort the given collection by specified country code.
 <p>
 For example:
 
 <pre>
 &lt;code&gt;
    #foreach ($rel in $sorter.sortByLocale($package, "DE"))
       $rel.name
    #end
 &lt;/code&gt;
 </pre>
<ul>
<li>$package is collection to sort</li>
<li>"DE" is the country argument for GERMANY (ISO Country Code)</li>
</ul>
 Note: This method performs sorting by attribute "name" of each element by default.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>locale</code> - identified country name</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortByLocale(java.util.Collection,java.lang.String,java.lang.String)">
<h3>sortByLocale</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">sortByLocale</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locale)</span></div>
<div class="block">Sort the given collection by specified country code.
 <p>
 For example:
 
 <pre>
 &lt;code&gt;
    #foreach ($rel in $sorter.sortByLocale($package, "DE"))
       $rel.name
    #end
 &lt;/code&gt;
 </pre>
<ul>
<li>$package is collection to sort</li>
<li>"DE" is the country argument for GERMANY (ISO Country Code)</li>
</ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>propertyName</code> - identify property name to sorting</dd>
<dd><code>locale</code> - identified country name</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection)</span></div>
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection,boolean)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 boolean isCaseInsensitive)</span></div>
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>isCaseInsensitive</code> - true to sort case-insensitive</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection,java.lang.String)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>propertyName</code> - property name to sorting and type of sorting</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection,java.util.Collection)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</span></div>
<div class="block">Special sorting function with human order.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>propertyNames</code> - collection of property name to sorting</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection,java.util.Collection,java.lang.String)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction)</span></div>
<div class="block">Special sorting function with human order.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>propertyNames</code> - collection of property name to sorting</dd>
<dd><code>direction</code> - type of sorting (asc, desc)</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection,java.lang.String,boolean)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 boolean isCaseInsensitive)</span></div>
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>propertyName</code> - identify property name to sorting and type of sorting</dd>
<dd><code>isCaseInsensitive</code> - true to sort case-insensitive</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="humanSort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">
<h3>humanSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">humanSort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction,
 boolean isCaseInsensitive)</span></div>
<div class="block">Special sorting function with human order, which says to split the text to be sorted into numeric and
 non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes "foo10" sort
 after "foo2"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dd><code>propertyNames</code> - collection of property name to sorting</dd>
<dd><code>direction</code> - type of sorting (asc, desc)</dd>
<dd><code>isCaseInsensitive</code> - true to sort case-insensitive</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortByFirstNumber(java.util.Collection)">
<h3>sortByFirstNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">sortByFirstNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection)</span></div>
<div class="block">Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.
 <p>
 For example:
 
 <pre>
 &lt;code&gt;
 ["1abc", "2abc", "a1bc", "a2bc"]
 &lt;/code&gt;
 </pre>
 
 The output order will be:
 
 <pre>
 &lt;code&gt;
 ["1abc", "a1bc", "2abc", "a2bc"]
 &lt;/code&gt;
 </pre></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection collection to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortByFirstNumber(java.util.Collection,java.util.Collection)">
<h3>sortByFirstNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">sortByFirstNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</span></div>
<div class="block">Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyNames</code> - collection of property name</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortByFirstNumber(java.util.Collection,java.lang.String)">
<h3>sortByFirstNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">sortByFirstNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.
 <p>
 For example:
 
 <pre>
 &lt;code&gt;
 ["1abc", "2abc", "a1bc", "a2bc"]
 &lt;/code&gt;
 </pre>
 
 The output order will be:
 
 <pre>
 &lt;code&gt;
 ["1abc", "a1bc", "2abc", "a2bc"]
 &lt;/code&gt;
 </pre></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dd><code>propertyName</code> - identify property name to sorting and type of sorting</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortByFirstNumber(java.util.Collection,java.util.Collection,java.lang.String)">
<h3>sortByFirstNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">sortByFirstNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> direction)</span></div>
<div class="block">Sort function with special text ordering. This function will sort the collection by give the priority to
 first digit found in String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to be sort</dd>
<dd><code>propertyNames</code> - collection of property name to be sort</dd>
<dt>Returns:</dt>
<dd>sorted collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNextToken(java.lang.String,int,int)">
<h3>getNextToken</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNextToken</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 int offset,
 int len)</span></div>
<div class="block">Return a next token of string from starting offset.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - input string</dd>
<dd><code>offset</code> - starting offset</dd>
<dd><code>len</code> - string length</dd>
<dt>Returns:</dt>
<dd>next token.</dd>
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
