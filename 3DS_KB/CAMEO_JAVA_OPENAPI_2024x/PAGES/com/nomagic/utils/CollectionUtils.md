# JAVA OPENAPI: CollectionUtils (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/utils/CollectionUtils.html
- source_path: `com/nomagic/utils/CollectionUtils.html`
- source_sha256: `9047de53d578d6fd66b01a89e0e21d6c1df3d4f315252720d86320ab7799c253`
- captured_utc: `2026-07-14T16:53:50.592059+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.utils](package-summary.html)

## Class CollectionUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.utils.CollectionUtils

@OpenApiAllpublic classCollectionUtils
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Collection related utility methods.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CollectionUtils](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static <T> void`
`[addIfNotNull](#addIfNotNull(T,java.util.Collection))(T element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)`

`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T> source,
 boolean allowDuplication)`
Append source to target collection.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Iterator,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication)`
Append source to target collection.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Iterator,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)`
Append source to target collection.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,T%5B%5D,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 T[] source,
 boolean allowDuplication)`
Append source array to target collection.
`static boolean`
`[contains](#contains(java.util.Iterator,java.lang.Object))([Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html) it,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Checks if given iterator contains given object.
`static boolean`
`[containsAny](#containsAny(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) location,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) what)`
Returns true if location contains any element from what
`static <S,
T,
C extends [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>> 
C`
`[convert](#convert(java.util.Collection,C,com.nomagic.utils.Converter))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<S> source,
 C target,
 [Converter](Converter.html)<? super S,? super T> converter)`
Convert one (source) collection into another (target) collection.
`static <C extends [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>,
E> 
C`
`[createCollection](#createCollection(java.lang.Class,java.util.Iterator))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<C> collection,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<E> it)`
Creates given type collection and fills it with objects from given iterator
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[createFromStringRepresentation](#createFromStringRepresentation(java.lang.String,java.lang.String,com.nomagic.utils.Converter))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),T> converter)`
Create collection from string.
`static <T> [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStringRepresentation](#createStringRepresentation(java.util.Collection,java.lang.String,com.nomagic.utils.Converter))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<T,[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> converter)`
Create string representation of given collection.
`static boolean`
`[equals](#equals(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection2)`
Checks if both collections are equal - size the same and elements by order are the same
`static <T> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T>`
`[filterByClassType](#filterByClassType(java.util.Collection,java.lang.Class))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> input,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)`
Filters and casts collection from one type to another
`static void`
`[leaveElements](#leaveElements(java.util.List,int))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) elements,
 int numberToLeave)`
Leaves a given number of first elements in the collection.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[mapToString](#mapToString(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> map)`
Serializes map to string.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[notDublicatedList](#notDublicatedList(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)`
Deprecated.
use [`notDuplicatedList(java.util.Collection)`](#notDuplicatedList(java.util.Collection))
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[notDuplicatedList](#notDuplicatedList(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)`
Removes duplicates from given collection.
`static <T> void`
`[setFirstValue](#setFirstValue(java.util.Collection,T))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 T value)`
Set first value of the given collection.
`static <T> void`
`[setSingleValue](#setSingleValue(java.util.Collection,T))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 T value)`
Removes all values from a given collection and adds a new one.
`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[stringToMap](#stringToMap(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) input)`
Deserialize map from string.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[toOptimizedCacheCollection](#toOptimizedCacheCollection(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)`
Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance

 Returned collection in unmodifiable
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[toOptimizedContainsCollection](#toOptimizedContainsCollection(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)`
Wrap the specified collection into containable collection that ensures
 optimized {{Collection.contains()}} performance.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CollectionUtils
public CollectionUtils()
 ============ METHOD DETAIL ========== 
Method Details
convert
public static <S,
T,
C extends [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>> C convert([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<S> source,
 C target,
 [Converter](Converter.html)<? super S,? super T> converter)
Convert one (source) collection into another (target) collection.
 Converts each source element and adds converted element to target collection.
Type Parameters:
`S` - source collection element type.
`T` - target collection element type.
`C` - target collection type.
Parameters:
`source` - source collection.
`target` - target collection.
`converter` - converts each element.
Returns:
target collection.
append
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T> source,
 boolean allowDuplication)
Append source to target collection.
Parameters:
`target` - target
`source` - source
`allowDuplication` - do not check for already added element if true
Returns:
appended collection
append
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication)
Append source to target collection.
Parameters:
`target` - target
`sourceIterator` - source iterator.
`allowDuplication` - do not check for already added element if true
Returns:
appended collection
append
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)
Append source to target collection.
Parameters:
`target` - target
`sourceIterator` - source iterator.
`allowDuplication` - do not check for already added element if true
`allowNulls` - allows nulls
Returns:
appended collection
append
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> target,
 T[] source,
 boolean allowDuplication)
Append source array to target collection.
Parameters:
`target` - target
`source` - source
`allowDuplication` - do not check for already added element if true
Returns:
appended vector
contains
public static boolean contains([Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html) it,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Checks if given iterator contains given object.
Parameters:
`it` - the iterator.
`o` - the object.
Returns:
true, if it contains o.
containsAny
public static boolean containsAny([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) location,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) what)
Returns true if location contains any element from what
Parameters:
`location` - location collection
`what` - what collection.
Returns:
boolean.
createCollection
public static <C extends [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>,
E> C createCollection([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<C> collection,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<E> it)
Creates given type collection and fills it with objects from given iterator
Parameters:
`collection` - type collection.
`it` - The given iterator.
Returns:
the result collection.
notDuplicatedList
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> notDuplicatedList([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)
Removes duplicates from given collection. After remove one element will be in collection only one time.
Parameters:
`collection` - collection to operate with. (makes sense when col are list (sets cant have identical elements).
Returns:
collection.
notDublicatedList
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> notDublicatedList([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)
Deprecated.
use [`notDuplicatedList(java.util.Collection)`](#notDuplicatedList(java.util.Collection))
Removes duplicates from given collection. After remove one element will be in collection only one time.
Parameters:
`collection` - collection to operate with. (makes sense when col are list (sets cant have identical elements).
Returns:
collection.
createStringRepresentation
public static <T> [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStringRepresentation([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<T,[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> converter)
Create string representation of given collection.
Parameters:
`collection` - collection.
`delimiter` - values delimiter.
`converter` - convert object to string.
Returns:
string representation of collection.
createFromStringRepresentation
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> createFromStringRepresentation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),T> converter)
Create collection from string.
Parameters:
`string` - string representation.
`delimiter` - values delimiter.
`converter` - convert string to object.
Returns:
collection.
leaveElements
public static void leaveElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) elements,
 int numberToLeave)
Leaves a given number of first elements in the collection.
Parameters:
`elements` - elements to filter.
`numberToLeave` - number of elements to leave.
mapToString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mapToString([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> map)
Serializes map to string.
Parameters:
`map` - map to serialize.
Returns:
string representation of the map.
stringToMap
public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> stringToMap([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) input)
Deserialize map from string.
Parameters:
`input` - input string.
Returns:
map.
filterByClassType
public static <T> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> filterByClassType([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> input,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)
Filters and casts collection from one type to another
Type Parameters:
`T` - type
Parameters:
`input` - input collection
`type` - desired output collection type
Returns:
new typed list
setSingleValue
public static <T> void setSingleValue([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 T value)
Removes all values from a given collection and adds a new one.
Parameters:
`collection` - collection
`value` - a new value
setFirstValue
public static <T> void setFirstValue([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 @CheckForNull
 T value)
Set first value of the given collection. If collection is empty, adds a new value.
 If value is null, removes first value from collection.
Parameters:
`collection` - collection
`value` - a new value
toOptimizedContainsCollection
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> toOptimizedContainsCollection([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)
Wrap the specified collection into containable collection that ensures
 optimized {{Collection.contains()}} performance.
 The provided collection should not change while the wrapped collection is used.
Parameters:
`collection` - a collection to wrap into containable collection
Returns:
return wrapped collection.
toOptimizedCacheCollection
public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> toOptimizedCacheCollection([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)
Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance

 Returned collection in unmodifiable
equals
public static boolean equals([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection2)
Checks if both collections are equal - size the same and elements by order are the same
Parameters:
`collection1` - first collection
`collection2` - second collection
Returns:
true if size the same and elements by order are the same
addIfNotNull
public static <T> void addIfNotNull(@CheckForNull
 T element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.utils</a></div>
<h1 class="title" title="Class CollectionUtils">Class CollectionUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.utils.CollectionUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CollectionUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Collection related utility methods.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CollectionUtils</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addIfNotNull(T,java.util.Collection)">addIfNotNull</a><wbr/>(T element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Collection,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt; source,
 boolean allowDuplication)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append source to target collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Iterator,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append source to target collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Iterator,boolean,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append source to target collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,T%5B%5D,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 T[] source,
 boolean allowDuplication)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append source array to target collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#contains(java.util.Iterator,java.lang.Object)">contains</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given iterator contains given object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#containsAny(java.util.Collection,java.util.Collection)">containsAny</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> location,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> what)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if location contains any element from what</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;S,<wbr/>
T,<wbr/>
C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;&gt;<br/>C</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.util.Collection,C,com.nomagic.utils.Converter)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;S&gt; source,
 C target,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;? super S,<wbr/>? super T&gt; converter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert one (source) collection into another (target) collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;,<wbr/>
E&gt;<br/>C</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCollection(java.lang.Class,java.util.Iterator)">createCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;C&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;E&gt; it)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates given type collection and fills it with objects from given iterator</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createFromStringRepresentation(java.lang.String,java.lang.String,com.nomagic.utils.Converter)">createFromStringRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>T&gt; converter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create collection from string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringRepresentation(java.util.Collection,java.lang.String,com.nomagic.utils.Converter)">createStringRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; converter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create string representation of given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.util.Collection,java.util.Collection)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if both collections are equal - size the same and elements by order are the same</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterByClassType(java.util.Collection,java.lang.Class)">filterByClassType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters and casts collection from one type to another</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#leaveElements(java.util.List,int)">leaveElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> elements,
 int numberToLeave)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Leaves a given number of first elements in the collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#mapToString(java.util.Map)">mapToString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; map)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Serializes map to string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#notDublicatedList(java.util.Collection)">notDublicatedList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#notDuplicatedList(java.util.Collection)"><code>notDuplicatedList(java.util.Collection)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#notDuplicatedList(java.util.Collection)">notDuplicatedList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes duplicates from given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFirstValue(java.util.Collection,T)">setFirstValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 T value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set first value of the given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSingleValue(java.util.Collection,T)">setSingleValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 T value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all values from a given collection and adds a new one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#stringToMap(java.lang.String)">stringToMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> input)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Deserialize map from string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toOptimizedCacheCollection(java.util.Collection)">toOptimizedCacheCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance

 Returned collection in unmodifiable</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toOptimizedContainsCollection(java.util.Collection)">toOptimizedContainsCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap the specified collection into containable collection that ensures
 optimized {{Collection.contains()}} performance.</div>
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
<h3>CollectionUtils</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CollectionUtils</span>()</div>
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
<section class="detail" id="convert(java.util.Collection,C,com.nomagic.utils.Converter)">
<h3 id="convert(java.util.Collection,java.util.Collection,com.nomagic.utils.Converter)">convert</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;S,<wbr/>
T,<wbr/>
C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;&gt;</span> <span class="return-type">C</span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;S&gt; source,
 C target,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;? super S,<wbr/>? super T&gt; converter)</span></div>
<div class="block">Convert one (source) collection into another (target) collection.
 Converts each source element and adds converted element to target collection.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>S</code> - source collection element type.</dd>
<dd><code>T</code> - target collection element type.</dd>
<dd><code>C</code> - target collection type.</dd>
<dt>Parameters:</dt>
<dd><code>source</code> - source collection.</dd>
<dd><code>target</code> - target collection.</dd>
<dd><code>converter</code> - converts each element.</dd>
<dt>Returns:</dt>
<dd>target collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,java.util.Collection,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt; source,
 boolean allowDuplication)</span></div>
<div class="block">Append source to target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>source</code> - source</dd>
<dd><code>allowDuplication</code> - do not check for already added element if true</dd>
<dt>Returns:</dt>
<dd>appended collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,java.util.Iterator,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication)</span></div>
<div class="block">Append source to target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>sourceIterator</code> - source iterator.</dd>
<dd><code>allowDuplication</code> - do not check for already added element if true</dd>
<dt>Returns:</dt>
<dd>appended collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,java.util.Iterator,boolean,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)</span></div>
<div class="block">Append source to target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>sourceIterator</code> - source iterator.</dd>
<dd><code>allowDuplication</code> - do not check for already added element if true</dd>
<dd><code>allowNulls</code> - allows nulls</dd>
<dt>Returns:</dt>
<dd>appended collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,T[],boolean)">
<h3 id="append(java.util.Collection,java.lang.Object[],boolean)">append</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 T[] source,
 boolean allowDuplication)</span></div>
<div class="block">Append source array to target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>source</code> - source</dd>
<dd><code>allowDuplication</code> - do not check for already added element if true</dd>
<dt>Returns:</dt>
<dd>appended vector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contains(java.util.Iterator,java.lang.Object)">
<h3>contains</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Checks if given iterator contains given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>it</code> - the iterator.</dd>
<dd><code>o</code> - the object.</dd>
<dt>Returns:</dt>
<dd>true, if it contains o.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsAny(java.util.Collection,java.util.Collection)">
<h3>containsAny</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">containsAny</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> location,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> what)</span></div>
<div class="block">Returns true if location contains any element from what</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - location collection</dd>
<dd><code>what</code> - what collection.</dd>
<dt>Returns:</dt>
<dd>boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollection(java.lang.Class,java.util.Iterator)">
<h3>createCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;,<wbr/>
E&gt;</span> <span class="return-type">C</span> <span class="element-name">createCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;C&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;E&gt; it)</span></div>
<div class="block">Creates given type collection and fills it with objects from given iterator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - type collection.</dd>
<dd><code>it</code> - The given iterator.</dd>
<dt>Returns:</dt>
<dd>the result collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notDuplicatedList(java.util.Collection)">
<h3>notDuplicatedList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">notDuplicatedList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Removes duplicates from given collection. After remove one element will be in collection only one time.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to operate  with. (makes sense when col are list (sets cant have identical elements).</dd>
<dt>Returns:</dt>
<dd>collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notDublicatedList(java.util.Collection)">
<h3>notDublicatedList</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">notDublicatedList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#notDuplicatedList(java.util.Collection)"><code>notDuplicatedList(java.util.Collection)</code></a></div>
</div>
<div class="block">Removes duplicates from given collection. After remove one element will be in collection only one time.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to operate  with. (makes sense when col are list (sets cant have identical elements).</dd>
<dt>Returns:</dt>
<dd>collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringRepresentation(java.util.Collection,java.lang.String,com.nomagic.utils.Converter)">
<h3>createStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStringRepresentation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; converter)</span></div>
<div class="block">Create string representation of given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection.</dd>
<dd><code>delimiter</code> - values delimiter.</dd>
<dd><code>converter</code> - convert object to string.</dd>
<dt>Returns:</dt>
<dd>string representation of collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFromStringRepresentation(java.lang.String,java.lang.String,com.nomagic.utils.Converter)">
<h3>createFromStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">createFromStringRepresentation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>T&gt; converter)</span></div>
<div class="block">Create collection from string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - string representation.</dd>
<dd><code>delimiter</code> - values delimiter.</dd>
<dd><code>converter</code> - convert string to object.</dd>
<dt>Returns:</dt>
<dd>collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="leaveElements(java.util.List,int)">
<h3>leaveElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">leaveElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> elements,
 int numberToLeave)</span></div>
<div class="block">Leaves a given number of first elements in the collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to filter.</dd>
<dd><code>numberToLeave</code> - number of elements to leave.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mapToString(java.util.Map)">
<h3>mapToString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">mapToString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; map)</span></div>
<div class="block">Serializes map to string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>map</code> - map to serialize.</dd>
<dt>Returns:</dt>
<dd>string representation of the map.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="stringToMap(java.lang.String)">
<h3>stringToMap</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">stringToMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> input)</span></div>
<div class="block">Deserialize map from string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input string.</dd>
<dt>Returns:</dt>
<dd>map.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterByClassType(java.util.Collection,java.lang.Class)">
<h3>filterByClassType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">filterByClassType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
<div class="block">Filters and casts collection from one type to another</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - type</dd>
<dt>Parameters:</dt>
<dd><code>input</code> - input collection</dd>
<dd><code>type</code> - desired output collection type</dd>
<dt>Returns:</dt>
<dd>new typed list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSingleValue(java.util.Collection,T)">
<h3 id="setSingleValue(java.util.Collection,java.lang.Object)">setSingleValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">setSingleValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 T value)</span></div>
<div class="block">Removes all values from a given collection and adds a new one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection</dd>
<dd><code>value</code> - a new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFirstValue(java.util.Collection,T)">
<h3 id="setFirstValue(java.util.Collection,java.lang.Object)">setFirstValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">setFirstValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 @CheckForNull
 T value)</span></div>
<div class="block">Set first value of the given collection. If collection is empty, adds a new value.
 If value is null, removes first value from collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection</dd>
<dd><code>value</code> - a new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toOptimizedContainsCollection(java.util.Collection)">
<h3>toOptimizedContainsCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">toOptimizedContainsCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Wrap the specified collection into containable collection that ensures
 optimized {{Collection.contains()}} performance.
 The provided collection should not change while the wrapped collection is used.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - a collection to wrap into containable collection</dd>
<dt>Returns:</dt>
<dd>return wrapped collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toOptimizedCacheCollection(java.util.Collection)">
<h3>toOptimizedCacheCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">toOptimizedCacheCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance

 Returned collection in unmodifiable</div>
</section>
</li>
<li>
<section class="detail" id="equals(java.util.Collection,java.util.Collection)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection2)</span></div>
<div class="block">Checks if both collections are equal - size the same and elements by order are the same</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection1</code> - first collection</dd>
<dd><code>collection2</code> - second collection</dd>
<dt>Returns:</dt>
<dd>true if size the same and elements by order are the same</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addIfNotNull(T,java.util.Collection)">
<h3 id="addIfNotNull(java.lang.Object,java.util.Collection)">addIfNotNull</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">addIfNotNull</span><wbr/><span class="parameters">(@CheckForNull
 T element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
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
