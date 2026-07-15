# JAVA OPENAPI: HyperlinkUtils (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/hyperlinks/HyperlinkUtils.html
- source_path: `com/nomagic/magicdraw/hyperlinks/HyperlinkUtils.html`
- source_sha256: `fac1508bbbbfd3f93cec004cbe1b5132f151738545e30e1d50cb85af491f0ac0`
- captured_utc: `2026-07-14T16:51:22.783223+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.hyperlinks](package-summary.html)

## Class HyperlinkUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.hyperlinks.HyperlinkUtils

@OpenApiAllpublic classHyperlinkUtils
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Hyperlink utilities.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[HyperlinkUtils.DisplayableHyperlinkText](HyperlinkUtils.DisplayableHyperlinkText.html)`
Value holder for hyperlink text
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HYPERLINK_MODEL_ACTIVE_TAG](#HYPERLINK_MODEL_ACTIVE_TAG)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HYPERLINK_MODEL_TAG](#HYPERLINK_MODEL_TAG)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HYPERLINK_OWNER](#HYPERLINK_OWNER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HYPERLINK_TEXT_ACTIVE_TAG](#HYPERLINK_TEXT_ACTIVE_TAG)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HYPERLINK_TEXT_TAG](#HYPERLINK_TEXT_TAG)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HyperlinkUtils](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static boolean`
`[addHyperlink](#addHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)`
Adds given hyperlink as tagged value to the element.
`static [Hyperlink](Hyperlink.html)`
`[createHyperlink](#createHyperlink(java.lang.String,com.nomagic.magicdraw.uml.BaseElement))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [BaseElement](../uml/BaseElement.html) element)`
Creates hyperlink to given element
`static [Hyperlink](Hyperlink.html)`
`[createHyperlink](#createHyperlink(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url)`
Deprecated.
Uses the active project to resolve element hyperlinks.
`static [Hyperlink](Hyperlink.html)`
`[createHyperlink](#createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url,
 [Project](../core/Project.html) context)`
Creates hyperlink from given string url in the given project.
`static [Hyperlink](Hyperlink.html)`
`[createHyperlink](#createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,java.util.Map))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url,
 [Project](../core/Project.html) context,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> attributes)`
Creates hyperlink from given string url in the given project.
`static [Hyperlink](Hyperlink.html)`
`[getActiveHyperlink](#getActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns active hyperlink of the element
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Hyperlink](Hyperlink.html)>`
`[getAllHyperlinks](#getAllHyperlinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns hyperlinks of the element.
`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Hyperlink](Hyperlink.html)>`
`[getAllHyperlinksToElement](#getAllHyperlinksToElement(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) targetElement)`
Collects information about all hyperlinks pointing to the given target element.
`static [HyperlinkUtils.DisplayableHyperlinkText](HyperlinkUtils.DisplayableHyperlinkText.html)`
`[getDisplayableHyperlinkText](#getDisplayableHyperlinkText(com.nomagic.magicdraw.hyperlinks.Hyperlink))([Hyperlink](Hyperlink.html) hyperlink)`
Return information about hyperlink text.
`static [HyperlinkUtils.DisplayableHyperlinkText](HyperlinkUtils.DisplayableHyperlinkText.html)`
`[getDisplayableHyperlinkText](#getDisplayableHyperlinkText(com.nomagic.magicdraw.hyperlinks.Hyperlink,boolean))([Hyperlink](Hyperlink.html) hyperlink,
 boolean colorfulText)`
Return information about hyperlink text.
`static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon(com.nomagic.magicdraw.hyperlinks.Hyperlink))([Hyperlink](Hyperlink.html) hyperlink)`
Return hyperlink icon
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getURL](#getURL(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Get URL of mdel:// protocol for a given element.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getURLWithVersion](#getURLWithVersion(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Get URL of mdel:// protocol for a given element.
`static boolean`
`[hasActiveHyperlink](#hasActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns active hyperlink of the element
`static boolean`
`[hasHyperlink](#hasHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if element has hyperlink(s).
`static boolean`
`[hasHyperlinks](#hasHyperlinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static boolean`
`[isActiveHyperlink](#isActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)`
Check given hyperlink is marked as active on the given element
`static void`
`[makeActive](#makeActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)`
Make given hyperlink as active on a given element
`static void`
`[removeActive](#removeActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Remove active hyperlink from a given element
`static void`
`[removeHyperlink](#removeHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)`
Remove given hyperlink from the element.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
HYPERLINK_TEXT_TAG
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HYPERLINK_TEXT_TAG
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_TEXT_TAG)
HYPERLINK_TEXT_ACTIVE_TAG
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HYPERLINK_TEXT_ACTIVE_TAG
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_TEXT_ACTIVE_TAG)
HYPERLINK_MODEL_TAG
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HYPERLINK_MODEL_TAG
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_MODEL_TAG)
HYPERLINK_MODEL_ACTIVE_TAG
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HYPERLINK_MODEL_ACTIVE_TAG
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_MODEL_ACTIVE_TAG)
HYPERLINK_OWNER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HYPERLINK_OWNER
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_OWNER)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HyperlinkUtils
public HyperlinkUtils()
 ============ METHOD DETAIL ========== 
Method Details
getURL
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getURL([BaseElement](../uml/BaseElement.html) element)
Get URL of mdel:// protocol for a given element.
Parameters:
`element` - the given element
Returns:
URL of element.
getURLWithVersion
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getURLWithVersion([BaseElement](../uml/BaseElement.html) element)
Get URL of mdel:// protocol for a given element.
 If project is remote project - include project version number,
 if project is local - method is equivalent to [`getURL(BaseElement)`](#getURL(com.nomagic.magicdraw.uml.BaseElement)).
Parameters:
`element` - the given element
Returns:
URL of element.
getAllHyperlinks
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Hyperlink](Hyperlink.html)> getAllHyperlinks([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns hyperlinks of the element.
Parameters:
`element` - given element
Returns:
a collection of all hyperlinks
getAllHyperlinksToElement
public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Hyperlink](Hyperlink.html)> getAllHyperlinksToElement([BaseElement](../uml/BaseElement.html) targetElement)
Collects information about all hyperlinks pointing to the given target element.
Parameters:
`targetElement` - targetElement
Returns:
information about hyperlinks
removeActive
public static void removeActive([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Remove active hyperlink from a given element
Parameters:
`element` - element
makeActive
public static void makeActive([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)
Make given hyperlink as active on a given element
Parameters:
`element` - given element
`hyperlink` - given hyperlink
createHyperlink
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Hyperlink](Hyperlink.html) createHyperlink(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url)
Deprecated.
Uses the active project to resolve element hyperlinks.
 Use [`createHyperlink(String, String, Project)`](#createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)) and pass the correct context project.
Creates hyperlink from given string url.
Parameters:
`text` - given text
`url` - hyperlink url
Returns:
hyperlink
createHyperlink
public static [Hyperlink](Hyperlink.html) createHyperlink(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url,
 @CheckForNull
 [Project](../core/Project.html) context)
Creates hyperlink from given string url in the given project.
 Url can be project specific(e.g. an element hyperlink),in order for such url to be resolved correctly into a hyperlink the Project context must be provided, otherwise null is sufficient.
Parameters:
`text` - given text
`url` - hyperlink url
`context` - project as context
Returns:
hyperlink
createHyperlink
public static [Hyperlink](Hyperlink.html) createHyperlink(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url,
 @CheckForNull
 [Project](../core/Project.html) context,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> attributes)
Creates hyperlink from given string url in the given project.
Parameters:
`text` - given text
`url` - hyperlink url
`context` - project as context
`attributes` - additional attributes
Returns:
hyperlink
createHyperlink
public static [Hyperlink](Hyperlink.html) createHyperlink(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [BaseElement](../uml/BaseElement.html) element)
Creates hyperlink to given element
Parameters:
`text` - given text
`element` - element
Returns:
hyperlink
getActiveHyperlink
@CheckForNullpublic static [Hyperlink](Hyperlink.html) getActiveHyperlink([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns active hyperlink of the element
Parameters:
`element` - given element
Returns:
active hyperlink
hasActiveHyperlink
public static boolean hasActiveHyperlink([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns active hyperlink of the element
Parameters:
`element` - given element
Returns:
active hyperlink
hasHyperlink
public static boolean hasHyperlink([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if element has hyperlink(s).
Parameters:
`element` - element
Returns:
true if element has at least one hyperlink
isActiveHyperlink
public static boolean isActiveHyperlink([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)
Check given hyperlink is marked as active on the given element
Parameters:
`element` - element
`hyperlink` - hyperlink
Returns:
true if hyperlink is active
getIcon
@CheckForNullpublic static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon([Hyperlink](Hyperlink.html) hyperlink)
Return hyperlink icon
Parameters:
`hyperlink` - hyperlink
Returns:
hyperlink icon
getDisplayableHyperlinkText
public static [HyperlinkUtils.DisplayableHyperlinkText](HyperlinkUtils.DisplayableHyperlinkText.html) getDisplayableHyperlinkText(@CheckForNull
 [Hyperlink](Hyperlink.html) hyperlink)
Return information about hyperlink text.
Parameters:
`hyperlink` - hyperlink
Returns:
hyperlink text information
getDisplayableHyperlinkText
public static [HyperlinkUtils.DisplayableHyperlinkText](HyperlinkUtils.DisplayableHyperlinkText.html) getDisplayableHyperlinkText(@CheckForNull
 [Hyperlink](Hyperlink.html) hyperlink,
 boolean colorfulText)
Return information about hyperlink text.
Parameters:
`hyperlink` - hyperlink
`colorfulText` - false if text should be without colors, true if where possible, text should be colorful
Returns:
hyperlink text information
removeHyperlink
public static void removeHyperlink([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)
Remove given hyperlink from the element.
Parameters:
`element` - element
`hyperlink` - hyperlink
addHyperlink
public static boolean addHyperlink([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) hyperlink)
Adds given hyperlink as tagged value to the element.
 Checks if it has tagDefinition, taggedValue, taggedValue value
Parameters:
`element` - element
`hyperlink` - hyperlink to add
Returns:
true if hyperlink was added, false if such hyperlink already exist on the element
hasHyperlinks
public static boolean hasHyperlinks(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.hyperlinks</a></div>
<h1 class="title" title="Class HyperlinkUtils">Class HyperlinkUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.hyperlinks.HyperlinkUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">HyperlinkUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Hyperlink utilities.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="HyperlinkUtils.DisplayableHyperlinkText.html" title="class in com.nomagic.magicdraw.hyperlinks">HyperlinkUtils.DisplayableHyperlinkText</a></code></div>
<div class="col-last even-row-color">
<div class="block">Value holder for hyperlink text</div>
</div>
</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HYPERLINK_MODEL_ACTIVE_TAG">HYPERLINK_MODEL_ACTIVE_TAG</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HYPERLINK_MODEL_TAG">HYPERLINK_MODEL_TAG</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HYPERLINK_OWNER">HYPERLINK_OWNER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HYPERLINK_TEXT_ACTIVE_TAG">HYPERLINK_TEXT_ACTIVE_TAG</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HYPERLINK_TEXT_TAG">HYPERLINK_TEXT_TAG</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">HyperlinkUtils</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">addHyperlink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds given hyperlink as tagged value to the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHyperlink(java.lang.String,com.nomagic.magicdraw.uml.BaseElement)">createHyperlink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates hyperlink to given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createHyperlink(java.lang.String,java.lang.String)">createHyperlink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Uses the active project to resolve element hyperlinks.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)">createHyperlink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates hyperlink from given string url in the given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,java.util.Map)">createHyperlink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates hyperlink from given string url in the given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getActiveHyperlink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns active hyperlink of the element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllHyperlinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAllHyperlinks</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns hyperlinks of the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllHyperlinksToElement(com.nomagic.magicdraw.uml.BaseElement)">getAllHyperlinksToElement</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> targetElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects information about all hyperlinks pointing to the given target element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="HyperlinkUtils.DisplayableHyperlinkText.html" title="class in com.nomagic.magicdraw.hyperlinks">HyperlinkUtils.DisplayableHyperlinkText</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDisplayableHyperlinkText(com.nomagic.magicdraw.hyperlinks.Hyperlink)">getDisplayableHyperlinkText</a><wbr/>(<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return information about hyperlink text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="HyperlinkUtils.DisplayableHyperlinkText.html" title="class in com.nomagic.magicdraw.hyperlinks">HyperlinkUtils.DisplayableHyperlinkText</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDisplayableHyperlinkText(com.nomagic.magicdraw.hyperlinks.Hyperlink,boolean)">getDisplayableHyperlinkText</a><wbr/>(<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink,
 boolean colorfulText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return information about hyperlink text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(com.nomagic.magicdraw.hyperlinks.Hyperlink)">getIcon</a><wbr/>(<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return hyperlink icon</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getURL(com.nomagic.magicdraw.uml.BaseElement)">getURL</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get URL of mdel:// protocol for a given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getURLWithVersion(com.nomagic.magicdraw.uml.BaseElement)">getURLWithVersion</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get URL of mdel:// protocol for a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasActiveHyperlink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns active hyperlink of the element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasHyperlink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if element has hyperlink(s).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasHyperlinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasHyperlinks</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">isActiveHyperlink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check given hyperlink is marked as active on the given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#makeActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">makeActive</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Make given hyperlink as active on a given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeActive</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove active hyperlink from a given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">removeHyperlink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove given hyperlink from the element.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="HYPERLINK_TEXT_TAG">
<h3>HYPERLINK_TEXT_TAG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HYPERLINK_TEXT_TAG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_TEXT_TAG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HYPERLINK_TEXT_ACTIVE_TAG">
<h3>HYPERLINK_TEXT_ACTIVE_TAG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HYPERLINK_TEXT_ACTIVE_TAG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_TEXT_ACTIVE_TAG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HYPERLINK_MODEL_TAG">
<h3>HYPERLINK_MODEL_TAG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HYPERLINK_MODEL_TAG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_MODEL_TAG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HYPERLINK_MODEL_ACTIVE_TAG">
<h3>HYPERLINK_MODEL_ACTIVE_TAG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HYPERLINK_MODEL_ACTIVE_TAG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_MODEL_ACTIVE_TAG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HYPERLINK_OWNER">
<h3>HYPERLINK_OWNER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HYPERLINK_OWNER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.hyperlinks.HyperlinkUtils.HYPERLINK_OWNER">Constant Field Values</a></li>
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
<h3>HyperlinkUtils</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HyperlinkUtils</span>()</div>
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
<section class="detail" id="getURL(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getURL</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getURL</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Get URL of mdel:// protocol for a given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dt>Returns:</dt>
<dd>URL of element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getURLWithVersion(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getURLWithVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getURLWithVersion</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Get URL of mdel:// protocol for a given element.
 If project is remote project - include project version number,
 if project is local - method is equivalent to <a href="#getURL(com.nomagic.magicdraw.uml.BaseElement)"><code>getURL(BaseElement)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
<dt>Returns:</dt>
<dd>URL of element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllHyperlinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAllHyperlinks</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a>&gt;</span> <span class="element-name">getAllHyperlinks</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns hyperlinks of the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>a collection of all hyperlinks</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllHyperlinksToElement(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getAllHyperlinksToElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a>&gt;</span> <span class="element-name">getAllHyperlinksToElement</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> targetElement)</span></div>
<div class="block">Collects information about all hyperlinks pointing to the given target element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetElement</code> - targetElement</dd>
<dt>Returns:</dt>
<dd>information about hyperlinks</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeActive</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeActive</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Remove active hyperlink from a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>makeActive</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">makeActive</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</span></div>
<div class="block">Make given hyperlink as active on a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dd><code>hyperlink</code> - given hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHyperlink(java.lang.String,java.lang.String)">
<h3>createHyperlink</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">createHyperlink</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Uses the active project to resolve element hyperlinks.
 Use <a href="#createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)"><code>createHyperlink(String, String, Project)</code></a> and pass the correct context project.</div>
</div>
<div class="block">Creates hyperlink from given string url.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - given text</dd>
<dd><code>url</code> - hyperlink url</dd>
<dt>Returns:</dt>
<dd>hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)">
<h3>createHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">createHyperlink</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 @CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> context)</span></div>
<div class="block">Creates hyperlink from given string url in the given project.
 Url can be project specific(e.g. an element hyperlink),in order for such url to be resolved correctly into a hyperlink the Project context must be provided, otherwise null is sufficient.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - given text</dd>
<dd><code>url</code> - hyperlink url</dd>
<dd><code>context</code> - project as context</dd>
<dt>Returns:</dt>
<dd>hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHyperlink(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,java.util.Map)">
<h3>createHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">createHyperlink</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 @CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; attributes)</span></div>
<div class="block">Creates hyperlink from given string url in the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - given text</dd>
<dd><code>url</code> - hyperlink url</dd>
<dd><code>context</code> - project as context</dd>
<dd><code>attributes</code> - additional attributes</dd>
<dt>Returns:</dt>
<dd>hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHyperlink(java.lang.String,com.nomagic.magicdraw.uml.BaseElement)">
<h3>createHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">createHyperlink</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Creates hyperlink to given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - given text</dd>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getActiveHyperlink</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">getActiveHyperlink</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns active hyperlink of the element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>active hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasActiveHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasActiveHyperlink</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns active hyperlink of the element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>active hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasHyperlink</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if element has hyperlink(s).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element has at least one hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isActiveHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>isActiveHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isActiveHyperlink</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</span></div>
<div class="block">Check given hyperlink is marked as active on the given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>hyperlink</code> - hyperlink</dd>
<dt>Returns:</dt>
<dd>true if hyperlink is active</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</span></div>
<div class="block">Return hyperlink icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hyperlink</code> - hyperlink</dd>
<dt>Returns:</dt>
<dd>hyperlink icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDisplayableHyperlinkText(com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>getDisplayableHyperlinkText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="HyperlinkUtils.DisplayableHyperlinkText.html" title="class in com.nomagic.magicdraw.hyperlinks">HyperlinkUtils.DisplayableHyperlinkText</a></span> <span class="element-name">getDisplayableHyperlinkText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</span></div>
<div class="block">Return information about hyperlink text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hyperlink</code> - hyperlink</dd>
<dt>Returns:</dt>
<dd>hyperlink text information</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDisplayableHyperlinkText(com.nomagic.magicdraw.hyperlinks.Hyperlink,boolean)">
<h3>getDisplayableHyperlinkText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="HyperlinkUtils.DisplayableHyperlinkText.html" title="class in com.nomagic.magicdraw.hyperlinks">HyperlinkUtils.DisplayableHyperlinkText</a></span> <span class="element-name">getDisplayableHyperlinkText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink,
 boolean colorfulText)</span></div>
<div class="block">Return information about hyperlink text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hyperlink</code> - hyperlink</dd>
<dd><code>colorfulText</code> - false if text should be without colors, true if where possible, text should be colorful</dd>
<dt>Returns:</dt>
<dd>hyperlink text information</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>removeHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeHyperlink</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</span></div>
<div class="block">Remove given hyperlink from the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>hyperlink</code> - hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addHyperlink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>addHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">addHyperlink</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> hyperlink)</span></div>
<div class="block">Adds given hyperlink as tagged value to the element.
 Checks if it has tagDefinition, taggedValue, taggedValue value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>hyperlink</code> - hyperlink to add</dd>
<dt>Returns:</dt>
<dd>true if hyperlink was added, false if such hyperlink already exist on the element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasHyperlinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasHyperlinks</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasHyperlinks</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
