# JAVA OPENAPI: DependencyMatrixProfile.DependencyMatrixStereotype (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.DependencyMatrixStereotype.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.DependencyMatrixStereotype.html`
- source_sha256: `c93c5a4dad5406c68e5cd989f1fa2bb6ca0797bada5be0fb77debffe51b6fc7f`
- captured_utc: `2026-07-14T16:45:32.734439+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.persistence](package-summary.html)

## Class DependencyMatrixProfile.DependencyMatrixStereotype

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)
com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype

Enclosing class:
`[DependencyMatrixProfile](DependencyMatrixProfile.html)`

public static classDependencyMatrixProfile.DependencyMatrixStereotype
extends [ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLUMNCOLLAPSEDNODES](#COLUMNCOLLAPSEDNODES)`
Specifies the collapsed nodes of the Dependency Matrix.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLUMNCUSTOMORDER](#COLUMNCUSTOMORDER)`
Contains Dependency Matrix column elements custom sorting order.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLUMNHEADERHEIGHT](#COLUMNHEADERHEIGHT)`
Specifies the height of the column header in pixels.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLUMNOWNERDISPLAYMODE](#COLUMNOWNERDISPLAYMODE)`
Select Compact tree mode to show only direct and common element owners in the nested mode.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLUMNSORTINGMODE](#COLUMNSORTINGMODE)`
Select Ascending or Descending to sort elements alphabetically.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLUMNTEXTDIRECTION](#COLUMNTEXTDIRECTION)`
Specifies the text direction of the Matrix column headers.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYCRITERIA](#DEPENDENCYCRITERIA)`
Select an expression type and specify the expression to be used as the relation criteria.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DESCRIPTIONAREA](#DESCRIPTIONAREA)`
Specify the description of the Dependency Matrix.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DIRECTION](#DIRECTION)`
Select Row to column or Column to row to filter the displayed dependencies by direction.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[HIDEDEPENDENCYCRITERIA](#HIDEDEPENDENCYCRITERIA)`
Set to false to show the Dependency Criteria filter.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[HIDESCOPE](#HIDESCOPE)`
Set to false to show the scope filter.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[HIDETYPES](#HIDETYPES)`
Set to false to show the types filter.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[LEGENDLOCATION](#LEGENDLOCATION)`
Legend explains the meaning of colors and styles of links in the Dependency Matrix.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[READONLY](#READONLY)`
Set to true to treat Dependency Matrix cells as non editable.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ROWCOLLAPSEDNODES](#ROWCOLLAPSEDNODES)`
Specifies the collapsed nodes of the Dependency Matrix.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ROWCUSTOMORDER](#ROWCUSTOMORDER)`
Contains Dependency Matrix row elements custom sorting order.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ROWHEADERWIDTH](#ROWHEADERWIDTH)`
Specifies the width of the row header in pixels.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ROWOWNERDISPLAYMODE](#ROWOWNERDISPLAYMODE)`
Select Compact tree mode to show only direct and common element owners in the nested mode.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ROWSORTINGMODE](#ROWSORTINGMODE)`
Select Ascending or Descending to sort elements alphabetically.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SHOWELEMENTS](#SHOWELEMENTS)`
Select All to show all elements from the selected scope.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SHOWINNERDEPENDENCIES](#SHOWINNERDEPENDENCIES)`
Set to true to show the number of dependencies in the owner element on cell.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[STEREOTYPE_NAME](#STEREOTYPE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SUPPRESSCRITERIAAREA](#SUPPRESSCRITERIAAREA)`
Set to false to show the Criteria area.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TAKEWHOLEMODELASSCOPE](#TAKEWHOLEMODELASSCOPE)`
Set to true to take whole model as default scope.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[DependencyMatrixStereotype](#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile))([DependencyMatrixProfile](DependencyMatrixProfile.html) profile)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addColumnCollapsedNodes](#addColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addDependencyCriteria](#addDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[addRowCollapsedNodes](#addRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`protected void`
`[clear](#clear())()`

`void`
`[clearColumnCollapsedNodes](#clearColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearColumnCustomOrder](#clearColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearColumnHeaderHeight](#clearColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearColumnOwnerDisplayMode](#clearColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearColumnSortingMode](#clearColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearColumnTextDirection](#clearColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearDependencyCriteria](#clearDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearDescriptionArea](#clearDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearDirection](#clearDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearHideDependencyCriteria](#clearHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearHideScope](#clearHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearHideTypes](#clearHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearLegendLocation](#clearLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearReadOnly](#clearReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRowCollapsedNodes](#clearRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRowCustomOrder](#clearRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRowHeaderWidth](#clearRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRowOwnerDisplayMode](#clearRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRowSortingMode](#clearRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowElements](#clearShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowInnerDependencies](#clearShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearSuppressCriteriaArea](#clearSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTakeWholeModelAsScope](#clearTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getColumnCollapsedNodes](#getColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getColumnCollapsedNodesProperty](#getColumnCollapsedNodesProperty())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getColumnCustomOrder](#getColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getColumnCustomOrderProperty](#getColumnCustomOrderProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html)`
`[getColumnHeaderHeight](#getColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getColumnHeaderHeightProperty](#getColumnHeaderHeightProperty())()`

`[DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html)`
`[getColumnOwnerDisplayMode](#getColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getColumnOwnerDisplayModeProperty](#getColumnOwnerDisplayModeProperty())()`

`[DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html)`
`[getColumnSortingMode](#getColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getColumnSortingModeProperty](#getColumnSortingModeProperty())()`

`[DependencyMatrixProfile.TextDirectionEnum](DependencyMatrixProfile.TextDirectionEnum.html)`
`[getColumnTextDirection](#getColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getColumnTextDirectionProperty](#getColumnTextDirectionProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[getDependencyCriteria](#getDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getDependencyCriteriaProperty](#getDependencyCriteriaProperty())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDescriptionArea](#getDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getDescriptionAreaProperty](#getDescriptionAreaProperty())()`

`[DependencyMatrixProfile.DirectionEnum](DependencyMatrixProfile.DirectionEnum.html)`
`[getDirection](#getDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getDirectionProperty](#getDirectionProperty())()`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getHideDependencyCriteriaProperty](#getHideDependencyCriteriaProperty())()`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getHideScopeProperty](#getHideScopeProperty())()`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getHideTypesProperty](#getHideTypesProperty())()`

`[DependencyMatrixProfile.LegendLocationEnum](DependencyMatrixProfile.LegendLocationEnum.html)`
`[getLegendLocation](#getLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getLegendLocationProperty](#getLegendLocationProperty())()`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getReadOnlyProperty](#getReadOnlyProperty())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getRowCollapsedNodes](#getRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRowCollapsedNodesProperty](#getRowCollapsedNodesProperty())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRowCustomOrder](#getRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRowCustomOrderProperty](#getRowCustomOrderProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html)`
`[getRowHeaderWidth](#getRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRowHeaderWidthProperty](#getRowHeaderWidthProperty())()`

`[DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html)`
`[getRowOwnerDisplayMode](#getRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRowOwnerDisplayModeProperty](#getRowOwnerDisplayModeProperty())()`

`[DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html)`
`[getRowSortingMode](#getRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRowSortingModeProperty](#getRowSortingModeProperty())()`

`[DependencyMatrixProfile.RelationOptionEnum](DependencyMatrixProfile.RelationOptionEnum.html)`
`[getShowElements](#getShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowElementsProperty](#getShowElementsProperty())()`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowInnerDependenciesProperty](#getShowInnerDependenciesProperty())()`

`[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Returns stereotype for this wrapper.
`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getSuppressCriteriaAreaProperty](#getSuppressCriteriaAreaProperty())()`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getTakeWholeModelAsScopeProperty](#getTakeWholeModelAsScopeProperty())()`

`boolean`
`[is](#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isHideDependencyCriteria](#isHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isHideScope](#isHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isHideTypes](#isHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static boolean`
`[isInstance](#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isReadOnly](#isReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isShowInnerDependencies](#isShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isSuppressCriteriaArea](#isSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isTakeWholeModelAsScope](#isTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[removeColumnCollapsedNodes](#removeColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeDependencyCriteria](#removeDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[removeRowCollapsedNodes](#removeRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setColumnCollapsedNodes](#setColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setColumnCustomOrder](#setColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setColumnHeaderHeight](#setColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setColumnOwnerDisplayMode](#setColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OwnerDisplayModeEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html) value)`

`void`
`[setColumnSortingMode](#setColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SortingModeEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html) value)`

`void`
`[setColumnTextDirection](#setColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TextDirectionEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.TextDirectionEnum](DependencyMatrixProfile.TextDirectionEnum.html) value)`

`void`
`[setDependencyCriteria](#setDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> value)`

`void`
`[setDescriptionArea](#setDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setDirection](#setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DirectionEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.DirectionEnum](DependencyMatrixProfile.DirectionEnum.html) value)`

`void`
`[setHideDependencyCriteria](#setHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setHideScope](#setHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setHideTypes](#setHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setLegendLocation](#setLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LegendLocationEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.LegendLocationEnum](DependencyMatrixProfile.LegendLocationEnum.html) value)`

`void`
`[setReadOnly](#setReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setRowCollapsedNodes](#setRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setRowCustomOrder](#setRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setRowHeaderWidth](#setRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setRowOwnerDisplayMode](#setRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OwnerDisplayModeEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html) value)`

`void`
`[setRowSortingMode](#setRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SortingModeEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html) value)`

`void`
`[setShowElements](#setShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RelationOptionEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [DependencyMatrixProfile.RelationOptionEnum](DependencyMatrixProfile.RelationOptionEnum.html) value)`

`void`
`[setShowInnerDependencies](#setShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setSuppressCriteriaArea](#setSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setTakeWholeModelAsScope](#setTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)
`[apply](../../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDerivedStereotype](../../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isSameOrDerivedStereotype](../../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [unApply](../../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STEREOTYPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.STEREOTYPE_NAME)
COLUMNCOLLAPSEDNODES
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLUMNCOLLAPSEDNODES
Specifies the collapsed nodes of the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNCOLLAPSEDNODES)
COLUMNCUSTOMORDER
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLUMNCUSTOMORDER
Contains Dependency Matrix column elements custom sorting order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNCUSTOMORDER)
COLUMNHEADERHEIGHT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLUMNHEADERHEIGHT
Specifies the height of the column header in pixels.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNHEADERHEIGHT)
COLUMNOWNERDISPLAYMODE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLUMNOWNERDISPLAYMODE
Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNOWNERDISPLAYMODE)
COLUMNSORTINGMODE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLUMNSORTINGMODE
Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNSORTINGMODE)
COLUMNTEXTDIRECTION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLUMNTEXTDIRECTION
Specifies the text direction of the Matrix column headers.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNTEXTDIRECTION)
DEPENDENCYCRITERIA
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DEPENDENCYCRITERIA
Select an expression type and specify the expression to be used as the relation criteria.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.DEPENDENCYCRITERIA)
DESCRIPTIONAREA
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DESCRIPTIONAREA
Specify the description of the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.DESCRIPTIONAREA)
DIRECTION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DIRECTION
Select Row to column or Column to row to filter the displayed dependencies by direction. Select Both to show all dependencies.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.DIRECTION)
HIDEDEPENDENCYCRITERIA
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) HIDEDEPENDENCYCRITERIA
Set to false to show the Dependency Criteria filter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.HIDEDEPENDENCYCRITERIA)
HIDESCOPE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) HIDESCOPE
Set to false to show the scope filter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.HIDESCOPE)
HIDETYPES
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) HIDETYPES
Set to false to show the types filter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.HIDETYPES)
LEGENDLOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) LEGENDLOCATION
Legend explains the meaning of colors and styles of links in the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.LEGENDLOCATION)
READONLY
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) READONLY
Set to true to treat Dependency Matrix cells as non editable.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.READONLY)
ROWCOLLAPSEDNODES
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ROWCOLLAPSEDNODES
Specifies the collapsed nodes of the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWCOLLAPSEDNODES)
ROWCUSTOMORDER
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ROWCUSTOMORDER
Contains Dependency Matrix row elements custom sorting order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWCUSTOMORDER)
ROWHEADERWIDTH
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ROWHEADERWIDTH
Specifies the width of the row header in pixels.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWHEADERWIDTH)
ROWOWNERDISPLAYMODE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ROWOWNERDISPLAYMODE
Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWOWNERDISPLAYMODE)
ROWSORTINGMODE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ROWSORTINGMODE
Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWSORTINGMODE)
SHOWELEMENTS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SHOWELEMENTS
Select All to show all elements from the selected scope. Select With relations to show the elements that have dependency criteria. Select Without relations to show the elements that have no dependency criteria.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.SHOWELEMENTS)
SHOWINNERDEPENDENCIES
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SHOWINNERDEPENDENCIES
Set to true to show the number of dependencies in the owner element on cell.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.SHOWINNERDEPENDENCIES)
SUPPRESSCRITERIAAREA
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SUPPRESSCRITERIAAREA
Set to false to show the Criteria area.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.SUPPRESSCRITERIAAREA)
TAKEWHOLEMODELASSCOPE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TAKEWHOLEMODELASSCOPE
Set to true to take whole model as default scope.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.TAKEWHOLEMODELASSCOPE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DependencyMatrixStereotype
protected DependencyMatrixStereotype([DependencyMatrixProfile](DependencyMatrixProfile.html) profile)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
public [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())`
Returns stereotype for this wrapper.
Specified by:
`[getStereotype](../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())` in class `[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)`
Returns:
stereotype
getColumnCollapsedNodesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getColumnCollapsedNodesProperty()
getColumnCustomOrderProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getColumnCustomOrderProperty()
getColumnHeaderHeightProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getColumnHeaderHeightProperty()
getColumnOwnerDisplayModeProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getColumnOwnerDisplayModeProperty()
getColumnSortingModeProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getColumnSortingModeProperty()
getColumnTextDirectionProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getColumnTextDirectionProperty()
getDependencyCriteriaProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getDependencyCriteriaProperty()
getDescriptionAreaProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getDescriptionAreaProperty()
getDirectionProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getDirectionProperty()
getHideDependencyCriteriaProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getHideDependencyCriteriaProperty()
getHideScopeProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getHideScopeProperty()
getHideTypesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getHideTypesProperty()
getLegendLocationProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getLegendLocationProperty()
getReadOnlyProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getReadOnlyProperty()
getRowCollapsedNodesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRowCollapsedNodesProperty()
getRowCustomOrderProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRowCustomOrderProperty()
getRowHeaderWidthProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRowHeaderWidthProperty()
getRowOwnerDisplayModeProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRowOwnerDisplayModeProperty()
getRowSortingModeProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRowSortingModeProperty()
getShowElementsProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowElementsProperty()
getShowInnerDependenciesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowInnerDependenciesProperty()
getSuppressCriteriaAreaProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getSuppressCriteriaAreaProperty()
getTakeWholeModelAsScopeProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getTakeWholeModelAsScopeProperty()
setColumnCollapsedNodes
public void setColumnCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearColumnCollapsedNodes
public void clearColumnCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addColumnCollapsedNodes
public void addColumnCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeColumnCollapsedNodes
public void removeColumnCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getColumnCollapsedNodes
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getColumnCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setColumnCustomOrder
public void setColumnCustomOrder([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
clearColumnCustomOrder
public void clearColumnCustomOrder([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getColumnCustomOrder
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getColumnCustomOrder([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setColumnHeaderHeight
public void setColumnHeaderHeight([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) value)
clearColumnHeaderHeight
public void clearColumnHeaderHeight([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getColumnHeaderHeight
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) getColumnHeaderHeight([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setColumnOwnerDisplayMode
public void setColumnOwnerDisplayMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html) value)
clearColumnOwnerDisplayMode
public void clearColumnOwnerDisplayMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getColumnOwnerDisplayMode
@CheckForNullpublic [DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html) getColumnOwnerDisplayMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setColumnSortingMode
public void setColumnSortingMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html) value)
clearColumnSortingMode
public void clearColumnSortingMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getColumnSortingMode
@CheckForNullpublic [DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html) getColumnSortingMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setColumnTextDirection
public void setColumnTextDirection([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.TextDirectionEnum](DependencyMatrixProfile.TextDirectionEnum.html) value)
clearColumnTextDirection
public void clearColumnTextDirection([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getColumnTextDirection
@CheckForNullpublic [DependencyMatrixProfile.TextDirectionEnum](DependencyMatrixProfile.TextDirectionEnum.html) getColumnTextDirection([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setDependencyCriteria
public void setDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> value)
clearDependencyCriteria
public void clearDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addDependencyCriteria
public void addDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
removeDependencyCriteria
public void removeDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
getDependencyCriteria
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> getDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setDescriptionArea
public void setDescriptionArea([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
clearDescriptionArea
public void clearDescriptionArea([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getDescriptionArea
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDescriptionArea([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setDirection
public void setDirection([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.DirectionEnum](DependencyMatrixProfile.DirectionEnum.html) value)
clearDirection
public void clearDirection([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getDirection
@CheckForNullpublic [DependencyMatrixProfile.DirectionEnum](DependencyMatrixProfile.DirectionEnum.html) getDirection([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setHideDependencyCriteria
public void setHideDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearHideDependencyCriteria
public void clearHideDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isHideDependencyCriteria
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isHideDependencyCriteria([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setHideScope
public void setHideScope([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearHideScope
public void clearHideScope([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isHideScope
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isHideScope([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setHideTypes
public void setHideTypes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearHideTypes
public void clearHideTypes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isHideTypes
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isHideTypes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setLegendLocation
public void setLegendLocation([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.LegendLocationEnum](DependencyMatrixProfile.LegendLocationEnum.html) value)
clearLegendLocation
public void clearLegendLocation([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getLegendLocation
@CheckForNullpublic [DependencyMatrixProfile.LegendLocationEnum](DependencyMatrixProfile.LegendLocationEnum.html) getLegendLocation([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setReadOnly
public void setReadOnly([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearReadOnly
public void clearReadOnly([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isReadOnly
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isReadOnly([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRowCollapsedNodes
public void setRowCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> value)
clearRowCollapsedNodes
public void clearRowCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addRowCollapsedNodes
public void addRowCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
removeRowCollapsedNodes
public void removeRowCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getRowCollapsedNodes
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getRowCollapsedNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRowCustomOrder
public void setRowCustomOrder([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
clearRowCustomOrder
public void clearRowCustomOrder([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getRowCustomOrder
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRowCustomOrder([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRowHeaderWidth
public void setRowHeaderWidth([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) value)
clearRowHeaderWidth
public void clearRowHeaderWidth([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getRowHeaderWidth
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) getRowHeaderWidth([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRowOwnerDisplayMode
public void setRowOwnerDisplayMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html) value)
clearRowOwnerDisplayMode
public void clearRowOwnerDisplayMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getRowOwnerDisplayMode
@CheckForNullpublic [DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html) getRowOwnerDisplayMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRowSortingMode
public void setRowSortingMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html) value)
clearRowSortingMode
public void clearRowSortingMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getRowSortingMode
@CheckForNullpublic [DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html) getRowSortingMode([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowElements
public void setShowElements([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [DependencyMatrixProfile.RelationOptionEnum](DependencyMatrixProfile.RelationOptionEnum.html) value)
clearShowElements
public void clearShowElements([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getShowElements
@CheckForNullpublic [DependencyMatrixProfile.RelationOptionEnum](DependencyMatrixProfile.RelationOptionEnum.html) getShowElements([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowInnerDependencies
public void setShowInnerDependencies([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearShowInnerDependencies
public void clearShowInnerDependencies([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isShowInnerDependencies
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isShowInnerDependencies([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setSuppressCriteriaArea
public void setSuppressCriteriaArea([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearSuppressCriteriaArea
public void clearSuppressCriteriaArea([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isSuppressCriteriaArea
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isSuppressCriteriaArea([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setTakeWholeModelAsScope
public void setTakeWholeModelAsScope([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) value)
clearTakeWholeModelAsScope
public void clearTakeWholeModelAsScope([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isTakeWholeModelAsScope
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isTakeWholeModelAsScope([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
clear
protected void clear()
is
public boolean is(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isInstance
public static boolean isInstance(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.persistence</a></div>
<h1 class="title" title="Class DependencyMatrixProfile.DependencyMatrixStereotype">Class DependencyMatrixProfile.DependencyMatrixStereotype</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation.StereotypeWrapper</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">DependencyMatrixProfile.DependencyMatrixStereotype</span>
<span class="extends-implements">extends <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></span></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COLUMNCOLLAPSEDNODES">COLUMNCOLLAPSEDNODES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the collapsed nodes of the Dependency Matrix.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLUMNCUSTOMORDER">COLUMNCUSTOMORDER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains Dependency Matrix column elements custom sorting order.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COLUMNHEADERHEIGHT">COLUMNHEADERHEIGHT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the height of the column header in pixels.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLUMNOWNERDISPLAYMODE">COLUMNOWNERDISPLAYMODE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Select Compact tree mode to show only direct and common element owners in the nested mode.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COLUMNSORTINGMODE">COLUMNSORTINGMODE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Select Ascending or Descending to sort elements alphabetically.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLUMNTEXTDIRECTION">COLUMNTEXTDIRECTION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies the text direction of the Matrix column headers.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYCRITERIA">DEPENDENCYCRITERIA</a></code></div>
<div class="col-last even-row-color">
<div class="block">Select an expression type and specify the expression to be used as the relation criteria.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DESCRIPTIONAREA">DESCRIPTIONAREA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specify the description of the Dependency Matrix.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIRECTION">DIRECTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Select Row to column or Column to row to filter the displayed dependencies by direction.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HIDEDEPENDENCYCRITERIA">HIDEDEPENDENCYCRITERIA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to false to show the Dependency Criteria filter.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HIDESCOPE">HIDESCOPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Set to false to show the scope filter.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HIDETYPES">HIDETYPES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to false to show the types filter.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LEGENDLOCATION">LEGENDLOCATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Legend explains the meaning of colors and styles of links in the Dependency Matrix.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#READONLY">READONLY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true to treat Dependency Matrix cells as non editable.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROWCOLLAPSEDNODES">ROWCOLLAPSEDNODES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the collapsed nodes of the Dependency Matrix.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROWCUSTOMORDER">ROWCUSTOMORDER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains Dependency Matrix row elements custom sorting order.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROWHEADERWIDTH">ROWHEADERWIDTH</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the width of the row header in pixels.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROWOWNERDISPLAYMODE">ROWOWNERDISPLAYMODE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Select Compact tree mode to show only direct and common element owners in the nested mode.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROWSORTINGMODE">ROWSORTINGMODE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Select Ascending or Descending to sort elements alphabetically.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWELEMENTS">SHOWELEMENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Select All to show all elements from the selected scope.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOWINNERDEPENDENCIES">SHOWINNERDEPENDENCIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Set to true to show the number of dependencies in the owner element on cell.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STEREOTYPE_NAME">STEREOTYPE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUPPRESSCRITERIAAREA">SUPPRESSCRITERIAAREA</a></code></div>
<div class="col-last even-row-color">
<div class="block">Set to false to show the Criteria area.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TAKEWHOLEMODELASSCOPE">TAKEWHOLEMODELASSCOPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true to take whole model as default scope.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile)">DependencyMatrixStereotype</a><wbr/>(<a href="DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a> profile)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addColumnCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">addDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addRowCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearColumnCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearColumnCustomOrder</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearColumnHeaderHeight</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearColumnOwnerDisplayMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearColumnSortingMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearColumnTextDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearDescriptionArea</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearHideDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearHideScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearHideTypes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearLegendLocation</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearReadOnly</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRowCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRowCustomOrder</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRowHeaderWidth</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRowOwnerDisplayMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRowSortingMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowInnerDependencies</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearSuppressCriteriaArea</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTakeWholeModelAsScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumnCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnCollapsedNodesProperty()">getColumnCollapsedNodesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumnCustomOrder</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnCustomOrderProperty()">getColumnCustomOrderProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumnHeaderHeight</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnHeaderHeightProperty()">getColumnHeaderHeightProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumnOwnerDisplayMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnOwnerDisplayModeProperty()">getColumnOwnerDisplayModeProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumnSortingMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnSortingModeProperty()">getColumnSortingModeProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.TextDirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.TextDirectionEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumnTextDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnTextDirectionProperty()">getColumnTextDirectionProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependencyCriteriaProperty()">getDependencyCriteriaProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDescriptionArea</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptionAreaProperty()">getDescriptionAreaProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.DirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DirectionEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectionProperty()">getDirectionProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHideDependencyCriteriaProperty()">getHideDependencyCriteriaProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHideScopeProperty()">getHideScopeProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHideTypesProperty()">getHideTypesProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.LegendLocationEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.LegendLocationEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLegendLocation</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLegendLocationProperty()">getLegendLocationProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReadOnlyProperty()">getReadOnlyProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRowCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowCollapsedNodesProperty()">getRowCollapsedNodesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRowCustomOrder</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowCustomOrderProperty()">getRowCustomOrderProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRowHeaderWidth</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowHeaderWidthProperty()">getRowHeaderWidthProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRowOwnerDisplayMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowOwnerDisplayModeProperty()">getRowOwnerDisplayModeProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRowSortingMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowSortingModeProperty()">getRowSortingModeProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.RelationOptionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.RelationOptionEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getShowElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowElementsProperty()">getShowElementsProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowInnerDependenciesProperty()">getShowInnerDependenciesProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype for this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuppressCriteriaAreaProperty()">getSuppressCriteriaAreaProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTakeWholeModelAsScopeProperty()">getTakeWholeModelAsScopeProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isHideDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isHideScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isHideTypes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstance</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isReadOnly</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowInnerDependencies</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSuppressCriteriaArea</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isTakeWholeModelAsScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeColumnCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">removeDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeRowCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setColumnCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setColumnCustomOrder</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setColumnHeaderHeight</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OwnerDisplayModeEnum)">setColumnOwnerDisplayMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SortingModeEnum)">setColumnSortingMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TextDirectionEnum)">setColumnTextDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.TextDirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.TextDirectionEnum</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setDescriptionArea</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DirectionEnum)">setDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.DirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DirectionEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setHideDependencyCriteria</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setHideScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setHideTypes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LegendLocationEnum)">setLegendLocation</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.LegendLocationEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.LegendLocationEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setReadOnly</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setRowCollapsedNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setRowCustomOrder</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setRowHeaderWidth</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OwnerDisplayModeEnum)">setRowOwnerDisplayMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SortingModeEnum)">setRowSortingMode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RelationOptionEnum)">setShowElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="DependencyMatrixProfile.RelationOptionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.RelationOptionEnum</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowInnerDependencies</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setSuppressCriteriaArea</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setTakeWholeModelAsScope</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation.StereotypeWrapper">Methods inherited from class com.nomagic.profiles.<a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></h3>
<code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">apply</a>, <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isDerivedStereotype</a>, <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isSameOrDerivedStereotype</a>, <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">unApply</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="STEREOTYPE_NAME">
<h3>STEREOTYPE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEREOTYPE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLUMNCOLLAPSEDNODES">
<h3>COLUMNCOLLAPSEDNODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLUMNCOLLAPSEDNODES</span></div>
<div class="block">Specifies the collapsed nodes of the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNCOLLAPSEDNODES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLUMNCUSTOMORDER">
<h3>COLUMNCUSTOMORDER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLUMNCUSTOMORDER</span></div>
<div class="block">Contains Dependency Matrix column elements custom sorting order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNCUSTOMORDER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLUMNHEADERHEIGHT">
<h3>COLUMNHEADERHEIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLUMNHEADERHEIGHT</span></div>
<div class="block">Specifies the height of the column header in pixels.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNHEADERHEIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLUMNOWNERDISPLAYMODE">
<h3>COLUMNOWNERDISPLAYMODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLUMNOWNERDISPLAYMODE</span></div>
<div class="block">Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNOWNERDISPLAYMODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLUMNSORTINGMODE">
<h3>COLUMNSORTINGMODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLUMNSORTINGMODE</span></div>
<div class="block">Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNSORTINGMODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLUMNTEXTDIRECTION">
<h3>COLUMNTEXTDIRECTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLUMNTEXTDIRECTION</span></div>
<div class="block">Specifies the text direction of the Matrix column headers.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.COLUMNTEXTDIRECTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYCRITERIA">
<h3>DEPENDENCYCRITERIA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYCRITERIA</span></div>
<div class="block">Select an expression type and specify the expression to be used as the relation criteria.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.DEPENDENCYCRITERIA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DESCRIPTIONAREA">
<h3>DESCRIPTIONAREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DESCRIPTIONAREA</span></div>
<div class="block">Specify the description of the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.DESCRIPTIONAREA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRECTION">
<h3>DIRECTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRECTION</span></div>
<div class="block">Select Row to column or Column to row to filter the displayed dependencies by direction. Select Both to show all dependencies.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.DIRECTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HIDEDEPENDENCYCRITERIA">
<h3>HIDEDEPENDENCYCRITERIA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HIDEDEPENDENCYCRITERIA</span></div>
<div class="block">Set to false to show the Dependency Criteria filter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.HIDEDEPENDENCYCRITERIA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HIDESCOPE">
<h3>HIDESCOPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HIDESCOPE</span></div>
<div class="block">Set to false to show the scope filter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.HIDESCOPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HIDETYPES">
<h3>HIDETYPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HIDETYPES</span></div>
<div class="block">Set to false to show the types filter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.HIDETYPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEGENDLOCATION">
<h3>LEGENDLOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEGENDLOCATION</span></div>
<div class="block">Legend explains the meaning of colors and styles of links in the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.LEGENDLOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="READONLY">
<h3>READONLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">READONLY</span></div>
<div class="block">Set to true to treat Dependency Matrix cells as non editable.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.READONLY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROWCOLLAPSEDNODES">
<h3>ROWCOLLAPSEDNODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROWCOLLAPSEDNODES</span></div>
<div class="block">Specifies the collapsed nodes of the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWCOLLAPSEDNODES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROWCUSTOMORDER">
<h3>ROWCUSTOMORDER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROWCUSTOMORDER</span></div>
<div class="block">Contains Dependency Matrix row elements custom sorting order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWCUSTOMORDER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROWHEADERWIDTH">
<h3>ROWHEADERWIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROWHEADERWIDTH</span></div>
<div class="block">Specifies the width of the row header in pixels.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWHEADERWIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROWOWNERDISPLAYMODE">
<h3>ROWOWNERDISPLAYMODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROWOWNERDISPLAYMODE</span></div>
<div class="block">Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWOWNERDISPLAYMODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROWSORTINGMODE">
<h3>ROWSORTINGMODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROWSORTINGMODE</span></div>
<div class="block">Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.ROWSORTINGMODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWELEMENTS">
<h3>SHOWELEMENTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWELEMENTS</span></div>
<div class="block">Select All to show all elements from the selected scope. Select With relations to show the elements that have dependency criteria. Select Without relations to show the elements that have no dependency criteria.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.SHOWELEMENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWINNERDEPENDENCIES">
<h3>SHOWINNERDEPENDENCIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWINNERDEPENDENCIES</span></div>
<div class="block">Set to true to show the number of dependencies in the owner element on cell.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.SHOWINNERDEPENDENCIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUPPRESSCRITERIAAREA">
<h3>SUPPRESSCRITERIAAREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SUPPRESSCRITERIAAREA</span></div>
<div class="block">Set to false to show the Criteria area.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.SUPPRESSCRITERIAAREA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TAKEWHOLEMODELASSCOPE">
<h3>TAKEWHOLEMODELASSCOPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TAKEWHOLEMODELASSCOPE</span></div>
<div class="block">Set to true to take whole model as default scope.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DependencyMatrixStereotype.TAKEWHOLEMODELASSCOPE">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile)">
<h3>DependencyMatrixStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">DependencyMatrixStereotype</span><wbr/><span class="parameters">(<a href="DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a> profile)</span></div>
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
<section class="detail" id="getStereotype()">
<h3>getStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Returns stereotype for this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">getStereotype</a></code> in class <code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnCollapsedNodesProperty()">
<h3>getColumnCollapsedNodesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getColumnCollapsedNodesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getColumnCustomOrderProperty()">
<h3>getColumnCustomOrderProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getColumnCustomOrderProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getColumnHeaderHeightProperty()">
<h3>getColumnHeaderHeightProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getColumnHeaderHeightProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getColumnOwnerDisplayModeProperty()">
<h3>getColumnOwnerDisplayModeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getColumnOwnerDisplayModeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getColumnSortingModeProperty()">
<h3>getColumnSortingModeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getColumnSortingModeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getColumnTextDirectionProperty()">
<h3>getColumnTextDirectionProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getColumnTextDirectionProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDependencyCriteriaProperty()">
<h3>getDependencyCriteriaProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getDependencyCriteriaProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDescriptionAreaProperty()">
<h3>getDescriptionAreaProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getDescriptionAreaProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDirectionProperty()">
<h3>getDirectionProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getDirectionProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHideDependencyCriteriaProperty()">
<h3>getHideDependencyCriteriaProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getHideDependencyCriteriaProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHideScopeProperty()">
<h3>getHideScopeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getHideScopeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHideTypesProperty()">
<h3>getHideTypesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getHideTypesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLegendLocationProperty()">
<h3>getLegendLocationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getLegendLocationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getReadOnlyProperty()">
<h3>getReadOnlyProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getReadOnlyProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRowCollapsedNodesProperty()">
<h3>getRowCollapsedNodesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRowCollapsedNodesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRowCustomOrderProperty()">
<h3>getRowCustomOrderProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRowCustomOrderProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRowHeaderWidthProperty()">
<h3>getRowHeaderWidthProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRowHeaderWidthProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRowOwnerDisplayModeProperty()">
<h3>getRowOwnerDisplayModeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRowOwnerDisplayModeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRowSortingModeProperty()">
<h3>getRowSortingModeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRowSortingModeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowElementsProperty()">
<h3>getShowElementsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowElementsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowInnerDependenciesProperty()">
<h3>getShowInnerDependenciesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowInnerDependenciesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSuppressCriteriaAreaProperty()">
<h3>getSuppressCriteriaAreaProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSuppressCriteriaAreaProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTakeWholeModelAsScopeProperty()">
<h3>getTakeWholeModelAsScopeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTakeWholeModelAsScopeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setColumnCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearColumnCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumnCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addColumnCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addColumnCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeColumnCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeColumnCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumnCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setColumnCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnCustomOrder</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearColumnCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumnCustomOrder</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumnCustomOrder</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getColumnCustomOrder</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setColumnHeaderHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnHeaderHeight</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearColumnHeaderHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumnHeaderHeight</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnHeaderHeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumnHeaderHeight</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getColumnHeaderHeight</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OwnerDisplayModeEnum)">
<h3>setColumnOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearColumnOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumnOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumnOwnerDisplayMode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a></span> <span class="element-name">getColumnOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SortingModeEnum)">
<h3>setColumnSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnSortingMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearColumnSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumnSortingMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumnSortingMode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a></span> <span class="element-name">getColumnSortingMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TextDirectionEnum)">
<h3>setColumnTextDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnTextDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.TextDirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.TextDirectionEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearColumnTextDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumnTextDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnTextDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumnTextDirection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.TextDirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.TextDirectionEnum</a></span> <span class="element-name">getColumnTextDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>addDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>removeDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setDescriptionArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescriptionArea</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearDescriptionArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDescriptionArea</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDescriptionArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDescriptionArea</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescriptionArea</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DirectionEnum)">
<h3>setDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.DirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DirectionEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDirection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.DirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DirectionEnum</a></span> <span class="element-name">getDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setHideDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHideDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearHideDependencyCriteria</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearHideDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isHideDependencyCriteria(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isHideDependencyCriteria</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isHideDependencyCriteria</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setHideScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHideScope</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearHideScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearHideScope</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isHideScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isHideScope</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isHideScope</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setHideTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHideTypes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearHideTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearHideTypes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isHideTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isHideTypes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isHideTypes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LegendLocationEnum)">
<h3>setLegendLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLegendLocation</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.LegendLocationEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.LegendLocationEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearLegendLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearLegendLocation</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLegendLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getLegendLocation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.LegendLocationEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.LegendLocationEnum</a></span> <span class="element-name">getLegendLocation</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReadOnly</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearReadOnly</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isReadOnly</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isReadOnly</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setRowCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRowCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRowCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addRowCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addRowCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeRowCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeRowCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRowCollapsedNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRowCollapsedNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRowCollapsedNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setRowCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowCustomOrder</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRowCustomOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRowCustomOrder</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRowCustomOrder(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRowCustomOrder</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRowCustomOrder</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setRowHeaderWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowHeaderWidth</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRowHeaderWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRowHeaderWidth</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRowHeaderWidth(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRowHeaderWidth</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getRowHeaderWidth</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OwnerDisplayModeEnum)">
<h3>setRowOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRowOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRowOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRowOwnerDisplayMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRowOwnerDisplayMode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a></span> <span class="element-name">getRowOwnerDisplayMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SortingModeEnum)">
<h3>setRowSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowSortingMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRowSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRowSortingMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRowSortingMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRowSortingMode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a></span> <span class="element-name">getRowSortingMode</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RelationOptionEnum)">
<h3>setShowElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowElements</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="DependencyMatrixProfile.RelationOptionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.RelationOptionEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowElements</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getShowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getShowElements</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.RelationOptionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.RelationOptionEnum</a></span> <span class="element-name">getShowElements</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowInnerDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowInnerDependencies</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowInnerDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowInnerDependencies</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowInnerDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowInnerDependencies</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowInnerDependencies</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setSuppressCriteriaArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuppressCriteriaArea</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearSuppressCriteriaArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearSuppressCriteriaArea</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSuppressCriteriaArea(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSuppressCriteriaArea</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isSuppressCriteriaArea</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setTakeWholeModelAsScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTakeWholeModelAsScope</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTakeWholeModelAsScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTakeWholeModelAsScope</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTakeWholeModelAsScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isTakeWholeModelAsScope</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isTakeWholeModelAsScope</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
</section>
</li>
<li>
<section class="detail" id="is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>is</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">is</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
