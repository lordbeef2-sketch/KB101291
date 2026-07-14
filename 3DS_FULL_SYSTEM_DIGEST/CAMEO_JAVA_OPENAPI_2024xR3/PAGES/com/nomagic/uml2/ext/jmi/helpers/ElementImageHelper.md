# JAVA OPENAPI: ElementImageHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/helpers/ElementImageHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/ElementImageHelper.html`
- source_sha256: `3a8d8a1c0086aa1f195f20a505c1343faa5acfea4d8d0113f387c682962705ca`
- captured_utc: `2026-07-14T16:56:15.824686+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class ElementImageHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper

@OpenApiAllpublic classElementImageHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Utility class to work with 'Image' property, which is contained by all elements.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html)`
Structure, which contains information of image: content, format and location.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementImageHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html)`
`[getCustomImageInformation](#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Gets image information by element if image is set.
`static [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html)`
`[getCustomImageInformation](#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)`
Deprecated.
use [`getCustomImageInformation(Element)`](#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
`static [Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getElementToSetImage](#getElementToSetImage(com.nomagic.magicdraw.uml.ModelElementProvider))([ModelElementProvider](../../../../magicdraw/uml/ModelElementProvider.html) pElement)`
Returns element to set image property
`static [ResizableIcon](../../../../ui/ResizableIcon.html)`
`[getIconFromCustomImageProperty](#getIconFromCustomImageProperty(com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation))([ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html) imageInformation)`
A helper method to create resizable icon from image information.
`static [ResizableIcon](../../../../ui/ResizableIcon.html)`
`[getIconFromCustomImageProperty](#getIconFromCustomImageProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../magicdraw/classes/mdkernel/Element.html) element)`
Gets 'ResizableIcon', which is created from the image information.
`static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html)`
`[getImageHolderStereotype](#getImageHolderStereotype(com.nomagic.magicdraw.core.Project))([Project](../../../../magicdraw/core/Project.html) project)`
Return image holder stereotype from a given project.
`static [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html)`
`[getProvidedElementImageInformation](#getProvidedElementImageInformation(com.nomagic.magicdraw.uml.ModelElementProvider))([ModelElementProvider](../../../../magicdraw/uml/ModelElementProvider.html) pElement)`
Returns image information of provided element
`static void`
`[setCustomImageInformation](#setCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html) imageInformation)`
Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype.
`static void`
`[setCustomImageInformation](#setCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Image))([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Image](../../magicdraw/mdprofiles/Image.html) image)`
Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementImageHelper
public ElementImageHelper()
 ============ METHOD DETAIL ========== 
Method Details
getCustomImageInformation
@CheckForNullpublic static [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html) getCustomImageInformation([Element](../../magicdraw/classes/mdkernel/Element.html) element)
Gets image information by element if image is set.
Parameters:
`element` - element, which contains image property.
Returns:
image information if image to element is set, otherwise null.
getCustomImageInformation
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html) getCustomImageInformation([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) stereotype)
Deprecated.
use [`getCustomImageInformation(Element)`](#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
Gets image information by element if image is set.
Parameters:
`element` - element, which contains image property.
Returns:
image information if image to element is set, otherwise null.
setCustomImageInformation
public static void setCustomImageInformation([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 [Image](../../magicdraw/mdprofiles/Image.html) image)
Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype.
Parameters:
`element` - element, which contains image property
`image` - information source used to set image
setCustomImageInformation
public static void setCustomImageInformation([Element](../../magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html) imageInformation)
Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype. If image is removed,
 stereotype is removed too.
Parameters:
`element` - element, which contains image property
`imageInformation` - structure, which contains information of image: content, format and location
getImageHolderStereotype
public static [Stereotype](../../magicdraw/mdprofiles/Stereotype.html) getImageHolderStereotype([Project](../../../../magicdraw/core/Project.html) project)
Return image holder stereotype from a given project.
Parameters:
`project` - project
Returns:
image holder stereotype
getIconFromCustomImageProperty
@CheckForNullpublic static [ResizableIcon](../../../../ui/ResizableIcon.html) getIconFromCustomImageProperty(@CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) element)
Gets 'ResizableIcon', which is created from the image information.
Parameters:
`element` - element, which contains image property
Returns:
'ResizableIcon' if image is set to element's 'Image' property, otherwise null
getIconFromCustomImageProperty
@CheckForNullpublic static [ResizableIcon](../../../../ui/ResizableIcon.html) getIconFromCustomImageProperty(@CheckForNull
 [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html) imageInformation)
A helper method to create resizable icon from image information.
Parameters:
`imageInformation` - image info
Returns:
icon
getElementToSetImage
@CheckForNullpublic static [Element](../../magicdraw/classes/mdkernel/Element.html) getElementToSetImage([ModelElementProvider](../../../../magicdraw/uml/ModelElementProvider.html) pElement)
Returns element to set image property
Parameters:
`pElement` - presentation element
Returns:
element to which image should be set
getProvidedElementImageInformation
@CheckForNullpublic static [ElementImageHelper.ImageInformation](ElementImageHelper.ImageInformation.html) getProvidedElementImageInformation([ModelElementProvider](../../../../magicdraw/uml/ModelElementProvider.html) pElement)
Returns image information of provided element
Parameters:
`pElement` - presentation element
Returns:
element to which image should be set

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class ElementImageHelper">Class ElementImageHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementImageHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with 'Image' property, which is contained by all elements.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></code></div>
<div class="col-last even-row-color">
<div class="block">Structure, which contains information of image: content, format and location.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementImageHelper</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCustomImageInformation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets image information by element if image is set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getCustomImageInformation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>getCustomImageInformation(Element)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementToSetImage(com.nomagic.magicdraw.uml.ModelElementProvider)">getElementToSetImage</a><wbr/>(<a href="../../../../magicdraw/uml/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> pElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns element to set image property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFromCustomImageProperty(com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation)">getIconFromCustomImageProperty</a><wbr/>(<a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a> imageInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">A helper method to create resizable icon from image information.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconFromCustomImageProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getIconFromCustomImageProperty</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets 'ResizableIcon', which is created from the image information.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageHolderStereotype(com.nomagic.magicdraw.core.Project)">getImageHolderStereotype</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return image holder stereotype from a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProvidedElementImageInformation(com.nomagic.magicdraw.uml.ModelElementProvider)">getProvidedElementImageInformation</a><wbr/>(<a href="../../../../magicdraw/uml/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> pElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns image information of provided element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation)">setCustomImageInformation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a> imageInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Image)">setCustomImageInformation</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype.</div>
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
<h3>ElementImageHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementImageHelper</span>()</div>
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
<section class="detail" id="getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCustomImageInformation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></span> <span class="element-name">getCustomImageInformation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets image information by element if image is set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element, which contains image property.</dd>
<dt>Returns:</dt>
<dd>image information if image to element is set, otherwise null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getCustomImageInformation</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></span> <span class="element-name">getCustomImageInformation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>getCustomImageInformation(Element)</code></a></div>
</div>
<div class="block">Gets image information by element if image is set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element, which contains image property.</dd>
<dt>Returns:</dt>
<dd>image information if image to element is set, otherwise null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Image)">
<h3>setCustomImageInformation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCustomImageInformation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../magicdraw/mdprofiles/Image.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Image</a> image)</span></div>
<div class="block">Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element, which contains image property</dd>
<dd><code>image</code> - information source used to set image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomImageInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation)">
<h3>setCustomImageInformation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCustomImageInformation</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a> imageInformation)</span></div>
<div class="block">Set image information to given element: stereotype 'CustomImageHolder' is applied on element
 and image information are saved to the tags of this stereotype. If image is removed,
 stereotype is removed too.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element, which contains image property</dd>
<dd><code>imageInformation</code> - structure, which contains information of image: content, format and location</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageHolderStereotype(com.nomagic.magicdraw.core.Project)">
<h3>getImageHolderStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getImageHolderStereotype</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Return image holder stereotype from a given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>image holder stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFromCustomImageProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getIconFromCustomImageProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconFromCustomImageProperty</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Gets 'ResizableIcon', which is created from the image information.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element, which contains image property</dd>
<dt>Returns:</dt>
<dd>'ResizableIcon' if image is set to element's 'Image' property, otherwise null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconFromCustomImageProperty(com.nomagic.uml2.ext.jmi.helpers.ElementImageHelper.ImageInformation)">
<h3>getIconFromCustomImageProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconFromCustomImageProperty</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a> imageInformation)</span></div>
<div class="block">A helper method to create resizable icon from image information.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageInformation</code> - image info</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementToSetImage(com.nomagic.magicdraw.uml.ModelElementProvider)">
<h3>getElementToSetImage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElementToSetImage</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/uml/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> pElement)</span></div>
<div class="block">Returns element to set image property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pElement</code> - presentation element</dd>
<dt>Returns:</dt>
<dd>element to which image should be set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProvidedElementImageInformation(com.nomagic.magicdraw.uml.ModelElementProvider)">
<h3>getProvidedElementImageInformation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementImageHelper.ImageInformation.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ElementImageHelper.ImageInformation</a></span> <span class="element-name">getProvidedElementImageInformation</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/uml/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> pElement)</span></div>
<div class="block">Returns image information of provided element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pElement</code> - presentation element</dd>
<dt>Returns:</dt>
<dd>element to which image should be set</dd>
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
