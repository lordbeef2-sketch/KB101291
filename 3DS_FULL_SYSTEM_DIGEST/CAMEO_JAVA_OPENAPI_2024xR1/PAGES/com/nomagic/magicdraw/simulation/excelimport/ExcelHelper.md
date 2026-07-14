# JAVA OPENAPI: ExcelHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/simulation/excelimport/ExcelHelper.html
- source_path: `com/nomagic/magicdraw/simulation/excelimport/ExcelHelper.html`
- source_sha256: `f807143f080bd9f9685ba2f3d8f9bbaec68d7eb55377d694b40364ae4d0d4d03`
- captured_utc: `2026-07-14T16:51:31.229336+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.excelimport](package-summary.html)

## Class ExcelHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.excelimport.ExcelHelper

@OpenApiAllpublic classExcelHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The helper class being used in the scripts for handling data transformation
 and other utilities between fUML runtime object and Excel file.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ExcelHelper](#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](../execution/session/SimulationSession.html) session)`
constructor.
`[ExcelHelper](#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([SimulationSession](../execution/session/SimulationSession.html) session,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) scriptContainer)`
constructor.
`[ExcelHelper](#%3Cinit%3E(fUML.Semantics.Classes.Kernel.Object_))(fUML.Semantics.Classes.Kernel.Object_ context)`
constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getCellValue](#getCellValue(java.lang.String,java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 int atCol)`
get value by specific row and column in the Excel file.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getCellValue](#getCellValue(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atCol)`
get value by specific row and column in the Excel file.
`int`
`[getLatestRowNum](#getLatestRowNum(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName)`
Get the latest row number of the sheet in the Excel file.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,int,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,java.lang.Number))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,java.lang.String,int,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectFromSpreadSheet](#readObjectFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int startRow,
 int endRow)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Number))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Number,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList for all rows in excel.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Read the Excel file and create the fUML ValueList for all rows in excel.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int startRow,
 int endRow)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,int,int,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int startRow,
 int endRow,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList.
`fUML.Semantics.Classes.Kernel.ValueList`
`[readObjectsFromSpreadSheet](#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Read the Excel file and create the fUML ValueList for all rows in excel.
`void`
`[setCellValue](#setCellValue(java.lang.Object,java.lang.String,java.lang.String,int,int))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 int atCol)`
Set fUML runtime value to specific row and column in the Excel file.
`void`
`[setCellValue](#setCellValue(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,java.lang.Number))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atCol)`
Set fUML runtime value to specific row and column in the Excel file.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,int))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,int,java.lang.Object))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Number))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Number,java.lang.Object))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,int))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,int,java.lang.Object))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,java.lang.Number))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[updatefUMLValueFromSpreadSheet](#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,java.lang.Number,java.lang.Object))(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
update the value of SpreadSheet to fUML runtime object.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,int,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int atRow,
 boolean isReplace)`
Write the fUML runtime value to the Excel file.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,int,boolean,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int atRow,
 boolean isReplace,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Write the fUML runtime value to the Excel file.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.Number,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace)`
Write the fUML runtime value to the Excel file.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.Number,boolean,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Write the fUML runtime value to the Excel file.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,int,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 boolean isReplace)`
Write the fUML runtime value to the Excel file.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,int,boolean,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 boolean isReplace,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Write the fUML runtime value to the Excel file.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace)`
Write the fUML runtime value to the Excel file.
`void`
`[writeObjectsToSpreadSheet](#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,boolean,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)`
Write the fUML runtime value to the Excel file.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ExcelHelper
public ExcelHelper([SimulationSession](../execution/session/SimulationSession.html) session)
constructor.
Parameters:
`session` - the running session.
ExcelHelper
public ExcelHelper([SimulationSession](../execution/session/SimulationSession.html) session,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) scriptContainer)
constructor.
Parameters:
`session` - the running session.
ExcelHelper
public ExcelHelper(fUML.Semantics.Classes.Kernel.Object_ context)
constructor.
Parameters:
`context` - the context of caller
 ============ METHOD DETAIL ========== 
Method Details
getLatestRowNum
public int getLatestRowNum([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName)
Get the latest row number of the sheet in the Excel file.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
Returns:
the latest row number of the sheet in the Excel file
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`rowIndex` - the index of row
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`rowIndex` - the index of row
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`rowIndex` - the index of row
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`rowIndex` - the index of row
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`rowIndex` - the index of row
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`rowIndex` - the index of row
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`rowIndex` - the index of row
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`rowIndex` - the index of row
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int startRow,
 int endRow)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`startRow` - the start row number
`endRow` - the end row number
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`startRow` - the start row number
`endRow` - the end row number
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`startRow` - the start row number
`endRow` - the end row number
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int startRow,
 int endRow)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`startRow` - the start row number
`endRow` - the end row number
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`startRow` - the start row number
`endRow` - the end row number
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList for all rows in excel.
Parameters:
`fileName` - the Excel file name
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList for all rows in excel.
Parameters:
`fileName` - the Excel file name
`name` - the name of Mapping Class or sheet name.
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList for all rows in excel.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) startRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) endRow,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`startRow` - the start row number
`endRow` - the end row number
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
readObjectsFromSpreadSheet
@CheckForNullpublic fUML.Semantics.Classes.Kernel.ValueList readObjectsFromSpreadSheet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int startRow,
 int endRow,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Read the Excel file and create the fUML ValueList.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`startRow` - the start row number
`endRow` - the end row number
`mappingClass` - the mapping class name `String` or mapping class `Element`
Returns:
the fUML ValueList of the data in the Excel file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - could be thrown if problem occurs when reading excel data
setCellValue
public void setCellValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 int atCol)
Set fUML runtime value to specific row and column in the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row index number
`atCol` - the column index number
setCellValue
public void setCellValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atCol)
Set fUML runtime value to specific row and column in the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row index number
`atCol` - the column index number
getCellValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getCellValue([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 int atCol)
get value by specific row and column in the Excel file.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row index number
`atCol` - the column index number
Returns:
the value of cell
getCellValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getCellValue([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atCol)
get value by specific row and column in the Excel file.
Parameters:
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row index number
`atCol` - the column index number
Returns:
the value of cell
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`rowIndex` - the row index
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`rowIndex` - the row index
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`sheetName` - the sheet name
`rowIndex` - the row index
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`sheetName` - the sheet name
`rowIndex` - the row index
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int rowIndex,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`rowIndex` - the row index
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`rowIndex` - the row index
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) rowIndex,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`sheetName` - the sheet name
`rowIndex` - the row index
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
updatefUMLValueFromSpreadSheet
public void updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int rowIndex,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
update the value of SpreadSheet to fUML runtime object.
Parameters:
`value` - the runtime object
`fileName` - the spreadSheet file path
`sheetName` - the sheet name
`rowIndex` - the row index
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int atRow,
 boolean isReplace,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 boolean isReplace)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 int atRow,
 boolean isReplace)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) atRow,
 boolean isReplace,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
writeObjectsToSpreadSheet
public void writeObjectsToSpreadSheet([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sheetName,
 int atRow,
 boolean isReplace,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) mappingClass)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Write the fUML runtime value to the Excel file.
Parameters:
`object` - the fUML runtime value (ValueList/Value)
`fileName` - the Excel file name
`sheetName` - the sheet name
`atRow` - the row number to write the data
`isReplace` - if true, it will replace the existing data
 if false, it will insert the data at atRow
`mappingClass` - the mapping class name `String` or mapping class `Element`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.excelimport</a></div>
<h1 class="title" title="Class ExcelHelper">Class ExcelHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.excelimport.ExcelHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ExcelHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The helper class being used in the scripts for handling data transformation
 and other utilities between fUML runtime object and Excel file.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">ExcelHelper</a><wbr/>(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color">
<div class="block">constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">ExcelHelper</a><wbr/>(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> scriptContainer)</code></div>
<div class="col-last odd-row-color">
<div class="block">constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(fUML.Semantics.Classes.Kernel.Object_)">ExcelHelper</a><wbr/>(fUML.Semantics.Classes.Kernel.Object_ context)</code></div>
<div class="col-last even-row-color">
<div class="block">constructor.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValue(java.lang.String,java.lang.String,int,int)">getCellValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 int atCol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get value by specific row and column in the Excel file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValue(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number)">getCellValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atCol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get value by specific row and column in the Excel file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLatestRowNum(java.lang.String,java.lang.String)">getLatestRowNum</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the latest row number of the sheet in the Excel file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,int)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,int,java.lang.Object)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,java.lang.Number)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Object)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,java.lang.String,int)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,java.lang.String,int,java.lang.Object)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Object)">readObjectFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,int,int)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int startRow,
 int endRow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Number)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Number,java.lang.Object)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.Object)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList for all rows in excel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.String)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList for all rows in excel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,int,int)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int startRow,
 int endRow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,int,int,java.lang.Object)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int startRow,
 int endRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number,java.lang.Object)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Object)">readObjectsFromSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read the Excel file and create the fUML ValueList for all rows in excel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCellValue(java.lang.Object,java.lang.String,java.lang.String,int,int)">setCellValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 int atCol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set fUML runtime value to specific row and column in the Excel file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCellValue(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,java.lang.Number)">setCellValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atCol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set fUML runtime value to specific row and column in the Excel file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,int)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,int,java.lang.Object)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Number)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Number,java.lang.Object)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,int)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,int,java.lang.Object)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,java.lang.Number)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,java.lang.Number,java.lang.Object)">updatefUMLValueFromSpreadSheet</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,int,boolean)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int atRow,
 boolean isReplace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,int,boolean,java.lang.Object)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int atRow,
 boolean isReplace,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.Number,boolean)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.Number,boolean,java.lang.Object)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,int,boolean)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 boolean isReplace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,int,boolean,java.lang.Object)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 boolean isReplace,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,boolean)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,boolean,java.lang.Object)">writeObjectsToSpreadSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write the fUML runtime value to the Excel file.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>ExcelHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExcelHelper</span><wbr/><span class="parameters">(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="block">constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the running session.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>ExcelHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExcelHelper</span><wbr/><span class="parameters">(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> scriptContainer)</span></div>
<div class="block">constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the running session.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(fUML.Semantics.Classes.Kernel.Object_)">
<h3>ExcelHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExcelHelper</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.Object_ context)</span></div>
<div class="block">constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - the context of caller</dd>
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
<section class="detail" id="getLatestRowNum(java.lang.String,java.lang.String)">
<h3>getLatestRowNum</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLatestRowNum</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName)</span></div>
<div class="block">Get the latest row number of the sheet in the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dt>Returns:</dt>
<dd>the latest row number of the sheet in the Excel file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,int)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,java.lang.Number)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,int,java.lang.Object)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Object)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,java.lang.String,int)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,java.lang.String,int,java.lang.Object)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Object)">
<h3>readObjectFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the index of row</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,int,int)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int startRow,
 int endRow)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>startRow</code> - the start row number</dd>
<dd><code>endRow</code> - the end row number</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Number)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>startRow</code> - the start row number</dd>
<dd><code>endRow</code> - the end row number</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.Number,java.lang.Number,java.lang.Object)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>startRow</code> - the start row number</dd>
<dd><code>endRow</code> - the end row number</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.String,int,int)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int startRow,
 int endRow)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>startRow</code> - the start row number</dd>
<dd><code>endRow</code> - the end row number</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>startRow</code> - the start row number</dd>
<dd><code>endRow</code> - the end row number</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.Object)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList for all rows in excel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.String)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList for all rows in excel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>name</code> - the name of Mapping Class or sheet name.</dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Object)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList for all rows in excel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number,java.lang.Object)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> startRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> endRow,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>startRow</code> - the start row number</dd>
<dd><code>endRow</code> - the end row number</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readObjectsFromSpreadSheet(java.lang.String,java.lang.String,int,int,java.lang.Object)">
<h3>readObjectsFromSpreadSheet</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">readObjectsFromSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int startRow,
 int endRow,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Read the Excel file and create the fUML ValueList.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>startRow</code> - the start row number</dd>
<dd><code>endRow</code> - the end row number</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Returns:</dt>
<dd>the fUML ValueList of the data in the Excel file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - could be thrown if problem occurs when reading excel data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCellValue(java.lang.Object,java.lang.String,java.lang.String,int,int)">
<h3>setCellValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCellValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 int atCol)</span></div>
<div class="block">Set fUML runtime value to specific row and column in the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row index number</dd>
<dd><code>atCol</code> - the column index number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCellValue(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,java.lang.Number)">
<h3>setCellValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCellValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atCol)</span></div>
<div class="block">Set fUML runtime value to specific row and column in the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row index number</dd>
<dd><code>atCol</code> - the column index number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellValue(java.lang.String,java.lang.String,int,int)">
<h3>getCellValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getCellValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 int atCol)</span></div>
<div class="block">get value by specific row and column in the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row index number</dd>
<dd><code>atCol</code> - the column index number</dd>
<dt>Returns:</dt>
<dd>the value of cell</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellValue(java.lang.String,java.lang.String,java.lang.Number,java.lang.Number)">
<h3>getCellValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getCellValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atCol)</span></div>
<div class="block">get value by specific row and column in the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row index number</dd>
<dd><code>atCol</code> - the column index number</dd>
<dt>Returns:</dt>
<dd>the value of cell</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,int)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Number)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,int)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,java.lang.Number)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,int,java.lang.Object)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int rowIndex,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Number,java.lang.Object)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,java.lang.Number,java.lang.Object)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> rowIndex,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updatefUMLValueFromSpreadSheet(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.String,int,java.lang.Object)">
<h3>updatefUMLValueFromSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updatefUMLValueFromSpreadSheet</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int rowIndex,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">update the value of SpreadSheet to fUML runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the runtime object</dd>
<dd><code>fileName</code> - the spreadSheet file path</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>rowIndex</code> - the row index</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,int,boolean,java.lang.Object)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int atRow,
 boolean isReplace,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.Number,boolean,java.lang.Object)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,int,boolean)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 boolean isReplace)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,boolean)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,int,boolean)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 int atRow,
 boolean isReplace)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.Number,boolean)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,java.lang.Number,boolean,java.lang.Object)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> atRow,
 boolean isReplace,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeObjectsToSpreadSheet(java.lang.Object,java.lang.String,java.lang.String,int,boolean,java.lang.Object)">
<h3>writeObjectsToSpreadSheet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeObjectsToSpreadSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetName,
 int atRow,
 boolean isReplace,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> mappingClass)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Write the fUML runtime value to the Excel file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime value (ValueList/Value)</dd>
<dd><code>fileName</code> - the Excel file name</dd>
<dd><code>sheetName</code> - the sheet name</dd>
<dd><code>atRow</code> - the row number to write the data</dd>
<dd><code>isReplace</code> - if true, it will replace the existing data
                                        if false, it will insert the data at atRow</dd>
<dd><code>mappingClass</code> - the mapping class name <code>String</code> or mapping class <code>Element</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
