# JAVA OPENAPI: ResourceManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/resources/ResourceManager.html
- source_path: `com/nomagic/magicdraw/resources/ResourceManager.html`
- source_sha256: `b3c1dc2609b6d9352046377ee3c089d91f3f7be5ec2203e8dd04059a14c1bc2d`
- captured_utc: `2026-07-14T16:51:28.639303+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.resources](package-summary.html)

## Class ResourceManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.resources.ResourceManager

@OpenApiAllpublic classResourceManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This class is used to retrieve the resources from
 the resource bundle files

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEFAULT](#DEFAULT)`
Deprecated.
replaced with [`SYSTEM`](#SYSTEM)
`static final int`
`[DIALOG_RESOURCE](#DIALOG_RESOURCE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIALOG_RESOURCE_BUNDLE](#DIALOG_RESOURCE_BUNDLE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ENGLISH](#ENGLISH)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXTENSION](#EXTENSION)`

`static final int`
`[METAMODEL_RESOURCE](#METAMODEL_RESOURCE)`

`static final int`
`[PROPERTY_RESOURCE](#PROPERTY_RESOURCE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[RESOURCES_CLASS_NAMES](#RESOURCES_CLASS_NAMES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SYSTEM](#SYSTEM)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ResourceManager](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[createAvailableLanguages](#createAvailableLanguages())()`
Creates Available language.
`static void`
`[fillAvailableLanguagesFromBundleInJar](#fillAvailableLanguagesFromBundleInJar(java.util.Collection,java.net.URL))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> languages,
 [URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) location)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[formatMessage](#formatMessage(java.lang.Object%5B%5D,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] messageArguments,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[formatMessage](#formatMessage(java.lang.String,java.lang.String...))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)... arguments)`

`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAvailableLanguages](#getAvailableLanguages())()`

`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[JarEntry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html)>`
`[getEntriesUnderPath](#getEntriesUnderPath(java.util.jar.JarFile,java.util.function.Predicate))([JarFile](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarFile.html) jar,
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[JarEntry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html)> pred)`

`static [Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html)`
`[getLocale](#getLocale())()`
Gets set locale.
`static [LocaleInfo](LocaleInfo.html)`
`[getLocaleInfo](#getLocaleInfo())()`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getMetaModelResource](#getMetaModelResource(com.nomagic.magicdraw.uml.MDElement))([MDElement](../uml/MDElement.html) presentationElement)`
Returns meta model resource.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getMetaModelResource](#getMetaModelResource(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)`
Returns meta model resource.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getMetaModelResource](#getMetaModelResource(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject element)`
Returns meta model resource.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringFor](#getStringFor(java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 int bundle)`
Get string according to key and bundle id.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringFor](#getStringFor(java.lang.String,int,java.lang.Object%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 int bundle,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] messageArguments)`
Get string according to key and bundle id.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringFor](#getStringFor(java.lang.String,int,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 int bundle,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) messageArguments)`
Get string according to key and bundle id.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringFor](#getStringFor(java.lang.String,java.lang.String,java.lang.ClassLoader))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bundleName,
 [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) loader)`
Get string according to key and bundle id.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringOrElse](#getStringOrElse(java.lang.String,java.lang.String,java.lang.ClassLoader,java.util.function.Supplier))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bundleName,
 [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) loader,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> alternative)`
Get string according to key and bundle id.
`static void`
`[setLocale](#setLocale(com.nomagic.magicdraw.resources.LocaleInfo))([LocaleInfo](LocaleInfo.html) localeInfo)`
Sets locale.
`static void`
`[setLocale](#setLocale(java.util.Locale))([Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html) locale)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
DIALOG_RESOURCE
public static final int DIALOG_RESOURCE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.DIALOG_RESOURCE)
PROPERTY_RESOURCE
public static final int PROPERTY_RESOURCE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.PROPERTY_RESOURCE)
METAMODEL_RESOURCE
public static final int METAMODEL_RESOURCE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.METAMODEL_RESOURCE)
EXTENSION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXTENSION
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.EXTENSION)
DEFAULT
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEFAULT
Deprecated.
replaced with [`SYSTEM`](#SYSTEM)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.DEFAULT)
SYSTEM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SYSTEM
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.SYSTEM)
ENGLISH
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ENGLISH
RESOURCES_CLASS_NAMES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] RESOURCES_CLASS_NAMES
DIALOG_RESOURCE_BUNDLE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIALOG_RESOURCE_BUNDLE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.DIALOG_RESOURCE_BUNDLE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ResourceManager
public ResourceManager()
 ============ METHOD DETAIL ========== 
Method Details
getMetaModelResource
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getMetaModelResource([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)
Returns meta model resource.
getMetaModelResource
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getMetaModelResource([MDElement](../uml/MDElement.html) presentationElement)
Returns meta model resource.
getMetaModelResource
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getMetaModelResource(javax.jmi.reflect.RefObject element)
Returns meta model resource.
getStringFor
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 int bundle)
Get string according to key and bundle id. If there are no such - returns key.
Parameters:
`key` - Key to fetch string
`bundle` - Bundle ID
Returns:
String for key from given bundle.
getStringFor
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bundleName,
 @CheckForNull
 [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) loader)
Get string according to key and bundle id. If there are no such - returns key.
Parameters:
`key` - Key to fetch string
`bundleName` - Bundle name
`loader` - loader to load resources
Returns:
String for key from given bundle.
getStringOrElse
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringOrElse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bundleName,
 @CheckForNull
 [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) loader,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> alternative)
Get string according to key and bundle id. If there is no such - returns alternative from the passed in supplier.
Parameters:
`key` - Key to fetch string
`bundleName` - Bundle name
`loader` - loader to load resources
`alternative` - result to be returned in case key or bundle is not found
Returns:
String for key from given bundle, or alternative if the key or bundle is not found
getStringFor
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 int bundle,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) messageArguments)
Get string according to key and bundle id. If there are no such - returns key. Can retrieve customizable message bundles.
Parameters:
`key` - Key to fetch string
`bundle` - Bundle ID
`messageArguments` - Set of the message bundle arguments.
Returns:
String for key from given bundle.
getStringFor
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringFor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 int bundle,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] messageArguments)
Get string according to key and bundle id. If there are no such - returns key. Can retrieve customizable message bundles.
Parameters:
`key` - Key to fetch string
`bundle` - Bundle id
`messageArguments` - Set of the message bundle arguments.
Returns:
String for key from given bundle.
formatMessage
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) formatMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)... arguments)
formatMessage
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) formatMessage([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] messageArguments,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
getLocale
public static [Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html) getLocale()
Gets set locale. If there are no such - creates default.
Returns:
locale, which is used for bundles
getLocaleInfo
public static [LocaleInfo](LocaleInfo.html) getLocaleInfo()
setLocale
public static void setLocale([Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html) locale)
setLocale
public static void setLocale([LocaleInfo](LocaleInfo.html) localeInfo)
Sets locale. This operation is called only when is read environment options
Parameters:
`localeInfo` - Bundles will be chosen according this locale
getAvailableLanguages
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAvailableLanguages()
createAvailableLanguages
public static void createAvailableLanguages()
Creates Available language.
fillAvailableLanguagesFromBundleInJar
public static void fillAvailableLanguagesFromBundleInJar([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> languages,
 [URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) location)
getEntriesUnderPath
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[JarEntry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html)> getEntriesUnderPath([JarFile](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarFile.html) jar,
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[JarEntry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html)> pred)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.resources</a></div>
<h1 class="title" title="Class ResourceManager">Class ResourceManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.resources.ResourceManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ResourceManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">This class is used to retrieve the resources from
 the resource bundle files</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT">DEFAULT</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">replaced with <a href="#SYSTEM"><code>SYSTEM</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIALOG_RESOURCE">DIALOG_RESOURCE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIALOG_RESOURCE_BUNDLE">DIALOG_RESOURCE_BUNDLE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENGLISH">ENGLISH</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXTENSION">EXTENSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METAMODEL_RESOURCE">METAMODEL_RESOURCE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROPERTY_RESOURCE">PROPERTY_RESOURCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RESOURCES_CLASS_NAMES">RESOURCES_CLASS_NAMES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SYSTEM">SYSTEM</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ResourceManager</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createAvailableLanguages()">createAvailableLanguages</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates Available language.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fillAvailableLanguagesFromBundleInJar(java.util.Collection,java.net.URL)">fillAvailableLanguagesFromBundleInJar</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; languages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#formatMessage(java.lang.Object%5B%5D,java.lang.String)">formatMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] messageArguments,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#formatMessage(java.lang.String,java.lang.String...)">formatMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... arguments)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAvailableLanguages()">getAvailableLanguages</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html" title="class or interface in java.util.jar">JarEntry</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEntriesUnderPath(java.util.jar.JarFile,java.util.function.Predicate)">getEntriesUnderPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarFile.html" title="class or interface in java.util.jar">JarFile</a> jar,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html" title="class or interface in java.util.jar">JarEntry</a>&gt; pred)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html" title="class or interface in java.util">Locale</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocale()">getLocale</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets set locale.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="LocaleInfo.html" title="class in com.nomagic.magicdraw.resources">LocaleInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocaleInfo()">getLocaleInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaModelResource(com.nomagic.magicdraw.uml.MDElement)">getMetaModelResource</a><wbr/>(<a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns meta model resource.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaModelResource(java.lang.Class)">getMetaModelResource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns meta model resource.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetaModelResource(javax.jmi.reflect.RefObject)">getMetaModelResource</a><wbr/>(javax.jmi.reflect.RefObject element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns meta model resource.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringFor(java.lang.String,int)">getStringFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 int bundle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get string according to key and bundle id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringFor(java.lang.String,int,java.lang.Object%5B%5D)">getStringFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 int bundle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] messageArguments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get string according to key and bundle id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringFor(java.lang.String,int,java.lang.String)">getStringFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 int bundle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> messageArguments)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get string according to key and bundle id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringFor(java.lang.String,java.lang.String,java.lang.ClassLoader)">getStringFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bundleName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get string according to key and bundle id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringOrElse(java.lang.String,java.lang.String,java.lang.ClassLoader,java.util.function.Supplier)">getStringOrElse</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bundleName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; alternative)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get string according to key and bundle id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocale(com.nomagic.magicdraw.resources.LocaleInfo)">setLocale</a><wbr/>(<a href="LocaleInfo.html" title="class in com.nomagic.magicdraw.resources">LocaleInfo</a> localeInfo)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets locale.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocale(java.util.Locale)">setLocale</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html" title="class or interface in java.util">Locale</a> locale)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="DIALOG_RESOURCE">
<h3>DIALOG_RESOURCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DIALOG_RESOURCE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.DIALOG_RESOURCE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROPERTY_RESOURCE">
<h3>PROPERTY_RESOURCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PROPERTY_RESOURCE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.PROPERTY_RESOURCE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METAMODEL_RESOURCE">
<h3>METAMODEL_RESOURCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">METAMODEL_RESOURCE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.METAMODEL_RESOURCE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTENSION">
<h3>EXTENSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTENSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.EXTENSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT">
<h3>DEFAULT</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">replaced with <a href="#SYSTEM"><code>SYSTEM</code></a></div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.DEFAULT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SYSTEM">
<h3>SYSTEM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SYSTEM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.SYSTEM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENGLISH">
<h3>ENGLISH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENGLISH</span></div>
</section>
</li>
<li>
<section class="detail" id="RESOURCES_CLASS_NAMES">
<h3>RESOURCES_CLASS_NAMES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">RESOURCES_CLASS_NAMES</span></div>
</section>
</li>
<li>
<section class="detail" id="DIALOG_RESOURCE_BUNDLE">
<h3>DIALOG_RESOURCE_BUNDLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIALOG_RESOURCE_BUNDLE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.resources.ResourceManager.DIALOG_RESOURCE_BUNDLE">Constant Field Values</a></li>
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
<h3>ResourceManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ResourceManager</span>()</div>
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
<section class="detail" id="getMetaModelResource(java.lang.Class)">
<h3>getMetaModelResource</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMetaModelResource</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</span></div>
<div class="block">Returns meta model resource.</div>
</section>
</li>
<li>
<section class="detail" id="getMetaModelResource(com.nomagic.magicdraw.uml.MDElement)">
<h3>getMetaModelResource</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMetaModelResource</span><wbr/><span class="parameters">(<a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a> presentationElement)</span></div>
<div class="block">Returns meta model resource.</div>
</section>
</li>
<li>
<section class="detail" id="getMetaModelResource(javax.jmi.reflect.RefObject)">
<h3>getMetaModelResource</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMetaModelResource</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject element)</span></div>
<div class="block">Returns meta model resource.</div>
</section>
</li>
<li>
<section class="detail" id="getStringFor(java.lang.String,int)">
<h3>getStringFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 int bundle)</span></div>
<div class="block">Get string according to key and bundle id. If there are no such - returns key.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - Key to fetch string</dd>
<dd><code>bundle</code> - Bundle ID</dd>
<dt>Returns:</dt>
<dd>String for key from given bundle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringFor(java.lang.String,java.lang.String,java.lang.ClassLoader)">
<h3>getStringFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bundleName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader)</span></div>
<div class="block">Get string according to key and bundle id. If there are no such - returns key.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - Key to fetch string</dd>
<dd><code>bundleName</code> - Bundle name</dd>
<dd><code>loader</code> - loader to load resources</dd>
<dt>Returns:</dt>
<dd>String for key from given bundle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringOrElse(java.lang.String,java.lang.String,java.lang.ClassLoader,java.util.function.Supplier)">
<h3>getStringOrElse</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringOrElse</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bundleName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; alternative)</span></div>
<div class="block">Get string according to key and bundle id. If there is no such - returns alternative from the passed in supplier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - Key to fetch string</dd>
<dd><code>bundleName</code> - Bundle name</dd>
<dd><code>loader</code> - loader to load resources</dd>
<dd><code>alternative</code> - result to be returned in case key or bundle is not found</dd>
<dt>Returns:</dt>
<dd>String for key from given bundle, or alternative if the key or bundle is not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringFor(java.lang.String,int,java.lang.String)">
<h3>getStringFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 int bundle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> messageArguments)</span></div>
<div class="block">Get string according to key and bundle id. If there are no such - returns key. Can retrieve customizable message bundles.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - Key to fetch string</dd>
<dd><code>bundle</code> - Bundle ID</dd>
<dd><code>messageArguments</code> - Set of the message bundle arguments.</dd>
<dt>Returns:</dt>
<dd>String for key from given bundle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringFor(java.lang.String,int,java.lang.Object[])">
<h3>getStringFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 int bundle,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] messageArguments)</span></div>
<div class="block">Get string according to key and bundle id. If there are no such - returns key. Can retrieve customizable message bundles.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - Key to fetch string</dd>
<dd><code>bundle</code> - Bundle id</dd>
<dd><code>messageArguments</code> - Set of the message bundle arguments.</dd>
<dt>Returns:</dt>
<dd>String for key from given bundle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="formatMessage(java.lang.String,java.lang.String...)">
<h3>formatMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">formatMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... arguments)</span></div>
</section>
</li>
<li>
<section class="detail" id="formatMessage(java.lang.Object[],java.lang.String)">
<h3>formatMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">formatMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] messageArguments,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLocale()">
<h3>getLocale</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html" title="class or interface in java.util">Locale</a></span> <span class="element-name">getLocale</span>()</div>
<div class="block">Gets set locale. If there are no such - creates default.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>locale, which is used for bundles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocaleInfo()">
<h3>getLocaleInfo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="LocaleInfo.html" title="class in com.nomagic.magicdraw.resources">LocaleInfo</a></span> <span class="element-name">getLocaleInfo</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLocale(java.util.Locale)">
<h3>setLocale</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLocale</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html" title="class or interface in java.util">Locale</a> locale)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLocale(com.nomagic.magicdraw.resources.LocaleInfo)">
<h3>setLocale</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLocale</span><wbr/><span class="parameters">(<a href="LocaleInfo.html" title="class in com.nomagic.magicdraw.resources">LocaleInfo</a> localeInfo)</span></div>
<div class="block">Sets locale. This operation is called only when is read environment options</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>localeInfo</code> - Bundles will be chosen according this locale</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAvailableLanguages()">
<h3>getAvailableLanguages</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAvailableLanguages</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createAvailableLanguages()">
<h3>createAvailableLanguages</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createAvailableLanguages</span>()</div>
<div class="block">Creates Available language.</div>
</section>
</li>
<li>
<section class="detail" id="fillAvailableLanguagesFromBundleInJar(java.util.Collection,java.net.URL)">
<h3>fillAvailableLanguagesFromBundleInJar</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">fillAvailableLanguagesFromBundleInJar</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; languages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> location)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEntriesUnderPath(java.util.jar.JarFile,java.util.function.Predicate)">
<h3>getEntriesUnderPath</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html" title="class or interface in java.util.jar">JarEntry</a>&gt;</span> <span class="element-name">getEntriesUnderPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarFile.html" title="class or interface in java.util.jar">JarFile</a> jar,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/jar/JarEntry.html" title="class or interface in java.util.jar">JarEntry</a>&gt; pred)</span></div>
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
