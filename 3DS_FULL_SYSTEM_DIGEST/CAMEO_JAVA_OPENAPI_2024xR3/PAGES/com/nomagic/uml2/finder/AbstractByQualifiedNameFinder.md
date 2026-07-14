# JAVA OPENAPI: AbstractByQualifiedNameFinder (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/finder/AbstractByQualifiedNameFinder.html
- source_path: `com/nomagic/uml2/finder/AbstractByQualifiedNameFinder.html`
- source_sha256: `b0dd286512ae8bfe670178691ebc2c6ac299d06952f9131acec1453a8c586fef`
- captured_utc: `2026-07-14T16:56:26.339804+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.finder](package-summary.html)

## Class AbstractByQualifiedNameFinder<R extends com.nomagic.uml2.project.ElementProject>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.finder.BaseFinder
com.nomagic.uml2.finder.AbstractByQualifiedNameFinder<R>

Direct Known Subclasses:
`[Finder.ByQualifiedNameFinder](../../magicdraw/uml/Finder.ByQualifiedNameFinder.html)`

@OpenApiAllpublic abstract classAbstractByQualifiedNameFinder<R extends com.nomagic.uml2.project.ElementProject>
extends com.nomagic.uml2.finder.BaseFinder

Search for elements by qualified name

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PACKAGE_SEPARATOR](#PACKAGE_SEPARATOR)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractByQualifiedNameFinder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[find](#find(java.util.Collection,java.lang.String,java.lang.Class%5B%5D))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> parents,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Finds element with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,java.lang.String,java.lang.Class%5B%5D,boolean,java.util.function.BiPredicate))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> parents,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean searchJustOne,
 [BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> compareBiPredicate)`
Finds elements with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[find](#find(R,java.lang.String))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)`
Find Element with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[find](#find(R,java.lang.String,java.lang.Class%5B%5D))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Finds element with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(R,java.lang.String,java.lang.Class%5B%5D,boolean))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] type,
 boolean searchJustOne)`
Finds elements with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(R,java.lang.String,java.lang.Class%5B%5D,boolean,java.util.function.BiPredicate))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean searchJustOne,
 [BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> compareBiPredicate)`
Finds elements with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[find](#find(R,java.lang.String,java.lang.Class))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> type)`
Finds element with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(R,java.lang.String,java.lang.Class,boolean))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> type,
 boolean searchJustOne)`
Finds elements with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findIgnoreCase](#findIgnoreCase(R,java.lang.String))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)`
Find Element with a given qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[findIgnoreCase](#findIgnoreCase(R,java.lang.String,java.lang.Class%5B%5D,boolean))([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] type,
 boolean searchJustOne)`
Finds elements with a given qualified name but ignores lower and upper cases.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findRelative](#findRelative(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class%5B%5D))([Element](../ext/magicdraw/classes/mdkernel/Element.html) root,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] type)`
Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findRelative](#findRelative(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class))([Element](../ext/magicdraw/classes/mdkernel/Element.html) root,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> type)`
Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.
`boolean`
`[isFinalPartOfQualifiedName](#isFinalPartOfQualifiedName(java.util.Collection,int))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> pathElements,
 int i)`
Deprecated, for removal: This API element is subject to removal in a future version.
will be removed
`<T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> 
boolean`
`[isMatchingElement](#isMatchingElement(java.util.function.BiPredicate,java.util.Collection,java.util.Collection,int,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> compareBiPredicate,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> pathElements,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T>> typeSet,
 int i,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Element](../ext/magicdraw/classes/mdkernel/Element.html) el)`
Deprecated, for removal: This API element is subject to removal in a future version.
will be removed
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[splitQualifiedName](#splitQualifiedName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)`
Deprecated, for removal: This API element is subject to removal in a future version.
will be removed
Methods inherited from class com.nomagic.uml2.finder.BaseFinder
`hasName, toRoots, toRoots, toSet, toTypes`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PACKAGE_SEPARATOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PACKAGE_SEPARATOR
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.uml2.finder.AbstractByQualifiedNameFinder.PACKAGE_SEPARATOR)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractByQualifiedNameFinder
public AbstractByQualifiedNameFinder()
 ============ METHOD DETAIL ========== 
Method Details
find
@CheckForNullpublic <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> T find([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)
Find Element with a given qualified name.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
Returns:
Element or null
findIgnoreCase
@CheckForNullpublic <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> T findIgnoreCase([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)
Find Element with a given qualified name.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
Returns:
Element or null
find
@CheckForNullpublic <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> T find([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> type)
Finds element with a given qualified name.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
`type` - strict class type of element. Null mean any type.
Returns:
Element or null
find
@CheckForNullpublic <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> T find([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Finds element with a given qualified name.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
`types` - strict class type of element. Null mean any type.
Returns:
Element or null
find
@CheckForNullpublic <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> T find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> parents,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Finds element with a given qualified name.
Parameters:
`parents` - root elements to start search from
`qualifiedName` - qualified name of Element
`types` - strict class type of element. Null mean any type.
Returns:
Element or null
find
public <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> type,
 boolean searchJustOne)
Finds elements with a given qualified name.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
`type` - strict class type of element. Null mean any type
`searchJustOne` - stop search if one element is found
Returns:
all elements with a given qualified name
findIgnoreCase
public <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> findIgnoreCase([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] type,
 boolean searchJustOne)
Finds elements with a given qualified name but ignores lower and upper cases.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
`type` - strict class type of element. Null mean any type
`searchJustOne` - stop search if one element is found
Returns:
all elements with a given qualified name with ignored lower and upper cases.
find
public <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] type,
 boolean searchJustOne)
Finds elements with a given qualified name.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
`type` - strict class type of element. Null mean any type
`searchJustOne` - stop search if one element is found
Returns:
all elements with a given qualified name
find
public <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([R](AbstractByQualifiedNameFinder.html) elementProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean searchJustOne,
 [BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> compareBiPredicate)
Finds elements with a given qualified name.
Parameters:
`elementProject` - provides root elements to start search from
`qualifiedName` - qualified name of Element
`types` - strict class types of element. Null mean any types
`searchJustOne` - stop search if one element is found
`compareBiPredicate` - check for element naming
Returns:
all elements with a given qualified name
find
public <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> parents,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean searchJustOne,
 [BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> compareBiPredicate)
Finds elements with a given qualified name.
Parameters:
`parents` - root elements to start search from
`qualifiedName` - qualified name of Element
`types` - strict class types of element. Null mean any types
`searchJustOne` - stop search if one element is found
`compareBiPredicate` - check for element naming
Returns:
all elements with a given qualified name
findRelative
@CheckForNullpublic <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> T findRelative([Element](../ext/magicdraw/classes/mdkernel/Element.html) root,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> type)
Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.
Parameters:
`root` - scope Element
`qualifiedName` - qualified name of element
`type` - strict class type of element. Nulls means any element
Returns:
Element or null
findRelative
@CheckForNullpublic <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> T findRelative([Element](../ext/magicdraw/classes/mdkernel/Element.html) root,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] type)
Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.
Parameters:
`root` - scope Element
`qualifiedName` - qualified name of element
`type` - strict class type of element. Nulls means any element
Returns:
Element or null
isMatchingElement
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public <T extends [Element](../ext/magicdraw/classes/mdkernel/Element.html)> boolean isMatchingElement([BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> compareBiPredicate,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> pathElements,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T>> typeSet,
 int i,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Element](../ext/magicdraw/classes/mdkernel/Element.html) el)
Deprecated, for removal: This API element is subject to removal in a future version.
will be removed
isFinalPartOfQualifiedName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public boolean isFinalPartOfQualifiedName([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> pathElements,
 int i)
Deprecated, for removal: This API element is subject to removal in a future version.
will be removed
splitQualifiedName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> splitQualifiedName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)
Deprecated, for removal: This API element is subject to removal in a future version.
will be removed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.finder</a></div>
<h1 class="title" title="Class AbstractByQualifiedNameFinder">Class AbstractByQualifiedNameFinder&lt;R extends com.nomagic.uml2.project.ElementProject&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.finder.BaseFinder
<div class="inheritance">com.nomagic.uml2.finder.AbstractByQualifiedNameFinder&lt;R&gt;</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../magicdraw/uml/Finder.ByQualifiedNameFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByQualifiedNameFinder</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractByQualifiedNameFinder&lt;R extends com.nomagic.uml2.project.ElementProject&gt;</span>
<span class="extends-implements">extends com.nomagic.uml2.finder.BaseFinder</span></div>
<div class="block">Search for elements by qualified name</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_SEPARATOR">PACKAGE_SEPARATOR</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractByQualifiedNameFinder</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.String,java.lang.Class%5B%5D)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; parents,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds element with a given qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.String,java.lang.Class%5B%5D,boolean,java.util.function.BiPredicate)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; parents,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean searchJustOne,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html" title="class or interface in java.util.function">BiPredicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; compareBiPredicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements with a given qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(R,java.lang.String)">find</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find Element with a given qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(R,java.lang.String,java.lang.Class%5B%5D)">find</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds element with a given qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(R,java.lang.String,java.lang.Class%5B%5D,boolean)">find</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean searchJustOne)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements with a given qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(R,java.lang.String,java.lang.Class%5B%5D,boolean,java.util.function.BiPredicate)">find</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean searchJustOne,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html" title="class or interface in java.util.function">BiPredicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; compareBiPredicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements with a given qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(R,java.lang.String,java.lang.Class)">find</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds element with a given qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(R,java.lang.String,java.lang.Class,boolean)">find</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; type,
 boolean searchJustOne)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements with a given qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIgnoreCase(R,java.lang.String)">findIgnoreCase</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find Element with a given qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIgnoreCase(R,java.lang.String,java.lang.Class%5B%5D,boolean)">findIgnoreCase</a><wbr/>(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean searchJustOne)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements with a given qualified name but ignores lower and upper cases.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelative(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class%5B%5D)">findRelative</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelative(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class)">findRelative</a><wbr/>(<a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isFinalPartOfQualifiedName(java.util.Collection,int)">isFinalPartOfQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; pathElements,
 int i)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">will be removed</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isMatchingElement(java.util.function.BiPredicate,java.util.Collection,java.util.Collection,int,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isMatchingElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html" title="class or interface in java.util.function">BiPredicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; compareBiPredicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; pathElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt;&gt; typeSet,
 int i,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> el)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">will be removed</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#splitQualifiedName(java.lang.String)">splitQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">will be removed</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.finder.BaseFinder">Methods inherited from class com.nomagic.uml2.finder.BaseFinder</h3>
<code>hasName, toRoots, toRoots, toSet, toTypes</code></div>
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
<section class="detail" id="PACKAGE_SEPARATOR">
<h3>PACKAGE_SEPARATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PACKAGE_SEPARATOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.uml2.finder.AbstractByQualifiedNameFinder.PACKAGE_SEPARATOR">Constant Field Values</a></li>
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
<h3>AbstractByQualifiedNameFinder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractByQualifiedNameFinder</span>()</div>
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
<section class="detail" id="find(R,java.lang.String)">
<h3 id="find(com.nomagic.uml2.project.ElementProject,java.lang.String)">find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block">Find Element with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dt>Returns:</dt>
<dd>Element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIgnoreCase(R,java.lang.String)">
<h3 id="findIgnoreCase(com.nomagic.uml2.project.ElementProject,java.lang.String)">findIgnoreCase</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findIgnoreCase</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block">Find Element with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dt>Returns:</dt>
<dd>Element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(R,java.lang.String,java.lang.Class)">
<h3 id="find(com.nomagic.uml2.project.ElementProject,java.lang.String,java.lang.Class)">find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; type)</span></div>
<div class="block">Finds element with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>type</code> - strict class type of element. Null mean any type.</dd>
<dt>Returns:</dt>
<dd>Element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(R,java.lang.String,java.lang.Class[])">
<h3 id="find(com.nomagic.uml2.project.ElementProject,java.lang.String,java.lang.Class[])">find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Finds element with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>types</code> - strict class type of element. Null mean any type.</dd>
<dt>Returns:</dt>
<dd>Element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.String,java.lang.Class[])">
<h3>find</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; parents,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Finds element with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parents</code> - root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>types</code> - strict class type of element. Null mean any type.</dd>
<dt>Returns:</dt>
<dd>Element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(R,java.lang.String,java.lang.Class,boolean)">
<h3 id="find(com.nomagic.uml2.project.ElementProject,java.lang.String,java.lang.Class,boolean)">find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; type,
 boolean searchJustOne)</span></div>
<div class="block">Finds elements with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>type</code> - strict class type of element. Null mean any type</dd>
<dd><code>searchJustOne</code> - stop search if one element is found</dd>
<dt>Returns:</dt>
<dd>all elements with a given qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIgnoreCase(R,java.lang.String,java.lang.Class[],boolean)">
<h3 id="findIgnoreCase(com.nomagic.uml2.project.ElementProject,java.lang.String,java.lang.Class[],boolean)">findIgnoreCase</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">findIgnoreCase</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean searchJustOne)</span></div>
<div class="block">Finds elements with a given qualified name but ignores lower and upper cases.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>type</code> - strict class type of element. Null mean any type</dd>
<dd><code>searchJustOne</code> - stop search if one element is found</dd>
<dt>Returns:</dt>
<dd>all elements with a given qualified name with ignored lower and upper cases.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(R,java.lang.String,java.lang.Class[],boolean)">
<h3 id="find(com.nomagic.uml2.project.ElementProject,java.lang.String,java.lang.Class[],boolean)">find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type,
 boolean searchJustOne)</span></div>
<div class="block">Finds elements with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>type</code> - strict class type of element. Null mean any type</dd>
<dd><code>searchJustOne</code> - stop search if one element is found</dd>
<dt>Returns:</dt>
<dd>all elements with a given qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(R,java.lang.String,java.lang.Class[],boolean,java.util.function.BiPredicate)">
<h3 id="find(com.nomagic.uml2.project.ElementProject,java.lang.String,java.lang.Class[],boolean,java.util.function.BiPredicate)">find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="AbstractByQualifiedNameFinder.html" title="type parameter in AbstractByQualifiedNameFinder">R</a> elementProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean searchJustOne,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html" title="class or interface in java.util.function">BiPredicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; compareBiPredicate)</span></div>
<div class="block">Finds elements with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementProject</code> - provides root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>types</code> - strict class types of element. Null mean any types</dd>
<dd><code>searchJustOne</code> - stop search if one element is found</dd>
<dd><code>compareBiPredicate</code> - check for element naming</dd>
<dt>Returns:</dt>
<dd>all elements with a given qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.String,java.lang.Class[],boolean,java.util.function.BiPredicate)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; parents,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean searchJustOne,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html" title="class or interface in java.util.function">BiPredicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; compareBiPredicate)</span></div>
<div class="block">Finds elements with a given qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parents</code> - root elements to start search from</dd>
<dd><code>qualifiedName</code> - qualified name of Element</dd>
<dd><code>types</code> - strict class types of element. Null mean any types</dd>
<dd><code>searchJustOne</code> - stop search if one element is found</dd>
<dd><code>compareBiPredicate</code> - check for element naming</dd>
<dt>Returns:</dt>
<dd>all elements with a given qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelative(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class)">
<h3>findRelative</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findRelative</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; type)</span></div>
<div class="block">Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - scope Element</dd>
<dd><code>qualifiedName</code> - qualified name of element</dd>
<dd><code>type</code> - strict class type of element. Nulls means any element</dd>
<dt>Returns:</dt>
<dd>Element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelative(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class[])">
<h3>findRelative</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findRelative</span><wbr/><span class="parameters">(<a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] type)</span></div>
<div class="block">Search is done in a given scope (root Element) by searching for an element with a given partial qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - scope Element</dd>
<dd><code>qualifiedName</code> - qualified name of element</dd>
<dd><code>type</code> - strict class type of element. Nulls means any element</dd>
<dt>Returns:</dt>
<dd>Element or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMatchingElement(java.util.function.BiPredicate,java.util.Collection,java.util.Collection,int,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isMatchingElement</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">boolean</span> <span class="element-name">isMatchingElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html" title="class or interface in java.util.function">BiPredicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; compareBiPredicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; pathElements,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt;&gt; typeSet,
 int i,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> el)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">will be removed</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isFinalPartOfQualifiedName(java.util.Collection,int)">
<h3>isFinalPartOfQualifiedName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFinalPartOfQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; pathElements,
 int i)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">will be removed</div>
</div>
</section>
</li>
<li>
<section class="detail" id="splitQualifiedName(java.lang.String)">
<h3>splitQualifiedName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">splitQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">will be removed</div>
</div>
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
