# JAVA OPENAPI: MatrixSettings (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/dependencymatrix/persistence/MatrixSettings.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/persistence/MatrixSettings.html`
- source_sha256: `1eb0dc77d6755d277186215e45bd5f58d1c08c83264bc4e92d1d7e1ebf11d2a1`
- captured_utc: `2026-07-14T16:55:13.927993+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.persistence](package-summary.html)

## Class MatrixSettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings

@OpenApiAllpublic classMatrixSettings
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Matrix settings source. All settings are loaded from Dependency Matrix diagram component
 and visible through edit specification dialog

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[MatrixSettings.Direction](MatrixSettings.Direction.html)`
Dependency filter and default edit direction setting enum
`static enum`
`[MatrixSettings.LegendLocation](MatrixSettings.LegendLocation.html)`

`static enum`
`[MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html)`
Dependency Matrix group tree display modes
`static enum`
`[MatrixSettings.RelationOption](MatrixSettings.RelationOption.html)`
Show relationships option enum
`static enum`
`[MatrixSettings.SortingMode](MatrixSettings.SortingMode.html)`
sort mode enum
`static enum`
`[MatrixSettings.TextDirection](MatrixSettings.TextDirection.html)`
Column elements text direction
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MatrixSettings](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) matrixElement)`
Loads matrix settings for this element
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[areTypesHidden](#areTypesHidden())()`
Hide Types property
`void`
`[clearColumnCustomOrder](#clearColumnCustomOrder())()`

`void`
`[clearRowCustomOrder](#clearRowCustomOrder())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getColumnCollapsedNodes](#getColumnCollapsedNodes())()`
Collapsed column nodes property
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getColumnCustomOrder](#getColumnCustomOrder())()`
Column custom order property
`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getColumnHeaderHeight](#getColumnHeaderHeight())()`
Column header height property
`[MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html)`
`[getColumnOwnerDisplayMode](#getColumnOwnerDisplayMode())()`
Column owner display mode property
`[MatrixSettings.SortingMode](MatrixSettings.SortingMode.html)`
`[getColumnSortingMode](#getColumnSortingMode())()`
Column sorting mode property
`[MatrixSettings.TextDirection](MatrixSettings.TextDirection.html)`
`[getColumnTextDirection](#getColumnTextDirection())()`
Column text direction property
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getDependencyCriteria](#getDependencyCriteria())()`
Dependency criteria property
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescriptionAreaText](#getDescriptionAreaText())()`
Description area property
`[MatrixSettings.Direction](MatrixSettings.Direction.html)`
`[getDirection](#getDirection())()`
Dependency direction property
`[MatrixSettings.LegendLocation](MatrixSettings.LegendLocation.html)`
`[getLegendLocation](#getLegendLocation())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getMatrixElement](#getMatrixElement())()`
Dependency matrix element
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getRowCollapsedNodes](#getRowCollapsedNodes())()`
Collapsed row nodes property
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRowCustomOrder](#getRowCustomOrder())()`
Row Custom Order property
`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getRowHeaderWidth](#getRowHeaderWidth())()`
Row header width property
`[MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html)`
`[getRowOwnerDisplayMode](#getRowOwnerDisplayMode())()`
Row owner display mode property
`[MatrixSettings.SortingMode](MatrixSettings.SortingMode.html)`
`[getRowSortingMode](#getRowSortingMode())()`
Row sorting mode property
`[MatrixSettings.RelationOption](MatrixSettings.RelationOption.html)`
`[getShowElementsOption](#getShowElementsOption())()`
Show Elements property
`boolean`
`[isCriteriaAreaSuppressed](#isCriteriaAreaSuppressed())()`
Suppress criteria area property
`boolean`
`[isDependencyCriteriaHidden](#isDependencyCriteriaHidden())()`
Hide dependency criteria property
`boolean`
`[isEditable](#isEditable())()`
Is dependency matrix elements may be changed
`boolean`
`[isLegendEnabled](#isLegendEnabled())()`

`boolean`
`[isReadOnly](#isReadOnly())()`
Read Only property
`boolean`
`[isScopeHidden](#isScopeHidden())()`
Scope Hidden property
`boolean`
`[isShowInnerDependencies](#isShowInnerDependencies())()`
Show inner dependencies property
`boolean`
`[isWholeModelTakenAsScope](#isWholeModelTakenAsScope())()`
Whole model as scope property
`void`
`[setColumnCollapsedNodes](#setColumnCollapsedNodes(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> columnCollapsedNodes)`
Collapsed column nodes property
`void`
`[setColumnCustomOrder](#setColumnCustomOrder(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) columnCustomSortedElements)`
Column custom order property
`void`
`[setColumnHeaderHeight](#setColumnHeaderHeight(int))(int height)`
Column header height property
`void`
`[setColumnOwnerDisplayMode](#setColumnOwnerDisplayMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.OwnerDisplayMode))([MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html) displayType)`
Column owner display mode property
`void`
`[setColumnSortingMode](#setColumnSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode))([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode)`
Column sorting mode property
`void`
`[setColumnSortingMode](#setColumnSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode,boolean))([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode,
 boolean handleOrderTag)`
Column sorting mode property.
`void`
`[setColumnTextDirection](#setColumnTextDirection(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.TextDirection))([MatrixSettings.TextDirection](MatrixSettings.TextDirection.html) direction)`
Column text direction property
`void`
`[setDependencyCriteria](#setDependencyCriteria(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> dependencyCriteria)`
Dependency criteria property
`void`
`[setDescriptionArea](#setDescriptionArea(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) descriptionArea)`
Description area property
`void`
`[setDirection](#setDirection(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.Direction))([MatrixSettings.Direction](MatrixSettings.Direction.html) direction)`
Dependency direction property
`void`
`[setHideDependencyCriteria](#setHideDependencyCriteria(boolean))(boolean hideCriteria)`
Hide dependency criteria property
`void`
`[setHideScope](#setHideScope(boolean))(boolean hideScope)`
Scope Hidden property
`void`
`[setHideTypes](#setHideTypes(boolean))(boolean hideTypes)`
Hide Types property
`void`
`[setReadOnly](#setReadOnly(boolean))(boolean readOnly)`
Read Only property
`void`
`[setRowCollapsedNodes](#setRowCollapsedNodes(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> rowCollapsedNodes)`
Collapsed row nodes property
`void`
`[setRowCustomOrder](#setRowCustomOrder(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rowCustomSortedElements)`
Row Custom Order property
`void`
`[setRowHeaderWidth](#setRowHeaderWidth(java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) width)`
Row header width property
`void`
`[setRowOwnerDisplayMode](#setRowOwnerDisplayMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.OwnerDisplayMode))([MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html) displayType)`
Row owner display mode property
`void`
`[setRowSortingMode](#setRowSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode))([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode)`
Row sorting mode property
`void`
`[setRowSortingMode](#setRowSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode,boolean))([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode,
 boolean handleOrderTag)`
Row sorting mode property
`void`
`[setShowElementsOption](#setShowElementsOption(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.RelationOption))([MatrixSettings.RelationOption](MatrixSettings.RelationOption.html) option)`
Show Elements property
`void`
`[setShowInnerDependencies](#setShowInnerDependencies(boolean))(boolean showInnerDependencies)`
Show inner dependencies property
`void`
`[setSuppressCriteriaArea](#setSuppressCriteriaArea(boolean))(boolean suppress)`
Suppress criteria area property
`void`
`[setTakeWholeModelAsScope](#setTakeWholeModelAsScope(boolean))(boolean wholeModelAsScope)`
Whole model as scope property
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MatrixSettings
public MatrixSettings([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) matrixElement)
Loads matrix settings for this element
Parameters:
`matrixElement` - matrix diagram element
 ============ METHOD DETAIL ========== 
Method Details
getColumnTextDirection
public [MatrixSettings.TextDirection](MatrixSettings.TextDirection.html) getColumnTextDirection()
Column text direction property
Returns:
text direction property
setColumnTextDirection
public void setColumnTextDirection([MatrixSettings.TextDirection](MatrixSettings.TextDirection.html) direction)
Column text direction property
Parameters:
`direction` - text direction property
setShowInnerDependencies
public void setShowInnerDependencies(boolean showInnerDependencies)
Show inner dependencies property
Parameters:
`showInnerDependencies` - Show inner dependencies property
isShowInnerDependencies
public boolean isShowInnerDependencies()
Show inner dependencies property
Returns:
Show inner dependencies property
setShowElementsOption
public void setShowElementsOption([MatrixSettings.RelationOption](MatrixSettings.RelationOption.html) option)
Show Elements property
Parameters:
`option` - Show Elements property
getShowElementsOption
public [MatrixSettings.RelationOption](MatrixSettings.RelationOption.html) getShowElementsOption()
Show Elements property
Returns:
Show Elements property
setColumnHeaderHeight
public void setColumnHeaderHeight(int height)
Column header height property
Parameters:
`height` - Column header height property
getColumnHeaderHeight
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getColumnHeaderHeight()
Column header height property
Returns:
Column header height property
setRowHeaderWidth
public void setRowHeaderWidth([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) width)
Row header width property
Parameters:
`width` - Row header width property
getRowHeaderWidth
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getRowHeaderWidth()
Row header width property
Returns:
Row header width property
setDirection
public void setDirection([MatrixSettings.Direction](MatrixSettings.Direction.html) direction)
Dependency direction property
Parameters:
`direction` - Dependency direction property
getDirection
public [MatrixSettings.Direction](MatrixSettings.Direction.html) getDirection()
Dependency direction property
Returns:
Dependency direction property
isEditable
public boolean isEditable()
Is dependency matrix elements may be changed
Returns:
Is matrix element editable
getDependencyCriteria
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getDependencyCriteria()
Dependency criteria property
Returns:
Dependency criteria property
setDependencyCriteria
public void setDependencyCriteria([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> dependencyCriteria)
Dependency criteria property
Parameters:
`dependencyCriteria` - Dependency criteria property
getMatrixElement
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getMatrixElement()
Dependency matrix element
Returns:
Dependency matrix diagram element
setSuppressCriteriaArea
public void setSuppressCriteriaArea(boolean suppress)
Suppress criteria area property
Parameters:
`suppress` - Suppress criteria area property
isCriteriaAreaSuppressed
public boolean isCriteriaAreaSuppressed()
Suppress criteria area property
Returns:
Suppress criteria area property
isLegendEnabled
public boolean isLegendEnabled()
getLegendLocation
public [MatrixSettings.LegendLocation](MatrixSettings.LegendLocation.html) getLegendLocation()
setColumnOwnerDisplayMode
public void setColumnOwnerDisplayMode([MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html) displayType)
Column owner display mode property
Parameters:
`displayType` - Column owner display mode property
getColumnOwnerDisplayMode
public [MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html) getColumnOwnerDisplayMode()
Column owner display mode property
Returns:
Column owner display mode property
setRowOwnerDisplayMode
public void setRowOwnerDisplayMode([MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html) displayType)
Row owner display mode property
Parameters:
`displayType` - Row owner display mode property
getRowOwnerDisplayMode
public [MatrixSettings.OwnerDisplayMode](MatrixSettings.OwnerDisplayMode.html) getRowOwnerDisplayMode()
Row owner display mode property
Returns:
Row owner display mode property
getRowCollapsedNodes
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getRowCollapsedNodes()
Collapsed row nodes property
Returns:
Collapsed row nodes property
setRowCollapsedNodes
public void setRowCollapsedNodes([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> rowCollapsedNodes)
Collapsed row nodes property
Parameters:
`rowCollapsedNodes` - Collapsed row nodes property
getColumnCollapsedNodes
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getColumnCollapsedNodes()
Collapsed column nodes property
Returns:
Collapsed column nodes property
setColumnCollapsedNodes
public void setColumnCollapsedNodes([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> columnCollapsedNodes)
Collapsed column nodes property
Parameters:
`columnCollapsedNodes` - Collapsed column nodes property
getDescriptionAreaText
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescriptionAreaText()
Description area property
Returns:
Description area property
setDescriptionArea
public void setDescriptionArea(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) descriptionArea)
Description area property
Parameters:
`descriptionArea` - Description area property
setHideTypes
public void setHideTypes(boolean hideTypes)
Hide Types property
Parameters:
`hideTypes` - Hide Types property
areTypesHidden
public boolean areTypesHidden()
Hide Types property
Returns:
Hide Types property
setHideScope
public void setHideScope(boolean hideScope)
Scope Hidden property
Parameters:
`hideScope` - Scope Hidden property
isScopeHidden
public boolean isScopeHidden()
Scope Hidden property
Returns:
Scope Hidden property
setHideDependencyCriteria
public void setHideDependencyCriteria(boolean hideCriteria)
Hide dependency criteria property
Parameters:
`hideCriteria` - hide dependency criteria property
isDependencyCriteriaHidden
public boolean isDependencyCriteriaHidden()
Hide dependency criteria property
Returns:
hide dependency criteria property
setRowSortingMode
public void setRowSortingMode([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode)
Row sorting mode property
Parameters:
`sortingMode` - Row sorting mode property
setRowSortingMode
public void setRowSortingMode([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode,
 boolean handleOrderTag)
Row sorting mode property
Parameters:
`sortingMode` - Row sorting mode property
`handleOrderTag` - if true, and the provided sorting mode is not Custom, clears the rowCustomOrder tag
clearRowCustomOrder
public void clearRowCustomOrder()
getRowSortingMode
public [MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) getRowSortingMode()
Row sorting mode property
Returns:
Row sorting mode property
setColumnSortingMode
public void setColumnSortingMode([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode)
Column sorting mode property
Parameters:
`sortingMode` - Column sorting mode property
setColumnSortingMode
public void setColumnSortingMode([MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) sortingMode,
 boolean handleOrderTag)
Column sorting mode property. If the mode is not Custom, cleans up the columnCustomOrder
Parameters:
`sortingMode` - Column sorting mode property
`handleOrderTag` - if true, and the provided sorting mode is not Custom, clears the columnCustomOrder tag
clearColumnCustomOrder
public void clearColumnCustomOrder()
getColumnSortingMode
public [MatrixSettings.SortingMode](MatrixSettings.SortingMode.html) getColumnSortingMode()
Column sorting mode property
Returns:
Column sorting mode property
setReadOnly
public void setReadOnly(boolean readOnly)
Read Only property
Parameters:
`readOnly` - Read Only property
isReadOnly
public boolean isReadOnly()
Read Only property
Returns:
Read Only property
setTakeWholeModelAsScope
public void setTakeWholeModelAsScope(boolean wholeModelAsScope)
Whole model as scope property
Parameters:
`wholeModelAsScope` - Whole model as scope property
isWholeModelTakenAsScope
public boolean isWholeModelTakenAsScope()
Whole model as scope property
Returns:
Whole model as scope property
getColumnCustomOrder
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getColumnCustomOrder()
Column custom order property
Returns:
Column custom order property
setColumnCustomOrder
public void setColumnCustomOrder(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) columnCustomSortedElements)
Column custom order property
Parameters:
`columnCustomSortedElements` - Column custom order property
getRowCustomOrder
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRowCustomOrder()
Row Custom Order property
Returns:
Row custom order property
setRowCustomOrder
public void setRowCustomOrder(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) rowCustomSortedElements)
Row Custom Order property
Parameters:
`rowCustomSortedElements` - Row custom order property

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.persistence</a></div>
<h1 class="title" title="Class MatrixSettings">Class MatrixSettings</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MatrixSettings</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Matrix settings source. All settings are loaded from Dependency Matrix diagram component
 and visible through edit specification dialog</div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Dependency filter and default edit direction setting enum</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="MatrixSettings.LegendLocation.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.LegendLocation</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Dependency Matrix group tree display modes</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="MatrixSettings.RelationOption.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.RelationOption</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Show relationships option enum</div>
</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a></code></div>
<div class="col-last even-row-color">
<div class="block">sort mode enum</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="MatrixSettings.TextDirection.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.TextDirection</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Column elements text direction</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">MatrixSettings</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> matrixElement)</code></div>
<div class="col-last even-row-color">
<div class="block">Loads matrix settings for this element</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#areTypesHidden()">areTypesHidden</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hide Types property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumnCustomOrder()">clearColumnCustomOrder</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRowCustomOrder()">clearRowCustomOrder</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnCollapsedNodes()">getColumnCollapsedNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collapsed column nodes property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnCustomOrder()">getColumnCustomOrder</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column custom order property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnHeaderHeight()">getColumnHeaderHeight</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column header height property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnOwnerDisplayMode()">getColumnOwnerDisplayMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column owner display mode property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnSortingMode()">getColumnSortingMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column sorting mode property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.TextDirection.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.TextDirection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnTextDirection()">getColumnTextDirection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column text direction property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependencyCriteria()">getDependencyCriteria</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency criteria property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptionAreaText()">getDescriptionAreaText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Description area property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirection()">getDirection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency direction property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.LegendLocation.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.LegendLocation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLegendLocation()">getLegendLocation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMatrixElement()">getMatrixElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency matrix element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowCollapsedNodes()">getRowCollapsedNodes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collapsed row nodes property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowCustomOrder()">getRowCustomOrder</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row Custom Order property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowHeaderWidth()">getRowHeaderWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row header width property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowOwnerDisplayMode()">getRowOwnerDisplayMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row owner display mode property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowSortingMode()">getRowSortingMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row sorting mode property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.RelationOption.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.RelationOption</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowElementsOption()">getShowElementsOption</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show Elements property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCriteriaAreaSuppressed()">isCriteriaAreaSuppressed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Suppress criteria area property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDependencyCriteriaHidden()">isDependencyCriteriaHidden</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hide dependency criteria property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is dependency matrix elements may be changed</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLegendEnabled()">isLegendEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isReadOnly()">isReadOnly</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read Only property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isScopeHidden()">isScopeHidden</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scope Hidden property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowInnerDependencies()">isShowInnerDependencies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show inner dependencies property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isWholeModelTakenAsScope()">isWholeModelTakenAsScope</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Whole model as scope property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnCollapsedNodes(java.util.List)">setColumnCollapsedNodes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; columnCollapsedNodes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collapsed column nodes property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnCustomOrder(java.lang.String)">setColumnCustomOrder</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnCustomSortedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column custom order property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnHeaderHeight(int)">setColumnHeaderHeight</a><wbr/>(int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column header height property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnOwnerDisplayMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.OwnerDisplayMode)">setColumnOwnerDisplayMode</a><wbr/>(<a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a> displayType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column owner display mode property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode)">setColumnSortingMode</a><wbr/>(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column sorting mode property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode,boolean)">setColumnSortingMode</a><wbr/>(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode,
 boolean handleOrderTag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column sorting mode property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnTextDirection(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.TextDirection)">setColumnTextDirection</a><wbr/>(<a href="MatrixSettings.TextDirection.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.TextDirection</a> direction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column text direction property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDependencyCriteria(java.util.List)">setDependencyCriteria</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; dependencyCriteria)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency criteria property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescriptionArea(java.lang.String)">setDescriptionArea</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> descriptionArea)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Description area property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirection(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.Direction)">setDirection</a><wbr/>(<a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a> direction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency direction property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHideDependencyCriteria(boolean)">setHideDependencyCriteria</a><wbr/>(boolean hideCriteria)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hide dependency criteria property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHideScope(boolean)">setHideScope</a><wbr/>(boolean hideScope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scope Hidden property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHideTypes(boolean)">setHideTypes</a><wbr/>(boolean hideTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hide Types property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReadOnly(boolean)">setReadOnly</a><wbr/>(boolean readOnly)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read Only property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowCollapsedNodes(java.util.List)">setRowCollapsedNodes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; rowCollapsedNodes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collapsed row nodes property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowCustomOrder(java.lang.String)">setRowCustomOrder</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rowCustomSortedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row Custom Order property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowHeaderWidth(java.lang.Integer)">setRowHeaderWidth</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row header width property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowOwnerDisplayMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.OwnerDisplayMode)">setRowOwnerDisplayMode</a><wbr/>(<a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a> displayType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row owner display mode property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode)">setRowSortingMode</a><wbr/>(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row sorting mode property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode,boolean)">setRowSortingMode</a><wbr/>(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode,
 boolean handleOrderTag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row sorting mode property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowElementsOption(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.RelationOption)">setShowElementsOption</a><wbr/>(<a href="MatrixSettings.RelationOption.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.RelationOption</a> option)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show Elements property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowInnerDependencies(boolean)">setShowInnerDependencies</a><wbr/>(boolean showInnerDependencies)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show inner dependencies property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuppressCriteriaArea(boolean)">setSuppressCriteriaArea</a><wbr/>(boolean suppress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Suppress criteria area property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTakeWholeModelAsScope(boolean)">setTakeWholeModelAsScope</a><wbr/>(boolean wholeModelAsScope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Whole model as scope property</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>MatrixSettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MatrixSettings</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> matrixElement)</span></div>
<div class="block">Loads matrix settings for this element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrixElement</code> - matrix diagram element</dd>
</dl>
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
<section class="detail" id="getColumnTextDirection()">
<h3>getColumnTextDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.TextDirection.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.TextDirection</a></span> <span class="element-name">getColumnTextDirection</span>()</div>
<div class="block">Column text direction property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>text direction property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColumnTextDirection(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.TextDirection)">
<h3>setColumnTextDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnTextDirection</span><wbr/><span class="parameters">(<a href="MatrixSettings.TextDirection.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.TextDirection</a> direction)</span></div>
<div class="block">Column text direction property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - text direction property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowInnerDependencies(boolean)">
<h3>setShowInnerDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowInnerDependencies</span><wbr/><span class="parameters">(boolean showInnerDependencies)</span></div>
<div class="block">Show inner dependencies property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showInnerDependencies</code> - Show inner dependencies property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowInnerDependencies()">
<h3>isShowInnerDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowInnerDependencies</span>()</div>
<div class="block">Show inner dependencies property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Show inner dependencies property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowElementsOption(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.RelationOption)">
<h3>setShowElementsOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowElementsOption</span><wbr/><span class="parameters">(<a href="MatrixSettings.RelationOption.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.RelationOption</a> option)</span></div>
<div class="block">Show Elements property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>option</code> - Show Elements property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShowElementsOption()">
<h3>getShowElementsOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.RelationOption.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.RelationOption</a></span> <span class="element-name">getShowElementsOption</span>()</div>
<div class="block">Show Elements property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Show Elements property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColumnHeaderHeight(int)">
<h3>setColumnHeaderHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnHeaderHeight</span><wbr/><span class="parameters">(int height)</span></div>
<div class="block">Column header height property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>height</code> - Column header height property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnHeaderHeight()">
<h3>getColumnHeaderHeight</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getColumnHeaderHeight</span>()</div>
<div class="block">Column header height property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Column header height property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRowHeaderWidth(java.lang.Integer)">
<h3>setRowHeaderWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowHeaderWidth</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> width)</span></div>
<div class="block">Row header width property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - Row header width property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowHeaderWidth()">
<h3>getRowHeaderWidth</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getRowHeaderWidth</span>()</div>
<div class="block">Row header width property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Row header width property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirection(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.Direction)">
<h3>setDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirection</span><wbr/><span class="parameters">(<a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a> direction)</span></div>
<div class="block">Dependency direction property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - Dependency direction property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirection()">
<h3>getDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">getDirection</span>()</div>
<div class="block">Dependency direction property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Dependency direction property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="block">Is dependency matrix elements may be changed</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Is matrix element editable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependencyCriteria()">
<h3>getDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getDependencyCriteria</span>()</div>
<div class="block">Dependency criteria property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Dependency criteria property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDependencyCriteria(java.util.List)">
<h3>setDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDependencyCriteria</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; dependencyCriteria)</span></div>
<div class="block">Dependency criteria property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dependencyCriteria</code> - Dependency criteria property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMatrixElement()">
<h3>getMatrixElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getMatrixElement</span>()</div>
<div class="block">Dependency matrix element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Dependency matrix diagram element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSuppressCriteriaArea(boolean)">
<h3>setSuppressCriteriaArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuppressCriteriaArea</span><wbr/><span class="parameters">(boolean suppress)</span></div>
<div class="block">Suppress criteria area property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suppress</code> - Suppress criteria area property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCriteriaAreaSuppressed()">
<h3>isCriteriaAreaSuppressed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCriteriaAreaSuppressed</span>()</div>
<div class="block">Suppress criteria area property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Suppress criteria area property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLegendEnabled()">
<h3>isLegendEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLegendEnabled</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLegendLocation()">
<h3>getLegendLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.LegendLocation.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.LegendLocation</a></span> <span class="element-name">getLegendLocation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setColumnOwnerDisplayMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.OwnerDisplayMode)">
<h3>setColumnOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a> displayType)</span></div>
<div class="block">Column owner display mode property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayType</code> - Column owner display mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnOwnerDisplayMode()">
<h3>getColumnOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a></span> <span class="element-name">getColumnOwnerDisplayMode</span>()</div>
<div class="block">Column owner display mode property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Column owner display mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRowOwnerDisplayMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.OwnerDisplayMode)">
<h3>setRowOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a> displayType)</span></div>
<div class="block">Row owner display mode property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayType</code> - Row owner display mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowOwnerDisplayMode()">
<h3>getRowOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.OwnerDisplayMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.OwnerDisplayMode</a></span> <span class="element-name">getRowOwnerDisplayMode</span>()</div>
<div class="block">Row owner display mode property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Row owner display mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowCollapsedNodes()">
<h3>getRowCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRowCollapsedNodes</span>()</div>
<div class="block">Collapsed row nodes property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Collapsed row nodes property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRowCollapsedNodes(java.util.List)">
<h3>setRowCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowCollapsedNodes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; rowCollapsedNodes)</span></div>
<div class="block">Collapsed row nodes property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowCollapsedNodes</code> - Collapsed row nodes property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnCollapsedNodes()">
<h3>getColumnCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnCollapsedNodes</span>()</div>
<div class="block">Collapsed column nodes property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Collapsed column nodes property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColumnCollapsedNodes(java.util.List)">
<h3>setColumnCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnCollapsedNodes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; columnCollapsedNodes)</span></div>
<div class="block">Collapsed column nodes property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>columnCollapsedNodes</code> - Collapsed column nodes property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescriptionAreaText()">
<h3>getDescriptionAreaText</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescriptionAreaText</span>()</div>
<div class="block">Description area property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Description area property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDescriptionArea(java.lang.String)">
<h3>setDescriptionArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescriptionArea</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> descriptionArea)</span></div>
<div class="block">Description area property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptionArea</code> - Description area property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHideTypes(boolean)">
<h3>setHideTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHideTypes</span><wbr/><span class="parameters">(boolean hideTypes)</span></div>
<div class="block">Hide Types property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hideTypes</code> - Hide Types property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="areTypesHidden()">
<h3>areTypesHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">areTypesHidden</span>()</div>
<div class="block">Hide Types property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Hide Types property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHideScope(boolean)">
<h3>setHideScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHideScope</span><wbr/><span class="parameters">(boolean hideScope)</span></div>
<div class="block">Scope Hidden property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hideScope</code> - Scope Hidden property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isScopeHidden()">
<h3>isScopeHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isScopeHidden</span>()</div>
<div class="block">Scope Hidden property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Scope Hidden property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHideDependencyCriteria(boolean)">
<h3>setHideDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHideDependencyCriteria</span><wbr/><span class="parameters">(boolean hideCriteria)</span></div>
<div class="block">Hide dependency criteria property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hideCriteria</code> - hide dependency criteria property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDependencyCriteriaHidden()">
<h3>isDependencyCriteriaHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDependencyCriteriaHidden</span>()</div>
<div class="block">Hide dependency criteria property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>hide dependency criteria property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRowSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode)">
<h3>setRowSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowSortingMode</span><wbr/><span class="parameters">(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode)</span></div>
<div class="block">Row sorting mode property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortingMode</code> - Row sorting mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRowSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode,boolean)">
<h3>setRowSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowSortingMode</span><wbr/><span class="parameters">(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode,
 boolean handleOrderTag)</span></div>
<div class="block">Row sorting mode property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortingMode</code> - Row sorting mode property</dd>
<dd><code>handleOrderTag</code> - if true, and the provided sorting mode is not Custom, clears the rowCustomOrder tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearRowCustomOrder()">
<h3>clearRowCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRowCustomOrder</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRowSortingMode()">
<h3>getRowSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a></span> <span class="element-name">getRowSortingMode</span>()</div>
<div class="block">Row sorting mode property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Row sorting mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColumnSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode)">
<h3>setColumnSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnSortingMode</span><wbr/><span class="parameters">(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode)</span></div>
<div class="block">Column sorting mode property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortingMode</code> - Column sorting mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColumnSortingMode(com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.SortingMode,boolean)">
<h3>setColumnSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnSortingMode</span><wbr/><span class="parameters">(<a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a> sortingMode,
 boolean handleOrderTag)</span></div>
<div class="block">Column sorting mode property. If the mode is not Custom, cleans up the columnCustomOrder</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortingMode</code> - Column sorting mode property</dd>
<dd><code>handleOrderTag</code> - if true, and the provided sorting mode is not Custom, clears the columnCustomOrder tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearColumnCustomOrder()">
<h3>clearColumnCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumnCustomOrder</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getColumnSortingMode()">
<h3>getColumnSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.SortingMode.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.SortingMode</a></span> <span class="element-name">getColumnSortingMode</span>()</div>
<div class="block">Column sorting mode property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Column sorting mode property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReadOnly(boolean)">
<h3>setReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReadOnly</span><wbr/><span class="parameters">(boolean readOnly)</span></div>
<div class="block">Read Only property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>readOnly</code> - Read Only property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReadOnly()">
<h3>isReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isReadOnly</span>()</div>
<div class="block">Read Only property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Read Only property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTakeWholeModelAsScope(boolean)">
<h3>setTakeWholeModelAsScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTakeWholeModelAsScope</span><wbr/><span class="parameters">(boolean wholeModelAsScope)</span></div>
<div class="block">Whole model as scope property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>wholeModelAsScope</code> - Whole model as scope property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isWholeModelTakenAsScope()">
<h3>isWholeModelTakenAsScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isWholeModelTakenAsScope</span>()</div>
<div class="block">Whole model as scope property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Whole model as scope property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnCustomOrder()">
<h3>getColumnCustomOrder</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getColumnCustomOrder</span>()</div>
<div class="block">Column custom order property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Column custom order property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColumnCustomOrder(java.lang.String)">
<h3>setColumnCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnCustomOrder</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnCustomSortedElements)</span></div>
<div class="block">Column custom order property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>columnCustomSortedElements</code> - Column custom order property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowCustomOrder()">
<h3>getRowCustomOrder</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRowCustomOrder</span>()</div>
<div class="block">Row Custom Order property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Row custom order property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRowCustomOrder(java.lang.String)">
<h3>setRowCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowCustomOrder</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rowCustomSortedElements)</span></div>
<div class="block">Row Custom Order property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowCustomSortedElements</code> - Row custom order property</dd>
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
