# JAVA OPENAPI: Table (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/generictable/Table.html
- source_path: `com/nomagic/reportwizard/tools/generictable/Table.html`
- source_sha256: `899e56f9713f4f9dd47857cf6ab743f62aa4afa05e625cffc1996aad2a73e353`
- captured_utc: `2026-07-14T16:58:40.760323+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.generictable](package-summary.html)

## Class Table

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.generictable.Table

@OpenApiAllpublic classTable
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Class for getting row elements, column name and cell value.

Since:
Jan 25, 2012

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Table](#%3Cinit%3E(com.nomagic.diagramtable.Table,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))(com.nomagic.diagramtable.Table table,
 [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends com.nomagic.diagramtable.rows.DiagramTableRow>`
`[getAllDiagramTableRow](#getAllDiagramTableRow())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getAllRows](#getAllRows())()`
Get all row elements including collapsed
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getCellValue](#getCellValue(com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String))(com.nomagic.diagramtable.rows.DiagramTableRow diagramTableRow,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)`
Get cell value by rowElement and column property.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCellValueAsString](#getCellValueAsString(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) cellValue)`
Get cell value as string by cellValue.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCellValueAsString](#getCellValueAsString(java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) cellValue,
 boolean useFullType)`
Get cell value as string by cellValue.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getColumn](#getColumn(int))(int columnNumber)`
Get column name by column number as if the column is not visible.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getColumn](#getColumn(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)`
Get column name from column ID.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getColumnIds](#getColumnIds())()`
Get all column IDs.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getColumnNames](#getColumnNames())()`
Get all column names.
`[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getDiagram](#getDiagram())()`
Get diagram
`com.nomagic.diagramtable.rows.DiagramTableRow`
`[getDiagramTableRow](#getDiagramTableRow(int))(int rowNumber)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends com.nomagic.diagramtable.rows.DiagramTableRow>`
`[getDiagramTableRows](#getDiagramTableRows())()`

`com.nomagic.reportwizard.tools.DiagramTableTool`
`[getDiagramTool](#getDiagramTool())()`
Get DiagramTableTool
`com.nomagic.diagramtable.rows.DiagramTableRow`
`[getFilteredDiagramTableRow](#getFilteredDiagramTableRow(int))(int rowNumber)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends com.nomagic.diagramtable.rows.DiagramTableRow>`
`[getFilteredDiagramTableRows](#getFilteredDiagramTableRows())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getFilteredRow](#getFilteredRow(int))(int rowNumber)`
Get filtered row element specific row number.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getFilteredRows](#getFilteredRows())()`
Get filtered row elements.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getRow](#getRow(int))(int rowNumber)`
Get row element specific row number.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRows](#getRows())()`
Get all row elements.
`com.nomagic.diagramtable.Table`
`[getTable](#getTable())()`
Get diagram table
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(int,int))(int rowNumber,
 int columnNumber)`
Get value from row number and column number.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)`
Get value from row element and column number.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnIdOrName)`
Get value from row element and column ID or column name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValueAsString](#getValueAsString(int,int))(int rowNumber,
 int columnNumber)`
Get value from row number and column Id or column name as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValueAsString](#getValueAsString(int,int,boolean))(int rowNumber,
 int columnNumber,
 boolean useFullType)`
Get value from row number and column Id or column name as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValueAsString](#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)`
Get value from row element and column number as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValueAsString](#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber,
 boolean useFullType)`
Get value from row element and column number as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValueAsString](#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnIdOrName)`
Get value from row element and column Id or column name as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValueAsString](#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnIdOrName,
 boolean useFullType)`
Get value from row element and column Id or column name as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getVisibleColumn](#getVisibleColumn(int))(int columnNumber)`
Get only visible column name by column number.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getVisibleColumnIds](#getVisibleColumnIds())()`
Get list of visible column id.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getVisibleValue](#getVisibleValue(int,int))(int rowNumber,
 int columnNumber)`
Get value from row number and column number.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getVisibleValue](#getVisibleValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)`
Get visible value from row element and column number.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getVisibleValueAsString](#getVisibleValueAsString(int,int))(int rowNumber,
 int columnNumber)`
Get value from row number and column Id or column name as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getVisibleValueAsString](#getVisibleValueAsString(int,int,boolean))(int rowNumber,
 int columnNumber,
 boolean useFullType)`
Get value from row number and column Id or column name as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getVisibleValueAsString](#getVisibleValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)`
Get visible value from row element and column number as String.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getVisibleValueAsString](#getVisibleValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber,
 boolean useFullType)`
Get visible value from row element and column number as String.
`boolean`
`[isFilteredRows](#isFilteredRows())()`
True for filtered rows
`void`
`[resetFilteredRows](#resetFilteredRows())()`
Reset isFilteredRows value by state from getRow
`void`
`[setFilteredRows](#setFilteredRows(boolean))(boolean isFilteredRows)`
True for filtered rows
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Table
public Table(com.nomagic.diagramtable.Table table,
 [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Constructor.
Parameters:
`table` - generic table instance
 ============ METHOD DETAIL ========== 
Method Details
getTable
public com.nomagic.diagramtable.Table getTable()
Get diagram table
getDiagram
public [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) getDiagram()
Get diagram
Returns:
diagram
getDiagramTool
public com.nomagic.reportwizard.tools.DiagramTableTool getDiagramTool()
Get DiagramTableTool
Returns:
DiagramTableTool
isFilteredRows
public boolean isFilteredRows()
True for filtered rows
Returns:
setFilteredRows
public void setFilteredRows(boolean isFilteredRows)
True for filtered rows
Parameters:
`isFilteredRows` -
resetFilteredRows
public void resetFilteredRows()
Reset isFilteredRows value by state from getRow
getDiagramTableRows
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends com.nomagic.diagramtable.rows.DiagramTableRow> getDiagramTableRows()
getRows
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRows()
Get all row elements.
Returns:
value is list of element
getAllRows
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getAllRows()
Get all row elements including collapsed
Returns:
value is list of element
getAllDiagramTableRow
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends com.nomagic.diagramtable.rows.DiagramTableRow> getAllDiagramTableRow()
getDiagramTableRow
public com.nomagic.diagramtable.rows.DiagramTableRow getDiagramTableRow(int rowNumber)
getRow
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getRow(int rowNumber)
Get row element specific row number.
Parameters:
`rowNumber` - row number starts with 0
Returns:
value is row element
getFilteredDiagramTableRows
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends com.nomagic.diagramtable.rows.DiagramTableRow> getFilteredDiagramTableRows()
getFilteredRows
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getFilteredRows()
Get filtered row elements.
Returns:
value is list of element
getFilteredDiagramTableRow
public com.nomagic.diagramtable.rows.DiagramTableRow getFilteredDiagramTableRow(int rowNumber)
getFilteredRow
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getFilteredRow(int rowNumber)
Get filtered row element specific row number.
Parameters:
`rowNumber` - row number starts with 0
Returns:
value is row element
getColumn
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getColumn([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)
Get column name from column ID.
Parameters:
`columnId` - the id of column. Using column id for benefiting of consistency between different languages
 e.g. French and English. The column ID can be retrieved by method getColumnIds().
Returns:
value is name of column
getColumn
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getColumn(int columnNumber)
Get column name by column number as if the column is not visible.
Parameters:
`columnNumber` - column number starts with 1. The column number 0 is row number.
Returns:
value is name of column
getColumnNames
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getColumnNames()
Get all column names.
Returns:
value is the list of column name
getColumnIds
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getColumnIds()
Get all column IDs.
Returns:
value is the list of column id
getValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnIdOrName)
Get value from row element and column ID or column name.
Parameters:
`rowElement` - row element
`columnIdOrName` - column id or column name
Returns:
value is the value at cell. If cell contains element, the value is Element.
getValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)
Get value from row element and column number.
Parameters:
`rowElement` - row element
`columnNumber` - column number starts with 0
Returns:
value is the value at cell. If cell contains element, the value is Element.
getValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue(int rowNumber,
 int columnNumber)
Get value from row number and column number.
Parameters:
`rowNumber` - row number start with 0
`columnNumber` - column number start with 1. The column number 0 is row number.
Returns:
value is the value at cell. If cell contains element, the value is Element.
getValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValueAsString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnIdOrName)
Get value from row element and column Id or column name as String.
Parameters:
`rowElement` - row element
`columnIdOrName` - column id or column name
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValueAsString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnIdOrName,
 boolean useFullType)
Get value from row element and column Id or column name as String.
Parameters:
`rowElement` - row element
`columnIdOrName` - column id or column name
`useFullType` - true to use full type when convert element to string using Representation Text api of MagicDraw
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValueAsString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)
Get value from row element and column number as String.
Parameters:
`rowElement` - row element
`columnNumber` - column number start with 0.
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValueAsString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber,
 boolean useFullType)
Get value from row element and column number as String.
Parameters:
`rowElement` - row element
`columnNumber` - column number start with 0.
`useFullType` - true to use full type when convert element to string using Representation Text api of MagicDraw
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValueAsString(int rowNumber,
 int columnNumber)
Get value from row number and column Id or column name as String.
Parameters:
`rowNumber` - row number start with 0
`columnNumber` - column number start with 1. The column number 0 is row number
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValueAsString(int rowNumber,
 int columnNumber,
 boolean useFullType)
Get value from row number and column Id or column name as String.
Parameters:
`rowNumber` - row number start with 0
`columnNumber` - column number start with 1. The column number 0 is row number
`useFullType` - true to use full type when convert element to string using Representation Text api of MagicDraw
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getVisibleColumnIds
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getVisibleColumnIds()
Get list of visible column id.
Returns:
list of visible column id.
getVisibleColumn
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getVisibleColumn(int columnNumber)
Get only visible column name by column number.
Parameters:
`columnNumber` - column number
Returns:
visible column name
getVisibleValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getVisibleValue([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)
Get visible value from row element and column number.
Parameters:
`rowElement` - row element
`columnNumber` - column number starts with 0
Returns:
value is the value at visible cell. If cell contains element, the value is Element.
getVisibleValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getVisibleValue(int rowNumber,
 int columnNumber)
Get value from row number and column number.
Parameters:
`rowNumber` - row number start with 0
`columnNumber` - column number start with 1. The column number 0 is row number.
Returns:
value is the value at cell. If cell contains element, the value is Element.
getVisibleValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getVisibleValueAsString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber)
Get visible value from row element and column number as String.
Parameters:
`rowElement` - row element
`columnNumber` - column number start with 0.
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getVisibleValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getVisibleValueAsString([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 int columnNumber,
 boolean useFullType)
Get visible value from row element and column number as String.
Parameters:
`rowElement` - row element
`columnNumber` - column number start with 0.
`useFullType` - true to use full type when convert element to string using Representation Text api of MagicDraw
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getVisibleValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getVisibleValueAsString(int rowNumber,
 int columnNumber)
Get value from row number and column Id or column name as String.
Parameters:
`rowNumber` - row number start with 0
`columnNumber` - column number start with 1. The column number 0 is row number
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getVisibleValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getVisibleValueAsString(int rowNumber,
 int columnNumber,
 boolean useFullType)
Get value from row number and column Id or column name as String.
Parameters:
`rowNumber` - row number start with 0
`columnNumber` - column number start with 1. The column number 0 is row number
`useFullType` - true to use full type when convert element to string using Representation Text api of MagicDraw
Returns:
value is the value at cell and converts into String. The String value is created by MagicDraw
 representation text API.
getCellValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getCellValue(com.nomagic.diagramtable.rows.DiagramTableRow diagramTableRow,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)
Get cell value by rowElement and column property.
Parameters:
`diagramTableRow` - diagram table row element
`columnId` - column id
Returns:
object of cell value
getCellValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCellValueAsString([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) cellValue,
 boolean useFullType)
Get cell value as string by cellValue.
Parameters:
`cellValue` - value at specified cell
`useFullType` - true to create representation as full type
Returns:
string of cell value
getCellValueAsString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCellValueAsString([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) cellValue)
Get cell value as string by cellValue.
Parameters:
`cellValue` - value at specified cell
Returns:
string of cell value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.generictable</a></div>
<h1 class="title" title="Class Table">Class Table</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.generictable.Table</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Table</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for getting row elements, column name and cell value.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 25, 2012</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.diagramtable.Table,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">Table</a><wbr/>(com.nomagic.diagramtable.Table table,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;? extends com.nomagic.diagramtable.rows.DiagramTableRow&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllDiagramTableRow()">getAllDiagramTableRow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllRows()">getAllRows</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all row elements including collapsed</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValue(com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">getCellValue</a><wbr/>(com.nomagic.diagramtable.rows.DiagramTableRow diagramTableRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get cell value by rowElement and column property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValueAsString(java.lang.Object)">getCellValueAsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> cellValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get cell value as string by cellValue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValueAsString(java.lang.Object,boolean)">getCellValueAsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> cellValue,
 boolean useFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get cell value as string by cellValue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumn(int)">getColumn</a><wbr/>(int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get column name by column number as if the column is not visible.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumn(java.lang.String)">getColumn</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get column name from column ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnIds()">getColumnIds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all column IDs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnNames()">getColumnNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all column names.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagram()">getDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.diagramtable.rows.DiagramTableRow</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramTableRow(int)">getDiagramTableRow</a><wbr/>(int rowNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;? extends com.nomagic.diagramtable.rows.DiagramTableRow&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramTableRows()">getDiagramTableRows</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.reportwizard.tools.DiagramTableTool</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramTool()">getDiagramTool</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get DiagramTableTool</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.diagramtable.rows.DiagramTableRow</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilteredDiagramTableRow(int)">getFilteredDiagramTableRow</a><wbr/>(int rowNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;? extends com.nomagic.diagramtable.rows.DiagramTableRow&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilteredDiagramTableRows()">getFilteredDiagramTableRows</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilteredRow(int)">getFilteredRow</a><wbr/>(int rowNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get filtered row element specific row number.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilteredRows()">getFilteredRows</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get filtered row elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRow(int)">getRow</a><wbr/>(int rowNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get row element specific row number.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRows()">getRows</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all row elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.diagramtable.Table</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTable()">getTable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get diagram table</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(int,int)">getValue</a><wbr/>(int rowNumber,
 int columnNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row number and column number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">getValue</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row element and column number.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getValue</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnIdOrName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row element and column ID or column name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueAsString(int,int)">getValueAsString</a><wbr/>(int rowNumber,
 int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row number and column Id or column name as String.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueAsString(int,int,boolean)">getValueAsString</a><wbr/>(int rowNumber,
 int columnNumber,
 boolean useFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row number and column Id or column name as String.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">getValueAsString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row element and column number as String.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int,boolean)">getValueAsString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber,
 boolean useFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row element and column number as String.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getValueAsString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnIdOrName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row element and column Id or column name as String.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean)">getValueAsString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnIdOrName,
 boolean useFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row element and column Id or column name as String.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleColumn(int)">getVisibleColumn</a><wbr/>(int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get only visible column name by column number.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleColumnIds()">getVisibleColumnIds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of visible column id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleValue(int,int)">getVisibleValue</a><wbr/>(int rowNumber,
 int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row number and column number.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">getVisibleValue</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get visible value from row element and column number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleValueAsString(int,int)">getVisibleValueAsString</a><wbr/>(int rowNumber,
 int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row number and column Id or column name as String.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleValueAsString(int,int,boolean)">getVisibleValueAsString</a><wbr/>(int rowNumber,
 int columnNumber,
 boolean useFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value from row number and column Id or column name as String.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">getVisibleValueAsString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get visible value from row element and column number as String.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int,boolean)">getVisibleValueAsString</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber,
 boolean useFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get visible value from row element and column number as String.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFilteredRows()">isFilteredRows</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">True for filtered rows</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetFilteredRows()">resetFilteredRows</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reset isFilteredRows value by state from getRow</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFilteredRows(boolean)">setFilteredRows</a><wbr/>(boolean isFilteredRows)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">True for filtered rows</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.diagramtable.Table,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>Table</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Table</span><wbr/><span class="parameters">(com.nomagic.diagramtable.Table table,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>table</code> - generic table instance</dd>
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
<section class="detail" id="getTable()">
<h3>getTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.diagramtable.Table</span> <span class="element-name">getTable</span>()</div>
<div class="block">Get diagram table</div>
</section>
</li>
<li>
<section class="detail" id="getDiagram()">
<h3>getDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">getDiagram</span>()</div>
<div class="block">Get diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramTool()">
<h3>getDiagramTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.reportwizard.tools.DiagramTableTool</span> <span class="element-name">getDiagramTool</span>()</div>
<div class="block">Get DiagramTableTool</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>DiagramTableTool</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFilteredRows()">
<h3>isFilteredRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFilteredRows</span>()</div>
<div class="block">True for filtered rows</div>
<dl class="notes">
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFilteredRows(boolean)">
<h3>setFilteredRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFilteredRows</span><wbr/><span class="parameters">(boolean isFilteredRows)</span></div>
<div class="block">True for filtered rows</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isFilteredRows</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetFilteredRows()">
<h3>resetFilteredRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetFilteredRows</span>()</div>
<div class="block">Reset isFilteredRows value by state from getRow</div>
</section>
</li>
<li>
<section class="detail" id="getDiagramTableRows()">
<h3>getDiagramTableRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends com.nomagic.diagramtable.rows.DiagramTableRow&gt;</span> <span class="element-name">getDiagramTableRows</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRows()">
<h3>getRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRows</span>()</div>
<div class="block">Get all row elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value is list of element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllRows()">
<h3>getAllRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getAllRows</span>()</div>
<div class="block">Get all row elements including collapsed</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value is list of element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllDiagramTableRow()">
<h3>getAllDiagramTableRow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends com.nomagic.diagramtable.rows.DiagramTableRow&gt;</span> <span class="element-name">getAllDiagramTableRow</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDiagramTableRow(int)">
<h3>getDiagramTableRow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.diagramtable.rows.DiagramTableRow</span> <span class="element-name">getDiagramTableRow</span><wbr/><span class="parameters">(int rowNumber)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRow(int)">
<h3>getRow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getRow</span><wbr/><span class="parameters">(int rowNumber)</span></div>
<div class="block">Get row element specific row number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number starts with 0</dd>
<dt>Returns:</dt>
<dd>value is row element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFilteredDiagramTableRows()">
<h3>getFilteredDiagramTableRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends com.nomagic.diagramtable.rows.DiagramTableRow&gt;</span> <span class="element-name">getFilteredDiagramTableRows</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getFilteredRows()">
<h3>getFilteredRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getFilteredRows</span>()</div>
<div class="block">Get filtered row elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value is list of element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFilteredDiagramTableRow(int)">
<h3>getFilteredDiagramTableRow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.diagramtable.rows.DiagramTableRow</span> <span class="element-name">getFilteredDiagramTableRow</span><wbr/><span class="parameters">(int rowNumber)</span></div>
</section>
</li>
<li>
<section class="detail" id="getFilteredRow(int)">
<h3>getFilteredRow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getFilteredRow</span><wbr/><span class="parameters">(int rowNumber)</span></div>
<div class="block">Get filtered row element specific row number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number starts with 0</dd>
<dt>Returns:</dt>
<dd>value is row element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumn(java.lang.String)">
<h3>getColumn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getColumn</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
<div class="block">Get column name from column ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>columnId</code> - the id of column. Using column id for benefiting of consistency between different languages
           e.g. French and English. The column ID can be retrieved by method getColumnIds().</dd>
<dt>Returns:</dt>
<dd>value is name of column</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumn(int)">
<h3>getColumn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getColumn</span><wbr/><span class="parameters">(int columnNumber)</span></div>
<div class="block">Get column name by column number as if the column is not visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>columnNumber</code> - column number starts with 1. The column number 0 is row number.</dd>
<dt>Returns:</dt>
<dd>value is name of column</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNames()">
<h3>getColumnNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnNames</span>()</div>
<div class="block">Get all column names.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value is the list of column name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnIds()">
<h3>getColumnIds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnIds</span>()</div>
<div class="block">Get all column IDs.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value is the list of column id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnIdOrName)</span></div>
<div class="block">Get value from row element and column ID or column name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnIdOrName</code> - column id or column name</dd>
<dt>Returns:</dt>
<dd>value is the value at cell. If cell contains element, the value is Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</span></div>
<div class="block">Get value from row element and column number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnNumber</code> - column number starts with 0</dd>
<dt>Returns:</dt>
<dd>value is the value at cell. If cell contains element, the value is Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(int,int)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(int rowNumber,
 int columnNumber)</span></div>
<div class="block">Get value from row number and column number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number start with 0</dd>
<dd><code>columnNumber</code> - column number start with 1. The column number 0 is row number.</dd>
<dt>Returns:</dt>
<dd>value is the value at cell. If cell contains element, the value is Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueAsString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnIdOrName)</span></div>
<div class="block">Get value from row element and column Id or column name as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnIdOrName</code> - column id or column name</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,boolean)">
<h3>getValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueAsString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnIdOrName,
 boolean useFullType)</span></div>
<div class="block">Get value from row element and column Id or column name as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnIdOrName</code> - column id or column name</dd>
<dd><code>useFullType</code> - true to use full type when convert element to string using Representation Text api of MagicDraw</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">
<h3>getValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueAsString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</span></div>
<div class="block">Get value from row element and column number as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnNumber</code> - column number start with 0.</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int,boolean)">
<h3>getValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueAsString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber,
 boolean useFullType)</span></div>
<div class="block">Get value from row element and column number as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnNumber</code> - column number start with 0.</dd>
<dd><code>useFullType</code> - true to use full type when convert element to string using Representation Text api of MagicDraw</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueAsString(int,int)">
<h3>getValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueAsString</span><wbr/><span class="parameters">(int rowNumber,
 int columnNumber)</span></div>
<div class="block">Get value from row number and column Id or column name as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number start with 0</dd>
<dd><code>columnNumber</code> - column number start with 1. The column number 0 is row number</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueAsString(int,int,boolean)">
<h3>getValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueAsString</span><wbr/><span class="parameters">(int rowNumber,
 int columnNumber,
 boolean useFullType)</span></div>
<div class="block">Get value from row number and column Id or column name as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number start with 0</dd>
<dd><code>columnNumber</code> - column number start with 1. The column number 0 is row number</dd>
<dd><code>useFullType</code> - true to use full type when convert element to string using Representation Text api of MagicDraw</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleColumnIds()">
<h3>getVisibleColumnIds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getVisibleColumnIds</span>()</div>
<div class="block">Get list of visible column id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of visible column id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleColumn(int)">
<h3>getVisibleColumn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVisibleColumn</span><wbr/><span class="parameters">(int columnNumber)</span></div>
<div class="block">Get only visible column name by column number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>columnNumber</code> - column number</dd>
<dt>Returns:</dt>
<dd>visible column name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">
<h3>getVisibleValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getVisibleValue</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</span></div>
<div class="block">Get visible value from row element and column number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnNumber</code> - column number starts with 0</dd>
<dt>Returns:</dt>
<dd>value is the value at visible cell. If cell contains element, the value is Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleValue(int,int)">
<h3>getVisibleValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getVisibleValue</span><wbr/><span class="parameters">(int rowNumber,
 int columnNumber)</span></div>
<div class="block">Get value from row number and column number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number start with 0</dd>
<dd><code>columnNumber</code> - column number start with 1. The column number 0 is row number.</dd>
<dt>Returns:</dt>
<dd>value is the value at cell. If cell contains element, the value is Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int)">
<h3>getVisibleValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVisibleValueAsString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber)</span></div>
<div class="block">Get visible value from row element and column number as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnNumber</code> - column number start with 0.</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleValueAsString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,int,boolean)">
<h3>getVisibleValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVisibleValueAsString</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 int columnNumber,
 boolean useFullType)</span></div>
<div class="block">Get visible value from row element and column number as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnNumber</code> - column number start with 0.</dd>
<dd><code>useFullType</code> - true to use full type when convert element to string using Representation Text api of MagicDraw</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleValueAsString(int,int)">
<h3>getVisibleValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVisibleValueAsString</span><wbr/><span class="parameters">(int rowNumber,
 int columnNumber)</span></div>
<div class="block">Get value from row number and column Id or column name as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number start with 0</dd>
<dd><code>columnNumber</code> - column number start with 1. The column number 0 is row number</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleValueAsString(int,int,boolean)">
<h3>getVisibleValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVisibleValueAsString</span><wbr/><span class="parameters">(int rowNumber,
 int columnNumber,
 boolean useFullType)</span></div>
<div class="block">Get value from row number and column Id or column name as String.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowNumber</code> - row number start with 0</dd>
<dd><code>columnNumber</code> - column number start with 1. The column number 0 is row number</dd>
<dd><code>useFullType</code> - true to use full type when convert element to string using Representation Text api of MagicDraw</dd>
<dt>Returns:</dt>
<dd>value is the value at cell and converts into String. The String value is created by MagicDraw
         representation text API.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellValue(com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">
<h3>getCellValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getCellValue</span><wbr/><span class="parameters">(com.nomagic.diagramtable.rows.DiagramTableRow diagramTableRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
<div class="block">Get cell value by rowElement and column property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramTableRow</code> - diagram table row element</dd>
<dd><code>columnId</code> - column id</dd>
<dt>Returns:</dt>
<dd>object of cell value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellValueAsString(java.lang.Object,boolean)">
<h3>getCellValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCellValueAsString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> cellValue,
 boolean useFullType)</span></div>
<div class="block">Get cell value as string by cellValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cellValue</code> - value at specified cell</dd>
<dd><code>useFullType</code> - true to create representation as full type</dd>
<dt>Returns:</dt>
<dd>string of cell value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellValueAsString(java.lang.Object)">
<h3>getCellValueAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCellValueAsString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> cellValue)</span></div>
<div class="block">Get cell value as string by cellValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cellValue</code> - value at specified cell</dd>
<dt>Returns:</dt>
<dd>string of cell value</dd>
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
