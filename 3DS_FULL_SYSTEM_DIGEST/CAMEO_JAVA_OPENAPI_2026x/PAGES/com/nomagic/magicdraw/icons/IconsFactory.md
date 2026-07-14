# JAVA OPENAPI: IconsFactory (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/icons/IconsFactory.html
- source_path: `com/nomagic/magicdraw/icons/IconsFactory.html`
- source_sha256: `de33ebff780e50c4d2a3dcc21f4af2a39361d357e36c3d37aab90d74a516dc06`
- captured_utc: `2026-07-14T16:57:58.575541+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.icons](package-summary.html)

## Class IconsFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.icons.IconsFactory

@OpenApiAllpublic classIconsFactory
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to load icons from MagicDraw icons package or other locations.
 
 All loaded icons are cached, so second attempt to load same icon will take it from a cache.
 
 Icons are loader using [`Class.getResource(String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)), so icon name should follow that notation.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[IconsFactory](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Load icon from a given resource
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.lang.Class,java.lang.String,boolean))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean silent)`
Load icon from a given resource.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Load icon from a given resource
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean silent)`
Load icon from a given resource.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.net.URI,byte%5B%5D))([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data)`
Load icon from given bytes.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.net.URI,byte%5B%5D,int))([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data,
 int size)`
Load icon from given bytes.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)`
Load icon from a given url.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.net.URL,int))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url,
 int size)`
Load icon from a given url.
`static byte[]`
`[getIconData](#getIconData(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Reads icon data from a given file.
`static byte[]`
`[getIconData](#getIconData(java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) input)`
Reads icon data from a given stream.
`static byte[]`
`[getIconData](#getIconData(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)`
Reads icon data from a given url.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getNotScaledIcon](#getNotScaledIcon(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Load icon from a given resource.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getNotScaledIcon](#getNotScaledIcon(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Load icon from a given resource.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getNotScaledIcon](#getNotScaledIcon(java.net.URI,byte%5B%5D))([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data)`
Load icon from given bytes.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getNotScaledIcon](#getNotScaledIcon(java.net.URI,byte%5B%5D,int))([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data,
 int size)`
Load icon from given bytes.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getNotScaledIcon](#getNotScaledIcon(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)`
Load icon from a given url.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getNotScaledIcon](#getNotScaledIcon(java.net.URL,int))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url,
 int size)`
Load icon from a given url.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getQualifiedResourceName](#getQualifiedResourceName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resourceName)`
Resolves given resource name to a qualified name in this package.
`static [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)`
`[getResource](#getResource(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Provide URL to a resource in this package
`static [InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html)`
`[getResourceAsStream](#getResourceAsStream(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Provide stream to a resource in this package
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getSvgIcon](#getSvgIcon(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)`
Load SVG icon from a given url.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
IconsFactory
public IconsFactory()
 ============ METHOD DETAIL ========== 
Method Details
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Load icon from a given resource
Parameters:
`name` - icon name
Returns:
icon
See Also:
[`Class.getResource(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String))
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Load icon from a given resource
Parameters:
`clazz` - icon resource class
`name` - icon name
Returns:
icon
See Also:
[`Class.getResource(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String))
getNotScaledIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getNotScaledIcon([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Load icon from a given resource. Does not scale icon by screen dpi.
Parameters:
`name` - icon name
Returns:
icon
See Also:
[`Class.getResource(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String))
getNotScaledIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getNotScaledIcon([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Load icon from a given resource. Does not scale icon by screen dpi.
Parameters:
`clazz` - icon resource class
`name` - icon name
Returns:
icon
See Also:
[`Class.getResource(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String))
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean silent)
Load icon from a given resource.
Parameters:
`name` - icon name
`silent` - true if missing icon should not be reported to a log file
Returns:
icon
See Also:
[`Class.getResource(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String))
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean silent)
Load icon from a given resource.
Parameters:
`clazz` - icon resource class
`name` - icon name
`silent` - true if missing icon should not be reported to a log file
Returns:
icon
See Also:
[`Class.getResource(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String))
getResourceAsStream
public static [InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) getResourceAsStream([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Provide stream to a resource in this package
Parameters:
`name` - resource name
Returns:
icon
See Also:
[`Class.getResourceAsStream(String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResourceAsStream(java.lang.String))
getResource
public static [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) getResource([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Provide URL to a resource in this package
Parameters:
`name` - resource name
Returns:
icon
See Also:
[`Class.getResource(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String))
getQualifiedResourceName
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getQualifiedResourceName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resourceName)
Resolves given resource name to a qualified name in this package. If resource name is already qualified (starts with "/"), returns it.
Parameters:
`resourceName` - resource name
Returns:
qualified resource name in this package
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)
Load icon from a given url.
Parameters:
`url` - url
Returns:
icon
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url,
 int size)
Load icon from a given url. Scales icon to a box of given size.
Parameters:
`url` - url
`size` - icon box size. -1 if scaling is not needed
Returns:
icon
getNotScaledIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getNotScaledIcon([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)
Load icon from a given url. Does not scale icon by screen dpi.
Parameters:
`url` - url
Returns:
icon
getNotScaledIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getNotScaledIcon([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url,
 int size)
Load icon from a given url. Scales icon to a box of given size. Does not scale icon by screen dpi.
Parameters:
`url` - url
`size` - icon box size. -1 if scaling is not needed
Returns:
icon
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data)
Load icon from given bytes.
Parameters:
`uri` - uri describing the location (or format) of the icon
`data` - an array of icon data bytes
Returns:
icon
getIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data,
 int size)
Load icon from given bytes. Scales icon to a box of given size. Does not scale icon by screen dpi.
Parameters:
`uri` - uri
`data` - an array of icon data
`size` - icon box size. Icon will be scaled to this box. -1 if scaling is not needed
Returns:
icon
See Also:
[`HiDPIScaleUtilities.scaleIcon(int)`](../../ui/HiDPIScaleUtilities.html#scaleIcon(int))
getNotScaledIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getNotScaledIcon([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data)
Load icon from given bytes. Scales icon to a box of given size. Does not scale icon by screen dpi.
Parameters:
`uri` - icon uri
`data` - an array of icon data
Returns:
icon
getNotScaledIcon
public static [ResizableIcon](../../ui/ResizableIcon.html) getNotScaledIcon([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 byte[] data,
 int size)
Load icon from given bytes. Scales icon to a box of given size. Does not scale icon by screen dpi.
Parameters:
`uri` - icon uri
`data` - an array of icon data
`size` - icon box size. Icon will be scaled to this box. -1 if scaling is not needed
Returns:
icon
getIconData
@CheckForNullpublic static byte[] getIconData([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
Reads icon data from a given file.
Parameters:
`file` - an icon file
Returns:
icon data from given file
getIconData
@CheckForNullpublic static byte[] getIconData([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)
Reads icon data from a given url.
Parameters:
`url` - icon url
Returns:
icon data from given url
getIconData
@CheckForNullpublic static byte[] getIconData([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) input)
Reads icon data from a given stream.
Parameters:
`input` - input stream
Returns:
icon data
getSvgIcon
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getSvgIcon([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)
Load SVG icon from a given url.
 Other getIcon(...) methods in this class also can read SVG icons, but this one does not return icon compatible with [`ImageIcon`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html).
Parameters:
`url` - icon url
Returns:
icon

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.icons</a></div>
<h1 class="title" title="Class IconsFactory">Class IconsFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.icons.IconsFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">IconsFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to load icons from MagicDraw icons package or other locations.
 <p></p>
 All loaded icons are cached, so second attempt to load same icon will take it from a cache.
 <p></p>
 Icons are loader using <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(String)</code></a>, so icon name should follow that notation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">IconsFactory</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.lang.Class,java.lang.String)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given resource</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.lang.Class,java.lang.String,boolean)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given resource.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.lang.String)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given resource</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.lang.String,boolean)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given resource.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.net.URI,byte%5B%5D)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from given bytes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.net.URI,byte%5B%5D,int)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data,
 int size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from given bytes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.net.URL)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given url.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.net.URL,int)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url,
 int size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given url.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconData(java.io.File)">getIconData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reads icon data from a given file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconData(java.io.InputStream)">getIconData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reads icon data from a given stream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconData(java.net.URL)">getIconData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reads icon data from a given url.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotScaledIcon(java.lang.Class,java.lang.String)">getNotScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given resource.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotScaledIcon(java.lang.String)">getNotScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given resource.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotScaledIcon(java.net.URI,byte%5B%5D)">getNotScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from given bytes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotScaledIcon(java.net.URI,byte%5B%5D,int)">getNotScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data,
 int size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from given bytes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotScaledIcon(java.net.URL)">getNotScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given url.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotScaledIcon(java.net.URL,int)">getNotScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url,
 int size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a given url.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getQualifiedResourceName(java.lang.String)">getQualifiedResourceName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Resolves given resource name to a qualified name in this package.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResource(java.lang.String)">getResource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Provide URL to a resource in this package</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceAsStream(java.lang.String)">getResourceAsStream</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Provide stream to a resource in this package</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSvgIcon(java.net.URL)">getSvgIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load SVG icon from a given url.</div>
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
<h3>IconsFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IconsFactory</span>()</div>
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
<section class="detail" id="getIcon(java.lang.String)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Load icon from a given resource</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - icon name</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.lang.Class,java.lang.String)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Load icon from a given resource</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - icon resource class</dd>
<dd><code>name</code> - icon name</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotScaledIcon(java.lang.String)">
<h3>getNotScaledIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getNotScaledIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Load icon from a given resource. Does not scale icon by screen dpi.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - icon name</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotScaledIcon(java.lang.Class,java.lang.String)">
<h3>getNotScaledIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getNotScaledIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Load icon from a given resource. Does not scale icon by screen dpi.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - icon resource class</dd>
<dd><code>name</code> - icon name</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.lang.String,boolean)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean silent)</span></div>
<div class="block">Load icon from a given resource.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - icon name</dd>
<dd><code>silent</code> - true if missing icon should not be reported to a log file</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.lang.Class,java.lang.String,boolean)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean silent)</span></div>
<div class="block">Load icon from a given resource.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - icon resource class</dd>
<dd><code>name</code> - icon name</dd>
<dd><code>silent</code> - true if missing icon should not be reported to a log file</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceAsStream(java.lang.String)">
<h3>getResourceAsStream</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></span> <span class="element-name">getResourceAsStream</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Provide stream to a resource in this package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - resource name</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResourceAsStream(java.lang.String)" title="class or interface in java.lang"><code>Class.getResourceAsStream(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResource(java.lang.String)">
<h3>getResource</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></span> <span class="element-name">getResource</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Provide URL to a resource in this package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - resource name</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html#getResource(java.lang.String)" title="class or interface in java.lang"><code>Class.getResource(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedResourceName(java.lang.String)">
<h3>getQualifiedResourceName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedResourceName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceName)</span></div>
<div class="block">Resolves given resource name to a qualified name in this package. If resource name is already qualified (starts with "/"), returns it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resourceName</code> - resource name</dd>
<dt>Returns:</dt>
<dd>qualified resource name in this package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.net.URL)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="block">Load icon from a given url.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.net.URL,int)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url,
 int size)</span></div>
<div class="block">Load icon from a given url. Scales icon to a box of given size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
<dd><code>size</code> - icon box size. -1 if scaling is not needed</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotScaledIcon(java.net.URL)">
<h3>getNotScaledIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getNotScaledIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="block">Load icon from a given url. Does not scale icon by screen dpi.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotScaledIcon(java.net.URL,int)">
<h3>getNotScaledIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getNotScaledIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url,
 int size)</span></div>
<div class="block">Load icon from a given url. Scales icon to a box of given size. Does not scale icon by screen dpi.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
<dd><code>size</code> - icon box size. -1 if scaling is not needed</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.net.URI,byte[])">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data)</span></div>
<div class="block">Load icon from given bytes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri describing the location (or format) of the icon</dd>
<dd><code>data</code> - an array of icon data bytes</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.net.URI,byte[],int)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data,
 int size)</span></div>
<div class="block">Load icon from given bytes. Scales icon to a box of given size. Does not scale icon by screen dpi.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri</dd>
<dd><code>data</code> - an array of icon data</dd>
<dd><code>size</code> - icon box size. Icon will be scaled to this box. -1 if scaling is not needed</dd>
<dt>Returns:</dt>
<dd>icon</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../ui/HiDPIScaleUtilities.html#scaleIcon(int)"><code>HiDPIScaleUtilities.scaleIcon(int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotScaledIcon(java.net.URI,byte[])">
<h3>getNotScaledIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getNotScaledIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data)</span></div>
<div class="block">Load icon from given bytes. Scales icon to a box of given size. Does not scale icon by screen dpi.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - icon uri</dd>
<dd><code>data</code> - an array of icon data</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotScaledIcon(java.net.URI,byte[],int)">
<h3>getNotScaledIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getNotScaledIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 byte[] data,
 int size)</span></div>
<div class="block">Load icon from given bytes. Scales icon to a box of given size. Does not scale icon by screen dpi.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - icon uri</dd>
<dd><code>data</code> - an array of icon data</dd>
<dd><code>size</code> - icon box size. Icon will be scaled to this box. -1 if scaling is not needed</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconData(java.io.File)">
<h3>getIconData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">getIconData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Reads icon data from a given file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - an icon file</dd>
<dt>Returns:</dt>
<dd>icon data from given file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconData(java.net.URL)">
<h3>getIconData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">getIconData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="block">Reads icon data from a given url.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - icon url</dd>
<dt>Returns:</dt>
<dd>icon data from given url</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconData(java.io.InputStream)">
<h3>getIconData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">getIconData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input)</span></div>
<div class="block">Reads icon data from a given stream.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input stream</dd>
<dt>Returns:</dt>
<dd>icon data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSvgIcon(java.net.URL)">
<h3>getSvgIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getSvgIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="block">Load SVG icon from a given url.
 Other getIcon(...) methods in this class also can read SVG icons, but this one does not return icon compatible with <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing"><code>ImageIcon</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - icon url</dd>
<dt>Returns:</dt>
<dd>icon</dd>
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
