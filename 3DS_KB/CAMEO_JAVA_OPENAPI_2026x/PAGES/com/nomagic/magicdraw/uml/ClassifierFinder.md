# JAVA OPENAPI: ClassifierFinder (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/ClassifierFinder.html
- source_path: `com/nomagic/magicdraw/uml/ClassifierFinder.html`
- source_sha256: `a475c994f2ab8b00c7edf5e9914fad6c7ec102c2a927211b6b33a7e0e7fc819b`
- captured_utc: `2026-07-14T16:58:27.050167+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class ClassifierFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.ClassifierFinder

@OpenApiAllpublic classClassifierFinder
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class for finding and creating classifiers by simple or qualified name.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html)`
A resolver of simple classifier name.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ClassifierFinder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[createClassifier](#createClassifier(java.lang.String,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> type,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)`
Creates a classifier and packages for classifier according qualified classifier name.
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[createClassifier](#createClassifier(java.lang.String,java.lang.Class,java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> type,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) suggestedByDSL,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)`

`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findClassifier](#findClassifier(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Class%5B%5D,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] types,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)`
Looks for a classifier by a given name (simple or qualified).
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findClassifier](#findClassifier(java.lang.String,java.lang.Class%5B%5D,java.util.Collection,java.util.Collection))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>[] types,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)> root)`
Looks for a classifier of type by a given name (simple or qualified)
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findClassifierOrDataType](#findClassifierOrDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Class%5B%5D,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>[] types,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)`
Looks for a classifier of type or standard data type by a given name (simple or qualified).
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findClassifierOrDataType](#findClassifierOrDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)`
Looks for a classifier or standard data type by the given name (simple or qualified).
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findOrCreateClassifier](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver))([Project](../core/Project.html) project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver)`
Searches for a classifier or standard data type with a given name (qualified or simple).
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findOrCreateClassifier](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean))([Project](../core/Project.html) project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver,
 boolean createIfNotFound)`
Searches for a classifier or standard data type with a given name (qualified or simple).
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findOrCreateClassifier](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class))([Project](../core/Project.html) project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType)`
Searches for a classifier or standard data type with a given name (qualified or simple).
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findOrCreateClassifier](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver))([Project](../core/Project.html) project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>> searchType,
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver)`
Searches for a classifier or standard data type with a given name (qualified or simple)
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findOrCreateClassifier](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean))([Project](../core/Project.html) project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>> searchType,
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver,
 boolean createIfNotFound)`
Searches for a classifier or standard data type with a given name (qualified or simple)
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findOrCreateClassifier](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Project](../core/Project.html) project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>> searchType,
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver,
 boolean createIfNotFound,
 [PresentationElement](symbols/PresentationElement.html) contextView)`
Searches for a classifier with given name (simple or qualified).
`static [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)`
`[findOrCreateNamespaceForElement](#findOrCreateNamespaceForElement(java.lang.String,java.lang.Class,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedElementName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)> searchType,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)> createType,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)`
Returns namespace according given qualified element name.
`static [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)`
`[findOrCreatePackageForElement](#findOrCreatePackageForElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedElementName,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)`
Creates or finds packages using a qualified name of element in the given root.
`static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)`
`[findStandardDataType](#findStandardDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted)`
Searches for a standard DataType from UMLStandardProfile or MagicDrawProfile modules.
`static boolean`
`[isQualifiedName](#isQualifiedName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementName)`
Check if given element name is a qualified name
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ClassifierFinder
public ClassifierFinder()
 ============ METHOD DETAIL ========== 
Method Details
findClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findClassifier([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] types,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 @CheckForNull
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)
Looks for a classifier by a given name (simple or qualified).
Parameters:
`project` - project
`name` - classifier name (simple or qualified)
`types` - classifier types
`restricted` - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)
`root` - root element. Null means whole project
Returns:
found classifier
findClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findClassifier([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>[] types,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)> root)
Looks for a classifier of type by a given name (simple or qualified)
Parameters:
`name` - classifier name (simple or qualified)
`types` - classifier types
`restricted` - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)
`root` - root elements. Empty means whole project
Returns:
found classifier
findStandardDataType
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findStandardDataType([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted)
Searches for a standard DataType from UMLStandardProfile or MagicDrawProfile modules.
Parameters:
`project` - project
`name` - data type name
`restricted` - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)
Returns:
found data type or null
findClassifierOrDataType
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findClassifierOrDataType([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 @CheckForNull
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)
Looks for a classifier or standard data type by the given name (simple or qualified).
Parameters:
`project` - project
`name` - classifier name simple or qualified)
`restricted` - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)
`root` - root element. Null means whole project
Returns:
found classifier
See Also:
[`UML2DataTypes.CORE_CLASSIFIERS`](../uml2/datatypes/UML2DataTypes.html#CORE_CLASSIFIERS)
findClassifierOrDataType
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findClassifierOrDataType([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>[] types,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) restricted,
 @CheckForNull
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)
Looks for a classifier of type or standard data type by a given name (simple or qualified).
Parameters:
`project` - project
`name` - classifier name
`types` - classifier types
`restricted` - Allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)
`root` - root element. Null means whole project
Returns:
found classifier
See Also:
[`UML2DataTypes.CORE_CLASSIFIERS`](../uml2/datatypes/UML2DataTypes.html#CORE_CLASSIFIERS)
findOrCreateClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findOrCreateClassifier([Project](../core/Project.html) project,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver)
Searches for a classifier or standard data type with a given name (qualified or simple). Creates UML Class if not found.
See Also:
[`findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)`](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean))
findOrCreateClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findOrCreateClassifier([Project](../core/Project.html) project,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver,
 boolean createIfNotFound)
Searches for a classifier or standard data type with a given name (qualified or simple). Creates UML Class if not found.
See Also:
[`findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)`](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean))
findOrCreateClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findOrCreateClassifier([Project](../core/Project.html) project,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType)
Searches for a classifier or standard data type with a given name (qualified or simple). Creates classifier of given type.
See Also:
[`findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)`](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean))
findOrCreateClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findOrCreateClassifier([Project](../core/Project.html) project,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>> searchType,
 @CheckForNull
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver)
Searches for a classifier or standard data type with a given name (qualified or simple)
See Also:
[`findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)`](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean))
findOrCreateClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findOrCreateClassifier(@CheckForNull
 [Project](../core/Project.html) project,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>> searchType,
 @CheckForNull
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver,
 boolean createIfNotFound)
Searches for a classifier or standard data type with a given name (qualified or simple)
See Also:
[`findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, java.lang.String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean, com.nomagic.magicdraw.uml.symbols.PresentationElement)`](#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean,com.nomagic.magicdraw.uml.symbols.PresentationElement))
findOrCreateClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) findOrCreateClassifier(@CheckForNull
 [Project](../core/Project.html) project,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> createType,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>> searchType,
 @CheckForNull
 [ClassifierFinder.SimpleNameResolver](ClassifierFinder.SimpleNameResolver.html) simpleNameResolver,
 boolean createIfNotFound,
 @CheckForNull
 [PresentationElement](symbols/PresentationElement.html) contextView)
Searches for a classifier with given name (simple or qualified).
 If such does not exist, creates a classifier with given name.
 Priorities:
 1. if qualified name is specified, searching by qualified name
 2. if context is not null, using context to find nearest Package and searching in it
 3. Searching in all packages
 4. Searching for standard data type
 Usage:
 getClassifierFor(root, "java::lang::String", Class.class)
 getClassifierFor(javaLangPackage, "String", Class.class)
 getClassifierFor(ioPackage, "Serializable", Interface.class)
Parameters:
`context` - element used to find nearest Package and use it as root
`name` - name of classifier. If classifier contains "::" then assuming that name is qualified
`createType` - a classifier type to create if not found (for example Class.class or Interface.class)
`searchType` - a collection of classifier types to search for (for example Class.class or Interface.class)
`simpleNameResolver` - simple name resolver
`createIfNotFound` - should new classifier be created if existing is not found
`contextView` - context view
createClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) createClassifier([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> type,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) suggestedByDSL,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)
createClassifier
@CheckForNullpublic static [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) createClassifier([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> type,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)
Creates a classifier and packages for classifier according qualified classifier name.
Parameters:
`qualifiedName` - qualifiedName
`type` - classifier type
`root` - root namespace
Returns:
create classifier ir null
findOrCreatePackageForElement
@CheckForNullpublic static [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) findOrCreatePackageForElement([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedElementName,
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)
Creates or finds packages using a qualified name of element in the given root.
Parameters:
`qualifiedElementName` - qualified name of element (not the package!) from a given root element
`root` - parent package where packages will be created
Returns:
leaf package
findOrCreateNamespaceForElement
@CheckForNullpublic static [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) findOrCreateNamespaceForElement([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedElementName,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)> searchType,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html)> createType,
 @Nonnull
 [Namespace](../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) root)
Returns namespace according given qualified element name.
Parameters:
`qualifiedElementName` - qualified name of element inside a namespace (not namespace itself!!!)
`searchType` - class type of namespace to find
`createType` - class type of namespace to create. Null if do not want to create a namespace
`root` - root
Returns:
found or created namespace element
isQualifiedName
public static boolean isQualifiedName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementName)
Check if given element name is a qualified name
Parameters:
`elementName` - name
Returns:
true if name is a qualified

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class ClassifierFinder">Class ClassifierFinder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.ClassifierFinder</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ClassifierFinder</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for finding and creating classifiers by simple or qualified name.</div>
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
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a></code></div>
<div class="col-last even-row-color">
<div class="block">A resolver of simple classifier name.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ClassifierFinder</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassifier(java.lang.String,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">createClassifier</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; type,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a classifier and packages for classifier according qualified classifier name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassifier(java.lang.String,java.lang.Class,java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">createClassifier</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> suggestedByDSL,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findClassifier(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Class%5B%5D,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">findClassifier</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a classifier by a given name (simple or qualified).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findClassifier(java.lang.String,java.lang.Class%5B%5D,java.util.Collection,java.util.Collection)">findClassifier</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;[] types,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt; root)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a classifier of type by a given name (simple or qualified)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findClassifierOrDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Class%5B%5D,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">findClassifierOrDataType</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;[] types,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a classifier of type or standard data type by a given name (simple or qualified).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findClassifierOrDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">findClassifierOrDataType</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for a classifier or standard data type by the given name (simple or qualified).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver)">findOrCreateClassifier</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)">findOrCreateClassifier</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver,
 boolean createIfNotFound)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class)">findOrCreateClassifier</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver)">findOrCreateClassifier</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;&gt; searchType,
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)">findOrCreateClassifier</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;&gt; searchType,
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver,
 boolean createIfNotFound)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean,com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOrCreateClassifier</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;&gt; searchType,
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver,
 boolean createIfNotFound,
 <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> contextView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a classifier with given name (simple or qualified).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreateNamespaceForElement(java.lang.String,java.lang.Class,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">findOrCreateNamespaceForElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedElementName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt; searchType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt; createType,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns namespace according given qualified element name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrCreatePackageForElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">findOrCreatePackageForElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedElementName,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates or finds packages using a qualified name of element in the given root.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findStandardDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection)">findStandardDataType</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Searches for a standard DataType from UMLStandardProfile or MagicDrawProfile modules.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isQualifiedName(java.lang.String)">isQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element name is a qualified name</div>
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
<h3>ClassifierFinder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassifierFinder</span>()</div>
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
<section class="detail" id="findClassifier(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Class[],java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>findClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findClassifier</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</span></div>
<div class="block">Looks for a classifier by a given name (simple or qualified).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>name</code> - classifier name (simple or qualified)</dd>
<dd><code>types</code> - classifier types</dd>
<dd><code>restricted</code> - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)</dd>
<dd><code>root</code> - root element. Null means whole project</dd>
<dt>Returns:</dt>
<dd>found classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findClassifier(java.lang.String,java.lang.Class[],java.util.Collection,java.util.Collection)">
<h3>findClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findClassifier</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;[] types,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt; root)</span></div>
<div class="block">Looks for a classifier of type by a given name (simple or qualified)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - classifier name (simple or qualified)</dd>
<dd><code>types</code> - classifier types</dd>
<dd><code>restricted</code> - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)</dd>
<dd><code>root</code> - root elements. Empty means whole project</dd>
<dt>Returns:</dt>
<dd>found classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findStandardDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection)">
<h3>findStandardDataType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findStandardDataType</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted)</span></div>
<div class="block">Searches for a standard DataType from UMLStandardProfile or MagicDrawProfile modules.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>name</code> - data type name</dd>
<dd><code>restricted</code> - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)</dd>
<dt>Returns:</dt>
<dd>found data type or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findClassifierOrDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>findClassifierOrDataType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findClassifierOrDataType</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</span></div>
<div class="block">Looks for a classifier or standard data type by the given name (simple or qualified).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>name</code> - classifier name simple or qualified)</dd>
<dd><code>restricted</code> - allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)</dd>
<dd><code>root</code> - root element. Null means whole project</dd>
<dt>Returns:</dt>
<dd>found classifier</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../uml2/datatypes/UML2DataTypes.html#CORE_CLASSIFIERS"><code>UML2DataTypes.CORE_CLASSIFIERS</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findClassifierOrDataType(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Class[],java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>findClassifierOrDataType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findClassifierOrDataType</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;[] types,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> restricted,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</span></div>
<div class="block">Looks for a classifier of type or standard data type by a given name (simple or qualified).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>name</code> - classifier name</dd>
<dd><code>types</code> - classifier types</dd>
<dd><code>restricted</code> - Allowed DSL elements. Collection should contain stereotypes and/or metaclass classes (java.lang.Class)</dd>
<dd><code>root</code> - root element. Null means whole project</dd>
<dt>Returns:</dt>
<dd>found classifier</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../uml2/datatypes/UML2DataTypes.html#CORE_CLASSIFIERS"><code>UML2DataTypes.CORE_CLASSIFIERS</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver)">
<h3>findOrCreateClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findOrCreateClassifier</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver)</span></div>
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple). Creates UML Class if not found.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)"><code>findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)">
<h3>findOrCreateClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findOrCreateClassifier</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver,
 boolean createIfNotFound)</span></div>
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple). Creates UML Class if not found.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)"><code>findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class)">
<h3>findOrCreateClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findOrCreateClassifier</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType)</span></div>
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple). Creates classifier of given type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)"><code>findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver)">
<h3>findOrCreateClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findOrCreateClassifier</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;&gt; searchType,
 @CheckForNull
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver)</span></div>
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)"><code>findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean)">
<h3>findOrCreateClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findOrCreateClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;&gt; searchType,
 @CheckForNull
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver,
 boolean createIfNotFound)</span></div>
<div class="block">Searches for a classifier or standard data type with a given name (qualified or simple)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean,com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>findOrCreateClassifier(com.nomagic.magicdraw.core.Project, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, java.lang.String, java.lang.Class, java.util.Collection, com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver, boolean, com.nomagic.magicdraw.uml.symbols.PresentationElement)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreateClassifier(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Class,java.util.Collection,com.nomagic.magicdraw.uml.ClassifierFinder.SimpleNameResolver,boolean,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>findOrCreateClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">findOrCreateClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; createType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;&gt; searchType,
 @CheckForNull
 <a href="ClassifierFinder.SimpleNameResolver.html" title="class in com.nomagic.magicdraw.uml">ClassifierFinder.SimpleNameResolver</a> simpleNameResolver,
 boolean createIfNotFound,
 @CheckForNull
 <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> contextView)</span></div>
<div class="block">Searches for a classifier with given name (simple or qualified).
 If such does not exist, creates a classifier with given name.
 Priorities:
 <ul>
<li>1. if qualified name is specified, searching by qualified name
 <li>2. if context is not null, using context to find nearest Package and searching in it
 <li>3. Searching in all packages
 <li>4. Searching for standard data type
 </li></li></li></li></ul>
 Usage:
 <ul>
<li> getClassifierFor(root, "java::lang::String", Class.class)
 <li> getClassifierFor(javaLangPackage, "String", Class.class)
 <li> getClassifierFor(ioPackage, "Serializable", Interface.class)
 </li></li></li></ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - element used to find nearest Package and use it as root</dd>
<dd><code>name</code> - name of classifier. If classifier contains "::" then assuming that name is qualified</dd>
<dd><code>createType</code> - a classifier type to create if not found (for example Class.class or Interface.class)</dd>
<dd><code>searchType</code> - a collection of classifier types to search for (for example Class.class or Interface.class)</dd>
<dd><code>simpleNameResolver</code> - simple name resolver</dd>
<dd><code>createIfNotFound</code> - should new classifier be created if existing is not found</dd>
<dd><code>contextView</code> - context view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassifier(java.lang.String,java.lang.Class,java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>createClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">createClassifier</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; type,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> suggestedByDSL,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</span></div>
</section>
</li>
<li>
<section class="detail" id="createClassifier(java.lang.String,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>createClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">createClassifier</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; type,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</span></div>
<div class="block">Creates a classifier and packages for classifier according qualified classifier name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedName</code> - qualifiedName</dd>
<dd><code>type</code> - classifier type</dd>
<dd><code>root</code> - root namespace</dd>
<dt>Returns:</dt>
<dd>create classifier ir null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreatePackageForElement(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>findOrCreatePackageForElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></span> <span class="element-name">findOrCreatePackageForElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedElementName,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</span></div>
<div class="block">Creates or finds packages using a qualified name of element in the given root.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedElementName</code> - qualified name of element (not the package!) from a given root element</dd>
<dd><code>root</code> - parent package where packages will be created</dd>
<dt>Returns:</dt>
<dd>leaf package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrCreateNamespaceForElement(java.lang.String,java.lang.Class,java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>findOrCreateNamespaceForElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></span> <span class="element-name">findOrCreateNamespaceForElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedElementName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt; searchType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>&gt; createType,
 @Nonnull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> root)</span></div>
<div class="block">Returns namespace according given qualified element name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedElementName</code> - qualified name of element inside a namespace (not namespace itself!!!)</dd>
<dd><code>searchType</code> - class type of namespace to find</dd>
<dd><code>createType</code> - class type of namespace to create. Null if do not want to create a namespace</dd>
<dd><code>root</code> - root</dd>
<dt>Returns:</dt>
<dd>found or created namespace element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isQualifiedName(java.lang.String)">
<h3>isQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</span></div>
<div class="block">Check if given element name is a qualified name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementName</code> - name</dd>
<dt>Returns:</dt>
<dd>true if name is a qualified</dd>
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
