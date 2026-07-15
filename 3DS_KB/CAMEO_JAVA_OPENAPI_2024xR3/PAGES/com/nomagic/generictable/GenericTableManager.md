# JAVA OPENAPI: GenericTableManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/generictable/GenericTableManager.html
- source_path: `com/nomagic/generictable/GenericTableManager.html`
- source_sha256: `bfe8f15d35188a50b095fdf083195e948e3a31a3a7263063f5ead5e35104cede`
- captured_utc: `2026-07-14T16:55:02.640867+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.generictable](package-summary.html)

## Class GenericTableManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.generictable.GenericTableManager

@OpenApiAllpublic classGenericTableManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Helps manage a generic table:
 create a new table,
 add, get and remove rows,
 add and get columns,
 get column values,
 get currently selected elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[GenericTableManager](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addColumnsById](#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> columnIDs)`
Adds generic table columns by id
`static void`
`[addGenericTableContextConfigurator](#addGenericTableContextConfigurator(com.nomagic.diagramtable.DTContextConfigurator))(com.nomagic.diagramtable.DTContextConfigurator configurator)`
Adds generic table context configurator.
`static void`
`[addGenericTableContextConfigurator](#addGenericTableContextConfigurator(java.lang.String,com.nomagic.diagramtable.DTContextConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tableType,
 com.nomagic.diagramtable.DTContextConfigurator configurator)`
Adds generic table context configurator.
`static void`
`[addGenericTableToolbarConfigurator](#addGenericTableToolbarConfigurator(com.nomagic.diagramtable.DTConfigurator))([DTConfigurator](../diagramtable/DTConfigurator.html) configurator)`
Adds generic table toolbar configurator.
`static void`
`[addGenericTableToolbarConfigurator](#addGenericTableToolbarConfigurator(java.lang.String,com.nomagic.diagramtable.DTConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tableType,
 [DTConfigurator](../diagramtable/DTConfigurator.html) configurator)`
Adds generic table toolbar configurator.
`static void`
`[addRowElement](#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Adds an element into generic table diagram as row
`static void`
`[collapseRows](#collapseRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)`
Collapses the given rows in table
`static void`
`[collapseRowsRecursively](#collapseRowsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)`
Collapses the rows of given elements and their recursive children in table
`static [Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[createGenericTable](#createGenericTable(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) genericTableDiagramName)`
Creates generic table diagram in given project with given name
`static void`
`[expandRows](#expandRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)`
Expands the given rows in table
`static void`
`[expandRowsIncludingParentsRecursively](#expandRowsIncludingParentsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)`
Expands the rows of given elements and their recursive parents in table
`static void`
`[expandRowsRecursively](#expandRowsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)`
Expands the rows of given elements and their recursive children in table
`static [Property](../magicdraw/properties/Property.html)`
`[getCellValue](#getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) columnId)`
Returns cell value by row element and column id.
`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Property](../magicdraw/properties/Property.html)>>`
`[getCellValues](#getCellValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Returns all cell values by row element and column id.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getCollapsedVisibleRowsElements](#getCollapsedVisibleRowsElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Gets the elements representing visible rows that are collapsed in the table
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getColumnIDByPropertyName](#getColumnIDByPropertyName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Creates Column ID for table from property name
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getColumnIDByTag](#getColumnIDByTag(java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Creates Column ID for table from stereotype tag name
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getColumnIds](#getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Returns column ids from a generic table diagram
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getColumnNameById](#getColumnNameById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.lang.String))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) columnId)`
Returns column name by id from a generic table diagram
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getColumnNames](#getColumnNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Returns column names from a generic table diagram
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getExpandedVisibleRowsElements](#getExpandedVisibleRowsElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Gets the elements representing visible rows that are expanded in the table
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getPossibleColumnIDs](#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) type)`
Returns all possible column ids for a generic table element types
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRowElements](#getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Returns row elements of generic table diagram
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getScope](#getScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Gets the scope elements from the table.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getSelectedElements](#getSelectedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Gets currently selected elements from the diagram table.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getTableElementTypes](#getTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Return generic table diagram element types
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getVisibleColumnIds](#getVisibleColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Returns visible column ids from a generic table diagram.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getVisibleRowElements](#getVisibleRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Returns visible row elements of generic table diagram.
`static void`
`[refreshTable](#refreshTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Refresh diagram table.
`static void`
`[registerToolbarActionsConfigurator](#registerToolbarActionsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../actions/AMConfigurator.html) configurator)`
Registers toolbar actions configurator.
`static void`
`[removeRowElement](#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Removes row element from a generic table diagram
`static void`
`[setScope](#setScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)`
Sets the scope elements for the table.
`static void`
`[setSelectedElements](#setSelectedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Selects rows which represent given model elements.
`static void`
`[setTableElementTypes](#setTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> tableElementTypes)`
Sets generic table diagram element types
 Element types specify what elements can be added to table.
`static void`
`[waitForCellValuesLoad](#waitForCellValuesLoad(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Waits until all cell values are loaded.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
GenericTableManager
public GenericTableManager()
 ============ METHOD DETAIL ========== 
Method Details
createGenericTable
public static [Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) createGenericTable([Project](../magicdraw/core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) genericTableDiagramName)
 throws [ReadOnlyElementException](../magicdraw/openapi/uml/ReadOnlyElementException.html)
Creates generic table diagram in given project with given name
Parameters:
`project` - project in which to create generic table diagram
`genericTableDiagramName` - generic table diagram name
Returns:
created generic table diagram
Throws:
`[ReadOnlyElementException](../magicdraw/openapi/uml/ReadOnlyElementException.html)` - if project is read only throws exception
setTableElementTypes
public static void setTableElementTypes([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> tableElementTypes)
Sets generic table diagram element types
 Element types specify what elements can be added to table.
 For example, if you specify only class element types, only class elements can be added to table.
Parameters:
`diagram` - generic table diagram to set element types
`tableElementTypes` - object list with elements or classes, to use as table element types.
 Element types can be classes, metaclasses and stereotypes.
See Also:
[`getTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)`](#getTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))
getTableElementTypes
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getTableElementTypes([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Return generic table diagram element types
Parameters:
`diagram` - generic table diagram for which to return element types
Returns:
generic table diagram element types list of objects representing the element types
See Also:
[`setTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)`](#setTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))
addColumnsById
public static void addColumnsById([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> columnIDs)
Adds generic table columns by id
Parameters:
`diagram` - generic table diagram in which to add columns
`columnIDs` - column ids - column id's must be created using [`getColumnIDByPropertyName`](#getColumnIDByPropertyName(java.lang.String)), [`getColumnIDByTagName`](#getColumnIDByTag(java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))
See Also:
[`getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
getPossibleColumnIDs
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getPossibleColumnIDs([Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) type)
Returns all possible column ids for a generic table element types
Parameters:
`type` - type of the element for which to get property IDs
Returns:
property IDs of the given element type as list
See Also:
[`addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)`](#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))
getCellValue
@CheckForNullpublic static [Property](../magicdraw/properties/Property.html) getCellValue([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) columnId)
Returns cell value by row element and column id.
 To get all cell values use [`getCellValues(Diagram)`](#getCellValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)).
Parameters:
`diagram` - generic table diagram from which to get cell value
`element` - row element (used to find table row)
`columnId` - column id
Returns:
if found - generic table cell value `Property`, else null
See Also:
[`getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)`](#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))
getCellValues
public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Property](../magicdraw/properties/Property.html)>> getCellValues([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Returns all cell values by row element and column id.
Parameters:
`diagram` - table diagram from which to get cell values.
Returns:
all cell values by row element and column id.
getColumnIds
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getColumnIds([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Returns column ids from a generic table diagram
Parameters:
`diagram` - generic table diagram from which to get column ids
Returns:
column ids as list
See Also:
[`getVisibleColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)`](#getVisibleColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))
[`getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)`](#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))
getVisibleColumnIds
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getVisibleColumnIds([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Returns visible column ids from a generic table diagram.
Parameters:
`diagram` - generic table diagram from which to get visible column ids.
Returns:
column ids as list.
See Also:
[`getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)`](#getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))
[`getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)`](#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))
getColumnNames
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getColumnNames([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Returns column names from a generic table diagram
Parameters:
`diagram` - generic table diagram from which to get column names
Returns:
If any columns found - list with column names, else - empty list
getColumnNameById
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getColumnNameById([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) columnId)
Returns column name by id from a generic table diagram
Parameters:
`diagram` - generic table diagram to look for column
`columnId` - column id to look for
Returns:
if found - column name, else null
See Also:
[`addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)`](#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))
[`getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
getRowElements
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRowElements([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Returns row elements of generic table diagram
Parameters:
`diagram` - generic table diagram to get rows from
Returns:
if diagram has any rows - list of elements, else - empty list
See Also:
[`addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
getVisibleRowElements
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getVisibleRowElements([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Returns visible row elements of generic table diagram. Result will not contain elements of the rows which are not satisfied by the table filter.
Parameters:
`diagram` - generic table diagram to get rows from
Returns:
if diagram has visible rows - list of elements, else - empty list
See Also:
[`addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
[`removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
addRowElement
public static void addRowElement([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Adds an element into generic table diagram as row
Parameters:
`diagram` - generic table diagram to add element to
`element` - element to add
See Also:
[`getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)`](#getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))
[`removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
getExpandedVisibleRowsElements
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getExpandedVisibleRowsElements([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Gets the elements representing visible rows that are expanded in the table
Parameters:
`diagram` - generic table diagram to get rows of
getCollapsedVisibleRowsElements
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getCollapsedVisibleRowsElements([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Gets the elements representing visible rows that are collapsed in the table
Parameters:
`diagram` - generic table diagram to get rows of
expandRows
public static void expandRows([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)
Expands the given rows in table
Parameters:
`diagram` - generic table diagram to expand row of
`rowElements` - elements of rows to expand
collapseRows
public static void collapseRows([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)
Collapses the given rows in table
Parameters:
`diagram` - generic table diagram to collapse row of
`rowElements` - elements of rows to collapse
expandRowsIncludingParentsRecursively
public static void expandRowsIncludingParentsRecursively([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)
Expands the rows of given elements and their recursive parents in table
Parameters:
`diagram` - generic table diagram to expand row of
`rowElements` - elements of rows to expand
expandRowsRecursively
public static void expandRowsRecursively([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)
Expands the rows of given elements and their recursive children in table
Parameters:
`diagram` - generic table diagram to expand row of
`rowElements` - elements of rows to expand
collapseRowsRecursively
public static void collapseRowsRecursively([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> rowElements)
Collapses the rows of given elements and their recursive children in table
Parameters:
`diagram` - generic table diagram to collapse row of
`rowElements` - elements of rows to collapse
removeRowElement
public static void removeRowElement([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Removes row element from a generic table diagram
Parameters:
`diagram` - generic table diagram from which to remove element
`element` - element to remove
See Also:
[`getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)`](#getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))
[`addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)`](#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
registerToolbarActionsConfigurator
public static void registerToolbarActionsConfigurator([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [AMConfigurator](../actions/AMConfigurator.html) configurator)
Registers toolbar actions configurator.
Parameters:
`diagramType` - diagram type.
`configurator` - [`DTConfigurator`](../diagramtable/DTConfigurator.html).
getColumnIDByPropertyName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getColumnIDByPropertyName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Creates Column ID for table from property name
Parameters:
`propertyName` - propertyName
Returns:
Column ID
See Also:
[`PropertyNames`](../uml2/impl/PropertyNames.html)
getColumnIDByTag
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getColumnIDByTag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Creates Column ID for table from stereotype tag name
Parameters:
`tagName` - tagName of stereotype
`stereotype` - stereotype
Returns:
Column ID
addGenericTableToolbarConfigurator
public static void addGenericTableToolbarConfigurator([DTConfigurator](../diagramtable/DTConfigurator.html) configurator)
Adds generic table toolbar configurator.
 It allows to configure toolbar actions: add, remove, modify them.
Parameters:
`configurator` - configurator to add.
addGenericTableToolbarConfigurator
public static void addGenericTableToolbarConfigurator(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tableType,
 [DTConfigurator](../diagramtable/DTConfigurator.html) configurator)
Adds generic table toolbar configurator.
 It allows to configure toolbar actions: add, remove, modify them.
Parameters:
`tableType` - table type.
`configurator` - configurator to add.
addGenericTableContextConfigurator
public static void addGenericTableContextConfigurator(com.nomagic.diagramtable.DTContextConfigurator configurator)
Adds generic table context configurator.
 It allows to configure context actions: add, remove, modify them.
Parameters:
`configurator` - configurator to add.
addGenericTableContextConfigurator
public static void addGenericTableContextConfigurator(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tableType,
 com.nomagic.diagramtable.DTContextConfigurator configurator)
Adds generic table context configurator.
 It allows to configure context actions: add, remove, modify them.
Parameters:
`tableType` - table type.
`configurator` - configurator to add.
getSelectedElements
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getSelectedElements([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Gets currently selected elements from the diagram table. If columns are sorted, the elements are sorted and returned
 as displayed in GUI. If generic table is not open, empty list is returned.
Parameters:
`diagram` - diagram model element which represents the generic table.
Returns:
currently selected elements in the generic table or empty list if diagram is not open.
setSelectedElements
public static void setSelectedElements([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Selects rows which represent given model elements.
Parameters:
`diagram` - diagram model element which represents the generic table.
`elements` - model elements to select.
refreshTable
public static void refreshTable([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Refresh diagram table.
Parameters:
`diagram` - diagram element which represents the table.
setScope
public static void setScope([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)
Sets the scope elements for the table.
Parameters:
`diagram` - diagram element which represents the table, for which scope should be set.
`scope` - elements which should be set as the scope for table.
getScope
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getScope([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Gets the scope elements from the table.
Parameters:
`diagram` - diagram element which represents the table, from which scope elements should be returned.
Returns:
collection of all the elements that are set as scope for the table.
waitForCellValuesLoad
public static void waitForCellValuesLoad([Diagram](../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
 throws [TimeoutException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeoutException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Waits until all cell values are loaded.
Parameters:
`diagram` - diagram element which represents the table, which values are loading.
Throws:
`[TimeoutException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeoutException.html)` - thrown when within specified time cell values loading tasks show no progress.
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)` - thrown when thread is interrupted.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.generictable</a></div>
<h1 class="title" title="Class GenericTableManager">Class GenericTableManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.generictable.GenericTableManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">GenericTableManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Helps manage a generic table:
 create a new table,
 add, get and remove rows,
 add and get columns,
 get column values,
 get currently selected elements.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">GenericTableManager</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">addColumnsById</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; columnIDs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds generic table columns by id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addGenericTableContextConfigurator(com.nomagic.diagramtable.DTContextConfigurator)">addGenericTableContextConfigurator</a><wbr/>(com.nomagic.diagramtable.DTContextConfigurator configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds generic table context configurator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addGenericTableContextConfigurator(java.lang.String,com.nomagic.diagramtable.DTContextConfigurator)">addGenericTableContextConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tableType,
 com.nomagic.diagramtable.DTContextConfigurator configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds generic table context configurator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addGenericTableToolbarConfigurator(com.nomagic.diagramtable.DTConfigurator)">addGenericTableToolbarConfigurator</a><wbr/>(<a href="../diagramtable/DTConfigurator.html" title="interface in com.nomagic.diagramtable">DTConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds generic table toolbar configurator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addGenericTableToolbarConfigurator(java.lang.String,com.nomagic.diagramtable.DTConfigurator)">addGenericTableToolbarConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tableType,
 <a href="../diagramtable/DTConfigurator.html" title="interface in com.nomagic.diagramtable">DTConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds generic table toolbar configurator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addRowElement</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds an element into generic table diagram as row</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collapseRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">collapseRows</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collapses the given rows in table</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collapseRowsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">collapseRowsRecursively</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collapses the rows of given elements and their recursive children in table</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createGenericTable(com.nomagic.magicdraw.core.Project,java.lang.String)">createGenericTable</a><wbr/>(<a href="../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> genericTableDiagramName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates generic table diagram in given project with given name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#expandRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">expandRows</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Expands the given rows in table</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#expandRowsIncludingParentsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">expandRowsIncludingParentsRecursively</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Expands the rows of given elements and their recursive parents in table</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#expandRowsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">expandRowsRecursively</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Expands the rows of given elements and their recursive children in table</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../magicdraw/properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getCellValue</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns cell value by row element and column id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="../magicdraw/properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getCellValues</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all cell values by row element and column id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCollapsedVisibleRowsElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getCollapsedVisibleRowsElements</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the elements representing visible rows that are collapsed in the table</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnIDByPropertyName(java.lang.String)">getColumnIDByPropertyName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates Column ID for table from property name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnIDByTag(java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getColumnIDByTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates Column ID for table from stereotype tag name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getColumnIds</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns column ids from a generic table diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnNameById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.lang.String)">getColumnNameById</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns column name by id from a generic table diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getColumnNames</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns column names from a generic table diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExpandedVisibleRowsElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getExpandedVisibleRowsElements</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the elements representing visible rows that are expanded in the table</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPossibleColumnIDs</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all possible column ids for a generic table element types</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getRowElements</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns row elements of generic table diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getScope</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the scope elements from the table.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getSelectedElements</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets currently selected elements from the diagram table.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getTableElementTypes</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return generic table diagram element types</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getVisibleColumnIds</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns visible column ids from a generic table diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getVisibleRowElements</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns visible row elements of generic table diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#refreshTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">refreshTable</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Refresh diagram table.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerToolbarActionsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">registerToolbarActionsConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Registers toolbar actions configurator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeRowElement</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes row element from a generic table diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">setScope</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the scope elements for the table.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">setSelectedElements</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Selects rows which represent given model elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">setTableElementTypes</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; tableElementTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets generic table diagram element types
 Element types specify what elements can be added to table.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#waitForCellValuesLoad(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">waitForCellValuesLoad</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Waits until all cell values are loaded.</div>
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
<h3>GenericTableManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GenericTableManager</span>()</div>
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
<section class="detail" id="createGenericTable(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>createGenericTable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">createGenericTable</span><wbr/><span class="parameters">(<a href="../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> genericTableDiagramName)</span>
                                  throws <span class="exceptions"><a href="../magicdraw/openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates generic table diagram in given project with given name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project in which to create generic table diagram</dd>
<dd><code>genericTableDiagramName</code> - generic table diagram name</dd>
<dt>Returns:</dt>
<dd>created generic table diagram</dd>
<dt>Throws:</dt>
<dd><code><a href="../magicdraw/openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if project is read only throws exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">
<h3>setTableElementTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTableElementTypes</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; tableElementTypes)</span></div>
<div class="block">Sets generic table diagram element types
 Element types specify what elements can be added to table.
 For example, if you specify only class element types, only class elements can be added to table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to set element types</dd>
<dd><code>tableElementTypes</code> - object list with elements or classes, to use as table element types.
                          Element types can be classes, metaclasses and stereotypes.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getTableElementTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getTableElementTypes</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Return generic table diagram element types</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram for which to return element types</dd>
<dt>Returns:</dt>
<dd>generic table diagram element types list of objects representing the element types</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)"><code>setTableElementTypes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">
<h3>addColumnsById</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addColumnsById</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; columnIDs)</span></div>
<div class="block">Adds generic table columns by id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram in which to add columns</dd>
<dd><code>columnIDs</code> - column ids - column id's must be created using <a href="#getColumnIDByPropertyName(java.lang.String)"><code>getColumnIDByPropertyName</code></a>, <a href="#getColumnIDByTag(java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)"><code>getColumnIDByTagName</code></a></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPossibleColumnIDs</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getPossibleColumnIDs</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> type)</span></div>
<div class="block">Returns all possible column ids for a generic table element types</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - type of the element for which to get property IDs</dd>
<dt>Returns:</dt>
<dd>property IDs of the given element type as list</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)"><code>addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getCellValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../magicdraw/properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getCellValue</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
<div class="block">Returns cell value by row element and column id.
 To get all cell values use <a href="#getCellValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getCellValues(Diagram)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram from which to get cell value</dd>
<dd><code>element</code> - row element (used to find table row)</dd>
<dd><code>columnId</code> - column id</dd>
<dt>Returns:</dt>
<dd>if found - generic table cell value <code>Property</code>, else null</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
<li><a href="#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)"><code>addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getCellValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="../magicdraw/properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;&gt;</span> <span class="element-name">getCellValues</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Returns all cell values by row element and column id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - table diagram from which to get cell values.</dd>
<dt>Returns:</dt>
<dd>all cell values by row element and column id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getColumnIds</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnIds</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Returns column ids from a generic table diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram from which to get column ids</dd>
<dt>Returns:</dt>
<dd>column ids as list</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getVisibleColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getVisibleColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)</code></a></li>
<li><a href="#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
<li><a href="#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)"><code>addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getVisibleColumnIds</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getVisibleColumnIds</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Returns visible column ids from a generic table diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram from which to get visible column ids.</dd>
<dt>Returns:</dt>
<dd>column ids as list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)</code></a></li>
<li><a href="#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
<li><a href="#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)"><code>addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getColumnNames</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnNames</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Returns column names from a generic table diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram from which to get column names</dd>
<dt>Returns:</dt>
<dd>If any columns found - list with column names, else - empty list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNameById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.lang.String)">
<h3>getColumnNameById</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getColumnNameById</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
<div class="block">Returns column name by id from a generic table diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to look for column</dd>
<dd><code>columnId</code> - column id  to look for</dd>
<dt>Returns:</dt>
<dd>if found - column name, else null</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)"><code>addColumnsById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, java.util.List)</code></a></li>
<li><a href="#getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>getPossibleColumnIDs(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getRowElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRowElements</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Returns row elements of generic table diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to get rows from</dd>
<dt>Returns:</dt>
<dd>if diagram has any rows - list of elements, else - empty list</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
<li><a href="#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getVisibleRowElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getVisibleRowElements</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Returns visible row elements of generic table diagram. Result will not contain elements of the rows which are not satisfied by the table filter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to get rows from</dd>
<dt>Returns:</dt>
<dd>if diagram has visible rows - list of elements, else - empty list</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
<li><a href="#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addRowElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addRowElement</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Adds an element into generic table diagram as row</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to add element to</dd>
<dd><code>element</code> - element to add</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)</code></a></li>
<li><a href="#removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpandedVisibleRowsElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getExpandedVisibleRowsElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getExpandedVisibleRowsElements</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Gets the elements representing visible rows that are expanded in the table</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to get rows of</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCollapsedVisibleRowsElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getCollapsedVisibleRowsElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getCollapsedVisibleRowsElements</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Gets the elements representing visible rows that are collapsed in the table</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to get rows of</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="expandRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">
<h3>expandRows</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">expandRows</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</span></div>
<div class="block">Expands the given rows in table</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to expand row of</dd>
<dd><code>rowElements</code> - elements of rows to expand</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collapseRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">
<h3>collapseRows</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collapseRows</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</span></div>
<div class="block">Collapses the given rows in table</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to collapse row of</dd>
<dd><code>rowElements</code> - elements of rows to collapse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="expandRowsIncludingParentsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">
<h3>expandRowsIncludingParentsRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">expandRowsIncludingParentsRecursively</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</span></div>
<div class="block">Expands the rows of given elements and their recursive parents in table</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to expand row of</dd>
<dd><code>rowElements</code> - elements of rows to expand</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="expandRowsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">
<h3>expandRowsRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">expandRowsRecursively</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</span></div>
<div class="block">Expands the rows of given elements and their recursive children in table</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to expand row of</dd>
<dd><code>rowElements</code> - elements of rows to expand</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collapseRowsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">
<h3>collapseRowsRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">collapseRowsRecursively</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; rowElements)</span></div>
<div class="block">Collapses the rows of given elements and their recursive children in table</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram to collapse row of</dd>
<dd><code>rowElements</code> - elements of rows to collapse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeRowElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeRowElement</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Removes row element from a generic table diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - generic table diagram from which to remove element</dd>
<dd><code>element</code> - element to remove</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)"><code>getRowElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)</code></a></li>
<li><a href="#addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>addRowElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerToolbarActionsConfigurator(java.lang.String,com.nomagic.actions.AMConfigurator)">
<h3>registerToolbarActionsConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerToolbarActionsConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a> configurator)</span></div>
<div class="block">Registers toolbar actions configurator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type.</dd>
<dd><code>configurator</code> - <a href="../diagramtable/DTConfigurator.html" title="interface in com.nomagic.diagramtable"><code>DTConfigurator</code></a>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnIDByPropertyName(java.lang.String)">
<h3>getColumnIDByPropertyName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getColumnIDByPropertyName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Creates Column ID for table from property name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - propertyName</dd>
<dt>Returns:</dt>
<dd>Column ID</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../uml2/impl/PropertyNames.html" title="class in com.nomagic.uml2.impl"><code>PropertyNames</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnIDByTag(java.lang.String,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getColumnIDByTag</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getColumnIDByTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Creates Column ID for table from stereotype tag name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tagName</code> - tagName of stereotype</dd>
<dd><code>stereotype</code> - stereotype</dd>
<dt>Returns:</dt>
<dd>Column ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addGenericTableToolbarConfigurator(com.nomagic.diagramtable.DTConfigurator)">
<h3>addGenericTableToolbarConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addGenericTableToolbarConfigurator</span><wbr/><span class="parameters">(<a href="../diagramtable/DTConfigurator.html" title="interface in com.nomagic.diagramtable">DTConfigurator</a> configurator)</span></div>
<div class="block">Adds generic table toolbar configurator.
 It allows to configure toolbar actions: add, remove, modify them.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addGenericTableToolbarConfigurator(java.lang.String,com.nomagic.diagramtable.DTConfigurator)">
<h3>addGenericTableToolbarConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addGenericTableToolbarConfigurator</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tableType,
 <a href="../diagramtable/DTConfigurator.html" title="interface in com.nomagic.diagramtable">DTConfigurator</a> configurator)</span></div>
<div class="block">Adds generic table toolbar configurator.
 It allows to configure toolbar actions: add, remove, modify them.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tableType</code> - table type.</dd>
<dd><code>configurator</code> - configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addGenericTableContextConfigurator(com.nomagic.diagramtable.DTContextConfigurator)">
<h3>addGenericTableContextConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addGenericTableContextConfigurator</span><wbr/><span class="parameters">(com.nomagic.diagramtable.DTContextConfigurator configurator)</span></div>
<div class="block">Adds generic table context configurator.
 It allows to configure context actions: add, remove, modify them.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addGenericTableContextConfigurator(java.lang.String,com.nomagic.diagramtable.DTContextConfigurator)">
<h3>addGenericTableContextConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addGenericTableContextConfigurator</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tableType,
 com.nomagic.diagramtable.DTContextConfigurator configurator)</span></div>
<div class="block">Adds generic table context configurator.
 It allows to configure context actions: add, remove, modify them.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tableType</code> - table type.</dd>
<dd><code>configurator</code> - configurator to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getSelectedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getSelectedElements</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Gets currently selected elements from the diagram table. If columns are sorted, the elements are sorted and returned
 as displayed in GUI. If generic table is not open, empty list is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram model element which represents the generic table.</dd>
<dt>Returns:</dt>
<dd>currently selected elements in the generic table or empty list if diagram is not open.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">
<h3>setSelectedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSelectedElements</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Selects rows which represent given model elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram model element which represents the generic table.</dd>
<dd><code>elements</code> - model elements to select.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refreshTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>refreshTable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">refreshTable</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Refresh diagram table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram element which represents the table.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.Collection)">
<h3>setScope</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setScope</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</span></div>
<div class="block">Sets the scope elements for the table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram element which represents the table, for which scope should be set.</dd>
<dd><code>scope</code> - elements which should be set as the scope for table.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getScope</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getScope</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Gets the scope elements from the table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram element which represents the table, from which scope elements should be returned.</dd>
<dt>Returns:</dt>
<dd>collection of all the elements that are set as scope for the table.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="waitForCellValuesLoad(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>waitForCellValuesLoad</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">waitForCellValuesLoad</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeoutException.html" title="class or interface in java.util.concurrent">TimeoutException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Waits until all cell values are loaded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram element which represents the table, which values are loading.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeoutException.html" title="class or interface in java.util.concurrent">TimeoutException</a></code> - thrown when within specified time cell values loading tasks show no progress.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code> - thrown when thread is interrupted.</dd>
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
