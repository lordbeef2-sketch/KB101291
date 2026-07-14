# JAVA OPENAPI: StyleManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/properties/StyleManager.html
- source_path: `com/nomagic/magicdraw/properties/StyleManager.html`
- source_sha256: `c5ccb58a2a3905319e603e8bd4edc0785fcba89c966b55796ba1cf1164ec015c`
- captured_utc: `2026-07-14T16:55:29.274170+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class StyleManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.properties.StyleManager

All Implemented Interfaces:
`com.nomagic.magicdraw.core.project.options.PersistentStyleManager`, `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApiAllpublic classStyleManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [PropertyVisitorAcceptor](PropertyVisitorAcceptor.html), [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html), [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html), com.nomagic.magicdraw.core.project.options.PersistentStyleManager

Style manager stores and manages a set of Styles.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[StyleManager.StyleListener](StyleManager.StyleListener.html)`
Listener for style events.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StyleManager](#%3Cinit%3E())()`
Default constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) visitor)`
Accepts the given visitor.
`void`
`[addStyle](#addStyle(com.nomagic.magicdraw.properties.Style))([Style](Style.html) style)`
Adds given style.
`static void`
`[addStyleListener](#addStyleListener(com.nomagic.magicdraw.properties.StyleManager.StyleListener))([StyleManager.StyleListener](StyleManager.StyleListener.html) listener)`
Adds static listener for listen style event.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`
Makes a copy of this manager.
`static void`
`[fireStyleAdded](#fireStyleAdded(com.nomagic.magicdraw.properties.StyleManager,com.nomagic.magicdraw.properties.Style))([StyleManager](StyleManager.html) manager,
 [Style](Style.html) style)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`[Style](Style.html)`
`[getDefaultStyle](#getDefaultStyle())()`
Returns default style.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Style](Style.html)>`
`[getOrderedStyles](#getOrderedStyles())()`
Returns styles ordered by names.
`[Style](Style.html)`
`[getStyle](#getStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns style with the specified name.
`[Style](Style.html)`
`[getStyleByID](#getStyleByID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Style](Style.html)>`
`[getStyles](#getStyles())()`
Returns all styles of this manager.
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`
Listens to PropertyNames.STYLE_MANAGER property change event.
`void`
`[removeStyle](#removeStyle(com.nomagic.magicdraw.properties.Style))([Style](Style.html) style)`
Removes given style.
`static void`
`[removeStyleListener](#removeStyleListener(com.nomagic.magicdraw.properties.StyleManager.StyleListener))([StyleManager.StyleListener](StyleManager.StyleListener.html) listener)`
Removes listener for listen style creation event.
`void`
`[setDefaultStyle](#setDefaultStyle(com.nomagic.magicdraw.properties.Style))([Style](Style.html) style)`
Sets default style for this manager.
`void`
`[setStyles](#setStyles(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Style](Style.html)> styles)`
Sets all styles.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StyleManager
public StyleManager()
Default constructor.
 ============ METHOD DETAIL ========== 
Method Details
addStyle
public void addStyle([Style](Style.html) style)
Adds given style.
Parameters:
`style` - the style to add.
removeStyle
public void removeStyle([Style](Style.html) style)
Removes given style.
Parameters:
`style` - the style to remove.
getDefaultStyle
@CheckForNullpublic [Style](Style.html) getDefaultStyle()
Returns default style.
Returns:
the default style of this manager.
getStyle
@CheckForNullpublic [Style](Style.html) getStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns style with the specified name.
Parameters:
`name` - style name.
Returns:
style if such exists or null if not found.
getStyleByID
@CheckForNullpublic [Style](Style.html) getStyleByID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
setDefaultStyle
public void setDefaultStyle(@CheckForNull
 [Style](Style.html) style)
Sets default style for this manager.
Parameters:
`style` - - the style to be default.
getStyles
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Style](Style.html)> getStyles()
Returns all styles of this manager.
Returns:
all styles. Collection is unmodifiable.
getOrderedStyles
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Style](Style.html)> getOrderedStyles()
Returns styles ordered by names.
Returns:
all styles ordered by name.
setStyles
public void setStyles([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Style](Style.html)> styles)
Sets all styles.
Parameters:
`styles` - a collection of new styles.
accept
public void accept([PropertyVisitor](PropertyVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Parameters:
`visitor` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Returns:
PropertyID.STYLE_MANAGER
See Also:
[`PropertyID.STYLE_MANAGER`](PropertyID.html#STYLE_MANAGER)
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Listens to PropertyNames.STYLE_MANAGER property change event.
 Takes `StyleManager`from new value and sets all styles from this manager to itself.
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Parameters:
`e` - the property change event.
clone
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) clone()
Makes a copy of this manager. Does deep clone.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
a clone of this manager.
fireStyleAdded
public static void fireStyleAdded([StyleManager](StyleManager.html) manager,
 [Style](Style.html) style)
addStyleListener
public static void addStyleListener([StyleManager.StyleListener](StyleManager.StyleListener.html) listener)
Adds static listener for listen style event. Listener is added in application scope and does not depends on project.
Parameters:
`listener` - Listener to be added.
removeStyleListener
public static void removeStyleListener([StyleManager.StyleListener](StyleManager.StyleListener.html) listener)
Removes listener for listen style creation event.
Parameters:
`listener` - Listener to be removed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class StyleManager">Class StyleManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.properties.StyleManager</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.core.project.options.PersistentStyleManager</code>, <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StyleManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a>, com.nomagic.magicdraw.core.project.options.PersistentStyleManager</span></div>
<div class="block">Style manager stores and manages a set of Styles.</div>
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
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StyleManager.StyleListener.html" title="interface in com.nomagic.magicdraw.properties">StyleManager.StyleListener</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listener for style events.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">StyleManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the given visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addStyle(com.nomagic.magicdraw.properties.Style)">addStyle</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds given style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addStyleListener(com.nomagic.magicdraw.properties.StyleManager.StyleListener)">addStyleListener</a><wbr/>(<a href="StyleManager.StyleListener.html" title="interface in com.nomagic.magicdraw.properties">StyleManager.StyleListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds static listener for listen style event.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Makes a copy of this manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fireStyleAdded(com.nomagic.magicdraw.properties.StyleManager,com.nomagic.magicdraw.properties.Style)">fireStyleAdded</a><wbr/>(<a href="StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> manager,
 <a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultStyle()">getDefaultStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns default style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrderedStyles()">getOrderedStyles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns styles ordered by names.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyle(java.lang.String)">getStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns style with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyleByID(java.lang.String)">getStyleByID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyles()">getStyles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all styles of this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens to PropertyNames.STYLE_MANAGER property change event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStyle(com.nomagic.magicdraw.properties.Style)">removeStyle</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStyleListener(com.nomagic.magicdraw.properties.StyleManager.StyleListener)">removeStyleListener</a><wbr/>(<a href="StyleManager.StyleListener.html" title="interface in com.nomagic.magicdraw.properties">StyleManager.StyleListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes listener for listen style creation event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultStyle(com.nomagic.magicdraw.properties.Style)">setDefaultStyle</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default style for this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyles(java.util.Collection)">setStyles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a>&gt; styles)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets all styles.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>StyleManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StyleManager</span>()</div>
<div class="block">Default constructor.</div>
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
<section class="detail" id="addStyle(com.nomagic.magicdraw.properties.Style)">
<h3>addStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addStyle</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
<div class="block">Adds given style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - the style to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStyle(com.nomagic.magicdraw.properties.Style)">
<h3>removeStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeStyle</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
<div class="block">Removes given style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - the style to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultStyle()">
<h3>getDefaultStyle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getDefaultStyle</span>()</div>
<div class="block">Returns default style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the default style of this manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyle(java.lang.String)">
<h3>getStyle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns style with the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - style name.</dd>
<dt>Returns:</dt>
<dd>style if such exists or null if not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyleByID(java.lang.String)">
<h3>getStyleByID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getStyleByID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDefaultStyle(com.nomagic.magicdraw.properties.Style)">
<h3>setDefaultStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultStyle</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
<div class="block">Sets default style for this manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - - the style to be default.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyles()">
<h3>getStyles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a>&gt;</span> <span class="element-name">getStyles</span>()</div>
<div class="block">Returns all styles of this manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all styles. Collection is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrderedStyles()">
<h3>getOrderedStyles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a>&gt;</span> <span class="element-name">getOrderedStyles</span>()</div>
<div class="block">Returns styles ordered by names.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all styles ordered by name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStyles(java.util.Collection)">
<h3>setStyles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyles</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a>&gt; styles)</span></div>
<div class="block">Sets all styles.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>styles</code> - a collection of new styles.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Returns property class type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.STYLE_MANAGER</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PropertyID.html#STYLE_MANAGER"><code>PropertyID.STYLE_MANAGER</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</span></div>
<div class="block">Listens to PropertyNames.STYLE_MANAGER property change event.
 Takes <code>StyleManager</code>from new value and sets all styles from this manager to itself.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - the property change event.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Makes a copy of this manager. Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a clone of this manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireStyleAdded(com.nomagic.magicdraw.properties.StyleManager,com.nomagic.magicdraw.properties.Style)">
<h3>fireStyleAdded</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">fireStyleAdded</span><wbr/><span class="parameters">(<a href="StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> manager,
 <a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
</section>
</li>
<li>
<section class="detail" id="addStyleListener(com.nomagic.magicdraw.properties.StyleManager.StyleListener)">
<h3>addStyleListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStyleListener</span><wbr/><span class="parameters">(<a href="StyleManager.StyleListener.html" title="interface in com.nomagic.magicdraw.properties">StyleManager.StyleListener</a> listener)</span></div>
<div class="block">Adds static listener for listen style event. Listener is added in application scope and does not depends on project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - Listener to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStyleListener(com.nomagic.magicdraw.properties.StyleManager.StyleListener)">
<h3>removeStyleListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeStyleListener</span><wbr/><span class="parameters">(<a href="StyleManager.StyleListener.html" title="interface in com.nomagic.magicdraw.properties">StyleManager.StyleListener</a> listener)</span></div>
<div class="block">Removes listener for listen style creation event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - Listener to be removed.</dd>
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
