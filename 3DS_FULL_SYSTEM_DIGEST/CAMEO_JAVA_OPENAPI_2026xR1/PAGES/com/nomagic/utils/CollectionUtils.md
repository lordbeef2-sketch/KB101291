# JAVA OPENAPI: CollectionUtils (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/utils/CollectionUtils.html
- source_path: `com/nomagic/utils/CollectionUtils.html`
- source_sha256: `77e3a951b9cfa3f60421f0dd425f8c240b7f69f5648d1a8c882ee05766eb4c74`
- captured_utc: `2026-07-14T16:46:50.198468+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.utils](package-summary.html)

## Class CollectionUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.utils.CollectionUtils

@OpenApiAllpublic classCollectionUtils
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Collection related utility methods.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CollectionUtils](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static <T> void`
`[addIfNotNull](#addIfNotNull(T,java.util.Collection))(T element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)`
Adds the given element to the collection unless it is null.
`static <T> boolean`
`[allMatch](#allMatch(java.util.Collection,java.util.function.Predicate))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)`
Check if all objects match given predicate.
`static <T> boolean`
`[anyMatch](#anyMatch(java.util.Collection,java.util.function.Predicate))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)`
Looks for any object matching given predicate.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends T> source,
 boolean allowDuplication)`
Append a source to a target collection.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Iterator,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication)`
Append a source to a target collection.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Iterator,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)`
Append a source to a target collection.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,T%5B%5D,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 T[] source,
 boolean allowDuplication)`
Append source array to a target collection.
`static <T> boolean`
`[checkOrder](#checkOrder(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list1,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list2)`
This method checks if the elements in both lists have the same order.
`static boolean`
`[contains](#contains(java.util.Iterator,java.lang.Object))([Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html) it,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`
Checks if given iterator contains a given object.
`static boolean`
`[containsAny](#containsAny(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) location,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) what)`
Returns true if location contains any element from what
`static <S,
T,
C extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>> 
C`
`[convert](#convert(java.util.Collection,C,com.nomagic.utils.Converter))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<S> source,
 C target,
 [Converter](Converter.html)<? super S,? super T> converter)`
Convert one (source) collection into another (target) collection.
`static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T>`
`[copyAndAdd](#copyAndAdd(java.util.List,java.util.Collection))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> toAdd)`
Creates copy of the given list, or new list if null is provided.
`static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T>`
`[copyAndAdd](#copyAndAdd(java.util.List,T))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list,
 T element)`
Creates copy of the given list, or new list if null is provided.
`static <C extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<E>,
E> 
C`
`[createCollection](#createCollection(java.lang.Class,java.util.Iterator))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<C> collection,
 [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<E> it)`
Creates a given type collection and fills it with objects from given iterator
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[createFromStringRepresentation](#createFromStringRepresentation(java.lang.String,java.lang.String,com.nomagic.utils.Converter))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),T> converter)`
Create a collection from string.
`static <T> [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createStringRepresentation](#createStringRepresentation(java.util.Collection,java.lang.String,com.nomagic.utils.Converter))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<T,[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> converter)`
Create string representation of a given collection.
`static <T> boolean`
`[endsWith](#endsWith(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> postfixCollection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)`
Checks if a collection ends with postfixCollection
 Example: a collection is [A, B, C], postfixCollection is [B, C], the result would be true.
`static boolean`
`[equals](#equals(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection1,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection2)`
Checks if both collections are equal - size the same and elements by order are the same
`static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T>`
`[filterByClassType](#filterByClassType(java.util.Collection,java.lang.Class))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> input,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)`
Filters and casts a collection from one type to another
`static <T> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[filterByClassType](#filterByClassType(java.util.stream.Stream,java.lang.Class))([Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<?> stream,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)`
Filter and map according given class.
`static <T> T`
`[find](#find(java.util.Collection,java.util.function.Predicate))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)`
Looks for object matching given predicate.
`static <T> T`
`[find](#find(java.util.Collection,java.lang.Class))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) input,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> castClass)`
Looks for object matching given class.
`static <T> T`
`[find](#find(java.util.function.Supplier,java.util.function.Supplier,java.util.function.Predicate,java.lang.Class))([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>> collection1,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>> collection2,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)`
Looks for object matching given predicate in the first collection and then in the second.
`static <T> T`
`[findByClassType](#findByClassType(java.util.Collection,java.lang.Class))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> input,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)`
Looks for an object of give class in the given collection.
`static <T> T`
`[getFirst](#getFirst(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)`
Gets the first element of this collection or null if a collection is empty.
`static void`
`[leaveElements](#leaveElements(java.util.List,int))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) elements,
 int numberToLeave)`
Leaves a given number of first elements in the collection.
`static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T>`
`[listOf](#listOf(T))(T element)`
Creates unmodifiable [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) with a given element.
`static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T>`
`[listOf](#listOf(T,java.util.List))(T element,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list)`
Appends a given element to new unmodifiable [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) constructed from the given list.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[mapToString](#mapToString(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> map)`
Serializes a map to string.
`static <T> void`
`[mergeInto](#mergeInto(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list1,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list2)`
Merges elements from list2 into list1, taking into account overlapping sequences.
`static <T> boolean`
`[noneMatch](#noneMatch(java.util.Collection,java.util.function.Predicate))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)`
Check if no object matches given predicate.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[notDuplicatedList](#notDuplicatedList(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)`
Removes duplicates from a given collection.
`static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T>`
`[removeIf](#removeIf(java.util.List,java.util.function.Predicate))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)`
Removes elements from the given list that don't match the predicate.
`static <T> void`
`[setFirstValue](#setFirstValue(java.util.Collection,T))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection,
 T value)`
Set the first value of the given collection.
`static <T> void`
`[setSingleValue](#setSingleValue(java.util.Collection,T))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection,
 T value)`
Removes all values from a given collection and adds a new one.
`static <T> boolean`
`[startsWith](#startsWith(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> prefixCollection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)`
Checks if a collection starts with prefixCollection
 Example: a collection is [A, B, C], prefixCollection is [A, B], the result would be true.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[stringToMap](#stringToMap(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) input)`
Deserialize map from string.
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[toOptimizedCacheCollection](#toOptimizedCacheCollection(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)`
Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance
`static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[toOptimizedContainsCollection](#toOptimizedContainsCollection(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)`
Wrap the specified collection into a containable collection that ensures
 optimized {{Collection.contains()}} performance.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CollectionUtils
public CollectionUtils()
 ============ METHOD DETAIL ========== 
Method Details
convert
public static <S,
T,
C extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>> C convert([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<S> source,
 C target,
 [Converter](Converter.html)<? super S,? super T> converter)
Convert one (source) collection into another (target) collection.
 Converts each source element and adds a converted element to a target collection.
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
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends T> source,
 boolean allowDuplication)
Append a source to a target collection.
Parameters:
`target` - target
`source` - source
`allowDuplication` - do not check for an already added element if true
Returns:
appended collection
append
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication)
Append a source to a target collection.
Parameters:
`target` - target
`sourceIterator` - source iterator.
`allowDuplication` - do not check for an already added element if true
Returns:
appended collection
append
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<? extends T> sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)
Append a source to a target collection.
Parameters:
`target` - target
`sourceIterator` - source iterator.
`allowDuplication` - do not check for an already added element if true
`allowNulls` - allows nulls
Returns:
appended collection
append
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> target,
 T[] source,
 boolean allowDuplication)
Append source array to a target collection.
Parameters:
`target` - target
`source` - source
`allowDuplication` - do not check for an already added element if true
Returns:
appended vector
contains
public static boolean contains([Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html) it,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
Checks if given iterator contains a given object.
Parameters:
`it` - the iterator.
`o` - the object.
Returns:
true, if it contains o.
containsAny
public static boolean containsAny([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) location,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) what)
Returns true if location contains any element from what
Parameters:
`location` - location collection
`what` - what collection.
Returns:
boolean.
createCollection
public static <C extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<E>,
E> C createCollection([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<C> collection,
 [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<E> it)
Creates a given type collection and fills it with objects from given iterator
Parameters:
`collection` - type collection.
`it` - The given iterator.
Returns:
the result collection.
notDuplicatedList
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> notDuplicatedList([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)
Removes duplicates from a given collection. After remove, one element will be in collection only once.
Parameters:
`collection` - collection to operate with (makes sense when a collection is a list (sets can't have identical elements)).
Returns:
collection.
createStringRepresentation
public static <T> [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createStringRepresentation([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<T,[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> converter)
Create string representation of a given collection.
Parameters:
`collection` - collection
`delimiter` - values delimiter
`converter` - convert an object to string
Returns:
string representation of a collection
createFromStringRepresentation
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> createFromStringRepresentation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) delimiter,
 [Converter](Converter.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),T> converter)
Create a collection from string.
Parameters:
`string` - string representation.
`delimiter` - values delimiter.
`converter` - convert string to object.
Returns:
collection.
leaveElements
public static void leaveElements([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) elements,
 int numberToLeave)
Leaves a given number of first elements in the collection.
Parameters:
`elements` - elements to filter.
`numberToLeave` - number of elements to leave.
mapToString
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) mapToString([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> map)
Serializes a map to string.
Parameters:
`map` - map to serialize.
Returns:
string representation of the map.
stringToMap
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> stringToMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) input)
Deserialize map from string.
Parameters:
`input` - input string.
Returns:
map.
filterByClassType
public static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> filterByClassType([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> input,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)
Filters and casts a collection from one type to another
Type Parameters:
`T` - type
Parameters:
`input` - input collection
`type` - desired output collection type
Returns:
new typed list
filterByClassType
public static <T> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> filterByClassType([Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<?> stream,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)
Filter and map according given class.
Parameters:
`stream` - stream to filer and map
`type` - desired output stream type
Returns:
filtered and mapped stream
findByClassType
@CheckForNullpublic static <T> T findByClassType([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> input,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)
Looks for an object of give class in the given collection.
Type Parameters:
`T` - type
Parameters:
`input` - input collection
`type` - desired output collection type
Returns:
found an object
anyMatch
public static <T> boolean anyMatch([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)
Looks for any object matching given predicate.
Parameters:
`input` - input collection
`predicate` - predicate to test
Returns:
true if any object in input collection matches the predicated. False if a collection is empty.
allMatch
public static <T> boolean allMatch([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)
Check if all objects match given predicate.
Parameters:
`input` - input collection
`predicate` - predicate to test
Returns:
true if all objects in input collection match the predicated. True if a collection is empty.
noneMatch
public static <T> boolean noneMatch([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)
Check if no object matches given predicate.
Parameters:
`input` - input collection
`predicate` - predicate to test
Returns:
true if input does not contain element matching predicate
find
@CheckForNullpublic static <T> T find([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> input,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)
Looks for object matching given predicate.
Parameters:
`input` - input collection
`predicate` - predicate to test
Returns:
found an object
find
@CheckForNullpublic static <T> T find([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) input,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> castClass)
Looks for object matching given class.
Parameters:
`input` - input collection
`castClass` - class to test
Returns:
found an object
setSingleValue
public static <T> void setSingleValue([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection,
 T value)
Removes all values from a given collection and adds a new one.
Parameters:
`collection` - collection
`value` - a new value
setFirstValue
public static <T> void setFirstValue([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection,
 @CheckForNull
 T value)
Set the first value of the given collection.
 If a collection is empty, add a new value.
 If the value is null, remove the first value from a collection.
Parameters:
`collection` - collection
`value` - a new value
toOptimizedContainsCollection
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> toOptimizedContainsCollection([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)
Wrap the specified collection into a containable collection that ensures
 optimized {{Collection.contains()}} performance.
 The provided collection should not change while the wrapped collection is used.
Parameters:
`collection` - a collection to wrap into a containable collection
Returns:
return wrapped collection.
toOptimizedCacheCollection
public static <T> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> toOptimizedCacheCollection([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)
Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance
 Returned collection in unmodifiable
equals
public static boolean equals([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection1,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> collection2)
Checks if both collections are equal - size the same and elements by order are the same
Parameters:
`collection1` - first collection
`collection2` - second collection
Returns:
true if size the same and elements by order are the same
addIfNotNull
public static <T> void addIfNotNull(@CheckForNull
 T element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)
Adds the given element to the collection unless it is null.
Parameters:
`element` - nullable element to add
`collection` - modifiable collection
copyAndAdd
public static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> copyAndAdd(@CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list,
 T element)
Creates copy of the given list, or new list if null is provided.
 Then adds the given element and returns the copy.
Parameters:
`list` - nullable list to create copy of
`element` - element to add
Returns:
copied and appended List
copyAndAdd
public static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> copyAndAdd(@CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> toAdd)
Creates copy of the given list, or new list if null is provided.
 Then adds the given collection at the end and returns the copy.
Parameters:
`list` - nullable list to create copy of
`toAdd` - collection to add
Returns:
copied and appended List
startsWith
public static <T> boolean startsWith([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> prefixCollection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)
Checks if a collection starts with prefixCollection
 Example: a collection is [A, B, C], prefixCollection is [A, B], the result would be true.
Parameters:
`prefixCollection` - collection that another collection potentially starts with
`collection` - collection to check in
Returns:
true if starts with prefixCollection, including when collections are equal
endsWith
public static <T> boolean endsWith([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> postfixCollection,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)
Checks if a collection ends with postfixCollection
 Example: a collection is [A, B, C], postfixCollection is [B, C], the result would be true.
Parameters:
`postfixCollection` - collection that another collection potentially ends with
`collection` - collection to check in
Returns:
true if ends with postfixCollection, including when collections are equal
listOf
public static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> listOf(@CheckForNull
 T element)
Creates unmodifiable [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) with a given element. Or empty unmodifiable list if element is null.
Type Parameters:
`T` - any object
Parameters:
`element` - element
Returns:
list
listOf
public static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> listOf(@CheckForNull
 T element,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list)
Appends a given element to new unmodifiable [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) constructed from the given list.
 Returns the given list if an element is null.
Type Parameters:
`T` - any object
Parameters:
`element` - element
`list` - list
Returns:
list
removeIf
public static <T> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> removeIf([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate)
Removes elements from the given list that don't match the predicate.
 Returns unmodifiable list and supports an unmodifiable list as input.
Type Parameters:
`T` - any object
Parameters:
`list` - list to operate with
`predicate` - predicate
Returns:
list
checkOrder
public static <T> boolean checkOrder([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list1,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list2)
This method checks if the elements in both lists have the same order.
 It doesn't matter if one list is bigger than the other,
 but the smaller list's order should match the larger list's order.
Type Parameters:
`T` - any object
Parameters:
`list1` - list
`list2` - list
Returns:
Return true if any of the lists is empty or equal or if the order of the elements is the same. Return false if the order of elements is different.
find
@CheckForNullpublic static <T> T find([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>> collection1,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>> collection2,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> predicate,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)
Looks for object matching given predicate in the first collection and then in the second.
Parameters:
`collection1` - first collection
`collection2` - second collection
`predicate` - predicate to test
`type` - object type
Returns:
found an object
mergeInto
public static <T> void mergeInto([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list1,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> list2)
Merges elements from list2 into list1, taking into account overlapping sequences.
 The longest suffix of list1 that matches a prefix of list2 is detected,
 and only the non-overlapping elements from list2 are added to list1.
Type Parameters:
`T` - the type of elements in the lists
Parameters:
`list1` - the first list to be extended (will be modified)
`list2` - the second list (remains unchanged)
getFirst
@CheckForNullpublic static <T> T getFirst([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> collection)
Gets the first element of this collection or null if a collection is empty.
Parameters:
`collection` - collection
Returns:
first element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.utils</a></div>
<h1 class="title" title="Class CollectionUtils">Class CollectionUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.utils.CollectionUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CollectionUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addIfNotNull(T,java.util.Collection)">addIfNotNull</a><wbr/>(T element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds the given element to the collection unless it is null.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#allMatch(java.util.Collection,java.util.function.Predicate)">allMatch</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if all objects match given predicate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#anyMatch(java.util.Collection,java.util.function.Predicate)">anyMatch</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for any object matching given predicate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Collection,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt; source,
 boolean allowDuplication)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append a source to a target collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Iterator,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append a source to a target collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Iterator,boolean,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append a source to a target collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.Collection,T%5B%5D,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 T[] source,
 boolean allowDuplication)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Append source array to a target collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkOrder(java.util.List,java.util.List)">checkOrder</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">This method checks if the elements in both lists have the same order.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#contains(java.util.Iterator,java.lang.Object)">contains</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given iterator contains a given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#containsAny(java.util.Collection,java.util.Collection)">containsAny</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> location,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> what)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if location contains any element from what</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;S,<wbr/>
T,<wbr/>
C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;&gt;<br/>C</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.util.Collection,C,com.nomagic.utils.Converter)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;S&gt; source,
 C target,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;? super S,<wbr/>? super T&gt; converter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert one (source) collection into another (target) collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyAndAdd(java.util.List,java.util.Collection)">copyAndAdd</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; toAdd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates copy of the given list, or new list if null is provided.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyAndAdd(java.util.List,T)">copyAndAdd</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list,
 T element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates copy of the given list, or new list if null is provided.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;,<wbr/>
E&gt;<br/>C</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCollection(java.lang.Class,java.util.Iterator)">createCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;C&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;E&gt; it)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a given type collection and fills it with objects from given iterator</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createFromStringRepresentation(java.lang.String,java.lang.String,com.nomagic.utils.Converter)">createFromStringRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>T&gt; converter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a collection from string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringRepresentation(java.util.Collection,java.lang.String,com.nomagic.utils.Converter)">createStringRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; converter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create string representation of a given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#endsWith(java.util.Collection,java.util.Collection)">endsWith</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; postfixCollection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if a collection ends with postfixCollection
 Example: a collection is [A, B, C], postfixCollection is [B, C], the result would be true.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.util.Collection,java.util.Collection)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if both collections are equal - size the same and elements by order are the same</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterByClassType(java.util.Collection,java.lang.Class)">filterByClassType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters and casts a collection from one type to another</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterByClassType(java.util.stream.Stream,java.lang.Class)">filterByClassType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;?&gt; stream,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filter and map according given class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.util.function.Predicate)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for object matching given predicate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.Class)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; castClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for object matching given class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.function.Supplier,java.util.function.Supplier,java.util.function.Predicate,java.lang.Class)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;&gt; collection2,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for object matching given predicate in the first collection and then in the second.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findByClassType(java.util.Collection,java.lang.Class)">findByClassType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for an object of give class in the given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirst(java.util.Collection)">getFirst</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the first element of this collection or null if a collection is empty.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#leaveElements(java.util.List,int)">leaveElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> elements,
 int numberToLeave)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Leaves a given number of first elements in the collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#listOf(T)">listOf</a><wbr/>(T element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates unmodifiable <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> with a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#listOf(T,java.util.List)">listOf</a><wbr/>(T element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Appends a given element to new unmodifiable <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> constructed from the given list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#mapToString(java.util.Map)">mapToString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; map)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Serializes a map to string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeInto(java.util.List,java.util.List)">mergeInto</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Merges elements from list2 into list1, taking into account overlapping sequences.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#noneMatch(java.util.Collection,java.util.function.Predicate)">noneMatch</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if no object matches given predicate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#notDuplicatedList(java.util.Collection)">notDuplicatedList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes duplicates from a given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeIf(java.util.List,java.util.function.Predicate)">removeIf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes elements from the given list that don't match the predicate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFirstValue(java.util.Collection,T)">setFirstValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 T value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set the first value of the given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSingleValue(java.util.Collection,T)">setSingleValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 T value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all values from a given collection and adds a new one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#startsWith(java.util.Collection,java.util.Collection)">startsWith</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; prefixCollection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if a collection starts with prefixCollection
 Example: a collection is [A, B, C], prefixCollection is [A, B], the result would be true.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#stringToMap(java.lang.String)">stringToMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> input)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Deserialize map from string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toOptimizedCacheCollection(java.util.Collection)">toOptimizedCacheCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toOptimizedContainsCollection(java.util.Collection)">toOptimizedContainsCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Wrap the specified collection into a containable collection that ensures
 optimized {{Collection.contains()}} performance.</div>
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
C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;&gt;</span> <span class="return-type">C</span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;S&gt; source,
 C target,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;? super S,<wbr/>? super T&gt; converter)</span></div>
<div class="block">Convert one (source) collection into another (target) collection.
 Converts each source element and adds a converted element to a target collection.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt; source,
 boolean allowDuplication)</span></div>
<div class="block">Append a source to a target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>source</code> - source</dd>
<dd><code>allowDuplication</code> - do not check for an already added element if true</dd>
<dt>Returns:</dt>
<dd>appended collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,java.util.Iterator,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication)</span></div>
<div class="block">Append a source to a target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>sourceIterator</code> - source iterator.</dd>
<dd><code>allowDuplication</code> - do not check for an already added element if true</dd>
<dt>Returns:</dt>
<dd>appended collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,java.util.Iterator,boolean,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; sourceIterator,
 boolean allowDuplication,
 boolean allowNulls)</span></div>
<div class="block">Append a source to a target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>sourceIterator</code> - source iterator.</dd>
<dd><code>allowDuplication</code> - do not check for an already added element if true</dd>
<dd><code>allowNulls</code> - allows nulls</dd>
<dt>Returns:</dt>
<dd>appended collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,T[],boolean)">
<h3 id="append(java.util.Collection,java.lang.Object[],boolean)">append</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; target,
 T[] source,
 boolean allowDuplication)</span></div>
<div class="block">Append source array to a target collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target</dd>
<dd><code>source</code> - source</dd>
<dd><code>allowDuplication</code> - do not check for an already added element if true</dd>
<dt>Returns:</dt>
<dd>appended vector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contains(java.util.Iterator,java.lang.Object)">
<h3>contains</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Checks if given iterator contains a given object.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">containsAny</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> location,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> what)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;,<wbr/>
E&gt;</span> <span class="return-type">C</span> <span class="element-name">createCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;C&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;E&gt; it)</span></div>
<div class="block">Creates a given type collection and fills it with objects from given iterator</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">notDuplicatedList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Removes duplicates from a given collection. After remove, one element will be in collection only once.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection to operate with (makes sense when a collection is a list (sets can't have identical elements)).</dd>
<dt>Returns:</dt>
<dd>collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringRepresentation(java.util.Collection,java.lang.String,com.nomagic.utils.Converter)">
<h3>createStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStringRepresentation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;T,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; converter)</span></div>
<div class="block">Create string representation of a given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection</dd>
<dd><code>delimiter</code> - values delimiter</dd>
<dd><code>converter</code> - convert an object to string</dd>
<dt>Returns:</dt>
<dd>string representation of a collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFromStringRepresentation(java.lang.String,java.lang.String,com.nomagic.utils.Converter)">
<h3>createFromStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">createFromStringRepresentation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a href="Converter.html" title="interface in com.nomagic.utils">Converter</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>T&gt; converter)</span></div>
<div class="block">Create a collection from string.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">leaveElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> elements,
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">mapToString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; map)</span></div>
<div class="block">Serializes a map to string.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">stringToMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> input)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">filterByClassType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
<div class="block">Filters and casts a collection from one type to another</div>
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
<section class="detail" id="filterByClassType(java.util.stream.Stream,java.lang.Class)">
<h3>filterByClassType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">filterByClassType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;?&gt; stream,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
<div class="block">Filter and map according given class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stream</code> - stream to filer and map</dd>
<dd><code>type</code> - desired output stream type</dd>
<dt>Returns:</dt>
<dd>filtered and mapped stream</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findByClassType(java.util.Collection,java.lang.Class)">
<h3>findByClassType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">findByClassType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
<div class="block">Looks for an object of give class in the given collection.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - type</dd>
<dt>Parameters:</dt>
<dd><code>input</code> - input collection</dd>
<dd><code>type</code> - desired output collection type</dd>
<dt>Returns:</dt>
<dd>found an object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="anyMatch(java.util.Collection,java.util.function.Predicate)">
<h3>anyMatch</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">boolean</span> <span class="element-name">anyMatch</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</span></div>
<div class="block">Looks for any object matching given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input collection</dd>
<dd><code>predicate</code> - predicate to test</dd>
<dt>Returns:</dt>
<dd>true if any object in input collection matches the predicated. False if a collection is empty.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="allMatch(java.util.Collection,java.util.function.Predicate)">
<h3>allMatch</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">boolean</span> <span class="element-name">allMatch</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</span></div>
<div class="block">Check if all objects match given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input collection</dd>
<dd><code>predicate</code> - predicate to test</dd>
<dt>Returns:</dt>
<dd>true if all objects in input collection match the predicated. True if a collection is empty.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="noneMatch(java.util.Collection,java.util.function.Predicate)">
<h3>noneMatch</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">boolean</span> <span class="element-name">noneMatch</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</span></div>
<div class="block">Check if no object matches given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input collection</dd>
<dd><code>predicate</code> - predicate to test</dd>
<dt>Returns:</dt>
<dd>true if input does not contain element matching predicate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.util.function.Predicate)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</span></div>
<div class="block">Looks for object matching given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input collection</dd>
<dd><code>predicate</code> - predicate to test</dd>
<dt>Returns:</dt>
<dd>found an object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.Class)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; castClass)</span></div>
<div class="block">Looks for object matching given class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input collection</dd>
<dd><code>castClass</code> - class to test</dd>
<dt>Returns:</dt>
<dd>found an object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSingleValue(java.util.Collection,T)">
<h3 id="setSingleValue(java.util.Collection,java.lang.Object)">setSingleValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">setSingleValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">setFirstValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 @CheckForNull
 T value)</span></div>
<div class="block">Set the first value of the given collection.
 If a collection is empty, add a new value.
 If the value is null, remove the first value from a collection.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">toOptimizedContainsCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Wrap the specified collection into a containable collection that ensures
 optimized {{Collection.contains()}} performance.
 The provided collection should not change while the wrapped collection is used.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - a collection to wrap into a containable collection</dd>
<dt>Returns:</dt>
<dd>return wrapped collection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toOptimizedCacheCollection(java.util.Collection)">
<h3>toOptimizedCacheCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">toOptimizedCacheCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Optimized for
 1) minimal memory footprint, for the stored cache data to be as small as possible
 2) contains() performance, while preserving iteration order and performance
 <p>
 Returned collection in unmodifiable</p></div>
</section>
</li>
<li>
<section class="detail" id="equals(java.util.Collection,java.util.Collection)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection2)</span></div>
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
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Adds the given element to the collection unless it is null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - nullable element to add</dd>
<dd><code>collection</code> - modifiable collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyAndAdd(java.util.List,T)">
<h3 id="copyAndAdd(java.util.List,java.lang.Object)">copyAndAdd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">copyAndAdd</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list,
 T element)</span></div>
<div class="block">Creates copy of the given list, or new list if null is provided.
 Then adds the given element and returns the copy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>list</code> - nullable list to create copy of</dd>
<dd><code>element</code> - element to add</dd>
<dt>Returns:</dt>
<dd>copied and appended List</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyAndAdd(java.util.List,java.util.Collection)">
<h3>copyAndAdd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">copyAndAdd</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; toAdd)</span></div>
<div class="block">Creates copy of the given list, or new list if null is provided.
 Then adds the given collection at the end and returns the copy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>list</code> - nullable list to create copy of</dd>
<dd><code>toAdd</code> - collection to add</dd>
<dt>Returns:</dt>
<dd>copied and appended List</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startsWith(java.util.Collection,java.util.Collection)">
<h3>startsWith</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">boolean</span> <span class="element-name">startsWith</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; prefixCollection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Checks if a collection starts with prefixCollection
 Example: a collection is [A, B, C], prefixCollection is [A, B], the result would be true.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prefixCollection</code> - collection that another collection potentially starts with</dd>
<dd><code>collection</code> - collection to check in</dd>
<dt>Returns:</dt>
<dd>true if starts with prefixCollection, including when collections are equal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="endsWith(java.util.Collection,java.util.Collection)">
<h3>endsWith</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">boolean</span> <span class="element-name">endsWith</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; postfixCollection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Checks if a collection ends with postfixCollection
 Example: a collection is [A, B, C], postfixCollection is [B, C], the result would be true.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>postfixCollection</code> - collection that another collection potentially ends with</dd>
<dd><code>collection</code> - collection to check in</dd>
<dt>Returns:</dt>
<dd>true if ends with postfixCollection, including when collections are equal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listOf(T)">
<h3 id="listOf(java.lang.Object)">listOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">listOf</span><wbr/><span class="parameters">(@CheckForNull
 T element)</span></div>
<div class="block">Creates unmodifiable <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> with a given element. Or empty unmodifiable list if element is null.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - any object</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listOf(T,java.util.List)">
<h3 id="listOf(java.lang.Object,java.util.List)">listOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">listOf</span><wbr/><span class="parameters">(@CheckForNull
 T element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list)</span></div>
<div class="block">Appends a given element to new unmodifiable <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> constructed from the given list.
 Returns the given list if an element is null.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - any object</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>list</code> - list</dd>
<dt>Returns:</dt>
<dd>list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIf(java.util.List,java.util.function.Predicate)">
<h3>removeIf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">removeIf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate)</span></div>
<div class="block">Removes elements from the given list that don't match the predicate.
 Returns unmodifiable list and supports an unmodifiable list as input.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - any object</dd>
<dt>Parameters:</dt>
<dd><code>list</code> - list to operate with</dd>
<dd><code>predicate</code> - predicate</dd>
<dt>Returns:</dt>
<dd>list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkOrder(java.util.List,java.util.List)">
<h3>checkOrder</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">boolean</span> <span class="element-name">checkOrder</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list2)</span></div>
<div class="block">This method checks if the elements in both lists have the same order.
 It doesn't matter if one list is bigger than the other,
 but the smaller list's order should match the larger list's order.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - any object</dd>
<dt>Parameters:</dt>
<dd><code>list1</code> - list</dd>
<dd><code>list2</code> - list</dd>
<dt>Returns:</dt>
<dd>Return true if any of the lists is empty or equal or if the order of the elements is the same. Return false if the order of elements is different.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.function.Supplier,java.util.function.Supplier,java.util.function.Predicate,java.lang.Class)">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;&gt; collection2,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; predicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
<div class="block">Looks for object matching given predicate in the first collection and then in the second.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection1</code> - first collection</dd>
<dd><code>collection2</code> - second collection</dd>
<dd><code>predicate</code> - predicate to test</dd>
<dd><code>type</code> - object type</dd>
<dt>Returns:</dt>
<dd>found an object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mergeInto(java.util.List,java.util.List)">
<h3>mergeInto</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">mergeInto</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; list2)</span></div>
<div class="block">Merges elements from list2 into list1, taking into account overlapping sequences.
 The longest suffix of list1 that matches a prefix of list2 is detected,
 and only the non-overlapping elements from list2 are added to list1.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - the type of elements in the lists</dd>
<dt>Parameters:</dt>
<dd><code>list1</code> - the first list to be extended (will be modified)</dd>
<dd><code>list2</code> - the second list (remains unchanged)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirst(java.util.Collection)">
<h3>getFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">getFirst</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection)</span></div>
<div class="block">Gets the first element of this collection or null if a collection is empty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection</dd>
<dt>Returns:</dt>
<dd>first element</dd>
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
