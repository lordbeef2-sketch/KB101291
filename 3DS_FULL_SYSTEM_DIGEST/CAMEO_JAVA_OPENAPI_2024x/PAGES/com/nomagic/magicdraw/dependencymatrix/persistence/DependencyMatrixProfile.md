# JAVA OPENAPI: DependencyMatrixProfile (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.html`
- source_sha256: `6383300dcd35b07219759275c3cb2d11f6a450c12c0555f569a9f36ad83f4574`
- captured_utc: `2026-07-14T16:51:17.269149+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.persistence](package-summary.html)

## Class DependencyMatrixProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation](../../../profiles/ProfileImplementation.html)
com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile

@OpenApiAllpublic classDependencyMatrixProfile
extends [ProfileImplementation](../../../profiles/ProfileImplementation.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[DependencyMatrixProfile.DependencyMatrixStereotype](DependencyMatrixProfile.DependencyMatrixStereotype.html)`

`static enum`
`[DependencyMatrixProfile.DirectionEnum](DependencyMatrixProfile.DirectionEnum.html)`

`static enum`
`[DependencyMatrixProfile.LegendLocationEnum](DependencyMatrixProfile.LegendLocationEnum.html)`

`static class`
`[DependencyMatrixProfile.MatrixFilterStereotype](DependencyMatrixProfile.MatrixFilterStereotype.html)`

`static enum`
`[DependencyMatrixProfile.OwnerDisplayModeEnum](DependencyMatrixProfile.OwnerDisplayModeEnum.html)`

`static enum`
`[DependencyMatrixProfile.RelationOptionEnum](DependencyMatrixProfile.RelationOptionEnum.html)`

`static enum`
`[DependencyMatrixProfile.SortingModeEnum](DependencyMatrixProfile.SortingModeEnum.html)`

`static enum`
`[DependencyMatrixProfile.TextDirectionEnum](DependencyMatrixProfile.TextDirectionEnum.html)`
Nested classes/interfaces inherited from class com.nomagic.profiles.[ProfileImplementation](../../../profiles/ProfileImplementation.html)
`[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY](#DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.COLUMNCOLLAPSEDNODES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY](#DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.COLUMNCUSTOMORDER
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY](#DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.COLUMNHEADERHEIGHT
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY](#DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.COLUMNOWNERDISPLAYMODE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY](#DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.COLUMNSORTINGMODE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY](#DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.COLUMNTEXTDIRECTION
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY](#DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.DEPENDENCYCRITERIA
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY](#DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.DESCRIPTIONAREA
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_DIRECTION_PROPERTY](#DEPENDENCYMATRIX_DIRECTION_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.DIRECTION
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY](#DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.HIDEDEPENDENCYCRITERIA
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_HIDESCOPE_PROPERTY](#DEPENDENCYMATRIX_HIDESCOPE_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.HIDESCOPE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_HIDETYPES_PROPERTY](#DEPENDENCYMATRIX_HIDETYPES_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.HIDETYPES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY](#DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.LEGENDLOCATION
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_READONLY_PROPERTY](#DEPENDENCYMATRIX_READONLY_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.READONLY
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY](#DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.ROWCOLLAPSEDNODES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY](#DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.ROWCUSTOMORDER
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY](#DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.ROWHEADERWIDTH
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY](#DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.ROWOWNERDISPLAYMODE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY](#DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.ROWSORTINGMODE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY](#DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.SHOWELEMENTS
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY](#DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.SHOWINNERDEPENDENCIES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_STEREOTYPE](#DEPENDENCYMATRIX_STEREOTYPE)`
Deprecated.
use DependencyMatrixStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY](#DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.SUPPRESSCRITERIAAREA
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY](#DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY)`
Deprecated.
use DependencyMatrixStereotype.TAKEWHOLEMODELASSCOPE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIRECTION_BOTH_LITERAL](#DIRECTION_BOTH_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIRECTION_COLUMN_TO_ROW_LITERAL](#DIRECTION_COLUMN_TO_ROW_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIRECTION_DATATYPE](#DIRECTION_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIRECTION_ROW_TO_COLUMN_LITERAL](#DIRECTION_ROW_TO_COLUMN_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL](#LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LEGENDLOCATION_DATATYPE](#LEGENDLOCATION_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL](#LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL](#LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY](#MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.COLUMNELEMENTTYPE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY](#MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.COLUMNPROPERTYFILTER
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_COLUMNQUERY_PROPERTY](#MATRIXFILTER_COLUMNQUERY_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.COLUMNQUERY
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_COLUMNSCOPE_PROPERTY](#MATRIXFILTER_COLUMNSCOPE_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.COLUMNSCOPE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY](#MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.COLUMNSCOPEDEFINED
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY](#MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.INCLUDEADDITIONALCONTENT
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY](#MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFCOLUMNTYPES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY](#MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFROWTYPES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY](#MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.INCLUDESUBTYPESOFCOLUMNTYPES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY](#MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.INCLUDESUBTYPESOFROWTYPES
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY](#MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.REMOVEDCOLUMNELEMENTS
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY](#MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.REMOVEDROWELEMENTS
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_ROWELEMENTTYPE_PROPERTY](#MATRIXFILTER_ROWELEMENTTYPE_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.ROWELEMENTTYPE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY](#MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.ROWPROPERTYFILTER
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_ROWQUERY_PROPERTY](#MATRIXFILTER_ROWQUERY_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.ROWQUERY
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_ROWSCOPE_PROPERTY](#MATRIXFILTER_ROWSCOPE_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.ROWSCOPE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY](#MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY)`
Deprecated.
use MatrixFilterStereotype.ROWSCOPEDEFINED
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MATRIXFILTER_STEREOTYPE](#MATRIXFILTER_STEREOTYPE)`
Deprecated.
use MatrixFilterStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OWNERDISPLAYMODE_COMPACT_TREE_LITERAL](#OWNERDISPLAYMODE_COMPACT_TREE_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL](#OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OWNERDISPLAYMODE_DATATYPE](#OWNERDISPLAYMODE_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL](#OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OWNERDISPLAYMODE_HIDDEN_LITERAL](#OWNERDISPLAYMODE_HIDDEN_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_NAME](#PROFILE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_URI](#PROFILE_URI)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RELATIONOPTION_ALL_LITERAL](#RELATIONOPTION_ALL_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL](#RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RELATIONOPTION_DATATYPE](#RELATIONOPTION_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL](#RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RELATIONOPTION_WITH_RELATIONS_LITERAL](#RELATIONOPTION_WITH_RELATIONS_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RELATIONOPTION_WITHOUT_RELATIONS_LITERAL](#RELATIONOPTION_WITHOUT_RELATIONS_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SORTINGMODE_ASCENDING_LITERAL](#SORTINGMODE_ASCENDING_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SORTINGMODE_CUSTOM_LITERAL](#SORTINGMODE_CUSTOM_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SORTINGMODE_DATATYPE](#SORTINGMODE_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SORTINGMODE_DESCENDING_LITERAL](#SORTINGMODE_DESCENDING_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TEXTDIRECTION_DATATYPE](#TEXTDIRECTION_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TEXTDIRECTION_HORIZONTAL_LITERAL](#TEXTDIRECTION_HORIZONTAL_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TEXTDIRECTION_VERTICAL_LITERAL](#TEXTDIRECTION_VERTICAL_LITERAL)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DependencyMatrixProfile](#%3Cinit%3E(com.nomagic.profiles.ProfileCache))(com.nomagic.profiles.ProfileCache cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[DependencyMatrixProfile.DependencyMatrixStereotype](DependencyMatrixProfile.DependencyMatrixStereotype.html)`
`[dependencyMatrix](#dependencyMatrix())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`

`[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getDependencyMatrix](#getDependencyMatrix())()`
Deprecated.
use getInstance(element).dependencyMatrix().getStereotype()
`[Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getDirection](#getDirection())()`

`static [DependencyMatrixProfile](DependencyMatrixProfile.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) baseElement)`

`static [DependencyMatrixProfile](DependencyMatrixProfile.html)`
`[getInstanceByProject](#getInstanceByProject(com.nomagic.uml2.project.ElementProject))(com.nomagic.uml2.project.ElementProject project)`

`[Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getLegendLocation](#getLegendLocation())()`

`[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getMatrixFilter](#getMatrixFilter())()`
Deprecated.
use getInstance(element).matrixFilter().getStereotype()
`[Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getOwnerDisplayMode](#getOwnerDisplayMode())()`

`[Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getRelationOption](#getRelationOption())()`

`[Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getSortingMode](#getSortingMode())()`

`[Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getTextDirection](#getTextDirection())()`

`static boolean`
`[isDependencyMatrix](#isDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use DependencyMatrixStereotype.isInstance(element)
`static boolean`
`[isMatrixFilter](#isMatrixFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use MatrixFilterStereotype.isInstance(element)
`[DependencyMatrixProfile.MatrixFilterStereotype](DependencyMatrixProfile.MatrixFilterStereotype.html)`
`[matrixFilter](#matrixFilter())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PROFILE_URI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_URI
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.PROFILE_URI)
PROFILE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_NAME
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.PROFILE_NAME)
DIRECTION_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIRECTION_DATATYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_DATATYPE)
LEGENDLOCATION_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEGENDLOCATION_DATATYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_DATATYPE)
OWNERDISPLAYMODE_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OWNERDISPLAYMODE_DATATYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_DATATYPE)
RELATIONOPTION_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RELATIONOPTION_DATATYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_DATATYPE)
SORTINGMODE_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SORTINGMODE_DATATYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_DATATYPE)
TEXTDIRECTION_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TEXTDIRECTION_DATATYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TEXTDIRECTION_DATATYPE)
DIRECTION_BOTH_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIRECTION_BOTH_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_BOTH_LITERAL)
DIRECTION_COLUMN_TO_ROW_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIRECTION_COLUMN_TO_ROW_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_COLUMN_TO_ROW_LITERAL)
DIRECTION_ROW_TO_COLUMN_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIRECTION_ROW_TO_COLUMN_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_ROW_TO_COLUMN_LITERAL)
LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL)
LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL)
LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL)
OWNERDISPLAYMODE_COMPACT_TREE_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OWNERDISPLAYMODE_COMPACT_TREE_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_COMPACT_TREE_LITERAL)
OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL)
OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL)
OWNERDISPLAYMODE_HIDDEN_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OWNERDISPLAYMODE_HIDDEN_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_HIDDEN_LITERAL)
RELATIONOPTION_ALL_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RELATIONOPTION_ALL_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_ALL_LITERAL)
RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL)
RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL)
RELATIONOPTION_WITHOUT_RELATIONS_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RELATIONOPTION_WITHOUT_RELATIONS_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_WITHOUT_RELATIONS_LITERAL)
RELATIONOPTION_WITH_RELATIONS_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RELATIONOPTION_WITH_RELATIONS_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_WITH_RELATIONS_LITERAL)
SORTINGMODE_ASCENDING_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SORTINGMODE_ASCENDING_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_ASCENDING_LITERAL)
SORTINGMODE_CUSTOM_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SORTINGMODE_CUSTOM_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_CUSTOM_LITERAL)
SORTINGMODE_DESCENDING_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SORTINGMODE_DESCENDING_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_DESCENDING_LITERAL)
TEXTDIRECTION_HORIZONTAL_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TEXTDIRECTION_HORIZONTAL_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TEXTDIRECTION_HORIZONTAL_LITERAL)
TEXTDIRECTION_VERTICAL_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TEXTDIRECTION_VERTICAL_LITERAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TEXTDIRECTION_VERTICAL_LITERAL)
DEPENDENCYMATRIX_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_STEREOTYPE
Deprecated.
use DependencyMatrixStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_STEREOTYPE)
DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY
Deprecated.
use DependencyMatrixStereotype.COLUMNCOLLAPSEDNODES
Specifies the collapsed nodes of the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY)
DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY
Deprecated.
use DependencyMatrixStereotype.COLUMNCUSTOMORDER
Contains Dependency Matrix column elements custom sorting order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY)
DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY
Deprecated.
use DependencyMatrixStereotype.COLUMNHEADERHEIGHT
Specifies the height of the column header in pixels.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY)
DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY
Deprecated.
use DependencyMatrixStereotype.COLUMNOWNERDISPLAYMODE
Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY)
DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY
Deprecated.
use DependencyMatrixStereotype.COLUMNSORTINGMODE
Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY)
DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY
Deprecated.
use DependencyMatrixStereotype.COLUMNTEXTDIRECTION
Specifies the text direction of the Matrix column headers.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY)
DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY
Deprecated.
use DependencyMatrixStereotype.DEPENDENCYCRITERIA
Select an expression type and specify the expression to be used as the relation criteria.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY)
DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY
Deprecated.
use DependencyMatrixStereotype.DESCRIPTIONAREA
Specify the description of the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY)
DEPENDENCYMATRIX_DIRECTION_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_DIRECTION_PROPERTY
Deprecated.
use DependencyMatrixStereotype.DIRECTION
Select Row to column or Column to row to filter the displayed dependencies by direction. Select Both to show all dependencies.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_DIRECTION_PROPERTY)
DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY
Deprecated.
use DependencyMatrixStereotype.HIDEDEPENDENCYCRITERIA
Set to false to show the Dependency Criteria filter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY)
DEPENDENCYMATRIX_HIDESCOPE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_HIDESCOPE_PROPERTY
Deprecated.
use DependencyMatrixStereotype.HIDESCOPE
Set to false to show the scope filter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_HIDESCOPE_PROPERTY)
DEPENDENCYMATRIX_HIDETYPES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_HIDETYPES_PROPERTY
Deprecated.
use DependencyMatrixStereotype.HIDETYPES
Set to false to show the types filter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_HIDETYPES_PROPERTY)
DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY
Deprecated.
use DependencyMatrixStereotype.LEGENDLOCATION
Legend explains the meaning of colors and styles of links in the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY)
DEPENDENCYMATRIX_READONLY_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_READONLY_PROPERTY
Deprecated.
use DependencyMatrixStereotype.READONLY
Set to true to treat Dependency Matrix cells as non editable.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_READONLY_PROPERTY)
DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY
Deprecated.
use DependencyMatrixStereotype.ROWCOLLAPSEDNODES
Specifies the collapsed nodes of the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY)
DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY
Deprecated.
use DependencyMatrixStereotype.ROWCUSTOMORDER
Contains Dependency Matrix row elements custom sorting order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY)
DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY
Deprecated.
use DependencyMatrixStereotype.ROWHEADERWIDTH
Specifies the width of the row header in pixels.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY)
DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY
Deprecated.
use DependencyMatrixStereotype.ROWOWNERDISPLAYMODE
Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY)
DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY
Deprecated.
use DependencyMatrixStereotype.ROWSORTINGMODE
Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY)
DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY
Deprecated.
use DependencyMatrixStereotype.SHOWELEMENTS
Select All to show all elements from the selected scope. Select With relations to show the elements that have dependency criteria. Select Without relations to show the elements that have no dependency criteria.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY)
DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY
Deprecated.
use DependencyMatrixStereotype.SHOWINNERDEPENDENCIES
Set to true to show the number of dependencies in the owner element on cell.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY)
DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY
Deprecated.
use DependencyMatrixStereotype.SUPPRESSCRITERIAAREA
Set to false to show the Criteria area.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY)
DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY
Deprecated.
use DependencyMatrixStereotype.TAKEWHOLEMODELASSCOPE
Set to true to take whole model as default scope.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY)
MATRIXFILTER_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_STEREOTYPE
Deprecated.
use MatrixFilterStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_STEREOTYPE)
MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY
Deprecated.
use MatrixFilterStereotype.COLUMNELEMENTTYPE
Select the type of the elements to be used to build the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY)
MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY
Deprecated.
use MatrixFilterStereotype.COLUMNPROPERTYFILTER
Select properties and values to filter elements included in the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY)
MATRIXFILTER_COLUMNQUERY_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_COLUMNQUERY_PROPERTY
Deprecated.
use MatrixFilterStereotype.COLUMNQUERY
Specify the expression to collect column elements.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNQUERY_PROPERTY)
MATRIXFILTER_COLUMNSCOPE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_COLUMNSCOPE_PROPERTY
Deprecated.
use MatrixFilterStereotype.COLUMNSCOPE
Select the scope of the model to be used to build the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNSCOPE_PROPERTY)
MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY
Deprecated.
use MatrixFilterStereotype.COLUMNSCOPEDEFINED
Set to true to take empty scope as whole model.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY)
MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY
Deprecated.
use MatrixFilterStereotype.INCLUDEADDITIONALCONTENT
Select to include additional content of elements (e.g., Smart Package) that fall within the specified row/column scope.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY)
MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY
Deprecated.
use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFCOLUMNTYPES
Select to include the custom types that extend the specified column element types. For example, if you specify a Package as a column element type, the custom types, such as a Smart Package, extending the Package will also be included.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY)
MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY
Deprecated.
use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFROWTYPES
Select to include the custom types that extend the specified row element types. For example, if you specify a Package as a row element type, the custom types, such as a Smart Package, extending the Package will also be included.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY)
MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY
Deprecated.
use MatrixFilterStereotype.INCLUDESUBTYPESOFCOLUMNTYPES
Select to include the subtypes of the specified column element types. For example, if you specify a Package as a column element type, its subtypes, such as a Model and Profile, will also be included.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY)
MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY
Deprecated.
use MatrixFilterStereotype.INCLUDESUBTYPESOFROWTYPES
Select to include the subtypes of the specified row element types. For example, if you specify a Package as a row element type, its subtypes, such as a Model and Profile, will also be included.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY)
MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY
Deprecated.
use MatrixFilterStereotype.REMOVEDCOLUMNELEMENTS
Select elements to exclude from the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY)
MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY
Deprecated.
use MatrixFilterStereotype.REMOVEDROWELEMENTS
Select elements to exclude from the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY)
MATRIXFILTER_ROWELEMENTTYPE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_ROWELEMENTTYPE_PROPERTY
Deprecated.
use MatrixFilterStereotype.ROWELEMENTTYPE
Select the type of the elements to be used to build the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWELEMENTTYPE_PROPERTY)
MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY
Deprecated.
use MatrixFilterStereotype.ROWPROPERTYFILTER
Select properties and values to filter elements included in the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY)
MATRIXFILTER_ROWQUERY_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_ROWQUERY_PROPERTY
Deprecated.
use MatrixFilterStereotype.ROWQUERY
Specify the expression to collect row elements.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWQUERY_PROPERTY)
MATRIXFILTER_ROWSCOPE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_ROWSCOPE_PROPERTY
Deprecated.
use MatrixFilterStereotype.ROWSCOPE
Select the scope of the model to be used to build the Dependency Matrix.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWSCOPE_PROPERTY)
MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY
Deprecated.
use MatrixFilterStereotype.ROWSCOPEDEFINED
Set to true to take empty scope as whole model.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DependencyMatrixProfile
public DependencyMatrixProfile(com.nomagic.profiles.ProfileCache cache)
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [DependencyMatrixProfile](DependencyMatrixProfile.html) getInstance([BaseElement](../../uml/BaseElement.html) baseElement)
getInstanceByProject
public static [DependencyMatrixProfile](DependencyMatrixProfile.html) getInstanceByProject(com.nomagic.uml2.project.ElementProject project)
dependencyMatrix
public [DependencyMatrixProfile.DependencyMatrixStereotype](DependencyMatrixProfile.DependencyMatrixStereotype.html) dependencyMatrix()
matrixFilter
public [DependencyMatrixProfile.MatrixFilterStereotype](DependencyMatrixProfile.MatrixFilterStereotype.html) matrixFilter()
getDirection
public [Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getDirection()
getLegendLocation
public [Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getLegendLocation()
getOwnerDisplayMode
public [Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getOwnerDisplayMode()
getRelationOption
public [Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getRelationOption()
getSortingMode
public [Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getSortingMode()
getTextDirection
public [Enumeration](../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getTextDirection()
getDependencyMatrix
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getDependencyMatrix()
Deprecated.
use getInstance(element).dependencyMatrix().getStereotype()
isDependencyMatrix
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isDependencyMatrix(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use DependencyMatrixStereotype.isInstance(element)
getMatrixFilter
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getMatrixFilter()
Deprecated.
use getInstance(element).matrixFilter().getStereotype()
isMatrixFilter
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isMatrixFilter(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use MatrixFilterStereotype.isInstance(element)
generatedGetAllElementWrappers
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper> generatedGetAllElementWrappers()
generatedGetAllStereotypes
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.persistence</a></div>
<h1 class="title" title="Class DependencyMatrixProfile">Class DependencyMatrixProfile</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DependencyMatrixProfile</span>
<span class="extends-implements">extends <a href="../../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></span></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.DependencyMatrixStereotype.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DependencyMatrixStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.DirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DirectionEnum</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.LegendLocationEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.LegendLocationEnum</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.MatrixFilterStereotype.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.MatrixFilterStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.OwnerDisplayModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.OwnerDisplayModeEnum</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.RelationOptionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.RelationOptionEnum</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.SortingModeEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.SortingModeEnum</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DependencyMatrixProfile.TextDirectionEnum.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.TextDirectionEnum</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Nested classes/interfaces inherited from class com.nomagic.profiles.<a href="../../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h2>
<code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY">DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNCOLLAPSEDNODES</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY">DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNCUSTOMORDER</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY">DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNHEADERHEIGHT</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY">DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNOWNERDISPLAYMODE</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY">DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNSORTINGMODE</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY">DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNTEXTDIRECTION</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY">DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.DEPENDENCYCRITERIA</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY">DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.DESCRIPTIONAREA</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_DIRECTION_PROPERTY">DEPENDENCYMATRIX_DIRECTION_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.DIRECTION</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY">DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.HIDEDEPENDENCYCRITERIA</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_HIDESCOPE_PROPERTY">DEPENDENCYMATRIX_HIDESCOPE_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.HIDESCOPE</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_HIDETYPES_PROPERTY">DEPENDENCYMATRIX_HIDETYPES_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.HIDETYPES</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY">DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.LEGENDLOCATION</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_READONLY_PROPERTY">DEPENDENCYMATRIX_READONLY_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.READONLY</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY">DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWCOLLAPSEDNODES</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY">DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWCUSTOMORDER</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY">DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWHEADERWIDTH</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY">DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWOWNERDISPLAYMODE</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY">DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWSORTINGMODE</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY">DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.SHOWELEMENTS</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY">DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.SHOWINNERDEPENDENCIES</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_STEREOTYPE">DEPENDENCYMATRIX_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY">DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.SUPPRESSCRITERIAAREA</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY">DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.TAKEWHOLEMODELASSCOPE</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIRECTION_BOTH_LITERAL">DIRECTION_BOTH_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIRECTION_COLUMN_TO_ROW_LITERAL">DIRECTION_COLUMN_TO_ROW_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIRECTION_DATATYPE">DIRECTION_DATATYPE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIRECTION_ROW_TO_COLUMN_LITERAL">DIRECTION_ROW_TO_COLUMN_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL">LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LEGENDLOCATION_DATATYPE">LEGENDLOCATION_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL">LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL">LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY">MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNELEMENTTYPE</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY">MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNPROPERTYFILTER</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_COLUMNQUERY_PROPERTY">MATRIXFILTER_COLUMNQUERY_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNQUERY</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_COLUMNSCOPE_PROPERTY">MATRIXFILTER_COLUMNSCOPE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNSCOPE</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY">MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNSCOPEDEFINED</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY">MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDEADDITIONALCONTENT</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY">MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFCOLUMNTYPES</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY">MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFROWTYPES</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY">MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDESUBTYPESOFCOLUMNTYPES</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY">MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDESUBTYPESOFROWTYPES</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY">MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.REMOVEDCOLUMNELEMENTS</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY">MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.REMOVEDROWELEMENTS</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_ROWELEMENTTYPE_PROPERTY">MATRIXFILTER_ROWELEMENTTYPE_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWELEMENTTYPE</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY">MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWPROPERTYFILTER</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_ROWQUERY_PROPERTY">MATRIXFILTER_ROWQUERY_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWQUERY</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_ROWSCOPE_PROPERTY">MATRIXFILTER_ROWSCOPE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWSCOPE</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY">MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWSCOPEDEFINED</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MATRIXFILTER_STEREOTYPE">MATRIXFILTER_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OWNERDISPLAYMODE_COMPACT_TREE_LITERAL">OWNERDISPLAYMODE_COMPACT_TREE_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL">OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OWNERDISPLAYMODE_DATATYPE">OWNERDISPLAYMODE_DATATYPE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL">OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OWNERDISPLAYMODE_HIDDEN_LITERAL">OWNERDISPLAYMODE_HIDDEN_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROFILE_NAME">PROFILE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROFILE_URI">PROFILE_URI</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RELATIONOPTION_ALL_LITERAL">RELATIONOPTION_ALL_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL">RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RELATIONOPTION_DATATYPE">RELATIONOPTION_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL">RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RELATIONOPTION_WITH_RELATIONS_LITERAL">RELATIONOPTION_WITH_RELATIONS_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RELATIONOPTION_WITHOUT_RELATIONS_LITERAL">RELATIONOPTION_WITHOUT_RELATIONS_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SORTINGMODE_ASCENDING_LITERAL">SORTINGMODE_ASCENDING_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SORTINGMODE_CUSTOM_LITERAL">SORTINGMODE_CUSTOM_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SORTINGMODE_DATATYPE">SORTINGMODE_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SORTINGMODE_DESCENDING_LITERAL">SORTINGMODE_DESCENDING_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEXTDIRECTION_DATATYPE">TEXTDIRECTION_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEXTDIRECTION_HORIZONTAL_LITERAL">TEXTDIRECTION_HORIZONTAL_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEXTDIRECTION_VERTICAL_LITERAL">TEXTDIRECTION_VERTICAL_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.profiles.ProfileCache)">DependencyMatrixProfile</a><wbr/>(com.nomagic.profiles.ProfileCache cache)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.DependencyMatrixStereotype.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DependencyMatrixStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dependencyMatrix()">dependencyMatrix</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDependencyMatrix()">getDependencyMatrix</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).dependencyMatrix().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirection()">getDirection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.nomagic.uml2.project.ElementProject)">getInstanceByProject</a><wbr/>(com.nomagic.uml2.project.ElementProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLegendLocation()">getLegendLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getMatrixFilter()">getMatrixFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).matrixFilter().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnerDisplayMode()">getOwnerDisplayMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationOption()">getRelationOption</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortingMode()">getSortingMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTextDirection()">getTextDirection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isDependencyMatrix</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isMatrixFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isMatrixFilter</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DependencyMatrixProfile.MatrixFilterStereotype.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.MatrixFilterStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#matrixFilter()">matrixFilter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="PROFILE_URI">
<h3>PROFILE_URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_URI</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.PROFILE_URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROFILE_NAME">
<h3>PROFILE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.PROFILE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRECTION_DATATYPE">
<h3>DIRECTION_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRECTION_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEGENDLOCATION_DATATYPE">
<h3>LEGENDLOCATION_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEGENDLOCATION_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OWNERDISPLAYMODE_DATATYPE">
<h3>OWNERDISPLAYMODE_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OWNERDISPLAYMODE_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONOPTION_DATATYPE">
<h3>RELATIONOPTION_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RELATIONOPTION_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SORTINGMODE_DATATYPE">
<h3>SORTINGMODE_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SORTINGMODE_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEXTDIRECTION_DATATYPE">
<h3>TEXTDIRECTION_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEXTDIRECTION_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TEXTDIRECTION_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRECTION_BOTH_LITERAL">
<h3>DIRECTION_BOTH_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRECTION_BOTH_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_BOTH_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRECTION_COLUMN_TO_ROW_LITERAL">
<h3>DIRECTION_COLUMN_TO_ROW_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRECTION_COLUMN_TO_ROW_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_COLUMN_TO_ROW_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRECTION_ROW_TO_COLUMN_LITERAL">
<h3>DIRECTION_ROW_TO_COLUMN_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRECTION_ROW_TO_COLUMN_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DIRECTION_ROW_TO_COLUMN_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL">
<h3>LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_ABOVE_COLUMN_HEADER_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL">
<h3>LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_DO_NOT_DISPLAY_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL">
<h3>LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.LEGENDLOCATION_TOP_LEFT_CORNER_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OWNERDISPLAYMODE_COMPACT_TREE_LITERAL">
<h3>OWNERDISPLAYMODE_COMPACT_TREE_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OWNERDISPLAYMODE_COMPACT_TREE_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_COMPACT_TREE_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL">
<h3>OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_COMPLETE_TREE_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL">
<h3>OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_FULL_QUALIFIED_NAME_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OWNERDISPLAYMODE_HIDDEN_LITERAL">
<h3>OWNERDISPLAYMODE_HIDDEN_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OWNERDISPLAYMODE_HIDDEN_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.OWNERDISPLAYMODE_HIDDEN_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONOPTION_ALL_LITERAL">
<h3>RELATIONOPTION_ALL_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RELATIONOPTION_ALL_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_ALL_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL">
<h3>RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_COLUMNS_WITHOUT_RELATIONS_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL">
<h3>RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_ROWS_WITHOUT_RELATIONS_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONOPTION_WITHOUT_RELATIONS_LITERAL">
<h3>RELATIONOPTION_WITHOUT_RELATIONS_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RELATIONOPTION_WITHOUT_RELATIONS_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_WITHOUT_RELATIONS_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONOPTION_WITH_RELATIONS_LITERAL">
<h3>RELATIONOPTION_WITH_RELATIONS_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RELATIONOPTION_WITH_RELATIONS_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.RELATIONOPTION_WITH_RELATIONS_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SORTINGMODE_ASCENDING_LITERAL">
<h3>SORTINGMODE_ASCENDING_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SORTINGMODE_ASCENDING_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_ASCENDING_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SORTINGMODE_CUSTOM_LITERAL">
<h3>SORTINGMODE_CUSTOM_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SORTINGMODE_CUSTOM_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_CUSTOM_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SORTINGMODE_DESCENDING_LITERAL">
<h3>SORTINGMODE_DESCENDING_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SORTINGMODE_DESCENDING_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.SORTINGMODE_DESCENDING_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEXTDIRECTION_HORIZONTAL_LITERAL">
<h3>TEXTDIRECTION_HORIZONTAL_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEXTDIRECTION_HORIZONTAL_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TEXTDIRECTION_HORIZONTAL_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEXTDIRECTION_VERTICAL_LITERAL">
<h3>TEXTDIRECTION_VERTICAL_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEXTDIRECTION_VERTICAL_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.TEXTDIRECTION_VERTICAL_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_STEREOTYPE">
<h3>DEPENDENCYMATRIX_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY">
<h3>DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNCOLLAPSEDNODES</div>
</div>
<div class="block">Specifies the collapsed nodes of the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNCOLLAPSEDNODES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY">
<h3>DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNCUSTOMORDER</div>
</div>
<div class="block">Contains Dependency Matrix column elements custom sorting order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNCUSTOMORDER_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY">
<h3>DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNHEADERHEIGHT</div>
</div>
<div class="block">Specifies the height of the column header in pixels.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNHEADERHEIGHT_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY">
<h3>DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNOWNERDISPLAYMODE</div>
</div>
<div class="block">Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNOWNERDISPLAYMODE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY">
<h3>DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNSORTINGMODE</div>
</div>
<div class="block">Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNSORTINGMODE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY">
<h3>DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.COLUMNTEXTDIRECTION</div>
</div>
<div class="block">Specifies the text direction of the Matrix column headers.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_COLUMNTEXTDIRECTION_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY">
<h3>DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.DEPENDENCYCRITERIA</div>
</div>
<div class="block">Select an expression type and specify the expression to be used as the relation criteria.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_DEPENDENCYCRITERIA_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY">
<h3>DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.DESCRIPTIONAREA</div>
</div>
<div class="block">Specify the description of the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_DESCRIPTIONAREA_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_DIRECTION_PROPERTY">
<h3>DEPENDENCYMATRIX_DIRECTION_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_DIRECTION_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.DIRECTION</div>
</div>
<div class="block">Select Row to column or Column to row to filter the displayed dependencies by direction. Select Both to show all dependencies.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_DIRECTION_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY">
<h3>DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.HIDEDEPENDENCYCRITERIA</div>
</div>
<div class="block">Set to false to show the Dependency Criteria filter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_HIDEDEPENDENCYCRITERIA_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_HIDESCOPE_PROPERTY">
<h3>DEPENDENCYMATRIX_HIDESCOPE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_HIDESCOPE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.HIDESCOPE</div>
</div>
<div class="block">Set to false to show the scope filter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_HIDESCOPE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_HIDETYPES_PROPERTY">
<h3>DEPENDENCYMATRIX_HIDETYPES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_HIDETYPES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.HIDETYPES</div>
</div>
<div class="block">Set to false to show the types filter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_HIDETYPES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY">
<h3>DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.LEGENDLOCATION</div>
</div>
<div class="block">Legend explains the meaning of colors and styles of links in the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_LEGENDLOCATION_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_READONLY_PROPERTY">
<h3>DEPENDENCYMATRIX_READONLY_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_READONLY_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.READONLY</div>
</div>
<div class="block">Set to true to treat Dependency Matrix cells as non editable.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_READONLY_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY">
<h3>DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWCOLLAPSEDNODES</div>
</div>
<div class="block">Specifies the collapsed nodes of the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWCOLLAPSEDNODES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY">
<h3>DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWCUSTOMORDER</div>
</div>
<div class="block">Contains Dependency Matrix row elements custom sorting order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWCUSTOMORDER_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY">
<h3>DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWHEADERWIDTH</div>
</div>
<div class="block">Specifies the width of the row header in pixels.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWHEADERWIDTH_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY">
<h3>DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWOWNERDISPLAYMODE</div>
</div>
<div class="block">Select Compact tree mode to show only direct and common element owners in the nested mode. Select Complete tree to show all owners in the nested mode. Select Hidden or Full qualified name to shown a regular elements list.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWOWNERDISPLAYMODE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY">
<h3>DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.ROWSORTINGMODE</div>
</div>
<div class="block">Select Ascending or Descending to sort elements alphabetically. Select Custom sorting mode to use your own order.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_ROWSORTINGMODE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY">
<h3>DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.SHOWELEMENTS</div>
</div>
<div class="block">Select All to show all elements from the selected scope. Select With relations to show the elements that have dependency criteria. Select Without relations to show the elements that have no dependency criteria.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_SHOWELEMENTS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY">
<h3>DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.SHOWINNERDEPENDENCIES</div>
</div>
<div class="block">Set to true to show the number of dependencies in the owner element on cell.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_SHOWINNERDEPENDENCIES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY">
<h3>DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.SUPPRESSCRITERIAAREA</div>
</div>
<div class="block">Set to false to show the Criteria area.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_SUPPRESSCRITERIAAREA_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY">
<h3>DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.TAKEWHOLEMODELASSCOPE</div>
</div>
<div class="block">Set to true to take whole model as default scope.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.DEPENDENCYMATRIX_TAKEWHOLEMODELASSCOPE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_STEREOTYPE">
<h3>MATRIXFILTER_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY">
<h3>MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNELEMENTTYPE</div>
</div>
<div class="block">Select the type of the elements to be used to build the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNELEMENTTYPE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY">
<h3>MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNPROPERTYFILTER</div>
</div>
<div class="block">Select properties and values to filter elements included in the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNPROPERTYFILTER_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_COLUMNQUERY_PROPERTY">
<h3>MATRIXFILTER_COLUMNQUERY_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_COLUMNQUERY_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNQUERY</div>
</div>
<div class="block">Specify the expression to collect column elements.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNQUERY_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_COLUMNSCOPE_PROPERTY">
<h3>MATRIXFILTER_COLUMNSCOPE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_COLUMNSCOPE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNSCOPE</div>
</div>
<div class="block">Select the scope of the model to be used to build the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNSCOPE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY">
<h3>MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.COLUMNSCOPEDEFINED</div>
</div>
<div class="block">Set to true to take empty scope as whole model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_COLUMNSCOPEDEFINED_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY">
<h3>MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDEADDITIONALCONTENT</div>
</div>
<div class="block">Select to include additional content of elements (e.g., Smart Package) that fall within the specified row/column scope.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDEADDITIONALCONTENT_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY">
<h3>MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFCOLUMNTYPES</div>
</div>
<div class="block">Select to include the custom types that extend the specified column element types. For example, if you specify a Package as a column element type, the custom types, such as a Smart Package, extending the Package will also be included.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDECUSTOMTYPESOFCOLUMNTYPES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY">
<h3>MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDECUSTOMTYPESOFROWTYPES</div>
</div>
<div class="block">Select to include the custom types that extend the specified row element types. For example, if you specify a Package as a row element type, the custom types, such as a Smart Package, extending the Package will also be included.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDECUSTOMTYPESOFROWTYPES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY">
<h3>MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDESUBTYPESOFCOLUMNTYPES</div>
</div>
<div class="block">Select to include the subtypes of the specified column element types. For example, if you specify a Package as a column element type, its subtypes, such as a Model and Profile, will also be included.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDESUBTYPESOFCOLUMNTYPES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY">
<h3>MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.INCLUDESUBTYPESOFROWTYPES</div>
</div>
<div class="block">Select to include the subtypes of the specified row element types. For example, if you specify a Package as a row element type, its subtypes, such as a Model and Profile, will also be included.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_INCLUDESUBTYPESOFROWTYPES_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY">
<h3>MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.REMOVEDCOLUMNELEMENTS</div>
</div>
<div class="block">Select elements to exclude from the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_REMOVEDCOLUMNELEMENTS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY">
<h3>MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.REMOVEDROWELEMENTS</div>
</div>
<div class="block">Select elements to exclude from the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_REMOVEDROWELEMENTS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_ROWELEMENTTYPE_PROPERTY">
<h3>MATRIXFILTER_ROWELEMENTTYPE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_ROWELEMENTTYPE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWELEMENTTYPE</div>
</div>
<div class="block">Select the type of the elements to be used to build the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWELEMENTTYPE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY">
<h3>MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWPROPERTYFILTER</div>
</div>
<div class="block">Select properties and values to filter elements included in the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWPROPERTYFILTER_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_ROWQUERY_PROPERTY">
<h3>MATRIXFILTER_ROWQUERY_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_ROWQUERY_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWQUERY</div>
</div>
<div class="block">Specify the expression to collect row elements.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWQUERY_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_ROWSCOPE_PROPERTY">
<h3>MATRIXFILTER_ROWSCOPE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_ROWSCOPE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWSCOPE</div>
</div>
<div class="block">Select the scope of the model to be used to build the Dependency Matrix.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWSCOPE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY">
<h3>MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.ROWSCOPEDEFINED</div>
</div>
<div class="block">Set to true to take empty scope as whole model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.persistence.DependencyMatrixProfile.MATRIXFILTER_ROWSCOPEDEFINED_PROPERTY">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.profiles.ProfileCache)">
<h3>DependencyMatrixProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DependencyMatrixProfile</span><wbr/><span class="parameters">(com.nomagic.profiles.ProfileCache cache)</span></div>
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
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstanceByProject(com.nomagic.uml2.project.ElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(com.nomagic.uml2.project.ElementProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="dependencyMatrix()">
<h3>dependencyMatrix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.DependencyMatrixStereotype.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.DependencyMatrixStereotype</a></span> <span class="element-name">dependencyMatrix</span>()</div>
</section>
</li>
<li>
<section class="detail" id="matrixFilter()">
<h3>matrixFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DependencyMatrixProfile.MatrixFilterStereotype.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile.MatrixFilterStereotype</a></span> <span class="element-name">matrixFilter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDirection()">
<h3>getDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getDirection</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLegendLocation()">
<h3>getLegendLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getLegendLocation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOwnerDisplayMode()">
<h3>getOwnerDisplayMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getOwnerDisplayMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRelationOption()">
<h3>getRelationOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getRelationOption</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSortingMode()">
<h3>getSortingMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getSortingMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTextDirection()">
<h3>getTextDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getTextDirection</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDependencyMatrix()">
<h3>getDependencyMatrix</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getDependencyMatrix</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).dependencyMatrix().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isDependencyMatrix</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDependencyMatrix</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DependencyMatrixStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getMatrixFilter()">
<h3>getMatrixFilter</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getMatrixFilter</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).matrixFilter().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isMatrixFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isMatrixFilter</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMatrixFilter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use MatrixFilterStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
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
