# JAVA OPENAPI: PropertyVisitorAdapter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/properties/PropertyVisitorAdapter.html
- source_path: `com/nomagic/magicdraw/properties/PropertyVisitorAdapter.html`
- source_sha256: `86d9c0e4bf8d58f4d4ec7702b178397a1acac3ff7f0f8738b3c7ab37b7d1c443`
- captured_utc: `2026-07-14T16:45:39.959533+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class PropertyVisitorAdapter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.properties.PropertyVisitorAdapter

All Implemented Interfaces:
`[PropertyVisitor](PropertyVisitor.html)`

@OpenApiAllpublic abstract classPropertyVisitorAdapter
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [PropertyVisitor](PropertyVisitor.html)

An abstract adapter class for property visiting.
 The methods in this class are empty.
 
 Extend this class to create a `PropertyVisitor` and override the methods for the required properties.
 (If you implement the `PropertyVisitor` interface, you have to define all of
 the methods in it. This abstract class defines empty methods for them
 all, so you can only override methods for properties you care about.)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PropertyVisitorAdapter](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[visit](#visit(com.nomagic.magicdraw.properties.BooleanProperty))([BooleanProperty](BooleanProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ChoiceListProperty))(com.nomagic.magicdraw.properties.ChoiceListProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ChoiceProperty))([ChoiceProperty](ChoiceProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty))([ClassPathEntriesListProperty](ClassPathEntriesListProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ColorProperty))([ColorProperty](ColorProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ConstraintProperty))(com.nomagic.magicdraw.properties.ConstraintProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.DateTimeProperty))([DateTimeProperty](DateTimeProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ElementInstanceProperty))(com.nomagic.magicdraw.properties.ElementInstanceProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ElementListProperty))([ElementListProperty](ElementListProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ElementProperty))([ElementProperty](ElementProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager))([ExtendablePropertyManager](ExtendablePropertyManager.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ExternalToolProperty))(com.nomagic.magicdraw.properties.ExternalToolProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.FileProperty))([FileProperty](FileProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.FontProperty))([FontProperty](FontProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ImageProperty))(com.nomagic.magicdraw.properties.ImageProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.JarEntryProperty))([JarEntryProperty](JarEntryProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty))([JDBCDriverClassNameProperty](JDBCDriverClassNameProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ListProperty))([ListProperty](ListProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.LocaleProperty))([LocaleProperty](LocaleProperty.html) p)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.MapProperty))(com.nomagic.magicdraw.properties.MapProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.NumberProperty))([NumberProperty](NumberProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PageFormatProperty))([PageFormatProperty](PageFormatProperty.html) p)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PasswordProperty))([PasswordProperty](PasswordProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.Property))([Property](Property.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram))([PropertyManagerByDiagram](PropertyManagerByDiagram.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype))([PropertyManagerByStereotype](PropertyManagerByStereotype.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.SpecificElementProperty))(com.nomagic.magicdraw.properties.SpecificElementProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.StringProperty))([StringProperty](StringProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.Style))([Style](Style.html) p)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.StyleManager))([StyleManager](StyleManager.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.TypeProperty))([TypeProperty](TypeProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty))(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty))(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PropertyVisitorAdapter
public PropertyVisitorAdapter()
 ============ METHOD DETAIL ========== 
Method Details
visit
public void visit([Property](Property.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.Property))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.ImageProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ImageProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([ColorProperty](ColorProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ColorProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([ChoiceProperty](ChoiceProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ChoiceProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.ChoiceListProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ChoiceListProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([FontProperty](FontProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.FontProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([FileProperty](FileProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.FileProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([BooleanProperty](BooleanProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.BooleanProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([NumberProperty](NumberProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.NumberProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([StyleManager](StyleManager.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.StyleManager))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([PropertyManager](PropertyManager.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PropertyManager))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([PropertyManagerByDiagram](PropertyManagerByDiagram.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([PropertyManagerByStereotype](PropertyManagerByStereotype.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([StringProperty](StringProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.StringProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([LocaleProperty](LocaleProperty.html) p)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.LocaleProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([PageFormatProperty](PageFormatProperty.html) p)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PageFormatProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([Style](Style.html) p)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.Style))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([JarEntryProperty](JarEntryProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.JarEntryProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([JDBCDriverClassNameProperty](JDBCDriverClassNameProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([PasswordProperty](PasswordProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PasswordProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([ClassPathEntriesListProperty](ClassPathEntriesListProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([TypeProperty](TypeProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.TypeProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([ElementProperty](ElementProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ElementProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.SpecificElementProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.SpecificElementProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.ConstraintProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ConstraintProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([ElementListProperty](ElementListProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ElementListProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.ElementInstanceProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ElementInstanceProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([ListProperty](ListProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ListProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([ExtendablePropertyManager](ExtendablePropertyManager.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.ExternalToolProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ExternalToolProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit(com.nomagic.magicdraw.properties.MapProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.MapProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visit
public void visit([DateTimeProperty](DateTimeProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Specified by:
`[visit](PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.DateTimeProperty))` in interface `[PropertyVisitor](PropertyVisitor.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class PropertyVisitorAdapter">Class PropertyVisitorAdapter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.properties.PropertyVisitorAdapter</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PropertyVisitorAdapter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></span></div>
<div class="block">An abstract adapter class for property visiting.
 The methods in this class are empty.
 <p></p>
 Extend this class to create a <code>PropertyVisitor</code> and override the methods for the required properties.
 (If you implement the <code>PropertyVisitor</code> interface, you have to define all of
 the methods in it. This abstract class defines empty methods for them
 all, so you can only override methods for properties you care about.)</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PropertyVisitorAdapter</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.BooleanProperty)">visit</a><wbr/>(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ChoiceListProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ChoiceListProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ChoiceProperty)">visit</a><wbr/>(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty)">visit</a><wbr/>(<a href="ClassPathEntriesListProperty.html" title="class in com.nomagic.magicdraw.properties">ClassPathEntriesListProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ColorProperty)">visit</a><wbr/>(<a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ConstraintProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ConstraintProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.DateTimeProperty)">visit</a><wbr/>(<a href="DateTimeProperty.html" title="class in com.nomagic.magicdraw.properties">DateTimeProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ElementInstanceProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ElementInstanceProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ElementListProperty)">visit</a><wbr/>(<a href="ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ElementProperty)">visit</a><wbr/>(<a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager)">visit</a><wbr/>(<a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties">ExtendablePropertyManager</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ExternalToolProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ExternalToolProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.FileProperty)">visit</a><wbr/>(<a href="FileProperty.html" title="class in com.nomagic.magicdraw.properties">FileProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.FontProperty)">visit</a><wbr/>(<a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ImageProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ImageProperty o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.JarEntryProperty)">visit</a><wbr/>(<a href="JarEntryProperty.html" title="class in com.nomagic.magicdraw.properties">JarEntryProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty)">visit</a><wbr/>(<a href="JDBCDriverClassNameProperty.html" title="class in com.nomagic.magicdraw.properties">JDBCDriverClassNameProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ListProperty)">visit</a><wbr/>(<a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.LocaleProperty)">visit</a><wbr/>(<a href="LocaleProperty.html" title="class in com.nomagic.magicdraw.properties">LocaleProperty</a> p)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.MapProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.MapProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.NumberProperty)">visit</a><wbr/>(<a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PageFormatProperty)">visit</a><wbr/>(<a href="PageFormatProperty.html" title="class in com.nomagic.magicdraw.properties">PageFormatProperty</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PasswordProperty)">visit</a><wbr/>(<a href="PasswordProperty.html" title="class in com.nomagic.magicdraw.properties">PasswordProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.Property)">visit</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PropertyManager)">visit</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram)">visit</a><wbr/>(<a href="PropertyManagerByDiagram.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByDiagram</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype)">visit</a><wbr/>(<a href="PropertyManagerByStereotype.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByStereotype</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.SpecificElementProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.SpecificElementProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.StringProperty)">visit</a><wbr/>(<a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.Style)">visit</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.StyleManager)">visit</a><wbr/>(<a href="StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.TypeProperty)">visit</a><wbr/>(<a href="TypeProperty.html" title="class in com.nomagic.magicdraw.properties">TypeProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<h3>PropertyVisitorAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyVisitorAdapter</span>()</div>
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
<section class="detail" id="visit(com.nomagic.magicdraw.properties.Property)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.Property)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ImageProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ImageProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ImageProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ColorProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ColorProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ChoiceProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ChoiceProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ChoiceListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ChoiceListProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ChoiceListProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.FontProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.FontProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.FileProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="FileProperty.html" title="class in com.nomagic.magicdraw.properties">FileProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.FileProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.BooleanProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.BooleanProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.NumberProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.NumberProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.StyleManager)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.StyleManager)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PropertyManager)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PropertyManagerByDiagram.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByDiagram</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PropertyManagerByStereotype.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByStereotype</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.StringProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.StringProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.LocaleProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="LocaleProperty.html" title="class in com.nomagic.magicdraw.properties">LocaleProperty</a> p)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.LocaleProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PageFormatProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PageFormatProperty.html" title="class in com.nomagic.magicdraw.properties">PageFormatProperty</a> p)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PageFormatProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.Style)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> p)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.Style)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.JarEntryProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="JarEntryProperty.html" title="class in com.nomagic.magicdraw.properties">JarEntryProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.JarEntryProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="JDBCDriverClassNameProperty.html" title="class in com.nomagic.magicdraw.properties">JDBCDriverClassNameProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PasswordProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PasswordProperty.html" title="class in com.nomagic.magicdraw.properties">PasswordProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.PasswordProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ClassPathEntriesListProperty.html" title="class in com.nomagic.magicdraw.properties">ClassPathEntriesListProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.TypeProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="TypeProperty.html" title="class in com.nomagic.magicdraw.properties">TypeProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.TypeProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ElementProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ElementProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.SpecificElementProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.SpecificElementProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.SpecificElementProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ConstraintProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ConstraintProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ConstraintProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ElementListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ElementListProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ElementInstanceProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ElementInstanceProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ElementInstanceProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ListProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties">ExtendablePropertyManager</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ExternalToolProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ExternalToolProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.ExternalToolProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.MapProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.MapProperty o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.MapProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.DateTimeProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="DateTimeProperty.html" title="class in com.nomagic.magicdraw.properties">DateTimeProperty</a> o)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitor.html#visit(com.nomagic.magicdraw.properties.DateTimeProperty)">visit</a></code> in interface <code><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
