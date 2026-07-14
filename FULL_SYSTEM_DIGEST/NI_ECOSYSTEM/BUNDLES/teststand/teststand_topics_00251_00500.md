# NI DOCUMENT BUNDLE: teststand

<!--NI_BUNDLE_CHUNK bundle=teststand start=251 end=500 -->
<!--NI_TOPIC bundle=teststand path=customizing-the-tools-menu.html language=enus -->
## TOPIC 00251: Customizing the Tools Menu

- bundle_id: `teststand`
- source_path: `customizing-the-tools-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-tools-menu.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Tools menu in the TestStand Sequence Editor and User Interfaces contains common tools for use with TestStand. You can modify the Tools menu to contain exactly the tools you need, and you can also use the Customize Tools Menu dialog box to add new items to the Tools menu.

### Customizing the Tools Menu

The Tools menu in the TestStand Sequence Editor and User Interfaces contains common tools for use with TestStand. You can modify the Tools menu to contain exactly the tools you need, and you can also use the Customize Tools Menu dialog box to add new items to the Tools menu.

Parent topic:

Extending TestStand

<!--NI_TOPIC bundle=teststand path=customizing-the-uut-report-header-atml-2.html language=enus -->
## TOPIC 00252: Customizing the UUT Report Header for an ATML Test Results 2.02 Report

- bundle_id: `teststand`
- source_path: `customizing-the-uut-report-header-atml-2.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-uut-report-header-atml-2.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a row in the header of a report that uses the TR_horizontal.xsl report style sheet to display the ID of the result set the report contains. Open the TR_horizontal.xsl file. Search for the CREATE_UUTHEADER_INFO comment and uncomment the following table row code tha

### Customizing the UUT Report
 Header for an ATML Test Results 2.02 Report

Complete the following steps to add a row in
 the header of a report that uses the
 TR_horizontal.xsl report style
 sheet to display the ID of the result set the
 report contains.

1. Open the TR_horizontal.xsl 
 file.
2. Search for the
 CREATE_UUTHEADER_INFO comment and uncomment the following table row
 code that appears after the
 comment: <tr level="0">
 <td>
 <font size="1"><b>ResultSet ID</b></font>
 </td>
 <td>
 <xsl:value-of select="n1:ResultSet/@ID"/>
 </td>
</tr>

The expression
 "n1:ResultSet/@ID" specifies the
 XPath expression to obtain the result set ID from
 the XML file. You must customize the XPath
 expression to match the data you want to add to
 the additional rows. Refer to the World Wide Web
 Consortium (W3C) website, located at
 www.w3.org, for more information
 about XPath.

Parent topic:

Customizing the ATML Test Results 2.02 Report Style Sheet

<!--NI_TOPIC bundle=teststand path=customizing-the-uut-report-header-for-an-atml.html language=enus -->
## TOPIC 00253: Customizing the UUT Report Header for an ATML Test Results 6.01 or 5.0 Report

- bundle_id: `teststand`
- source_path: `customizing-the-uut-report-header-for-an-atml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-uut-report-header-for-an-atml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a row in the header of a report to display the ID of the result set the report contains. Open the .xsl file. Search for the CREATE_UUTHEADER_INFO comment and uncomment the following table row code that appears after the comment:<tr> <td> ResultSet ID </td> <td> <x

### Customizing the UUT Report Header for an
 ATML Test Results 6.01 or 5.0 Report

Complete the following steps to add a
 row in the header of a report to display the ID of the result set the report
 contains.

1. Open the .xsl file.
2. Search for the CREATE_UUTHEADER_INFO comment and uncomment the
 following table row code that appears after the
 comment: <tr>
 <td>
 ResultSet ID
 </td>
 <td>
 <xsl:value-of select="tr:ResultSet/@ID"/>
 </td>
</tr>

The expression "tr:ResultSet/@ID" specifies the XPath expression to
 obtain the result set ID from the XML file. You must customize the XPath expression to match
 the data you want to add to the additional rows. Refer to the World Wide Web Consortium
 (W3C) website, located at www.w3.org, for more information about
 XPath.

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

<!--NI_TOPIC bundle=teststand path=customizing-the-uut-report-header-in-an-xml-r.html language=enus -->
## TOPIC 00254: Customizing the UUT Report Header in an XML Report

- bundle_id: `teststand`
- source_path: `customizing-the-uut-report-header-in-an-xml-r.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-uut-report-header-in-an-xml-r.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add columns and corresponding data to the UUT Report header in reports that use the horizontal.xsl. You can add rows and corresponding data to the UUT Report header in reports that use the report.xsl or expand.xsl. Complete the following steps to add extra columns or rows to the report heade

### Customizing the UUT Report Header in an XML Report

You can add columns and corresponding data to the UUT Report header in reports that use the horizontal.xsl. You can add rows and corresponding data to the UUT Report header in reports that use the report.xsl or expand.xsl.

Complete the following steps to add extra columns or rows to the report header.

1. Open the .xsl file you want to change.
2. Complete the following steps in the horizontal.xsl , report.xsl , and expand.xsl files to create an extra column and the corresponding data in the UUT header table to show the type of report generated.
  1. Search for the CREATE_UUTHEADER_INFO comment.
  2. Remove the comment tags from around the following code that appears after the
 CREATE_UUTHEADER_INFO comment:
 <tr valign="top">
 <td style="white-space:nowrap">
 <span style='font-size:0.6em'>
 <b>Type of Report</b>
 </span>
 </td>
 <td style='white-space:nowrap'>
 <span>
 <xsl:attribute name="style">font-size:0.6em;</xsl:attribute>
 <xsl:value-of select="@Type"/>
 </span>
 </td>
</tr>

#### horizontal.xsl

The following figure shows a modified report header showing the report type using horizontal.xsl:

[IMAGE alt='image' src='GUID-EBBF3229-42B8-458B-B0E4-D6C029AE762D-a5.png']

#### report.xsl

The following figure shows a modified report header showing the report type using report.xsl:

[IMAGE alt='image' src='GUID-D33242CD-0D07-480E-B2CE-2E703FF728D5-a5.png']

#### expand.xsl

The following figure shows a modified report header showing the report type using expand.xsl:

[IMAGE alt='image' src='GUID-649CC6EC-85D3-4E74-99F4-3C1BB37F6325-a5.png']

Parent topic:

Customizing XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=customizing-toolbars-and-menus.html language=enus -->
## TOPIC 00255: Customizing TestStand Sequence Editor Toolbars and Menus

- bundle_id: `teststand`
- source_path: `customizing-toolbars-and-menus.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-toolbars-and-menus.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default toolbars and menus in the TestStand Sequence Editor are fully customizable. You can rearrange top-level menus and toolbar items within a toolbar by holding down the <Alt> key and dragging the menu or toolbar command to a new location. Select View»Reset UI Configuration at any time to r

### Customizing TestStand Sequence Editor
 Toolbars and Menus

The default toolbars and menus in the TestStand Sequence Editor are fully customizable.

Note

The Customize dialog box contains the following tabs:

- Toolbars —Controls the visibility of toolbars, creates new
 toolbars, and resets the commands available in toolbars.
- Commands —The available commands for menus and toolbars. You
 can drag and drop commands from the Commands tab to menus or toolbars to the menus
 and toolbars in the main application. You can also remove a command from a menu or
 toolbar by dragging the command from the main application and dropping it in the
 Commands control. You can also drag and drop commands between toolbars and menus
 to rearrange the order of toolbars and menus. Select
 Rearrange to launch the Rearrange Commands dialog
 box, in which you can add, delete, and rearrange the commands within menus and
 toolbars.
- Options —Specifies whether the sequence editor personalizes
 menus and toolbars, shows icons for menus and toolbars, shows toolbar tips, and if
 toolbar animation is enabled.

Keyboard

Note

When the Customize dialog box is visible, you can also right-click a menu, a menu
 command, or a toolbar command to display a context menu for customizing the appearance
 of a command.

Parent topic:

TestStand Sequence Editor

<!--NI_TOPIC bundle=teststand path=customizing-xml-report-style-sheets.html language=enus -->
## TOPIC 00256: Customizing XML Report Style Sheets

- bundle_id: `teststand`
- source_path: `customizing-xml-report-style-sheets.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-xml-report-style-sheets.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a text editor to customize an XML report style sheet in the following ways: Add columns and rows to reports Add images and text to headers and footers Add Sequence Call step results to reports without indentation Change the display format of execution time Customize the UUT Report header

### Customizing XML Report Style Sheets

You can use a text editor to customize an XML report style sheet in the following ways:

- Add columns and rows to reports
- Add images and text to headers and footers
- Add Sequence Call step results to reports without indentation
- Change the display format of execution time
- Customize the UUT Report header
- Exclude results from reports based on step properties
- Modify table cell background color based on step status
- Render HTML elements and new line characters in reports

Note

<TestStand>\Components\Models\TestStandModels\StyleSheets

<TestStand Public>\Components\Models\TestStandModels\StyleSheets

Style Sheet

Parent topic:

XML Report Style Sheets

Related concepts:

- XML Report Style Sheets
- Adding Columns and Rows to an XML Report
- Adding Images and Text to an XML Report Header or Footer
- Adding Sequence Call Step Results to an XML Report without Indentation
- Changing the Display Format of Execution Time in an XML Report
- Customizing the UUT Report Header in an XML Report
- Excluding Results from an XML Report Based on Step Properties
- Modifying Cell Background Color Based on Step Status in an XML Report
- Rendering HTML Elements and New Line Characters in an XML Report
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=data-links.html language=enus -->
## TOPIC 00257: Data Links

- bundle_id: `teststand`
- source_path: `data-links.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/data-links.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must define a data link when you specify the database where TestStand logs results or when you use the Database step types. Use the Data Link Properties dialog box to create or edit a data link connection string and to specify initialization properties for an Object Linking and Embedding Databas

### Data Links

You must define a data link when you specify the database where TestStand logs results or when you use the Database step types. Use the Data Link Properties dialog box to create or edit a data link connection string and to specify initialization properties for an Object Linking and Embedding Database (OLE DB) provider.

For example, to connect to a Microsoft SQL Server database, specify the Object Linking and Embedding Database (OLE DB) provider for an SQL Server, a server name, a database name, a user ID, and a password. To connect to a Microsoft Access database, specify Microsoft Jet in 32-bit TestStand and Microsoft ACE OLE DB in 64-bit TestStand or specify the OLE DB provider for Open Database Connectivity (ODBC) and an ODBC data source name. The ODBC data source name specifies which ODBC driver to use, the database file (.mdb), and an optional user ID and password. Use the ODBC Administrator on the Windows Control Panel to define ODBC data source names.

Note

A connection string is a string version of the connection information in the data link required to open a session to a database. Use the Data Link Properties dialog box to build a connection string. The Data Link Properties dialog box and the information contained in the connection string vary according to the OLE DB provider. For example, a connection string for an SQL Server database might contain the following information:

Provider=SQLOLEDB.1;Integrated Security=SSPI;Persist Security Info=True;User ID=guest;Initial Catalog=pubs;Data Source=SERVERCOMPUTER

Complete the following steps to store the contents of a connection string in a Microsoft Data Link file (.udl).

1. Create a Data Link file by right-clicking in Windows Explorer and selecting New»Text Document .
2. Change the file extension to .udl .
3. Right-click the new file and select Open to launch the Data Link Properties dialog box.
4. Click the Connection tab and enable the Use connection string option.
5. Click the Build button to launch the Select Data Link dialog box, in which you can build a connection string. When you finish, click OK to close the Select Data Link dialog box.
6. Use the other options on the Provider, Connection, Advanced, and All tabs to provide additional configuration information for the .udl file.
7. Click OK to close the Data Link Properties dialog box. The .udl file automatically saves when you exit the dialog box.

Parent topic:

Database Logging

Related concepts:

- Data Links

<!--NI_TOPIC bundle=teststand path=data-types.html language=enus -->
## TOPIC 00258: Data Types

- bundle_id: `teststand`
- source_path: `data-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/data-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you insert variables, parameters, or step properties, you can select a data type to use for the item. You can also create and modify custom data types to meet the needs of an application.

### Data Types

When you insert variables, parameters, or step properties, you can select a data type to use for the item. You can also create and modify custom data types to meet the needs of an application.

Parent topic:

Extending TestStand

Related concepts:

- Modifying Type Instances, Values, and Type Definitions
- Creating Custom Data Types
- Type Concepts

<!--NI_TOPIC bundle=teststand path=database-known-issues.html language=enus -->
## TOPIC 00259: Database Known Issues

- bundle_id: `teststand`
- source_path: `database-known-issues.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/database-known-issues.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following issues when you use a database management system with TestStand: On 64-bit Windows operating systems, the Data Sources (ODBC) application in the Windows Control Panel is the 64-bit version of the application, located at C:\Windows\system32\odbcad32.exe. NI recommends that you

### Database Known Issues

Consider the following issues when you use a database management system with TestStand:

- On 64-bit Windows operating systems, the Data Sources (ODBC) application in the Windows Control
 Panel is the 64-bit version of the application, located at
 C:\Windows\system32\odbcad32.exe . NI recommends that you
 use the 32-bit version of the OBDC application, located at
 C:\Windows\SysWOW64\odbcad32.exe to create any system DSNs
 for use in 32-bit TestStand. If you create a system DSN using the 64-bit
 version, the ODBC application creates a 64-bit DSN. If you create a system DSN
 using the 32-bit version, the ODBC application creates a 32-bit DSN. If you
 attempt to use system data links from the 32-bit TestStand Database Options
 dialog box or the Database Viewer, TestStand launches the 32-bit version of the
 Data Link Properties dialog box, which cannot display 64-bit system DSNs. User
 defined DSNs can be configured from the 32-bit version or the 64-bit version of
 the Data Sources (ODBC) application. If you attempt to use data links from the
 Database Options dialog box or the Database Viewer, the Data Link Properties
 dialog box matching TestStand’s bitness will be launched. A 32-bit or 64-bit
 version of this dialog can only display 32-bit or 64-bit DSNs respectively.
 Therefore, ensure that the DSNs are configured in the correct version of Data
 Sources (ODBC) application for it to be visible from TestStand

[IMAGE alt='image' src='GUID-1F1850A5-1203-4D53-9806-2E18FF24C32B-a5.png'] Microsoft Access
 Issues

- You must enable the Share Data Link Between Executions option on the Database Options dialog box to eliminate possible contention for access to a shared database file from multiple executions, and when you enable more than one database result processing plug-ins in the Result Processing dialog box.
- TestStand 3.5 or later includes a workaround for incorrect database logging when using the Microsoft Jet Provider 4.0. The Microsoft Jet Provider 3.51 and 4.0 incorrectly swap the month and day numeric components under the following conditions: For example, when TestStand logs the value January 13, 2012, the Microsoft Jet Provider stored date is correct. However, when TestStand logs the value January 12, 2012, the Microsoft Jet Provider stored date is December 1, 2012.
  - The Regional Options on the Microsoft Windows Control Panel specify a locale with a default date format that shows the day before the month
  - The TestStand Database Options data link uses the Microsoft Jet 3.51 or 4.0 Provider
  - The TestStand Database Options schema uses parameterized INSERT statements and includes a column defined with a Date data type
  - The day in the date falls between the 1st and the 12th of the month.
- The Database Viewer application fails to view data inside a Microsoft Access database when the data link uses the Microsoft Open Database Connectivity (ODBC) Driver and the base filename contains a period character in addition to the period in the file extension. This error appears to be a problem with the Microsoft ODBC Driver. This error may make the Database Viewer application unstable. Rename the database file or use the Microsoft Jet 4.0 Object Linking and Embedding (OLE) DB Provider instead.
- When the Microsoft Access ODBC Driver and Jet Provider return the error Operation cancelled , verify that the ODBC data source or data link connection string references a valid .mdb file.
- The Microsoft Jet 4.0 OLE DB Provider and ODBC Driver might return an error message when more than one execution or thread attempts to gain write access to the same table because executions and threads do not share handles when opening unique connections to the database or executing unique statements on a table. The Access drivers use an on-demand file access method that can cause this error. Take one of the following actions to resolve this issue:
  - When this error occurs while using the TestStand database logging feature from within a single process, enable the Share Data Link Between Executions option on the Data Link tab of the Database Options dialog box.
  - When this error occurs while accessing an Access database from multiple processes or different computers, ignore the error or retry the failing database action.
  - In some cases, when you open the statement recordset using the Batch Optimistic Locking option,
 the problem might not occur.
- When you use the Microsoft Access ODBC Driver, values for the STEP_TYPE field in the STEP_RESULT table might be NULL because MDAC sets the values for a MEMO field to NULL for all records when the value of the first record written is not specified. By default, the script files used to create the table attempt to create TEXT fields. When the tables are created with the Access ODBC driver, the field type is TEXT of size 255. When the tables are created with the Access OLE DB Provider, the field type is MEMO. Complete one of the following actions to resolve this issue:
  - Use the Microsoft Jet 4.0 OLE DB Provider instead of the Access ODBC driver to log results.
  - Change the field types in the STEP_RESULT and UUT_RESULT tables from MEMO to TEXT within Access. A message warns you that data could be truncated to 255 characters, which is the limit of a TEXT field.

[IMAGE alt='image' src='GUID-1F1850A5-1203-4D53-9806-2E18FF24C32B-a5.png'] MySQL Issues

- The MySQL ODBC drivers incorrectly report a catastrophic failure error when you specify a connection string that includes the "Initial Catalog=xxx" parameter. Specify the default database in the ODBC data source using the ODBC Administrator to resolve this issue.
- When you use the MySQL ODBC driver and the operating computer specifies a comma character as the decimal symbol character, the ODBC driver might return an error because the ODBC driver internally converts a floating-point value to a string value. The computer locale causes MySQL to interpret the comma decimal symbol character in the SQL syntax as a multi-value list character separator. Configure the MySQL data source in the ODBC Administrator and enable the Don't Use Set Locale option in the Miscellaneous Options section to resolve this error.
- The MySQL ODBC driver returns an error while logging results to a database when you specify column data type as String (BSTR) because the MySQL ODBC driver fails to encapsulate string values in quotation marks when constructing SQL statements. Specify string columns as String (varchar) instead.
- The MySQL ODBC driver returns an error while logging results to the database when the schema in the Database Options dialog box specifies a column data type as GUID . Specify string columns as String (varchar) instead.
- The MySQL ODBC 3.51 driver ignores the initial catalog setting specified in this dialog box or the Database Viewer application. You must specify the database in the ODBC connection string or in the DSN specified in the ODBC Administrator.
- The MySQL ODBC 3.51 driver might return an error when the Database Viewer application attempts to view a different database when you change the name in the Catalog ring control. The MySQL ODBC driver internally fails to properly terminate the string that contains the database name, which causes extra characters to appear on the end of the database name.
- The MySQL ODBC 3.51 driver does not permit the creation of new empty records when using a SELECT statement. When you attempt to use the On-The-Fly Database Logging option with schemas that use SELECT statements, the MySQL database returns the following error: Empty row cannot be inserted. Row must have at least one column value set.
- Enable the Don't Optimize Column Width option when you configure the DSN in the ODBC Administrator dialog box to prevent the MySQL ODBC 3.51 driver from returning the Operation is not allowed in this context (-2146825069) error when logging data to a binary field.
- When you perform a validate operation, the MySQL ODBC 3.51 driver incorrectly returns a maximum length of 64,000 for LONGBLOB or MEDIUMBLOB columns.
- NI recommends not using the Fetch Record by Index operation mode of the Data Operation database
 step type when reading a table with a VARCHAR field. In cases where multiple
 VARCHAR fields exist in the database and the Fetch Record By Index operation
 executes multiple times, a System Level Exception might occur. Instead, use the
 Next – Fetch Next Record operation to step through records in the table or use
 the Fetch Record by Index operation if the offset from the current record to the
 record index is small.
- A MySQL connection string requires that you specify the Initial or Default schema to which you are connecting. If this field is not specified or left empty in the connection string, Memory Access Violation errors occur when you connect to MySQL using the Database Viewer the MySQL ODBC Driver version 5.2 or later, for example, Driver={MySQL ODBC 5.2 ANSI Driver};Server=servname;Database=TSInsert;User=tester;Password=secret;Option=259; .
- MySQL returns Access Violation errors when retrieving metadata on the database schema if there are no relevant objects to retrieve. For example, if the application attempts to fetch the list of views in a MySQL schema and no views are defined, an Access Violation error occurs. You can ignore this error with no negative consequences.
- MySQL returns a MySQL server has gone away error when when using MySQL for database logging, the On-The-Fly Reporting option is enabled, and you run the sequence using the batch or parallel model.

[IMAGE alt='image' src='GUID-1F1850A5-1203-4D53-9806-2E18FF24C32B-a5.png'] SQL Server Issues

- Memory usage can increase when using the SQL Server Stored Proc schema and the database connection string uses the Microsoft OLE DB Provider for SQL Server. The memory usage appears to oscillate but shows growth over time. Use the Microsoft SQL Native Client database provider to avoid this issue.

[IMAGE alt='image' src='GUID-1F1850A5-1203-4D53-9806-2E18FF24C32B-a5.png'] Oracle Issues

- Use MDAC 2.7 with Oracle to prevent error -2147217915, which occurs when you execute the stored procedure for the STEP_RESULT schema statement.
- When you use an Oracle stored procedure to log data to a foreign key column that uses the GUID type and the data type of the parameter in the database logging schema is GUID, Oracle returns error -2147467259 when no value or NULL is assigned to the parameter. Change the data type from GUID to String for the foreign key parameter in the schema to resolve this issue.
- The Database Viewer application cannot show the contents of an Oracle database table when the table contains a LONG column. The Microsoft data grid control returns an "Object is open" error.
- Oracle recommends using Oracle Provider 11.1.0.6.0 or later if you want to read64-bit integer values stored in NUMBER columns.
- When you enable the Share Data Link Between Execution option and multiple executions simultaneously log binary data to a BLOB column in an Oracle database, Oracle can return the error "ORA-22990: LOB locators cannot span transactions." Disable the Share Data Link Between Execution option or enable the Use Transaction Processing option to prevent this error.
- When you use the Oracle ODBC Driver with server-side cursors to log data in TestStand with
 On-The-Fly logging enabled, the Oracle ODBC driver fails to return a proper key
 value for a parent provisional result of a Sequence Call step. Consequently,
 TestStand cannot update the fields of the parent provisional result and instead
 creates a new Sequence Call step result, and the foreign keys values for the
 steps in the called sequence incorrectly reference the empty provisional result.
 To work around this limitation of the Oracle driver, configure statements to use
 client-side cursors for the schema in the Statements tab of the Database Options
 dialog box. NI recommends using the Oracle OleDB provider with server-side
 cursors to avoid this issue with the Oracle ODBC Driver.

[IMAGE alt='image' src='GUID-1F1850A5-1203-4D53-9806-2E18FF24C32B-a5.png'] Sybase Issues

- The Sybase Adaptive Server Anywhere ODBC and OLE DB Provider do not store string data properly into a column when logging results to database when you specify the column data type as String (BSTR) . Specify string columns as String (varchar) instead.

Parent topic:

Database Logging

Related concepts:

- STEP_RESULT Table Schema
- UUT_RESULT Table Schema
- On-the-Fly Database Logging
- ODBC Data Source Administrator Dialog Box

<!--NI_TOPIC bundle=teststand path=database-logging.html language=enus -->
## TOPIC 00260: Database Logging

- bundle_id: `teststand`
- source_path: `database-logging.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/database-logging.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand can automatically log results from executions to a database and provides built-in step types for accessing databases directly from test sequences. The database logging capability is not native to the TestStand Engine or the TestStand Sequence Editor. The NI_DatabaseLogger.seq process model

### Database Logging

TestStand can automatically log results from executions to a database and provides built-in step types for accessing databases directly from test sequences.

The database logging capability is not native to the TestStand Engine or the TestStand Sequence Editor. The NI_DatabaseLogger.seq process model plug-in implements the database logging features. You can also customize or replace any portion of the database logging plug-in.

The default process model, which calls the Main sequence in the client sequence file to test a UUT, relies on the automatic result collection capabilities of the engine to accumulate the raw data to log to a database for each UUT. The engine automatically compiles the result of each step into a result list for an entire sequence, which contains the result of each step and the result list of each subsequence call it makes.

The Test UUTs and Single Pass Execution entry points in the TestStand process models log the raw results to a database. By default, the Test UUTs Execution entry point logs results after each pass through the UUT loop.

Select Configure»Result Processing to launch the Result Processing dialog box. Click the checkbox in the Enabled column of the Database row to enable database logging. Click the icon in the Options column to launch the Database Options dialog box, in which you can specify the following options:

- The data link connection string TestStand uses to log results.
- The database schema TestStand uses. A schema contains the SQL statements, table definitions, and TestStand expressions that instruct TestStand how to log results to a database. TestStand includes a set of predefined schemas, which contains at least one schema for each supported database management system. You can also create new schemas that log results to tables you define.
- Filtering options to limit the amount of data TestStand logs.
- If the process models log data after executing each step or after passing through each UUT loop.

Parent topic:

Fundamentals

Related concepts:

- Process Model Plug-In Architecture
- Process Model Architecture
- Result Collection
- Configuring Logging to Custom Database
- TestStand Database Fundamentals

<!--NI_TOPIC bundle=teststand path=database-sessions.html language=enus -->
## TOPIC 00261: Database Sessions

- bundle_id: `teststand`
- source_path: `database-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/database-sessions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Database operations occur within a database session. The lifetime of the session varies depending on the component connection to the database. Use the Database results processing plug-in to log execution results to a database. Use the Property Loader step type to import property and variable values

### Database Sessions

Database operations occur within a database session. The lifetime of the session varies depending on the component connection to the database. Use the Database results processing plug-in to log execution results to a database. Use the Property Loader step type to import property and variable values from a file or database during an execution. Use a code module or the built-in Database step types to communicate with a database.

A simple database operation includes the following steps:

1. Use the Open Database step type to connect to a database.
2. Use the Open SQL Statement step type to perform an SQL query on tables in the database.
3. Use Data Operation step types to create new records and to retrieve and update existing records.
4. Use the Close SQL Statement step type to close the SQL query.
5. Use the Close Database step type to disconnect from a database.

Right-click the Database step and select Edit <step type> from the context menu to configure the step type and to set the custom step properties. You can also click the Edit <step type> button on the edit tab of the Step Settings pane.

Parent topic:

TestStand Database Fundamentals

<!--NI_TOPIC bundle=teststand path=database-step-types.html language=enus -->
## TOPIC 00262: Database Step Types

- bundle_id: `teststand`
- source_path: `database-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/database-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Database step types to delete and create tables in a database, as well as how to modify the records in the database. Example File Location <TestStand Public>\Examples\Built-In Step Types\Database Step Types\Database Step Types.seq Highlighted Features

### Database Step Types

#### Purpose

This example demonstrates how to use the Database step types to delete and create tables in a database, as well as how to modify the records in the database.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Database Step Types\Database
 Step Types.seq

#### Highlighted Features

Database step types

#### Major API

None

#### Prerequisites

(32-bit
 TestStand) You must have the Microsoft Jet 4.0 Object Linking and Embedding Database
 (OLE DB) Provider installed. (64-bit TestStand) You must have the Microsoft Access
 Database Engine 2010 Redistributable installed. Visit ni.com/info
 and enter the Info Code 64TSaccdb to access the NI support article,
 Using Microsoft Access Databases with 64-bit TestStand, for more information about
 installing this provider.

#### How to Use This Example

Complete the following steps to use this example.

1. Review the following steps in the MainSequence :
  1. The Find Access MDB File step, which is a Statement step, attempts to locate the Microsoft Access database file ( .mdb ) and store its path in the MDBFilePath local variable.
  2. The Open Database step opens the database for use in TestStand, returns a handle, and stores the handle in the DatabaseHandle local variable.
  3. The Drop Table step, which is an Open SQL Statement step, drops the TEST_TABLE database table, if it exists.
  4. The Create Table step, which is an Open SQL Statement step, creates the TEST_TABLE table.
  5. The Open SQL Statement step selects all columns in the TEST_TABLE table.
  6. The SQL Action - Set Values step, which is a Data Operation step, adds data to the TEST_TABLE table and loops 10 times because the Goto step that follows the SQL Action - Set Values step targets the Start Loop step, which is a Label step, and specifies a post action and precondition that starts and stops the loop.
  7. The Start Loop 2 step starts a second loop that uses Data Operation steps to obtain the values and strings written to the TEST_TABLE table.
  8. The Cleanup step group contains Close SQL Statement and Close Database steps.
2. Select Execute»Single Pass to run the sequence.
3. When execution completes, select Tools»Database Viewer to launch the TestStand Database Viewer application.
4. Select File»Open , browse to <TestStand Public>\Examples\Database\Access.mdb , and click OK .
5. Right-click the TEST_TABLE table and select View Data from the context menu to display the data contained in the TEST_TABLE table.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- Databases and Tables
- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=database-viewer-application.html language=enus -->
## TOPIC 00263: Database Viewer Application

- bundle_id: `teststand`
- source_path: `database-viewer-application.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/database-viewer-application.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand includes the Database Viewer application for viewing data in a database, editing table information, and executing SQL commands. You can access the Database Viewer application in the following ways: Select Tools»Database Viewer in the TestStand Sequence Editor. (Windows 8.1) Click the NI La

### Database Viewer Application

TestStand includes the Database Viewer application for viewing data in a
 database, editing table information, and executing SQL commands.

You can access the Database Viewer application in the following ways:

- Select Tools»Database Viewer in the TestStand Sequence Editor.
- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»TestStand Database Viewer .
- (Windows 10 or 7) Select Start»All Programs»National Instruments»TestStand»Tools»TestStand Database Viewer .
- Run <TestStand>\Components\Tools\DatabaseView\DatabaseView.exe .
- Run <TestStand>\Components\Tools\DatabaseView\DatabaseView.exe from the command line.

The Database Viewer supports the following functionality:

- Database Explorer —The Database Explorer pane displays information about open database connections. You can view and edit data, add or remove database tables, and open or close database connections.
- Database Viewer Tabs —The Database Viewer contains Edit Data and Execute SQL tabs, which are associated with an open database connection. All operations performed in each tab execute on the database connection associated with that tab. The connection you select from the connection list when you create a tab becomes the connection associated with that tab.
- Binary Data Viewer —The Binary Data Viewer allows you to view binary data that has been logged to the database. You can view the data as a table, a graph, or as the layout in memory.

Note

- [Executing SQL Commands in the SQL Editor Window](executing-sql-commands-in-the-sql-editor-wind.html)
- [Customizing the Database Viewer User Interface](customizing-the-database-viewer-user-interfac.html)
- [Printing and Exporting Data in Database Viewer](printing-and-exporting-data-in-database-viewe.html)
- [Configuring Connection Strings](configuring-connection-strings.html)
- [Database Viewer Known Issues](database-viewer-known-issues.html)

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Search Directories
- Database Logging

Related information:

- Command Line Arguments
- Database Viewer Menu Bar

<!--NI_TOPIC bundle=teststand path=database-viewer-known-issues.html language=enus -->
## TOPIC 00264: Database Viewer Known Issues

- bundle_id: `teststand`
- source_path: `database-viewer-known-issues.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/database-viewer-known-issues.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following known issues exist for the Database Viewer application: Issues with Using the MSDASQL Provider in Database Viewer

### Database Viewer Known Issues

The following known issues exist for the Database Viewer application:

- Issues with Using the MSDASQL Provider in Database Viewer

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand path=databases-and-tables.html language=enus -->
## TOPIC 00265: Databases and Tables

- bundle_id: `teststand`
- source_path: `databases-and-tables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/databases-and-tables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A database is an organized collection of data, where you can store and retrieve information. Most modern database management systems (DBMSs), also known as database servers, store data in tables. Tables contain records, also known as rows. Each row contains fields, also known as columns. Every table

### Databases and Tables

A database is an organized collection of data, where you can store and retrieve information. Most modern database management systems (DBMSs), also known as database servers, store data in tables.

Tables contain records, also known as rows. Each row contains fields, also known as columns. Every table in a database must have a unique name, and every column within a table must have a unique name. Each column in a table has a data type, which varies depending on the DBMS. For example, the following table contains columns for the unit under test (UUT) number, a step name, a step result, and a measurement.

| UUT_NUM | STEP_NAME | RESULT | MEAS |
| --- | --- | --- | --- |
| 20860B456 | TEST1 | PASS | 0.5 |
| 20860B456 | TEST2 | PASS | (NULL) |
| 20860B123 | TEST1 | FAIL | 0.1 |
| 20860B789 | TEST1 | PASS | 0.3 |
| 20860B789 | TEST2 | PASS | (NULL) |

A row can contain an empty column value, which means the specific cell contains a NULL value, also referred to as an SQL NULL value.

The order of the data in the table is not important. Ordering, grouping, and other manipulations of the data occur when you retrieve the data from the table. Use an SQL SELECT command, or query, to retrieve records from a database. The query defines the content and order of the data you want to retrieve. The result of a query is called a recordset or SQL Statement data. You can retrieve certain columns and rows from one table, or you can retrieve data from multiple tables. You can refer to each column you retrieve by the name of the column or by a one-based number that refers to the order of the column in the query.

Parent topic:

TestStand Database Fundamentals

<!--NI_TOPIC bundle=teststand path=db-options-specify-data-link-schema.html language=enus -->
## TOPIC 00266: Database Options—Specifying a Data Link and Schema

- bundle_id: `teststand`
- source_path: `db-options-specify-data-link-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/db-options-specify-data-link-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure the database logging options. Launch the TestStand Sequence Editor and log in as Administrator. Select Configure»Result Processing to launch the Result Processing dialog box and click the icon in the Options column for the built-in database plug-in to launch

### Database Options—Specifying a Data Link and
 Schema

Complete the following steps to configure the database logging options.

1. Launch the TestStand Sequence Editor and log in as Administrator .
2. Select Configure»Result Processing to launch the Result
 Processing dialog box and click the icon in the Options column for the built-in database
 plug-in to launch the Database Options dialog box. The Logging Options tab is active.
3. Enable database logging by removing the checkmark in the Disable Database
 Logging option.
4. Click the Data Link tab of the Database Options dialog box.
5. Select Access from the Database Management System ring
 control.
6. Click the Build button to launch the Data Link Properties dialog
 box.
7. Select Microsoft Jet 4.0 OLE DB Provider on the Provider tab of
 the Data Link Properties dialog box if the 32-bit version of the application is running.
 If the 64-bit version of the application is running, select the Microsoft
 Office 12.0 Access Database Engine OLE DB Provider Visit
 ni.com/info and enter the Info Code 64TSaccdb to
 access the NI support article, Using Microsoft Access Databases with 64-bit TestStand, for
 more information about installing this provider..
8. Click Next .
9. On the Connection tab, click Browse to launch the Select Access
 Database dialog box. (32-bit TestStand) Using the Select Access Database dialog box,
 locate a Microsoft Access database file ( .mdb ) and click
 Open to select the file. (64-bit TestStand)Enter the path of the
 Microsoft Access database file ( .mdb ) in the Data Source control.
10. In the Data Link Properties dialog box, click the Test Connection 
 button to verify that you properly entered the required information.
11. Click OK to close the Data Link Properties dialog box.

Notice that the Connection String Expression in the Database Options dialog box now
 contains a literal string expression version of the data link connection string.

Parent topic:

Example Data Link and Result Table Setup for Microsoft Access

<!--NI_TOPIC bundle=teststand path=db-viewer-create-result-tables.html language=enus -->
## TOPIC 00267: Database Viewer—Creating Result Tables

- bundle_id: `teststand`
- source_path: `db-viewer-create-result-tables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/db-viewer-create-result-tables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create the default result tables in a database. If you are continuing from the steps in the Database Options—Specifying a Data Link and Schema section, skip to step 2. Otherwise, complete the following steps. Launch the TestStand Sequence Editor and log in as Administ

### Database Viewer—Creating Result
 Tables

Complete the following steps to create the default result tables in a database.

1. If you are continuing from the steps in the Database Options—Specifying a Data Link and
 Schema section, skip to step 2. Otherwise, complete the following steps.
  1. Launch the TestStand Sequence Editor and log in as
 Administrator .
  2. Select Configure»Result Processing to launch the Result
 Processing dialog box and click the icon in the Options column for the built-in
 database plug-in to launch the Database Options dialog box. The Logging Options tab is
 active.
  3. Enable database logging by removing the checkmark in the Disable Database
 Logging option.
  4. Click the Data Link tab of the Database Options dialog box.
2. Click the View Data button to launch the Database Viewer
 application and open the data link. Note The Connection String Expression must contain a valid expression to launch
 the Database Viewer application.
3. In the Database Viewer application, select File»Execute SQL
 Window to open an Execute SQL window.
4. Click the Load From SQL File button.
5. Select <TestStand>\Components\Models\TestStandModels\Database\Access Create
 Generic Recordset Result Tables.sql and click Open . Notice that the
 SQL Commands control now contains a set of SQL commands for creating the default result
 tables.
6. Click the Execute button to create the default result tables.
7. Review the results of the SQL commands on the Output tab to ensure that you created the
 tables successfully.
8. Click the Refresh button in the Database Explorer pane to view
 the created tables.

After you have completed these steps, any execution you launch with the Test UUTs or Single
 Pass Execution entry point automatically logs results to the database.

Parent topic:

Example Data Link and Result Table Setup for Microsoft Access

Related concepts:

- Database Options—Specifying a Data Link and Schema
- TestStand Directory Structure
- Entry Points

<!--NI_TOPIC bundle=teststand path=dcom-settings-for-a-local-client.html language=enus -->
## TOPIC 00268: DCOM Settings for a Local Client

- bundle_id: `teststand`
- source_path: `dcom-settings-for-a-local-client.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/dcom-settings-for-a-local-client.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure DCOM access permissions on the client computer. You must restart TestStand for these changes to take effect. Log in as a user with administrator privileges. Navigate to the standard Windows Control Panel facility for administrative tools and select Component

### DCOM Settings for a Local Client

Complete the following steps to configure DCOM access permissions on the client computer. You must restart TestStand for these changes to take effect.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for administrative tools and select Component Services or run dcomcnfg from the command line to launch the Component Services window.
3. On the left pane of the Component Services window, select Component Services»Computers»My Computer .
4. Right-click My Computer and select Properties to launch the My Computer Properties dialog box.
5. Click the COM Security tab of the My Computer Properties dialog box and complete the following steps to set permissions:
  1. Click the Edit Limits button in the Access Permissions section to launch the Access Permissions dialog box.
  2. Select ANONYMOUS LOGON in the user name list and enable Remote Access in the Permissions Section. If ANONYMOUS LOGON does not appear in the user name list, click the Add button to add it.
  3. Click OK to close the Access Permissions dialog box.

You must also disable DCOM authentication for the client application if it is not the TestStand Sequence Editor (SeqEdit.exe) or one of the TestStand User Interfaces named testexec.exe. For client applications built with LabVIEW, disable DCOM authentication for the application by adding the following line to the INI file associated with the application, as in yourclient.ini where yourclient.exe is the name of the application:ole.AuthnLevel=1

For all other client applications, disable DCOM authentication for the application by adding the following registry entry, where yourclient.exe is the name of your application:

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\yourclient.exe] "AppID" ="{C31FD07F-DEAC-4962-9BBF-092F0F3BFF3C}"

Parent topic:

Settings Windows System Security on a Local Client

<!--NI_TOPIC bundle=teststand path=dcom-settings-for-remote-servers.html language=enus -->
## TOPIC 00269: DCOM Settings for Remote Servers

- bundle_id: `teststand`
- source_path: `dcom-settings-for-remote-servers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/dcom-settings-for-remote-servers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable the Allow All Users Access From Remote Machines option on the Remote Execution tab of the Station Options dialog box to minimize the configuration of security permissions. (Windows 10/8.1/7) Windows launches a User Account Control elevation prompt for you to manually resolve when you enable t

### DCOM Settings for Remote Servers

Enable the Allow All Users Access From Remote Machines option on the Remote Execution tab of the Station Options dialog box to minimize the configuration of security permissions.

(Windows 10/8.1/7) Windows launches a User Account Control elevation prompt for you to manually resolve when you enable this option.

Note

When you enable the Allow All Users Access From Remote Machines option, TestStand configures the DCOM security permissions for you in the following ways:

- TestStand grants the Remote Launch and Remote Activation privileges to the Everyone and ANONYMOUS LOGON user names.
- TestStand changes the computer Component Object Model (COM) security limits to grant the Remote Launch, Remote Activation, and Remote Access privileges to the Everyone and ANONYMOUS LOGON user names.

In addition, when you enable the Allow All Users Access From Remote Machines option, the remote engine application overrides the application DCOM authentication level setting and does not authenticate connections. When you disable this option, TestStand revokes all the privileges listed previously, even if they were granted before the option was enabled.

When you do not enable the Allow All Users Access From Remote Machines option, complete the following steps to configure the DCOM security permissions for the server on a remote computer.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for administrative tools and select Component Services or run dcomcnfg from the command line to launch the Component Services window.
3. On the left pane of the Component Services window, select Component Services»Computers»My Computer .
4. Right-click My Computer and select Properties to launch the My Computer Properties dialog box.
5. On the Default Properties tab of the My Computer Properties dialog box, enable the Enable Distributed COM on this computer option. Note You must restart the computer for changes to the value of the Enable Distributed COM on this computer option to take effect.
6. Click the COM Security tab of the My Computer Properties dialog box and complete the following steps to set permissions.
  1. Click the Edit Limits button in the Access Permissions section to launch the Access Permission dialog box.
  2. Click Add to add the users for whom you want to grant remote access. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  3. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  4. Select the user you added and enable Remote Access in the Permissions section.
  5. Click OK to close the Access Permission dialog box.
  6. (Windows 10/8.1/7) Click the Edit Limits button in the Launch and Activation Permissions section to launch the Launch and Activation Permission dialog box.
  7. Click Add to add the users you want to give remote access to. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  8. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  9. Select the user you added and enable Remote Launch and Remote Activation in the Permissions section.
  10. (Windows 10/8.1/7) Click OK to close the Launch and Activation Permission dialog box. Note You can grant access permission to the remote computer to everyone but grant launch permissions only to appropriate users because launch permissions allow access to the TestStand server on the remote computer.
7. Click OK to close the My Computer Properties dialog box.
8. On the left pane of the Component Services window, select My Computer»DCOM Config to display a list of applications on the right pane.
9. Right-click NI TestStand Remote Engine and select Properties from the context menu to launch the NI TestStand Remote Engine Properties dialog box.
10. On the General tab of the NI TestStand Remote Engine Properties dialog box, set the Authentication Level to None if the user is not a domain account.
11. On the Identity tab of the NI TestStand Remote Engine Properties dialog box, select the This user option and enter a username and password or select the The interactive user option.
  - If you select the This user option, you must disable the Show the System Tray Icon While the TestStand Remote System is Active on this Machine option on the Remote Execution tab of the Station Options dialog box.
  - If you select the The interactive user option, a user must be logged in at the physical computer console during remote sequence execution. You can automatically log on a user each time a computer reboots by setting registry keys. Refer to Microsoft support article 315231 for more information about activating automatic logon. Note Regardless of whether you select the This user option or The interactive user option, the user account used on the remote computer must be an administrator account.
12. Click the Security tab of the NI TestStand Remote Engine Properties dialog box and complete the following steps to set permissions.
  1. (Windows 10/8.1/7) Select the Customize option and click the Edit button in the Launch and Activation Permissions section to launch the Launch and Activation Permission dialog box.
  2. Click Add to add the users for whom you want to grant remote access. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  3. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  4. Select the user you added and enable Remote Launch and Remote Activation in the Permissions section.
  5. (Windows 10/8.1/7) Click OK to close the Launch and Activation Permission dialog box.
  6. Select the Customize option and click the Edit button in the Access Permissions section to launch the Access Permission dialog box.
  7. Click Add to add the users for whom you want to grant remote access. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  8. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  9. Select the user you added and enable Remote Access in the Permissions section.
  10. Click OK to close the Access Permission dialog box.
13. Click OK to close the NI TestStand Remote Engine Properties dialog box.

Parent topic:

Setting Windows System Security on a Remote Server

Related concepts:

- Setting Windows System Security on a Remote Server

<!--NI_TOPIC bundle=teststand path=dcom-settings-for-the-local-computer-setting.html language=enus -->
## TOPIC 00270: DCOM Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `dcom-settings-for-the-local-computer-setting.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/dcom-settings-for-the-local-computer-setting.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure Distributed Component Object Model (DCOM) access permissions on the computer that accesses the synchronization object. You must restart TestStand for these changes to take effect. Log in as a user with administrator privileges. Navigate to the standard Windo

### DCOM Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Complete the following steps to configure Distributed Component Object Model (DCOM) access permissions on the computer that accesses the synchronization object. You must restart TestStand for these changes to take effect.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for administrative tools and select Component Services or run dcomcnfg from the command line to launch the Component Services window.
3. On the left pane of the Component Services window, select Component Services»Computers»My Computer .
4. Right-click My Computer and select Properties to launch the My Computer Properties dialog box.
5. Click the COM Security tab of the My Computer Properties dialog box and complete the following steps to set permissions.
  1. Click the Edit Limits button in the Access Permissions section to launch the Access Permissions dialog box.
  2. Select ANONYMOUS LOGON in the user name list and enable Remote Access in the Permissions Section. If ANONYMOUS LOGON does not appear in the user name list, click the Add button to add it.
  3. Click OK to close the Access Permissions dialog box.

You must also disable DCOM authentication for the client application if it is not the TestStand Sequence Editor (SeqEdit.exe) or one of the TestStand User Interfaces named testexec.exe. For client applications built with LabVIEW, disable DCOM authentication for the application by adding the following line to the INI file associated with the application, as in yourclient.ini where yourclient.exe is the name of your application:

ole.AuthnLevel=1

For all other client applications, disable DCOM authentication for the application by adding the following registry entry, where yourclient.exe is the name of your application:

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\yourclient.exe]"AppID" ="{C31FD07F-DEAC-4962-9BBF-092F0F3BFF3C}"

Parent topic:

Setting Up TestStand for Accessing Synchronization Objects Remotely

Related concepts:

- Effectively Using LabVIEW with TestStand

<!--NI_TOPIC bundle=teststand path=dcom-settings-for-the-remote-computer-setting.html language=enus -->
## TOPIC 00271: DCOM Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `dcom-settings-for-the-remote-computer-setting.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/dcom-settings-for-the-remote-computer-setting.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following information to configure the Distributed Component Object Model (DCOM) security permissions for the TSAutoMgr.exe server on the computer that creates the synchronization object. Complete the following steps to configure the DCOM security permissions. Log in as a user with administr

### DCOM Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Use the following information to configure the Distributed Component Object Model (DCOM) security permissions for the TSAutoMgr.exe server on the computer that creates the synchronization object.

Complete the following steps to configure the DCOM security permissions.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for administrative tools and select Component Services or run dcomcnfg from the command line to launch the Component Services window.
3. On the left pane of the Component Services window, select Component Services»Computers»My Computer .
4. Right-click My Computer and select Properties to launch the My Computer Properties dialog box.
5. On the Default Properties tab of the My Computer Properties dialog box, enable the Enable Distributed COM on this computer option.
 
 Note 

 You must restart the computer for changes to the value of the Enable Distributed COM on this computer option to take effect.
6. Click the COM Security tab of the My Computer Properties dialog box and complete the following steps to set permissions.
  1. Click the Edit Limits button in the Access Permissions section to launch the Access Permission dialog box.
  2. Click Add to add the users you want to give remote access to. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  3. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  4. Select the user you added and enable Remote Access in the Permissions section.
  5. Click OK to close the Access Permission dialog box.
  6. (Windows 10/8.1/7) Click the Edit Limits button in the Launch and Activation Permissions section to launch the Launch and Activation Permission dialog box.
  7. Click Add to add the users you want to give remote access to. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  8. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  9. Select the user you added and enable Remote Launch and Remote Activation in the Permissions section.
  10. (Windows 10/8.1/7) Click OK to close the Launch and Activation Permission dialog box.
7. Click OK to close the My Computer Properties dialog box.
8. On the left pane of the Component Services window, select My Computer»DCOM Config to display a list of applications on the right pane.
9. Right-click NI TestStand AutoMgr and select Properties from the context menu to launch the NI TestStand AutoMgr Properties dialog box.
10. On the General tab of the NI TestStand AutoMgr Properties dialog box, change the Authentication Level to None .
11. Click the Security tab of the of the NI TestStand AutoMgr Properties dialog box and complete the following steps to set permissions.
  1. (Windows 10/8.1/7) Select the Customize option and click the Edit button in the Launch and Activation Permission section to launch the Launch and Activation Permission dialog box.
  2. Click Add to add the users you want to give remote access to. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  3. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  4. Select the user you added and enable Remote Launch and Remote Activation in the Permissions section.
  5. (Windows 10/8.1/7) Click OK to close the Launch and Activation Permission dialog box.
  6. Select the Customize option and click the Edit button in the Access Permissions section to launch the Access Permission dialog box.
  7. Click Add to add the users you want to give remote access to. If the computer is not on a domain or the user is not a domain account, add the ANONYMOUS LOGON user.
  8. (Windows 10/8.1/7) Click OK to close the Select Users or Groups dialog box.
  9. Select the user you added and enable Remote Access in the Permissions section.
  10. Click OK to close the Access Permission dialog box.
12. On the Identity tab of the NI TestStand AutoMgr Properties dialog box,
 select the This user option and enter a user name and
 password or select the The interactive user option. Click
 OK to close the dialog box. If you select the
 The interactive user option, a user must be logged in at
 the physical computer console during remote sequence execution. You can
 automatically log on a user each time a computer reboots by setting registry keys.
 Refer to Microsoft support article 315231 for more information about activating
 automatic logon. Note 
 Regardless of whether you select the This user option
 or The interactive user option, the user account used on
 the remote computer must be an administrator account.

Parent topic:

Setting Up TestStand for Accessing Synchronization Objects Remotely

Related information:

- Turn on Automatic Logon in Windows

<!--NI_TOPIC bundle=teststand path=debug-python-modules.html language=enus -->
## TOPIC 00272: Debugging Python Modules

- bundle_id: `teststand`
- source_path: `debug-python-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debug-python-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can perform step into debugging operations on Python modules using the Python Adapter. Before you can step into Python modules, you must install the following software and configure the Python Adapter: Install the debugpy package in Python. Install Visual Studio Code. Select either User Installe

### Debugging Python Modules

You can perform step into debugging operations on Python modules using the Python
 Adapter.

1. Install the debugpy package in Python.
2. Install Visual Studio Code. Select either User Installer or System Installer
 from the download page. TestStand uses VS Code as the IDE for debugging Python
 modules.
3. Install NI TestStand Support for Debugging Python Code. This VS Code extension
 also installs the Python extension if your computer is connected to the
 internet. If the computer is not connected to the internet, you must install the
 Python extension for VS Code. If your computer had VS Code installed before
 installing TestStand, the TestStand installation process also installs the
 VS Code extension. In VS Code, confirm that NITestStand Support for
 Debugging Python Code is installed. Otherwise, complete the following
 steps:
  1. Launch the TestStand Version Selector.
  2. Under Installed TestStand Versions, select TestStand 2021 SP1 or later,
 then click Activate or
 Configure . The TestStand Version Selector
 performs the action of installing the extension when you activate
 TestStand 2021 SP1 or later. Note If you
 ever uninstall the extension, repeat this step to reinstall it.
4. Configure Workspace Trust in VS Code.
  1. Click Manage»Workspace Trust .
  2. Click Add Folder .
  3. Add C:\<My Documents>\TestStand\Python as a
 trusted folder. Note You may need to create the folder first.
5. Configure the Python Adapter for Debugging.
  1. In the TestStand Sequence Editor, click
 Configure»Adapters , select
 Python , and click
 Configure .
  2. Select the Enable Debugging option.
  3. Select Enable Just My Code to debug only your
 Python code and exclude installed libraries when debugging. Otherwise,
 deselect Enable Just My Code to debug both your
 Python code and any installed libraries your code imports.
  4. For the Executable Path option, browse to the
 location of python.exe you want to use to debug Python
 modules. The version number of the executable must match the version
 number in the Version option.

Complete the following steps to debug functions you call
 from TestStand using the Python Adapter.

1. Place a breakpoint at a step that calls a Python module.
2. Select Execute»Run MainSequence. The execution pauses at
 the Python step.
3. Click the Step Into button at the top of the Execution
 window. VS Code becomes the active application, in which the Python module is
 open and in a suspended state.
4. Click Step Into or Step Over on
 the VS Code toolbar to begin stepping through the function. You can click
 Continue at any time to finish stepping through the
 module and return to TestStand.
5. Click the Resume button on the Execution toolbar in
 TestStand to complete the execution.

Parent topic:

Python Adapter

#### Known Limitations of Python Step-Into
 Debugging

The following considerations are important to keep in mind when debugging Python
 modules.

- Sometimes VS Code will not come to front when you step into a Python module, but it
 will blink in the taskbar.
- You cannot step into set/get attributes.
- You cannot step into Python code if the step overrides Python Adapter settings.
- During debugging, if you come out from VS Code to TestStand by clicking step into or
 step over, VS Code stops when any additional Python code is executed, regardless of
 whether you step into that Python code from TestStand.

#### Attaching the Python Debugger to an External
 Process

Python code modules are executed in an external process on the system where the Python
 interpreter is hosted. You can attach the Python debugger to the external
 process.

| Python Version | Code |
| --- | --- |
| 3.6+ | import os import ctypes ctypes.windll.user32.MessageBoxW(None, "Process name: niPythonHost.exe and Process ID: " + str(os.getpid()), "Attach debugger", 0) |

A dialog box with the process name is displayed upon execution. Attach the Python
 debugger to the specified process and click OK to start
 debugging the code module in your debugger.

<!--NI_TOPIC bundle=teststand path=debugging-a-patch-deployment.html language=enus -->
## TOPIC 00273: Debugging a Patch Deployment

- bundle_id: `teststand`
- source_path: `debugging-a-patch-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-a-patch-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creating a patch deployment might require more care than creating a full deployment because the changes you include in a patch deployment might negatively affect files in the deployed test system on the test station computer. To avoid this situation, ensure that you correctly prepare the source comp

### Debugging a Patch Deployment

Creating a patch deployment might require more care than creating a full deployment because the changes you include in a patch deployment might negatively affect files in the deployed test system on the test station computer. To avoid this situation, ensure that you correctly prepare the source components for the patch deployment and that you analyze the test system before you create the deployment.

The TestStand Deployment Utility includes several errors and warnings specifically related to patch deployments.

Use the Build Status tab of the deployment utility to view information about the patch deployment, such as which files the patch deployment modifies or adds. The Patch Files tab of the Build Summary message in the Status Log includes specific information about all the files detected, whether the utility included the files, and the checksums used to compare against the previous versions of the files. If the Status Log indicates that the patch deployment does not include a file you expect it to, select View Build Preview in the View control on the Distributed Files tab of the deployment utility to verify that the correct source file is included. In addition, verify that the source file contains all changes made since the previous deployment.

Parent topic:

Patching Deployments

Related concepts:

- Preparing Source Components for Deployment
- Analyzing the Test System

<!--NI_TOPIC bundle=teststand path=debugging-analysis-and-rule-config-mods.html language=enus -->
## TOPIC 00274: Debugging Analysis Modules and Rule Configuration Modules

- bundle_id: `teststand`
- source_path: `debugging-analysis-and-rule-config-mods.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-analysis-and-rule-config-mods.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can debug your analysis modules and rule configuration modules by setting a breakpoint in the module and then calling the module from the TestStand Sequence Analyzer. Complete the following steps to debug an analysis module or rule configuration module, depending on the application you used to c

### Debugging Analysis Modules and Rule Configuration Modules

You can debug your analysis modules and rule configuration modules by setting a
 breakpoint in the module and then calling the module from the TestStand Sequence
 Analyzer. Complete the following steps to debug an analysis module or rule configuration
 module, depending on the application you used to create the module.

Parent topic:

TestStand Sequence Analyzer

Related information:

- Edit Analysis Module Dialog Box
- Edit Rule Dialog Box

#### Debugging Analysis Modules and Rule
 Configuration Modules in LabVIEW

1. Disable the Run VI in LabVIEW Run-Time Engine option on
 the Edit Analysis Module dialog box for an analysis module or on the Advanced
 tab of the Edit Rule dialog box for a rule configuration module.
2. Configure the LabVIEW Adapter to use the LabVIEW development system.
3. In LabVIEW, open the VI and set breakpoints in the block diagram for debugging.
 Refer to the LabVIEW Help for more information about using
 breakpoints.

#### Debugging Analysis Modules and Rule
 Configuration Modules in LabWindows/CVI

1. Build a debuggable DLL in LabWindows/CVI.
2. Set a breakpoint in the analysis module or rule configuration module
 function.
3. In LabWindows/CVI, select Run»Select External Process in
 the Project window to identify the executable for the sequence editor or the
 standalone sequence analyzer application and then select Run»Debug
 <executable name> to start debugging the executable.

#### Debugging Analysis Modules and Rule
 Configuration Modules in Microsoft Visual C# and Microsoft Visual C++

1. Build a debug version of the DLL in Microsoft Visual Studio.
2. Set a breakpoint in the analysis module or rule configuration module
 function.
3. In Visual Studio, set the Command setting in the Debugging project settings to
 the executable for the sequence editor or the standalone sequence analyzer
 application and select Debug»Start Debugging to start
 debugging the executable.

<!--NI_TOPIC bundle=teststand path=debugging-and-tracing-of-vis-executed-using-t.html language=enus -->
## TOPIC 00275: Debugging and Tracing of VIs Executed Using the LabVIEW Runtime

- bundle_id: `teststand`
- source_path: `debugging-and-tracing-of-vis-executed-using-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-and-tracing-of-vis-executed-using-t.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the LabVIEW Development System, you can debug VIs that execute using the LabVIEW Runtime in the TestStand Sequence Editor. Using the LabVIEW Desktop Execution Trace Toolkit (DETT), you can trace and capture events for VIs executed using the LabVIEW Runtime in the TestStand Sequence Editor and

### Debugging and Tracing of VIs Executed Using the LabVIEW Runtime

Using the LabVIEW Development System, you can debug VIs that execute using the LabVIEW Runtime in the TestStand Sequence Editor. Using the LabVIEW Desktop Execution Trace Toolkit (DETT), you can trace and capture events for VIs executed using the LabVIEW Runtime in the TestStand Sequence Editor and the TestStand User Interfaces on the local machine.

The LabVIEW Development System that debugs a VI code module must match the version and bitness of the LabVIEW Runtime that executed the VI code module. In LabVIEW, you can configure breakpoints and probes on diagrams to debug VIs that TestStand executes using the LabVIEW Runtime.

Using the DETT, you can capture and trace events, such as the order of VI execution, thread IDs, reference leaks, timing details, and user-defined trace information. Trace and event information can be helpful when diagnosing complex threading issues, identifying performance bottlenecks, and debugging other complex problems.

To enable debugging and tracing in TestStand, use the Enable Debugging and Tracing option in the LabVIEW Adapter Configuration dialog box.

Note

- Changes to the Enable Debugging and Tracing setting will not take effect until you restart a TestStand application.
- LabVIEW 2015 or later is required to debug and trace VIs executed in the LabVIEW Runtime.
- DETT 2015 or later is required to trace VIs executed in the LabVIEW Runtime.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Debugging Code Module VIs with LabVIEW
- Tracing with the DETT

<!--NI_TOPIC bundle=teststand path=debugging-code-module-vis-with-labview.html language=enus -->
## TOPIC 00276: Debugging Code Module VIs with LabVIEW

- bundle_id: `teststand`
- source_path: `debugging-code-module-vis-with-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-code-module-vis-with-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When executing your VIs in the LabVIEW Development System, you can debug your VIs using LabVIEW by setting breakpoints and probes in VIs being executed. The LabVIEW Development System can also debug applications that execute VIs using the LabVIEW Runtime, such as VIs executed using the TestStand Lab

### Debugging Code Module VIs with LabVIEW

When executing your VIs in the LabVIEW Development System, you can debug your VIs using LabVIEW by setting breakpoints and probes in VIs being executed. The LabVIEW Development System can also debug applications that execute VIs using the LabVIEW Runtime, such as VIs executed using the TestStand LabVIEW Adapter and LabVIEW-built DLLs executed using the TestStand C/C++ DLL Adapter. Refer to the LabVIEW Help for more information about debugging remote applications and VIs executed using the LabVIEW Runtime.

Complete the following steps to debug VIs when the TestStand Sequence Editor executes VIs using a LabVIEW Runtime:

1. Ensure that the Enable Debugging and Tracing option in the LabVIEW Adapter Configuration dialog box is enabled, and restart the TestStand Sequence Editor if required.
2. Ensure that you save all VIs you want to debug in the version of the LabVIEW development system you are using to debug the VIs.
3. Ensure that the LabVIEW code modules you want to debug are loaded into memory. You can load the modules by executing the sequence once, or by starting execution of the sequence if the modules are set to preload when execution begins.
4. In the LabVIEW Development System, open a debug connection to the TestStand Sequence Editor by selecting Operate»Debug Application or Shared Library to open the Debug Application or Shared Library dialog box. Set the Machine name or IP address to localhost , select seqEdit.exe in the Application or shared library option, and click Connect . LabVIEW opens a debug connection to the TestStand Sequence Editor and downloads the code module VIs for debugging. See the Debug Application or Shared Library Dialog Box topic in the LabVIEW Help for more information about this step.
5. In LabVIEW, add the required breakpoints and probes to the downloaded VIs to debug, then save the VI.
6. (Optional) View the VIs loaded for debugging using LabVIEW RTE Debugging Viewer.vi , located in <TestStand Public>/AdapterSupport/LabVIEW . When you launch this tool, it will display the VIs loaded in the debugging application instance. If no VIs are shown, you can use the Application to Debug menu to manually select the application instance you want to view. If none of the options contain seqEdit.exe , verify that the debug connection was successful.
7. Execute the TestStand sequence again to execute and debug the VIs. Once the TestStand execution reaches the VI, the first breakpoint will be triggered in a new instance of the VI. To add additional breakpoints or probes, add them to this instance of the VI.
8. To make changes to the VI after debugging, right-click on the front panel of the debugging instance of the VI and select Remote Debugging»Quit Debug Session .

Note

- This feature is only supported when executing VIs in the TestStand Sequence Editor.
- Step Into commands in TestStand are not supported when debugging VIs executing using the LabVIEW Runtime.
- You cannot debug TestStand steps configured to execute Express VIs or property nodes.
- LabVIEW will not connect to the TestStand Sequence Editor if the relevant LabVIEW Runtime does not have any VI code modules loaded.

#### Debugging VIs executing in different LabVIEW projects

If you have a sequence file that executes VIs in one or more project contexts, you can connect to each project context by selecting the item named SeqEdit.exe - <Project Name>.lvproj – My Computer from the Application or shared library option in the LabVIEW Debug Application or Shared Library dialog box.

#### Debugging VIs executing in different LabVIEW Runtimes

You can only debug code module VIs executing in one LabVIEW Runtime at a time. If you want to debug VIs executing in a different LabVIEW Runtime, you must close the existing debug connection from LabVIEW and open a new debug connection using the LabVIEW Development System that matches the LabVIEW Runtime version and bitness.

#### Debugging VIs executed in a User Interface

You can debug VIs executed in a TestStand User Interface by launching the User Interface in the LabVIEW Development System and setting the LabVIEW Adapter to execute VIs using the LabVIEW Development System before you execute your test sequence.

#### Closing a Debug Connection

When you open a debug connection from LabVIEW, LabVIEW will continue to debug VIs executed by the runtime until all code module VIs being debugged are closed. You can also close the debug connection using one of the following approaches:

- In the LabVIEW Development System, right-click on the front panel of one of the VIs to debug and select Remote Debugging»Quit Debug Session from the shortcut menu.
- In the TestStand Sequence Editor, unload all modules by using either the File menu or the TestStand Engine API.

Parent topic:

Debugging and Tracing of VIs Executed Using the LabVIEW Runtime

<!--NI_TOPIC bundle=teststand path=debugging-dlls.html language=enus -->
## TOPIC 00277: Debugging DLLs

- bundle_id: `teststand`
- source_path: `debugging-dlls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-dlls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To debug a DLL TestStand calls, first create the DLL with debugging enabled in the ADE. Then, launch the TestStand Sequence Editor or TestStand User Interface executable from the ADE or attach to the sequence editor or user interface process from the ADE, when supported. Debugging LabVIEW DLLs To bu

### Debugging DLLs

To debug a DLL TestStand calls, first create the DLL with debugging enabled in the ADE. Then, launch the TestStand Sequence Editor or TestStand User Interface executable from the ADE or attach to the sequence editor or user interface process from the ADE, when supported.

#### Debugging LabVIEW DLLs

To build a debuggable shared library in the LabVIEW development system, you must configure the shared library to enable debugging in the build specification for the shared library before building the shared library. Using the LabVIEW development system, you can then connect to the TestStand application process that loads and calls the VIs in the debuggable shared library.

#### Debugging LabWindows/CVI DLLs

Select Run»Select External Process in the Project window to identify the executable for the sequence editor or user interface and select Run»Debug <executable name> to start debugging the executable. For Visual Studio, you must enable native code debugging.

When you suspend a sequence on a step that calls a debuggable DLL, click the Step Into button in TestStand to suspend at the first statement in the DLL function within LabWindows/CVI or Microsoft Visual Studio.

To step into a code module with LabWindows/CVI, you must configure the step to use the LabWindows/CVI Adapter. You can step into a code module when you configure the LabWindows/CVI Adapter to execute steps in-process or in an external instance of LabWindows/CVI.

The LabWindows/CVI debugger automatically attaches to a TestStand process when you perform a step into operation on a LabWindows/CVI Adapter step. If the LabWindows/CVIDLL is debuggable and the source code is available, LabWindows/CVI suspends the processing the called DLL function; otherwise, TestStand performs a step over operation. You do not need to launch the Sequence Editor from LabWindows/CVI to access the debugger or choose to attach the debugger to an existing process.

Note

#### Debugging Microsoft Visual Studio DLLs

To step into a DLL directly from TestStand into a supported version of Visual Studio, you must configure the step to use the C/C++ DLL Adapter. When you attempt to step into a DLL while Visual Studio is not attached to the TestStand process, TestStand launches Visual Studio, which automatically attaches to the TestStand process using native debugging.

When you launch Visual Studio from TestStand, Visual Studio runs with the same privileges you used to run TestStand. If you launch TestStand while logged in as a user with standard privileges and then you launch Visual Studio from TestStand, you cannot execute tasks in Visual Studio that require administrator privileges. Refer to the LabWindows/CVI and Visual Studio documentation for more information about debugging DLLs in an external process.

Note

- Save sequence files and workspaces before you stop debugging and terminate the TestStand process because most ADEs terminate the process without prompting you to save modified files in TestStand.
- When you use LabWindows/CVI to debug a DLL in the TestStand process, you cannot debug a .NET assembly at the same time. When you use Visual Studio to debug an assembly in TestStand and you want to use LabWindows/CVI to debug code modules at the same time, you must configure the LabWindows/CVI Adapter to execute the steps in an external instance of LabWindows/CVI.
- You must attach Visual Studio to the TestStand process correctly depending on the type of code
 module you want to debug. For C++ code modules, NI recommends using only
 native debugging when attaching Visual Studio.
- When the Step Over command executes on an End step in a Pre-Step callback sequence, TestStand attempts to step into the code module.

Parent topic:

Calling DLLs from TestStand

Related concepts:

- Programming with the TestStand API in LabWindows/CVI
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=debugging-executions.html language=enus -->
## TOPIC 00278: Debugging Executions

- bundle_id: `teststand`
- source_path: `debugging-executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-executions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the commands in the Debug menu to suspend executions, control how TestStand single-steps within executions, set breakpoints, and stop executions prematurely. Because the Allow Break While in Code Modules option on the Execution tab of the Station Options dialog box is enabled by default, executi

### Debugging Executions

Use the commands in the Debug menu to suspend executions, control how TestStand single-steps within executions, set breakpoints, and stop executions prematurely. Because the Allow Break While in Code Modules option on the Execution tab of the Station Options dialog box is enabled by default, executions suspend even if some threads are executing code inside a code module. Using the Thread.ExternallySuspended property results in the same behavior.

Use the following panes in the Execution window to gather information when you single-step through an execution:

- Threads and Call Stack panes —The Threads pane displays the threads running in the execution and selects the active thread to view. The Call Stack pane displays the sequence invocations for the active thread and selects the active sequence invocation to view. TestStand updates these panes while tracing.
- Variables pane —Displays the sequence context for the sequence invocation currently selected on the Call Stack pane when executions suspend. Use the Variables pane to examine and modify the values of the variables and properties the sequence context contains.
- Watch View pane —Displays the values of the watch expressions you enter. The TestStand Sequence Editor updates the values on the Watch View pane when execution suspends at a breakpoint. When you enable tracing, the sequence editor also updates the values after executing each step and highlights values that change in red. Notice Watch View pane expressions that modify the structure of objects, such as deleting subproperties or changing the size of an array, can prevent the Variables pane from refreshing correctly or can cause the Variables pane to generate errors.
- Output pane —Displays generic messages, warnings, and error messages. By default, the Output pane is empty. Use the OutputMessage expression function or the Engine.NewOutputMessage method and the OutputMessage.Post method to generate the messages you want to display. Each message specifies a severity and a timestamp. The message can also specify an icon, a category, and additional execution information. Double-click a message or right-click a message and select Goto Location In»Step from the context menu to go to the step that generates the message. By default, the sequence editor generates output messages for any information a source code control provider generates.

Note

Parent topic:

Executing Sequences

Related concepts:

- Sequence Context

<!--NI_TOPIC bundle=teststand path=debugging-result-processing-plug-ins-with-off.html language=enus -->
## TOPIC 00279: Debugging Result Processing Plug-ins with Offline Results

- bundle_id: `teststand`
- source_path: `debugging-result-processing-plug-ins-with-off.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-result-processing-plug-ins-with-off.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can set breakpoints in and debug model plug-ins like in any other sequence. However, if you create a result processing plug-in and the plug-in returns errors only when the TestStand Offline Results Processing Utility invokes the plug-in to process a TestStand results (.tsr) file, you cannot debu

### Debugging Result Processing Plug-ins with Offline Results

You can set breakpoints in and debug model plug-ins like in any other sequence. However, if you create a result processing plug-in and the plug-in returns errors only when the TestStand Offline Results Processing Utility invokes the plug-in to process a TestStand results (.tsr) file, you cannot debug the plug-in from within the utility. For debugging purposes, you can process a .tsr file from within the TestStand sequence editor by invoking the Process Results File [for testing and debugging] sequence in the NI_OfflineResultsGenerator.seq.

The sequence processes the .tsr files you select with the <Default for Offline Processing> configuration. Edit the value of the Locals.OfflineProcessingConfiguration variable to specify a different configuration.

Parent topic:

Process Model Plug-In Architecture

<!--NI_TOPIC bundle=teststand path=debugging-sequences.html language=enus -->
## TOPIC 00280: Debugging Sequences

- bundle_id: `teststand`
- source_path: `debugging-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can debug sequences by tracing, setting breakpoints and conditional breakpoints, stepping through code, and including watch expressions. Refer to Using the Watch View Pane for more information about watch expressions. Completed solution files are located in the <TestStand Public>\Tutorial\Soluti

### Debugging Sequences

You can debug sequences by tracing, setting breakpoints and conditional breakpoints, stepping through code, and including watch expressions. Refer to Using the Watch View Pane for more information about watch expressions.

Note

<TestStand Public>\Tutorial\Solution

#### Step Mode Execution

Note

Configure»Station Options

Execution

OK

#### Setting a Breakpoint

Complete the following steps to set a breakpoint in a sequence file.

1. Open <TestStand Public>\Tutorial\Computer2.seq , which you created in the previous tutorial.
2. Select File»Save <filename> As and save the sequence file as Computer3.seq in the <TestStand Public>\Tutorial directory.
3. Select Execute»Break on First Step to suspend an execution on the first step TestStand executes. A checkmark appears to the left of the menu option to indicate that you enabled this option.
4. Expand the Cleanup step group on the Steps pane. Steps in the Cleanup step group execute regardless of whether the sequence completes successfully or whether a run-time error occurs in the sequence. If a step in the Setup or Main step group causes a run-time error to occur or if the operator terminates the execution, the flow of execution stops and jumps to the Cleanup step group. Steps in the Cleanup group always run even when some of the steps in the Setup group do not run. When a step in the Cleanup group causes a run-time error, execution continues to the next step in the Cleanup group.
5. Insert a Message Popup step in the Cleanup step group and rename the step Cleanup Message .
6. On the Text and Buttons tab of the Step Settings pane, enter "I am now in the Cleanup Step Group." , including the quotation marks, in the Message Expression expression control. Note You must enclose literal strings in double quotation marks ("…") in any TestStand expression field.For this example, use the default values for all the settings on the Options tab and the Layout tab of the Step Settings pane.
7. Save the changes. Leave the sequence file open for the next tutorial.

#### Stepping through a Sequence
 File

When you suspend an execution, you can step through the sequence
 using the Step Into, Step Over, and Step Out buttons on the Execution
 window.

You can find these and other debugging tools in the Debug menu of the
 sequence editor.

Complete the following steps to step through an execution of
 the Computer3.seq sequence file you created in the previous
 tutorial.

1. Select Execute»Run MainSequence . After the execution
 starts, the sequence editor immediately suspends at the first step of the
 sequence because you enabled the Break on First Step option in step 3 of the
 previous tutorial. The Execution window tab includes an execution pointer icon
 to indicate the running state of the execution. When the execution suspends, you
 can step through the sequence using the Step Into, Step Over, and Step Out
 commands at the top of the Execution window.
2. Click the Step Over button to execute the Display Dialog
 step, which launches the Test Simulator dialog box.
3. Select the RAM test to fail and click
 Done . After the Test Simulator dialog box closes, the
 sequence editor suspends the sequence execution at the end of the Setup step
 group on <End Group> .
4. Insert a breakpoint at the CPU Test step by clicking to the left of the step
 icon. In the Execution window, a dark red icon appears to the left of the CPU
 Test step to indicate the breakpoint. Note To specify a conditional
 breakpoint, right-click the breakpoint icon and select
 Breakpoint»Breakpoint Settings to launch the
 Breakpoint Settings dialog box, in which you can specify an expression that
 must evaluate to True to activate the breakpoint. Click
 OK to close the Breakpoint Settings dialog box.
 Conditional breakpoints use an orange icon in the Sequence File and
 Execution windows. Disabled breakpoints use a gray icon. When you globally
 disable all breakpoints, the breakpoints use a white icon. Refer to Using
 Variables and Properties for more information about
 expressions.
5. Click the Resume button to continue the execution. The
 sequence editor suspends the execution on the CPU Test 
 step.
6. Click the Step Into button to step into the
 MainSequence subsequence in CPU.seq , and
 click the Call Stack pane. If the Call Stack pane is not
 visible, click View»Debug»Call Stack to display it.
 Sequence call steps are similar to subVIs in LabVIEW and function or method
 calls in C/C++. When a step invokes a subsequence, the sequence that contains
 the calling step waits for the subsequence to return. The subsequence invocation
 is nested in the invocation of the calling sequence. The sequence that is
 currently executing is the most nested sequence. The chain of active sequences
 that wait for nested subsequences to complete is called the call stack. The
 first item in the call stack is the most-nested sequence invocation. The Call
 Stack pane displays the call stack for the execution thread currently selected
 on the Threads pane. A yellow pointer icon appears to the right of the most
 nested sequence invocation while the sequence executes, as shown in Figure 4-2.
7. Select each sequence on the Call Stack pane to view each sequence invocation.
 Return to the most nested sequence invocation in the call stack,
 CPU.seq .
8. Click the Step Over button to step through the
 CPU.seq subsequence one step at a time. Before you reach
 the end of the CPU.seq sequence, click the Step
 Out button. TestStand resumes the execution through the end of
 the current sequence and suspends the execution at the next step of the calling
 sequence or breakpoint, whichever comes first.
9. Continue stepping through the Computer3.seq sequence by
 clicking the Step Over button until the Cleanup
 Message step you added to the Cleanup step group executes. You must
 step over each of the 10 loops of the Video Test step.
10. Click OK to close the Cleanup Message dialog box and
 click the Step Over button to complete the execution. The
 Execution window dims when the execution completes. Do not close the Execution
 window.
11. Click the Restart button to rerun the execution. The
 Execution window must be the active window to restart the execution.
12. After the sequence editor suspends the execution on the first step, click the
 Terminate Execution button. TestStand launches the
 Cleanup Message dialog box even though you terminated the sequence execution.
 When an operator or run-time error terminates the execution, TestStand proceeds
 immediately to the steps in the Cleanup step group. Click
 OK to close the Cleanup Message dialog box. The
 Execution window dims when the execution completes.
13. Click the Restart button to rerun the execution. The
 Execution window must be the active window to restart the execution.
14. After the sequence editor suspends the execution on the first step, select
 Debug»Abort All (no cleanup) . The execution of the
 sequence immediately stops, and TestStand does not execute any steps in the
 Cleanup step group.
15. Save the changes and close all the windows in the sequence editor.

Parent topic:

Getting Started with TestStand

Related concepts:

- Using Variables and Properties

<!--NI_TOPIC bundle=teststand path=debugging.html language=enus -->
## TOPIC 00281: Debugging .NET Assemblies

- bundle_id: `teststand`
- source_path: `debugging.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/debugging.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To debug a .NET assembly, first create the assembly with debugging enabled in the ADE. Then, launch the sequence editor or user interface from Microsoft Visual Studio or attach to the sequence editor or user interface process from Visual Studio. When you use a supported version of Visual Studio and

### Debugging .NET Assemblies

To debug a .NET assembly, first create the assembly with debugging enabled in the ADE. Then, launch the sequence editor or user interface from Microsoft Visual Studio or attach to the sequence editor or user interface process from Visual Studio.

When you use a supported version of Visual Studio and you suspend a sequence on a step that calls a debuggable assembly, click the Step Into button in TestStand to suspend Visual Studio at the first statement in the assembly method or property.

When you attempt to step into an assembly while Visual Studio is not attached to the TestStand process, TestStand launches Visual Studio, which automatically attaches to the TestStand process using managed and native debugging. When you debug managed code in a TestStand process with Visual Studio, TestStand does not unload assemblies when you select File»Unload All Modules.

(Windows 10/8.1/7) When you launch Visual Studio from TestStand, Visual Studio runs with
 the same privileges you used to run TestStand. For example, if you launch TestStand while
 logged in as a user with standard privileges and then you launch Visual Studio from
 TestStand, you cannot execute tasks in Visual Studio that require administrator
 privileges.

Note

- Save sequence files and workspaces before you stop debugging and terminate the TestStand process because Visual Studio might terminate the process without prompting you to save modified files in TestStand.
- You must attach Visual Studio to the TestStand process correctly depending on the type of code
 module you want to debug. For .NET code modules, NI recommends using only
 managed debugging when attaching Visual Studio.
- When you use LabWindows/CVI to debug a DLL in the TestStand process, you cannot debug a .NET assembly at the same time. When you use Visual Studio to debug an assembly in TestStand and you want to use LabWindows/CVI to debug code modules at the same time, you must configure the LabWindows/CVI Adapter to execute the steps in an external instance of LabWindows/CVI.

Parent topic:

.NET Adapter

Related concepts:

- Debugging DLLs
- Options for Stepping Out of a Microsoft Visual Studio Assembly

Related information:

- TestStand and .NET Framework Compatibility

<!--NI_TOPIC bundle=teststand path=default-process-model-sequences-and-functions.html language=enus -->
## TOPIC 00282: Default Process Model Sequences and Functions for Generating Step Results

- bundle_id: `teststand`
- source_path: `default-process-model-sequences-and-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/default-process-model-sequences-and-functions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default process model sequences and C functions in the <TestStand>\Components\Models\TestStandModels directory that generate the report body for each step result. Report Format Generator Description ATML 6.01 or 5.0 AddReportBody sequence in reportgen_atml.seq calls the

### Default Process Model Sequences and Functions for Generating Step Results

The following table lists the default process model sequences and C functions in the <TestStand>\Components\Models\TestStandModels directory that generate the report body for each step result.

| Report Format Generator | Description |
| --- | --- |
| ATML 6.01 or 5.0 | AddReportBody sequence in reportgen_atml.seq calls the Get_Atml_ReportSection_For_Body function in ATML_Report.c in the <TestStand>\\Components\\Models\\TestStandModels\\ATML\\ATMLSupport.prj LabWindows/CVI project. |
| ATML 2.02 | GetATMLReport sequence in reportgen_atml.seq calls the Get_Atml_Report function in ATML_Report.c in the <TestStand>\\Components\\Models\\TestStandModels\\ATML\\ATMLSupport.prj LabWindows/CVI project. |
| XML | AddReportBody sequence in reportgen_xml.seq calls the TestStand API PropertyObject.GetXML method. |
| HTML sequence | AddReportBody sequence in reportgen_html.seq, which indirectly calls the PutOneResultInReport sequence for each result. |
| HTML DLL | GetReportBody_CImplementation function in c_report.c in the modelsupport2.prj LabWindows/CVI project. |
| Text sequence | AddReportBody sequence in reportgen_txt.seq, which indirectly calls the PutOneResultInReport sequence for each result. |
| Text DLL | GetReportBody_CImplementation function in c_report.c in the modelsupport2.prj LabWindows/CVI project. |

Parent topic:

Report Generation Functions and Sequences

Related concepts:

- TestStand Directory Structure
- ATML
- XML Reports

<!--NI_TOPIC bundle=teststand path=default-report-generator-process-model-plug-i.html language=enus -->
## TOPIC 00283: Default Report Generator Process Model Plug-in Sequences that Generate Reports

- bundle_id: `teststand`
- source_path: `default-report-generator-process-model-plug-i.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/default-report-generator-process-model-plug-i.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the report generator process model plug-in sequences in the <TestStand>\Components\Models\TestStandModels directory that generate reports. Report Format Header Footer ATML 6.01 or 5.0 AddReportHeader sequence in reportgen_atml.seq. AddReportFooter sequence in reportgen_atml

### Default Report Generator Process Model Plug-in Sequences that Generate Reports

The following table lists the report generator process model plug-in sequences in the <TestStand>\Components\Models\TestStandModels directory that generate reports.

| Report Format | Header | Footer |
| --- | --- | --- |
| ATML 6.01 or 5.0 | AddReportHeader sequence in reportgen_atml.seq. | AddReportFooter sequence in reportgen_atml.seq. |
| ATML 2.02 | GetATMLReport sequence in reportgen_atml.seq generates the header when it generates the report body. | GetATMLReport sequence in reportgen_atml.seq generates the footer when it generates the report body. |
| XML | AddReportHeader sequence in reportgen_xml.seq. | AddReportFooter sequence in reportgen_xml.seq. |
| HTML | AddReportHeader sequence in reportgen_html.seq. | AddReportFooter sequence in reportgen_html.seq. |
| Text | AddReportHeader sequence in reportgen_txt.seq. | AddReportFooter sequence in reportgen_txt.seq. |

Parent topic:

Report Generation Functions and Sequences

Related concepts:

- TestStand Directory Structure
- ATML
- XML Reports

<!--NI_TOPIC bundle=teststand path=default-teststand-table-schemas.html language=enus -->
## TOPIC 00284: Default TestStand Table Schemas

- bundle_id: `teststand`
- source_path: `default-teststand-table-schemas.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/default-teststand-table-schemas.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand database schema requires the following tables in the database: UUT_RESULT STEP_RESULT STEP_SEQCALL PROP_RESULT PROP_BINARY PROP_ANALOGWAVEFORM PROP_DIGITALWAVEFORM PROP_NUMERICLIMIT The UUT_RESULT table contains information about each UUT. The STEP_RESULT table contains informa

### Default TestStand Table Schemas

The default TestStand database schema requires the following tables in the database:

- UUT_RESULT
- STEP_RESULT
- STEP_SEQCALL
- PROP_RESULT
- PROP_BINARY
- PROP_ANALOGWAVEFORM
- PROP_DIGITALWAVEFORM
- PROP_NUMERICLIMIT

The UUT_RESULT table contains information about each UUT. The STEP_RESULT table contains information about each step TestStand executes while testing each UUT. The STEP_SEQCALL table contains the sequence a Sequence Call step calls. The PROP_RESULT table contains information about the properties in a step result. The other table names with the prefix "PROP" contain information about specific property data types.

Each table contains a primary key column ID and might contain foreign key column IDs. The column data types are Number, String, or GUID depending on the schema. The column data types must match the primary key the data types reference.

Note

- The default TestStand database schemas do not log attribute values for result properties.
- The default database schemas assume that result tables conform to the table definitions. When you want to modify the table schema, you must alter the tables in the database and create a new schema using the Database Options dialog box.

Parent topic:

TestStand Database Result Tables

Related concepts:

- UUT_RESULT Table Schema
- STEP_RESULT Table Schema
- STEP_SEQCALL Table Schema
- PROP_RESULT Table Schema
- PROP_BINARY Table Schema
- PROP_ANALOGWAVEFORM Table Schema
- PROP_DIGITALWAVEFORM Table Schema
- PROP_NUMERICLIMIT Table Schema
- Logging Attribute Values

<!--NI_TOPIC bundle=teststand path=defining-an-environment.html language=enus -->
## TOPIC 00285: Defining an Environment

- bundle_id: `teststand`
- source_path: `defining-an-environment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/defining-an-environment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand environments are defined by an INI text file with the .tsenv extension. The file can specify the TestStand Public directory, TestStand Application (CommonAppData) directory (which implicitly defines the TestStand Config directory), and/or the TestStand LocalApplication (LocalAppData) direc

### Defining an Environment

TestStand environments are defined by an INI text file with the
 .tsenv extension. The file can specify the TestStand Public
 directory, TestStand Application (CommonAppData) directory (which implicitly defines
 the TestStand Config directory), and/or the TestStand LocalApplication
 (LocalAppData) directory. For example, an environment file might look like this:

[TestStandPaths]

CommonAppData = "EnvironmentRoot\\CommonAppData"

LocalAppData = "EnvironmentRoot\\LocalAppData"

Public = "EnvironmentRoot\\TestStandPublic"

The paths may be absolute or relative to the location of the environment file.

Note

Any directory not specified, or specified as an empty string, will map to the default
 location that TestStand uses when no environment is specified, also called the
 global environment.

You can edit .tsenv files with a text editor or use the Configure
 Environment dialog box available in the Sequence Editor under
 Configure»Environment.

To define the environment, you must define the following fields in the
 .tsenv file:

- CommonAppData —Specifies the <TestStand
 Application Data> directory. Specifying CommonAppData
 for an environment also implicitly specifies the TestStandConfig directory,
 which contains various TestStand configuration files. Environments with
 different CommonAppData directories have different configuration files, and
 therefore do not share the associated settings and data. For example,
 environments with different CommonAppData locations have independent sets of
 Station Globals, StationOptions, and model plugin configurations. To simplify
 user management, all TestStand environments share the global
 Users.ini. This means there is still only a single set of
 TestStand users for a given system. Use theStationOptions.UserFilePath property
 to obtain the path of the Users.ini file,regardless of the
 current environment. Note The TestStand engine creates
 default versions of any required configuration files that are missing at
 startup. To base a new environment on an existing configuration, copy any
 desired configuration files from the existing environment to the
 configuration directory of the new environment.
- LocalAppData —Specifies the <TestStand Local Application
 Data> directory.This directory contains configuration files
 typically related to the layout and/or state of the Sequence Editor or TestStand
 User Interface. Data and settings persisted in these files are maintained
 separately from those of environments specifying a different LocalAppData. The
 Sequence Editor and TestStand User Interfaces create default versions of
 required configuration files that are missing at startup. Note In the global
 environment, each Windows user account has its ownLocalAppData directory.
 When an environment specifies the LocalAppDatadirectory, all Windows user
 accounts share the specified directory.
- Public —Specifies the <TestStand Public> 
 directory, which can contain modifications and customizations to existing
 TestStand components, custom user components, and other TestStand-related files.
 For example, specifying the public directory allows an environment to have its
 own customized language files, process models, and callback files. Note If the
 AdapterSupport folder is missing in an environment with a custom Public
 directory, the TestStand Engine creates it at startup by copying the global
 AdapterSupport folder. No other public files are copied automatically, but
 you can copy them manually if required.

Parent topic:

TestStand Environments

Related concepts:

- <TestStand Application Data> Directory
- TestStand Local Application Data Directory
- TestStand Public Directory

<!--NI_TOPIC bundle=teststand path=defining-custom-privileges.html language=enus -->
## TOPIC 00286: Defining Custom Privileges

- bundle_id: `teststand`
- source_path: `defining-custom-privileges.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/defining-custom-privileges.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, all users and groups include an empty Privileges.Custom category. Add Boolean properties to the NI_UserCustomPrivileges standard data type in the User Manager file in the Types window to define new privileges in the category. When you add new properties to the data type, increment the ve

### Defining Custom Privileges

By default, all users and groups include an empty Privileges.Custom category. Add Boolean properties to the NI_UserCustomPrivileges standard data type in the User Manager file in the Types window to define new privileges in the category. When you add new properties to the data type, increment the version of the type to remove the modified flag and to ensure that TestStand uses the modified type instead of the default type TestStand installs.

The sequence editor and user interfaces that use the TestStand User Interface Controls do not recognize custom privileges you define. You must add code to user interfaces to handle the custom privileges you create. For example, you can add a calibration operation to the user interface where you want to define a custom privilege so only specific users can perform the operation.

Parent topic:

Privileges

Related concepts:

- Modifying Types
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=deploying-32-bit-teststand-and-64-bit-teststa.html language=enus -->
## TOPIC 00287: Deploying 32-bit TestStand and 64-bit TestStand Systems

- bundle_id: `teststand`
- source_path: `deploying-32-bit-teststand-and-64-bit-teststa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-32-bit-teststand-and-64-bit-teststa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 32-bit TestStand Deployment Utility creates only 32-bit deployments and installers, and the 64-bit deployment utility creates only 64-bit deployments and installers. You cannot use the 64-bit installer on 32-bit operating systems. NI recommends creating a separate deployable image for the 32-bit

### Deploying 32-bit TestStand and 64-bit TestStand Systems

The 32-bit TestStand Deployment Utility creates only 32-bit deployments and installers, and the 64-bit deployment utility creates only 64-bit deployments and installers. You cannot use the 64-bit installer on 32-bit operating systems.

NI recommends creating a separate deployable image for the 32-bit version of a test system and
 the 64-bit version of a test system. The deployment specification files
 (.tsd) the deployment utility creates are bitness independent
 except for installation destination issues. Therefore, you can create a single
 .tsd and use it to deploy a test system using the 32-bit
 deployment utility and the 64-bit deployment utility.

There are some cases in which you want to create a system that has 32-bit files and 64-bit files, such as when you create a custom sequence editor or create a library for a third party to reuse. If you want to create a deployment that contains 32-bit versions of files and 64-bit versions of files, you must add all the files in the test system to the workspace. If the deployment contains VIs, you must enable the Include without Processing Item or Dependencies option on the Distributed Files tab of the deployment utility for all the VIs to prevent the deployment utility from automatically compiling the VIs with the active version of LabVIEW.

When you deploy VIs, you must use a version of LabVIEW that matches the bitness of the deployment utility because the utility creates a LabVIEW distribution and automatically removes the source-only flag from the VIs.

You can use the $(Platform) path macro to specify paths in sequence files, and the deployment utility uses the search directories for the current bitness of the utility to locate files. When the deployment utility processes sequence files and creates the distribution image, the bitness specific directory replaces the path macro in the sequence files.

You must use the 32-bit TestStand Deployment Utility to create a patch for a 32-bit full deployment, and you must use the 64-bit TestStand Deployment Utility to create a patch for a 64-bit full deployment. Create a new full deployment to update a 32-bit test system to a 64-bit test system.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- Installer Issues for 32-bit TestStand and 64-bit TestStand
- Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- Cross-Bitness Support using the LabVIEW Development System
- Remote Execution in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=deploying-a-user-interface.html language=enus -->
## TOPIC 00288: Deploying a User Interface

- bundle_id: `teststand`
- source_path: `deploying-a-user-interface.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-a-user-interface.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand Deployment Utility to deploy a user interface. Refer to the Distributing a User Interface and Including a User Interface in a Deployment topics for more information about deploying user interfaces.

### Deploying a User Interface

You can use the TestStand Deployment Utility to deploy a user interface. Refer to the Distributing a User Interface and Including a User Interface in a Deployment topics for more information about deploying user interfaces.

Parent topic:

User Interface Development Best Practices

Related concepts:

- Including a User Interface in a Deployment
- Distributing a User Interface
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=deploying-custom-rules-modules.html language=enus -->
## TOPIC 00289: Deploying Custom Rules and Analysis Modules

- bundle_id: `teststand`
- source_path: `deploying-custom-rules-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-custom-rules-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can deploy custom rules and analysis modules to use in analysis projects or to analyze individual files on other computers on which TestStand is installed. By default, when you import custom rules and analysis modules on a target computer, the TestStand Sequence Analyzer enables the rule for all

### Deploying Custom Rules and Analysis
 Modules

You can deploy custom rules and analysis modules to use in analysis projects or to
 analyze individual files on other computers on which TestStand is installed. By default,
 when you import custom rules and analysis modules on a target computer, the TestStand
 Sequence Analyzer enables the rule for all new and existing projects on that computer. You
 must manually disable the rule in each project on the computer.

Note

Note

Note

1. On your computer, launch the Configure Sequence Analyzer Available
 Rules dialog box.
2. Click the Export button to launch the Export
 Items to File dialog box.
3. In the Export Items to File dialog box, enable the custom
 rules and analysis module specifications you want to export in the
 Select Items to Export list.
4. Click the Export button to launch a file dialog box, in
 which you create or browse to the rules file (.tsarules) to
 use. By default the sequence analyzer saves the file in the
 <TestStand Public>\Components\Analyzer
 directory.
5. Click Close in the Export Items to
 File dialog box.
6. Copy the VIs, .NET assemblies, and DLLs for your custom analysis modules and
 rule configuration modules to the same location on the target computer. Also
 copy strings files and any other supporting files the modules require to the
 target computer.
7. Copy the rules file you created in step 4 on your computer to the same location
 on the target computer.
8. On the target computer, launch the Configure Sequence Analyzer
 Available Rules dialog box.
9. Click the Import button to launch the Import
 Items from File dialog box.
10. Select the rules file you copied in step 7 in the Select File to
 Import From control.
11. Enable the custom rules and analysis modules you want to import in the
 Select Items to Import list.
12. Click the Import button to add the custom rules and
 analysis modules to the target computer.
13. Click Close in the Import Items from
 File dialog box to return to the Configure Sequence
 Analyzer Available Rules dialog box.

Note

- [Sequence Analyzer Install Utility](sequence-analyzer-install-utility.html)

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Search Directories

Related information:

- Configure Sequence Analyzer Available Rules Dialog Box
- Edit Analysis Module Dialog Box
- Export Items to File Dialog Box
- Import Items from File Dialog Box

<!--NI_TOPIC bundle=teststand path=deploying-labview-project-libraries.html language=enus -->
## TOPIC 00290: Deploying LabVIEW Project Libraries

- bundle_id: `teststand`
- source_path: `deploying-labview-project-libraries.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-labview-project-libraries.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the deployment includes a VI that a project library references, the deployment must include a copy of the project library, which might include files the test system does not require. However, including such non-dependent project library files in the deployment can increase the time required to cr

### Deploying LabVIEW Project Libraries

If the deployment includes a VI that a project library references, the deployment must include a copy of the project library, which might include files the test system does not require. However, including such non-dependent project library files in the deployment can increase the time required to create the deployment and the disk space the deployment requires. Therefore, the TestStand Deployment Utility creates partial project libraries that include only the VIs the test system requires to reduce the time required to create deployments, the size of deployment installers, and the size of installed deployments on test station computers.

NI does not recommend using partial project libraries to deploy VIs that were previously
 deployed, including VIs from vi.lib, instr.lib, or
 user.lib.

Parent topic:

Preparing Source Components for Deployment

Related concepts:

- Partial Project Libraries
- Troubleshooting LabVIEW Code Module Issues

<!--NI_TOPIC bundle=teststand path=deploying-multiple-test-systems-to-the-same-t.html language=enus -->
## TOPIC 00291: Deploying Multiple Test Systems to the Same Test Station

- bundle_id: `teststand`
- source_path: `deploying-multiple-test-systems-to-the-same-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-multiple-test-systems-to-the-same-t.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multiple test systems can exist on the same test station computer. For example, you might want a legacy version and the current version of a test system on the same test station computer. When you install deployments for different versions of TestStand on the same computer, use the TestStand Version

### Deploying Multiple Test Systems to the Same Test Station

Multiple test systems can exist on the same test station computer. For example, you might want a
 legacy version and the current version of a test system on the same test station
 computer. When you install deployments for different versions of TestStand on the
 same computer, use the TestStand Version Selector to select the active version of
 TestStand before you launch the deployed TestStand application. NI does not support
 running applications that use two different versions of TestStand at the same
 time.

To effectively use multiple test systems on the same test station computer, you must design the test systems to avoid potential conflicts when the test systems or . If you are creating MSI-based installers, use the Save As option in the TestStand Deployment Utility and select the option to create a new installer to create a new TSD file with a different installer GUID so both installers can install side by side. You can also create installers that install side by side.

If you are creating package distributions, ensure that the product and/or company name fields are different for each distribution, since these fields are used to generate the package name which must be unique for each package you create.

The following changes you make to one test system affect all test systems installed on a test station computer:

Note

- Changing TestStand configuration settings stored in GeneralEngine.cfg, Adapters.cfg, TypePallete.cfg, and SearchDirectories.cfg affects all test systems on the test station computer. For example, if one test system adds a directory to the search paths, another test system on the test station computer can also find a file in that directory. You can use LabVIEW projects, unique filenames in each test system, or different configuration directories for each test system on the test station computer to work around this behavior. If you want to use a separate configuration file for multiple deployments on a single test station, you can deploy the files using an engine environment file to specify a custom location for the configuration files for each deployment. See the Deploying with Environments topic for more information.
- Updating NI drivers affects all test systems on the test station computer.

#### Supporting Multiple Versions of TestStand

When you use the deployment utility to build an installer, the deployment utility can include multiple versions of the TestStand Runtime. The Include TestStand Runtime option includes only the version of the TestStand Runtime that matches the version of the deployment utility. Use the Drivers and Components dialog box to include additional TestStand Runtimes. Multiple versions of the TestStand Runtime can exist on the test station computer, but the test system uses the most recently registered version of TestStand. You can use the TestStand Version Selector to change the currently active version of TestStand.

#### Test Systems That Do not Share Files or Execute at the Same Time

Test systems that do not share files and that do not load or execute simultaneously rarely conflict with each other when you deploy the test systems to the same test station computer.

To ensure that the test systems do not share files, install the test systems to different directory hierarchies on the test station computer and ensure that each test system uses separate copies of the code modules, including code modules used in all test systems on the test station computer. If the test systems do not share files, you can update any file in one test system without affecting another test system.

To ensure that the files do not load in memory simultaneously, unload all code modules after you execute one test system and before you load the next test system to avoid conflicts among the test systems installed on the same test station computer.

#### Test Systems That Share Files

Shared files must work correctly with all the test systems that use the shared files. You must test changes to shared files with all the test systems on the test station computer to ensure that the test systems execute successfully after the update.

Consider the following guidelines when you change shared files:

- If you change the prototypes of exposed interfaces of shared files, you must update all the callers in all the test systems that use the shared files to ensure that the callers execute without errors. Exposed interfaces include VI connector panes and DLL function prototypes.
- Do not delete files until you confirm that no test system installed on the test station computer uses the files.
- Do not install an updated version of the file unless both test systems can use the updated version of the file.
- Compiling a test system to use a later version of LabVIEW also updates any shared files to use the later version of LabVIEW, which can break VIs in the test systems you did not update.
- Uninstalling an installer you built with the TestStand Deployment Utility removes shared files from other test systems installed on the test station computer unless you distributed the files as LabVIEW packed project libraries.
- When you update existing test systems, the installer replaces a previously installed configuration file or does not modify the file. When you replace a configuration file, such as GeneralEngine.cfg , you replace all the settings stored in the file. TestStand does not merge the existing settings with the new settings in the file. Because configuration files are non-versioned files, you can use the Force File to Install option on the Distributed Files tab of the deployment utility to ensure that deployments always install configuration files, such as GeneralEngine.cfg . If you want to use a separate configuration file for multiple deployments on a single test station, you can deploy the files using an engine environment file to specify a custom location for the configuration files for each deployment. See the Deploying with Environments topic for more information. Notice When you enable the Force File to Install option, an installer can replace a newer version of a file with an older version of a file, which can be problematic for DLLs because components on the computer might rely on functionality available only in the newer version of the DLL and might not execute correctly when the installer downgrades the DLL.

#### Test Systems That Execute Simultaneously

Name collisions or type conflicts can occur if you load sequence files from multiple test systems simultaneously. Name collisions can occur among VIs or among dependent DLLs. Type conflicts can occur when TestStand loads two sequence files that include data types or step types with the same type version but different definitions.

Use the following techniques to avoid VI and DLL dependency name collisions or type conflicts:

- Use unique filenames or unique qualified names for VIs across test systems you install on the same test station computer.
- Call VIs in the context of LabVIEW projects that are unique to each test system to avoid name collisions and partial project library conflicts.
- Because TestStand cannot load two DLLs that load dependencies with the same name from different paths, change the DLLs to use the same dependency with the same path or use unique names for the dependencies.
- Download the NI TestStand Toolkit for Large Application Development from ni.com and use the type differ tool to locate type differences between sequence files of two test systems.

Parent topic:

Transferring Files

Related concepts:

- Building a Customized MSI-based Installer
- Choosing Single or Multiple Deployments
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Managing Versioned and Non-Versioned Files
- Managing Type Revisions
- Partial Project Libraries

<!--NI_TOPIC bundle=teststand path=deploying-network-published-shared-variables.html language=enus -->
## TOPIC 00292: Deploying Network-Published Shared Variables

- bundle_id: `teststand`
- source_path: `deploying-network-published-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-network-published-shared-variables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use network-published shared variables so VIs on distributed systems can share data across the network. LabVIEW identifies shared variables through a network path that includes the computer name (target name), project library name(s), and shared variable name. LabVIEW must create shared variables in

### Deploying Network-Published Shared Variables

Use network-published shared variables so VIs on distributed systems can share data across the network. LabVIEW identifies shared variables through a network path that includes the computer name (target name), project library name(s), and shared variable name. LabVIEW must create shared variables in the Shared Variable Engine before a test system can access the shared variables.

#### With a LabVIEW Project

When the test system executes VIs in the context a LabVIEW project, enable the Auto Deploy Shared Variables on First Load of any VI in a Project option and the Auto Undeploy Shared Variables on Last Unload of all VIs in a Project option in the LabVIEW Adapter Configuration dialog box to automatically deploy and undeploy shared variables defined in the LabVIEW project when the project is first loaded for execution.

#### Without a LabVIEW Project

When the test system executes VIs without a project, TestStand cannot automatically deploy shared variables. Therefore, you must deploy shared variables to the local computer in one of the following ways:

- Manually deploy the shared variables in the LabVIEW development system using a LabVIEW project.
- Use the Deploy Library step type to deploy or undeploy to the local computer the shared variables defined in a LabVIEW project library file or packed project library file, or to deploy or undeploy shared variables defined in LabVIEW project libraries within a selected LabVIEW project.

Note

- The project library or packed project library must contain only shared variables and cannot contain any VI files.
- TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the LabVIEW Help for more information about deploying shared variables and NI-PSP URLs.
- NI recommends that you do not use a Deploy Library step to deploy or undeploy shared variables
 when steps in different threads or executions might access the shared
 variables.
- TestStand does not support calling a VI or DLL that programmatically deploys shared variables using the LabVIEW Deploy Library method on a LabVIEW Application reference or using the LabVIEW Deploy Items method on a LabVIEW Project reference. When you programmatically deploy shared variables, the TestStand or LabVIEW application might return an error and terminate. You can use the Deploy Library method from within a stand-alone executable without adverse effects on TestStand.
- TestStand cannot auto-deploy shared variables defined in a LabVIEW packed project library specified in a LabVIEW project or in a LabVIEW project library saved in an LLB specified in a LabVIEW project.
- TestStand cannot deploy project libraries that have shared variables that are aliased to existing shared variables in a project or an NI-PSP data item on the network.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Organizing Test Program Files with LabVIEW Project Libraries
- Organizing Test Program Files with LabVIEW Projects
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=deploying-stand-alone-vis.html language=enus -->
## TOPIC 00293: Deploying Stand-alone VIs

- bundle_id: `teststand`
- source_path: `deploying-stand-alone-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-stand-alone-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations and requirements for deploying VIs when you decide whether to use stand-alone VIs in a TestStand system: NI does not recommend distributing two VIs with the same name to different locations on a target computer. When a VI with the same name from a different loc

### Deploying Stand-alone VIs

Consider the following recommendations and requirements for deploying VIs when you decide whether to use stand-alone VIs in a TestStand system:

- NI does not recommend distributing two VIs with the same name to different locations on a target
 computer. When a VI with the same name from a different location is in memory,
 LabVIEW uses the VI in memory when attempting to load a subVI. However, LabVIEW
 reports an error when you attempt to load a top-level VI with the same name as a
 VI in memory even when the similarly named VI in memory is an exact copy of the
 one you want to load.
- TestStand does not support including two VIs with the same name in a deployment unless the VIs are in different project libraries.
- When you build a TestStand deployment that calls VIs that use shared variables, you must complete the following tasks:
  - Add project library files that contain shared variables to the workspace you use to create the deployment or deploy the files using a LabVIEW Utility Deploy Library step in the test sequences. The TestStand Deployment Utility automatically includes project library files it finds in the workspace or from LabVIEW Utility Deploy Library step references when you configure the step to deploy the project library.
  - Add an aliases file to the deployment and configure the deployment to install the aliases file to the proper location on the destination system so LabVIEW can resolve network paths.
  - Include the NI Variable Engine component in the installer to ensure that the destination system can use the shared variables.
- You must execute a LabVIEW Utility Deploy Library step in a TestStand sequence to deploy shared variables to the local computer. You can also manually deploy shared variables to the local computer using a project in the LabVIEW development system.

Parent topic:

Organizing Test Program Files with Stand-alone VIs

Related concepts:

- Deploying TestStand Systems
- Organizing Test Program Files with Stand-alone VIs
- Organizing Test Program Files with LabVIEW Project Libraries
- Deploying Network-Published Shared Variables
- Resolving References to Shared Variables
- Editing Stand-alone VIs
- Processing LabVIEW Code Modules for Deployment
- Updating and Patching Stand-alone VIs

<!--NI_TOPIC bundle=teststand path=deploying-teststand-systems.html language=enus -->
## TOPIC 00294: Deploying TestStand Systems

- bundle_id: `teststand`
- source_path: `deploying-teststand-systems.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-teststand-systems.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about the following concepts: Evaluating deployment-related concepts before you design a test system. Selecting the most effective mechanism for creating one or multiple deployments depending on the functional and maintenance requirements of the test system and rela

### Deploying TestStand Systems

This section contains information about the following concepts:

- Evaluating deployment-related concepts before you design a test system.
- Selecting the most effective mechanism for creating one or multiple deployments depending on the functional and maintenance requirements of the test system and related deployment.
- Using the TestStand Deployment Utility to create a customized full test system deployment or patch deployment.

The NI TestStand Advanced Architecture Series is a suite of documents, located on the NI website, authored by TestStand architects and developers to provide more advanced concept and architecture information for experienced TestStand users with complex projects.

Related concepts:

- Before You Begin
- Deployment Process Overview
- Choosing a Deployment Mechanism
- Choosing Single or Multiple Deployments
- Customizing Components You Deploy
- Patching Deployments
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=deploying-the-teststand-runtime.html language=enus -->
## TOPIC 00295: Deploying the TestStand Runtime

- bundle_id: `teststand`
- source_path: `deploying-the-teststand-runtime.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-the-teststand-runtime.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to deploy the TestStand Runtime. Select Tools»Deploy TestStand System in the TestStand Sequence Editor to launch the TestStand Deployment Utility. On the System Source tab, enable the Deploy Files»From TestStand Public Directories option to collect files from the <TestSt

### Deploying the TestStand Runtime

Complete the following steps to deploy the TestStand Runtime.

1. Select Tools»Deploy TestStand System in the TestStand Sequence Editor to launch the TestStand Deployment Utility.
2. On the System Source tab, enable the Deploy Files»From TestStand Public Directories option to collect files from the <TestStand Public> directories. When you select this option, the deployment utility distributes to the test station computer any component file customizations, such as process models, step types, user interfaces, and language strings, you saved in the <TestStand Public> subdirectories.

#### Option A: MSI-based Installer

Complete the following steps to configure the MSI-based installer.

1. On the Mode tab, select the MSI-based installer output type.
2. On the Installer Options tab, use the Installer Directory control to specify the directory to which the deployment utility copies the installer for the test system.
3. On the Installer Options tab, enable the Install TestStand Runtime option.
4. Click the Drivers and Components button to launch the Drivers and Components dialog box, in which you can select additional components to include in the installer.
5. To include development components such as the TestStand sequence editor, disable the Only display runtime installers option to display the TestStand product.
6. Select the TestStand product to include the sequence editor in the TestStand Runtime installation.
7. Click OK to apply the new settings and close the dialog box.
8. Click Save and save the build as EngineInstaller.tsd .
9. Click the Build button to build the installer.

#### Option B: Package-based distribution

Complete the following steps to configure the package distribution:

1. On the Mode tab, select the Package-based Distribution output type, then select the Package Installer option.
2. On the Package Distribution Options tab, use the Output Directory control to specify the directory to which the deployment utility copies the installer for the test system.
3. On the Package Distribution Options tab, enable the Install TestStand Runtime option.
4. Click the Dependencies button to launch the Drivers and Components dialog box, in which you can select additional components to include in the distribution.
5. Select the TestStand Sequence Editor product to include the sequence editor in the TestStand Runtime installation.
6. Click OK to apply the new settings and close the dialog box.
7. Click Save to save the build as EnginePackageInstaller.tsd.
8. Click Build to build the package installer.

#### Installing the Test System

Complete the following steps to install the test system.

1. To use the installer, copy all the files from the installer directory you specified on the Installer Options tab to the distribution media you want to use or to a shared directory on a network.
2. On the test station computer, insert the distribution media or connect to the network and run the installer executable to start the installer.
3. When the installation completes, complete the following steps to verify that the TestStand Runtime installed correctly.
  - Launch NI Package Manager
  - Select the Installed tab, and enter teststand in the search field.
  - Verify that the TestStand products you included are present in the list of packages.
4. Activate a license when the sequence editor prompts you.

Parent topic:

Common Deployment Scenarios

Related concepts:

- TestStand Directory Structure
- Activating and Licensing TestStand
- Distributing a User Interface

<!--NI_TOPIC bundle=teststand path=deploying-translators-and-custom-sequence-fil.html language=enus -->
## TOPIC 00296: Deploying Translators and Custom Sequence Files

- bundle_id: `teststand`
- source_path: `deploying-translators-and-custom-sequence-fil.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-translators-and-custom-sequence-fil.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you place a custom sequence file translator DLL and its support files in the <TestStand Public>\Components\Translators directory on the computer you use to build the deployment, the TestStand Deployment Utility automatically includes these files in the deployment when you enable the Deploy File

### Deploying Translators and Custom Sequence Files

When you place a custom sequence file translator DLL and its support files in the
 <TestStand Public>\Components\Translators directory
 on the computer you use to build the deployment, the TestStand Deployment Utility
 automatically includes these files in the deployment when you enable the Deploy
 Files in TestStand Public Directories option on the System Source tab of the
 deployment utility. Alternatively, you can add the translator files to the workspace
 and set the target destination directory for the files to the
 <TestStand Public>\Components\Translators
 directory.

When the deployment utility analyzes a TestStand sequence file, the utility completes the following steps to ensure that TestStand can locate the code module on the computer where you deploy the files.

1. Locates the code modules the steps in the sequence file call.
2. Adds the code module files to the deployment.
3. Changes absolute path references in sequence files to relative path references.

You can add custom sequence files to the workspace the deployment utility uses to build a deployment. The deployment utility must load and translate custom sequence files to locate the code modules the steps in the sequence file call. However, the deployment utility does not modify the paths in the custom sequence file and returns a warning when the deployment utility cannot ensure that TestStand can locate the code module on the computer where you deploy the files. You must fix the paths on the computer you use to build the deployment, or you must fix the paths on the target computer after deployment.

Parent topic:

Sequence File Translators

Related concepts:

- Creating a Sequence File Translator DLL
- TestStand Directory Structure
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=deploying-type-palette-files.html language=enus -->
## TOPIC 00297: Deploying Type Palette Files

- bundle_id: `teststand`
- source_path: `deploying-type-palette-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-type-palette-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to deploy a type palette file. Add the type palette file to the TestStand workspace you want to deploy or copy the type palette file to the directory you want to deploy. On the Distributed Files tab of the TestStand Deployment Utility, click the Analyze Source Files butt

### Deploying Type Palette Files

Complete the following steps to deploy a type palette file.

1. Add the type palette file to the TestStand workspace you want to deploy or copy the type palette file to the directory you want to deploy.
2. On the Distributed Files tab of the TestStand Deployment Utility, click the Analyze Source Files button to verify that the type palette file appears in the list of files to deploy.

Type palette files are normally located in the <TestStand Public>\Components\TypePalettes directory. Complete the following steps to set the type palette file destination to this directory.

1. Select the type palette file.
2. Select TestStand Public Documents Directory for the Installation Destination option.
3. Enter Components\TypePalettes for the Installation Destination Subdirectory option.

Parent topic:

User Components

Related concepts:

- Type Palette Files
- Using a TestStand Workspace File to Create a Deployment
- Using a Directory to Create a Deployment
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=deploying-vis-in-labview-packed-project-libra.html language=enus -->
## TOPIC 00298: Deploying VIs in LabVIEW Packed Project Libraries

- bundle_id: `teststand`
- source_path: `deploying-vis-in-labview-packed-project-libra.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-vis-in-labview-packed-project-libra.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations and requirements for deploying VIs when you decide whether to use LabVIEW packed project libraries in a TestStand system: Packed project libraries reduce the number of files required to create a deployment using the TestStand Deployment Utility and reduce the t

### Deploying VIs in LabVIEW Packed Project Libraries

Consider the following recommendations and requirements for deploying VIs when you decide whether to use LabVIEW packed project libraries in a TestStand system:

- Packed project libraries reduce the number of files required to create a deployment using the TestStand Deployment Utility and reduce the total build time because packed project libraries are precompiled files.
- Packed project libraries are compressed files and therefore occupy less disk space than VIs.
- You must determine whether the test system will benefit more from the faster build times
 the pre-built packed project libraries offer or the convenience of using the deployment
 utility to build the packed project library:
  - If you are deploying a pre-built packed project library, the deployment utility
 copies only the packed project library.
  - If you configure the deployment utility to create a packed project library, it must
 create the packed project library on every build.
- Packed project libraries are compressed files and therefore occupy less disk space than VIs.
- The deployment utility supports building the packed project library with debugging information to support debugging of the packed project library on the deployed system.

Note

- Use the Deploy Library step type to deploy or undeploy to the local computer the shared variables defined in a LabVIEW project library file or packed project library file, or to deploy or undeploy shared variables defined in LabVIEW project libraries within a selected LabVIEW project.
- The project library or packed project library must contain only shared variables and cannot contain any VI files.
- TestStand cannot auto-deploy shared variables defined in a LabVIEW packed project library specified in a LabVIEW project or in a LabVIEW project library saved in an LLB specified in a LabVIEW project.

Parent topic:

Organizing Test Program Files with LabVIEW Packed Project Libraries

Related concepts:

- Deploying TestStand Systems
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Deploying Network-Published Shared Variables
- Creating a Deployable Image
- Editing VIs in LabVIEW Packed Project Libraries
- Processing LabVIEW Code Modules for Deployment
- Updating and Patching VIs in LabVIEW Packed Project Libraries

<!--NI_TOPIC bundle=teststand path=deploying-vis-in-labview-projects.html language=enus -->
## TOPIC 00299: Deploying VIs in LabVIEW Projects

- bundle_id: `teststand`
- source_path: `deploying-vis-in-labview-projects.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deploying-vis-in-labview-projects.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations and requirements for deploying VIs when you decide whether to use LabVIEW projects in a TestStand system: The size of a deployment affects its size on disk and the time required to install. If the test system contains multiple LabVIEW projects, the size of the

### Deploying VIs in LabVIEW Projects

Consider the following recommendations and requirements for deploying VIs when you decide whether to use LabVIEW projects in a TestStand system:

- The size of a deployment affects its size on disk and the time required to install. If the test system contains multiple LabVIEW projects, the size of the deployed image is larger and takes longer to build. To reduce the time required to create a deployable build that includes multiple LabVIEW projects, enable the Consolidate Files Shared by Projects option in LabVIEW VI Options dialog box of the TestStand Deployment Utility to create a merged project for use in a deployable image.
- TestStand does not support deploying project libraries with the same name and different file paths. You receive an error when you attempt to include two project libraries with the same name.

Parent topic:

Organizing Test Program Files with LabVIEW Projects

Related concepts:

- Deploying TestStand Systems
- Organizing Test Program Files with LabVIEW Projects
- Organizing Test Program Files with LabVIEW Project Libraries
- Editing VIs in LabVIEW Projects
- Processing LabVIEW Code Modules for Deployment
- Updating and Patching VIs in LabVIEW Projects

<!--NI_TOPIC bundle=teststand path=deployment-process-overview.html language=enus -->
## TOPIC 00300: Deployment Process Overview

- bundle_id: `teststand`
- source_path: `deployment-process-overview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/deployment-process-overview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following tasks to carefully plan, design, implement, execute, and validate a full or patch deployment process for a complex TestStand-based test system.

### Deployment Process Overview

Complete the following tasks to carefully
 plan, design, implement, execute, and validate a full or patch deployment process
 for a complex TestStand-based test system.

[IMAGE alt='image' src='GUID-397CF6D5-0305-4150-8B3A-A3B2467CE4C9-a5.svg']

1. Identifying Components to Deploy
2. Choosing a Deployment Mechanism
3. Preparing Source Components for Deployment
4. Customizing Components You Deploy
5. Creating Deployments
6. Transferring Files
7. Validating Deployments

Parent topic:

Deploying TestStand Systems

Related concepts:

- Patching Deployments

<!--NI_TOPIC bundle=teststand path=determining-resource-usage.html language=enus -->
## TOPIC 00301: Determining Resource Usage

- bundle_id: `teststand`
- source_path: `determining-resource-usage.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/determining-resource-usage.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Locks and Resource Usage The Execution Profiler cannot directly determine when a thread uses a logical or physical resource. Instead, the profiler records when a thread waits for, acquires, or releases a TestStand lock. Typical TestStand applications use TestStand locks to surround the use of logica

### Determining Resource Usage

#### Locks and Resource Usage

The Execution Profiler cannot directly determine when a thread uses a logical or physical resource. Instead, the profiler records when a thread waits for, acquires, or releases a TestStand lock. Typical TestStand applications use TestStand locks to surround the use of logical and physical resources to guarantee that only one thread accesses the resources at a time. Because lock acquisition and resource usage correspond, viewing the time line of lock acquisitions provides a close approximation of actual resource usage. In addition, because threads wait to acquire locks rather than resources, viewing lock operations shows when threads block waiting for a resource to become available. If threads block excessively because of limited resources or a design flaw, viewing the associated lock operations can highlight the location of the performance issue.

A system might use resources you protect with mechanisms other than TestStand locks, including lower-level primitives, such as operating system critical sections and mutexes. To view the uses of resources with non-TestStand locks in the profiler, you must also surround the resources with TestStand locks.

Depending on the system, you might be able to place TestStand locks at a much higher level than the underlying thread synchronization. For example, if a step calls a code module you write that spends most of its time in a call to an instrument driver function that internally synchronizes thread access to the instrument, you can place a TestStand lock around the calling step to approximate the instrument driver synchronization in a way that is viewable in the profiler.

Use the Lock step type or the Use Lock to Allow Only One Thread at a Time to Execute the Step option to create and invoke TestStand locks. You can also call the TestStand API to create and invoke TestStand locks from within code modules you write.

Parent topic:

Execution Profiler

Related concepts:

- Code Modules

Related information:

- Lock Step

<!--NI_TOPIC bundle=teststand path=developing-platform-independent-test-systems.html language=enus -->
## TOPIC 00302: Developing Platform Independent Test Systems

- bundle_id: `teststand`
- source_path: `developing-platform-independent-test-systems.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/developing-platform-independent-test-systems.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how you can create test sequences that can execute in 32-bit TestStand and 64-bit TestStand with no modifications. The example uses the $(Platform) path macro in the module path to call the correct version of a LabWindows/CVI DLL and a C++ DLL based on the current b

### Developing Platform Independent Test Systems

#### Purpose

This example demonstrates how you can create test sequences that can execute in 32-bit TestStand and 64-bit TestStand with no modifications.

The example uses the $(Platform) path macro in the module path to call the correct version of a LabWindows/CVI DLL and a C++ DLL based on the current bitness of TestStand.

The example uses a LabVIEW code module with the Separate Compiled Code from source file option enabled so 32-bit LabVIEW and 64-bit LabVIEW can execute the VI.

The example assembly is built using the Any CPU configuration so that 32-bit TestStand and 64-bit TestStand can call it.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Developing Platform Independent Test
 Systems\Developing Platform Independent Test Systems.seq

#### Highlighted Features

- $(Platform) path macro
- Separate Compiled Code from Source File LabVIEW option
- Any CPU Visual Studio Build Configuration setting

#### Major API

Engine.Is64Bit property

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select the CVI step or the C++ Action 
 step. Observe that the $(Platform) path macro is present in the Module
 path. This macro evaluates as win32 or x64 in the
 resolved path based on the current TestStand bitness.
2. Select the .NET Action step and click Edit 
 to open the VI. Notice that the same code module path will be used for 32-bit TestStand
 and 64-bit TestStand. Because the assembly is built using the Any CPU Visual Studio Build
 Configuration Setting, the module can be called by either bitness of TestStand.
3. If the LabVIEW development system is installed, select the LabVIEW
 Action step and click Edit to open the VI. In
 LabVIEW, select File»VI Properties . Notice that the
 Separate Compiled code from source file option is enabled. This
 setting allows the same VI to execute in 32-bit LabVIEW and 64-bit LabVIEW.
4. Observe that the IF statement uses the Engine.Is64Bit property to
 determine the current bitness of TestStand. This property allows you to define different
 behavior for 32-bit TestStand and 64-bit the bitness of TestStand.
5. Run the example and notice that the executed code module bitness matches TestStand.
6. If possible, open the example in the other bitness of TestStand and observe the
 difference in behavior.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure
- Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- Executing VIs with Separate Compiled Code
- AnyCPU Assemblies in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=developing-teststand-systems.html language=enus -->
## TOPIC 00303: Developing TestStand Systems

- bundle_id: `teststand`
- source_path: `developing-teststand-systems.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/developing-teststand-systems.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the NI TestStand Advanced Architecture Series for more advanced concept and architecture information. This series is a suite of documents TestStand architects and developers created to provide detailed information for experienced TestStand users with complex projects. Visit ni.com/info and

### Developing TestStand Systems

Refer to the NI TestStand Advanced Architecture Series for more advanced concept and architecture information. This series is a suite of documents TestStand architects and developers created to provide detailed information for experienced TestStand users with complex projects.

Visit ni.com/info and enter the Info Code BldTestSys to access the NI Fundamentals of Building a Test System guides for more information about the recommended process for building test systems.

Visit ni.com/info and enter the Info Code TestMgtSWDevGd to access the NI Test Management Software Developers Guide for more information about developing test systems.

Parent topic:

Extending TestStand

<!--NI_TOPIC bundle=teststand path=differences-between-patch-deployments-and-ful.html language=enus -->
## TOPIC 00304: Differences between Patch Deployments and Full Deployments

- bundle_id: `teststand`
- source_path: `differences-between-patch-deployments-and-ful.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/differences-between-patch-deployments-and-ful.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use patch deployments to add new or update changed files, drivers, or components in a previously installed full deployment. Patch deployments typically include only the files and installers you modified since creating the full deployment. Avoid using patch deployments when you need to reorganize fil

### Differences between Patch Deployments and Full Deployments

Use patch deployments to add new or update changed files, drivers, or components in a previously installed full deployment. Patch deployments typically include only the files and installers you modified since creating the full deployment. Avoid using patch deployments when you need to reorganize files or add or modify a significant number of files on the test station computer.

Use full deployments to install a test system to a test station computer that does not include any previously installed version of the deployment. A full deployment includes all the required files and installers you configured in the TestStand deployment specification file (.tsd) for the deployment. Avoid using full deployments when you need to make only small changes or add or change only a few files on the test station computer.

| Deployment Type | Advantages | Disadvantages | Typical Use Cases | Best Practices |
| --- | --- | --- | --- | --- |
| Patch deployment | Smaller than full deployment it updates (Size is proportional to the size and number of changed files, drivers, components, and installers in the test system.) Installs faster than full deployment it updates Requires installed full deployment on test station computer to prevent installing files with missing dependencies | Creating patch installers requires the corresponding full deployment installer Cannot uninstall the patch installer without uninstalling the full deployment installer Can make only limited changes | Fixing bugs in full deployment Adding new files or features to full deployment | Create cumulative patch deployments that include changes from all previous patch deployments you created from a full deployment Create baseline patch deployments, from which you can create dependency patch deployments Save the .tsd files to store information required to create dependency patch deployments Validate the test system before deploying patch deployments |
| Full deployment | Installs to test station computer that does not have any previously deployed test system Unlimited changes, such as deleting or moving files, when updating a previous full deployment on the test station computer | Inefficient for making changes to a subset of files in a previously deployed test system Same or larger size as previous full deployment, even when you modify only one file Same or larger size installer, which typically takes longer to install than patch deployments because installers for full deployments uninstall and then reinstall all the files in the deployable image | Providing foundation from which to create patch deployments Frequently installing test systems to new test station computers (A single full deployment typically takes less effort to install than installing a full deployment and then installing several patches to update the test system.) Changing a significant number of files, drivers, or components on the test station computer Making changes beyond the limits of patches, such as deleting files or reorganizing the directory structure of files included in a previously deployed test system Using different upgrade codes to install multiple versions of a test system side-by-side on test station computers | Save the .tsd file to store information required to create patch deployments Back up .tsd files so you can revert changes if needed Save the full installers to store information required to build patch installers |

Parent topic:

Patching Deployments

Related concepts:

- Limitations of Patch Deployments
- Patching Deployments
- Validating Deployments
- Upgrade Codes That Affect MSI-based Installer Behavior
- Creating Independent Patch Deployments
- Uninstalling a TestStand Deployment

<!--NI_TOPIC bundle=teststand path=differences-between-standard-mode-and-manual.html language=enus -->
## TOPIC 00305: Differences between Standard Mode and Manual Mode

- bundle_id: `teststand`
- source_path: `differences-between-standard-mode-and-manual.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/differences-between-standard-mode-and-manual.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default User Files to Include and Upgrades and Patches to Include options on the Mode tab of the TestStand Deployment Utility include built-in safeguards to help you ensure that the test system can execute without errors on the test station computer when you install a patch deployment. NI recomm

### Differences between Standard Mode and Manual Mode

The default User Files to Include and Upgrades and Patches to Include options on the Mode tab of
 the TestStand Deployment Utility include built-in safeguards to help you ensure that
 the test system can execute without errors on the test station computer when you
 install a patch deployment. NI recommends using the default values for these options
 in almost all cases to ensure you include all the required files in a patch
 deployment. The default value for the User Files to Include option is Modified
 Files. The default value for the Upgrades and Patches to Include option is TestStand
 Runtime and Drivers.

Select Manual Mode in the User Files to Include option only when you are certain you know which files to include in or exclude from a patch deployment or installer. When you select Manual Mode, you can use the techniques in the following table to complete certain tasks:

| Technique | Deployment Utility Behavior | When to Use | Additional Actions to Complete |
| --- | --- | --- | --- |
| Create patch deployments without analyzing the files during the build process, which can reduce the amount of time the deployment utility requires to build an installer for a patch deployment. | Uses the previous analysis results for the deployment. | When you know exactly which files you want to include. | Click the Analyze Source Files button on the Distributed Files tab to begin analyzing all files included in the patch deployment. |
| Use the Add Patch File button on the Distributed Files tab to add arbitrary files to the patch deployment. | Adds these files without processing them. | When you want to add a file without finding the dependencies. | To process the files you add, disable the Include without Processing Item or Dependencies option on the File Properties tab of the Distributed Files tab and click the Analyze Source Files button to analyze the files you add. |
| Select a file to replace an original file in the deployable image. | Does not automatically include dependencies for the replacement file. | When you have an updated version of a file located in the non-default location that you want to include in the patch deployment. | — |

When you use Manual Mode to create a patch deployment, the deployment utility generates additional data for files you add to and replace in the deployment. The deployment utility discards the additional data for the files you add after you create a full deployment or a patch deployment using Standard Mode. The deployment utility maintains the additional data for replacement files until you delete it.

#### Example

Complete the following steps to use the deployment utility to include a single modified file in a patch deployment.

1. Load the TestStand deployment specification file ( .tsd ) you used to create the full deployment.
2. Select Create new patch deployment on the Mode tab.
3. Select Manual Mode in the User Files to Include option.
4. Click the Distributed Files tab, select View Build Preview , and select the modified file you want to add to the patch deployment.
5. Click Build to create the patch deployment that includes only the modified file you selected.

Note

Parent topic:

Including and Excluding Files in MSI-based Installer Patches

<!--NI_TOPIC bundle=teststand path=displaying-additional-timing-information.html language=enus -->
## TOPIC 00306: Displaying Additional Timing Information

- bundle_id: `teststand`
- source_path: `displaying-additional-timing-information.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/displaying-additional-timing-information.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Displaying Additional Timing Information If you want to view the timing of additional operations the system performs relative to the operations the Execution Profiler shows, surround the additional operations with TestStand locks, even if the resources involved do not need multiple thread access pro

### Displaying Additional Timing Information

#### Displaying Additional Timing Information

If you want to view the timing of additional operations the system performs relative to the operations the Execution Profiler shows, surround the additional operations with TestStand locks, even if the resources involved do not need multiple thread access protection. For example, to display when a lengthy calculation takes place and how long it takes, you can surround the calculation with a TestStand lock named "My Lengthy Calculation".

If you add a lock for profiling purposes around an operation that does not need thread synchronization, you can use a unique lock in each thread to ensure that multiple threads can run the operation in parallel. When each thread uses its own lock, a thread can never block waiting for another thread to release the lock. You can create a lock unique to a thread by appending a name unique to the thread to the name of the lock you create. A convenient source of a name unique to a TestStand thread is the Thread.UniqueThreadId property, which is available in TestStand expressions and from the TestStand API. For example, you can surround a lengthy calculation with a lock named "My Lengthy Calculation - " + RunState.Thread.UniqueThreadId.

An alternative method to display information in the profiler is to call the Engine.LogProfilerAction method.For example, before starting an operation you want the profiler to display, you might execute an expression similar to:

RunState.Engine.LogProfilerAction("Calibration", "", ThisContext, Str(RunState.Thread.Id), RunState.Thread.DisplayName, "Measure Fixture Wiring Delay", ProfilerState_InUse, "Delay Compensation", -1, True, Nothing)

After the operation completes, you might execute an expression similar to:

RunState.Engine.LogProfilerAction("Calibration", "", ThisContext, Str(RunState.Thread.Id), RunState.Thread.DisplayName, "Measure Fixture Wiring Delay", ProfilerState_Completed, "Delay Compensation", -1, True, Nothing)

Parent topic:

Execution Profiler

<!--NI_TOPIC bundle=teststand path=displaying-graphs-in-a-report.html language=enus -->
## TOPIC 00307: Displaying Graphs in a Report

- bundle_id: `teststand`
- source_path: `displaying-graphs-in-a-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/displaying-graphs-in-a-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Description This example demonstrates how to include an array from a step that calls a code module in the test report. Example File Location <TestStand Public>\Examples\Customizing Result Processing\Displaying Graphs In a Report\Displaying Graphs In a Report.seq Highlighted FeaturesCustom step types

### Displaying Graphs in a Report

#### Description

This example
 demonstrates how to include an array from a step that calls a code module in the
 test report.

#### Example File
 Location

<TestStand Public>\Examples\Customizing
 Result Processing\Displaying Graphs In a Report\Displaying Graphs In a
 Report.seq

#### Highlighted Features

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

To execute the sequence, select Execute»Single pass.

The Methods of Logging Array Data section of the MainSequence demonstrates the following two approaches for adding array data to the report:

- Log Array using Custom Action Step is an instance of a custom step type that specifies the custom property Step.Result.ResultArray . The Custom Action Step calls a code module that generates an array and writes it to Step.Result.ResultArray . TestStand step types set the IncludeInReport property flag on a subset of their result properties to specify that these properties automatically appear in the report. The IncludeInReport flag has been enabled for the Step.Result.ResultArray property so that TestStand automatically adds the values of ResultArray to the report during report generation.
- Log Array using Additional Results uses the Log field to specify that a parameter should be in the report. This field is configured in the Parameters pane, located in the module tab of the step settings pane. The log field allows you to easily log data with no further customization.

You can customize how TestStand displays the array in the report with the Include Arrays option on the Contents tab of the Report Options dialog box. TestStand can insert arrays as tables or graphs. In this example, the ReportOptions callback sets arrays to display as graphs.

In the Using Graph Attributes section of the example, you can customize the graph of an array by using the attributes of the array property, Locals.OutputData. To view or edit the attributes of a property, right click the property, then select Advanced»Edit Attributes. To customize the appearance of a graph, use the DataLayout and DataOrientation attributes, as described in the Displaying Array Data as Graphs help topic.

Review the comments for the Set Graph Attributes and Log steps for more information about the graph behavior for each value of the DataLayoutand DataOrientation attributes.

Parent topic:

Examples for Customizing Result Processing

Related concepts:

- TestStand Directory Structure
- Custom Step Types

<!--NI_TOPIC bundle=teststand path=displaying-measurement-data-as-graphs.html language=enus -->
## TOPIC 00308: Displaying Measurement Data as Graphs

- bundle_id: `teststand`
- source_path: `displaying-measurement-data-as-graphs.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/displaying-measurement-data-as-graphs.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand supports displaying one- and two-dimensional measurement array data as a graph in ATML 6.01, ATML 5.0, XML, and HTML reports using the HTML5 graph control, located in the <TestStand>\Components\Models\TestStandModels\GraphControl directory. The graph control supports displaying data as a Y

### Displaying Measurement Data as Graphs

TestStand supports displaying one- and two-dimensional measurement array data as a graph in ATML 6.01, ATML 5.0, XML, and HTML reports using the HTML5 graph control, located in the <TestStand>\Components\Models\TestStandModels\GraphControl directory. The graph control supports displaying data as a Y plot or as an XY plot. The graph control supports orientation of the array data by rows or columns.

You can add PropertyObject attributes to variables you log to specify the layout and orientation of the array data. For example, for parameters, you can add these attributes to local variables you specify in the value expression for each parameter. The graph control uses these PropertyObject attributes to interpret the data and display the appropriate plot or plots.

By default, the graph control adds plots using the row-based orientation of the array data. You can add a PropertyObject attribute with the TestStand.DataOrientation namespace to configure the graph control to interpret the array data by columns.

The type of plot the graph control displays depends on the following factors, as the following table describes:

- The number of dimensions of the array data being displayed.
- The value of the array data PropertyObject attribute with the TestStand.DataLayout namespace.
- The value of the array data PropertyObject attribute with the TestStand.DataOrientation namespace.

| Dimension of Array Data | DataLayout PropertyObject Attribute Value | DataOrientation PropertyObject Attribute Value | Plot(s) Displayed in the Report |
| --- | --- | --- | --- |
| 1D | <EmptyString> | <NotApplicable> | Single Y plot. The X coordinates of the plotted points are the array indexes. The Y coordinates of the plotted points are the array data values. |
| 2D | <EmptyString> | <NotUsed> | Multiple Y plots. A plot is created for each row in the array. The X coordinates of the plotted points are the array indexes. The Y coordinates of the plotted points are the array data values. |
| 2D | MultipleY | Row Based | Multiple Y plots. A plot is created for each row in the array. The X coordinates of the plotted points are the array indexes. The Y coordinates of the plotted points are the array data values. |
| 2D | MultipleY | Column Based | Multiple Y plots. A plot is created for each column in the array. The X coordinates of the plotted points are the array indexes. The Y coordinates of the plotted points are the array data values. |
| 2D | SingleX-MultipleY | Row Based | Multiple XY plots. A plot is created for each row in the array. The X coordinates of the plotted points are the array data values in the first row of the array. The Y coordinates of the plotted points are the array data values of every row in the array except the first row. |
| 2D | SingleX-MultipleY | Column Based | Multiple XY plots. A plot is created for each column in the array. The X coordinates of the plotted points are the array data values in the first column of the array. The Y coordinates of the plotted points are the array data values of every column in the array except the first column. |

Note

TestStand.DataLayout

TestStand.DataOrientation

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- TestStand Directory Structure
- PropertyObject Attributes

<!--NI_TOPIC bundle=teststand path=displaying-measurement-data-in-an-xml-report.html language=enus -->
## TOPIC 00309: Displaying Measurement Data in an XML Report

- bundle_id: `teststand`
- source_path: `displaying-measurement-data-in-an-xml-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/displaying-measurement-data-in-an-xml-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: XML reports might unexpectedly display a table of measurement data instead of a graph under one of the following conditions: The TSGraphControl3.dll ActiveX control, located in the <National Instruments>\Shared\TestStand directory, is not installed or registered on the computer. The My Computer secu

### Displaying Measurement Data in an XML Report

XML reports might unexpectedly display a table of measurement data instead of a graph under one of the following conditions:

- The TSGraphControl3.dll ActiveX control, located in the <National Instruments>\Shared\TestStand directory, is not installed or registered on the computer.
- The My Computer security zone setting on the Security tab of the Internet Options dialog box on the Microsoft Windows Control Panel is High . Microsoft Internet Explorer security settings can prevent web pages from using scripting to create and use an ActiveX control. When you view web pages located on the computer, Internet Explorer uses the My Computer security zone setting. A security zone setting of High prevents scripting from running locally. By default, the settings for the My Computer security zone are not visible in the Internet Options dialog box.

Parent topic:

Displaying Measurement Data as Graphs

Related concepts:

- Displaying Measurement Data as Graphs

<!--NI_TOPIC bundle=teststand path=displaying-or-hiding-teststand-specific-infor.html language=enus -->
## TOPIC 00310: Displaying or Hiding TestStand-Specific Information in an ATML Test Results 2.02 Report

- bundle_id: `teststand`
- source_path: `displaying-or-hiding-teststand-specific-infor.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/displaying-or-hiding-teststand-specific-infor.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, the report does not display TestStand-specific properties. You can enable the TR_horizontal.xsl report style sheet to display the following TestStand-specific properties in the report: TestStand Step ID Step Type Step Group Block Level Index Step Caused Sequence Failure Loop Index Number

### Displaying or Hiding TestStand-Specific Information in an ATML Test Results 2.02 Report

By default, the report does not display TestStand-specific properties. You can enable the TR_horizontal.xsl report style sheet to display the following TestStand-specific properties in the report:

- TestStand Step ID
- Step Type
- Step Group
- Block Level
- Index
- Step Caused Sequence Failure
- Loop Index
- Number of Iterations
- Number of Steps Passed
- Number of Steps Failed
- Ending Loop Index
- Interactive Execution #
- Remote Server
- Partial TPS Executed
- Number of Results
- Test Socket Index

Note

Block Level

Index

Interactive Execution #

Test Socket Index

Complete the following steps to display TestStand-specific properties in the report. When you enable the report to display TestStand-specific properties, the properties appear in a separate collapsible section in the report.

1. In TestStand, enable the Include TestStand Extension Elements option on the Contents tab of the Report Options dialog box.
2. Open the TR_horizontal.xsl file in a text editor.
3. Search for the gShowTestStandSpecificInformation XSLT variable.
4. Set the variable to true() to display TestStand-specific properties. You can reset the variable to false() to disable displaying TestStand-specific properties in the report.

Note

Partial TPS Executed

Number of Results

Test Socket Index

false()

gShowTestStandSpecificInformation

#### TestStand Extension Elements

The ATML Test Results and Session Information schema defines extension elements so users can add industry-specific or product-specific data to the report.

TestStand ATML report generators log the following additional step properties to the report in <Extension> child elements of the <TestGroup>, <SessionAction>, and <Test> elements. Enable the Include TestStand Extension Elements option on the Contents tab of the Report Options dialog box to include these extension elements in the generated report. Refer to the TestResultsTSExtension.xsd file, located in the <TestStand>\Components\Models\TestStandModels\ATML\Schemas\ATML 5 directory and the <TestStand>\Components\Models\TestStandModels\ATML\Schemas\ATML 2.02 directory, for more information about the elements you can add to the <Extension> child elements.

- TestStand Step ID
- Step Type
- Step Group
- Block Level
- Step Caused Sequence Failure
- Index
- Loop Index
- Number of Iterations
- Number of Steps Passed
- Number of Steps Failed
- Ending Loop Index
- Interactive Execution #
- Remote Server
- Partial TPS Executed
- Number of Results
- Test Socket Index

TestStand ATML report generators add the following step properties only for ATML 6.01 or 5.0 reports:

- Total time
- Module time

TestStand ATML report generators add the following TestStand-specific information in the <Extension> child element for the <TestResults> and <TestResult> element:

- Critical failure stack
- Number of step results
- Batch and Parallel report
  - Batch serial Number
  - Test socket Index
- TSR files
  - File name
  - File ID
  - Is TSR file closed
  - TSR file status

Parent topic:

Customizing the ATML Test Results 2.02 Report Style Sheet

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=displaying-the-fully-expanded-atml-test-resul.html language=enus -->
## TOPIC 00311: Displaying the Fully Expanded ATML Test Results 2.02 Report in Plain HTML

- bundle_id: `teststand`
- source_path: `displaying-the-fully-expanded-atml-test-resul.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/displaying-the-fully-expanded-atml-test-resul.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to display the fully expanded state of the report in a plain HTML format without any additional expand or collapse functionality. By default, the report enables the expand and collapse functionality. Open the TR_horizontal.xsl file. Search for the gGeneratePlainHTML XSLT

### Displaying the Fully Expanded ATML Test Results 2.02 Report in Plain HTML

Complete the following steps to display the fully expanded state of the report in a plain HTML format without any additional expand or collapse functionality. By default, the report enables the expand and collapse functionality.

1. Open the TR_horizontal.xsl file.
2. Search for the gGeneratePlainHTML XSLT variable.
3. Set the variable to true() to display the plain HTML format. You can reset the variable to false() to disable displaying the plain HTML format.

Parent topic:

Customizing the ATML Test Results 2.02 Report Style Sheet

<!--NI_TOPIC bundle=teststand path=distributing-a-user-interface.html language=enus -->
## TOPIC 00312: Distributing a User Interface

- bundle_id: `teststand`
- source_path: `distributing-a-user-interface.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/distributing-a-user-interface.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must install LabVIEW or LabWindows/CVI Run-Time Engine version and the .NET version that corresponds to the development environment version you use to create user interfaces on the test station computer. Complete the following steps to distribute a user interface. In the TestStand Sequence Edito

### Distributing a User Interface

Note

Complete the following steps to distribute a user interface.

1. In the TestStand Sequence Editor, select File»New»Workspace File to create and save a new workspace file as Deploy User Interface.tsw .
2. Right-click the Workspace window and select Insert New Project into Workspace from the context menu.
3. Save the project as User Interface.tpj .
4. Right-click the User Interface project and select Add Files to Project from the context menu.
5. In the file browse dialog box, browse to the <TestStand Public>\UserInterfaces\Simple\CVI \SourceCode directory and change the Files of Type setting to All Files (*.*) .
6. Select TestExec.exe and TestExec.uir and click Add . If TestStand prompts you to resolve the path, select the Use a relative path for the file you selected option and enable the Apply to All option.
7. Click OK to close the dialog boxes.
8. Save the workspace file.

#### Distributing Tests from a Workspace

Complete the following steps to distribute tests from a workspace.

1. Select Tools»Deploy TestStand System in the sequence editor to launch the TestStand Deployment Utility.
2. On the System Source tab, enable the Deploy Files»From TestStand Workspace File option.
3. Click the File Browse button located to the right of the From TestStand Workspace File control.
4. Browse to the workspace file you saved in .
5. Click Open .
6. Click the Distributed Files tab.
7. Click Yes in the dialog box that launches to allow the deployment utility to analyze the workspace file and dependent files.
8. Select TestExec.exe in the Distributed Files list. The File Properties section to the right of the Distributed Files list updates for this selection.
9. In the File Properties section on the Distributed Files tab, enable the Create Program Item option.
10. Enter Simple CVI UI in the associated string control to add a shortcut menu item for TestExec.exe .

#### Option A: Configuring the Installer

Complete the following steps to configure the installer.

1. On the Mode tab, select the MSI-based installer output type.
2. On the Installer Options tab, use the Installer Directory control to specify the directory to which the deployment utility copies the installer for the test system and enable the Install TestStand Runtime option.
3. Click Save to save the build as SimpleCVIUI.tsd .
4. Click the Build button to build the installer.

#### Option B: Configuring the Package Distribution

Complete the following steps to configure the installer:

1. On the Mode tab, select the Package-based distribution output type, then select the Package Installer option.
2. On the Package Distribution Options tab, use the Output Directory control to specify the directory to which the deployment utility copies the installer for the test system and enable the Install TestStand Runtime option.
3. Click Save and save the build as SimpleCVIUI.tsd.
4. Click Build to build the installer.

#### Installing the Test System

Complete the following steps to install the test system.

1. To use the installer, copy all the files from the installer directory you specified on the Installer Options tab to the distribution media you want to use or to a shared directory on a network.
2. On the test station computer, insert the distribution media or connect to the network and run the installer executable to start the installer.
3. When the installation completes, complete the following steps to verify that the TestStand Runtime installed correctly.
  - Launch NI Package Manager
  - Select the Installed tab, and enter teststand in the search field.
  - Verify that the TestStand products you included are present in the list of packages.
4. Activate a license when the sequence editor prompts you.

Parent topic:

Common Deployment Scenarios

Related concepts:

- Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand
- TestStand Directory Structure
- Activating and Licensing TestStand

<!--NI_TOPIC bundle=teststand path=distributing-tests-from-a-workspace.html language=enus -->
## TOPIC 00313: Distributing Tests from a Workspace

- bundle_id: `teststand`
- source_path: `distributing-tests-from-a-workspace.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/distributing-tests-from-a-workspace.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to distribute tests from a workspace. Select Tools»Deploy TestStand System in the TestStand Sequence Editor to launch the TestStand Deployment Utility. On the System Source tab, enable the Deploy Files»From TestStand Workspace File option. Click the File Browse button lo

### Distributing Tests from a Workspace

Complete the following steps to distribute tests from a workspace.

1. Select Tools»Deploy TestStand System in the TestStand Sequence Editor to launch the TestStand Deployment Utility.
2. On the System Source tab, enable the Deploy Files»From TestStand Workspace File option.
3. Click the File Browse button located to the right of the From TestStand Workspace File control.
4. Browse to the <TestStand Public>\Examples\Fundamentals\Deployment directory and select the test.tsw workspace file.
5. Click Open .
6. Click the Distributed Files tab.
7. Click Yes in the dialog box that launches to allow the deployment utility to analyze the workspace file and dependent files.
8. Click the Build Status tab and review the Status Log to check for analysis result warnings.

#### Configuring the Installer

Complete the following steps to configure the installer.

1. On the Installer Options tab, use the Installer Directory control to specify the directory to which the deployment utility copies the installer for the test system.
2. Disable the unused.dll option to remove it from the deployment because the example test system does not use this DLL.
3. On the Installer Options tab, enable the Install TestStand Runtime option.
4. Click the Drivers and Components button to launch the Drivers and Components dialog box, in which you can select additional components to include in the installer.
5. Disable the Only display runtime installers option to display the
 TestStand product.
6. Select the TestStand product to include the sequence editor in the TestStand Runtime installation.
7. Click OK to apply the new settings and close the dialog box.
8. Click Save to save the build as test.tsd .
9. Click the Build button to build the installer.

#### Package-based distribution

Complete the following steps to configure the package distribution:

1. On the Mode tab, select the Package-based Distribution output type, then select the Package Installer option.
2. On the Package Distribution Options tab, use the Output Directory control to specify the directory to which the deployment utility copies the installer for the test system.
3. On the Package Distribution Options tab, enable the Install TestStand Runtime option.
4. Click the Dependencies button to launch the Drivers and Components dialog box, in which you can select additional components to include in the distribution.
5. Select the TestStand Sequence Editor product to include the sequence editor in the TestStand Runtime installation.
6. Click OK to apply the new settings and close the dialog box.
7. Click Save to save the build as EnginePackageInstaller.tsd.
8. Click Build to build the package installer.

#### Installing the Test System

Complete the following steps to install the test system.

1. To use the installer, copy all the files from the installer directory you specified on the Installer Options tab to the distribution media you want to use or to a shared directory on a network.
2. On the test station computer, insert the distribution media or connect to the network and run the installer executable to start the installer.
3. When the installation completes, complete the following steps to verify that the TestStand Runtime installed correctly.
  - Launch NI Package Manager
  - Select the Installed tab, and enter teststand in the search field.
  - Verify that the TestStand products you included are present in the list of packages.
4. Activate a license when the sequence editor prompts you.
5. Verify the installation by loading and running <TestStand Public>\Examples\Fundamentals\Deployment\test.seq .

Parent topic:

Common Deployment Scenarios

Related concepts:

- TestStand Directory Structure
- Activating and Licensing TestStand
- Adding Dynamically Called Files to a Workspace
- Distributing a User Interface

<!--NI_TOPIC bundle=teststand path=distributing-xml-reports.html language=enus -->
## TOPIC 00314: Distributing XML Reports

- bundle_id: `teststand`
- source_path: `distributing-xml-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/distributing-xml-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the XML Packaging Utility, which you can launch in the following ways, to distribute XML reports: Select Tools»Package XML/HTML Files for Distribution in the TestStand Sequence Editor. (Windows 10) Select Start»National Instruments»TestStand XML Packaging Utility. This utility copies the local X

### Distributing XML Reports

Use the XML Packaging Utility, which you can launch in the following ways, to distribute XML reports:

- Select Tools»Package XML/HTML Files for Distribution in the TestStand Sequence Editor.
- (Windows 10) Select Start»National Instruments»TestStand XML Packaging Utility .

This utility copies the local XML report files you select, including related style sheets, image files, and referenced files, to a destination directory you specify so you can view the XML report on a computer that does not have TestStand installed.

Parent topic:

XML Reports

Related concepts:

- XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=documenting-custom-user-interfaces.html language=enus -->
## TOPIC 00315: Documenting Custom User Interfaces

- bundle_id: `teststand`
- source_path: `documenting-custom-user-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/documenting-custom-user-interfaces.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Using the NI TestStand User Interfaces document, located at <TestStand>\Doc\UsingtheTestStandUserInterfaces.html, as a starting point for creating custom documentation for user interface applications you customize based on the TestStand full-featured user interface examples. In addit

### Documenting Custom User Interfaces

You can use the Using the NI TestStand User Interfaces document, located at <TestStand>\Doc\UsingtheTestStandUserInterfaces.html, as a starting point for creating custom documentation for user interface applications you customize based on the TestStand full-featured user interface examples.

In addition, the menus for the TestStand full-featured user interface examples include the CommandKind_DefaultHelpMenu_Set constant, which contains a set of commands that corresponds to the typical items in the Help menu of a TestStand application, including support for using the <F1> key to display help for the currently active TestStand User Interface control.

Parent topic:

User Interface Development Best Practices

Related concepts:

- TestStand Directory Structure
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=drag-and-drop-tse.html language=enus -->
## TOPIC 00316: Drag and Drop Step Creation in the TestStand Sequence Editor

- bundle_id: `teststand`
- source_path: `drag-and-drop-tse.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/drag-and-drop-tse.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dragging and Dropping Sequences to Create Sequence Call Steps The TestStand Sequence Editor supports basic drag and drop operations like dragging and dropping of sequences from the Sequences Pane in one Sequence File Window to the Sequences Pane of another Sequence File Window. In addition, the Sequ

### Drag and Drop Step Creation in the TestStand
 Sequence Editor

#### Dragging and Dropping Sequences to Create Sequence Call Steps

The TestStand Sequence Editor supports basic drag and drop operations like dragging and dropping of
sequences from the Sequences Pane in one Sequence File Window to the Sequences Pane of
another Sequence File Window. In addition, the Sequence Editor also supports dragging of
sequences from the Sequences Pane and dropping them as Sequence Call steps into the Steps
Pane. TestStand will create as many Sequence Call steps as the number of sequences that were
dragged. These steps will be configured to call the sequences that were dropped into the Steps
Pane.

You can drop sequences as steps into any sequence in the same sequence file or a different sequence file. In the Sequences View, use your mouse to drag a sequence and hover it over the sequence into which you want to drop it. When that sequence is selected, you can drop the first sequence as a Sequence Call step in the Steps Pane.

To drag and drop any sequence as a step into an already open sequence, press the <ALT> key before dragging the sequence. This action will ensure that the open sequence remains unchanged, and allow you to choose another sequence to drag and drop into the Steps Pane.

Note

#### Modifying the Default Step Type

By default, the drag and drop feature will create Sequence Call steps. You can modify the default step type by changing a configuration file setting contained in the
GeneralEngine.cfg file located in the <TestStand Configuration> directory. The
GeneralEngine.cfg file is saved in .xml format by default.

The GeneralEngine.cfg configuration file contains an XML section named:
StepTypesForGeneratingSeqCallSteps. This section contains the following array
definition, which determines the default step type:

<StepTypesForGeneratingSeqCallSteps classname='Strs'>
<value lbound='[0]' ubound='[0]'>
<value arrayindex='[0]'>SequenceCall</value>
</value>
</StepTypesForGeneratingSeqCallSteps>

To add additional step types from which to choose, increase the bounds of the array definition and add new
elements, as shown below:

<value lbound='[0]' ubound='[2]'>
<value arrayindex='[0]'>SequenceCall</value>
<value arrayindex='[1]'>MyCustomSequenceCall1</value>
<value arrayindex='[2]'>MyCustomSequenceCall2</value>
</value>

Save GeneralEngine.cfg and restart the Sequence Editor for these settings to take effect.

Note

Parent topic:

TestStand Sequence Editor

<!--NI_TOPIC bundle=teststand path=driver-support-for-64-bit-teststand.html language=enus -->
## TOPIC 00317: Driver Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `driver-support-for-64-bit-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/driver-support-for-64-bit-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The bitness of the user mode portion of any driver TestStand loads in-process must match the bitness of TestStand, regardless of which adapter you use to communicate with the driver. As a workaround, 64-bit TestStand can use in-process 32-bit drivers by invoking them indirectly with a remote sequenc

### Driver Support for 64-bit TestStand

The bitness of the user mode portion of any driver TestStand loads in-process must match the bitness of TestStand, regardless of which adapter you use to communicate with the driver. As a workaround, 64-bit TestStand can use in-process 32-bit drivers by invoking them indirectly with a remote sequence call.

Drivers you invoke out-of-process using the LabVIEW Adapter do not have to match the bitness of TestStand. TestStand can invoke LabVIEW code modules using an external (out-of-process) instance of the LabVIEW development system. In this case, the bitness of LabVIEW must match the bitness of the driver, but the bitness of LabVIEW does not have to match the bitness of TestStand. You can make cross-bitness calls using the LabVIEW Adapter only when you use the LabVIEW development system. Code modules that execute using the LabVIEW Run-Time Engine execute in-process and therefore must match the bitness of TestStand.

Similarly, the bitness of an out-of-process COM server you call using the ActiveX/COM Adapter does not have to match the bitness of TestStand.

The bitness of drivers you invoke using the LabWindows/CVI Adapter must match the bitness of TestStand even when run out-of-process using the LabWindows/CVI development environment.

If most or all of the in-process drivers a test system uses are available for only one
 architecture, NI recommends using the bitness of TestStand that matches the drivers.
 If a 64-bit version of a driver you need will be available in a reasonable amount of
 time, consider using 64-bit TestStand and remote sequence calls as a temporary
 workaround to communicate with the 32-bit drivers until the 64-bit version of the
 driver becomes available.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- Remote Execution in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=duplicating-com-references-in-labview.html language=enus -->
## TOPIC 00318: Duplicating COM References in LabVIEW

- bundle_id: `teststand`
- source_path: `duplicating-com-references-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/duplicating-com-references-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When TestStand passes an ActiveX reference to a LabVIEW code module, the reference automatically closes when the called VI completes executing and returns to TestStand. Wiring the reference to a global variable or to a shift register in another VI does not prevent the reference from closing. Consequ

### Duplicating COM References in LabVIEW

When TestStand passes an ActiveX reference to a LabVIEW code module, the reference automatically closes when the called VI completes executing and returns to TestStand. Wiring the reference to a global variable or to a shift register in another VI does not prevent the reference from closing. Consequently, any subsequent use of the original reference within LabVIEW fails.

Use the LabVIEW Variant to Data function to create a duplicate reference for use after calling a VI. Wire the original reference to the type and variant inputs of the Variant to Data function and wire the data output to a global variable, as shown in the following figure.

[IMAGE alt='image' src='GUID-6107E255-FCCA-475F-96CE-65D3E46E7663-a5.png']

The reference in the global variable prevents TestStand from releasing the referenced object until you explicitly close the reference in LabVIEW or until TestStand unloads the code module into which it passed the reference.

When LabVIEW no longer needs the duplicate reference, read the global variable and wire the reference to the LabVIEW Close Reference function to close the reference. Wire the global variable to the LabVIEW Not A Refnum constant to close the global variable, as shown in the following figure.

[IMAGE alt='image' src='GUID-44828A2B-3C30-4738-9A8C-E6C17AD6D354-a5.png']

Parent topic:

Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=dynamic-array-sizing.html language=enus -->
## TOPIC 00319: Dynamic Array Sizing

- bundle_id: `teststand`
- source_path: `dynamic-array-sizing.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/dynamic-array-sizing.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can resize an array during execution. In an expression, use the GetNumElements and SetNumElements expression functions to obtain and modify the upper and lower bounds for a one-dimensional array. For multi-dimensional arrays or to change the number of dimensions in the array, use the GetArrayBou

### Dynamic Array Sizing

You can resize an array during execution. In an expression, use the GetNumElements and SetNumElements expression functions to obtain and modify the upper and lower bounds for a one-dimensional array. For multi-dimensional arrays or to change the number of dimensions in the array, use the GetArrayBounds and SetArrayBounds expression functions. The Operators/Functions tab of the Expression Browser dialog box includes documentation for each expression function.

In a code module, use the PropertyObjectType.ArrayDimensions method to obtain or specify the upper and lower bounds of an array or to change the number of dimensions in the array.

Parent topic:

Specifying Array Sizes

<!--NI_TOPIC bundle=teststand path=dynamically-set-the-client-sequence-file.html language=enus -->
## TOPIC 00320: Dynamically Set the Client Sequence File

- bundle_id: `teststand`
- source_path: `dynamically-set-the-client-sequence-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/dynamically-set-the-client-sequence-file.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to dynamically specify a client sequence file. This example uses the Execution.ClientFile property to set the client sequence file of the process model. Example File Location <TestStand Public>\Examples\Modifying Process Models\Dynamically Setting the Client Seq

### Dynamically Set the Client Sequence File

#### Purpose

This example demonstrates how to dynamically specify a client sequence file. This example uses the Execution.ClientFile property to set the client sequence file of the process model.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying Process Models\Dynamically Setting the
 Client Sequence File\Dynamically Set the Client Sequence
 File.seq

#### Highlighted Features

- TestStand API
- Process model plug-in architecture

#### Major API

- Engine.GetSequenceFileEx
- Execution.ClientFile
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This Example

When you run this example, TestStand prompts you to select Sequence A or Sequence B to run as the client sequence file of the process model. Run the example several times using the Test UUTs or Single Pass Execution entry points and review the report, which includes information relevant to the sequence file you selected.

Open the process model plug-in file, DynamicClientFileExampleModelPluginAddon.seq, associated with this example. Notice that the Model Plugin - Pre UUT sequence sets the Execution.ClientFile property to the file you select at run time.

Note

Complete the following steps to use this example.

1. Open <TestStand Public>\Examples\Modifying Process Models\Dynamically Setting the Client Sequence File\Example -Dynamically Set the Client Sequence File.seq , read the dialog box that appears, and dismiss the dialog box.
2. Select Execute»Single Pass . Select the sequence you want to run when prompted.
3. Review the report that TestStand displays when execution completes.
4. Repeat steps 2-3 but select Execute»Test UUTs to run the sequence using the Test UUTs Execution entry point.

The example copies the DynamicClientFileExampleModelPluginAddon.seq file from the <TestStand Public>\Examples directory to the <TestStand Public>\Components\ModelsPlugins\Addons directory so that the process model automatically executes the Model Plugin - Pre UUT sequence in the file. If you want to set a breakpoint in the Model Plugin - Pre UUT sequence, set the breakpoint in the copy of the file in the <TestStand Public>\Components\ModelsPlugins\Addons directory. If you make any changes to the file in the Addons directory you must change the name of the file because the Example - Dynamically Set the Client Sequence File.seq file overwrites the DynamicClientFileExampleModelPluginAddon.seq file in the Addons directory when you load the Example - Dynamically Set the Client Sequence File.seq file and deletes the DynamicClientFileExampleModelPluginAddon.seq file from the Addons directory when you unload the Example - Dynamically Set the Client Sequence File.seq file.

Entry Point Ignores Client File

Show Entry Point for All Windows

Parent topic:

Examples for Modifying Process Models

Related concepts:

- TestStand Directory Structure
- Process Model Plug-In Architecture
- Execution Entry Points in the Sequential Process Model

<!--NI_TOPIC bundle=teststand path=edit-atlas-call-dialog-box.html language=enus -->
## TOPIC 00321: Edit ATLAS Call Dialog Box

- bundle_id: `teststand`
- source_path: `edit-atlas-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/edit-atlas-call-dialog-box.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select an ATLAS step in a sequence and click the Edit ATLAS Step button on the Step Settings pane to launch the Edit ATLAS Call dialog box, in which you can specify the test program set (TPS) the step executes and the parameters passed between TestStand and the TPS. The Edit ATLAS Call dialog box co

### Edit ATLAS Call Dialog Box

Select an ATLAS step in a sequence and click the Edit ATLAS Step button on the Step Settings pane to launch the Edit ATLAS Call dialog box, in which you can specify the test program set (TPS) the step executes and the parameters passed between TestStand and the TPS.

The Edit ATLAS Call dialog box contains the following options:

- TPS —The file path to the TPS the step executes. The control below the TPS control shows the complete file path of the selected TPS and indicates whether the file was found.
- Run TPS on a Remote Computer —When enabled, the TPS executes on a remote computer. When disabled, the TPS executes on the local computer. This option is disabled by default.
  - Remote Host Name Expression —The name of the remote computer. This option is available only when you enable the Run TPS on a Remote Computer option. You can enter the name in the control or click the Network Browser Dialog Box button to launch the Browse for Computer dialog box and select the remote computer. If you enter the name in the control, you must use quotes around the name because the content of the control is a TestStand expression. You can specify a TestStand expression instead of a hard-coded name. TestStand evaluates the expression at run time to resolve the name of the remote computer. You can click the Expression Browser Dialog Box button to launch the Expression Browser dialog box, in which you can construct the expression.
- Parameters —The parameters passed between TestStand and the ATLAS TPS. TestStand parameters correspond to PAWS global variables, parameters, and results. You must specify parameters to pass only when you pass data between TestStand and the TPS.
- Add Parameter —Adds a new parameter to the list of parameters to pass. Use the Parameter Details section to configure the new parameter.
- Delete Parameter —Deletes the selected parameter from the list of parameters.
- Move Parameter Up —Moves the selected parameter up in the list of parameters.
- Move Parameter Down —Moves the selected parameter down in the list of parameters.
- Parameter Details —Specifies the following information for the selected parameter in the list of parameters:
  - Name —The name of the parameter.
  - Type —The data type for the number. The type can be a number, string, or Boolean.
  - Mode —Specifies if the data type mode is read, write, or read and write.
  - Global Variable —When enabled, the parameter is a PAWS global variable or a PAWS parameter/result.
  - Value Expression —The value expression for the parameter. The sequence context used to evaluate parameter values is the step context.

Note

- If you can specify the file path to the TPS using relative or absolute paths, TestStand launches a File Not Found dialog box that contains options for specifying the file location.
- You must properly configure the DCOM settings for the PAWS Run-Time Server (RTS) on both the host and remote computers for remote execution to work. Refer to PAWS documentation for more information about configuring the PAWS RTS for remote execution.
- You must specify the name of the parameter value exactly as the TPS and TPS server expect. The TPS server allows verification of parameter names prior to execution. The ATLAS custom step type generates an error if the parameter cannot be read or written.
- TestStand updates properties referred in the Value Expression control with the parameter values the TPS server passes after TestStand calls the TPS server when executing an ATLAS step.

Parent topic:

ATLAS Step Type

Related concepts:

- ATLAS Step Type
- Sequence Context

<!--NI_TOPIC bundle=teststand path=edit-java-call-dialog-box.html language=enus -->
## TOPIC 00322: Edit Java Call Dialog Box

- bundle_id: `teststand`
- source_path: `edit-java-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/edit-java-call-dialog-box.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select a Java Methods and Static Methods step in a sequence and click the Edit Call or Edit Static Call button on the Step Settings pane to launch the Edit Java Call dialog box, in which you can configure the step to call the appropriate Java method. The Edit Java Call dialog box contains the follow

### Edit Java Call Dialog Box

Select a Java Methods and Static Methods step in a sequence and click the Edit Call or Edit Static Call button on the Step Settings pane to launch the Edit Java Call dialog box, in which you can configure the step to call the appropriate Java method.

The Edit Java Call dialog box contains the following options:

- Java Class to Load —The Java class that contains the method to call. If TestStand cannot locate the file, TestStand launches the File Class Not Found dialog box. Select the Add the directory containing the file you selected to the list of search directories option and click OK . Do not select Use an absolute path for the file you selected . The control below the Java Class to Load control displays the complete file path of the specified class. If the file is incorrect, add the appropriate directory to the list of TestStand search directory paths or move the directory up to a higher position in the list of search paths. Note Always use a relative path for the Java class to load. If you specify an absolute path, the Java virtual machine (JVM) cannot locate the class name and you receive a -1000 Class Not Found error.
- Java Method —The name of the method to call. Specify the name after you select the Java class that contains the method.
- Parameters —Contains the following options for creating and configuring parameters to pass to the specified method:
  - Method Parameter —The list of parameters to pass to the specified method. Select a parameter from the ring control to specify the argument type and value expression for the parameter. The order of parameters must match the order the Java method header uses in the parameter list. If no parameters are to be passed, delete all parameters from the list.
  - New —Adds a new parameter to the list of parameters.
  - Argument Type —The type of the parameter. The available types are the Java types represented in the Java method header.
  - Delete —Deletes the selected parameter from the list of parameters.
  - Value Expression —The value expression for the parameter. If the value to be passed is stored in a TestStand variable, click Browse to locate the variable. Otherwise, enter the value of the parameter. You must verify that the type of the value or TestStand variable is compatible with the Java parameter type. Note Enclose literal strings and characters in double quotes.
- Return Value —Contains the following options for specifying a return value for the specified method:
  - Return Value —The return value.
  - Argument Type —The type of the return value. The type must match the variable that stores the return value, or the return value must be compatible for the appropriate comparisons to occur. For example, the Numeric Limit Test steps require the return value to be stored in Step.Result.Numeric , the String Value Test steps require the return value to be stored in Step.Result.String , and the Pass Fail Test steps require the return value to be stored in Step.Result.PassFail . For Action steps, select void for the argument type if no return value exists.
  - Value Expression —The value expression for the return value, which TestStand stores in a variable. Click Browse to locate the variable. You must verify that the type of the value or TestStand variable is compatible with Java types.

Parent topic:

Java Step Types

Related concepts:

- Java Step Types
- Search Directories

<!--NI_TOPIC bundle=teststand path=editing-custom-rules-and-analysis-modules.html language=enus -->
## TOPIC 00323: Editing Custom Rules and Analysis Modules

- bundle_id: `teststand`
- source_path: `editing-custom-rules-and-analysis-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/editing-custom-rules-and-analysis-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you edit a custom rule and corresponding analysis module, the changes apply to all projects. Before you edit a VI, .NET assembly, or DLL analysis module, you must unload the analysis module from memory. You can unload all analysis modules by right-clicking anywhere on the Analysis Modules tab o

### Editing Custom Rules and Analysis Modules

When you edit a custom rule and corresponding analysis module, the changes apply to all
 projects.

Before you edit a VI, .NET assembly, or DLL analysis module, you must unload the analysis
 module from memory. You can unload all analysis modules by right-clicking anywhere on
 the Analysis Modules tab of the Configure Sequence Analyzer Available Rules dialog box
 and selecting Unload All Modules from the context menu. In the
 TestStand Sequence Editor, you can also select File»Unload All
 Modules to unload all modules, including analysis modules, from memory.

Parent topic:

TestStand Sequence Analyzer

Related information:

- Configure Sequence Analyzer Available Rules Dialog Box

<!--NI_TOPIC bundle=teststand path=editing-stand-alone-vis.html language=enus -->
## TOPIC 00324: Editing Stand-alone VIs

- bundle_id: `teststand`
- source_path: `editing-stand-alone-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/editing-stand-alone-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations and requirements for editing VIs when you decide whether to use stand-alone VIs in a TestStand system: NI recommends that you save all code modules in one version of LabVIEW. VIs saved in different versions of LabVIEW cannot share data when executed using the L

### Editing Stand-alone VIs

Consider the following recommendations and requirements for editing VIs when you decide whether to use stand-alone VIs in a TestStand system:

- NI recommends that you save all code modules in one version of LabVIEW. VIs saved in different
 versions of LabVIEW cannot share data when executed using the LabVIEW Run-Time
 Engine (RTE).
- Loading multiple stand-alone VIs can negatively impact performance, especially if the test sequences load VIs dynamically.
- Using multiple stand-alone VIs can result in name conflicts. LabVIEW does not support loading multiple VIs with the same name from different locations. Use LabVIEW project libraries and packed project libraries to add a namespace to the VIs and avoid name conflicts.
- NI does not recommend editing packaged VIs on a deployed system because unexpected errors, such
 as broken VIs or run-time errors, can occur. NI recommends rebuilding and
 redeploying the deployment image in this situation. Analysis and instrument
 drivers are examples of VIs that use project libraries.

Parent topic:

Organizing Test Program Files with Stand-alone VIs

Related concepts:

- Organizing Test Program Files with Stand-alone VIs
- Organizing Test Program Files with LabVIEW Project Libraries
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Deploying TestStand Systems
- Creating Deployments
- Deploying Stand-alone VIs
- Updating and Patching Stand-alone VIs

<!--NI_TOPIC bundle=teststand path=editing-steps-in-a-sequence.html language=enus -->
## TOPIC 00325: Editing Steps in a Sequence

- bundle_id: `teststand`
- source_path: `editing-steps-in-a-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/editing-steps-in-a-sequence.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add a step to a sequence, configure the step to call a code module or subsequence, and configure the properties of a step. The Insertion Palette contains a set of predefined step types you can add to sequences. Step types define the standard behavior and a set of step properties for each ste

### Editing Steps in a Sequence

You can add a step to a sequence, configure the step to call a code module or subsequence, and configure the properties of a step.

The Insertion Palette contains a set of predefined step types you can add to sequences. Step types define the standard behavior and a set of step properties for each step of that type. All steps of the same type have the same properties, but the values of the properties can differ.

When you build sequence files, you can also use the Templates list in the Insertion Palette. Use the Templates list to hold copies of steps, variables, and sequences you reuse during the development of sequence files. For example, you can add a step that calls a specific LabVIEW VI you typically use or a sequence that contains common setup steps, cleanup steps, and local variables.

Note

<TestStand Public>\Tutorial\Solution

#### Adding a New Step

Complete the following steps to add a Pass/Fail Test step to a sequence and configure the step to call a function in a LabWindows/CVI DLL code module by specifying the module adapter to use. TestStand does not need the source code to invoke a DLL code module. Instead, TestStand uses module adapters to determine the type of code module, how to call the code module, and how to pass parameters to the code module.

1. Open <TestStand Public>\Tutorial\Computer.seq .
2. Select File»Save <filename> As and save the sequence file as Computer2.seq in the <TestStand Public>\Tutorial directory. Note When you must save a file, this tutorial specifies the suggested name. If other users will use the tutorial files on the same computer, save the files with unique filenames.
3. Select the LabWindows/CVI adapter from the Adapter ring control above the Step Types list to specify the module adapter the step uses. The adapter you select applies only to the step types that can use the module adapter. 
 Note If you left the Tutorial.tsw workspace open after completing the Loading and Running Sequences tutorial, you might need to click the Insertion Palette tab to show the Insertion Palette. 
 When you insert a step in a sequence, TestStand configures the step to use the adapter you selected from the Insertion Palette. The icon for the step reflects the adapter you selected. When you select <None> as the adapter and then insert a step, the new step does not call a code module. Use the General panel on the Properties tab of the Step Settings pane to change the associated adapter after you insert the step.
4. On the Insertion Palette, select Tests»Pass/Fail Test and drag the step below the RAM step on the Steps pane to add a Pass/Fail Test step. By default, the name of the new step is Pass/Fail Test. 
 Note You can also create steps by right-clicking the Steps pane, selecting Insert Step from the context menu, and selecting the type of step you want to insert. 
 Use a Pass/Fail Test step to call a code module that returns a pass/fail determination. After the code module executes, the Pass/Fail Test step evaluates a Boolean expression to determine whether the step passed or failed.
5. Rename the new step Video Test by selecting the step on the Steps pane and pressing the <F2> key.
6. Save the changes. Leave the sequence file open for the next tutorial.

#### Specifying the Code Module

Complete the following steps to specify the code module the step executes and to specify the parameters for a function in the code module for the Computer2.seq sequence file you created in the previous tutorial.

1. Select the Video Test step and click the Module tab of the Step Settings pane.
2. Click the Browse button located to the right of the Module control, select <TestStand Public>\Tutorial\computer.dll , and click Open . When you select a DLL, TestStand reads the type library or exported information of the DLL and lists the functions TestStand can call in the Function ring control.
3. Select VideoTest from the Function ring control. TestStand uses the prototype information stored in the type library or the exported information of the DLL to populate the Parameters Table.
4. In the Value Expression column of the result parameter, enter Step.Result.PassFail . When TestStand returns from calling the VideoTest function during execution, TestStand assigns the value from the result parameter to the Step.Result.PassFail property of the step.
5. Save the changes. Leave the sequence file open for the next tutorial.

For more information about calling code modules, refer to the following tutorials:

- Calling LabVIEW VIs
- Calling LabWindows/CVI Code Modules

#### Configuring Step Properties

Note

Configure»Station Options

Execution

OK

Each step in a sequence contains properties. All steps have a common set of properties that determine the following attributes:

- When to load the code module for the step
- When to execute the step
- What information TestStand examines to determine the status of the step
- Whether TestStand executes the step in a loop
- What conditional actions occur after a step executes

Steps can also contain additional properties the step type defines. Use the Properties tab of the Step Settings pane to examine and modify the values of properties of a step.

Complete the following steps to examine and modify step properties in the Computer2.seq sequence file you created in the previous tutorial.

1. Select the Video Test step on the Steps pane and click the Properties tab of the Step Settings pane.
2. Click Preconditions on the Properties tab to show the Preconditions panel. A precondition is a set of conditions for a step that must evaluate to True for TestStand to execute the step during the normal flow of execution in a sequence.
3. Complete the following steps to define a precondition so the Video Test step executes only if the Power On step passes.
  1. Click the Precondition Builder button, located to the right of the Precondition Expression control on the Preconditions panel, to launch the Precondition Builder dialog box.
  2. In the Insert Step Status section, select the Power On step from the list of step names for the Main step group and click the Insert Step Pass button. The Conditions control now contains the string PASS Power On , which indicates that the step executes only if the Power On step passes.
  3. Click OK to close the Precondition Builder dialog box and confirm that the Preconditions panel displays the expression you created.
4. Click Post Actions on the Properties tab of the Step Settings pane to show the Post Actions panel, on which you can specify what type of action occurs after the step executes. You can make the action conditional on the pass/fail status of the step or on any custom condition expression.
5. Select Terminate execution from the On Fail ring control.
6. Click Looping on the Properties tab of the Step Settings pane to show the Looping panel, on which you can configure an individual step to run repeatedly in a loop when the step executes. Use the Loop Type ring control to select the type of looping for the step. 
 TestStand determines the final status of the step based on the number of passes, failures, or loop iterations that occur.
7. On the Looping panel, enter the following values into the corresponding controls. When you change the value of a property, TestStand shows the new value in bold to indicate that it differs from the default value. 
 
 Using these settings, TestStand executes the Video Test step 10 times and sets the overall status for the step to Failed if fewer than 8 of the 10 iterations pass.
  - Loop Type —Fixed number of loops
  - Number of Loops — 10
  - Loop result is Fail if —< 80%
8. Confirm that the Settings column on the Steps pane of the Sequence File window shows that the Video Test step contains Loop, Precondition, and Post Action settings. Use the tooltip in the Settings column to verify the values for each setting.
9. Save the changes and select Execute»Single Pass .
10. Select the Video test to fail and click Done . The sequence immediately terminates after calling the Video Test step 10 times in a loop. TestStand records the result of each loop iteration in the report.
11. Close the Execution window.

#### Calling Subsequences

Use the Sequence Call step to call another sequence in the current sequence file or in another sequence file.

Complete the following steps to add a Sequence Call step to the Computer2.seq sequence file you created in the previous tutorial.

1. Insert a Sequence Call step after the Power On step on the Steps pane and rename the step CPU Test .
2. On the Module tab of the Step Settings pane for the CPU Test step, click the Browse button located to the right of the File Pathname control and select <TestStand Public>\Tutorial\CPU.seq to specify the sequence the step invokes.
3. Select MainSequence from the Sequence ring control on the Module tab of the Step Settings pane.
4. Save the changes and double-click the CPU Test step to open the sequence and show the MainSequence of CPU.seq in a new Sequence File window.
5. Select Execute»Run MainSequence . Examine the execution of CPU.seq so you can recognize it later when you execute the Computer2.seq sequence file that calls CPU.seq .
6. Close the Execution window and the CPU.seq Sequence File window.
7. In the Computer2.seq Sequence File window, select Execute»Single Pass .
8. Select a test to fail and click Done . After the sequence executes, review the test report. TestStand logs the results of the steps in the subsequence in addition to the steps from the parent sequence.
9. Close the Execution window. Leave the Computer2.seq sequence file open for the next tutorial.

#### Using Step Templates

The Insertion Palette contains the Step Types list and the Templates list. Use the Templates list to hold copies of steps, variables, and sequences you reuse during the development of sequence files. For example, you can add a step that calls a specific LabVIEW VI you typically use or a sequence that contains common setup steps, cleanup steps, and local variables.

Drag steps from the Steps pane, variables from the Variables pane, and sequences from the Sequences pane and drop them on the Templates list to add steps, variables, or sequences to the Templates list. Use the context menu to rename, copy, paste, delete, import, and export the items in the Templates list. You can drag and drop items to rearrange the list. Select Insert Folder from the context menu to add folders to the list. TestStand stores the settings for the Templates list, including any modifications to the list, in the <TestStand Application Data>\Cfg\Templates.ini file.

You cannot directly modify templates. Drag a sequence, step, or variable from the Templates list to a sequence file to edit the item. Then, drag the item back to the Templates list and delete the original item from the Templates list.

#### Inserting a Template Step

Complete the following steps to import a set of template steps to the Insertion Palette, insert a step from the Templates list in a sequence, and add a new step to the Templates list in the Computer2.seq sequence file you created in the previous tutorial.

1. Right-click the Steps folder in the Templates list of the Insertion Palette and select Import from the context menu.
2. Navigate to the <TestStand Public>\Tutorial directory, select Tutorial Templates.ini , and click Open . The sequence editor adds a Tutorial folder under the Steps folder.
3. Expand the Tutorial subfolder of the Steps folder to view the following imported template steps:
  - Retry if Previous Step Fails —A Message Popup step that prompts you to retry the previous step on failure.
  - Open Notepad —A Call Executable step configured to launch the Microsoft Notepad application.
  - Output Message —A statement step that logs an output message in which the logged text is the step name.
  - Waveform Popup —A step that calls the WaveformGraphPopup function in the LabWindows/CVI user interface library.
4. In the Templates list, select Retry if Previous Step Fails , drag the step below the Power On step on the Steps pane, and rename the step Retry Power On .
5. Save the changes and select Execute»Single Pass .
6. Select the Power On test to fail and click Done . TestStand executes the Retry Power On step and launches the Step 'Power On' Failed dialog box because the precondition for the step determined that the previous Power On step failed.
7. Click Retry in the Step 'Power On' Failed dialog box to execute the Power On step again. The Power On step fails again, and TestStand launches the Step 'Power On' Failed dialog box again.
8. Click Continue in the Step 'Power On' Failed dialog box to continue the execution.
9. Review the report. Notice that the Power On step executed twice, and the second call to Retry Power On continued the execution.
10. Close the Execution window. Leave the sequence file open for the next tutorial.

#### Creating a Template
 Step

Complete the following steps to update the Retry Power On step so
 that it automatically selects the Continue button if you do
 not respond to the prompt in the Computer2.seq sequence file you
 created in the previous tutorial.

1. In the Sequence File window, select the Retry Power On 
 step on the Steps pane.
2. Click the Text and Buttons tab of the Step Settings
 pane.
3. In the Button Options section, select Button 2 from the
 Timeout Button ring control.
4. Enter 20 in the Time To Wait control to instruct the step to
 wait for 20 seconds before continuing. This technique is useful if an operator
 is not present to acknowledge a non-critical message during testing.
5. Save the changes and select Execute»Single Pass .
6. Select the Power On test to fail and click
 Done . TestStand executes the Retry Power On step and
 launches the Step 'Power On' Failed dialog box. Do not take any action in this
 dialog box. When the timeout reaches zero, the execution continues as if you
 clicked Continue .
7. In the Sequence File window, drag the Retry Power On step into the Tutorial
 folder in the Templates list.
8. Rename the new template step Timeout Retry . You can use the new
 template step in subsequent development. The sequence editor automatically saves
 the templates list when you shut down the sequence editor.
9. Close the Computer2.seq sequence file and the Execution
 window.
10. You no longer need the Tutorial folder in the Templates list, and you can delete
 the folder if you want. Right-click the Tutorial folder
 in the Templates list and select Delete from the context
 menu to remove the folder.

Parent topic:

Getting Started with TestStand

Related concepts:

- Calling LabVIEW VIs
- Calling LabWindows/CVI Code Modules

<!--NI_TOPIC bundle=teststand path=editing-vis-in-labview-packed-project-librari.html language=enus -->
## TOPIC 00326: Editing VIs in LabVIEW Packed Project Libraries

- bundle_id: `teststand`
- source_path: `editing-vis-in-labview-packed-project-librari.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/editing-vis-in-labview-packed-project-librari.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations and requirements for editing VIs when you decide whether to use LabVIEW packed project libraries in a TestStand system: NI recommends creating an architecture with multiple packed project libraries that group similar sets of VIs together so that you can update

### Editing VIs in LabVIEW Packed Project Libraries

Consider the following recommendations and requirements for editing VIs when you decide whether to use LabVIEW packed project libraries in a TestStand system:

- NI recommends creating an architecture with multiple packed project libraries that group similar
 sets of VIs together so that you can update code more easily.
- You cannot edit VIs inside packed project libraries. You must have the source VIs and the project that contains the build specification for the packed project library to make a change to the packed project library. To modify a VI stored in a packed project library, you must modify the source VI and rebuild the packed project library, and replace the older packed project library with the newer version.
- NI recommends enabling the Callers adapt at run time to Exported VI connector pane
 state option on the Connector Pane State page of the Packed
 Library Properties dialog box in the packed project library build specification
 in LabVIEW when using other LabVIEW VIs to call exported VIs stored in the
 LabVIEW packed project library. When you enable this option, VI callers of a
 packed project library can adapt to inplaceness changes in an exported VI
 without having to recompile.
- NI recommends that you wait until you have finished making major changes to VIs before building
 the packed project library. If VIs that use the packed project library are in
 the same project, you can replace all instances of VIs in the project library
 with a call to a built packed project library in the LabVIEW Project Explorer
 window.
- You cannot load a VI stored in a packed project library independently of other items in the same packed project library. LabVIEW loads every VI in the packed project library when you call the first VI, resulting in a longer initial load time and higher memory usage. LabVIEW loads subsequent VIs immediately.
- When you call the first VI in a packed project library, LabVIEW consolidates types in all VIs in the packed project library to reduce the time required to load every VI inside the packed project library. This behavior is faster than loading the same VIs if they were stored outside of the packed project library. Packed project libraries are also faster to load because they consist of a single file, so the test system does not have to search the disk for additional files.
- Packed project libraries support debugging when built with debugging information. However, including the debugging information makes the packed project library larger and slightly slower to execute. Consider benchmarking the differences in size and execution speed to determine the impact of including the debugging information in the packed project library.

Parent topic:

Organizing Test Program Files with LabVIEW Packed Project Libraries

Related concepts:

- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Organizing Test Program Files with LabVIEW Projects
- Organizing Test Program Files with LabVIEW Project Libraries
- Deploying TestStand Systems
- Deploying VIs in LabVIEW Packed Project Libraries
- Updating and Patching VIs in LabVIEW Packed Project Libraries

<!--NI_TOPIC bundle=teststand path=editing-vis-in-labview-projects.html language=enus -->
## TOPIC 00327: Editing VIs in LabVIEW Projects

- bundle_id: `teststand`
- source_path: `editing-vis-in-labview-projects.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/editing-vis-in-labview-projects.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations and requirements for editing VIs when you decide whether to use LabVIEW projects in a TestStand system: TestStand supports VIs organized in folders, LabVIEW project libraries, LabVIEW libraries, or LabVIEW packed project libraries defined in the LabVIEW project

### Editing VIs in LabVIEW Projects

Consider the following recommendations and requirements for editing VIs when you decide whether to use LabVIEW projects in a TestStand system:

- TestStand supports VIs organized in folders, LabVIEW project libraries, LabVIEW libraries, or LabVIEW packed project libraries defined in the LabVIEW project under the My Computer target. LabVIEW creates an application instance for each target in a LabVIEW project, including My Computer .
- VIs you call from TestStand in the context of a LabVIEW project cannot use global variables to share data with VIs outside of that project because when you open a VI specified in a LabVIEW project, the VI opens in the application instance for the project. LabVIEW also creates a main application instance that contains open VIs not included in a project and VIs you did not open from a project. Additionally, LabVIEW loads shared libraries in a unique application instance, which prevents naming conflicts with the VIs in the shared library or with VIs outside of the shared library.
- NI recommends using shared variables to transfer data between VIs executing in more than one
 project. Note 
 TestStand supports automatically deploying and undeploying shared variables
 defined in LabVIEW projects.

Parent topic:

Organizing Test Program Files with LabVIEW Projects

Related concepts:

- Organizing Test Program Files with LabVIEW Projects
- Organizing Test Program Files with LabVIEW Project Libraries
- Organizing Test Program Files with LabVIEW Libraries
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Deploying Network-Published Shared Variables
- Deploying VIs in LabVIEW Projects
- Updating and Patching VIs in LabVIEW Projects

<!--NI_TOPIC bundle=teststand path=editor-versus-operator-interface-applications.html language=enus -->
## TOPIC 00328: Editor Versus Operator Interface Applications

- bundle_id: `teststand`
- source_path: `editor-versus-operator-interface-applications.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/editor-versus-operator-interface-applications.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An Editor application permits users to create, edit, and save sequence files. An Operator Interface application permits users only to run sequences. Use the TestStand User Interface (UI) Controls to create Editor applications, Operator Interface applications, and applications that can switch between

### Editor Versus Operator Interface Applications

An Editor application permits users to create, edit, and save sequence files. An Operator Interface application permits users only to run sequences.

Use the TestStand User Interface (UI) Controls to create Editor applications, Operator Interface applications, and applications that can switch between Editor Mode and Operator Mode.

Parent topic:

Getting Started with User Interface Development

Related concepts:

- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=effectively-using-labview-with-teststand.html language=enus -->
## TOPIC 00329: Effectively Using LabVIEW with TestStand

- bundle_id: `teststand`
- source_path: `effectively-using-labview-with-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/effectively-using-labview-with-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to use advanced features of LabVIEW to organize and deploy VIs for a TestStand system. These LabVIEW features can impact the performance, robustness, and deployment capabilities of a test system. Consider the requirements and organization of the test system when using these features. TestS

### Effectively Using LabVIEW with TestStand

Learn how to use advanced features of LabVIEW to organize and deploy VIs for a TestStand system.
 These LabVIEW features can impact the performance, robustness, and deployment
 capabilities of a test system. Consider the requirements and organization of the
 test system when using these features.

Note

.vim

Related concepts:

- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=enabling-large-address-aware-functionality-in.html language=enus -->
## TOPIC 00330: Enabling Large Address Aware Functionality in 32-bit TestStand

- bundle_id: `teststand`
- source_path: `enabling-large-address-aware-functionality-in.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enabling-large-address-aware-functionality-in.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because 32-bit Microsoft Windows applications can use only 2 GB of memory by default, you might encounter memory limits when developing memory-intensive TestStand applications. To increase the amount of memory 32-bit TestStand can use, you can configure 32-bit TestStand to be large address aware. Th

### Enabling Large Address Aware Functionality in 32-bit TestStand

Because 32-bit Microsoft Windows applications can use only 2 GB of memory by default, you might encounter memory limits when developing memory-intensive TestStand applications. To increase the amount of memory 32-bit TestStand can use, you can configure 32-bit TestStand to be large address aware.

Note

When you enable the Large Address Aware flag for an executable file, you increase the maximum amount of memory available to a 32-bit application from 2 GB of memory to 3 GB of memory on 32-bit Windows, and up to 4 GB of memory on 64-bit Windows.

If you are using 32-bit Windows, you must configure Windows to support large address aware applications to access the additional memory. Refer to the Microsoft Developer Network website for additional information about configuring Windows to be large address aware using the Microsoft 4-Gigabyte Tuning feature.

Note

Visit ni.com/info and enter the Info Code exfu2i to access the
 NI support article 5ZREUK2G, Using the Large Address Aware Flag With TestStand
 Applications, for more information about using the large address aware
 functionality.

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=teststand path=enabling-or-disabling-editing-of-ni-modelplug.html language=enus -->
## TOPIC 00331: Enabling or Disabling Editing of NI_ModelPlugin Properties

- bundle_id: `teststand`
- source_path: `enabling-or-disabling-editing-of-ni-modelplug.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enabling-or-disabling-editing-of-ni-modelplug.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Although you can provide sub-dialog boxes for plug-in end users to edit plug-in-specific option properties, plug-in end users can also use the parent configuration dialog box to edit the following properties common to all plug-ins: Base.Enabled Base.DisplayNameExpression Base.NewThread Base.Complete

### Enabling or Disabling Editing of NI_ModelPlugin Properties

Although you can provide sub-dialog boxes for plug-in end users to edit plug-in-specific option properties, plug-in end users can also use the parent configuration dialog box to edit the following properties common to all plug-ins:

- Base.Enabled
- Base.DisplayNameExpression
- Base.NewThread
- Base.CompleteBeforeNextUUT
- PluginSpecific.Options
- PluginSpecific.AdditionalOptions

You can restrict plug-in end users from editing these properties by modifying the value of the NI.EnabledExpression expression (string) attribute that contains a Boolean expression for the property for which you want to restrict editing. For example, the expression CurrentUserHasPrivilege("ConfigReport") specifies that only users with the ConfigReport user privilege can edit the property. Apply this change to the FileGlobal instance of the property, located within the FileGlobals.ModelPluginComponentDescription.Default container.

Parent topic:

Process Model Plug-In Architecture

<!--NI_TOPIC bundle=teststand path=enabling-or-disabling-table-indentation-in-an.html language=enus -->
## TOPIC 00332: Enabling or Disabling Table Indentation in an ATML Test Results 2.02 Report

- bundle_id: `teststand`
- source_path: `enabling-or-disabling-table-indentation-in-an.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enabling-or-disabling-table-indentation-in-an.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to enable or disable the indentation of all tables the report that uses the TR_horizontal.xsl report style sheet displays. By default, the report displays indentation of all tables. Open the TR_horizontal.xsl file. Search for the gIndentTables XSLT variable. Set the vari

### Enabling or Disabling Table Indentation in an ATML Test Results 2.02 Report

Complete the following steps to enable or disable the indentation of all tables the report that uses the TR_horizontal.xsl report style sheet displays. By default, the report displays indentation of all tables.

1. Open the TR_horizontal.xsl file.
2. Search for the gIndentTables XSLT variable.
3. Set the variable to false() to disable the indentation of all tables. You can reset the variable to true() to enable displaying indentation.

Parent topic:

Customizing the ATML Test Results 2.02 Report Style Sheet

<!--NI_TOPIC bundle=teststand path=enforcing-user-privileges.html language=enus -->
## TOPIC 00333: Enforcing User Privileges

- bundle_id: `teststand`
- source_path: `enforcing-user-privileges.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enforcing-user-privileges.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most of the dialog boxes you can launch using methods in the TestStand Engine verify user privileges for you and disable controls the user does not have permission to access. However, most of the TestStand API does not enforce privileges to avoid overly restrictive situations. For example, if the Te

### Enforcing User Privileges

Most of the dialog boxes you can launch using methods in the TestStand Engine verify user privileges for you and disable controls the user does not have permission to access. However, most of the TestStand API does not enforce privileges to avoid overly restrictive situations. For example, if the TestStand API strictly enforced the execution privilege, the application could not run the LoginLogout callback sequence to allow a user to log in.

The application developer is responsible for enforcing user privileges. TestStand provides a predefined set of user privileges and an Engine method you can call to verify whether the current user has a specific privilege. To determine whether to disable controls or menu items in the application, call the Engine.CurrentUserHasPrivilege method. Pass the value of one of the UserPrivileges string constants for the privilegeName parameter. If no user is currently logged in, the Engine.CurrentUserHasPrivilege method always returns False. If privilege checking is disabled, the Engine.CurrentUserHasPrivilege method always returns True.

Parent topic:

Writing an Application with the TestStand Engine API

Related concepts:

- Privileges

<!--NI_TOPIC bundle=teststand path=engine-callback.html language=enus -->
## TOPIC 00334: Engine Callback

- bundle_id: `teststand`
- source_path: `engine-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/engine-callback.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Sequential, Parallel, and Batch process models include the following Engine callback: ProcessModelPostResults—The process model enables this callback when you enable the On-The-Fly option for any process model plug-in. TestStand calls this Engine callback periodically as it collects results.

### Engine Callback

The Sequential, Parallel, and Batch process models include the following Engine callback:

- ProcessModelPostResults —The process model enables this callback when you
 enable the On-The-Fly option for any process model plug-in. TestStand calls this
 Engine callback periodically as it collects results.

Parent topic:

Features Common to All TestStand Process Models

Related concepts:

- Sequential Process Model
- Parallel Process Model
- Batch Process Model
- On-the-Fly Report Generation

<!--NI_TOPIC bundle=teststand path=engine-callbacks.html language=enus -->
## TOPIC 00335: Engine Callbacks

- bundle_id: `teststand`
- source_path: `engine-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/engine-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand specifies a set of Engine callback sequences it invokes at specific points during execution. Use Engine callbacks to direct TestStand to call certain sequences before and after the execution of individual steps, before and after interactive executions, after loading a sequence file, and be

### Engine Callbacks

TestStand specifies a set of Engine callback sequences it invokes at specific points during execution.

Use Engine callbacks to direct TestStand to call certain sequences before and after the execution of individual steps, before and after interactive executions, after loading a sequence file, and before unloading a sequence file. Because the TestStand Engine controls the execution of steps and the loading and unloading of sequence files, TestStand defines the set of Engine callbacks and their names.

Parent topic:

Result Collection

Related concepts:

- List of Engine Callbacks
- Interactively Executing Steps
- Modifying Engine Callbacks

<!--NI_TOPIC bundle=teststand path=entry-point-sequences.html language=enus -->
## TOPIC 00336: Entry Point Sequences

- bundle_id: `teststand`
- source_path: `entry-point-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/entry-point-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can invoke Execution entry point sequences and Configuration entry point sequences from the TestStand Sequence Editor or User Interface menus to run client files or to configure model settings. Each entry point is a sequence in the process model file. Execution Entry Points Execution entry point

### Entry Point Sequences

You can invoke Execution entry point sequences and Configuration entry point sequences from the TestStand Sequence Editor or User Interface menus to run client files or to configure model settings. Each entry point is a sequence in the process model file.

#### Execution Entry Points

Execution entry points run test programs typically by calling the MainSequence callback in the client sequence file. The Sequential, Parallel, and Batch process models contain the following Execution entry points:

- Test UUTs —Tests and identifies multiple UUTs or batches of UUTs in a loop.
- Single Pass —Tests one UUT or a single batch of UUTs without identifying the UUTs.

By default, the Execute menu lists Execution entry points only when the active window contains a sequence file that uses the process model.

Configuration entry points configure a feature of the process model and usually save the configuration information in a .ini file the <TestStand Application Data>\Cfg directory. The process models contain the following Configuration entry points:

- Configure Result Processing —Launches the Result Processing dialog box, in which you enable or disable the installed built-in and custom result processing plug-ins in the active result processing configuration and also configure how the plug-ins process test results. Use the built-in reporting, database, and offline results plug-ins to generate reports, log data to databases, and store results in compact offline result files for processing later, respectively. By default, you can configure the following result processors:
  - Database —Configure a database results processor to enable UUT result logging and configure the schema for mapping TestStand results to database tables and columns.
  - Report —Configure a reports results processor to enable UUT report generation and configure the report type and contents of the report files.
  - Offline Results File —Configure an offline results processor to enable storing of TestStand results in a compact raw result format ( .tsr ) for offline processing at a time other than when sequence execution occurs or on a different computer, and to configure the location of the offline results files.
- Configure Model Options —Launches the Model Options dialog box, in which you configure the number of test sockets and other process model-related options.

#### Configuration Entry Points

By default, the Configure menu lists the Configuration entry points.

Parent topic:

Modifying Process Model Sequence Files

Related concepts:

- Model Callbacks in the Batch Process Model
- Sequential Process Model
- Parallel Process Model
- Batch Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=entry-points.html language=enus -->
## TOPIC 00337: Entry Points

- bundle_id: `teststand`
- source_path: `entry-points.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/entry-points.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A process model defines a set of entry points, and each entry point is a sequence in the process model file that invokes a test sequence file. Defining multiple entry points in a process model provides the test station operator different ways to invoke a Main sequence or configure the process model.

### Entry Points

A process model defines a set of entry points, and each entry point is a sequence in the process model file that invokes a test sequence file. Defining multiple entry points in a process model provides the test station operator different ways to invoke a Main sequence or configure the process model.

The sequence for a process model entry point can contain calls to DLLs, subsequences, Goto steps, and so on. You can specify Execution entry points or Configuration entry points.

Parent topic:

Process Models

Related concepts:

- Entry Point Sequences
- Using Execution Entry Points
- Configuration Entry Points

<!--NI_TOPIC bundle=teststand path=enumeration-options.html language=enus -->
## TOPIC 00338: Enumeration Options

- bundle_id: `teststand`
- source_path: `enumeration-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enumeration-options.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Strict vs. Loose Enumerations A TestStand enumeration can be either strict or loose. A loose enumeration can take on any numeric value. Enums in C, C++, and C# can be described loose in this sense. A strict enumeration can take on only those values defined by its enumerators. Attempting to set a str

### Enumeration Options

#### Strict vs. Loose Enumerations

A TestStand enumeration can be either strict or loose. A loose enumeration can take on any
 numeric value. Enums in C, C++, and C# can be described loose in this sense. A strict
 enumeration can take on only those values defined by its enumerators. Attempting to set a
 strict TestStand enumeration to a value that does not correspond to its enumerators results
 in an error. By default, TestStand enumerations are strict.

#### Flag Enumerations

TestStand
 enumerations may be designated as “flags.” This is conceptually similar to adding
 the [Flags] attribute to an enum in .NET, although the
 functionality is different. In TestStand, flags enumerations support bitwise
 semantics to specify combinations of enumerators. Non-flags enumerations do not
 support these semantics.

Parent topic:

Using Enumerations in TestStand

<!--NI_TOPIC bundle=teststand path=enumerations-and-type-merging.html language=enus -->
## TOPIC 00339: Enumerations and Type Merging

- bundle_id: `teststand`
- source_path: `enumerations-and-type-merging.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enumerations-and-type-merging.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When updating an enumeration instance, the enumerator information is never changed. If the enumerator exists in the updated type definition, the numeric value of the instance is updated to match the new type definition. If the enumerator does not exist, the instance being updated is left unchanged,

### Enumerations and Type Merging

When updating an enumeration instance, the enumerator information is never changed. If the enumerator exists in the updated type definition, the numeric value of the instance is updated to match the new type definition. If the enumerator does not exist, the instance being updated is left unchanged, but is now invalid.

This behavior is analogous to behavior in C, C++, and C#. In these languages, changing the value of an enumerator in the enumeration definition implicitly changes the numeric value ofthe enumerator everywhere it is used in source files. Deleting or renaming an enumerator inthe enumeration definition causes dependent code not to compile until it has been fixed.

Note

Parent topic:

Using Enumerations in TestStand

<!--NI_TOPIC bundle=teststand path=enumerations-as-numbers.html language=enus -->
## TOPIC 00340: Enumerations as Numbers

- bundle_id: `teststand`
- source_path: `enumerations-as-numbers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enumerations-as-numbers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enumeration data types have numeric format and representation just like TestStand numbers. Both can be set on the type definition in exactly the same way they are set for numbers. The numeric format may be different for type instances than it is for the definition. The numeric representation is a pr

### Enumerations as Numbers

Enumeration data types have numeric format and representation just like TestStand numbers. Both can be set on the type definition in exactly the same way they are set for numbers. The numeric format may be different for type instances than it is for the definition. The numeric representation is a property of the type and cannot be changed on individual instances.

Flags enumerations with the default 64-bit float representation must be integers in the range [0, 2^32 - 1] inclusive. You can set non-flags enumerations with the default representation to any value, although you should use non-integer values with caution since most code modules treat enumerations as integers.

You can convert a TestStand enumeration to a number using GetValNumber(), GetValInteger64(), or GetValUnsignedInteger64() as appropriate with thePropOption_CoerceFromEnum option. Alternatively, you can use the Float64(), Int64(), orUInt64() expression functions. You can assign a number to an enumeration usingSetValNumber(), SetValInteger64(), or SetValUnsignedInteger64() as appropriate with thePropOption_CoerceToEnum option. For further details, see the Enumerations asPropertyObjects and Enumerations in TestStand Expressions sections.

Parent topic:

TestStand Enumerations Reference Guide

Related concepts:

- Enumerations as PropertyObjects
- Enumerations in TestStand Expressions

<!--NI_TOPIC bundle=teststand path=enumerations-as-propertyobjects.html language=enus -->
## TOPIC 00341: Enumerations as PropertyObjects

- bundle_id: `teststand`
- source_path: `enumerations-as-propertyobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enumerations-as-propertyobjects.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand enumerations are PropertyObjects just like other TestStand data types. As such, you can invoke PropertyObject methods and properties on enumerations. In most cases, the extension of existing methods to TestStand enumerations is obvious, but cases specifically related to type or value requi

### Enumerations as PropertyObjects

TestStand enumerations are PropertyObjects just like other TestStand data types. As such, you can invoke PropertyObject methods and properties on enumerations. In most cases, the extension of existing methods to TestStand enumerations is obvious, but cases specifically related to type or value require further explanation.

<Enumeration.Type.ValueType> — Returns PropValType_Enum.

<Enumeration>.SetValString() — SetValString() fails with a type mismatch error unless you pass PropOption_CoerceToEnum. With the PropOption_CoerceToEnum option, SetValString()attempts to set the enumeration instance to the enumerator matching the string value passed. If the string value matches one of the enumerators, the call succeeds and both the enumerator and numeric values of the enumeration instance are updated. For flags enumerations, the string can be any combination of enumerators combined with bitwise OR, including the empty string. Passing a string that does not correspond to the enumerators results in a runtime error.

<Enumeration>.GetValString() — GetValString() fails with a type mismatch error unless you pass PropOption_CoerceFromEnum. With the PropOption_CoerceFromEnum option,GetValString() returns a string representation of the enumeration. If the enumeration instance has enumerator information, the enumerator name is returned. For flags, this may be multiple enumerators combined with bitwise OR.

If the enumeration instance has no enumerator information (i.e. because it is loose and set to a value that does not correspond to its enumerators), the behavior depends on the options you pass. If you pass PropOption_CoerceFromNumber, the numeric value is converted to a string and returned. For flags enumerations, this may be a combination of enumerators combined with bitwise OR along with whatever number is left over. If you do not passPropOption_CoerceFromNumber, GetValString() returns an empty string. Generally,PropOption_CoerceFromNumber is appropriate when the purpose of the string is for display.PropOption_CoerceFromNumber is not usually appropriate for data persistence applications.

Calling GetValString() on an invalid enumeration results in a runtime error.

Note

| Property Options(s) | Enum State | Result |
| --- | --- | --- |
| None | Any | Runtime error |
| CoerceFromEnum | Has enumerator info | Enumerator(s) represented as string. |
| CoerceFromEnum | No enumerator info | Empty string. |
| CoerceFromEnum \| CoerceFromNumber | Has enumerator info | Enumerator(s) represented as string. |
| CoerceFromEnum \| CoerceFromNumber | No enumerator info | Numeric value converted to a string. For flags enumerations, could be some combination of enumerators combined with the OR operator with left-over number. |
| Any | Invalid | Runtime error |

<Enumeration>.SetValNumber() — SetValNumber() fails with a type mismatch error unless you pass PropOption_CoerceToEnum. With the PropOption_CoerceToEnum option, SetValNumber() attempts to set the enumeration instance to the specified value. If the number matches one of the enumerators, the call succeeds. For flags enumerations, the number can correspond to any combination of enumerators combined with a bitwise OR, including 0, which indicates no enumerators. The enumerator info is cleared unless the CoerceToString option is passed. If CoerceToString is passed, the enumerator information will be updated to match the numeric value. If there are multiple enumerators or combinations of flags that can represent the specified numeric value, a valid combination is chosen arbitrarily.

If the number does not correspond to the enumerators, the behavior depends on whether the enumeration is strict or loose. If the enumeration is loose, the number is updated to the specified value and the enumeration information is cleared. If the enumeration is strict,SetValNumber() fails with a runtime error.

| Property Options(s) | Strict/Loose | Number In Range | Behavior |
| --- | --- | --- | --- |
| None | Any | Any | Runtime error |
| CoerceToEnum | Any | In Range | Numeric value set. Enumeratorinformation cleared. |
| CoerceToEnum \| CoerceToString | Any | In Range | Numeric value set. TestStand engine sets enumerator(s) matching specified value. If ambiguous, choice is arbitrary. |
| CoerceToEnum | Strict | Out of Range | Runtime error. (CoerceToString has no effect.) |
| CoerceToEnum | Loose | Out of Range | Numeric value set. Enumeratorinformation cleared. (CoerceToStringhas no effect.) |

<Enumeration>.GetValNumber() — GetValNumber() fails with a type mismatch error unless you pass PropOption_CoerceFromEnum. With the PropOption_CoerceFromEnum option,GetValNumber() returns the numeric value of the enumeration. Calling GetValNumber() on an invalid enumeration results in a runtime error.

GetValInteger64() and GetValUnsignedInteger64() work similarly for enumerations with the associated representations. As with TestStand numbers, passingPropOption_CoerceFromNumber coerces the numeric representation if necessary.

Parent topic:

TestStand Enumerations Reference Guide

<!--NI_TOPIC bundle=teststand path=enumerations-in-teststand-expressions.html language=enus -->
## TOPIC 00342: Enumerations in TestStand Expressions

- bundle_id: `teststand`
- source_path: `enumerations-in-teststand-expressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/enumerations-in-teststand-expressions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Casting Functions Float64() — Equivalent to calling GetValNumber() with PropOption_Coerce.Int64() — Equivalent to calling GetValInteger64() with PropOption_Coerce.UInt64() — Equivalent to calling GetValUnsignedInteger64() with PropOption_Coerce.Str() — Equivalent to calling GetValString() with PropO

### Enumerations in TestStand Expressions

#### Casting Functions

Float64() — Equivalent to calling GetValNumber() with PropOption_Coerce.Int64() — Equivalent to calling GetValInteger64() with PropOption_Coerce.UInt64() — Equivalent to calling GetValUnsignedInteger64() with PropOption_Coerce.Str() — Equivalent to calling GetValString() with PropOption_Coerce.

#### Operators

Equality (==) and Inequality (!=) — To enforce type safety,
 enumerations can be compared only to other enumerations of the same named type. The equality
 and inequality operations compare the numeric values of the enumeration instances, ignoring
 any enumerator information. For example, if both Scarlet and
 Red have the numeric value of 2, then an enumeration set to
 Scarlet will equal an enumeration set to Red. (This
 behavior corresponds to the behavior of enums in C#, C, and C++.)

Assignment (=) — To enforce type safety, enumerations can be assigned
 only to other enumerations of the same named type.

Logical NOT (!) — Supported for flags enumerations only. Returns true
 if the numeric value is zero, false otherwise. Use logical NOT to check if any flags are
 set.

Bitwise AND (&), OR (|) and XOR (^) — Supported for flags
 enumerations only. To enforce type safety, enumerations can be combined only with other
 enumerations of the same named type. The TestStand engine performs the specified operation
 on the numeric values of the two operands, then constructs a new instance of the enumeration
 type and sets the value.

Note

Bitwise NOT(~) — Supported for flags enumerations only. The TestStand
 engine performs the bitwise NOT operation on the numeric value of the operand, then
 constructs a new instance ofthe enumeration type and sets the value.

Note

Unsupported Operations (<, >, +, -, *, /, %, +=, -=, *=, /=, %=,
 &&, ||, <<, >> ) — These operations are not supported for
 enumerations. To perform these operations, you must first convert the enumeration to a
 number.

#### Enumeration Constants

Use the Enum() expression function or the Enums keyword
 to specify an enumeration constant in an expression.

Enums keyword — Use the syntax
 Enums.<TYPE>.<ENUMERATOR> to specify an enumeration constant in a
 TestStand expression. For example, Enums.Color.Red specifies the
 Red value from the Color type in the Getting Started
 Creating a TestStand Enumeration section.

Enum(String type, [String|Number] value) — Returns an instance of an
 enumeration with the specified type and value. If value is a string, the enumerator and
 number are set as if by callingSetValString(). Passing an out of range value results in an
 error. If value is a number, the value is set as if by calling SetValNumber(),
 SetValInteger64(), SetValUnsignedInteger64() as appropriate for the representation of the
 enumeration type. Passing an out of range value to a strict enumeration results in a runtime
 error.

Parent topic:

TestStand Enumerations Reference Guide

Related concepts:

- Getting Started Creating a TestStand Enumeration

<!--NI_TOPIC bundle=teststand path=environment-behavior.html language=enus -->
## TOPIC 00343: Environment Behavior

- bundle_id: `teststand`
- source_path: `environment-behavior.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/environment-behavior.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Environments change the locations of the TestStand Public directory, the TestStandCommonAppData directory (which implicitly defines the location of TestStand Config directory), and/or the TestStand LocalAppData directory. These settings affect the associated TestStand Search Directories, as well as

### Environment Behavior

Environments change the locations of the TestStand Public directory, the
 TestStandCommonAppData directory (which implicitly defines the location of TestStand
 Config directory), and/or the TestStand LocalAppData directory. These settings
 affect the associated TestStand Search Directories, as well as the paths returned by
 the Engine.GetTestStandPathmethod. The table below describes how environment
 settings affect the valuesEngine.GetTestStandPath returns and the built-in search
 directory paths.

| TestStand Paths Value | Environment Location | Affected Search Directory |
| --- | --- | --- |
| TestStandPath_Bin | Not affected by environment |  |
| TestStandPath_CommonAppData | CommonAppData |  |
| TestStandPath_Config | CommonAppData\\Cfg |  |
| TestStandPath_LocalAppData | LocalAppData |  |
| TestStandPath_NIComponents | Not affected by environment |  |
| TestStandPath_Public | Public | TestStand Public |
| TestStandPath_PublicComponents | Public\\Components | TestStand Public Components |
| TestStandPath_Temp | Not affected by environment |  |
| TestStandPath_Temporary | Not affected by environment |  |
| TestStandPath_TestStand | Not affected by environment |  |

Environments are largely transparent to an application that uses the Engine.
 GetTestStandPath and Search Directories APIs to obtain directory locations. In most
 cases, an application should not care whether it is running within an environment or
 not. For applications that do require information about the environment in which
 they are running, the following API is available:

- Engine.GetEnvironmentPath —Returns the path of the current
 environment, or emptystring if the TestStand Engine is running in the global
 environment.
- Engine.GetTestStandPath —The following constants return
 the associated path for the global environment: TestStandPath_GlobalConfig,
 TestStandPath_GlobalPublic,TestStandPath_GlobalCommonAppData, and
 TestStandPath_GlobalLocalAppData.

Parent topic:

TestStand Environments

<!--NI_TOPIC bundle=teststand path=error-and-commonresults.html language=enus -->
## TOPIC 00344: Error and CommonResults

- bundle_id: `teststand`
- source_path: `error-and-commonresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/error-and-commonresults.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand inserts a Results property in every step you add to a sequence. The Results property includes at least three subproperties—Error, Status, and Common. Steps use the Error subproperty to indicate run-time errors. The Error subproperty uses the Error standard data type, which is a container t

### Error and CommonResults

TestStand inserts a Results property in every step you add to a sequence. The Results property includes at least three subproperties—Error, Status, and Common.

Steps use the Error subproperty to indicate run-time errors. The Error subproperty uses the Error standard data type, which is a container that includes Code, Msg, and Occurred subproperties. When a run-time error occurs in a step, the step sets the Code subproperty to a value that indicates the source of the error, the Msg subproperty to a string that describes the error, and the Occurred subproperty to True.

The Common subproperty uses the CommonResults standard data type, which is an initially empty object. By adding subproperties to the CommonResults data type, you can add extra result information to all steps in a standard way.

The default CommonResults standard data type version (3.1.0.100) is empty and does not change in newer versions of TestStand to ensure that any use of a newer version of CommonResults in sequence files is maintained and not automatically overridden in a newer version of TestStand.

Note

When you modify CommonResults without incrementing the version number, you might see a type
 conflict when you open other sequence files, such as FrontEndCallbacks.seq
 when TestStand loads the LoginLogout Front-End callback sequence before you log in or out.
 TestStand prompts you to increment the version number when you save changes to any data type
 or step type. You can avoid the type conflicts by re-saving the type palette files and
 instructing TestStand to increment the type version for CommonResults before opening any
 other files. NI recommends modifying the CommonResults data type only when you want to make
 an architectural change to all step types that you use. Share the modified CommonResults
 data type and the step types that use the CommonResults data type only with systems on which
 you are certain you will not deploy any conflicting changes to CommonResults. If you want to
 add additional results to particular steps, NI recommends using the Additional Results
 feature rather than modifying CommonResults.

Parent topic:

Using Standard Named Data Types

Related concepts:

- Type Versioning
- Managing Type Revisions
- Modifying Front-End Callbacks
- Type Concepts

<!--NI_TOPIC bundle=teststand path=error-codes-atlas.html language=enus -->
## TOPIC 00345: Error Codes and Descriptions

- bundle_id: `teststand`
- source_path: `error-codes-atlas.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/error-codes-atlas.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible error codes you might receive while using the ATLAS step type example and the corresponding descriptions. Error Code Description -17001 The test program set (TPS) cannot continue execution because the NI ATLAS Step Type ActiveX server is in an unrecognized state. U

### Error Codes and Descriptions

The following table lists possible error codes you might receive while using the ATLAS step type example and the corresponding descriptions.

| Error Code | Description |
| --- | --- |
| -17001 | The test program set (TPS) cannot continue execution because the NI ATLAS Step Type ActiveX server is in an unrecognized state. Unload the server from TestStand and restart the execution. |
| -17205 | The TPS cannot be executed because the PAWS Run-Time System (RTS) is in a bad state or cannot be initialized. Terminate the current instance of the PAWS RTS and run the TPS again. |
| -17208 | The specified TPS file was not found. Ensure that the file path is correctly specified so TestStand can locate the file and its directory. |
| -17401 | The TPS cannot be executed because another TPS exists and is currently running on the requested host. Only one instance of the PAWS RTS can exist on a host at any time. Wait for the currently running TPS to complete execution or terminate the execution before executing another TPS. |
| -17500 | The execution failed because the RTS reported an error. The RTS error displays as part of the error message. |
| -17501 | An unexpected error occurred. |
| -17600 | The TPS cannot be loaded because the RTS was interrupted during the load process. Check the TPS and PAWS RTS for errors and try running the TPS again. |
| -17601 | No TPS file was specified for execution. Use the Edit ATLAS Call dialog box to select a file to call before executing the step. |

Parent topic:

ATLAS Step Type

Related concepts:

- ATLAS Step Type
- Edit ATLAS Call Dialog Box

<!--NI_TOPIC bundle=teststand path=error-codes-java.html language=enus -->
## TOPIC 00346: Error Codes and Descriptions

- bundle_id: `teststand`
- source_path: `error-codes-java.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/error-codes-java.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible error codes you might receive while using the Java step types example and the corresponding descriptions. Error Code Error Message Explanation -1001 Could not launch JVM The creation of the Java virtual machine (JVM) failed. Refer to the Sun website at java.sun.com

### Error Codes and Descriptions

The following table lists possible error codes you might receive while using the Java step types example and the corresponding descriptions.

| Error Code | Error Message | Explanation |
| --- | --- | --- |
| -1001 | Could not launch JVM | The creation of the Java virtual machine (JVM) failed. Refer to the Sun website at java.sun.com for information about the possible causes of the failure. Verify that jvm.dll was found and is not corrupt, and ensure that the class path is valid. |
| -1001 | Could not attach thread to JVM | The current thread was detached from the JVM. Restart TestStand and ensure that the Java run-time environment is installed correctly. |
| -1001 | Could not detach current thread | The current thread could not be detached from the JVM. Restart TestStand and ensure that the Java run-time environment is installed correctly. |
| -1002 | Could not launch JVM | The current thread was detached from the JVM. Restart TestStand and ensure that the Java run-time environment is installed correctly. |
| -1003 | Could not launch JVM | A Java Native Interface (JNI) version error occurred. The wrong version of the JVM was found. Ensure that the Java run-time environment is installed correctly. |
| -1004 | Could not launch JVM | Insufficient memory to create the JVM. |
| -1005 | Could not launch JVM | The JVM already exists in memory. |
| -1006 | Could not launch JVM | Invalid arguments are passed. Verify that the class path is correct and ensure that the Java run-time environment is installed correctly. |
| -1500 | Cannot find class | The specified class name was not found in the class path. Verify the class name and that the file that contains the class exists in the class path. |
| -2000 | Incorrect class name | The specified class name is incorrect. Re-enter the class name in the Edit Java Call dialog box. |
| -3000 | Cannot find method | The specified method was not found in the specified class. Verify that the method name is correct and that it exists in the specified class. |
| -3500 | Too many arguments passed for void method | Too many arguments are passed for a void method. |
| -4000 | Error reading returned string | The string returned from Java is corrupt. Verify that the return type of the Java method is a string value. |
| -5000 | Invalid return type found | The return type of the Java method does not match the return type specified in TestStand. Ensure that the variable types in TestStand are compatible with the Java types. |
| -6000 | JVM not invoked | The JVM was not created. Verify that TestStand calls the StartJVM step before this step. |
| -7000 | Unable to find registry key for Java run time | The registry key that contains the entry for the Java run-time environment cannot be found. The JVM installer registers the key. Reinstall the JVM. |
| -7500 | Unable to find registry keys for Java | The registry entry that specifies the location of jvm.dll was not found. The Java run-time environment installs the entry. Reinstall the JVM. |
| -8000 | Unable to find run-time DLL for Java | The registry entry for jvm.dll points to an invalid location, which indicates that the DLL was not found at the location. Reinstall the JVM. |
| -9000 | Unable to find CreateJavaVM function jvm.dll | The jvm.dll file does not contain the CreateJavaVM function, which indicates that the DLL is invalid. Reinstall the JVM. |
| -10000 | Cannot allocate memory | The system is low on resources and memory allocation failed. |

Parent topic:

Java Step Types

Related concepts:

- Java Step Types
- Edit Java Call Dialog Box

<!--NI_TOPIC bundle=teststand path=error-reporting-for-broken-vis-in-the-labview.html language=enus -->
## TOPIC 00347: Error Reporting for Broken VIs in the LabVIEW Run-Time Engine

- bundle_id: `teststand`
- source_path: `error-reporting-for-broken-vis-in-the-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/error-reporting-for-broken-vis-in-the-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Adapter provides detailed information about broken VIs when used with the LabVIEW 2018 or later run-time engine. The error information is displayed in the error tooltip in the Step Settings Pane and when you execute the step. Detailed information about the error is also logged into a tex

### Error Reporting for Broken VIs in the LabVIEW Run-Time Engine

The LabVIEW Adapter provides detailed information about broken VIs when used with the LabVIEW 2018 or later run-time engine. The error information is displayed in the error tooltip in the Step Settings Pane and when you execute the step.

Detailed information about the error is also logged into a text file, named the same as the VI name configured in the TestStand step. The log file is saved to the TestStand temp directory (<TestStand_Temp>), which in in the TestStand subdirectory in the directory the TEMP environment variable specifies, which by default is %USERPROFILE%\AppData\Local\Temp.

Parent topic:

LabVIEW Adapter

<!--NI_TOPIC bundle=teststand path=escaping-special-characters-in-reports.html language=enus -->
## TOPIC 00348: Escaping Special Characters in Reports

- bundle_id: `teststand`
- source_path: `escaping-special-characters-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/escaping-special-characters-in-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand ATML or XML reports escape certain characters in strings to correctly convert the characters to HTML codes for displaying XML tags in a web browser, as the following table describes. TestStand HTML reports never escape these characters. TestStand ATML or XML reports do not escape these cha

### Escaping Special Characters in Reports

TestStand ATML or XML reports escape certain characters in strings to correctly convert the characters to HTML codes for displaying XML tags in a web browser, as the following table describes. TestStand HTML reports never escape these characters.

Note

Step.Result.Error.Msg

Step.Result.ReportText

| XML Character | Escaped Character |
| --- | --- |
| < | < |
| > | > |
| & | & |
| ' | ' |
| " | " |

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- ATML
- XML Reports

<!--NI_TOPIC bundle=teststand path=evaluating-conditional-disable-structures-and.html language=enus -->
## TOPIC 00349: Evaluating Conditional Disable Structures and Symbols

- bundle_id: `teststand`
- source_path: `evaluating-conditional-disable-structures-and.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/evaluating-conditional-disable-structures-and.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Conditional Disable Structure contains one or more subdiagrams, or cases. You can specify conditions for the structure based on custom symbols defined in a project. For all VIs in the main application instance, TestStand evaluates any conditions that use custom symbols when the VI is recompiled.

### Evaluating Conditional Disable Structures and Symbols

The Conditional Disable Structure contains one or more subdiagrams, or cases. You can specify conditions for the structure based on custom symbols defined in a project.

For all VIs in the main application instance, TestStand evaluates any conditions that use custom symbols when the VI is recompiled. These expressions are not evaluated again during execution.

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Executing VIs with Separate Compiled Code
- Calling VIs That Create ActiveX References

<!--NI_TOPIC bundle=teststand path=events-typical-applications-handle.html language=enus -->
## TOPIC 00350: Events Typical Applications Handle

- bundle_id: `teststand`
- source_path: `events-typical-applications-handle.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/events-typical-applications-handle.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create an application, you can direct the application to handle any subset of the available TestStand User Interface (UI) Control events. However, an application typically handles the events described in the following table. Event Description ExitApplication The Application Manager control

### Events Typical Applications Handle

When you create an application, you can direct the application to handle any subset of the available TestStand User Interface (UI) Control events. However, an application typically handles the events described in the following table.

| Event | Description |
| --- | --- |
| ExitApplication | The Application Manager control generates this event to request that the application exit. Handle this event by directing the application to exit normally. |
| Wait | The Application Manager control generates this event to request that the application display or remove a busy indicator. Handle this event by displaying or removing a wait cursor according to the value of the showWait event parameter. |
| ReportError | The Application Manager control generates this event to request that the user interface return an error during user input or during an asynchronous operation. Handle this event by displaying the error code and description in a dialog box or by appending the error code and description to an error log. The ApplicationMgr.ReportError event indicates an application error, not a sequence execution error. The ApplicationMgr.BreakOnRunTimeError event indicates a sequence execution error. |
| DisplaySequenceFile | The Application Manager control generates this event to request that the application display a particular sequence file. Handle this event by displaying the sequence file by setting the SequenceFileViewMgr.SequenceFile property.If the application has only a single window, set this property on the SequenceFileView Manager control that resides on the window.If the application displays each sequence file in a separate window using separate SequenceFileView Manager controls, call the ApplicationMgr.GetSequenceFileViewMgr method to find the SequenceFileView Manager control that currently displays the sequence file so you can activate the window that contains the sequence file.If no SequenceFileView Manager control currently displays the sequence file, a multiple window application can create a new window that contains a SequenceFileView Manager control. The application can then set the SequenceFileViewMgr.SequenceFile property to display the sequence file in the new window. |
| DisplayExecution | The Application Manager control generates this event to request that the application display a particular execution. Handle this event by displaying the execution by setting the ExecutionViewMgr.Execution property. If the application has only a single window, set this property on the ExecutionView Manager control that resides on the window.If the application displays each execution in a separate window using separate ExecutionView Manager controls, call the ApplicationMgr.GetExecutionViewMgr method to find the ExecutionView Manager control that currently displays the execution so you can activate the window that contains the execution.If no ExecutionView Manager control currently displays the execution, a multiple window application can create a new window that contains an ExecutionView Manager control. The application can then set the ExecutionViewMgr.Execution property to display the execution in the new window. |

Parent topic:

Handling Events

Related concepts:

- Application Manager
- Startup and Shutdown
- SequenceFileView Manager
- ExecutionView Manager

<!--NI_TOPIC bundle=teststand path=example-data-link-and-result-table-setup-for.html language=enus -->
## TOPIC 00351: Example Data Link and Result Table Setup for Microsoft Access

- bundle_id: `teststand`
- source_path: `example-data-link-and-result-table-setup-for.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/example-data-link-and-result-table-setup-for.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can link a TestStand data link to a Microsoft Access database file (.mdb) using the Jet Object Linking and Embedding Database (OLE DB) provider in 32-bit TestStand and the Microsoft Office 12.0 Access Database Engine OLE DB Provider in 64-bit TestStand to log results using the default process mo

### Example Data Link and Result Table Setup for Microsoft Access

You can link a TestStand data link to a Microsoft Access database file
 (.mdb) using the Jet Object Linking and Embedding Database (OLE
 DB) provider in 32-bit TestStand and the Microsoft Office 12.0 Access Database
 Engine OLE DB Provider in 64-bit TestStand to log results using the default process
 model. Visit ni.com/info and enter the Info Code
 64TSaccdb to access the NI support article, Using
 Microsoft Access Databases with 64-bit TestStand, for more information about
 installing this provider.

Parent topic:

Data Links

Related concepts:

- Database Options—Specifying a Data Link and Schema
- Microsoft ADO, OLE DB, and ODBC Database Technologies

<!--NI_TOPIC bundle=teststand path=example-legacy-labwindows-cvi-code-module.html language=enus -->
## TOPIC 00352: Example Legacy LabWindows/CVI Code Module

- bundle_id: `teststand`
- source_path: `example-legacy-labwindows-cvi-code-module.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/example-legacy-labwindows-cvi-code-module.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a legacy code module for the LabWindows/CVI Adapter, you must add the stdtst.h header file located in the <TestStand Public>\AdapterSupport\CVI directory to the source file. The stdtst.h file includes the type definitions for the tTestData and tTestError structures. The following is

### Example Legacy LabWindows/CVI Code Module

When you create a legacy code module for the LabWindows/CVI Adapter, you must add the stdtst.h header file located in the <TestStand Public>\AdapterSupport\CVI directory to the source file. The stdtst.h file includes the type definitions for the tTestData and tTestError structures.

The following is an example code module that uses the LabWindows/CVI standard prototype:

// Simple test example

#include "stdtst.h"

void TX_TEST __declspec(dllexport) FunctionName (tTestData *testData, tTestError *testError)

{

int error = 0;

double measurement = 5.0;

char *lastUserName = NULL;

testData->measurement = measurement;

if ((error = TS_PropertyGetValString (testData->seqContextCVI, NULL, "StationGlobals.TS.LastUserName", 0, &lastUserName)) < 0) goto Error;

Error:

// FREE RESOURCES

CA_FreeMemory(lastUserName);

// Set the error flag to cause a run-time error

if (error < 0)

{

testError->errorFlag = TRUE;

testError->errorCode = error;

testData->replaceStringFuncPtr(&testError->

errorMessage, "ErrorText");

}

}

Parent topic:

Calling Legacy LabWindows/CVI Code Modules

Related concepts:

- Search Directories
- Updating Step Properties

Related information:

- tTestData Structure
- tTestError Structure

<!--NI_TOPIC bundle=teststand path=example-programs.html language=enus -->
## TOPIC 00353: TestStand Example Programs

- bundle_id: `teststand`
- source_path: `example-programs.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/example-programs.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand includes a variety of example programs that you can use to help you learn key concepts or to serve as a starting point for applications you create. You can browse the examples in the following ways: Open the Examples.tsw workspace file located in the <TestStand Public>\Examples directory.

### TestStand Example Programs

TestStand includes a variety of example programs that you can use to help you learn key concepts
 or to serve as a starting point for applications you create.

You can browse the examples in the following ways:

- Open the Examples.tsw workspace file located in the <TestStand
 Public>\Examples directory.
- Open an example sequence file from the subdirectories of the <TestStand Public>\Examples directory.

- [Examples for Built-In Step Types](examples-for-built-in-step-types.html) The Built-In Step Types examples demonstrate how to use the default step types provided in the TestStand insertion palette. This directory includes the following example programs.
- [Examples for Custom Step Types](examples-for-custom-step-types.html) The Custom Step Types examples extend TestStand with additional custom step types to call different types of test code. This directory includes the following example programs.
- [Examples for Customizing Result Processing](examples-for-customizing-result-processing.html) The Customizing Result Processing examples demonstrate common approaches for customizing default TestStand result processing plug-ins, and for creating custom result processing plug-ins. This directory includes the following example programs.
- [Examples for Demos](examples-for-demos.html) The Demo examples provide an overview of TestStand features. You can execute these examples without installing additional software. This directory includes the following example programs.
- [Examples for Fundamentals](examples-for-fundamentals.html) The Fundamentals examples demonstrate key concepts for developing TestStand systems. This directory includes the following example programs.
- [Examples for Interfacing with Hardware](examples-for-interfacing-with-hardware.html) The Interfacing with Hardware examples demonstrate how you can use TestStand to communicate with and coordinate your test hardware resources. This directory includes the following example programs.
- [Examples for Modifying Process Models](examples-for-modifying-process-models.html) The Modifying Process Models examples demonstrate common methods for overriding or extending default process model functionality in the client sequence file. This directory includes the following example programs.
- [Examples for Modifying User Interfaces](examples-for-modifying-user-interfaces.html) The Modifying User Interfaces examples demonstrate common TestStand user interface features and customizations. This directory includes the following example programs.
- [Examples for Parallel Testing](examples-for-parallel-testing.html) The Parallel Testing examples demonstrate TestStand features for running your test code in parallel. This directory includes the following example programs.
- [Examples for the TestStand API](examples-for-the-teststand-api.html) The TestStand API examples demonstrate how to implement common applications of the TestStand API in the TestStand expression language and other programming languages. This directory includes the following example programs.
- [Examples for TestStand Debugging Features](examples-for-teststand-debugging-features.html) The TestStand Debugging Features examples highlight TestStand features for troubleshooting your test sequences. This directory includes the following example programs.

Related concepts:

- TestStand Directory Structure

Related information:

- TestStand Featured Examples

<!--NI_TOPIC bundle=teststand path=example-sequence-file-translators.html language=enus -->
## TOPIC 00354: Example Sequence File Translators

- bundle_id: `teststand`
- source_path: `example-sequence-file-translators.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/example-sequence-file-translators.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW, LabWindows/CVI, and Microsoft Visual C++ example projects demonstrate how to build translator DLLs and provide guidance for developing translators. The examples illustrate two simple translators for each development environment that use the TestStand API to convert sample test descripti

### Example Sequence File Translators

The LabVIEW, LabWindows/CVI, and Microsoft Visual C++ example projects demonstrate how to build translator DLLs and provide guidance for developing translators. The examples illustrate two simple translators for each development environment that use the TestStand API to convert sample test descriptions in XML and ASCII text formats into TestStand sequence files. The example translators for each file format produce the same TestStand sequence file.

The sample test descriptions specify steps that perform a calculation, display the result of the calculation in a graph, compare the result with an expected value, and display a message that indicates whether the test passed or failed. The translation from the example format into a sequence file involves adding steps and local variables to a sequence in a new sequence file object and configuring the steps to perform the required operations. The translators also use a custom step type TestStand loads from a type palette file that you must place in the <TestStand Public>\Components\TypePalettes directory.

Complete the following steps to use an example.

1. Open the TextTranslator or XMLTranslator directory for one of the examples in the <TestStand Public>\Examples\Fundamentals\Sequence File Translators - Examples directory.
2. Copy the type NI_ExampleTranslatorTypes.ini file from the <TestStand Public>\Examples\Fundamentals\Sequence File Translators - Examples directory to the <TestStand Public>\Components\TypePalettes directory.
3. Open and review the project in the development environment for the example.
4. When you make any changes to the project, rebuild the project to update the translator DLL. Copy the translator DLL into the <TestStand Public>\Components\Translators directory.
5. Launch the TestStand Sequence Editor or a TestStand User Interface to load the translator DLLs.
6. Select File»Open File and select SampleTestFile.xml , SampleTestFile.lvtf for the text version of the file for LabVIEW, SampleTestFile.cvitf for the text version of the file for LabWindows/CVI, or SampleTestFile.vctf for the text version of the file for Microsoft Visual C++.
7. Review the translated sequence file.
8. Launch an execution using the MainSequence in the sequence file.

Parent topic:

Sequence File Translators

Related concepts:

- Sequence File Translators
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=example-user-interfaces.html language=enus -->
## TOPIC 00355: Example User Interfaces

- bundle_id: `teststand`
- source_path: `example-user-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/example-user-interfaces.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand>\UserInterfaces directory includes the following subdirectories that contain the executable, project, and source code files for each example user interface: Full-Featured—Contains user interfaces for loading, viewing, editing, saving, executing, and debugging sequence files. The full-

### Example User Interfaces

The <TestStand>\UserInterfaces directory includes the following subdirectories that contain the executable, project, and source code files for each example user interface:

- Full-Featured —Contains user interfaces for loading, viewing, editing, saving, executing, and debugging sequence files. The full-featured examples include menus and localization options.
- Simple —contains similar but limited user interfaces with fewer commands and options but no menus. Also, the simple example user interfaces display the steps for executions you run but do not display steps for sequences you load.

Note

The following table lists all the simple and full-featured example user interfaces that TestStand provides:

| ADE | Full-Featured User Interface | Simple User Interface |
| --- | --- | --- |
| C++ (MFC) | <TestStand Public>\\UserInterfaces\\Full-Featured\\C++ (MFC)\\Source Code\\TestExec.vcproj | <TestStand Public>\\UserInterfaces\\Simple\\C++ (MFC)\\Source Code\\TestExec.vcproj |
| C# | <TestStand Public>\\UserInterfaces\\Full-Featured\\CSharp\\Source Code\\TestExec.VS2010.csproj | <TestStand Public>\\UserInterfaces\\Simple\\CSharp\\Source Code\\TestExec.VS2010.csproj |
| LabVIEW | <TestStand Public>\\UserInterfaces\\Full-Featured\\LabVIEW\\Source Code\\TestExec.llb\\Full UI - Top-Level VI.vi | <TestStand Public>\\UserInterfaces\\Simple\\LabVIEW\\Source Code\\TestExec.llb\\Simple OI - Top-Level VI.vi |
| LabWindows/CVI | <TestStand Public>\\UserInterfaces\\Full-Featured\\CVI\\Source Code\\TestExec.prj | <TestStand Public>\\UserInterfaces\\Simple\\CVI\\Source Code\\TestExec.prj |
| Microsoft Visual Basic .NET | <TestStand Public>\\UserInterfaces\\Full-Featured\\VB.Net\\Source Code\\TestExec.VS2010.vbproj | <TestStand Public>\\UserInterfaces\\Simple\\VB.Net\\Source Code\\TestExec.VS2010.vbproj |

TestStand installs the source code files for the default user interfaces in the
 <TestStand>\UserInterfaces and
 <TestStand Public>\UserInterfaces directories. To
 modify the installed user interfaces or to create new user interfaces, modify the
 files in the <TestStand Public>\UserInterfaces directory.
 You can use the read-only source files for the default user interfaces in the
 <TestStand>\UserInterfaces directory as a reference.
 NI recommends that you track the changes you make to the user interface source code
 files so you can integrate the changes with any enhancements in future versions of
 the TestStand User Interfaces.

Parent topic:

Creating Custom User Interfaces

Related concepts:

- TestStand Directory Structure
- Special Considerations for a LabVIEW Custom User Interface
- Required Visual Studio Components for Building Custom C# User Interfaces
- Caveats for Using the LabVIEW Example User Interfaces

<!--NI_TOPIC bundle=teststand path=examples-for-built-in-step-types.html language=enus -->
## TOPIC 00356: Examples for Built-In Step Types

- bundle_id: `teststand`
- source_path: `examples-for-built-in-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-built-in-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Built-In Step Types examples demonstrate how to use the default step types provided in the TestStand insertion palette. This directory includes the following example programs.

### Examples for Built-In Step Types

The Built-In Step Types examples demonstrate how to use the default step types provided
 in the TestStand insertion palette. This directory includes the following example
 programs.

- [Database Step Types](database-step-types.html)
- [Flow Control Step Types](flow-control-step-types.html)
- [IVI Step Types](ivi-step-types.html)
- [Message Popup Step Type - Automatically Dismissing](message-popup-step-type-automatically-dismiss.html)
- [Message Popup Step Type - Get User Input](message-popup-step-type-get-user-input.html)
- [Multiple Numeric Limit Test Step Type](multiple-numeric-limit-test-step-type.html)
- [Property Loader Step Type - Loading Limits from a Database](property-loader-step-type-loading-limits-db.html)
- [Property Loader Step Type - Loading Limits from a File Containing Alias](pl-step-type-loading-limits-alias.html)
- [Property Loader Step Type - Loading Limits from a Microsoft Excel File](pl-step-type-loading-limits-excel.html)
- [Property Loader Step Type - Loading Limits for Multiple Sequences](property-loader-step-type-loading-limits-for.html)
- [Property Loader Step Type - Loading Limits from Multiple Sources](pl-step-type-loading-limits-mult-source.html)
- [Property Loader Step Type - Loading Limits from Two Different Text Files](pl-step-type-loading-limits-text.html)
- [Statement Step Type](statement-step-type.html)
- [Synchronization Step Types - Auto Schedule](synchronization-step-types-auto-schedule.html)
- [Synchronization Step Types - Batch Synchronization](synchronization-step-types-batch-synchronizat.html)
- [Synchronization Step Types - Lock](synchronization-step-types-lock.html)
- [Synchronization Step Types - Notification and Wait](synchronization-step-types-notification-and-w.html)
- [Synchronization Step Types - Queue](synchronization-step-types-queue.html)
- [Synchronization Step Types - Rendezvous and Semaphore](synchronization-step-types-rendezvous-and-sem.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-custom-step-types.html language=enus -->
## TOPIC 00357: Examples for Custom Step Types

- bundle_id: `teststand`
- source_path: `examples-for-custom-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-custom-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Custom Step Types examples extend TestStand with additional custom step types to call different types of test code. This directory includes the following example programs.

### Examples for Custom Step Types

The Custom Step Types examples extend TestStand with additional custom step types to call
 different types of test code. This directory includes the following example
 programs.

- [Agilent VEE Step Types](agilent-vee-step-types.html)
- [ATLAS Step Type](atlas-step-type.html)
- [Java Step Types](java-step-types.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-customizing-result-processing.html language=enus -->
## TOPIC 00358: Examples for Customizing Result Processing

- bundle_id: `teststand`
- source_path: `examples-for-customizing-result-processing.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-customizing-result-processing.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Customizing Result Processing examples demonstrate common approaches for customizing default TestStand result processing plug-ins, and for creating custom result processing plug-ins. This directory includes the following example programs.

### Examples for Customizing Result
 Processing

The Customizing Result Processing examples demonstrate common approaches for customizing
 default TestStand result processing plug-ins, and for creating custom result
 processing plug-ins. This directory includes the following example
 programs.

- [Adding Custom Data to a Report](adding-custom-data-to-a-report.html)
- [Adding Custom Images to a Report](adding-custom-images-to-a-report.html)
- [Displaying Graphs in a Report](displaying-graphs-in-a-report.html)
- [Including Hyperlinks in a Report](including-hyperlinks-in-a-report.html)
- [Including Hyperlinks in a Report - TDMS File](including-hyperlinks-in-a-report-tdms-file.html)
- [Model Plug-in - Basic Step Time Report](model-plug-in-basic-step-time-report.html)
- [Model Plug-in - Simple Text Report](model-plug-in-simple-text-report.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-demos.html language=enus -->
## TOPIC 00359: Examples for Demos

- bundle_id: `teststand`
- source_path: `examples-for-demos.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-demos.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Demo examples provide an overview of TestStand features. You can execute these examples without installing additional software. This directory includes the following example programs.

### Examples for Demos

The Demo examples provide an overview of TestStand features. You can execute these
 examples without installing additional software. This directory includes the
 following example programs.

- [Computer Motherboard Test](computer-motherboard-test.html)
- [Mobile Device Test Demo](mobile-device-test-demo.html)
- [Parallel Test Strategies Demo](parallel-test-strategies-demo.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-fundamentals.html language=enus -->
## TOPIC 00360: Examples for Fundamentals

- bundle_id: `teststand`
- source_path: `examples-for-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-fundamentals.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Fundamentals examples demonstrate key concepts for developing TestStand systems. This directory includes the following example programs.

### Examples for Fundamentals

The Fundamentals examples demonstrate key concepts for developing TestStand systems. This
 directory includes the following example programs.

- [Calling Dynamic Dispatch VIs](calling-dynamic-dispatch-vis.html)
- [Developing Platform Independent Test Systems](developing-platform-independent-test-systems.html)
- [Launching a Modal Dialog](launching-a-modal-dialog.html)
- [Launching an MFC Dialog with ActiveX Controls](launching-an-mfc-dialog-with-activex-controls.html)
- [Overriding Engine Callbacks - SequenceFilePostStepFailure](overriding-engine-callbacks-sequencefileposts.html)
- [Overriding Engine Callbacks - SequenceFilePostStepRuntimeError](override-sfps-runtime-error.html)
- [Passing Clusters to Code Modules - LabVIEW](passing-clusters-to-code-modules-labview.html)
- [Passing Structs to Code Modules](passing-structs-to-code-modules.html)
- [Pausing Executions with Running Code Modules](pausing-executions-with-running-code-modules.html)
- [Interpreter Session Management in Python](interpreter-session-management-in-python.html)
- [Passing Data between TestStand and Python](passing-data-between-teststand-and-python.html)
- [Sequence File Translators](sequence-file-translators-ex.html)
- [Structure of TestStand Executions](structure-of-teststand-executions.html)
- [Termination Monitor](termination-monitor.html)
- [Using Data Streams](using-data-streams.html)
- [Using Sweep Loops](using-sweep-loops.html)
- [Using TestStand Enumerations](using-teststand-enumerations.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-interfacing-with-hardware.html language=enus -->
## TOPIC 00361: Examples for Interfacing with Hardware

- bundle_id: `teststand`
- source_path: `examples-for-interfacing-with-hardware.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-interfacing-with-hardware.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Interfacing with Hardware examples demonstrate how you can use TestStand to communicate with and coordinate your test hardware resources. This directory includes the following example programs.

### Examples for Interfacing with Hardware

The Interfacing with Hardware examples demonstrate how you can use TestStand to
 communicate with and coordinate your test hardware resources. This directory
 includes the following example programs.

- [Instrument Control Step Types](instrument-control-step-types.html)
- [InstrumentStudio](instrumentstudio.html)
- [Interfacing with NI-Hardware drivers using Python Custom step and Python Adapter](interfacing-with-ni-hardware-drivers-using-py.html)
- [Session Manager](session-manager-ex.html)
- [Switch Executive](switch-executive.html)
- [Characterization of a Transistor](characterization-of-a-transistor.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-modifying-process-models.html language=enus -->
## TOPIC 00362: Examples for Modifying Process Models

- bundle_id: `teststand`
- source_path: `examples-for-modifying-process-models.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-modifying-process-models.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Modifying Process Models examples demonstrate common methods for overriding or extending default process model functionality in the client sequence file. This directory includes the following example programs.

### Examples for Modifying Process Models

The Modifying Process Models examples demonstrate common methods for overriding or
 extending default process model functionality in the client sequence
 file. This directory includes the following example
 programs.

- [Dynamically Set the Client Sequence File](dynamically-set-the-client-sequence-file.html)
- [Overriding PreUUT Model Callbacks](overriding-preuut-model-callbacks.html)
- [Overriding PreUUT and PostUUT Parallel Model Callbacks](overriding-preuut-and-postuut-parallel-model.html)
- [Overriding PreUUT and PostUUT Batch Model Callbacks](overriding-preuut-and-postuut-batch-model-cal.html)
- [Overriding PreBatch and PostBatch Model Callbacks](overriding-prebatch-and-postbatch-model-callb.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-modifying-user-interfaces.html language=enus -->
## TOPIC 00363: Examples for Modifying User Interfaces

- bundle_id: `teststand`
- source_path: `examples-for-modifying-user-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-modifying-user-interfaces.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Modifying User Interfaces examples demonstrate common TestStand user interface features and customizations. This directory includes the following example programs.

### Examples for Modifying User Interfaces

The Modifying User Interfaces examples demonstrate common TestStand user interface
 features and customizations. This directory includes the following
 example programs.

- [Building a TestStand UI with Native Controls](building-a-teststand-ui-with-native-controls.html)
- [Connecting UI Controls Demo](connecting-ui-controls-demo.html)
- [Creating a Basic User Interface](creating-a-basic-user-interface.html)
- [Handling UI Messages](handling-ui-messages.html)
- [Updating the Status Bar Using UI Messages](updating-the-status-bar-using-ui-messages.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-parallel-testing.html language=enus -->
## TOPIC 00364: Examples for Parallel Testing

- bundle_id: `teststand`
- source_path: `examples-for-parallel-testing.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-parallel-testing.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Parallel Testing examples demonstrate TestStand features for running your test code in parallel. This directory includes the following example programs.

### Examples for Parallel Testing

The Parallel Testing examples demonstrate TestStand features for running your test code
 in parallel. This directory includes the following example
 programs.

- [Comparing Resource Usage Strategies](comparing-resource-usage-strategies.html)
- [Executing Code Modules in Parallel](executing-code-modules-in-parallel.html)
- [Executing Sequences in Parallel](executing-sequences-in-parallel.html)
- [Testing UUTs in Parallel - Batch Model](testing-uuts-in-parallel-batch-model.html)
- [Testing UUTs in Parallel - Parallel Model](testing-uuts-in-parallel-parallel-model.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-teststand-debugging-features.html language=enus -->
## TOPIC 00365: Examples for TestStand Debugging Features

- bundle_id: `teststand`
- source_path: `examples-for-teststand-debugging-features.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-teststand-debugging-features.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Debugging Features examples highlight TestStand features for troubleshooting your test sequences. This directory includes the following example programs.

### Examples for TestStand Debugging Features

The TestStand Debugging Features examples highlight TestStand features for
 troubleshooting your test sequences. This directory includes the
 following example programs.

- [Benchmarks](benchmarks.html)
- [Custom Analyzer Rules](custom-analyzer-rules.html)
- [Generating Output Messages](generating-output-messages.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=examples-for-the-teststand-api.html language=enus -->
## TOPIC 00366: Examples for the TestStand API

- bundle_id: `teststand`
- source_path: `examples-for-the-teststand-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/examples-for-the-teststand-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand API examples demonstrate how to implement common applications of the TestStand API in the TestStand expression language and other programming languages. This directory includes the following example programs.

### Examples for the TestStand API

The TestStand API examples demonstrate how to implement common applications of the
 TestStand API in the TestStand expression language and other
 programming languages. This directory includes the following example
 programs.

- [Accessing Arrays Using API](accessing-arrays-using-api.html)
- [Accessing Properties Using API](accessing-properties-using-api.html)
- [Building a Sequence Using API](building-a-sequence-using-api.html)
- [Creating and Deleting Users Using API](creating-and-deleting-users-using-api.html)
- [Creating New Properties Using API](creating-new-properties-using-api.html)
- [Executing Sequences Using API](executing-sequences-using-api.html)
- [Type Casting API Classes](type-casting-api-classes.html)

Parent topic:

TestStand Example Programs

<!--NI_TOPIC bundle=teststand path=exceptions-to-custom-result-properties.html language=enus -->
## TOPIC 00367: Exceptions to Custom Result Properties

- bundle_id: `teststand`
- source_path: `exceptions-to-custom-result-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/exceptions-to-custom-result-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Limits.Low, Limits.High, Limits.String, and Comp properties are not subproperties of the Result property for the Numeric Limit Test and the String Value Test step types. Therefore, TestStand does not automatically include these properties in the step result. Depending on options you specify when

### Exceptions to Custom Result Properties

The Limits.Low, Limits.High, Limits.String, and Comp properties are not subproperties of the Result property for the Numeric Limit Test and the String Value Test step types. Therefore, TestStand does not automatically include these properties in the step result. Depending on options you specify when configuring the step, the default process model uses the TestStand API to include the Limits.Low, Limits.High, Limits.String, and Comp properties in the step results for Numeric Limit Test and String Value Test steps that contain these properties.

The AsyncID and AsyncMode properties are not subproperties of the Result property for the Sequence Call step type. TestStand adds these properties to the step results only for Sequence Call steps that call subsequences asynchronously or in a new execution.

Parent topic:

Custom Result Properties

Related concepts:

- TestStand ActiveX API Overview
- Step Types That Work with Specific Module Adapters
- Custom Result Properties
- Result Collection

<!--NI_TOPIC bundle=teststand path=excluding-items-from-profiling.html language=enus -->
## TOPIC 00368: Excluding Items from Profiling

- bundle_id: `teststand`
- source_path: `excluding-items-from-profiling.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/excluding-items-from-profiling.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Excluding Items from Profiling You can prevent the profiler from recording events for Sequence Files, Sequences, Steps, and Executions. To do so, add a container property to the item's attributes named NIProfiler. Within that container, create a Boolean property named Exclude. Note that if you creat

### Excluding Items from Profiling

#### Excluding Items from Profiling

You can prevent the profiler from recording events for Sequence Files, Sequences, Steps, and Executions. To do so, add a container property to the item's attributes named NIProfiler. Within that container, create a Boolean property named Exclude. Note that if you create these attributes programmatically, in the case of a SequenceFile, add the attributes to the SequenceFile.Data container rather than directly to the SequenceFile object.

Parent topic:

Execution Profiler

<!--NI_TOPIC bundle=teststand path=excluding-new-or-modified-files-from-a-patch.html language=enus -->
## TOPIC 00369: Excluding New or Modified Files from a Patch Deployment

- bundle_id: `teststand`
- source_path: `excluding-new-or-modified-files-from-a-patch.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/excluding-new-or-modified-files-from-a-patch.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to exclude new or modified files from a patch deployment. Select the file in the Distributed Files section of the Distributed Files tab of the TestStand Deployment Utility. Select Not Included in the File Status control of the File Properties tab. Selecting the Not Inclu

### Excluding New or Modified Files from a Patch Deployment

Complete the following steps to exclude new or modified files from a patch deployment.

1. Select the file in the Distributed Files section of the Distributed Files tab of the TestStand Deployment Utility.
2. Select Not Included in the File Status control of the File Properties tab.

Selecting the Not Included option always excludes the file in the patch deployment, even if the file is modified.

Note

Note

Parent topic:

Including and Excluding Files in MSI-based Installer Patches

<!--NI_TOPIC bundle=teststand path=excluding-results-from-an-xml-report-based-on.html language=enus -->
## TOPIC 00370: Excluding Results from an XML Report Based on Step Properties

- bundle_id: `teststand`
- source_path: `excluding-results-from-an-xml-report-based-on.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/excluding-results-from-an-xml-report-based-on.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to exclude results of specific steps based on step properties. Open the .xsl file you want to change. Search for the XSLT variable gEnableResultFiltering. Set the variable to 1 to enable result filtering. You can set the variable to 0 to disable result filtering. Search

### Excluding Results from an XML Report Based on Step Properties

Complete the following steps to exclude results of specific steps based on step properties.

1. Open the .xsl file you want to change.
2. Search for the XSLT variable gEnableResultFiltering .
3. Set the variable to 1 to enable result filtering. You can set the variable to 0 to disable result filtering.
4. Search for the string ADD_STEP_FILTERING_CONDITION . The filtering condition
 in the style sheets includes two expressions. The first expression defines
 an XPath expression for the filter condition. The second expression performs
 the filtering based on the filter condition. The style sheets include the
 following expressions to include only Passed steps in the
 report:
 filteringCondition = node.selectSingleNode("Prop[@Name='Status']/Value");
if (filteringCondition.text == 'Passed')Refer
 to the World Wide Web Consortium (W3C) website, located at
 www.w3.org, for more information about XPath.

The node you pass in as a parameter to the CheckIfStepSatisfiesFilteringCondition_node function corresponds to the <TEResult> node of the step. The report does not include steps under a Sequence Call step when the Sequence Call step itself does not meet the filtering conditions. The report always includes the result of the MainSequence callback step, even if the step does not meet the filtering conditions you set. To include all the steps in a sequence file that satisfy the filtering condition, use a condition to check Sequence Call step types regardless of step status.

Skipped

```text
var filteringCondition = node.selectSingleNode("Prop[@Name='Status']/Value");
if (filteringCondition.text != 'Skipped')
```

Passed

Done

```text
var filteringCondition = node.selectSingleNode("Prop[@Name='Status']/Value");
var stepTypeCondition = node.selectSingleNode("Prop[@Name = 'TS']/Prop[@Name = 'StepType']/Value");
var stepTypeConditionString;
if (stepTypeCondition)
    stepTypeConditionString = stepTypeCondition.text;
else stepTypeConditionString = 'SequenceCall'; //To handle psuedosequencecall steps
if ((filteringCondition.text == 'Passed' || filteringCondition.text == 'Done') || stepTypeConditionString == 'SequenceCall')
```

#### horizontal.xsl

The following figure shows a filtered report using horizontal.xsl:

[IMAGE alt='image' src='GUID-056A8491-0CFD-4962-B84D-A0912F97830C-a5.png']

#### report.xsl

The following figure shows a filtered report using report.xsl:

[IMAGE alt='image' src='GUID-1069F1D1-F029-4618-A181-CE68985898B0-a5.png']

#### expand.xsl

The following figure shows a filtered report using expand.xsl:

[IMAGE alt='image' src='GUID-321A9E23-6944-49B2-819D-9D50BBE8E41B-a5.png']

Parent topic:

Customizing XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=execute-sovi-lvrte-ts.html language=enus -->
## TOPIC 00371: Executing Source-Only VIs in LabVIEW Runtime Engine

- bundle_id: `teststand`
- source_path: `execute-sovi-lvrte-ts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/execute-sovi-lvrte-ts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Version Independent Runtime Engine Support feature in the LabVIEW Adapter as an option to avoid potential issues when executing source-only VIs using the LabVIEW Runtime Engine through the LabVIEW adapter. These issues can occur if the LabVIEW version the source-only VI was saved or mass-com

### Executing Source-Only VIs in LabVIEW Runtime
 Engine

Use the Version Independent Runtime Engine Support feature in the
 LabVIEW Adapter as an option to avoid potential issues when executing source-only VIs using the
 LabVIEW Runtime Engine through the LabVIEW adapter. These issues can occur if the LabVIEW
 version the source-only VI was saved or mass-compiled in does not match the LabVIEW Runtime
 engine version, as VI version no longer gets updated during a save or mass-compile.

AutoDetect

.lvversion

1. Option 1: Disable the Save version
 feature in LabVIEW, and re-save your VIs.
  1. Close TestStand.
  2. Open LabVIEW, navigate to Tools»Options»Environment, and disable the Maintain the Save Version of Loaded
 Projects by Default feature.
  3. Clear the compiled object cache in LabVIEW by navigating to Tools»Advanced»Clear Compiled Object Cache. 
 Note If you have files copied to
 user.lib or instr.lib, delete the
 .vidb cache file located at <LabVIEW Install
 Directory>\VIObjCache\<version>\objFileDB.vidb.
  4. Set the save version of your LabVIEW projects to Editor
 Version in the project properties.
  5. Delete any .lvversion files you created in your project
 folders.
  6. Mass-compile your LabVIEW files.
2. Option 2: Use the Version Independent Runtime Engine
 Support feature in TestStand.
  1. In TestStand, Enable the Enable Version Independent Runtime
 Engine option in the LabVIEW Adapter Configuration
 dialog box.
  2. Set the LabVIEW Runtime Version control to match the version
 of LabVIEW that you used to save or mass-compile your VIs.
  3. Restart TestStand.
3. Option 3: If your files do not need to be source-only, disable
 the Separate compiled code from source file setting for your VI,
 project, library, or entire environment in LabVIEW.

Parent topic:

LabVIEW Adapter

Related concepts:

- Build Source Files and Execute
- Version Independent Run-Time Engine Support

Related information:

- Saving for a Previous Version
- Separating Compiled Code From VIs and Other File Types

<!--NI_TOPIC bundle=teststand path=executing-a-sequence-directly.html language=enus -->
## TOPIC 00372: Executing a Sequence Directly

- bundle_id: `teststand`
- source_path: `executing-a-sequence-directly.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-a-sequence-directly.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To execute a sequence without using a process model, select Execute»Run <sequence name>, where <sequence name> is the name of the current sequence. Executing a sequence directly skips the process model operations, such as UUT identification and report generation. You can use this method to execute a

### Executing a Sequence Directly

To execute a sequence without using a process model, select Execute»Run <sequence name>, where <sequence name> is the name of the current sequence. Executing a sequence directly skips the process model operations, such as UUT identification and report generation. You can use this method to execute any sequence. Executing a sequence directly is helpful for performing unit testing or debugging.

Parent topic:

Executing Sequences

<!--NI_TOPIC bundle=teststand path=executing-a-sequence-in-an-application.html language=enus -->
## TOPIC 00373: Executing a Sequence in an Application

- bundle_id: `teststand`
- source_path: `executing-a-sequence-in-an-application.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-a-sequence-in-an-application.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The most direct way to create an execution is to execute a specific sequence in a specific sequence file. Although this method does not use a process model, it provides additional control for debugging. To execute a particular sequence, call the Engine.NewExecution method and pass the arguments list

### Executing a Sequence in an Application

The most direct way to create an execution is to execute a specific sequence in a specific sequence file. Although this method does not use a process model, it provides additional control for debugging. To execute a particular sequence, call the Engine.NewExecution method and pass the arguments listed in the following table.

| Parameter Name | What to Pass |
| --- | --- |
| sequenceFileParam | A reference to the sequence file that contains the sequence to execute. |
| sequenceNameParam | A string that contains the name of the sequence to execute. |
| processModelParam | A NULL reference. Depending on the application development environment you use, pass 0 or the Nothing keyword to indicate a NULL reference. |
| breakAtFirstStep | False. |
| executionTypeMaskParam | The value of the ExecTypeMask_Normal constant. |
| sequenceArgsParam[Optional] | Leave this parameter unspecified. |
| editArgsParam[Optional] | Leave this parameter unspecified. |
| InteractiveArgsParam[Optional] | Leave this parameter unspecified. |

Parent topic:

Writing an Application with the TestStand Engine API

<!--NI_TOPIC bundle=teststand path=executing-code-modules-in-an-external-instanc.html language=enus -->
## TOPIC 00374: Out-of-Process LabWindows/CVI Code Module Execution

- bundle_id: `teststand`
- source_path: `executing-code-modules-in-an-external-instanc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-code-modules-in-an-external-instanc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To execute tests in an external instance of LabWindows/CVI, the LabWindows/CVI Adapter launches a copy of the LabWindows/CVI development environment and loads an execution server project. You can specify the execution server project to load in the LabWindows/CVI Adapter Configuration dialog box. The

### Out-of-Process LabWindows/CVI Code Module
 Execution

To execute tests in an external instance of LabWindows/CVI, the LabWindows/CVI Adapter launches a copy of the LabWindows/CVI development environment and loads an execution server project. You can specify the execution server project to load in the LabWindows/CVI Adapter Configuration dialog box. The default project is <TestStand Public>\AdapterSupport\CVI\tscvirun.prj.

When a step calls a function in an object, static library, or DLL file, the execution server project automatically loads the code module and executes the function in an external instance of LabWindows/CVI. When you want a step to call a function in a C source file, you must include the C source file in the execution server project before you run the project. You must also include any support libraries other than LabWindows/CVI libraries the object, static library, or C source file requires.

#### Debugging Code Modules

You can debug C source and DLL code modules when the LabWindows/CVI Adapter executes tests in an external instance of LabWindows/CVI. To debug DLL code modules, you must create a debuggable DLL in LabWindows/CVI. LabWindows/CVI honors all breakpoints you set in the source files for the DLL project.

When you execute tests in an external instance of LabWindows/CVI, you do not need to launch the sequence editor or user interface application from LabWindows/CVI to debug DLL code modules you call with the LabWindows/CVI Adapter.

When you click Step Into in the sequence editor while the execution is suspended on a step that calls into the DLL code module, LabWindows/CVI suspends on the first statement in the called function.

Parent topic:

LabWindows/CVI Step Execution Locations

Related concepts:

- Search Directories
- Code Modules

<!--NI_TOPIC bundle=teststand path=executing-code-modules-in-parallel.html language=enus -->
## TOPIC 00375: Executing Code Modules in Parallel

- bundle_id: `teststand`
- source_path: `executing-code-modules-in-parallel.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-code-modules-in-parallel.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to run code modules in parallel. This sequence uses two Sequence Call steps that each call a subsequence in a new execution. Each subsequence calls a LabWindows/CVI code module to display a panel, which is updated by a loop in the MainSequence asynchronous from

### Executing Code Modules in Parallel

#### Purpose

This example demonstrates how to run code modules in parallel. This sequence uses two Sequence Call steps that each call a subsequence in a new execution. Each subsequence calls a LabWindows/CVI code module to display a panel, which is updated by a loop in the MainSequence asynchronous from the original execution.

#### Example File
 Location

<TestStand
 Public>\Examples\Parallel Testing\Executing Code Modules In
 Parallel\Executing Code Modules In Parallel.seq

#### Highlighted Features

- Sequence Call steps
- Wait steps

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane, select the Launch Display Panel 1 step, which is a Sequence Call step.
2. On the Step Settings pane, click the Sequence Call Module tab. The Execution Options ring control specifies the Use New Execution option.
3. Click the Sequence Call Advanced Settings button, located to the right of the Execution Options ring control, to launch the Sequence Call Advanced Settings window, in which the options change depending on the execution option you select. The Wait for Execution to Complete ring control specifies the Do not wait option. This sequence uses the Do not wait option and a set of Wait steps at the end of the MainSequence to collect results from each subsequence.
4. On the Steps pane, select the Wait on Panel 1 for Results step, which is a Wait step.
5. On the Step Settings pane, click the Wait Settings edit tab. The Specify by Sequence Call option specifies that the step waits for the Launch Display Panel 1 sequence call to finish executing. Similarly, the Wait on Panel 2 for Results step waits for the Launch Display Panel 2 sequence call to finish executing.
6. On the Sequences pane, select the Display 1 sequence.
7. On the Steps pane, select the Display Panel 1 step, which is an Action step that uses the LabWindows/CVI Adapter.
8. On the Step Settings pane, click the LabWindows/CVI Module tab. This step calls a DLL that polls the Counter1 file global variable and displays the content. Similarly, the Display Panel 2 step in the Display 2 sequence polls the Counter2 file global variable and displays the content.
9. On the Sequences pane, select the MainSequence and select Execute»Single Pass to run the sequence. TestStand begins three executions: one execution updates the Counter1 and Counter2 variables, and the other executions polls the values of the variables.
10. Click Stop for both Display Panel 1 and Display Panel 2. Scroll to the bottom of the report, which displays results for the Display Panel 1 and Display Panel 2 steps under the Wait steps for each new execution. If the sequence did not use Wait steps, TestStand would not log results for the steps run in new executions.

Parent topic:

Examples for Parallel Testing

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=executing-labwindows-cvi-code-modules-in-proc.html language=enus -->
## TOPIC 00376: In-Process LabWindows/CVI Code Module Execution

- bundle_id: `teststand`
- source_path: `executing-labwindows-cvi-code-modules-in-proc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-labwindows-cvi-code-modules-in-proc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When executing code modules in the same process as the sequence editor or user interface, the LabWindows/CVI Adapter loads and runs code modules directly without using the LabWindows/CVI development environment. Object and Library Code Modules When the LabWindows/CVI Adapter loads an object or stati

### In-Process LabWindows/CVI Code Module
 Execution

When executing code modules in the same process as the sequence editor or user interface, the LabWindows/CVI Adapter loads and runs code modules directly without using the LabWindows/CVI development environment.

#### Object and Library Code Modules

When the LabWindows/CVI Adapter loads an object or static library file, the LabWindows/CVI Run-Time Engine resolves all external references in the file. When running code modules in-process, the adapter must load the support libraries on which the object file or static library file depends before loading the code module file.

To configure a list of support libraries for the LabWindows/CVI Adapter to load, manually copy the support libraries to the <TestStand Public>\AdapterSupport\CVI\AutoLoadLibs directory.

#### Source Code Modules

When TestStand executes code modules in-process, the LabWindows/CVI Adapter cannot directly execute code modules that exist in C source files. Instead, the adapter attempts to find an object file with the same name. When the adapter finds the object file, it executes the code in the object file. When the adapter cannot find the object file, it prompts you to create the object file in an external instance of LabWindows/CVI. When you decline to create the object file, the adapter reports a run-time error.

#### Debugging DLL Code Modules

You can debug in-process code modules, but the code modules must exist in DLLs enabled for debugging in LabWindows/CVI at the time they were built. To debug a DLL in-process, you must launch the sequence editor or user interface from LabWindows/CVI. Select Run»Specify External Process in the LabWindows/CVI project window to identify the executable you want to launch. Select Run»Debug Project to launch the executable and begin debugging.

When you click Step Into in the sequence editor while the execution is suspended on a step that calls into a LabWindows/CVI DLL you are debugging, LabWindows/CVI suspends on the first statement in the DLL function.

In TestStand 2016 and later, the LabWindows/CVI debugger automatically attaches to a TestStand process when you
perform a step into operation on a LabWindows/CVI Adapter step. If the LabWindows/CVI
DLL is debuggable and the source code is available, LabWindows/CVI suspends the process
in the called DLL function; otherwise, TestStand performs a step over operation. You do not need to launch the Sequence Editor from LabWindows/CVI to access the debugger or
choose to attach the debugger to an existing process.

Note

Refer to the LabWindows/CVI documentation for more information about debugging DLLs.

Parent topic:

LabWindows/CVI Step Execution Locations

Related concepts:

- Code Modules
- Search Directories

<!--NI_TOPIC bundle=teststand path=executing-sequences-in-parallel.html language=enus -->
## TOPIC 00377: Executing Sequences in Parallel

- bundle_id: `teststand`
- source_path: `executing-sequences-in-parallel.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences-in-parallel.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to launch a parallel, independent sequence execution with a Sequence Call step in conjunction with a Wait step so that the execution results of the primary sequence are combined with the execution results of the subsequence. Alternatively, you can run the subseq

### Executing Sequences in Parallel

#### Purpose

This example demonstrates how to launch a parallel, independent sequence execution with a Sequence Call step in conjunction with a Wait step so that the execution results of the primary sequence are combined with the execution results of the subsequence.

Alternatively, you can run the subsequence in the same execution as the primary sequence. Review the report TestStand generates after either scenario to see the difference in where the results are collected for the Sequence Call steps.

#### Example File
 Location

<TestStand
 Public>\Examples\Parallel Testing\Executing Sequences In
 Parallel\Executing Sequences In Parallel.seq

#### Highlighted Features

- Sequence Call steps
- Wait steps

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane, select the Parallel Call step, which is a Sequence Call step.
2. On the Step Settings pane, click the Sequence Call Module tab. The Execution Options ring control specifies the Use New Execution option.
3. On the Steps pane, select the Sequential Call step, which is a Sequence Call step.
4. On the Step Settings pane, click the Sequence Call Module tab. The Execution Options ring control specifies the None option.
5. On the Steps pane, select the Wait step.
6. On the Step Settings pane, click the Wait Settings edit tab. The Specify by Sequence Call option specifies that the step waits for the Parallel Call sequence call to finish executing.
7. Select Execute»Single Pass to run the sequence.
8. Review the information in the dialog box that launches, and click the Run DemoSequence in New Execution button. A dialog box launches for each execution simultaneously. You may have to move or click OK in each dialog box to see the others.
9. Click OK in each dialog box.
10. Review the report. The results for the Message Popup step from the DemoSequence appears after the Wait step.
11. Select Execute»Restart to restart the MainSequence execution.
12. Review the information in the dialog box that launches, and click the Run DemoSequence Sequentially button. Now, only one dialog box launches at a time.
13. Click OK in each dialog box, and review the report. The Message Popup step from the DemoSequence now appears after the Message Popup 2 step.

Parent topic:

Examples for Parallel Testing

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=executing-sequences-remotely.html language=enus -->
## TOPIC 00378: Executing Sequences Remotely

- bundle_id: `teststand`
- source_path: `executing-sequences-remotely.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences-remotely.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use the Sequence Call Module tab to specify a sequence file pathname for a Sequence Call step and specify Use Remote Computer in the Execution Options section, TestStand locates the sequence file according to the type of path, as the following table describes. Type of Path Location at Edit

### Executing Sequences Remotely

When you use the Sequence Call Module tab to specify a sequence file pathname for a Sequence Call step and specify Use Remote Computer in the Execution Options section, TestStand locates the sequence file according to the type of path, as the following table describes.

| Type of Path | Location at Edit Time | Location During Execution | Example |
| --- | --- | --- | --- |
| Relative | In the TestStand search paths you configure on the client (local) computer | In the TestStand search paths you configure on the server (remote) computer | Transmit.seq |
| Absolute | On the client (local) computer | On the server (remote) computer | C:\\Projects\\Transmit.seq |
| Network | On the computer the network path specifies | On the computer the network path specifies | \\\\Remote\\Projects\\Transmit.seq |

When you edit a step in a sequence file on a client computer and you specify an absolute or relative path for the sequence file the step calls, TestStand resolves the path for the sequence file on the client computer. When you execute the step on the client computer, TestStand resolves the path for the sequence file on the server computer.

You can manage remote sequence files for remote execution in the following ways:

- Add a common pathname to the search paths for the client and the server computers so that each resolves to the same relative pathname.
- Duplicate the files on the client and the server computers so that the file you edit on the client computer is identical to the file the server computer executes.
- Use absolute paths that specify a mapped network drive or full network path so that the file the client computer edits and the file the server computer executes are the same sequence file.

When you execute a remote sequence, you cannot single-step or set breakpoints in the remote sequence. When you enable tracing, TestStand updates the status bar with tracing information for the remote sequence.

When a remote sequence executes on a server, the sequence context and call stack include only the sequences that run on the remote computer. When you want to access properties from the client sequence context, you must pass the PropertyObject objects or their values as parameters to the remote sequence. You can use the TestStand API to access properties within a property object.

Note

Parent topic:

Executing Sequences

Related concepts:

- Search Directories
- TestStand ActiveX API Overview
- Configuring Remote Executions

<!--NI_TOPIC bundle=teststand path=executing-sequences-using-api-labview.html language=enus -->
## TOPIC 00379: Executing Sequences Using API - LabVIEW

- bundle_id: `teststand`
- source_path: `executing-sequences-using-api-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences-using-api-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates various methods of calling a sequence using the TestStand API. If you are developing a TestStand user interface which must handle TestStand UI messages, do not use the WaitForEndEx() method, since this method does not process the UI messages while it waits for the e

### Executing Sequences Using API - LabVIEW

#### Purpose

This example demonstrates various methods of calling a sequence using the TestStand API.

Note

WaitForEndEx()

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Executing Sequences Using
 API\LabVIEW\Executing Sequences Using API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.GetSequenceFileEx
- Engine.NewExecution
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to review the sequences and steps in
 the example.

1. Open Executing Sequences Using API.seq .
2. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps that
 correspond to the different approaches demonstrated in this example.
3. On the Sequences pane, select the Execute With No Process
 Model sequence. This sequence uses the
 Engine.GetSequenceFileEx and
 Engine.NewExecution methods from the TestStand API to open
 and execute a sequence file. Because this type of execution does not use a
 process model, it is similar to selecting Execute»Run
 MainSequence in the target sequence file.
4. After execution completes, the Engine.ReleaseSequenceFileEx 
 method releases the target sequence file. This is a necessary step for any
 sequence file loaded with the Engine.GetSequenceFile 
 method.
5. On the Sequences pane, select the Execute With Process Model 
 sequence. This sequence loads a process model with the
 Engine.GetSequenceFileEx method and uses the
 Engine.NewExecution method to execute a client sequence
 file using one of the entry points from the process model.
6. On the Sequences pane, select the Execute With Sequence
 Parameters sequence. This sequence passes parameters to the
 target sequence by using the Engine.NewPropertyObject ,
 PropertyObject.SetValNumber , and
 PropertyObject.SetValString methods to create a container
 to store the parameters. The parameters must be declared in the same order they
 appear in the target sequence. Observe that the new
 PropertyObject container is passed to the
 Engine.NewExecution method as one of its parameters.
7. Open Target Sequence File.seq .
8. On the Sequences pane, select the MainSequence . This
 sequence includes a Message Popup step to indicate to the user that the sequence
 has executed.
9. On the Sequences pane, select the Subsequence . Observe
 that this sequence includes two parameters, which are displayed in the Message
 Popup step.

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. As each section of code executes, the Message Popup from the target sequence
 appears. Click OK on these dialog boxes to continue
 execution.
3. When the Execute With Sequence Parameters sequence executes,
 enter a number and string in the Message Popups that appear. Notice that these
 values are displayed in the final Message Popup.

Parent topic:

Executing Sequences Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=executing-sequences-using-api-labwindows-cvi.html language=enus -->
## TOPIC 00380: Executing Sequences Using API - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `executing-sequences-using-api-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences-using-api-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates various methods of calling a sequence using the TestStand API. If you are developing a TestStand user interface which must handle TestStand UI messages, do not use the WaitForEndEx() method, since this method does not process the UI messages while it waits for the e

### Executing Sequences Using API - LabWindows/CVI

#### Purpose

This example demonstrates various methods of calling a sequence using the TestStand API.

Note

WaitForEndEx()

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Executing Sequences Using
 API\CVI\Executing Sequences Using API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.GetSequenceFileEx
- Engine.NewExecution
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to review the sequences and steps in
 the example.

1. Open Executing Sequences Using API.seq .
2. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps that
 correspond to the different approaches demonstrated in this example.
3. On the Sequences pane, select the Execute With No Process
 Model sequence. This sequence uses the
 Engine.GetSequenceFileEx and
 Engine.NewExecution methods from the TestStand API to open
 and execute a sequence file. Because this type of execution does not use a
 process model, it is similar to selecting Execute»Run
 MainSequence in the target sequence file.
4. After execution completes, the Engine.ReleaseSequenceFileEx 
 method releases the target sequence file. This is a necessary step for any
 sequence file loaded with the Engine.GetSequenceFile 
 method.
5. On the Sequences pane, select the Execute With Process
 Model sequence. This sequence loads a process model with the
 Engine.GetSequenceFileEx method and uses the
 Engine.NewExecution method to execute a client sequence
 file using one of the entry points from the process model.
6. On the Sequences pane, select the Execute With Sequence
 Parameters sequence. This sequence passes parameters to the
 target sequence by using the Engine.NewPropertyObject ,
 PropertyObject.SetValNumber , and
 PropertyObject.SetValString methods to create a container
 to store the parameters. The parameters must be declared in the same order they
 appear in the target sequence. Observe that the new
 PropertyObject container is passed to the
 Engine.NewExecution method as one of its parameters.
7. Open Target Sequence File.seq .
8. On the Sequences pane, select the MainSequence . This
 sequence includes a Message Popup step to indicate to the user that the sequence
 has executed.
9. On the Sequences pane, select the Subsequence . Observe
 that this sequence includes two parameters, which are displayed in the Message
 Popup step.

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. As each section of code executes, the Message Popup from the target sequence
 appears. Click OK on these dialog boxes to continue
 execution.
3. When the Execute With Sequence Parameters sequence executes,
 enter a number and string in the Message Popups that appear. Notice that these
 values are displayed in the final Message Popup.

Parent topic:

Executing Sequences Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=executing-sequences-using-api-net.html language=enus -->
## TOPIC 00381: Executing Sequences Using API - .NET

- bundle_id: `teststand`
- source_path: `executing-sequences-using-api-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences-using-api-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates various methods of calling a sequence using the TestStand API. If you are developing a TestStand user interface which must handle TestStand UI messages, do not use the WaitForEndEx() method, since this method does not process the UI messages while it waits for the e

### Executing Sequences Using API - .NET

#### Purpose

This example demonstrates various methods of calling a sequence using the TestStand API.

Note

WaitForEndEx()

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Executing Sequences Using
 API\DotNet\Executing Sequences Using API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.GetSequenceFileEx
- Engine.NewExecution
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to review the sequences and steps in
 the example.

1. Open Executing Sequences Using API.seq .
2. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps that
 correspond to the different approaches demonstrated in this example.
3. On the Sequences pane, select the Execute With No Process
 Model sequence. This sequence uses the
 Engine.GetSequenceFileEx and
 Engine.NewExecution methods from the TestStand API to open
 and execute a sequence file. Because this type of execution does not use a
 process model, it is similar to selecting Execute»Run
 MainSequence in the target sequence file.
4. After execution completes, the Engine.ReleaseSequenceFileEx 
 method releases the target sequence file. This is a necessary step for any
 sequence file loaded with the Engine.GetSequenceFile 
 method.
5. On the Sequences pane, select the Execute With Process
 Model sequence. This sequence loads a process model with the
 Engine.GetSequenceFileEx method and uses the
 Engine.NewExecution method to execute a client sequence
 file using one of the entry points from the process model.
6. On the Sequences pane, select the Execute With Sequence
 Parameters sequence. This sequence passes parameters to the
 target sequence by using the Engine.NewPropertyObject ,
 PropertyObject.SetValNumber , and
 PropertyObject.SetValString methods to create a container
 to store the parameters. The parameters must be declared in the same order they
 appear in the target sequence. Observe that the new
 PropertyObject container is passed to the
 Engine.NewExecution method as one of its parameters.
7. Open Target Sequence File.seq .
8. On the Sequences pane, select the MainSequence . This
 sequence includes a Message Popup step to indicate to the user that the sequence
 has executed.
9. On the Sequences pane, select the Subsequence . Observe
 that this sequence includes two parameters, which are displayed in the Message
 Popup step.

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. As each section of code executes, the Message Popup from the target sequence
 appears. Click OK on these dialog boxes to continue
 execution.
3. When the Execute With Sequence Parameters sequence executes,
 enter a number and string in the Message Popups that appear. Notice that these
 values are displayed in the final Message Popup.

Parent topic:

Executing Sequences Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=executing-sequences-using-api-teststand-expre.html language=enus -->
## TOPIC 00382: Executing Sequences Using API - TestStand Expressions

- bundle_id: `teststand`
- source_path: `executing-sequences-using-api-teststand-expre.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences-using-api-teststand-expre.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates various methods of calling a sequence using the TestStand API. If you are developing a TestStand user interface which must handle TestStand UI messages, do not use the WaitForEndEx() method, since this method does not process the UI messages while it waits for the e

### Executing Sequences Using API - TestStand Expressions

#### Purpose

This example demonstrates various methods of calling a sequence using the TestStand API.

Note

WaitForEndEx()

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Executing Sequences Using
 API\TestStand Expressions\Executing Sequences Using
 API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.GetSequenceFileEx
- Engine.NewExecution
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to review the sequences and steps in
 the example.

1. Open Executing Sequences Using API.seq .
2. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps that
 correspond to the different approaches demonstrated in this example.
3. On the Sequences pane, select the Execute With No Process
 Model sequence. This sequence uses the
 Engine.GetSequenceFileEx and
 Engine.NewExecution methods from the TestStand API to open
 and execute a sequence file. Because this type of execution does not use a
 process model, it is similar to selecting Execute»Run
 MainSequence in the target sequence file.
4. After execution completes, the Engine.ReleaseSequenceFileEx 
 method releases the target sequence file. This is a necessary step for any
 sequence file loaded with the Engine.GetSequenceFile 
 method.
5. On the Sequences pane, select the Execute With Process
 Model sequence. This sequence loads a process model with the
 Engine.GetSequenceFileEx method and uses the
 Engine.NewExecution method to execute a client sequence
 file using one of the entry points from the process model.
6. On the Sequences pane, select the Execute With Sequence
 Parameters sequence. This sequence passes parameters to the
 target sequence by using the Engine.NewPropertyObject ,
 PropertyObject.SetValNumber , and
 PropertyObject.SetValString methods to create a container
 to store the parameters. The parameters must be declared in the same order they
 appear in the target sequence. Observe that the new
 PropertyObject container is passed to the
 Engine.NewExecution method as one of its parameters.
7. Open Target Sequence File.seq .
8. On the Sequences pane, select the MainSequence . This
 sequence includes a Message Popup step to indicate to the user that the sequence
 has executed.
9. On the Sequences pane, select the Subsequence . Observe
 that this sequence includes two parameters, which are displayed in the Message
 Popup step.

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. As each section of code executes, the Message Popup from the target sequence
 appears. Click OK on these dialog boxes to continue
 execution.
3. When the Execute With Sequence Parameters sequence executes,
 enter a number and string in the Message Popups that appear. Notice that these
 values are displayed in the final Message Popup.

Parent topic:

Executing Sequences Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=executing-sequences-using-api.html language=enus -->
## TOPIC 00383: Executing Sequences Using API

- bundle_id: `teststand`
- source_path: `executing-sequences-using-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences-using-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\TestStand API\Executing Sequences Using API directory contains the following examples.

### Executing Sequences Using API

The <TestStand
 Public>\Examples\TestStand API\Executing Sequences Using
 API directory contains the following examples.

- [Executing Sequences Using API - LabWindows/CVI](executing-sequences-using-api-labwindows-cvi.html)
- [Executing Sequences Using API - LabVIEW](executing-sequences-using-api-labview.html)
- [Executing Sequences Using API - .NET](executing-sequences-using-api-net.html)
- [Executing Sequences Using API - TestStand Expressions](executing-sequences-using-api-teststand-expre.html)

Parent topic:

Examples for the TestStand API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=executing-sequences.html language=enus -->
## TOPIC 00384: Executing Sequences

- bundle_id: `teststand`
- source_path: `executing-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can initiate an execution in the following ways: Launch a sequence through an Execution entry point Execute a sequence directly Interactively execute a group of steps During an execution, you can complete the following actions: Debug executions Terminate or abort executions Check for suspended o

### Executing Sequences

You can initiate an execution in the following ways:

- Launch a sequence through an Execution entry point
- Execute a sequence directly
- Interactively execute a group of steps

During an execution, you can complete the following actions:

- Debug executions
- Terminate or abort executions
- Check for suspended or stopped executions within code modules

The following figure illustrates how sequence files execute.

[IMAGE alt='image' src='GUID-A302FDD5-FE4A-4196-8829-CF5324FEAFCF-a5.svg']

Parent topic:

Executions

Related concepts:

- Using Execution Entry Points
- Executing a Sequence Directly
- Interactively Executing Steps
- Debugging Executions
- Terminating and Aborting Executions
- Checking for Suspended or Stopped Execution within Code Modules
- Executing Sequences in Parallel

<!--NI_TOPIC bundle=teststand path=executing-sql-commands-in-the-sql-editor-wind.html language=enus -->
## TOPIC 00385: Executing SQL Commands in the SQL Editor Window

- bundle_id: `teststand`
- source_path: `executing-sql-commands-in-the-sql-editor-wind.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-sql-commands-in-the-sql-editor-wind.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Database Viewer supports performing multiple delimited SQL commands in a single operation. The SQL commands you enter are split into multiple commands based on the command delimiter used, and these commands are executed sequentially. The Output Tab is updated with the results of all the commands in

### Executing SQL Commands in the SQL Editor Window

Database Viewer supports performing multiple delimited SQL commands in a single operation. The SQL commands you enter are split into multiple commands based on the command delimiter used, and these commands are executed sequentially. The Output Tab is updated with the results of all the commands in the batch.

The various databases management systems supported by TestStand use different delimiters for SQL commands. To maintain compatibility with all of these systems, Database Viewer supports the following command delimiters for databases:

- Access — ~
- MySQL and Sybase — ;
- Oracle — /
- SQL Server — GO

Note

Use each command delimiter on a new line. You should also add a new line after the delimiter and before the subsequent commands.

You can use any of the command delimiters mentioned above for execution of multiple commands from Database Viewer. Refer to the following example of delimited SQL commands entered using the ; command delimiter for MySQL and Sybase:

```text
CREATE TABLE PROP_BINARY
(
ID                      CHAR (38) PRIMARY KEY,
PROP_RESULT             CHAR (38) NOT NULL,
UPPER_BOUNDS            VARCHAR (32),
LOWER_BOUNDS            VARCHAR (32),
DATA_FORMAT             VARCHAR (32),
DATA                    MEDIUMBLOB,
CONSTRAINT PROP_BINARY_FK FOREIGN KEY (PROP_RESULT) REFERENCES PROP_RESULT (ID)
)
;
CREATE TABLE PROP_NUMERICLIMIT
(
ID                      CHAR (38) PRIMARY KEY,
PROP_RESULT             CHAR (38) NOT NULL,
COMP_OPERATOR           VARCHAR (32),
HIGH_LIMIT              DOUBLE,
LOW_LIMIT               DOUBLE,
UNITS                   VARCHAR (255),
STATUS                  VARCHAR (255),
CONSTRAINT PROP_NUMERICLIMIT_FK FOREIGN KEY (PROP_RESULT) REFERENCES PROP_RESULT (ID)
)
;
```

The following individual SQL commands are identified and executed sequentially:

```text
CREATE TABLE PROP_BINARY
(
ID                      CHAR (38) PRIMARY KEY,
PROP_RESULT             CHAR (38) NOT NULL,
UPPER_BOUNDS            VARCHAR (32),
LOWER_BOUNDS            VARCHAR (32),
DATA_FORMAT             VARCHAR (32),
DATA                    MEDIUMBLOB,
CONSTRAINT PROP_BINARY_FK FOREIGN KEY (PROP_RESULT) REFERENCES PROP_RESULT (ID)
)
```

and

```text
CREATE TABLE PROP_NUMERICLIMIT
(
ID                      CHAR (38) PRIMARY KEY,
PROP_RESULT             CHAR (38) NOT NULL,
COMP_OPERATOR           VARCHAR (32),
HIGH_LIMIT              DOUBLE,
LOW_LIMIT               DOUBLE,
UNITS                   VARCHAR (255),
STATUS                  VARCHAR (255),
CONSTRAINT PROP_NUMERICLIMIT_FK FOREIGN KEY (PROP_RESULT) REFERENCES PROP_RESULT (ID)
)
;
```

The SQL commands you enter can also contain comments.
For single line comments, use the following syntax:

- Access, Oracle and SQL Server — #<comment text><new line>
- MySQL — --<comment text><new line>
- Sybase — //<comment text><new line>

For multi-line comments, use the following syntax:

/*<comment text>

<comment text>*/

Note

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand path=executing-vis-with-separate-compiled-code.html language=enus -->
## TOPIC 00386: Executing VIs with Separate Compiled Code

- bundle_id: `teststand`
- source_path: `executing-vis-with-separate-compiled-code.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executing-vis-with-separate-compiled-code.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In LabVIEW 2010 or later, you can separate compiled code from a VI. When you open a VI with separate compiled code, LabVIEW generates and saves a VI object file (.viobj) with the compiled code. When you separate compiled code from a VI, recompiling the code of the VI does not create an unsaved chang

### Executing VIs with Separate Compiled Code

In LabVIEW 2010 or later, you can separate compiled code from a VI.

When you open a VI with separate compiled code, LabVIEW generates and saves a VI object file (.viobj) with the compiled code.

When you separate compiled code from a VI, recompiling the code of the VI does not create an unsaved change. As a result, if you use a source code control system, you do not have to check out all the files in a hierarchy when you edit a VI.

TestStand supports calling these VIs from LabVIEW. During deployment, the TestStand Deployment Utility converts these VIs with separated compiled code to regular VIs so that TestStand can execute these VIs using the LabVIEW Run-Time Engine on the deployed machine.

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Deploying TestStand Systems
- Partially Specifying LabVIEW Clusters
- Evaluating Conditional Disable Structures and Symbols
- Processing LabVIEW Code Modules for Deployment

<!--NI_TOPIC bundle=teststand path=execution-entry-points-in-the-sequential-proc.html language=enus -->
## TOPIC 00387: Execution Entry Points in the Sequential Process Model

- bundle_id: `teststand`
- source_path: `execution-entry-points-in-the-sequential-proc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/execution-entry-points-in-the-sequential-proc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Sequential process model includes the following Execution entry point sequences: Test UUTs—Tests and identifies multiple UUTs in a loop. The Execute menu includes the Test UUTs item when a window for a client sequence file is active. When you select the Test UUTs Execution entry point to start a

### Execution Entry Points in the Sequential Process Model

The Sequential process model includes the following Execution entry point sequences:

- Test UUTs—Tests and identifies multiple UUTs in a loop. The Execute menu includes the Test UUTs item when a window for a client sequence file is active. Note When you select the Test UUTs Execution entry point to start an execution that continuously tests UUTs, any subsequent configuration changes you make to model options, report options, database logging options, or other result processing options do not affect UUTs tested in the execution.
- Single Pass—Tests one UUT without identifying the UUTs. The Single Pass Execution entry point performs a single iteration of the loop the Test UUTs Execution entry point performs. The Execute menu includes the Single Pass item when a window for a client sequence file is active.

Parent topic:

Sequential Process Model

Related concepts:

- Test UUTs Execution Entry Point in the Sequential Process Model
- Single Pass Execution Entry Point in the Sequential Process Model

<!--NI_TOPIC bundle=teststand path=execution-events.html language=enus -->
## TOPIC 00388: Execution Events

- bundle_id: `teststand`
- source_path: `execution-events.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/execution-events.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most user interface messages notify you to update an Execution window. When you receive one of these user interface messages, use the UIMessage.Execution property to obtain a reference to the Execution object to which the message applies. Use the Execution.Id property to determine which user interfa

### Execution Events

Most user interface messages notify you to update an Execution window. When you receive one of these user interface messages, use the UIMessage.Execution property to obtain a reference to the Execution object to which the message applies. Use the Execution.Id property to determine which user interface display to update.

The following user interface messages apply to executions:

- Start/End Events—If you receive a UIMsg_StartExecution event, create a new window for the
 execution or reinitialize an existing window for the execution. The Execution
 window already exists when the user restarts the execution. If you receive a
 UIMsg_EndExecution event, modify the display for the execution to show that the
 execution has ended. Then, release any handles to Thread ,
 Step , or SequenceContext objects you have
 for the execution, and display the execution report, if one exists. TestStand
 posts the UIMsg_StartInteractiveExecution and UIMsg_EndInteractiveExecution
 events to notify you when the user runs steps interactively in an execution.
 The user can run steps interactively in a new execution or from an existing
 execution while at a breakpoint. TestStand posts the
 UIMsg_StartFileExecution and UIMsg_EndFileExecution events to notify the
 user interface of the period during which an execution uses a particular
 sequence file. You can use this information to disable the editing of the
 sequence file or to indicate that it is in use.
- Break Events—TestStand posts the UIMsg_BreakOnBreakpoint, UIMsg_BreakOnUserRequest, or
 UIMsg_BreakOnRunTimeError user interface message when an execution enters a
 suspended state. Each of these messages indicates a different reason for the
 change in state. For each of these events, you can choose to display the
 following information: To display information about the steps in the currently executing step
 group, you must first obtain the foreground Thread object by obtaining the value
 of the Execution.ForegroundThreadIndex property and then calling the
 Execution.GetThread method with the index. From the Thread 
 object, you can then obtain the SequenceContext object that represents the top
 of the call stack by calling the Thread.GetSequenceContext method. Pass
 0 for the call stack index and then pass a variable in
 which to store the frame ID, which is a unique identifier for the call stack
 entry. The frame ID is not required to handle this event, but is useful when
 handling . Once you have the SequenceContext object, you can access all the
 information about the currently executing sequence. The Sequence object from
 the SequenceContext.Sequence property provides the run-time copy of the
 sequence. Access this run-time copy to obtain all the information about the
 steps you require. You can also use the other
 SequenceContext properties to obtain information such
 as the currently executing step group, the sequence file that contains the
 executing sequence, and other information. To display a call stack
 list, first obtain the Thread.CallStackSize property of the current thread
 to determine the number of call stack entries. Then obtain the
 SequenceContext object for each entry by passing its
 zero-based index to the Thread.GetSequenceContext method.
 Use the SequenceContext.CallStackName property to obtain the display name
 for an entry. To display a thread list, first obtain the number of
 threads from the Execution.NumThreads property. Then, obtain each thread by
 passing its zero-based index to the Execution.GetThread
 method. Obtain the display name of the thread from the Thread.DisplayName
 property. When you receive the UIMsg_BreakOnRunTimeError event,
 display the run-time error to the user after updating the user interface.
 Obtain the run-time error message from the
 SequenceContext.GetRunTimeErrorMessageEx method for the top-level
 SequenceContext. Resuming execution from a
 UIMsg_BreakOnRunTimeError event causes the execution to
 go to the Cleanup step group. To ignore the run-time error, you must first
 call the Thread.ClearCurrentRTE method of the foreground thread. However,
 for trace events, call the Engine.DisplayRunTimeErrorDialogEx method to
 launch the Run-time Error dialog box. You can also create a custom dialog
 box to launch instead.
  - Information about the steps in the currently executing step group
  - A call stack list that identifies the locations of the active sequence
 calls in the current thread
  - A list of the threads the execution contains
- Trace Events—The update to the user interface a UIMsg_Trace event requires is very similar to
 that of a break event, except that you use only the name of the foreground
 thread and the top entry in the call stack list instead of the names of all the
 threads and call stack entries because the user interface disallows switching
 threads or browsing the call stack while tracing. In addition, because the trace
 event does not indicate a suspended state, you do not need to call the
 Execution.Resume method to continue. Instead, execution continues automatically
 when you finish handling the user interface message for the trace event by
 releasing the user interface message or returning from the event handling
 callback sequence. In addition, you can use the frameId 
 output parameter of the Thread.GetSequenceContext method to
 update the display. As an optimization, the user interface holds the step
 group and frameId value from the last trace event. If
 the next event is a trace event and its sequence context specifies the same
 frameId value and step group, you need only to
 update the display of the previously executed step and the step to execute
 next. Because this is typically the case when users trace through a long
 list of steps in the same sequence and step group, this optimization can
 significantly increase the maximum tracing speed of the
 application. Note If the application polls for
 user interface messages, the rate at which you poll limits the maximum
 tracing rate.
- Resume Events—TestStand posts the UIMsg_ResumeFromBreak event to the user interface whenever an
 execution is about to resume from a suspended state. This event allows the user
 interface to update the enabled state of controls on its execution display and
 to show that the execution is running.
- Execution State Change Events—The purpose of the execution state change events is to notify the
 user interface that the state of an execution is about to change. The action
 these events specify does not occur until you finish handling the user interface
 message by releasing the user interface message or returning from the event
 handling callback. also signify an execution state change. The name of the
 following execution state change events indicate the meaning for each
 event:
  - UIMsg_TerminatingExecution
  - UIMsg_TerminationCancelled
  - UIMsg_TerminatingInteractiveExecution
  - UIMsg_AbortingExecution
  - UIMsg_KillingExecutionThreads
- Progress Events—A step posts progress events to notify the user interface to update its
 progress indicator or text message, if one exists. If you receive a
 UIMsg_ProgressPercent event, check the UIMessage.NumericData property for the
 percentage of the progress indicator to shade. If you receive a
 UIMsg_ProgressText event, you can find the text to display in the
 UIMessage.StringData property.

Parent topic:

Handling Specific User Interface Messages

Related concepts:

- Posting User Interface Messages

<!--NI_TOPIC bundle=teststand path=execution-profiler.html language=enus -->
## TOPIC 00389: Execution Profiler

- bundle_id: `teststand`
- source_path: `execution-profiler.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/execution-profiler.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the button to launch the Execution Profiler window to view and record duration of steps, code modules, and other resources a multithreaded TestStand system uses over a period of time. You can review the recorded data in graphs and sortable tables to identify performance bottlenecks and design

### Execution Profiler

Select the [IMAGE alt='image' src='GUID-18777715-AE81-4ADE-A132-AE41A70E61A2-a5.gif'] button to launch the Execution Profiler window to view and
 record duration of steps, code modules, and other resources a multithreaded TestStand
 system uses over a period of time.

You can review the recorded data in graphs and sortable tables to identify performance bottlenecks and design flaws and to gain insight into the behavior and timing of complex multithreaded systems. You can copy the information to external applications, such as Microsoft Word or Excel.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Comparing Resource Usage Strategies

Related information:

- Synchronization Step Types

<!--NI_TOPIC bundle=teststand path=executions.html language=enus -->
## TOPIC 00390: Executions

- bundle_id: `teststand`
- source_path: `executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you run a sequence, TestStand creates an Execution object that contains all the information TestStand needs to run the sequence and subsequences, as shown in the following figure. When an execution is active, you can start other executions by running the same sequence again or by running differ

### Executions

When you run a sequence, TestStand creates an Execution object that contains all the information TestStand needs to run the sequence and subsequences, as shown in the following figure.

[IMAGE alt='image' src='GUID-360BB1D8-FD88-48A6-91F1-2763BDA6ABCD-a5.svg']

When an execution is active, you can start other executions by running the same sequence again or by running different sequences. TestStand does not limit the number of executions you can run concurrently.

An execution can start with a single thread. You can use Sequence Call multithreading options to create additional threads within an execution or to launch new executions. An execution groups related threads so that setting a breakpoint suspends all threads in the execution. When you suspend, terminate, or abort an execution, you stop all threads in the execution.

Multiple instances of a sequence can run at the same time, such as when you call a sequence recursively or when a sequence runs in multiple concurrent threads. For each instance of the sequence, TestStand creates a copy of the sequence parameters, local variables, and custom properties of each step. When a sequence completes, TestStand discards the values of the parameters, local variables, and discards the values of custom properties when you set the value of the Optimize Non-Reentrant Calls to This Sequence option on the General tab of the Sequence Properties dialog box to False.

When TestStand begins executing a sequence, it creates a run-time copy of the sequence local variables and the custom properties of the steps in a sequence. If the sequence calls itself recursively, TestStand creates a separate run-time copy of the local variables and custom step properties for each running instance of the sequence. Modifications to the values of local variables and custom step properties apply only to the run-time copy and do not affect the sequence file in memory or on disk.

Note

For each execution thread, TestStand maintains an execution pointer that points to the current step, a call stack, and a run-time copy of the local variables and custom properties for all sequences and steps on the call stack.

The Execution tab of the Station Options dialog box tab provides a number of execution options that control tracing, breakpoints, and result collection.

Parent topic:

Fundamentals

Related concepts:

- Built-In Step Properties
- Sequences

<!--NI_TOPIC bundle=teststand path=executionview-manager.html language=enus -->
## TOPIC 00391: ExecutionView Manager

- bundle_id: `teststand`
- source_path: `executionview-manager.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/executionview-manager.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ExecutionView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected TestStand execution: Designates an execution as the selected execution. Tracks which thread, stack frame, sequence, step group, and step

### ExecutionView Manager

The ExecutionView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected TestStand execution:

- Designates an execution as the selected execution.
- Tracks which thread, stack frame, sequence, step group, and steps users select in the execution.
- Tracks which variables or properties users select in the execution.
- Displays aspects of the selected execution in the visible TestStand UI Controls to which the ExecutionView Manager control connects.
- Enables visible TestStand UI Controls to which the ExecutionView Manager control connects to change the selected thread, stack frame, sequence, step group, and steps.
- Sends events to notify the application of the progress and state of the execution.
- Provides debugging commands.
- Updates the ReportView control to show the current report for the execution.

An application needs one ExecutionView Manager control for each location, such as a window, form, or panel, in which you display an execution or let users select an execution.

Parent topic:

Manager Controls

Related concepts:

- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=exporting-class-methods-and-functions-in-micr.html language=enus -->
## TOPIC 00392: Exporting Class Methods and Functions in Microsoft Visual Studio

- bundle_id: `teststand`
- source_path: `exporting-class-methods-and-functions-in-micr.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/exporting-class-methods-and-functions-in-micr.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the C/C++ DLL Adapter to call functions and static class methods in DLLs. The C/C++ DLL Adapter obtains a list of available functions and methods from the list of exports contained in the DLL file. In addition, the C/C++ DLL Adapter determines parameter type information by reading a type library

### Exporting Class Methods and Functions in Microsoft Visual Studio

Use the C/C++ DLL Adapter to call functions and static class methods in DLLs. The C/C++ DLL Adapter obtains a list of available functions and methods from the list of exports contained in the DLL file. In addition, the C/C++ DLL Adapter determines parameter type information by reading a type library or by examining the decorated names the Microsoft Visual Studio compiler generates.

To ensure that the functions and methods are available to the C/C++ DLL Adapter, follow these rules when defining the functions and classes:

- Use __declspec(dllexport) to export the function or method. You can export an entire C++ class by placing the __declspec(dllexport) before the class name, or you can export a single method by placing __declspec(dllexport) before the method name.
- Make class methods static and public. The C/C++ DLL Adapter does not allow you to call public non-static methods.
- Use only types the C/C++ DLL Adapter recognizes.
- Avoid using a .DEF file to export symbols. Using a .DEF file prevents the C/C++ DLL Adapter from obtaining type information for function and method parameters.
- Avoid using the extern "C" syntax to export symbols. The extern "C" syntax prevents the C/C++ DLL Adapter from obtaining type information for function and method parameters.

Refer to the following examples for more information:

#### Example 1

class __declspec(dllexport) ClassName
{

public:
static void MethodName(void);

};

#### Example 2

class ClassName
{

public:
static void __declspec(dllexport) MethodName(void);

};

#### Example 3

void __declspec(dllexport) Function(void);

Parent topic:

C/C++ DLL Adapter

<!--NI_TOPIC bundle=teststand path=exporting-values-to-an-sle-server.html language=enus -->
## TOPIC 00393: Exporting Values to an SLE Server from TestStand

- bundle_id: `teststand`
- source_path: `exporting-values-to-an-sle-server.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/exporting-values-to-an-sle-server.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: When specifications are imported into a sequence file from an SLE server, the SLE data result processing plug-in is automatically added to the active processing configuration. This plug-in generates a measurement data file with all measurement values logged during an execution. You can upload these

### Exporting Values to an SLE Server from
 TestStand

When specifications are imported into a sequence file from an SLE server, the SLE data
 result processing plug-in is automatically added to the active processing configuration.
 This plug-in generates a measurement data file with all measurement values logged during an
 execution. You can upload these measurement values to SLE at the end of an
 execution.

To export specifications from TestStand to an SLE server, Specify options for the
 generated SLE data report file using the SystemLink Enterprise Report
 Options dialog box:

1. Open the SystemLink Enterprise Report Options dialog box
 by clicking on the icon in the Options column for the SLE
 data reporting plug-in in the Result Processing dialog
 box. 
 [IMAGE alt='image' src='GUID-5962FFCB-1868-4D07-A79F-A79EF3ECD352-a5.png']
2. Set the directory where the report generator writes the report file using the
 Report Directory ring control.
3. Ensure you upload the SLE data report file to SLE after the report is generated
 by enabling the Upload Report to SystemLink Enterprise
 option. 
 [IMAGE alt='image' src='GUID-2DB7315F-5D2D-4C98-99CE-757D4986B145-a5.png']
 Note The Upload
 Report to SystemLink Enterprise option is enabled by
 default, so uploading the measurement data file to SLE is the default
 behavior of the SLE data result processing plug-in.

Parent topic:

Importing Specifications into TestStand Using the Specifications Pane

<!--NI_TOPIC bundle=teststand path=express-vis-and-property-node-calls-in-32-bit.html language=enus -->
## TOPIC 00394: Express VIs and Property Node Calls in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `express-vis-and-property-node-calls-in-32-bit.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/express-vis-and-property-node-calls-in-32-bit.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW steps that invoke Express VIs or property nodes embed the configured VI in step properties as files that include the front panel, block diagram, and compiled code. You can use the 32-bit LabVIEW development system and the 64-bit LabVIEW development system to execute steps with embedded VIs w

### Express VIs and Property Node Calls in 32-bit TestStand and 64-bit TestStand

LabVIEW steps that invoke Express VIs or property nodes embed the configured VI in step properties as files that include the front panel, block diagram, and compiled code.

You can use the 32-bit LabVIEW development system and the 64-bit LabVIEW development system to execute steps with embedded VIs without modifying the sequence file because LabVIEW recompiles the embedded VIs at execution. If you use the LabVIEW Run-Time Engine (RTE) to execute steps, the bitness of TestStand must match the bitness of the LabVIEW development system that last configured or saved the embedded VI. In TestStand, select Tools»Update VI Calls to update Express VIs and property node calls to use the appropriate version of LabVIEW.

#### Using Express VIs and Property Node Calls in Step Types

When you use the LabVIEW RTE to call a LabVIEW step configured with Express VIs or property node calls, you must provide separate step types that correspond to each version and bitness of LabVIEW you support. This restriction does not apply when you use the LabVIEW development system to call step types configured with Express VIs or property node calls because LabVIEW recompiles the embedded VI. Selecting Tools»Update VI Calls does not update step types. You can allow users to manually update the prototype to specify the version and bitness of LabVIEW to use, but this action causes the step type to change.

Parent topic:

LabVIEW Code Module Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=expression-operators.html language=enus -->
## TOPIC 00395: Expression Operators

- bundle_id: `teststand`
- source_path: `expression-operators.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/expression-operators.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: 6 Expression Operators Operator Class Operators in Symbol Form Arithmetic The arithmetic symbols include the following items: +, -, *, /, MOD, %, ++, and --. Assignment The assignment symbols include the following items: =, +=, -=, *=, /=, %=, ^=, &=, and |=. The equal operator evaluates the express

### Expression Operators

| Operator Class | Operators in Symbol Form |
| --- | --- |
| Arithmetic | The arithmetic symbols include the following items: +, -, *, /, MOD, %, ++, and --. |
| Assignment | The assignment symbols include the following items: =, +=, -=, *=, /=, %=, ^=, &=, and \|=. The equal operator evaluates the expression on the right side of the operator and sets the operand on the left side of the operator to the result. When operating on container properties, the hierarchy of subproperty names on the left and right side must match. For each property value, the assignment converts between different data types whenever possible, for example, numeric to string. |
| Bitwise | The bitwise symbols include the following items: AND, OR, NOT, XOR, &, \|, ~, ^ , >>, and <<. |
| Comparison | The comparison symbols include the following items: ==, !=, <>, >, >=, <, and <=. Floating-point comparisons use 14 digits of precision.Comparison operators work on string, numeric, and Boolean values. If one operand is a string and another is a numeric, the operator converts the string to a numeric value. If both operands are strings, the comparison is case-insensitive. If both operands are non-zero floating-point numeric values, the comparison uses 14 digits of precision. TestStand treats NAN and IND as equivalent in expression comparisons. |
| Logical | The logical symbols include the following items: &&, \|\|, and !. |
| Other | Some additional operators include the following items: () Parentheses—Alter evaluation order. . Dot—Property field separator. .. Double Dot—Specify a range of indexes in array subscripts. This operator indexes multiple elements in the array and returns a subarray. The operand on each side of the range operator must evaluate to a numeric value, such as array[1..3]. [] Brackets—Array subscript Note The operand for an array subscript must evaluate to a numeric value, unless the array contains step or sequence elements. For arrays of step or sequence elements, the subscript can evaluate to a string value that contains the name of a step or sequence element in the array, such as RunState.Sequence.Main["MyGoto"]. You can use the double dot operator (..) within the [] operator to index multiple elements in the array and return a subarray. For example, the expression array[1..3][2] returns the elements at indexes [1][2], [2][2], and [3][2] in a new subarray., Comma—Expression separator or terminator. ?: Conditional—Given a Boolean value, chooses one of two other expressions to evaluate Usage: booleanValue ? expr1 : expr2{} Array constant. // Single line comment (C++). ’ Single line comment (Basic). /* */ Comment (C/C++). & Get Reference—Returns a Reference that refers to the operand. * Dereference—Returns the object to which the Reference operand refers. The Reference must refer to an object that supports the TestStand PropertyObject interface. -> Dereference and access field—Returns the specified subproperty of the object to which the Reference operand refers. The Reference must refer to an object that supports the TestStand PropertyObject interface. |
| Constants | The formats for the different types of constants include the following items:1.23e-4 Floating point 1234 Integer 0x1234efa9 Hexadecimal integer 0b11011011 Binary number 1234i64 64-bit integer constant 1234ui64 64-bit unsigned integer constant True Boolean False Boolean "1234wxyz" String @"file path" Unescaped string, such as @"C:\\Windows\\temp" Nothing Empty ActiveX reference NAN Not a number IND Indeterminate number INF Infinite number PI PI constant (3.141592...) tsRed Color constant Note TestStand declares some special constant values that are similar to values used in other environments or used infrequently. |

Parent topic:

Expressions

Related concepts:

- Levels of Precedence in Operators
- Special Constant Values

<!--NI_TOPIC bundle=teststand path=expression.html language=enus -->
## TOPIC 00396: Expression

- bundle_id: `teststand`
- source_path: `expression.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/expression.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Expression standard data type to store an expression as a string so TestStand can locate expression values saved in variables and step properties when editing or analyzing sequence files.

### Expression

Use the Expression standard data type to store an expression as a string so TestStand can locate expression values saved in variables and step properties when editing or analyzing sequence files.

Parent topic:

Using Standard Named Data Types

Related concepts:

- Expressions

<!--NI_TOPIC bundle=teststand path=expressions.html language=enus -->
## TOPIC 00397: Expressions

- bundle_id: `teststand`
- source_path: `expressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/expressions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the values of variables and properties in numerous ways, such as passing a variable to a code module or using a property value to determine whether to execute a step. For these same purposes, you can use an expression, which is a formula that calculates a new value from the values of mul

### Expressions

You can use the values of variables and properties in numerous ways, such as passing a variable to a code module or using a property value to determine whether to execute a step. For these same purposes, you can use an expression, which is a formula that calculates a new value from the values of multiple variables or properties. In expressions, you can access all variables and properties active in the sequence context when TestStand evaluates the expression.

You can use an expression wherever you would use a simple variable or property value. TestStand supports all applicable expression operators and syntax you can use in C, C++, Java, and Visual Basic .NET. You can also call the TestStand API directly from within expressions.

The following is an example of an expression:

Locals.MidBandFrequency = (Step.HighFrequency +Step.LowFrequency) / 2

All TestStand controls that accept expressions provide context-sensitive editing features, such as drop-down lists, syntax checking, and expression coloring to help you create expressions. At any point while editing an expression, you can press <Ctrl-Space> to show a drop-down list of valid expression elements.

The expression editor includes visual assistance for finding and manipulating nested delimiters such as parenthesis, brackets, and braces.

- Place your cursor to the left of a delimiter and the expression editor makes the matching pair bold.
- Type <Ctrl + ]> to toggle the cursor between the matching delimiters.
- Type <Ctrl + Shift + ]> to select the matching delimiters and everything between them.

Parent topic:

TestStand Building Blocks

Related concepts:

- Expression Operators
- TestStand ActiveX API Overview
- Statement Step Type

<!--NI_TOPIC bundle=teststand path=extended-support-changes.html language=enus -->
## TOPIC 00398: Updates and Changes for TestStand Extended Support Versions

- bundle_id: `teststand`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/extended-support-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in TestStand versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible change

### Updates and Changes for TestStand Extended Support Versions

Browse updates and changes made in TestStand versions
 on extended support.

Note

Release Notes

- [TestStand 2022 Q4 Changes](teststand-2022-q4-changes.html) Learn about new features, behavior changes, and other updates in TestStand 2022 Q4.
- [TestStand 2021 SP1 Changes](teststand-2021-sp1-changes.html) Learn about new features, behavior changes, and other updates in TestStand 2021 SP1.
- [TestStand 2021 Changes](teststand-2021-changes.html) Learn about new features, behavior changes, and other updates in TestStand 2021.
- [TestStand 2020 Changes](teststand-2020-changes.html) Learn about new features, behavior changes, and other updates in TestStand 2020.
- [TestStand 2019 Changes](teststand-2019-changes.html) Learn about new features, behavior changes, and other updates in TestStand 2019.
- [TestStand 2017 SP1 Changes](teststand-2017-sp1-changes.html) Learn about new features, behavior changes, and other updates in TestStand 2017 SP1.
- [TestStand 2017 Changes](teststand-2017-changes.html) Learn about new features, behavior changes, and other updates in TestStand 2017.

<!--NI_TOPIC bundle=teststand path=extending-teststand.html language=enus -->
## TOPIC 00399: Extending TestStand

- bundle_id: `teststand`
- source_path: `extending-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/extending-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure TestStand using the following components: Test Station Options—You can customize options that apply to all TestStand applications. TestStand Sequence Editor Options and Panes—You can customize options and the panel and document layout of the sequence editor. TestStand User Interfac

### Extending TestStand

You can configure TestStand using the following components:

- Test Station Options —You can customize options that apply to all TestStand applications.
- TestStand Sequence Editor Options and Panes —You can customize options and the panel and document layout of the sequence editor.
- TestStand User Interface Options —You can customize options for user interfaces.
- Tools Menu —You can customize the Tools menus in the TestStand Sequence Editor and User Interfaces to contain exactly the tools you need.
- Directory Structure —You can customize the search path TestStand uses to locate files specified by relative paths.
- Adapters —You can configure unique settings for each adapter, such as specifying which run time to use or whether to display parameter information.
- Result Processing and Model Options —

You can also customize the following TestStand components:

- Data Types —You can customize copies of the standard data types or create and modify your own data types
- Step Types —You can customize copies of the standard step types or create and modify your own step types.
- Callbacks —You can modify callbacks to customize the operation of test stations.
- Process Model Plug-ins —TestStand includes process model plug-ins that perform functions such as reporting and database logging. You can create custom process model plug-ins to extend the functionality of all process models.
- User Interfaces —TestStand includes full source code in several different programming languages so you can modify the user interfaces to meet the specific needs of your application.
- Process Models —TestStand includes fully customizable Sequential, Parallel, and Batch process models to meet specific testing needs.
- Sequence File Translators —You can create sequence file translators to generate and load a sequence file from a test description file saved in a custom format, such as XML or text.
- TestStand Sequence Analyzer Rules —You can customize options for built-in rules and create custom rules to evaluate during sequence analysis.

#### Configure Menu

Use the Configure menu in the TestStand Sequence Editor and in a TestStand User Interface to control the operation of the TestStand station.

Related concepts:

- Customizing the Tools Menu
- Data Types
- Type Concepts
- Custom Step Types
- Customizing Process Models and Callbacks
- Process Model Plug-In Architecture
- Creating Custom User Interfaces

<!--NI_TOPIC bundle=teststand path=failure-chain-in-reports.html language=enus -->
## TOPIC 00400: Failure Chain in Reports

- bundle_id: `teststand`
- source_path: `failure-chain-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/failure-chain-in-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: For UUTs that fail, ATML 6.01, ATML 5.0, XML, HTML, and ASCII-text reports include in the report header a failure chain section, which includes the following information: The first item in the failure chain table shows the step failure that caused the UUT to fail. The remaining items show the Sequen

### Failure Chain in Reports

For UUTs that fail, ATML 6.01, ATML 5.0, XML, HTML, and ASCII-text reports include in the report header a failure chain section, which includes the following information:

- The first item in the failure chain table shows the step failure that caused the UUT to fail.
- The remaining items show the Sequence Call steps through which the execution reached the failing step.

In ATML 6.01, ATML 5.0, XML, and HTML reports, each step name in the failure chain links to the section of the report that displays the result for the step.

Parent topic:

Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=features-64-bit-teststand-does-not-support.html language=enus -->
## TOPIC 00401: Features 64-Bit TestStand does not Support

- bundle_id: `teststand`
- source_path: `features-64-bit-teststand-does-not-support.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/features-64-bit-teststand-does-not-support.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: 64-bit TestStand does not support the following features: IVI Step Types—Use code modules to communicate with IVI drivers. HTBasic Adapter—HTBasic steps do not execute in 64-bit TestStand. Measurement Studio C++ MFC data types—No 64-bit version of Measurement Studio C++ MFC exists. As a workaround,

### Features 64-Bit TestStand does not Support

64-bit TestStand does not support the following features:

- IVI Step Types —Use code modules to communicate with IVI drivers.
- HTBasic Adapter —HTBasic steps do not execute in 64-bit TestStand.
- Measurement Studio C++ MFC data types —No 64-bit version of Measurement Studio C++ MFC exists.

As a workaround, you can use these features indirectly from 64-bit TestStand by remotely
 executing a sequence using 32-bit TestStand. However, because this technique
 increases overhead and forfeits the benefits the 64-bit architecture offers, NI
 recommends using this technique only as a temporary solution or in situations in
 which these features perform only a limited role in the test system. If these
 features are a major or critical part of the test system, NI recommends using 32-bit
 TestStand.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- Remote Execution in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=features-common-to-all-teststand-process-mode.html language=enus -->
## TOPIC 00402: Features Common to All TestStand Process Models

- bundle_id: `teststand`
- source_path: `features-common-to-all-teststand-process-mode.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/features-common-to-all-teststand-process-mode.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: All TestStand process models identify UUTs and display UUT status information. Process models also call process model plug-ins that generate reports and log results to databases or files. You can use client sequence files to customize various process model operations by overriding model-defined call

### Features Common to All TestStand Process Models

All TestStand process models identify UUTs and display UUT status information. Process models also call process model plug-ins that generate reports and log results to databases or files.

You can use client sequence files to customize various process model operations by overriding model-defined callback sequences. You can also create or modify process model plug-ins to add or modify functionality.

Process models provide Configuration and Execution entry points for configuring model settings and running client files under the model. Each entry point is a sequence in the process model file. The Configure and Execute menus of an application typically include the model entry points.

Parent topic:

Process Model Architecture

Related concepts:

- Process Model Plug-In Architecture
- Database Logging
- Callback Sequences
- Creating Process Model Plug-ins
- Configuration Entry Points
- Engine Callback

<!--NI_TOPIC bundle=teststand path=filtering-and-excluding-files.html language=enus -->
## TOPIC 00403: Filtering and Excluding Files

- bundle_id: `teststand`
- source_path: `filtering-and-excluding-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/filtering-and-excluding-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can and dependencies that you do not want to include in a deployment in the following ways: Filter files that you want to enable or disable when you create the deployment with the deployment utility. TestStand adds filtered files to the list of distributed files but does not include the files in

### Filtering and Excluding Files

You can and dependencies that you do not want to include in a deployment in the following ways:

- Filter files that you want to enable or disable when you create the deployment with the deployment utility. TestStand adds filtered files to the list of distributed files but does not include the files in the deployment by default. You must manually include the files.
- Exclude files that you are sure you never want to include in a deployment. TestStand does not add excluded files to the list of distributed files, even if the files are dependencies of included files.

For example, do not include a Microsoft Windows system DLL a TestStand step calls because deploying a Windows system DLL from a development computer that runs Windows 10/8.1/7 to a test station computer that runs Windows XP might result in operating system incompatibility issues. Do not include TestStand files the TestStand Runtime installs, such as DLLs from the <TestStand>\Bin directory. Install the TestStand Runtime rather than individual TestStand files to ensure you install all necessary dependencies. Do not include Microsoft Visual Studio and LabWindows/CVI files. Install these files with the corresponding run-time engine.

#### Filtered Files

Use file filtering based on directories and file extensions to remove dependencies you are not likely to need in the deployment. For example, the deployment utility filters executables from the Windows directory because those files most likely are part of the operating system on the test station computer.

The Distributed Files list on the Distributed Files tab of the deployment utility displays filtered files but does not enable the files to include in the deployment. You must manually enable filtered files to include them in the deployment. By default, the deployment utility filters the following types of files as dependencies:

- Files in the <TestStand>\Bin , <TestStand>\Components , or <TestStand>\CodeTemplates subdirectories
- Files in the <TestStand Public>\Components\Tools\DeploymentUtility directory
- Files with a .exe or .dll extension in the Windows or Windows\System32 directories

Note

#### Excluded Files

Use
 exclusions to specify directories where dependent EXEs and DLLs should not be
 included in the deployment. For example, NI excludes DLLs that might cause
 incompatibility issues if you include them in a deployment. Exclusions apply to code
 modules specified by a step and the dependencies of those code modules. The
 Distributed Files list on the Distributed Files tab of the deployment utility does
 not display excluded files to prevent you from accidentally including the files in a
 deployment. To include an excluded file in a deployment, you must manually add a
 reference to the excluded file in the TestStand workspace.

Note

- Use caution when you include excluded files in a deployment to prevent
 incompatibility issues on the test station computer.
- Exclusions do not apply to dependencies of LabVIEW files, including VI code
 modules, subVIs, or DLL dependencies of LabVIEW code modules.

#### Editing the Filter.ini
 File

You can edit the Filter.ini file located in the
 <TestStand Application Data>\Cfg directory to prevent
 including unwanted files in a deployment and to customize the files the deployment
 utility filters and excludes from deployments. NI recommends that you use the
 default values in the Filter.ini file and that you do not remove
 items from the file but instead add custom exclusions or filters.

Each of the
 following sections in the Filter.ini file contains filters, which
 are regular expressions that use the Match Pattern Function VI syntax.

| Section | Syntax | Description |
| --- | --- | --- |
| [Version] | Version="Number" | Version number of the Filter.ini file. The deployment utility only uses Filter.ini files with a later version number than the default file version number. If the version number is earlier than the deployment utility expects, the deployment utility overwrites the file with the default Filter.ini file. Increment the version number of the Filter.ini file when you want to move a Filter.ini file from a previous version of TestStand. |
| [Exclude_Company_Product] | COMPANY_#="Name of company" PRODUCT_#="Name of product" | Excludes executables or DLLs with company and product name properties that match the regular expressions, which can contain wild card characters to match multiple products. For example, "Microsoft.?.?.?.?.?.?.?Windows" matches "Microsoft Windows" and "Microsoft Windows NT". |
| [Excluded_Filenames] | FILE_#="Name of the file to filter, including file extension" | Excludes DLLs with the names you specify. Use this exclusion for DLLs that do not have company or product information or when you want to use some but not all DLLs from a product. |
| [Excluded_Dirs] | DIR_#="Name of directory" | Excludes all EXE and DLL dependencies in the directory you specify. |
| [Windows] | FILTER_#="Regular expression" | Filters any file that matches the regular expression in the Windows directory. |
| [System32] | FILTER_#="Regular expression" | Filters any file that matches the regular expression in the Windows\\System32 directory. |
| [TestStand] | FILTER_#="Regular expression" | Filters any file that matches the regular expression in the <TestStand> directory. |
| [TestStandPublic] | FILTER_#="Regular expression" | Filters any file that matches the regular expression in the <TestStand Public> directory. |

#### Filtering Examples

Use the
 [Exclude_Company_Products],
 [Excluded_Filenames], and [Excluded_Dirs]
 sections to exclude DLLs by company name, product name, filename, or directory
 location. The Filter.ini file uses the company name or product name
 of a DLL because some applications, such as Microsoft Office, can install to any
 directory. The Filter.ini file uses filenames of DLLs because some
 DLLs do not define company or product names.

The following table includes
 examples to help you define a filter.

| Use Case | Section | Syntax | Example Scenario | Example Filter | More Information |
| --- | --- | --- | --- | --- | --- |
| Exclude components from a product of a certain company | [Exclude_Company_Product] | COMPANY_#="Name of company" PRODUCT_#="Name of product" | Exclude all TestStand and LabWindows/CVI files | [Exclude_Company_Products] COMPANY_0="National Instruments" PRODUCT_0="TestStand" COMPANY_1="National Instruments" PRODUCT_1="LabWindows.CVI" | During deployment, the deployment utility checks the version information strings for company and product names for all included files and excludes the matching files. |
| Exclude all files that have a certain filename | [Excluded_Filenames] | FILE_#="Name of the file to filter, including file extension" | Exclude all files named readme.txt or image.jpg | [Excluded_Filenames] FILE_0="readme.txt" FILE_1="image.jpg" | The [Excluded_Filenames] section does not support regular expressions. |
| Exclude all files from a certain directory | [Excluded_Dirs] | DIR_#="Name of directory" | Exclude all files from the Program Files directory and files from the Windows public directory | [Excluded_Dirs] DIR_0="Program Files" DIR_1="Program Files (x86)" DIR_2="Users\\Public" | You do not have to specify a full directory path. The filter excludes any directory with a name that matches the specified regular expression. |
| You can also use the predefined [Windows], [System32], [TestStand], and [TestStandPublic] sections to exclude files from those directories and their subdirectories. You can also create a custom section with a name that is the absolute path of a directory to exclude files from the directory. Enter a regular expression for the filter to specify the files you want to exclude. | FILTER_#="Regular expression" | Exclude all executable files from the Windows and Windows\\System32 directories and their subdirectories | [Windows] FILTER_0=".*exe" [System32] FILTER_0=".*exe" |  |  |
| Exclude all files from the <TestStand>\\Bin directory | [TestStand] FILTER_0="BIN\\.*" |  |  |  |  |
| Exclude all .txt and .jpg files from the C:\\Users directory and its subdirectories | [C:\\Users] FILTER_0=".*txt" FILTER_1=".*jpg" |  |  |  |  |

Parent topic:

Creating Deployments

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=finding-a-property-path.html language=enus -->
## TOPIC 00404: Finding a Property Path

- bundle_id: `teststand`
- source_path: `finding-a-property-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/finding-a-property-path.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because the existence or content of some properties might vary at run time, you can browse the sequence context during the execution of the sequence to locate a specific property path. Complete the following steps to locate a property path. Set a breakpoint on the step in which you intend to use the

### Finding a Property Path

Because the existence or content of some properties might vary at run time, you can browse the sequence context during the execution of the sequence to locate a specific property path.

Complete the following steps to locate a property path.

1. Set a breakpoint on the step in which you intend to use the property path and then execute the sequence.
2. When TestStand reaches the breakpoint, click the Variables pane in the Execution window and browse to the property.
3. To copy the path to the property to the system clipboard, select Copy from the context menu of the property. You can then paste the path into a text field in TestStand, such as an expression, or into the source code for a code module. If you paste into the Variables pane, TestStand inserts a copy of the object.

When searching for a property path, you must consider the method by which you execute the sequence. For example, one common property path is that of the unit under test (UUT) serial number. The local variable that contains the serial number exists within the Test UUTs Execution entry point sequence of the process model. You can only browse to this property while executing the sequence using the Test UUTs Execution entry point. The property path of the UUT serial number is RunState.Root.Locals.UUT.SerialNumber. In this case, the RunState.Root property contains the sequence context of the Test UUTs Execution entry point.

Parent topic:

Property Paths

Related concepts:

- Sequence Context

<!--NI_TOPIC bundle=teststand path=flags-enumerations-and-bitwise-or-semantics.html language=enus -->
## TOPIC 00405: Flags Enumerations and Bitwise OR Semantics

- bundle_id: `teststand`
- source_path: `flags-enumerations-and-bitwise-or-semantics.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/flags-enumerations-and-bitwise-or-semantics.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand enumerations may be designated as "flags." This is conceptually similar to adding the [Flags] attribute to an enumeration in .NET, although the functionality is different. In TestStand, flags enumerations support bitwise semantics to specify combinations of enumerators. Non-flags enumerati

### Flags Enumerations and Bitwise OR Semantics

TestStand enumerations may be designated as "flags." This is conceptually similar to adding the [Flags] attribute to an enumeration in .NET, although the functionality is different. In TestStand, flags enumerations support bitwise semantics to specify combinations of enumerators. Non-flags enumerations do not support these semantics. Use the Edit Enumerators dialog box to specify that an enumeration data type is a flags enumeration.

Parent topic:

Getting Started Creating a TestStand Enumeration

<!--NI_TOPIC bundle=teststand path=flow-control-step-types.html language=enus -->
## TOPIC 00406: Flow Control Step Types

- bundle_id: `teststand`
- source_path: `flow-control-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/flow-control-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates using the Flow Control step types to control sequence flow. These step types include If, Else If, Else, For, For Each, While, Do While, Select, Case, Break, Continue, and End. Example File Location <TestStand Public>\Examples\Built-In Step Types\Flow Control Step Ty

### Flow Control Step Types

#### Purpose

This example demonstrates using the Flow Control step types to control sequence flow. These step types include If, Else If, Else, For, For Each, While, Do While, Select, Case, Break, Continue, and End.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Flow Control Step Types\Flow
 Control Step Types.seq

#### Highlighted Features

Flow Control step types

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

The example sequence file demonstrates several methods for controlling sequence flow.

#### If, Else If, and End

The Prompt for option for If/ElseIf/Else step prompts you to click one of three buttons, and each launches its own message popup that indicates the button you clicked. The If step determines whether you clicked the Option A button. If the step evaluates to True, the sequence executes the steps that immediately follow the If step. If the step evaluates to False, the sequence continues to the first Else step, which in this case is an Else If step.

The Else If step behaves the same as the If step and determines whether you clicked the Option B button. If the step evaluates to True, the sequence continues executing until it encounters another Else step or encounters an End step. If the Else If step evaluates to False, the sequence executes the next Else step or continues to an End step if no additional Else steps exist.

When a sequence encounters an Else step, the sequence always executes all steps that follow the Else step. You can only use one Else step for each If step, but you can use multiple Else If steps.

#### Select and Case

The Prompt for option for Select/Case step prompts you to click one of three buttons, and each launches its own message popup that indicates the button you clicked. The Select step determines which button you clicked. Two or more Case steps always follow a Select step. You can specify multiple values for a single case using an array, such as {"y","yes"}. All the steps contained in a Case block execute, depending on the value the Select step evaluates. The End steps specify the end of a Case block or a Select structure.

#### For

The For step executes a block of steps multiple times. The For Loop edit tab on the Step Settings pane specifies that the For step begins with the Locals.index variable set to 0. The loop continues until the value of the Locals.index variable is greater than or equal to the value you specify. Each time the For step executes, the Locals.index variable increments by 1. Therefore, the Beep at done determined by loop index step in the For block executes the specified number of times and uses the increasing index.

#### For Each

The For Each step behaves like the For step but iterates over every element in an array rather than iterate depending on a specified condition. The Locals.CurrentMembers variable is an array that specifies three elements, so the steps in the For Each block execute three times. The current element that the loop is iterating on is stored in the Locals.CurrentName property. This setting is specified in the ForEach loop tab of the step settings of the For Each step.

#### Do While

The Do While step defines a block of steps that always execute at least once. The DoWhile Loop edit tab on the Step Settings pane specifies an expression that the Do While step evaluates after all the steps in the Do While block execute. If the expression evaluates to True, the steps in the Do While block execute again. If the expression evaluates to False, the sequence continues to the next step.

#### While

The While step defines a block of steps that execute when an expression specified on the While Loop edit tab on the Step Settings pane evaluates to True. If the expression evaluates to False, the sequence continues to the next step. The While loop differs from the Do While loop because the While loop evaluates its expression before each iteration and not after each iteration. Therefore, the steps in the While block might never execute.

#### Break and Continue

The Break step terminates a For, For Each, While, or Do While loop or a Case block. When a
 sequence encounters a Break step, the sequence exits the block and continues to the next
 step.

The Continue step terminates the current iteration of a For, For Each, While, or Do While
 loop and prompts the sequence to begin the next iteration of the loop.

In addition to Flow Control step types, you can also use preconditions or post actions step
 properties to control sequence flow.

An advantage of using step properties is that the sequence can use fewer steps. In
 addition, the flow control logic is attached to the step. For example, if you specify a
 precondition of Locals.PowerSupplyOn == True for a step, the precondition
 remains attached to the step even if you move or copy the step to a new location. A
 disadvantage is that the sequence flow logic is not immediately visible when viewing the
 sequence. You can make flow control more visible by using preconditions on separate Goto
 steps and using Label steps as branch targets. However, the functionality you create in this
 way, such as loops or conditionally-executed blocks of steps, is embedded in the
 precondition expressions and branch targets, and requires anyone who reads the sequence to
 review the preconditions and branch targets to understand the flow control.

An advantage of using separate Flow Control steps is that the flow control logic is visible
 in the sequence it is expressed in separate steps that identify the flow control operations
 the steps perform. In addition, applications typically display the flow control structures
 you create with Flow Control steps with indentation and grouping bars that improve the
 readability of the sequence. Furthermore, because Flow Control steps operate on blocks of
 steps demarcated with separate End steps, you do not need to specify specific steps as
 branch destinations, so you can more easily edit and rearrange steps because you do not need
 to update branch destinations. You can use step properties, separate Flow Control steps, or
 both, depending on which functionality best suites the requirements of an application.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=format-strings-for-database-date-values.html language=enus -->
## TOPIC 00407: Format Strings for Database Date Values

- bundle_id: `teststand`
- source_path: `format-strings-for-database-date-values.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/format-strings-for-database-date-values.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Format control on the Column/Parameters section of the Database Options dialog box and the Format String control on the Column/Parameter Values section of the Edit Data Operation dialog box support the following format strings when reading date values from a database and writing date values to a

### Format Strings for Database Date Values

The Format control on the Column/Parameters section of the Database Options dialog box and the Format String control on the Column/Parameter Values section of the Edit Data Operation dialog box support the following format strings when reading date values from a database and writing date values to a database. A format string consists of symbols that describe how to convert a date value read from a database to a string value, or how to interpret a string value when writing a date value to a database.

| Format String | Value | Formatted Value |
| --- | --- | --- |
| mm/dd/yy | Oct 20, 2010 | 10/20/10 |
| dd.mm.yy | Oct 20, 2010 | 20.10.10 |
| 'Jane Doe, born' Mmmm d, yyyy | Oct 20, 2010 | Jane Doe, born October 20, 2010 |
| hh:mm:ss | 3:47:42 PM | 15:47:42 |
| hh:mm:ss AM/PM | 3:47:42 PM | 03:47:42 PM |

| Symbol | Description | Example Output |
| --- | --- | --- |
| m | Month as number without leading zero. | 12, 5 |
| mm | Month as number with leading zero when applicable. | 12, 05 |
| mmm | Month as three-letter abbreviation, lowercase. | mar |
| Mmm | Month as three-letter abbreviation, initial cap. | Mar |
| MMM | Month as three-letter abbreviation, uppercase. | MAR |
| mmmm | Month as full name, lowercase. | march |
| Mmmm | Month as full name, initial cap. | March |
| MMMM | Month as full name, uppercase. | MARCH |
| d | Day of the month as number without leading zero. | 25, 5 |
| dd | Day of the month as number with leading zero when applicable. | 25, 05 |
| ddd | Day of the month as three-letter abbreviation, lowercase. | tue |
| Ddd | Day of the month as three-letter abbreviation, initial cap. | Tue |
| DDD | Day of the month as three-letter abbreviation, uppercase. | TUE |
| dddd | Day of the month as full name, lowercase. | tuesday |
| Dddd | Day of the month as full name, initial cap. | Tuesday |
| DDDD | Day of the month as full name, uppercase. | TUESDAY |
| yy | Last two digits of year. | 08 |
| yyyy | Four-digit year. | 2010 |
| h | Hour of the day, without leading zero (use am/pm symbol for 12-hour style). | 12, 5 |
| hh | Hour of the day, with leading zero (use am/pm symbol for 12-hour style). | 12, 05 |
| i (or m) | Minute of the hour, without leading zero. | 57, 5 |
| ii (or mm) | Minute of the hour, with leading zero. | 57, 05 |
| s | Second of the minute, without leading zero. | 57, 5 |
| ss | Second of the minute, with leading zero. | 57, 05 |
| ss.ssssss | Second of the minute with fractional seconds (up to six ‘s’ symbols after the decimal point). | 57.123456 |
| am/pm | "am" or "pm" string, lowercase (forces 12-hour clock). | am |
| AM/PM | "AM" or "PM" string, uppercase (forces 12-hour clock). | AM |
| a/p | "a" or "p" string (forces 12-hour clock). | a |
| A/P | "A" or "P" string, uppercase (forces 12-hour clock). | A |
| / - . : , <space> | Output the character. | — |
| \\<character> | Output the character following the ‘\\’ character. | \\U\\T\\C is UTC |
| "<string>" '<string>' | Output the string. | "UTC" is UTC |
| GD | General format for dates is the Short Date Format in the Regional Options section of the Microsoft Windows Control Panel. Note Do not combine other format symbols with GD except [US]. | — |
| GDT | General format for dates with times. The Time Format control in the Regional Options section of the Windows Control Panel is appended to the Short Date Style. This is the default when no format string is given. Note Do not combine other format symbols with GDT except [US]. | — |
| GL | General long format for dates. The Long Date Style control in the Regional Options section of the Windows Control Panel. Note Do not combine other format symbols with GL except [US]. | — |
| GLT | General long format for dates with times. The Time Style control in the Regional Options section of the Windows Control Panel is appended to the Long Date Format. Note Do not combine other format symbols with GLT except [US]. | — |
| GT | General format for time. The Time Style control in the Regional Options section of the Windows Control Panel. Note Do not combine other format symbols with GT except [US]. | — |
| [US] | Combine with GD, GDT, GL, GLT, or GT to override the Regional Options section of the Windows Control Panel and use the United States defaults instead. | — |

Parent topic:

TestStand Database Fundamentals

<!--NI_TOPIC bundle=teststand path=fundamentals.html language=enus -->
## TOPIC 00408: Fundamentals

- bundle_id: `teststand`
- source_path: `fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/fundamentals.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about TestStand concepts, including creating and debugging sequences, logging data, extending TestStand functionality, and integrating TestStand with other application development environments, such as LabVIEW and LabWindows/CVI. If you are a new user, NI recommends that you complete the tutor

### Fundamentals

Learn about TestStand concepts, including creating and debugging sequences, logging data,
 extending TestStand functionality, and integrating TestStand with other application
 development environments, such as LabVIEW and LabWindows/CVI.

If you are a new user, NI recommends that you complete the tutorials in *Getting Started
 with TestStand* to familiarize yourself with TestStand concepts and
 features.

Related concepts:

- Database Logging
- Extending TestStand
- Effectively Using LabVIEW with TestStand
- Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=general-environment-limitations.html language=enus -->
## TOPIC 00409: General Environment Limitations

- bundle_id: `teststand`
- source_path: `general-environment-limitations.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/general-environment-limitations.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using TestStand environments can present limitations in the following scenarios: Multibyte Strings—If the global environment has multibyte strings enabled, then all environments must have multibyte strings enabled. This is mainly because all environments share the Users.ini file of the global enviro

### General Environment Limitations

Using TestStand environments can present limitations in the following scenarios:

- Multibyte Strings —If the global environment has multibyte
 strings enabled, then all environments must have multibyte strings enabled. This
 is mainly because all environments share the Users.ini file of
 the global environment.
- User Management —Environments do not support loading an
 alternate set of users and passwords that differ from the global environment. All
 environments use the Users.ini file defined in the global
 environment, which defaults to <TestStandApplication
 Data>\Cfg\Users.ini .Nevertheless, certain forms of privilege
 escalation can be accomplished by creating custom configuration folders. For
 example, a user who cannot normally configure the engine can effectively do so
 within the context of an environment they create. To accomplish this,the user
 can create an environment with a custom CommonAppData directory and
 prepopulate the directory with configuration files.
- Disable Environments Feature —You can completely disable
 the environments feature by defining the following registry key:Path:
 HKEY_LOCAL_MACHINE\SOFTWARE\National
 Instruments\TestStand\ , or 64-Bit
 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\National
 Instruments\TestStand\ Name:
 DisableTestStandEnvironments Type:
 DWord Value: 0x1 An error will
 occur if you enable this registry key and launch a TestStand application that
 attempts to use an environment other than the global environment. This setting
 applies to all installed versions and bitnesses of TestStand.
- Remote Engine —The TestStand remote engine does not
 support environments. The remote engine always runs in the global
 environment.
- Simultaneous Execution —Although it is possible to run two
 or more instances of the TestStand engine simultaneously in different
 environments, the instances are not completely isolated from each other. Certain
 features of TestStand are shared at runtime, and could conflict. For example:
  - Out-of-process synchronization objects are global to the system and not
 scoped by environments. (In-process synchronization objects are private
 to the process and therefore cannot conflict across environments.)
  - Out-of-process execution for LabVIEW and CVI Adapter steps will
 generally occur within a single shared instance of the external LabVIEW
 or CVI ADE. (In-process execution remains private to the process, so it
 cannot conflict.)
  - 64-bit TestStand applications configured to use the 32-bit NI Switch
 Executive (NISE) share a single instance of the out-of-process NISE.
 64-bit TestStand applications configured to run NISE in-process will not
 conflict. 32-bit TestStand applications always run NISE in-process, and
 therefore cannot conflict.
  - When debugging, stepping into a code module from an adapter step can use
 an existing instance of the external ADE already in use by a TestStand
 application running in a different environment.

Parent topic:

TestStand Environments

<!--NI_TOPIC bundle=teststand path=general-strategies-for-optimizing-labview-cod.html language=enus -->
## TOPIC 00410: General Strategies for Optimizing LabVIEW Code Module Performance on SMP Systems

- bundle_id: `teststand`
- source_path: `general-strategies-for-optimizing-labview-cod.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/general-strategies-for-optimizing-labview-cod.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand-based test systems can have many different kinds of VIs. For the purpose of evaluating the performance of VIs on symmetric multiprocessing (SMP) systems, it is helpful to categorize VIs in the following ways: VIs that have singular linear data flow—Executing these VIs with multiple threads

### General Strategies for Optimizing LabVIEW Code Module Performance on SMP Systems

TestStand-based test systems can have many different kinds of VIs. For the purpose of evaluating the performance of VIs on symmetric multiprocessing (SMP) systems, it is helpful to categorize VIs in the following ways:

- VIs that have singular linear data flow —Executing these VIs with multiple threads provides no performance benefit.
- VIs that have complex data flows —Executing these VIs with multiple threads can provide better performance than a single thread because different data flow branches can execute concurrently on different CPUs.

Use the following recommended LabVIEW Adapter settings to achieve optimal LabVIEW code module performance, depending on the LabVIEW data flow complexity of the majority of the VIs on the test system and the amount of tuning you intend to complete:

- If most of the VIs in the test system have singular linear data flow, NI recommends that you
 disable the Execute ‘Same as caller’ VIs Using Multiple Threads option in the
 LabVIEW Adapter Configuration dialog box to avoid time spent in the LabVIEW
 Adapter creating superfluous threads.
- If most of the VIs in the test system have complex data flow or if the distribution of simple
 and complex data flow VIs in the test system is even, NI recommends that you
 enable the Execute ‘Same as caller’ VIs Using Multiple Threads option. Depending
 on the complexity of the VIs, you can obtain even better performance by using
 the Number of Threads option in the LabVIEW Adapter Configuration dialog box to
 modify the number of LabVIEW execution threads TestStand configures the LabVIEW
 RTE to use to execute VIs. Furthermore, if you have manually tuned the CPU
 affinity of TestStand execution threads, NI recommends that you run performance
 tests to determine whether enabling the Additional Threads Inherit Calling
 Thread’s CPU Affinity option in the LabVIEW Adapter Configuration dialog box
 improves or degrades performance.
- Regardless of the distribution of simple and complex data flow VIs in the test system, you can fine-tune the SMP performance of the system by completing the following steps.
  1. Disable the Execute ‘Same as caller’ VIs Using Multiple Threads option.
  2. Run performance tests to identify specific VIs that perform better when executing using multiple threads.
  3. Set the Preferred Execution System option on the Execution page of the VI Properties dialog box in LabVIEW for the VIs you identify to something other than same as caller or user interface .
- Fine-tuning performance might also require that you configure the default number of threads available in a LabVIEW execution system.

Parent topic:

Symmetric Multiprocessing in VIs Executed from TestStand

Related concepts:

- Symmetric Multiprocessing in VIs Executed from TestStand
- Programming with the TestStand API in LabVIEW
- Using TestStand on SMP Systems
- Configuring the Number of Execution Threads Assigned to a LabVIEW Execution System

<!--NI_TOPIC bundle=teststand path=general-test-executive-concepts.html language=enus -->
## TOPIC 00411: General Test Executive Concepts

- bundle_id: `teststand`
- source_path: `general-test-executive-concepts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/general-test-executive-concepts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A test executive organizes and executes sequences of reusable code modules you can create in a variety of programming environments. The following concepts are applicable to test executives in general: Code module—A program module, such as a Microsoft Windows DLL or LabVIEW VI (.vi), that contains on

### General Test Executive Concepts

A test executive organizes and executes sequences of reusable code modules you can create in a variety of programming environments.

The following concepts are applicable to test executives in general:

- Code module —A program module, such as a Microsoft Windows DLL or LabVIEW VI ( .vi ), that contains one or more functions that perform a specific test or other action.
- Step —An individual element of a test sequence that can call code modules or perform other operations.
- Sequence —A series of steps you specify to execute in a particular order. Whether and when a step executes depends on the results of previous steps.
- Subsequence —A sequence another sequence calls as a step.
- Sequence file —A file that contains the definition of one or more sequences.
- Sequence editor —A program that provides a graphical user interface (GUI) for creating, editing, executing, and debugging sequences.
- User interface —A program that provides a GUI for executing sequences on a production station. A sequence editor and user interface can be separate applications or different aspects of the same application.
- Test executive engine —A module or set of modules that provide an API for creating, editing, executing, and debugging sequences. A sequence editor or user interface uses the services of a test executive engine.
- Application Development Environment (ADE) —A programming environment, such as LabVIEW, LabWindows™/CVI™, or Microsoft Visual Studio, in which you create code modules and user interfaces.
- Unit Under Test (UUT) —The device or component to test.
- Deployment —An image or an installer for an image to transfer a test system from development to production.

Parent topic:

Parts of a TestStand Application

<!--NI_TOPIC bundle=teststand path=generating-a-test-report.html language=enus -->
## TOPIC 00412: Generating a Test Report

- bundle_id: `teststand`
- source_path: `generating-a-test-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-a-test-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate a report to process collected test results. Most of the report generation capabilities are not native to the TestStand Engine or to the TestStand Sequence Editor. The default process model, which calls the Main sequence in the client sequence file to test a UUT, relies on the automa

### Generating a Test Report

You can generate a report to process collected test results. Most of the report
 generation capabilities are not native to the TestStand Engine or to the TestStand
 Sequence Editor. The default process model, which calls the Main sequence in the client
 sequence file to test a UUT, relies on the automatic result collection capabilities of
 the TestStand Engine to accumulate the raw data for each report. The engine
 automatically compiles the result of each step into a result list for an entire
 sequence, which contains the result of each step and the result list of each subsequence
 call made.

When you run a sequence using the Test UUTs or Single Pass Execution entry point, the
 default report generation process model plug-in, NI_ReportGenerator.seq, located in the
 <TestStand>\Components\Models\ModelPlugins directory, generates the report by
 traversing the results for the Main sequence in the client sequence file and all the
 subsequences called.

#### Configuring Report Options

Select
 Configure»Result Processing to launch the Result Processing dialog box.
 Place a checkmark in the Enabled column of the Report row to enable the
 default report generation process model plug-in. You can customize or replace any
 portion of the report generator process model plug-in.

Click the [IMAGE alt='image' src='GUID-8F1FF70D-B038-4F57-BF17-252092B11C6B-a5.png'] icon in the Options column
 for the reporting model plug-in to launch the Report Options dialog box, in which
 you can specify options that determine the content and format of the report and the
 names and locations of report files.

#### Viewing and Using Reports

You can use
 reports in the following ways in TestStand:

- The Report pane of the Execution window displays the report for the current
 execution. Usually, the Report pane is empty until execution completes. 
 Alternatively, you can use an external application to view reports. Select
 Configure»External Viewers to launch the Configure External
 Viewers dialog box, in which you can specify the external application
 TestStand launches to display a particular report format. In the Execution
 window, click the Viewer button on the Report pane to view the report
 in the external viewer you specified.
- You can generate reports on-the-fly to progressively log result data
 concurrently with the execution instead of waiting until UUT testing completes.
- You can generate reports in different formats. The default process model
 generates reports in Automatic Test Markup Language (ATML), XML, HTML, or
 ASCII-text formats.
- You can include hyperlinks in supported versions of ATML, XML, and HTML reports.
- You can distribute these types of report files to view on a computer that does
 not have TestStand installed.
- You can create a custom result processing model plug-in, and you can configure
 multiple instances of reporting model plug-ins in the Result Processing dialog
 box, in which case you can use the Active Report control on the Report
 pane toolbar to select which report to view.
- The report generator can generate a PDF report. Refer to Generating PDF Reports.

Note

Parent topic:

Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=generating-and-customizing-teststand-reports.html language=enus -->
## TOPIC 00413: Generating and Customizing TestStand Reports

- bundle_id: `teststand`
- source_path: `generating-and-customizing-teststand-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-and-customizing-teststand-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consult the topics in this section to learn how to generate a report for a test execution and how to customize the content and format of the report. In addition, this section describes how to choose the appropriate report generation strategy for a test system by reviewing how the report generation f

### Generating and Customizing TestStand Reports

Consult the topics in this section to learn how to generate a report for a test
 execution and how to customize the content and format of the report.

In addition, this section describes how to choose the appropriate report generation
 strategy for a test system by reviewing how the report generation features in TestStand can
 help meet requirements and by describing the tradeoffs to consider when designing report
 generation for a test system. Use cases illustrate how common test system characteristics
 and requirements map to specific report generation strategies.

Parent topic:

Fundamentals

Related concepts:

- Choosing the Appropriate Report Generation Strategy

<!--NI_TOPIC bundle=teststand path=generating-and-viewing-the-report-during-test.html language=enus -->
## TOPIC 00414: Generating and Viewing the Report during Test Sequence Execution

- bundle_id: `teststand`
- source_path: `generating-and-viewing-the-report-during-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-and-viewing-the-report-during-test.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some test procedures can require several hours or more to complete because the procedures contain a significant number of tests or contain a small number of tests that take a long time to complete. To help diagnose issues early in such test systems, you can generate and display a partial report whil

### Generating and Viewing the Report during Test Sequence Execution

Some test procedures can require several hours or more to complete because the procedures contain a significant number of tests or contain a small number of tests that take a long time to complete. To help diagnose issues early in such test systems, you can generate and display a partial report while the test sequence executes instead of waiting until the end of execution to generate and display the report.

You can configure TestStand to generate a report on-the-fly to support such test sequences. NI
 benchmarks show that if you want to view the entire report as the testing
 progresses, an on-the-fly ASCII report provides the best throughput. If you do not
 need to see the entire report, all reports generated on-the-fly when you enable the
 Only Display Latest Results option on the Contents tab of
 the Report Options dialog box provide approximately equivalent throughput. Because
 you cannot generate the report associated with raw results until after the execution
 completes, you cannot use the raw results file format to generate and view the
 report during the test sequence execution.

Test sequences that specify a large number of steps generate very large reports. Generating and
 viewing a large report while executing a test sequence can cause significant
 performance issues. Therefore, when you generate reports on-the-fly, NI recommends
 that you enable the Only Display Latest Results option.

#### Recommended Report
 Options

The following table summarizes the recommended options you
 configure in the Report Options dialog box when you optimize for generating and
 viewing the report during test sequence execution:

| Report Option | Value for a Sequence with Few Steps and Long Execution Time | Value for a Sequence with Many Steps |
| --- | --- | --- |
| Format | ASCII, ATML, HTML, XML (best to worst) | ASCII, ATML, HTML, XML (best to worst) |
| Asynchronous | N/A | N/A |
| On-the-Fly Report | True | True |
| Only Display Latest Results | False | True |

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for generating and viewing
 the report during test sequence execution:

- Maximize test system throughput
- Interoperate with other processes and systems
- Support post-failure information recovery
- Generate reports immediately for the current UUT before testing the next
 UUT

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Maximizing Test System Throughput
- Interoperating with Other Processes and Systems
- Supporting Post-Failure Information Recovery
- Generating the Report for the Current UUT before Testing the Next UUT
- Generating Multiple Reports for Each UUT
- Use Case: Generate Different Types of Reports from the Same Data Set
- On-the-Fly Report Generation

<!--NI_TOPIC bundle=teststand path=generating-multiple-reports-for-each-uut.html language=enus -->
## TOPIC 00415: Generating Multiple Reports for Each UUT

- bundle_id: `teststand`
- source_path: `generating-multiple-reports-for-each-uut.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-multiple-reports-for-each-uut.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some test systems might specify a requirement to generate more than one report for each unit under test (UUT). For example, you might want to generate a fast and simple summary ASCII report and a detailed ATML report that can be post-processed by a Manufacturing Execution System (MES). You might als

### Generating Multiple Reports for Each UUT

Some test systems might specify a requirement to generate more than one report for each unit under test (UUT). For example, you might want to generate a fast and simple summary ASCII report and a detailed ATML report that can be post-processed by a Manufacturing Execution System (MES). You might also want to generate a summary report for customers and a detailed report for internal use.

You can configure TestStand to generate multiple reports for each UUT. NI benchmarks show that
 generating a raw results file and processing it offline to generate multiple reports
 yields the maximum throughput on multi-core computers.

#### Recommended Report
 Options

The following table summarizes the recommended options you
 configure in the Report Options dialog box when you optimize for generating multiple
 reports:

| Report Option | Value |
| --- | --- |
| Format | TSR*, ASCII, ATML, XML, HTML (best to worst) |
| Asynchronous | True |
| On-the-Fly Report | False |
| Only Display Latest Results | False |

Note

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for generating multiple
 reports:

- Maximize test system throughput
- Interoperate with other processes and systems
- Generate reports immediately for the current UUT before testing the next
 one
- Generate and view the report during test sequence execution

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Maximizing Test System Throughput
- Interoperating with Other Processes and Systems
- Generating the Report for the Current UUT before Testing the Next UUT
- Generating and Viewing the Report during Test Sequence Execution

<!--NI_TOPIC bundle=teststand path=generating-output-messages.html language=enus -->
## TOPIC 00416: Generating Output Messages

- bundle_id: `teststand`
- source_path: `generating-output-messages.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-output-messages.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to generate output messages using the OutputMessage expression function and the Engine.NewOutputMessage and OutputMessage.Post methods of the TestStand API. The Output pane of the TestStand Sequence Editor displays the messages. Example File Location <TestStand

### Generating Output Messages

#### Purpose

This example demonstrates how to generate output messages using the OutputMessage expression function and the Engine.NewOutputMessage and OutputMessage.Post methods of the TestStand API. The Output pane of the TestStand Sequence Editor displays the messages.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand Debugging Features\Generating Output
 Messages\Generating Output Messages.seq

#### Highlighted Features

- Action step
- ActiveX/COM Adapter
- Sequence Call step
- Statement step

#### Major API

- Engine.NewOutputMessage
- OutputMessage.Post

#### Prerequisites

(LabVIEW) You must have the LabVIEW development system installed and you must configure the LabVIEW Adapter to use the LabVIEW development system.

(LabWindows/CVI)You must have the LabWindows/CVI Run-Time Engine installed and you must configure the LabWindows/CVI Adapter to execute steps in-process. If you want to use the Execute Steps in an External Instance of CVI option, you must have the LabWindows/CVI development environment installed.

#### How to Use This Example

#### LabVIEW Action Step

Open OutputMessageExample.vi, located in the <TestStand Public>\Examples\TestStand Debugging Features\Generating Output Messages directory, and switch to the block diagram, which describes the following functionality for the VI:

- The invoke node labeled IEngine invokes the Engine.NewOutputMessage method.
- Parameters that enter the VI determine the sequence for which the message is intended and the content, category, and severity of the message.
- The subsequent property nodes specify color and icon name.
- The final invoke node invokes the OutputMessage.Post method to display the output message on the Output pane in the sequence editor

#### LabWindows/CVI Action Step

The LabWindows/CVI Action step calls a LabWindows/CVI DLL named GenerateOutputMessages.dll, located in the <TestStand Public>\Examples\TestStand Debugging Features\Generating Output Messages directory.

Select the Generate Output Messages using a CVI Module step and click the LabWindows/CVI Module tab on the Step Settings pane, which describes the following functionality for the LabWindows/CVI step:

- The Module control specifies GenerateOutputMessages.dll .
- The Function control specifies the GenerateOutputMessages function.
- The Parameters table lists the parameters the DLL accepts. The SeqContextCVI parameter accepts the sequence context, and the other parameters handle errors or log information for inclusion in the report.

#### Statement Step

The Statement step is the simplest way to generate output messages. Select the Generate Output Message using a Statement step step and click the Expression edit tab on the Step Settings pane, which describes the following functionality for the Statement step:

- The expression specifies a simple comparison to determine if the RunState.LoopIndex value is a multiple of 10. If true, the modulus 10 operation evaluates to 0, and TestStand calls the OutputMessage function.
- The parameters of the OutputMessage function accept a message and a severity, and specify the font color and icon to display with the message.

#### ActiveX/COM Steps

The final step in the MainSequence is a Sequence Call step that calls the Using ActiveX Adapter steps sequence. Select the Using ActiveX Adapter steps on the Sequences pane to display the steps in the Using ActiveX Adapter steps sequence, which describes the following functionality:

- A For loop contains all the steps in the sequence. The If step specifies that the steps execute during only every tenth iteration through the loop.
- The New Output Message step creates the output message by calling the Engine.NewOutputMessage method. This step also specifies the message text, category, and severity and obtains a reference to the sequence context.
- The Set Text Color step uses the Set Property option on the TextColor property to change the message font color to cyan.
- The Set Icon Name step specifies the icon to display next to the message.
- The Post Output Message step invokes the OutputMessage.Post method to display the output message on the Output pane. Simply creating the message using the Engine.NewOutputMessage method is insufficient.

Parent topic:

Examples for TestStand Debugging Features

Related concepts:

- TestStand Directory Structure
- Sequence Context

<!--NI_TOPIC bundle=teststand path=generating-pdf-reports.html language=enus -->
## TOPIC 00417: Generating PDF Reports

- bundle_id: `teststand`
- source_path: `generating-pdf-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-pdf-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The report generator can generate a PDF version of all report formats except for ASCII text. Navigate to the Report Options dialog box for your report, then select Generate PDF. TestStand generates PDF reports only at the end of execution even if you enable on-the-fly reporting. PDF report generatio

### Generating PDF Reports

The report generator can generate a PDF version of all report formats except for ASCII text.

Navigate to the Report Options dialog box for your report, then select Generate PDF. TestStand generates PDF reports only at the end of execution even if you enable on-the-fly reporting.

Note

- PDF report generation is limited to reports of less than 80 MB. When the report exceeds 80 MB, PDF report generation is skipped and no error is reported.
- For images to appear correctly in PDF reports, use an absolute path when you specify an image location in the Step.Result.ReportText property.

Parent topic:

Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=generating-the-report-for-the-current-uut-bef.html language=enus -->
## TOPIC 00418: Generating the Report for the Current UUT before Testing the Next UUT

- bundle_id: `teststand`
- source_path: `generating-the-report-for-the-current-uut-bef.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-the-report-for-the-current-uut-bef.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: At the end of the test sequence execution, some systems require moving a printout of a report associated with the unit under test (UUT) to the next stage of the manufacturing process along with the UUT. For such reports, raw results generators and asynchronous report generation are not appropriate.

### Generating the Report for the Current UUT before Testing the Next UUT

At the end of the test sequence execution, some systems require moving a printout of a report associated with the unit under test (UUT) to the next stage of the manufacturing process along with the UUT. For such reports, raw results generators and asynchronous report generation are not appropriate. This requirement does not impact other report formats.

You can generate on-the-fly reports to satisfy this requirement because TestStand generates on-the-fly reports synchronously.

#### Recommended Report
 Options

The following table summarizes the recommended options you
 configure in the Report Options dialog box when you optimize for ensuring the report
 for a UUT is generated before the next UUT is tested:

| Report Option | Value |
| --- | --- |
| Format | ASCII, ATML, XML, HTML (best to worst) |
| Asynchronous | False |
| On-the-Fly Report | True |
| Only Display Latest Results | N/A |

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for ensuring the report for a
 UUT is generated before the next UUT is tested:

- Maximize test system throughput
- Generate multiple reports for each UUT
- Generate and view the report during test sequence execution

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Maximizing Test System Throughput
- Generating Multiple Reports for Each UUT
- Generating and Viewing the Report during Test Sequence Execution
- Supporting Post-Failure Information Recovery
- On-the-Fly Report Generation

<!--NI_TOPIC bundle=teststand path=generating-type-library-information-to-includ.html language=enus -->
## TOPIC 00419: Generating Type Library Information to Include in a DLL

- bundle_id: `teststand`
- source_path: `generating-type-library-information-to-includ.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/generating-type-library-information-to-includ.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabWindows/CVI can use the information specified in a function panel file to generate type library information to include in a DLL. Complete the following steps to generate a type library resource from a function panel and add the type library resource to a DLL. Open a new function panel file and cr

### Generating Type Library Information to Include in a DLL

LabWindows/CVI can use the information specified in a function panel file to generate type library information to include in a DLL. Complete the following steps to generate a type library resource from a function panel and add the type library resource to a DLL.

1. Open a new function panel file and create a function panel for each exported function you want to include in the type library.
2. Add the function panel file to the LabWindows/CVI project.
3. In the LabWindows/CVI project window, select Build»Target Settings to launch the Target Settings dialog box.
4. In the Target Settings dialog box, click the Type Library button to launch the Type Library dialog box.
5. In the Type Library dialog box, enable the Add type library resource to DLL option and enter the path to the file in the Function panel file control.
6. Click OK to close the Type Library dialog box and to close the Target Settings dialog box.
7. In the Project window, select Build»Create Debuggable Dynamic Link Library to build the DLL. Click OK when LabWindows/CVI prompts you that the files are created.

LabWindows/CVI imposes certain requirements on the declaration of the DLL API in a type library. Use the following guidelines to ensure that TestStand can use the DLL:

- Use typedefs for structure, union, and enumeration parameters.
- Do not use structures that require forward references or that contain pointers.
- Do not use pointer types except when passing parameters by reference.

Refer to the LabWindows/CVI documentation for more information about adding type libraries to DLLs.

Parent topic:

Adding Type Libraries to LabWindows/CVI DLLs

Related concepts:

- Adding Type Libraries to LabWindows/CVI DLLs
- Specifying String Buffer Size in a Type Library

<!--NI_TOPIC bundle=teststand path=getting-started-creating-a-teststand-enumerat.html language=enus -->
## TOPIC 00420: Getting Started Creating a TestStand Enumeration

- bundle_id: `teststand`
- source_path: `getting-started-creating-a-teststand-enumerat.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/getting-started-creating-a-teststand-enumerat.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`

### Getting Started Creating a TestStand Enumeration

- [Creating an Enumeration Data Type and Defining the Enumerators](creating-an-enumeration-data-type-and-definin.html)
- [Range Checking: Strict and Loose Enumerations](range-checking-strict-and-loose-enumerations.html)
- [Flags Enumerations and Bitwise OR Semantics](flags-enumerations-and-bitwise-or-semantics.html)
- [Creating an Enumeration Instance](creating-an-enumeration-instance.html)

Parent topic:

Using Enumerations in TestStand

<!--NI_TOPIC bundle=teststand path=getting-started-with-teststand.html language=enus -->
## TOPIC 00421: Getting Started with TestStand

- bundle_id: `teststand`
- source_path: `getting-started-with-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/getting-started-with-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are using TestStand for the first time, NI recommends that you complete the tutorials in this manual. These tutorials begin with a general introduction to the TestStand Sequence Editor and continue by teaching you how to build sequences, manage test data, and customize TestStand functionality

### Getting Started with TestStand

If you are using TestStand for the first time, NI recommends that you complete the tutorials in this manual. These tutorials begin with a general introduction to the TestStand Sequence Editor and continue by teaching you how to build sequences, manage test data, and customize TestStand functionality. Because the steps of the tutorials depend on elements from previous tutorials, NI recommends that you follow the chapter outline in order. Completed solution files are located in the <TestStand Public>\Tutorial\Solution directory.

Note

<TestStand Public>

C:\Users\Public\Documents\National Instruments\TestStand

1. Introduction to TestStand
2. Loading and Running Sequences
3. Editing Steps in a Sequence
4. Debugging Sequences
5. Using Variables and Properties
6. Using Callback Sequences
7. Adding Users and Setting Privileges
8. Interactive Executions
9. Calling Sequences Dynamically
10. Customizing Reports
11. Calling LabVIEW VIs
12. Calling LabWindows/CVI Code Modules

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=teststand path=getting-started-with-user-interface-developme.html language=enus -->
## TOPIC 00422: Getting Started with User Interface Development

- bundle_id: `teststand`
- source_path: `getting-started-with-user-interface-developme.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/getting-started-with-user-interface-developme.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand provides manager controls and visible controls that work together to simplify programming a custom user interface.

### Getting Started with User Interface Development

TestStand provides manager controls and visible controls that work together to simplify programming a custom user interface.

Parent topic:

Creating Custom User Interfaces

Related concepts:

- Manager Controls
- Visible Controls
- Creating Custom User Interfaces

<!--NI_TOPIC bundle=teststand path=handling-events-in-a-labview-user-interface.html language=enus -->
## TOPIC 00423: Handling Events in a LabVIEW User Interface

- bundle_id: `teststand`
- source_path: `handling-events-in-a-labview-user-interface.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-events-in-a-labview-user-interface.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To handle an event in LabVIEW, you register a callback VI, which LabVIEW automatically calls when the control generates the event. Complete the following steps to use the Register Event Callback function, available in the LabVIEW Full or Professional Development System. Wire the reference of the con

### Handling Events in a LabVIEW User Interface

To handle an event in LabVIEW, you register a callback VI, which LabVIEW automatically calls when the control generates the event.

Complete the following steps to use the Register Event Callback function, available in the LabVIEW Full or Professional Development System.

1. Wire the reference of the control that sends the event you want to handle to the Event input of the Register Event Callback function.
2. Use the Event input terminal drop-down list to select the specific event you want to handle.
3. When you want to pass custom data to the callback VI, wire the custom data to the User Parameter input of the Register Event Callback function. The User Parameter input can be any data type.
4. Right-click the VI Ref input of the Register Event Callback function and select Create Callback VI from the context menu. LabVIEW creates an empty callback VI with the correct input parameters for the particular event, including an input parameter for any custom data you wired to the User Parameter input in step 3.
5. Save the new callback VI. The block diagram that contains the Register Event Callback function now shows a Static VI Reference node wired to the VI Ref input of the function. This node returns a strictly typed reference to the new callback VI.
6. Complete the block diagram of the callback VI to perform the operation you specify when the control generates the event.
7. When the application finishes handling events for the control, use the Unregister for Events function to close the event callback refnum output of the Register Event Callback function.

The following figure shows how to register a callback VI to handle the Break event for the Application Manager control:

[IMAGE alt='image' src='GUID-BC75FB6B-F101-4F78-A3A5-DDB1FF8D746B-a5.png']

You can resize the Register Event Callback function node to show multiple sets of terminals to handle multiple events. Refer to the Simple OI - Configure Event Callbacks and to the Full UI - Configure Event Callbacks example user interface VIs for examples of registering and handling events from the TestStand User Interface (UI) Controls.

#### Optimizing Event Handling Performance

You must limit the tasks you perform in a callback VI to ensure that LabVIEW handles the event in a timely manner to allow the front panel to quickly respond to user input and prevent possible hang conditions. When a callback VI performs ActiveX operations that can process messages or performs TestStand operations that can call back into LabVIEW, the application must perform these operations outside of the callback VI. You can define a user event the callback VI generates to defer these types of operations.

The ReDraw user event in the full example user interface shows how callback VIs can defer operations to perform outside of the callback VI. The example user interface performs the following tasks:

- Calls the Full UI - Create LabVIEW Application Events VI to create the ReDraw user event.
- Callback VIs, such as the Full UI - Resized Event Callback VI, generate the ReDraw user event when the user interface must resize and reposition controls on the front panel.
- The ReDraw User Event case in the main event loop of the Full UI - Top-Level VI sets a global variable while processing the current event to prevent callback VIs from generating new ReDraw events. The ReDraw User Event case calls the Full UI - Disable Panel Updates VI to prevent the front panel from updating, calls the Full UI - ArrangeControls VI to update the position and size of controls on the front panel, and calls the Full UI - Re-enable Panel Updates VI to update the front panel.

Parent topic:

Handling Events

Related concepts:

- Handling Events
- Example User Interfaces
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=handling-events-in-a-labwindows-cvi-user-inte.html language=enus -->
## TOPIC 00424: Handling Events in a LabWindows/CVI User Interface

- bundle_id: `teststand`
- source_path: `handling-events-in-a-labwindows-cvi-user-inte.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-events-in-a-labwindows-cvi-user-inte.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To handle an event in LabWindows/CVI, you register a callback function, which LabWindows/CVI automatically calls when the control generates the event. Use the Event Callback Registration functions in the TestStand User Interface (UI) Controls driver to perform event registration. For example, the fo

### Handling Events in a LabWindows/CVI User Interface

To handle an event in LabWindows/CVI, you register a callback function, which LabWindows/CVI automatically calls when the control generates the event. Use the Event Callback Registration functions in the TestStand User Interface (UI) Controls driver to perform event registration.

For example, the following statement registers a callback function for the OnExitApplication event sent from the Application Manager control:

TSUI__ApplicationMgrEventsRegOnExitApplication (gAppMgrHandle, AppMgr_OnExitApp, NULL, 1, NULL);

```text
HRESULT CVICALLBACK AppMgr_OnExitApp(CAObjHandle caServerObjHandle, void *caCallbackData)
    {
    VBOOL canExitNow;
    if (!TSUI_ApplicationMgrShutdown(gAppMgrHandle, &errorInfo, &canExitNow) && (canExitNow))
        QuitUserInterface(0);
    return S_OK;
    }
```

Parent topic:

Handling Events

Related concepts:

- Handling Events
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=handling-events.html language=enus -->
## TOPIC 00425: Handling Events

- bundle_id: `teststand`
- source_path: `handling-events.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-events.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand User Interface (UI) Controls generate events to notify an application of user input and of application events, such as an execution completing. The visible controls generate user input events, such as KeyDown or MouseDown. The manager controls generate application state events, such as the

### Handling Events

TestStand User Interface (UI) Controls generate events to notify an application of user input and of application events, such as an execution completing. The visible controls generate user input events, such as KeyDown or MouseDown. The manager controls generate application state events, such as the ApplicationMgr.SequenceFileOpened event or the ApplicationMgr.UserChanged event. You can handle events according to the needs of the application, as shown in the following table.

| ADE | Description |
| --- | --- |
| LabVIEW | Register event handler VIs with the Register Event Callback function. |
| LabWindows/CVI | Install ActiveX event callback functions by calling the TSUI_<object class>EventsRegOn<event name> functions in tsui.fp. |
| .NET | Create .NET control event handlers from the form designer. |
| C++ (MFC) | Create ActiveX event handlers from the Message Maps page in the Class Wizard dialog box. |

Parent topic:

Getting Started with User Interface Development

Related concepts:

- TestStand UI Controls
- Visible Controls
- Manager Controls
- Handling Events in a LabVIEW User Interface
- Handling Events in a LabWindows/CVI User Interface

<!--NI_TOPIC bundle=teststand path=handling-large-amounts-of-data.html language=enus -->
## TOPIC 00426: Handling Large Amounts of Data

- bundle_id: `teststand`
- source_path: `handling-large-amounts-of-data.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-large-amounts-of-data.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a test generates large amounts of data, TestStand might appear to hang while processing the data and generating the report. Use one of the following approaches to handle large amounts of data in your reports. Avoid putting large amounts of data directly in the report. Instead, store the data in

### Handling Large Amounts of Data

When a test generates large amounts of data, TestStand might appear to hang while processing the data and generating the report. Use one of the following approaches to handle large amounts of data in your reports.

- Avoid putting large amounts of data directly in the report. Instead, store the data in a large data file, such as TDMS, and provide a link to the file in the report.
- If you want to add a large amount of data to a report without referencing an external file, use
 a TSR plugin to generate a TSR file when testing. On a different machine or
 after testing, use the TSR file to generate reports. Note The TSR format
 generates a compact raw results file and, if used, requires the TestStand
 Offline Results Processing Utility to generate the final report.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- Including Hyperlinks in Reports

<!--NI_TOPIC bundle=teststand path=handling-python-code-execution-when-importing.html language=enus -->
## TOPIC 00427: Handling Python Code Execution when Importing Modules

- bundle_id: `teststand`
- source_path: `handling-python-code-execution-when-importing.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-python-code-execution-when-importing.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Include conditional code in your Python modules to handle cases where a module can function as the top-level environment or an imported module. Python is designed in such a way that when the top-level Python module imports a second Python module, the interpreter evaluates and executes the statements

### Handling Python Code Execution when Importing Modules

Include conditional code in your Python modules to handle cases where a module can function as the top-level environment or an imported module.

Python is designed in such a way that when the top-level Python module imports a second Python module, the interpreter evaluates and executes the statements in the second module. With the Python Adapter in TestStand, the interpreter treats TestStand as the top-level environment. TestStand imports the specified module at certain events to determine if the module is valid or not, and to determine the contents of the module. Therefore, any Python module you specify in a Python Adapter step will run when TestStand loads the module, even when the sequence is not executing.

To prevent the interpreter from executing Python code when it imports a module, encapsulate Python module code within the following statement:

```text
if __name__ == "__main__":
```

When a Python module runs directly as the top-level script, the interpreter sets the variable __name__ to __main__. For imported modules, the interpreter sets the variable __name__ to the name of the module. Encapsulating executable code within the conditional statement ensures that the interpreter will check whether the module code is running in the __main__ environment, and if not, the code will not execute on import.

Refer to Python documentation for more information about using the __name__ variable.

Parent topic:

Python Adapter

Related information:

- Module Tab - Edit Python Call Dialog Box
- Python Parameter Passing Tab - Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand path=handling-specific-user-interface-messages.html language=enus -->
## TOPIC 00428: Handling Specific User Interface Messages

- bundle_id: `teststand`
- source_path: `handling-specific-user-interface-messages.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-specific-user-interface-messages.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The first thing to do when you receive a user interface message is to check its UIMessage.Event property, the value of which is a UIMessageCode. Use the UIMessageCode to determine which items, if any, to update on the user interface.

### Handling Specific User Interface Messages

The first thing to do when you receive a user interface message is to check its UIMessage.Event property, the value of which is a UIMessageCode. Use the UIMessageCode to determine which items, if any, to update on the user interface.

Parent topic:

User Interface Messages (UIMessages)

<!--NI_TOPIC bundle=teststand path=handling-ui-messages-labview.html language=enus -->
## TOPIC 00429: Handling UI Messages - LabVIEW

- bundle_id: `teststand`
- source_path: `handling-ui-messages-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-ui-messages-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how you can use custom UI messages to communicate between the client sequence file and the user interface. Sending data from the sequence to the UI—The Sequence posts UI messages containing a status string. The UI message handler reads the string and updates a UI control w

### Handling UI Messages - LabVIEW

#### Purpose

This example shows how you can use custom UI messages to communicate between the client sequence file and the user interface.

- Sending data from the sequence to the UI —The Sequence posts UI messages containing a status string. The UI message handler reads the string and updates a UI control with the data.
- Sending data from the UI to the sequence —Before executing, the sequence posts a message requesting the state of the "show dialogs" UI setting. The UI message handler sets the Locals.ShowDialogs sequence property using the TestStand API, based on the value specified in the UI.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Handling UI
 Messages\LabVIEW\Using Custom UI Messages.lvproj

#### Highlighted Features

- User Interface Messages
- TestStand User Interface controls

#### Major API

Thread.PostUIMessageEx

#### Prerequisites

You must have the LabVIEW Development System installed to view this example.

#### How to Use This Example

Complete the following steps to run the example:

1. In Using Custom UI Messages.lvproj , open Basic User Interface with UI Message Handler.vi.
2. Click the Run button on the VI to start the user interface. The UI Message example sequence is opened by the UI automatically.
3. Run the sequence. Notice that the sequence status is updated as each UI message is posted with ID 10100.
4. After the execution completes, uncheck the Show Sequence Dialogs option on the user interface. Run the sequence again and notice that the message dialogs no longer appear. The dialogs no longer appear because the Sequence File posts UI message 10200. The handler for this message sets the FileGlobals.ShowDialogs property to the value of the Show Sequence Dialogs setting in the setup step group.
5. You can optionally execute this sequence file in other user interfaces that do not handle the specified user messages. The sequence will run successfully, but the user messages posted will have no effect.

Complete the following steps to review the UI message handling code in the UI:

1. In Using Custom UI Messages.lvproj , open Basic User Interface with UI Message Handler.vi.
2. In the Register Event Callbacks case, notice that UserMessage Event Callback.vi is registered to the UserMessage event.
3. Open the UserMessage Event Callback.vi and review the message handling code in each case.

Complete the following steps to review how UI messages are posted from an executing sequence:

1. Open the example sequence file <TestStand Public>\Examples\Modifying User Interfaces\Handling UI Messages\UI Message Example.seq
2. Inspect the statement steps. Each of these steps posts a UI message using the Thread.postUIMessageEx method.

Parent topic:

Handling UI Messages

Related concepts:

- TestStand Directory Structure
- User Interface Messages (UIMessages)
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=handling-ui-messages-labwindows-cvi.html language=enus -->
## TOPIC 00430: Handling UI Messages - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `handling-ui-messages-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-ui-messages-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how you can use custom UI messages to communicate between the client sequence file and the user interface. Sending data from the sequence to the UI—The Sequence posts UI messages containing a status string. The UI message handler reads the string and updates a UI control w

### Handling UI Messages - LabWindows/CVI

#### Purpose

This example shows how you can use custom UI messages to communicate between the client sequence file and the user interface.

- Sending data from the sequence to the UI —The Sequence posts UI messages containing a status string. The UI message handler reads the string and updates a UI control with the data.
- Sending data from the UI to the sequence —Before executing, the sequence posts a message requesting the state of the "show dialogs" UI setting. The UI message handler sets the Locals.ShowDialogs sequence property using the TestStand API, based on the value specified in the UI.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Handling UI
 Messages\CVI\Using Custom UI Messages.prj

#### Highlighted Features

- User Interface Messages
- TestStand User Interface controls

#### Major API

Thread.PostUIMessageEx

#### Prerequisites

You must have LabWindows/CVI installed to execute this example.

#### How to Use This Example

Complete the following steps to run the example:

1. (64-bit TestStand) Navigate to Build»Configuration and select Debug64 as the configuration.
2. Click Debug Project in CVI to start the user interface. The UI Message example sequence is opened by the UI automatically.
3. Run the sequence. Notice that the sequence status is updated as each UI message is posted with ID 10100.
4. After the execution completes, uncheck the Show Sequence Dialogs option on the user interface. Run the sequence again, and notice that the message dialogs no longer appear. The dialogs no longer appear because the Sequence File posts UI message 10200. The handler for this message sets the FileGlobals.ShowDialogs property to the value of the Show Sequence Dialogs setting in the setup step group.
5. You can optionally execute this sequence file in other user interfaces that do not handle the specified user messages. The sequence will run successfully, but the user messages posted will have no effect.

Complete the following steps to review the UI message handling code in the CVI UI:

1. In Using Custom UI Messages.prj , open TestExec.c .
2. Find the function TSUI__ApplicationMgrEventsRegOnUserMessage. This function registers the ApplicationMgr_OnUserMessage function as the User Message message handler. The UserMessage Event begins when a UI message with ID greater than 10000 is posted. These IDs are reserved for user-generated messages.
3. Find the ApplicationMgr_OnUserMessage function. Notice that each UI message is defined as a case in the switch block. These cases define how each UI message is handled.

Complete the following steps to review how UI messages are posted from an executing sequence:

1. Open the example sequence file <TestStand Public>\Examples\Modifying User Interfaces\Handling UI Messages\UI Message Example.seq
2. Inspect the statement steps. Each of these steps posts a UI message using the Thread.postUIMessageEx method.

Parent topic:

Handling UI Messages

Related concepts:

- TestStand Directory Structure
- User Interface Messages (UIMessages)
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=handling-ui-messages-net.html language=enus -->
## TOPIC 00431: Handling UI Messages - .NET

- bundle_id: `teststand`
- source_path: `handling-ui-messages-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-ui-messages-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how you can use custom UI messages to communicate between the client sequence file and the user interface. Sending data from the sequence to the UI—The Sequence posts UI messages containing a status string. The UI message handler reads the string and updates a UI control w

### Handling UI Messages - .NET

#### Purpose

This example shows how you can use custom UI messages to communicate between the client sequence file and the user interface.

- Sending data from the sequence to the UI —The Sequence posts UI messages containing a status string. The UI message handler reads the string and updates a UI control with the data.
- Sending data from the UI to the sequence —Before executing, the sequence posts a message requesting the state of the "show dialogs" UI setting. The UI message handler sets the Locals.ShowDialogs sequence property using the TestStand API, based on the value specified in the UI.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Handling UI
 Messages\DotNet\Handling UI Messages.sln

#### Highlighted Features

- User Interface Messages
- TestStand User Interface controls

#### Major API

Thread.PostUIMessageEx

#### Prerequisites

You must have Visual Studio installed to execute this example.

#### How to Use This Example

Complete the following steps to run the example:

1. Click Start Debugging in Visual Studio to start the user interface. The UI Message example sequence is opened by the UI automatically.
2. Run the sequence. Notice that the sequence status is updated as each UI message is posted with ID 10100.
3. After the execution completes, uncheck the Show Sequence Dialogs option on the user interface. Run the sequence again and notice that the message dialogs no longer appear. The dialogs no longer appear because the Sequence File posts UI message 10200. The handler for this message sets the FileGlobals.ShowDialogs property to the value of the Show Sequence Dialogs setting in the setup step group.
4. You can optionally execute this sequence file in other user interfaces that do not handle the specified user messages. The sequence will run successfully, but the user messages posted will have no effect.

Complete the following steps to review the UI message handling code in the UI:

1. In Handling UI Messages.sln , open MainForm.cs .
2. In the form designer, select the Application manager control. In the properties pane, click the Events icon to view the registered events for the ApplicationManager.
3. Find the User message event, and notice that the axApplicationMgr_UserMessageCallback method is registered to handle this event. The UserMessage Event begins when a UI message with ID greater than 10000 is posted. These IDs are reserved for user-generated messages.
4. Double click the ApplicationMgr_OnUserMessage to navigate to the method code. Notice that each UI message is defined as a case in the switch block. These cases define how each UI message is handled.

Complete the following steps to review how UI messages are posted from an executing sequence:

1. Open the example sequence file <TestStand Public>\Examples\Modifying User Interfaces\Handling UI Messages\UI Message Example.seq
2. Inspect the statement steps. Each of these steps posts a UI message using the Thread.postUIMessageEx method.

Parent topic:

Handling UI Messages

Related concepts:

- TestStand Directory Structure
- User Interface Messages (UIMessages)
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=handling-ui-messages.html language=enus -->
## TOPIC 00432: Handling UI Messages

- bundle_id: `teststand`
- source_path: `handling-ui-messages.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-ui-messages.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Modifying User Interfaces\Handling UI Messages directory contains the following examples.

### Handling UI Messages

The <TestStand
 Public>\Examples\Modifying User Interfaces\Handling UI
 Messages directory contains the following examples.

- [Handling UI Messages - LabWindows/CVI](handling-ui-messages-labwindows-cvi.html)
- [Handling UI Messages - LabVIEW](handling-ui-messages-labview.html)
- [Handling UI Messages - .NET](handling-ui-messages-net.html)

Parent topic:

Examples for Modifying User Interfaces

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=handling-unknown-events.html language=enus -->
## TOPIC 00433: Handling Unknown Events

- bundle_id: `teststand`
- source_path: `handling-unknown-events.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-unknown-events.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you receive a user interface message with an event ID the application does not expect, complete one of the following steps: If you are polling, release the user interface message and continue polling. If you receive the user interface message in a callback, return from the callback without respon

### Handling Unknown Events

If you receive a user interface message with an event ID the application does not expect, complete one of the following steps:

- If you are polling, release the user interface message and continue polling.
- If you receive the user interface message in a callback, return from the callback without responding to the message.

Note

Parent topic:

Handling Specific User Interface Messages

<!--NI_TOPIC bundle=teststand path=handling-variants-in-labwindows-cvi-user-inte.html language=enus -->
## TOPIC 00434: Handling Variants in LabWindows/CVI User Interfaces

- bundle_id: `teststand`
- source_path: `handling-variants-in-labwindows-cvi-user-inte.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/handling-variants-in-labwindows-cvi-user-inte.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Several functions in the TestStand API return variants. If the return value of these functions is a reference to an ActiveX/COM object, you must cast these variants to a valid handle type. To do this properly in LabWindows/CVI, you must create a temporary variable to hold the value and then convert

### Handling Variants in LabWindows/CVI User Interfaces

Several functions in the TestStand API return variants. If the return value of these functions is a reference to an ActiveX/COM object, you must cast these variants to a valid handle type. To do this properly in LabWindows/CVI, you must create a temporary variable to hold the value and then convert the value to the correct type of handle.

Use the following function call to convert an IUnknown reference to a CAObjHandle:

CA_CreateObjHandleFromInterface (IUnknownReference, &IID_IUnknown, 0, LOCALE_NEUTRAL, 0, 0, &CAObjToCreate);

Use the following function call to convert a variant to a CAObjHandle:

CA_VariantConvertToType(&VariantReference, CAVT_OBJHANDLE, &CAObjToCreate);

A common situation where you need to use this technique is when you handle UIMessages. The following example shows how you can extract the ActiveXData parameter of the custom user message as a property object to handle UIMessages:

```text
HRESULT CVICALLBACK ApplicationMgr_OnUserMessage(CAObjHandle caServerObjHandle, void 
*caCallbackData, TSUIObj_UIMessage uiMsg)
{
    int error = 0;
    ErrMsg errMsg = "";
    ERRORINFO errorInfo;
    LPUNKNOWN tempPropObject = 0;
    CAObjHandle PropObject = 0;
    tsErrChk(TS_UIMessageGetActiveXData(uiMsg, NULL, &tempPropObject));
    CA_CreateObjHandleFromInterface (tempPropObject, &IID_IUnknown, 0, LOCALE_NEUTRAL, 0, 0, &PropObject);
    //TODO: Implement your code here
Error:
    //free resources
    if (PropObject)
        CA_DiscardObjHandle(PropObject);
    return error;
}
```

Parent topic:

Using TestStand UI Controls in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=hidden-execution-entry-points-in-the-batch-pr.html language=enus -->
## TOPIC 00435: Hidden Execution Entry Points in the Batch Process Model

- bundle_id: `teststand`
- source_path: `hidden-execution-entry-points-in-the-batch-pr.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/hidden-execution-entry-points-in-the-batch-pr.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main Execution entry points of the Batch process model use but do not display the following hidden Execution entry point sequences to initiate test socket executions: Test UUTs - Test Socket Entry Point—The controlling execution invokes this entry point in a new execution once for each test sock

### Hidden Execution Entry Points in the Batch Process Model

The main Execution entry points of the Batch process model use but do not display the following hidden Execution entry point sequences to initiate test socket executions:

- Test UUTs - Test Socket Entry Point—The controlling execution invokes this entry point in a new execution once for each test socket to create the test socket executions.
- Single Pass - Test Socket Entry Point—The controlling execution invokes this entry point in a new execution once for each test socket to create the test socket executions.

Parent topic:

Batch Process Model

Related concepts:

- Main Execution Entry Points in the Batch Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model
- Single Pass - Test Socket Entry Point in the Batch Process Model

<!--NI_TOPIC bundle=teststand path=hidden-execution-entry-points-in-the-parallel.html language=enus -->
## TOPIC 00436: Hidden Execution Entry Points in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `hidden-execution-entry-points-in-the-parallel.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/hidden-execution-entry-points-in-the-parallel.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main Execution entry points of the Parallel process model use but do not display the following hidden Execution entry point sequences to initiate test socket executions: Test UUTs - Test Socket Entry Point—The controlling execution uses this entry point to create the test socket executions and i

### Hidden Execution Entry Points in the Parallel Process Model

The main Execution entry points of the Parallel process model use but do not display the following hidden Execution entry point sequences to initiate test socket executions:

- Test UUTs - Test Socket Entry Point—The controlling execution uses this entry point to create the test socket executions and implement the Test UUTs Execution entry point for the test socket executions.
- Single Pass - Test Socket Entry Point—The controlling execution uses this entry point to create the test socket executions and implement the Single Pass Execution entry point for test socket executions.

Parent topic:

Parallel Process Model

Related concepts:

- Main Execution Entry Points in the Parallel Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Parallel Process Model
- Test UUTs Execution Entry Point in the Parallel Process Model
- Single Pass - Test Socket Execution Entry Point in the Parallel Process Model
- Single Pass Execution Entry Point in the Parallel Process Model

<!--NI_TOPIC bundle=teststand path=htbasic-adapter.html language=enus -->
## TOPIC 00437: HTBasic Adapter

- bundle_id: `teststand`
- source_path: `htbasic-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/htbasic-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The HTBasic Adapter is hidden by default. Use the Adapter Configuration dialog box to configure the HTBasic Adapter. Use the HTBasic Adapter to call HTBasic subroutines without passing parameters directly to a subroutine. TestStand provides a library of CSUB routines that use the TestStand API to ac

### HTBasic Adapter

Note

Note

- (Windows 8.1/8/7/Vista) HTBasic currently does not support Windows 8.1/8/7/Vista. If you installed the HTBasic 9.0 development environment under Windows 8.1/8/7/Vista, you can perform the Edit Subroutine and Create Subroutine functions on the HTBasic Module tab in the TestStand Sequence Editor when you use a step configured to use the HTBasic Adapter, but the HTBasic code modules might not run correctly.
- (64-bit TestStand) 64-bit TestStand does not support the HTBasic Adapter.

When you specify a module for a step, the sequence editor displays the HTBasic Module tab and TestStand User Interfaces launch the Edit HTBasic Subroutine Call dialog box.

Parent topic:

Module Adapters

Related concepts:

- Code Modules
- Features 64-Bit TestStand does not Support
- Programming with the TestStand API in HTBasic

<!--NI_TOPIC bundle=teststand path=identifying-components-to-deploy.html language=enus -->
## TOPIC 00438: Identifying Components to Deploy

- bundle_id: `teststand`
- source_path: `identifying-components-to-deploy.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/identifying-components-to-deploy.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following table to identify the files to explicitly include in the deployment to ensure that the test system executes successfully on the test station computer: Component Guidance TestStand license Review the TestStand license options to determine which license to use. Sequence files Identif

### Identifying Components to Deploy

[IMAGE alt='image' src='GUID-DC6D85FB-3D00-4085-A284-D626A061B7FC-a5.svg']

Use the
 following table to identify the files to explicitly include in the deployment to
 ensure that the test system executes successfully on the test station
 computer:

| Component | Guidance |
| --- | --- |
| TestStand license | Review the TestStand license options to determine which license to use. |
| Sequence files | Identify the set of sequence files the test system requires by creating a list of the high-level tasks the test system performs, including trouble-shooting, calibrating devices, and performing other diagnostic tasks. For each task, identify the root sequence or sequences that accomplish the task. For each sequence, identify the process models the sequence uses. The TestStand Deployment Utility automatically identifies and includes sequence files for the sequences that Sequence Call steps statically reference. You must manually identify and include sequence files for sequences that Sequence Call steps dynamically reference. Use the Sequence Hierarchy window in the TestStand Sequence Editor to display a graph of the hierarchy of all sequences and sequence calls that use expressions for a sequence file. |
| TestStand Runtime | A test system you deploy to a test station computer requires the TestStand Runtime to execute TestStand sequence files. You can customize the features of the TestStand Runtime to include in the installer you build with the deployment utility, such as excluding the default TestStand examples and tutorials. The TestStand Engine is part of the TestStand Runtime. The TestStand Engine includes a backward-compatible API so you can use existing property and method calls in later versions of the TestStand Engine without modification and so you can run user interfaces built in earlier versions of TestStand with later versions of the TestStand Engine. |
| Code modules | The deployment utility automatically includes static dependencies of code modules, such as utility DLLs statically linked to code module DLLs and VI dependencies. However, you must manually include implicitly referenced files, such as documentation, images, and support files, and dynamically referenced files, such as VIs you call using VI Server or dynamically loaded DLLs.You must verify that the test system uses all the dynamically called files you added to the workspace or to destination directories, including code modules you added to a workspace by using the Insert Code Modules context menu item in the Workspace Browser dialog box or the Insert Code Modules context menu item in the Workspace pane. |
| Files that Property Loader steps call | The deployment utility automatically includes source files that Property Loader steps reference. If the file is specified dynamically through a TestStand expression that can only be evaluated at runtime, you must manually include all the files the expression could potentially reference. TestStand Deployment Utility will display a message listing any expressions that it could not evaluate. |
| Image files, support files, configuration files, or data files | Because other files in a test system typically implicitly reference image, support, configuration, and data files, you must manually include these types of files. |
| LabVIEW toolkits | Most LabVIEW toolkits do not require the toolkit license to execute VIs you build with the toolkit. Refer to the toolkit licensing requirements to determine if you need to include the toolkit license or any additional components required to execute these VIs. |
| LabWindows/CVI Run-Time Engine | You can use the shared or side-by-side version of the LabWindows/CVI Run-Time Engine (RTE) to execute DLLs built with LabWindows/CVI from TestStand. |
| LabVIEW Run-Time Engine | By default, the deployment utility includes all required dependencies and compiles all VIs included in the deployment. You must manually include any dynamically-called VIs in the deployment. |
| LabVIEW NXG Run-Time Engine | By default, the deployment utility invokes LabVIEW NXG to recompile all GLL binaries included in the deployment using the associated source files. You can optionally include source files in the deployment to make changes to LabVIEW NXG code modules on the test station computer. The LabVIEW NXG run-time engine is required to execute test code within GLLs. |
| LabVIEW modules | The LabVIEW DataLogging and Supervisory Control (DSC) Module requires the LabVIEW DSC Module Run-Time System installed on the test station computer. In contrast, you can run LabVIEW Real-Time Module VIs on a pre-configured, real-time computer without including the LabVIEW Real-Time Module in the deployment. Refer to the documentation for the LabVIEW module to determine whether you need to include it. |
| Configuration files in the <TestStand Application Data>\\Cfg directory | Include the configuration files you customized for the settings you want to use on the test station computer. You can use configuration files customized for test sequence developers to use on development computers that are different from configuration files you customize for operators to use on test station computers. |
| TestStand components | Include the components you customized in the <TestStand Public>\\Components directory, such as a process model you modified to launch a customized dialog box for entering scanned UUT serial numbers or a user interface you customized to provide debugging information for operators. Enable the From TestStand Public Directories option in the Deploy Files section on the System Source tab of the deployment utility to include all files in the <TestStand Public>\\Components directory. If you deploy a process model based on an NI model, the model uses a language resource file to support localized strings. For model strings to appear correctly, you must also include the required language file in your deployment:<TestStand>\\Components\\Language\\English\\ModelStrings.ini. To ensure this file is included, copy it to the <TestStand Public>\\Components\\Language\\English directory before deploying. |
| User interface executable | You can deploy the default user interfaces TestStand includes or you can create a customized user interface to deploy. If you deploy a customized user interface, include the following files:The user interface executableConfiguration filesDependent DLLs, ActiveX controls, or .NET assemblies or controlsLanguage .ini files for localization, if requiredRequired run-time engines |
| Run-time engines | The following file types require certain components on the test station computer to execute correctly. You do not need to include the required component in the deployment if the test station computer already has the component installed.Code modules, executables or DLLs you built with LabVIEW—Version of LabVIEW RTE that matches the version of LabVIEW you used to create the code module, executable, or DLLYou can install multiple versions of the LabVIEW RTE on a test station computer. However, NI recommends using only one version of the LabVIEW RTE in a single test system to simplify deployment.Code modules, executables or DLLs you built with LabVIEW NXG—Version of LabVIEW NXG RTE that matches the active version of LabVIEW NXG you used to rebuild the GLL binariesYou can install multiple versions of the LabVIEW NXG RTE on a test station computer. However, NI recommends using only one version of the LabVIEW NXG RTE in a single test system to simplify deployment. DLL code modules or executables you built with LabWindows/CVI—Version of LabWindows/CVI RTE that matches or that is later than the version of LabWindows/CVI you used to create the executable or DLLYou can install or upgrade only one version of the default LabWindows/CVI RTE on a test station computer at a time, but you can install or upgrade multiple versions of the side-by-side version of the LabWindows/CVI RTE.When you deploy a user interface executable or a DLL module that is bound to a side-by-side version of the LabWindows/CVI RTE, you must explicitly include the side-by-side version of the LabWindows/CVI RTE in the deployable image you use to build an installer with the deployment utility.In the Drivers and Components dialog box, you must enable the item in the Components to Include list that corresponds to the side-by-side version of the LabWindows/CVI RTE you want to use, such as NI LabWindows/CVI Side-By-Side Run-Time Engine 2012..NET assembly—Version of .NET that supports executing the assembly (Refer to Microsoft documentation for more information about .NET version compatibility and deployment.) |
| NI hardware drivers | Refer to the documentation for the NI device the test system uses to determine the driver to include. You do not need to include the NI hardware driver in the deployment if the test station computer already has the driver installed. You can also include NI hardware configuration information. |
| Third-party components | Include the third-party hardware drivers or software components required to execute the test system correctly. You can include the collection of third-party files in the single installer you build with the deployment utility using custom commands. |

#### Components to Deploy for Editing on a
 Test Station

In some cases you might need to make changes to debug or fix
 an issue with the test system. Typically, after you correct the issue with the test
 system, you re-deploy the entire test system or you deploy a patch that contains
 only the updated module.

If you want to edit code modules on the test station
 computer, you must install the LabWindows/CVI Development System to debug or
 recompile DLLs you built with LabWindows/CVI, and you must install the LabVIEW
 Development System and all toolkits and modules required to debug or edit VIs. You
 can use a TestStand Debug Deployment Environment License on the test station
 computer to edit code modules on the test station computer.

Exclude
 VIs from vi.lib, instr.lib, or
 user.lib from deployments when you deploy VIs that you expect
 others to edit, such as when you deploy VIs to another development computer or to a
 test station computer that includes the LabVIEW Development System, the TestStand
 Runtime, a custom user interface, and a TestStand Custom Sequence Editor License so
 other developers can modify and redeploy test sequences.

To include source
 files for LabVIEW NXG code modules, enable the Include LabVIEW NXG source
 files option, located in the LabVIEW NXG
 options tab of the LabVIEW VI options dialog. Launch the LabVIEW VI
 options dialog using the LabVIEW Options button on the Distributed Files
 tab.

Parent topic:

Deployment Process Overview

Related concepts:

- Including Source Components
- Activating and Licensing TestStand
- Manually Adding or Removing Files to or from Deployments
- Choosing Between the Shared or Side-by-Side Version of the LabWindows/CVI Run-Time Engine
- Including TestStand Configuration Files in a Deployment
- TestStand Directory Structure
- Configuration Files
- Including Files from the TestStand Public Directory in a Deployment
- User Components
- Including a User Interface in a Deployment
- Creating Custom User Interfaces
- Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand
- Building a Customized MSI-based Installer
- Including Hardware Configuration Information in a Deployment
- Using Custom Commands to Execute Third-Party Installers
- Customizing Components You Deploy

<!--NI_TOPIC bundle=teststand path=image-connections.html language=enus -->
## TOPIC 00439: Image Connections

- bundle_id: `teststand`
- source_path: `image-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/image-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Image connections display icons that illustrate the status of the application. For example, you can use the ExecutionView Manager control to connect an image to a Button control or a StatusBar pane so the button or pane displays an image that indicates the execution state of the selected execution.

### Image Connections

Image connections display icons that illustrate the status of the application. For example, you can use the ExecutionView Manager control to connect an image to a Button control or a StatusBar pane so the button or pane displays an image that indicates the execution state of the selected execution.

The ImageSources enumeration defines the set of images to which you can connect. Some images apply to the selected item in the manager control with which you connect them. For example, the CurrentStepGroup enumeration constant displays an image for the currently selected step group when you connect it to a SequenceFileView Manager control and displays an image for the currently executing step group when you connect it to an ExecutionView Manager control.

Call the following methods to connect an image to a Button control or a StatusBar pane:

- SequenceFileViewMgr.ConnectImage
- ExecutionViewMgr.ConnectImage

Call the following methods to obtain an image without connecting the image to a control:

- ApplicationMgr.GetImageName
- SequenceFileViewMgr.GetImageName
- ExecutionViewMgr.GetImageName

To obtain an image from an image name, you must use properties from the TestStand API, such as the Engine.SmallImageListEx property, the Engine.LargeImageListEx property, and the Engine.Images property.

Parent topic:

Information Source Connections

Related concepts:

- ExecutionView Manager
- Manager Controls
- SequenceFileView Manager

<!--NI_TOPIC bundle=teststand path=implementing-a-tools-menu.html language=enus -->
## TOPIC 00440: Implementing a Tools Menu

- bundle_id: `teststand`
- source_path: `implementing-a-tools-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/implementing-a-tools-menu.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To implement a Tools menu, you must first call the Engine.GetRunTimeToolMenuItems method, which returns a collection of RunTimeMenuItem objects. Each object in the collection represent menu items or submenus to display. The Engine.GetRunTimeToolMenuItems method takes an EditArgs object as a paramete

### Implementing a Tools Menu

To implement a Tools menu, you must first call the Engine.GetRunTimeToolMenuItems method, which returns a collection of RunTimeMenuItem objects. Each object in the collection represent menu items or submenus to display. The Engine.GetRunTimeToolMenuItems method takes an EditArgs object as a parameter. Pass an EditArgs object to indicate which execution, sequences, and steps are selected when the user requests to display the Tools menu.

For each menu item, the RunTimeMenuItem.Text property specifies the menu item text and the RunTimeMenuItem.ItemEnabled property specifies whether the menu item is enabled. If the RunTimeMenuItem.SubMenuItems property is not NULL, you must display the menu item as a submenu. The RunTimeMenuItem.SubMenuItems property returns a collection of its submenu items.

Use RunTimeMenuItem.InvokeItem to execute a menu item, which launches an executable or runs a sequence in a new execution. Pass the same EditArgs object as the parameter you used when calling the Engine.GetRunTimeToolMenuItems method.

In addition to displaying the Tools menu items in an application, you can also add a Customize menu item to allow the user to configure the Tools menu. To do so, add a menu item to the Tools menu that calls the Engine.DisplayToolMenuDialog method. To customize the Tools menu programmatically, operate on the collection the Engine.GetEditTimeToolMenuItems method returns.

Parent topic:

Writing an Application with the TestStand Engine API

<!--NI_TOPIC bundle=teststand path=implementing-analysis-modules.html language=enus -->
## TOPIC 00441: Implementing Analysis Modules

- bundle_id: `teststand`
- source_path: `implementing-analysis-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/implementing-analysis-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The sequence analyzer passes an AnalysisContext object to the analysis module. After calling a VI, the sequence analyzer checks the Error Out cluster output and reports an Internal Error analysis message if the status indicates that an error occurred. After calling a .NET method, the sequence report

### Implementing Analysis Modules

The sequence analyzer passes an
 AnalysisContext
 object to the analysis module. After calling a VI, the sequence analyzer checks the
 Error Out cluster output and reports an Internal Error
 analysis message if the status indicates that an error occurred. After calling a .NET
 method, the sequence reports an Internal Error analysis message if the method returns
 False. After calling a DLL function, the sequence analyzer checks
 the return value and reports an Internal Error analysis message if the
 bool value is False or if the
 int value is not 0. The Analysis Results
 pane in the TestStand Sequence Editor and the Messages tab in the stand-alone sequence
 analyzer application include the error message the analysis module returns for the most
 recent analysis of the current project.

Analysis modules use the AnalysisContext properties and methods to
 analyze individual objects. The sequence analyzer does not maintain or recognize any
 relationships between analysis modules and rules. The sequence analyzer calls all
 analysis modules regardless of which rules are disabled, but the sequence analyzer
 discards messages reported for disabled rules. To improve performance when a rule is
 disabled, ensure that an analysis module first checks if the rule is enabled before
 performing any analysis. Pass the rule ID to the
 AnalysisContext.GetRuleConfiguration
 method to get the RuleConfiguration for the rule and check the
 RuleConfiguration.Enabled
 property. Pass the rule ID to the
 AnalysisContext.NewMessage
 method to create a new message for the rule, and call the
 AnalysisContext.ReportMessage
 method to report the message to the sequence analyzer. Use the
 AnalysisContext.File
 and
 AnalysisContext.Object
 properties to get the analyzed file and object.

The sequence analyzer calls an analysis module only for the kinds of objects you specify
 in the Edit Analysis Module dialog box. Each time the sequence analyzer makes a
 transition between analyzing one type of object to analyzing a different type of object,
 it calls analysis modules configured to be called for that type of transition. If you
 specify analysis transitions in the Edit Analysis Module dialog box, the sequence
 analyzer calls the analysis module at those transitions. Use the
 AnalysisContext.Transition
 property to determine which transition is in effect.

Use the
 AnalysisContext.GetRuleAnalysisData
 method to get an empty
 PropertyObject
 container to which you add subproperties to store data associated with a rule during the
 current analysis session. You must use the
 GetRuleAnalysisDataOption_Lock
 option if the analysis module modifies the data.

If you use global variables during analysis, use the following techniques to help ensure
 data integrity:

- Use locks to protect access to the global data by preventing the sequence analyzer
 from calling analysis modules from multiple threads at the same time.
- Use the
 AnalysisContext.AnalysisId
 property to get a unique identifier for the current analysis session that you can
 use to index into a global table to avoid interference between simultaneous analysis
 sessions.
- Use the
 AnalysisTransition_BeforeSystem
 and
 AnalysisTransition_AfterSystem
 transitions to initialize and clean up global data.

When you stop the analysis before it completes, the sequence analyzer waits for the
 currently executing analysis module to complete. If the sequence analyzer has called any
 analysis modules for any Before analysis transitions, the
 sequence analyzer calls the same analysis modules for the corresponding
 After analysis transitions. Analysis modules generally should
 not report messages after you stop analysis. If the analysis module reports messages
 during the After analysis transitions, check the
 AnalysisContext.StopRequested
 property to determine whether users stopped the analysis so you can avoid reporting the
 messages.

Use the
 AnalysisContext.Utilities
 property to access the
 AnalysisUtilities
 methods, which perform common types of checks, such as validating
 expressions,
 paths, and remote hosts, or enabling automatic property checking. The built-in analysis
 modules perform some of these checks on all instances of certain types, such as
 validating expressions and paths. To disable the built-in checking for subproperties of
 certain objects for a custom rule, set the
 AnalysisUtilities.AutomaticPropertyCheckingEnabled
 property to False in the custom analysis module the sequence analyzer
 calls for those objects. For instance, to disable automatic checking of subproperties of
 a step type that you implemented, set the
 AnalysisUtilities.AutomaticPropertyCheckingEnabled property to
 False in the custom analysis module the sequence analyzer calls for
 instances of the custom step type.

Parent topic:

Creating Analysis Modules for Custom Rules

Related concepts:

- Expressions
- Prototypes for Analysis Modules

Related information:

- RuleConfiguration
- AnalysisContext
- PropertyObject
- GetRuleAnalysisDataOptions
- AnalysisUtilities
- AnalysisTransition

<!--NI_TOPIC bundle=teststand path=implementing-batch-controller-and-test-socket.html language=enus -->
## TOPIC 00442: Implementing Batch Controller and Test Socket Synchronization for a Custom Model Plug-in

- bundle_id: `teststand`
- source_path: `implementing-batch-controller-and-test-socket.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/implementing-batch-controller-and-test-socket.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default result processing model plug-ins perform controller and test socket synchronization when you execute a sequence using the Batch process model. For example, the default Report result processing model plug-in, located at <TestStand>\Components\Models\ModelPlugins\NI_ReportGenerator.seq, pe

### Implementing Batch Controller and Test Socket Synchronization for a Custom Model Plug-in

The default result processing model plug-ins perform controller and test socket synchronization when you execute a sequence using the Batch process model.

For example, the default Report result processing model plug-in, located at <TestStand>\Components\Models\ModelPlugins\NI_ReportGenerator.seq, performs controller and test socket synchronization to force test sockets to serially write individual UUT reports to a file on disk after the controller writes the Batch report to a file on disk.

Use the following information to help you implement controller and test socket synchronization in a custom model plug-in.

#### Enabling Controller and Test Socket Synchronization for a Model Plug-in

The NI_ModelPlugin data type in a process model plug-in sequence file contains a Base.RequiresBatchControllerAndSocketSynchronization Boolean subproperty that enables or disables batch controller and test socket synchronization functionality for the plug-in. To use controller and test socket synchronization in a plug-in, ensure that this property is True.

Note

True

False

#### Implementing Batch Controller and Test Socket Synchronization in a Model Plug-in Entry Point

Model plug-ins use the Locals.ControllerAndSocketSynchronizationManager object reference to implement controller and test socket synchronization between the Model Plugin – Batch Start and Model Plugin – UUT Start entry points and between the Model Plugin – Batch Done and Model Plugin – UUT Done entry points. Model plug-ins must synchronize between these entry points because these entry points execute asynchronously to the corresponding UUT entry point counterparts. The Batch process model synchronizes all other Batch/UUT model plug-in entry point pairs.

Note

- Implementing controller and test socket synchronization in any model plug-in entry point other than the Model Plugin – Batch Start, Model Plugin – UUT Start, Model Plugin – UUT Done, and Model Plugin – Batch Done entry points might cause TestStand to hang when you execute sequences using the Batch process model.
- When you use the Result Processing dialog box to create a plug-in, the Locals.ControllerAndSocketSynchronizationManager object reference already exists. If you manually create a plug-in, you must correctly implement the Locals.ControllerAndSocketSynchronizationManager object reference. Refer to the Model Plugin – UUT Done and Model Plugin – Batch Done entry points of the default Report result processing model plug-in for an example of using the Locals.ControllerAndSocketSynchronizationManager object reference in an existing plug-in.

You must conditionally execute all calls to the SyncWithController method in the Model Plugin – UUT Start and Model Plugin – UUT Done entry points only when you execute sequences in the Batch process model. When a Model Plugin – UUT Start or Model Plugin – UUT Done entry point contains a call to the SyncWithController method, you can use the following precondition on the calling step to specify that the entry point executes the call only when the Batch process model calls the entry point:

Parameters.ModelData.ModelType == "Batch"

Refer to the Model Plugin – UUT Start and Model Plugin – UUT Done entry points of the default Report result processing model plug-in for an example of specifying this precondition in an existing plug-in entry point.

Parent topic:

Batch Controller and Test Socket Synchronization Architecture

Related concepts:

- Process Model Plug-In Architecture
- Batch Process Model
- TestStand Directory Structure
- Creating Process Model Plug-ins
- Model Plugin – Batch Start
- Model Plugin – UUT Start
- Model Plugin – Batch Done
- Model Plugin – UUT Done
- Model Plug-in Entry Points

<!--NI_TOPIC bundle=teststand path=implementing-command-line-arguments-for-a-use.html language=enus -->
## TOPIC 00443: Implementing Command-Line Arguments for a User Interface

- bundle_id: `teststand`
- source_path: `implementing-command-line-arguments-for-a-use.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/implementing-command-line-arguments-for-a-use.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Application Manager control automatically processes the command-line argument that invokes the application when you call the ApplicationMgr.Start method. Set the ApplicationMgr.ProcessCommandLine property to False before you call the ApplicationMgr.Start method to disable command-line processing

### Implementing Command-Line Arguments for a User Interface

The Application Manager control automatically processes the command-line argument that invokes the application when you call the ApplicationMgr.Start method. Set the ApplicationMgr.ProcessCommandLine property to False before you call the ApplicationMgr.Start method to disable command-line processing.

You can also handle the ApplicationMgr.ProcessUserCommandLineArguments event to support additional command-line arguments. The ApplicationMgr.ProcessUserCommandLineArguments event occurs when the Application Manager control parses and processes an unrecognized command-line flag.

Parent topic:

Advanced User Interface Development

Related concepts:

- Application Manager
- Configuring Sequence Editor and User Interface Startup Options

<!--NI_TOPIC bundle=teststand path=import-sle-sm.html language=enus -->
## TOPIC 00444: Importing Specifications from SLE Specification Manager

- bundle_id: `teststand`
- source_path: `import-sle-sm.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/import-sle-sm.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Specifications pane to import product specifications from SLE Specification Manager for use in a TestStand sequence. You must define an SLE server address, API token value, and the products and categories you want to import for initial specification imports. To import values from SLE Specifi

### Importing Specifications from SLE
 Specification Manager

Use the Specifications pane to import product specifications from
 SLE Specification Manager for use in a TestStand sequence. You must define an SLE server
 address, API token value, and the products and categories you want to import for initial
 specification imports.

To import values from SLE Specification Manager into TestStand:

1. Launch the Manage Specifications dialog box by
 right-clicking in the Specifications pane and selecting Browse Files»Download from SystemLink Enterprise. 
 [IMAGE alt='image' src='GUID-4E0B29D5-ECD3-4002-860A-78E920CEAFB3-a5.png']
2. Enter the server information for the SLE server you want to connect to. 
 [IMAGE alt='image' src='GUID-C61E1829-933E-481D-85C6-97AB6C8057C1-a5.png']
  1. Enter the URL of the SLE server you want to connect to.
  2. Enter the API token value created in the SLE server you are connecting
 to.
  3. Click Connect.
3. Select the products and categories you want to import from the SLE
 server. 
 [IMAGE alt='image' src='GUID-ABD938DD-AE2D-41B1-9BB0-D5DDF0FEE4F7-a5.png']
4. Click OK to save the product name and selected
 categories and load your specifications in the active sequence file.

You can map imported specifications to
 measurement plug-ins and code modules and use them to create steps in your sequence
 file.

Parent topic:

Importing Specifications into TestStand Using the Specifications Pane

<!--NI_TOPIC bundle=teststand path=import-spec-external-file.html language=enus -->
## TOPIC 00445: Importing Specifications from Specification Files

- bundle_id: `teststand`
- source_path: `import-spec-external-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/import-spec-external-file.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the Specifications pane to import specification values from specification files. You can find the template specifications file recommended for use in this process at C:\Users\Public\Documents\National Instruments\TestStand 2024 (64-bit)\Examples\Specifications Integration. Launch the Man

### Importing Specifications from Specification
 Files

You can use the Specifications pane to import specification values
 from specification files.

C:\Users\Public\Documents\National Instruments\TestStand
 2024 (64-bit)\Examples\Specifications
 Integration

1. Launch the Manage Specifications dialog
 box by right-clicking in the
 Specifications pane and
 selecting Browse Files»Upload from this Device. 
 [IMAGE alt='image' src='GUID-4E0B29D5-ECD3-4002-860A-78E920CEAFB3-a5.png']
2. Select the file you want to import specifications from and click
 OK.
3. Select the specification categories you want to import. and
  1. Open the Select Category
 dialog box by clicking the
 Pencil icon next to your
 imported specification file. 
 [IMAGE alt='image' src='GUID-F6D9E8B9-A127-4203-8B5C-953C9F509EF4-a5.png']
  2. Select the required categories from the
 category list. 
 [IMAGE alt='image' src='GUID-68BDB202-DFA6-41AF-8C54-C270447AD6D2-a5.png']

You can map imported
 specifications to measurement plug-ins and code modules and use them to
 create steps in your sequence file.

Parent topic:

Importing Specifications into TestStand Using the Specifications Pane

<!--NI_TOPIC bundle=teststand path=importing-and-exporting-with-a-legacy-source.html language=enus -->
## TOPIC 00446: Importing and Exporting with a Legacy Source

- bundle_id: `teststand`
- source_path: `importing-and-exporting-with-a-legacy-source.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/importing-and-exporting-with-a-legacy-source.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Importing and Exporting with a Legacy Source To use the Legacy Import/Export Properties tool in TestStand, you must add it to the Tools Menu. Complete the following steps to add the Legacy Import/Export Properties tool to the Tools Menu: Copy <TestStand>\Components\StepTypes\Database \LegacyImportEx

### Importing and Exporting with a Legacy Source

#### Importing and Exporting with a Legacy Source

To use the Legacy Import/Export Properties tool in TestStand, you must add it to the
Tools Menu. Complete the following steps to add the Legacy Import/Export Properties tool to
the Tools Menu:

1. Copy <TestStand>\Components\StepTypes\Database
\LegacyImportExportTool.ini to the <TestStandPublic>\Setup
\ToolMenusToInstall directory.
2. Restart TestStand.

Use the Legacy Import/Export Properties tool from the Tools Menu to export data to legacy
formats and to import data from legacy formats.

To use legacy source with the new Property Loader step, create an instance of the property
loader step in your sequence. In the Source Type, select one of the following legacy source
types:

- NI Legacy Tab Delimited Text (*.txt)
- NI Legacy Comma Delimited Text (*.csv)
- NI Legacy Excel File (*.xls)
- NI Legacy Database

The following features are not supported when using legacy sources in the new Property
Loader step:

- Using alias names
- Import status in Step.Result
- Import Sequence File Attributes, Sequence Attributes, Step Attributes and Sequence
Parameters
- Property Loader groups
- Override default column names for selected properties in database

Note

Parent topic:

Using the Property Loader Step Type

<!--NI_TOPIC bundle=teststand path=importing-data-to-non-existing-properties.html language=enus -->
## TOPIC 00447: Importing Data to Non-Existing Properties

- bundle_id: `teststand`
- source_path: `importing-data-to-non-existing-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/importing-data-to-non-existing-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Importing Data to Non-Existing Properties You can use the Property Selector step to import to a property which will be created during runtime or you can configure the Property Loader step to create non-existing properties. To import values to the non-existing properties, you can choose to perform on

### Importing Data to Non-Existing Properties

#### Importing Data to Non-Existing Properties

You can use the Property Selector step to import to a property which will be created during
runtime or you can configure the Property Loader step to create non-existing properties.

To import values to the non-existing properties, you can choose to perform one of the
following options:

Option 1: Make sure the property loader source contains the details about the non-existing
property and choose Import All Data from Source option.

Option 2: Make sure the property loader source has a group named Expressions that
contains the details about the non-existing properties. Use the Expressions group in the
property selector to specify the lookup of non-existing properties. The value of the expression
should be as follows:

- StationGlobals.<Lookup> - Specifies station global variable to import
- FileGlobals.<Lookup> - Specifies file global variable to import
- Sequence[‘<SequenceName>’].Locals.<Lookup> - Specifies sequence local to
import
- Sequence[‘<SequenceName>’].Parameters.<Lookup> - Specifies sequence
parameter to import
- Sequence[‘<SequenceName>’].Step[‘<UniqueStepId>’].<Lookup> -
Specifies the step variable to import

<Lookup> - Replace it with the lookup of the variable to import

<SequenceName> - Replace it with the name of the sequence under which the variable exists
to import

<UniqueStepId> - Replace it with the unique step id representing the step. Unique step id
should be calculated based on what is configured for Unique Step Id in the property loader
configuration.

Parent topic:

Using the Property Loader Step Type

<!--NI_TOPIC bundle=teststand path=improving-performance-for-creating-deployment.html language=enus -->
## TOPIC 00448: Improving Performance for Creating Deployments

- bundle_id: `teststand`
- source_path: `improving-performance-for-creating-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/improving-performance-for-creating-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following guidelines for reducing the time required to create a deployment: Divide the test system into multiple, smaller deployments to avoid rebuilding parts of the test system that have not changed. For example, if you include the TestStand Runtime and NI driver components in separat

### Improving Performance for Creating Deployments

Consider the following guidelines for reducing the time required to create a deployment:

- Divide the test system into multiple, smaller deployments to avoid rebuilding parts of the test
 system that have not changed. For example, if you include the TestStand Runtime
 and NI driver components in separate deployments, you do not have to redeploy
 those components until you install a new version of TestStand or a new version
 of the driver.
- Use the Components to Include option in the Drivers and Components dialog box to exclude drivers and components the test system does not use, such as unused LabVIEW Run-Time Engines.
- Enable the To minimize media prompts while building your installers, copy the
 selected installers and all future installers to this computer 
 option in the Drivers and Components dialog box to copy all necessary components
 from a deployment to a permanent location on the local computer before the
 deployment utility creates the deployment and to copy all NI deployable
 installers to a permanent location on the local computer when you run the
 installers.
- Ensure that you mass compile all the VIs in the version of LabVIEW the test system requires
 before you create a deployment. When you create a deployment, the TestStand
 Deployment Utility invokes LabVIEW to save copies of all VIs the test system
 uses. When saving a copy of a VI, LabVIEW automatically recompiles the VI in the
 following situations: Because compiling VIs can require a significant amount of time, NI
 recommends that you compile all the VIs at once instead of recompiling the same
 set of VIs each time you create a deployment.
  - The compiled code of the VI is out of date
  - The compiled code of the VI is saved in a different version of
 LabVIEW
  - The VI is a source-only VI, which is a VI with separate compiled code,
 and has not been compiled on the development computer
- Ensure that you disable the Check for Broken VIs options in the LabVIEW VI Options dialog box to prevent the deployment utility from checking for broken VIs before and after creating the deployable image.
- Use packed project libraries because the TestStand Deployment Utility can include a packed project library in the deployment without having to recompile any of the VIs the packed project library contains.
- If you call VIs in the context of multiple LabVIEW projects, enable the Consolidate Files Shared By Projects option in the LabVIEW VI Options dialog box to deploy the VIs in a single, merged source distribution when possible instead of using a source distribution for each LabVIEW project. This consolidation increases build speed and decreases disk usage for multiple projects that share common subVIs by making a single source distribution for every project. This optimization is not always possible because two projects might compile the same source VI differently, which can result in slower build times.
- If you are deploying VIs using a version of LabVIEW released after the current TestStand version, creating the first deployment takes longer because the deployment utility compiles all the files it requires in the newer version of LabVIEW. Creating subsequent deployments does not take as long.

Parent topic:

Deploying TestStand Systems

Related concepts:

- Choosing Single or Multiple Deployments
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Organizing LabVIEW-Based TestStand Systems

<!--NI_TOPIC bundle=teststand path=in-process-com-servers-support-in-32-bit-test.html language=enus -->
## TOPIC 00449: In-Process COM Servers Support in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `in-process-com-servers-support-in-32-bit-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/in-process-com-servers-support-in-32-bit-test.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In-process COM servers must match the bitness of TestStand. If both versions of the server are registered, TestStand automatically locates the correct server using Microsoft Windows registry redirection, and the ActiveX/COM Adapter step typically does not require modification. Use bitness-conditiona

### In-Process COM Servers Support in 32-bit TestStand and 64-bit TestStand

In-process COM servers must match the bitness of TestStand. If both versions of the server are registered, TestStand automatically locates the correct server using Microsoft Windows registry redirection, and the ActiveX/COM Adapter step typically does not require modification. Use bitness-conditional code with the ActiveX/COM Adapter when the 32-bit version and the 64-bit version of COM interfaces differ.

Parent topic:

ActiveX/COM Code Module Support for 64-bit TestStand

Related concepts:

- Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces

<!--NI_TOPIC bundle=teststand path=including-a-user-interface-in-a-deployment.html language=enus -->
## TOPIC 00450: Including a User Interface in a Deployment

- bundle_id: `teststand`
- source_path: `including-a-user-interface-in-a-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-a-user-interface-in-a-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must explicitly add user interface files to the deployment. If you are using a TestStand workspace to create a deployment, create a new project for the user interface that includes all the required files and add the user interface project to the workspace. If you are using a directory to create

### Including a User Interface in a Deployment

You must explicitly add user interface files to the deployment. If you are using a TestStand workspace to create a deployment, create a new project for the user interface that includes all the required files and add the user interface project to the workspace. If you are using a directory to create a deployment, ensure that the directory you use includes a copy of all the required user interface files.

Enable the Include Without Processing Item or Dependencies option in the File Properties section on the Distributed Files tab of the TestStand Deployment Utility for the user interface files for the deployment utility to include the user interface without modifications and without detecting dependencies because user interfaces and dependent files are designed to work together without modification.

#### Modifying the Built-In LabVIEW Simple or Full-Featured User Interface Examples

When you run the TestExec.exe build specification to generate an executable, LabVIEW prefixes VIs listed under the Dependencies node in the LabVIEW project with Simple UI — or Full UI — for the simple and full-featured user interfaces, respectively, to avoid name collisions. If you load any VI from the user interface by name, you must update the code that loads the VI to include VI prefixes.

Complete one of the following options for all dynamic calls listed under the Dependencies node, including VIs that you call from top-level files but that you have not explicitly added to the My Computer target in the LabVIEW project, to resolve this issue:

- Add the Simple UI — or Full UI — prefix to the path you pass to the Open VI Reference function when the caller VI runs in the LabVIEW RTE. You can use the Application:Kind property in LabVIEW to determine whether the VI is running in the development system or the LabVIEW RTE.
- Add the VIs listed under the Dependencies node to the My Computer target to prevent the name
 change when you build the executable. LabVIEW prefixes only the files listed
 under the Dependencies node. NI recommends that you prefix these VIs manually to
 avoid potential name collisions that might prevent the user interface from
 running VIs that have conflicting names.

Parent topic:

Including Source Components

Related concepts:

- Identifying Components to Deploy
- Using a TestStand Workspace File to Create a Deployment
- Distributing a User Interface
- Using a Directory to Create a Deployment
- Customizing Components You Deploy

<!--NI_TOPIC bundle=teststand path=including-additional-ni-installers-in-a-deplo.html language=enus -->
## TOPIC 00451: Including Additional NI Installers in a Deployment

- bundle_id: `teststand`
- source_path: `including-additional-ni-installers-in-a-deplo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-additional-ni-installers-in-a-deplo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends that you do not install a deployment that includes NI drivers or components on the build computer, which is the computer on which you are running the TestStand Deployment Utility to build a custom installer for deploying TestStand systems. If you have already installed a deployment on

### Including Additional NI Installers in a Deployment

NI recommends that you do not install a deployment that includes NI drivers or components on the
 build computer, which is the computer on which you are running the TestStand
 Deployment Utility to build a custom installer for deploying TestStand systems. If
 you have already installed a deployment on the build computer, NI recommends that
 you uninstall it. Use the NI Device Driver DVD that ships with TestStand, or a later
 version of the driver DVD, to reinstall the drivers/components you want to include
 in the custom installer the deployment utility builds.

If the version of the NI product installed on the build computer and on the test station computer do not match, the installer updates the test station computer with the version included in the installer. If the test station computer contains the later version, the installer does nothing.

If you choose to include drivers or components from a previous deployment in a TestStand installer, such as those the deployment utility builds, you might encounter the following problems:

- The custom installer is missing features —A custom installer that you build contains only those features that also have their dependencies installed on the build computer. For example, NI-DAQmx contains LabVIEW Real-Time drivers that depend on the LabVIEW Real-Time Module. If the LabVIEW Real-Time Module is not installed on the build computer, the custom installer will not contain the LabVIEW Real-Time drivers.
- The custom installer removes features from the test station computer —The test station computer contains a feature from an older NI product and that feature was not included in the installer. For example, NI-DAQmx 7.1 with the LabVIEW Real-Time Module is installed on the test station computer. The build computer has NI-DAQmx 8.0 without the LabVIEW Real-Time Module. The LabVIEW Real-Time drivers are removed from the test station computer because they depend on the LabVIEW Real-Time Module and the LabVIEW Real-Time Module was not included in the installer. NI-DAQmx 7.1 is also updated to NI-DAQmx 8.0. Therefore, a custom installer you build might uninstall components or features on the test station computer without reinstalling updated versions of those components. As part of the installation process, the installer launches a dialog box that lists what features the installer will uninstall and allows the user to continue or quit the installation.

Parent topic:

Including Source Components

Related concepts:

- Using a Dedicated Build Computer
- Calling VIs on Remote Computers

<!--NI_TOPIC bundle=teststand path=including-all-necessary-report-content.html language=enus -->
## TOPIC 00452: Including All Necessary Report Content

- bundle_id: `teststand`
- source_path: `including-all-necessary-report-content.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-all-necessary-report-content.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Test systems have different data logging requirements influenced by system-level requirements of storage for traceability or analysis and by the testing and debugging processes used. Each report format TestStand can generate contains different pieces of information. For example, the ASCII and HTML r

### Including All Necessary Report Content

Test systems have different data logging requirements influenced by system-level requirements of storage for traceability or analysis and by the testing and debugging processes used.

Each report format TestStand can generate contains different pieces of information. For example, the ASCII and HTML report formats contain only the step name, status, limits, limit comparison type, module time, and any additional results associated with the step. The TSR format contains all the information available in the ASCII and HTML formats and additional information, such as the parent step IDs of steps and the execution thread IDs.

Use the following categories to consider the set of data available in each report format:

- Minimal —Contains minimal context information, such as the station ID, user name, execution start date and time, overall status, and minimal step-related information (such as the step name, module time, measurement value, and limits and module time).
- Controlled —Contains all the information in a minimal report and information associated with a step, such as step ID.
- Moderate —Contains all the information in a controlled report and other information, such as the step type, step group, total step execution time, and report options.
- Complete —Contains all the information in a moderate report and other information, such as the parent step IDs and execution thread IDs. The ResultLogRecordTypes enumeration specifies the complete list of all data logged.

The following table summarizes how the built-in TestStand report formats correspond to these report type categories:

| Report Type | ASCII | ATML 6.01, 5.0, or 2.02 | ATML 6.01, 5.0, or 2.02 with Extensions | HTML | TSR | XML |
| --- | --- | --- | --- | --- | --- | --- |
| Minimal | ✓ | — | — | ✓ | — | — |
| Controlled | — | ✓ | — | — | — | — |
| Moderate | — | — | ✓ | — | — | ✓ |
| Complete | — | — | — | — | ✓ | — |

#### Recommended Report
 Options

The following table summarizes the recommended options you
 configure in the Report Options dialog box when you optimize for report
 content:

| Report Option | Value |
| --- | --- |
| Format | ATML, XML, TSR*, ASCII, HTML (best to worst) |
| Asynchronous | N/A |
| On-the-Fly Report | N/A |
| Only Display Latest Results | N/A |

Note

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for report content:

- Maximize test system throughput
- Minimize report file size
- Interoperate with other processes and systems

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Maximizing Test System Throughput
- Minimizing Report File Size
- Interoperating with Other Processes and Systems
- Customizing the ATML Test Results Report Generator

<!--NI_TOPIC bundle=teststand path=including-and-excluding-files-in-msi-based-in.html language=enus -->
## TOPIC 00453: Including and Excluding Files in MSI-based Installer Patches

- bundle_id: `teststand`
- source_path: `including-and-excluding-files-in-msi-based-in.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-and-excluding-files-in-msi-based-in.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`

### Including and Excluding Files in MSI-based
 Installer Patches

- [Adding New Files to a Patch Deployment](adding-new-files-to-a-patch-deployment.html)
- [Including Modified Files in a Patch Deployment](including-modified-files-in-a-patch-deploymen.html)
- [Including Unmodified Files in a Patch Deployment](including-unmodified-files-in-a-patch-deploym.html)
- [Including NI Drivers or the TestStand Runtime in a Patch Deployment and Installer](including-ni-drivers-or-the-teststand-runtime.html)
- [Excluding New or Modified Files from a Patch Deployment](excluding-new-or-modified-files-from-a-patch.html)
- [Differences between Standard Mode and Manual Mode](differences-between-standard-mode-and-manual.html)

Parent topic:

Patching Deployments

<!--NI_TOPIC bundle=teststand path=including-binary-strings-in-reports.html language=enus -->
## TOPIC 00454: Including Binary Strings in Reports

- bundle_id: `teststand`
- source_path: `including-binary-strings-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-binary-strings-in-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Typically, you cannot store binary data in a string since strings cannot contain zero bytes, and strings must not contain invalid multibyte character set (MBCS) sequences. However, the TestStand LabVIEW Adapter and the TestStand API function SetValBinary support assigning binary values to string var

### Including Binary Strings in Reports

Typically, you cannot store binary data in a string since strings cannot contain zero bytes, and strings must not contain invalid multibyte character set (MBCS) sequences. However, the TestStand LabVIEW Adapter and the TestStand API function SetValBinary support assigning binary values to string variables or properties. TestStand stores binary string values as compressed and encoded binary data using only printable non-MBCS-lead-byte characters.

The default TestStand report generator process model plug-in generates the binary string values in the compressed encoded formats. See the Retrieving Binary String Values from Reports and Databases topic for more information about retrieving binary data from string values.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- Retrieving Binary String Values from Reports and Databases

<!--NI_TOPIC bundle=teststand path=including-files-from-the-teststand-public-dir.html language=enus -->
## TOPIC 00455: Including Files from the TestStand Public Directory in a Deployment

- bundle_id: `teststand`
- source_path: `including-files-from-the-teststand-public-dir.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-files-from-the-teststand-public-dir.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public> directory contains TestStand components you customize and copies of the TestStand User Interfaces. Enable the From TestStand Public Directories option in the Deploy Files section on the System Source tab of the TestStand Deployment Utility to include these files in a deploymen

### Including Files from the TestStand Public Directory in a Deployment

The <TestStand Public> directory contains TestStand components you customize and copies of the TestStand User Interfaces. Enable the From TestStand Public Directories option in the Deploy Files section on the System Source tab of the TestStand Deployment Utility to include these files in a deployment. If the Distributed Files list on the Distributed Files tab includes files you do not want to include in the deployment, remove the checkmark next to the file or directory you want to exclude from the deployable image in the View Source or View Build Preview view.

Parent topic:

Including Source Components

Related concepts:

- TestStand Directory Structure
- User Components

<!--NI_TOPIC bundle=teststand path=including-hardware-configuration-information.html language=enus -->
## TOPIC 00456: Including Hardware Configuration Information in a Deployment

- bundle_id: `teststand`
- source_path: `including-hardware-configuration-information.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-hardware-configuration-information.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the test system includes NI hardware devices, include the configuration information from Measurement & Automation Explorer (MAX) in the installer you build with the TestStand Deployment Utility for the test system to execute correctly on the test station computer. Examples of the types of configu

### Including Hardware Configuration Information in a Deployment

If the test system includes NI hardware devices, include the configuration information from
 Measurement & Automation Explorer (MAX) in the installer you build with the
 TestStand Deployment Utility for the test system to execute correctly on the test
 station computer. Examples of the types of configuration information you can export
 include NI-VISA aliases, DAQ device settings, virtual channels, IVI Logical Names,
 IVI Driver Sessions, NI Switch Executive Virtual Devices, and DAQ tasks you define
 in MAX.

Enable the Include Hardware Configuration from Measurement & Automation Explorer option the Drivers and Components dialog box and enter or browse to the existing NI Configuration Export File (.nce) you want to include in the deployment. You can also click the New button to launch the Configuration Export Wizard, which you can use to create a new .nce file. After you run the installer and reboot the test station computer, MAX imports the hardware configuration information from the .nce file after users log in to the test station computer.

Use the Measurement & Automation Explorer Import Options control in the Drivers and Components dialog box to specify how to merge the configuration information you include in the deployment with the configuration data defined in MAX on the test station computer.

Enable the Display Dialog During Import option in the Drivers and Components dialog box to launch a MAX dialog box during the installation process so users can monitor the installation and respond to prompts if necessary.

Note

ni.com

Parent topic:

Including Source Components

<!--NI_TOPIC bundle=teststand path=including-hyperlinks-in-a-report-tdms-file.html language=enus -->
## TOPIC 00457: Including Hyperlinks in a Report - TDMS File

- bundle_id: `teststand`
- source_path: `including-hyperlinks-in-a-report-tdms-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-hyperlinks-in-a-report-tdms-file.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the NI_TDMSReference and Path data types to include hyperlinks to files in reports TestStand generates. Example File Location <TestStand Public>\Examples\Customizing Result Processing\Including Hyperlinks in a Report\Including Hyperlinks in a Report - TDM

### Including Hyperlinks in a Report - TDMS File

#### Purpose

This example demonstrates how to use the NI_TDMSReference and Path data types to include hyperlinks to files in reports TestStand generates.

#### Example File
 Location

<TestStand
 Public>\Examples\Customizing Result Processing\Including
 Hyperlinks in a Report\Including Hyperlinks in a Report - TDMS
 File.seq

#### Highlighted Features

- NI_TDMSReference data type
- Path data type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to use this example.

1. Select the Provide links to TDMS file and Image in the generated report step. This step adds the TDMSRef and ImagePath variables to the ResultList using the Additional Results feature.
2. Select Execute»Single Pass .
3. When the execution completes, review the report, which contains links to the TDMS file and the image. Text reports do not include hyperlinks.
4. Click the links to open the corresponding files. TestStand uses the default application you specify for the file format to open the file when you click the link in the report.

Parent topic:

Examples for Customizing Result Processing

Related concepts:

- NI_TDMSReference
- Path
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=including-hyperlinks-in-a-report.html language=enus -->
## TOPIC 00458: Including Hyperlinks in a Report

- bundle_id: `teststand`
- source_path: `including-hyperlinks-in-a-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-hyperlinks-in-a-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to include hyperlinks in reports that TestStand generates. You can use the Path type, with the attribute TestStand.Hyperlink set to True, to convert any path displayed in the report to a hyperlink. Example File Location <TestStand Public>\Examples\Customizing Re

### Including Hyperlinks in a Report

#### Purpose

This example demonstrates how to include hyperlinks in reports that TestStand generates. You can use the Path type, with the attribute TestStand.Hyperlink set to True, to convert any path displayed in the report to a hyperlink.

#### Example File
 Location

<TestStand
 Public>\Examples\Customizing Result Processing\Including
 Hyperlinks in a Report\Including Hyperlinks in a
 Report.seq

#### Highlighted Features

Path data type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example.

1. To link to an image, select the Create a link to an image on disk step. This step stores an image path in a local variable and adds this variable to the report as an additional result. This data must be stored in a TestStand property before logging so that the hyperlink attribute can be set to True for the property. Click Edit Attributes next to the local variables to view this attribute.
2. To link to a web page, select the Create a link to a webpage step. This step stores a URL in a local variable and adds this variable to the report as an additional result.
3. Select the CPU Test step. If this step fails, an additional result is logged to link to an HTML file that contains troubleshooting instructions for the operator.
4. Select Execute»Single Pass .
5. When the execution completes, review the report, which contains links to the image, web page, and local HTML file.
6. Click the links to open the corresponding locations.

Parent topic:

Examples for Customizing Result Processing

Related concepts:

- TestStand Directory Structure
- Path

<!--NI_TOPIC bundle=teststand path=including-hyperlinks-in-reports.html language=enus -->
## TOPIC 00459: Including Hyperlinks in Reports

- bundle_id: `teststand`
- source_path: `including-hyperlinks-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-hyperlinks-in-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can include hyperlinks in supported versions of ATML, XML, and HTML reports. TestStand uses the default application you specify for the file format to open the file when you click the link in the report. The web browser returns an error when you click a link for which the file has been moved or

### Including Hyperlinks in Reports

You can include hyperlinks in supported versions of ATML, XML, and HTML reports. TestStand uses the default application you specify for the file format to open the file when you click the link in the report. The web browser returns an error when you click a link for which the file has been moved or no longer exists.

Complete the following steps to create a hyperlink in a report.

1. Create a local variable with a data type of Path.
2. Use the absolute path to the file for which you want to include a link in the report as the value of the variable.
3. Create a container attribute named TestStand .
4. Create a Boolean attribute named Hyperlink in the TestStand container attribute.
5. Set the value of the Hyperlink attribute to True to include a link to the file in the report. If the value of the Hyperlink attribute is False , the report displays the path as a string, not a link.
6. Log the variable in the report.

Note

TestStand

Hyperlink

When you use the XML Packaging Utility to distribute ATML, XML, and HTML reports that include links, the utility also distributes the target file of the link.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- Path
- Including Hyperlinks in a Report - TDMS File

<!--NI_TOPIC bundle=teststand path=including-modified-files-in-a-patch-deploymen.html language=enus -->
## TOPIC 00460: Including Modified Files in a Patch Deployment

- bundle_id: `teststand`
- source_path: `including-modified-files-in-a-patch-deploymen.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-modified-files-in-a-patch-deploymen.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Deployment Utility automatically includes modified files in a patch deployment. When you create a full deployment, the deployment utility stores checksums for each file in the deployment specification file (.tsd). When you create a patch deployment, the deployment utility completes the

### Including Modified Files in a Patch Deployment

The TestStand Deployment Utility automatically includes modified files in a patch deployment. When you create a full deployment, the deployment utility stores checksums for each file in the deployment specification file (.tsd).

When you create a patch deployment, the deployment utility completes the following tasks:

1. Creates a temporary full deployable image.
2. Compares the new file checksums to the previous file checksums stored in the .tsd file to identify modified files.
3. Includes the modified files in the patch deployable image.

Note

Parent topic:

Including and Excluding Files in MSI-based Installer Patches

Related concepts:

- Creating a Deployable Image

<!--NI_TOPIC bundle=teststand path=including-ni-drivers-or-the-teststand-runtime.html language=enus -->
## TOPIC 00461: Including NI Drivers or the TestStand Runtime in a Patch Deployment and Installer

- bundle_id: `teststand`
- source_path: `including-ni-drivers-or-the-teststand-runtime.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-ni-drivers-or-the-teststand-runtime.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Upgrades and Patches to Include option on the Mode tab of the TestStand Deployment Utility to include or exclude updates to NI drivers or the TestStand Runtime included in the full deployment installer in an installer for a patch deployment. To add additional NI drivers or TestStand Runtime

### Including NI Drivers or the TestStand Runtime
 in a Patch Deployment and Installer

Use the Upgrades and Patches to Include option on the Mode tab of the TestStand Deployment
 Utility to include or exclude updates to NI drivers or the TestStand Runtime
 included in the full deployment installer in an installer for a patch deployment. To
 add additional NI drivers or TestStand Runtime components to the patch deployment
 installer, use the Installer Options tab of the deployment utility and click the
 Drivers and Components button to launch the Drivers and
 Components dialog box and select the additional components.

Note

Parent topic:

Including and Excluding Files in MSI-based Installer Patches

<!--NI_TOPIC bundle=teststand path=including-source-components.html language=enus -->
## TOPIC 00462: Including Source Components

- bundle_id: `teststand`
- source_path: `including-source-components.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-source-components.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following tasks before you use a TestStand workspace file or directory to create a deployment: Determine whether you will use multiple deployments to simplify future upgrades Identify the components to deploy, including files from the <TestStand Public> directory, a user interface and s

### Including Source Components

Complete the following tasks before you use a TestStand workspace file or directory to create a deployment:

- Determine whether you will use multiple deployments to simplify future upgrades
- Identify the components to deploy, including files from the <TestStand
 Public> directory, a user interface and supporting files,
 TestStand configuration files, and NI hardware configuration information
- Prepare the components for deployment

Parent topic:

Creating Deployments

Related concepts:

- Using a TestStand Workspace File to Create a Deployment
- Using a Directory to Create a Deployment
- Choosing Single or Multiple Deployments
- Identifying Components to Deploy
- Including Files from the TestStand Public Directory in a Deployment
- Including a User Interface in a Deployment
- Including TestStand Configuration Files in a Deployment
- Including Hardware Configuration Information in a Deployment
- Preparing Source Components for Deployment

<!--NI_TOPIC bundle=teststand path=including-teststand-configuration-files-in-a.html language=enus -->
## TOPIC 00463: Including TestStand Configuration Files in a Deployment

- bundle_id: `teststand`
- source_path: `including-teststand-configuration-files-in-a.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-teststand-configuration-files-in-a.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must explicitly add configuration files to the deployment by adding the files to a workspace or by ensuring that the directory you use to create the deployment includes a copy of the configuration files. If you deploy to a test station computer a configuration file that is different from the con

### Including TestStand Configuration Files in a Deployment

You must explicitly add configuration
 files to the deployment by adding the files to a workspace or by ensuring that the
 directory you use to create the deployment includes a copy of the configuration
 files.

If you deploy to a test station computer a configuration file that is
 different from the configuration file you use on a development computer or if you
 deploy a configuration file from a directory other than the <TestStand
 Application Data>\Cfg directory, use the Installation Destination and Installation
 Destination Subdirectory options in the Installer Properties section on the
 Distributed Files tab of the TestStand Deployment Utility to change the installation
 destination of the configuration file.

Parent topic:

Including Source Components

<!--NI_TOPIC bundle=teststand path=including-unmodified-files-in-a-patch-deploym.html language=enus -->
## TOPIC 00464: Including Unmodified Files in a Patch Deployment

- bundle_id: `teststand`
- source_path: `including-unmodified-files-in-a-patch-deploym.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/including-unmodified-files-in-a-patch-deploym.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to include unmodified files in a patch deployment. Select the file in the Distributed Files section of the Distributed Files tab of the TestStand Deployment Utility. Select Included in the File Status control of the File Properties tab. Selecting the Included option alwa

### Including Unmodified Files in a Patch Deployment

Complete the following steps to include unmodified files in a patch deployment.

1. Select the file in the Distributed Files section of the Distributed Files tab of the TestStand Deployment Utility.
2. Select Included in the File Status control of the File Properties tab.

Selecting the Included option always includes the file in the patch deployment, even if the file is unmodified. Use this technique to return a file that might have been modified on a test station computer to a known state or to set installer properties, such as registering an ActiveX Automation server or creating a new program item.

Note

Parent topic:

Including and Excluding Files in MSI-based Installer Patches

<!--NI_TOPIC bundle=teststand path=information-source-connections.html language=enus -->
## TOPIC 00465: Information Source Connections

- bundle_id: `teststand`
- source_path: `information-source-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/information-source-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use manager controls to establish caption, image, and numeric value information source connections to Label controls, ExpressionEdit controls, and StatusBar panes to display information about the state of the application.

### Information Source Connections

You can use manager controls to establish caption, image, and numeric value information source connections to Label controls, ExpressionEdit controls, and StatusBar panes to display information about the state of the application.

Parent topic:

Connecting Manager Controls to Visible Controls

Related concepts:

- Manager Controls
- Caption Connections
- Image Connections
- Numeric Value Connections

<!--NI_TOPIC bundle=teststand path=initialize-with-options.html language=enus -->
## TOPIC 00466: Initialize with Options

- bundle_id: `teststand`
- source_path: `initialize-with-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/initialize-with-options.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An option string configures the IVI driver features of state caching, range checking, simulation, status checking, and record value coercions. For instrument drivers that support a family of instruments, you can use the DriverSetup option string to set the particular model of instrument you want the

### Initialize with Options

An option string configures the IVI driver features of state caching, range checking, simulation, status checking, and record value coercions. For instrument drivers that support a family of instruments, you can use the DriverSetup option string to set the particular model of instrument you want the driver to emulate. The IVI Engine then uses the option string settings when it runs the test application.

To enable an IVI feature, set the value to 1 in the option string. To disable a feature, set the value to 0. You do not have to specify all the properties. If you do not specify one of the properties, the session uses the default value. If you pass NULL or an empty string for the options parameter, the session uses the default values for the properties.

The following table lists IVI driver features, the corresponding strings for the option string, and the default value setting for each feature. The IVI Engine uses these default values when you do not name a feature in the option string. A comma separates each option you specify.

| Feature Option | String | Default Value | Default State |
| --- | --- | --- | --- |
| State Caching | Cache | 1 | Enabled |
| Range Checking | RangeCheck | 1 | Enabled |
| Simulation | Simulate | 0 | Disabled |
| Status Checking | QueryInstrStatus | 1 | Enabled |
| Record Value Coercions | RecordCoercions | 0 | Disabled |
| NI I/O TraceNI I/O Trace is an application that monitors, records, and displays National Instruments API calls made by applications. | Spy | 0 | Disabled |
| Interchangeability CheckingInterchangeability checking verifies that the program produces the same behavior when you use it with a different instrument. | InterchangeCheck | 0 | Disabled |
| Specific Instrument ControlUse the DriverSetup option to specify a specific model of an instrument you want to control. | DriverSetup | "" | "" |

For example, the option string: "Simulate=0, RangeCheck=1, QueryInstrStatus=1, Cache=1, Spy=1, InterchangeCheck=0, DriverSetup = Model:6652A" results in the following configuration:

- Instrument simulation is disabled
- Range checking is enabled
- Status checking is enabled
- State caching is enabled
- Recording of coercions of values is disabled
- NI I/O Trace is enabled
- InterchangeCheck is disabled
- Control of the HP 6652A model

Refer to the IVI Driver Help for more information about IVI driver feature options.

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=initialselection-subproperties.html language=enus -->
## TOPIC 00467: InitialSelection Subproperties

- bundle_id: `teststand`
- source_path: `initialselection-subproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/initialselection-subproperties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RunState.InitialSelection subproperty specifies the set of properties, steps, and sequences, as well as the file or execution that is selected or active when you start a new execution. The TestStand Sequence Editor automatically specifies the appropriate subproperties of InitialSelection when th

### InitialSelection Subproperties

The RunState.InitialSelection subproperty specifies the set of properties, steps, and sequences, as well as the file or execution that is selected or active when you start a new execution. The TestStand Sequence Editor automatically specifies the appropriate subproperties of InitialSelection when the Station Global, Sequence File, and Execution windows are active. You usually use this property in sequences that custom Tools menu commands or Process Model entry points call.

| Sequence Context Subproperty | Description |
| --- | --- |
| SelectedSteps | Contains an array of Step objects selected when the execution started. The array is empty for non-root sequence contexts. When the Steps pane of an Execution window is initially active, the array contains execution versions of the Step objects. |
| SelectedPropertyObjects | Contains an array of PropertyObject objects selected when the execution started. When a sequence file is initially active, the array contains subproperties of a Step object, local variable, file global variable, or station global variable. When the Variables pane of an Execution window is initially active, the array contains the currently selected properties. The array is empty for non-root sequence contexts. |
| SelectedSequences | Contains an array of Sequence objects selected when the execution started. The array is empty for non-root sequence contexts. When the Steps tab of an Execution window is initially active, the array contains execution versions of the Sequence objects. |
| SelectedStepGroupByIndex | Contains the index of the step group selected when the execution started. The index values are as follows: 0—Setup step group 1—Main step group 2—Cleanup step group This property exists only in the root sequence context. |
| SelectedFile | Specifies the SequenceFile object for the active sequence file when the execution started. This property exists only in the root sequence context when a sequence file is initially active, or when the Steps pane of an Execution window is initially active. |
| SelectedPropertyObjectFile | Specifies the PropertyObjectFile object for the active file when the execution started. When a sequence file is initially active, this property is identical to SelectedFile. This property exists only in the root sequence context when a Sequence File window is initially active, or when the Steps pane of an Execution window is initially active. |
| SelectedExecution | When you select an existing Execution window and start a new execution, this property specifies the Execution object for the existing execution the window shows. This property exists only in the root sequence context when an Execution window is initially active. |

Parent topic:

RunState Subproperties

<!--NI_TOPIC bundle=teststand path=installer-issues-for-32-bit-teststand-and-64.html language=enus -->
## TOPIC 00468: Installer Issues for 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `installer-issues-for-32-bit-teststand-and-64.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/installer-issues-for-32-bit-teststand-and-64.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends creating a separate installer for the 32-bit version of a test system and for the 64-bit version of a test system. If you use the deployment utility to build an installer that includes the TestStand Runtime, the utility also includes dependent runtimes if any are necessary. Installers

### Installer Issues for 32-bit TestStand and 64-bit TestStand

NI recommends creating a separate installer for the 32-bit version of a test system and for
 the 64-bit version of a test system. If you use the deployment utility to build an installer
 that includes the TestStand Runtime, the utility also includes dependent runtimes if any are
 necessary.

Installers you build with the deployment utility install files to different directories depending on the bitness of the deployment utility you used to build the installer, as shown in the following table.

| Destination | 32-bit Directory | 64-bit Directory |
| --- | --- | --- |
| TestStand directory | 32-bit TestStand directory | 64-bit TestStand directory |
| Program Files | 32-bit operating system: Program Files64-bit operating system: Program Files x86 | 64-bit operating system: Program Files |
| National Instruments directory | 32-bit National Instruments directory | 64-bit National Instruments directory |
| TestStand Public directory | 32-bit TestStand Public directory | 64-bit TestStand Public directory |
| TestStand Application Data directory | 32-bit TestStand Application Data directory | 64-bit TestStand Application Data directory |
| System WOW64 directory | N/A | <Windows>\\SysWOW64 |

Note

System32

SysWOW64

System32

SysWOW64

Parent topic:

Deploying 32-bit TestStand and 64-bit TestStand Systems

<!--NI_TOPIC bundle=teststand path=installing-teststand.html language=enus -->
## TOPIC 00469: Installing TestStand

- bundle_id: `teststand`
- source_path: `installing-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/installing-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Consider the following conditions when installing TestStand on your system: The default TestStand installation location is <Program Files>\National Instruments\TestStand <Version Year>. You can install TestStand on a computer which has a previous TestStand version installed, but you cannot install T

### Installing TestStand

- The default TestStand installation location is <Program
 Files>\National Instruments\TestStand <Version Year> .
- You can install TestStand on a computer which has a previous TestStand version
 installed, but you cannot install TestStand over a previous version and cannot
 install TestStand in the default installation directory for a previous version.
 If you installed a previous version of TestStand in a non-default directory, you
 can uninstall the previous version of TestStand and install the new version of
 TestStand to that directory.
- You cannot install TestStand to a network path or a mapped network path. You
 must install TestStand on a local computer.
- If you uninstall one bitness of a TestStand version, NI recommends that you use
 the TestStand Version Selector to reactivate the remaining bitness of that
 version and launch TestStand to properly register its components. For example,
 if you uninstall TestStand 2023 Q4 64-bit, use the TestStand Version Selector to
 set TestStand 2023 Q4 32-bit to active and launch TestStand to properly register
 your remaining version of TestStand 2023 Q4.

1. Download the TestStand installer. 
 Note If you purchased this
 product with an NI Software Suite or NI Product Bundle, use the installation
 media that shipped with your purchase to install this product.
2. Run the TestStand installer and follow instructions to select your desired
 software components and install them. Consider the following information for
 unique installation configurations: 
 To install only TestStand Runtime on a machine, deselect all optional
 products by clicking Deselect All on the
 Select tab. You cannot automate the
 installation of TestStand Runtime in NI Package Manager using the
 command line. To automate the installation of TestStand Runtime, you
 must create a custom installer using NI Package Builder.
 The TestStand GraphControl and
 IVIStepTypes packages are available in the
 TestStand offline installer for manual or automatic installation using
 NI Package Manager. These packages can be included in custom installers
 built using NI Package Builder.
 TestStand can use newer versions of the LabVIEW Runtime Engine (RTE)
 when you install LabVIEW on a development system. You can include newer
 versions of the LabVIEW RTE in deployments using the Drivers
 and Components dialog box of the TestStand Deployment
 Utility. 
 Note NI Package Manager is
 required to install TestStand. The installer will install NI Package Manager
 first if it is not present on your machine.
3. Reboot your system once the installation is complete.

- Log in to your NI user account to check for associated licenses
- Enter the serial number on the Certificate of Ownership included with your
 TestStand software kit
- Enter an activation code
- Connect to a volume license server

Related concepts:

- TestStand User Manual

Related information:

- Download TestStand
- NI Package Manager Manual
- Downloading Individual Offline Installers for NI Software
- NI Package Builder Manual
- Activating Software
- License Setup and Activation

<!--NI_TOPIC bundle=teststand path=instrument-control-step-types.html language=enus -->
## TOPIC 00470: Instrument Control Step Types

- bundle_id: `teststand`
- source_path: `instrument-control-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrument-control-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to implement a TestStand HP34401a instrument control step type in LabWindows/CVI. You can use the step type to access commonly-used functionality of the HP34401a multimeter from a TestStand sequence. Example File Location <TestStand Public>\Examples\Interfacing

### Instrument Control Step Types

#### Purpose

This example
 demonstrates how to implement a TestStand HP34401a instrument control step type in
 LabWindows/CVI. You can use the step type to access commonly-used functionality of
 the HP34401a multimeter from a TestStand sequence.

#### Example File
 Location

<TestStand Public>\Examples\Interfacing with
 Hardware\Instrument Control Step Types - HP34401a\Instrument Control Step Types
 - HP34401a.seq

#### Highlighted
 Features

TestStand step types

#### Major API

N/A

#### Prerequisites

You must
 install the HP34401a IVI instrument driver from the Instrument Driver Network at
 ni.com/devzone/idnet before running this
 example.

Note

#### How to Use This
 Example

This example demonstrates optional features you can include in
 step types you create. You can decide which, if any, of the following features to
 support in step types you create:

- Tabbed editing dialog box
- Multiple selectable run-time operations
- Configuration settings you can specify with TestStand expressions
- Groups of configuration settings you can load or save to a TestStand custom data
 type, which you can then execute according to a group of settings you store in a
 local variable or receive as a sequence parameter
- Instrument driver session obtained from the Session Manager to maximize the
 sharing of the instrument handle between steps and other code modules
- Multiple language string support

#### Installation Issues

Step
 types might depend on files such as code modules, icon files, or string resource
 files. For TestStand to locate these files, the files must reside in specific
 directories.

- Code Module Files (.dll, .vi, and so on) —Place step type
 code module files in a subdirectory you create in the <TestStand
 Public>\Components\StepTypes directory. TestStand finds code
 modules you place in this directory because the TestStand default search paths
 include all directories under the <TestStand
 Public>\Components directory. Although this example does not
 install its code module, HP34401aStepType.dll , to the
 <TestStand Public>\Components directory,
 TestStand can find the step type code module because the step type specifies a
 relative path from the <TestStand Public>\Examples\Interfacing
 with Hardware\Instrument Control Step Types - HP34401a 
 directory.
- Icon Files —Place icon files for step types in the
 <TestStand Public>\Components\Icons directory.
 TestStand loads icons from this directory and the
 <TestStand>\Components\Icons directory. TestStand
 installs the icon for this example to <TestStand
 Public>\Components\Icons\NI_Examples\Example_HP34401a.ico .
- String Resource Files —Place string resource files you
 create in the <TestStand
 Public>\Components\Language\<language>\TestStandExamples.ini 
 file.

The HP34401a_StepTypeExample.seq example sequence file
 contains the example step type definition. You can store step type definitions you
 create in any sequence file, and you can add a step type to a new or existing
 TestStand type palette file. You can install a type palette file on another computer
 by placing the file in the <TestStand
 Public>\Components\TypePalettes directory. You must prefix the
 filenames of the type palettes you install with Install_. At
 startup, TestStand searches the TypePalettes directory for type
 palette files with the Install_ prefix. When TestStand finds a
 palette file to install and the base filename is not the same as any existing
 palette file, TestStand removes the Install_ prefix and adds
 the palette to the palette list. When TestStand finds a palette file to install and
 the base filename is the same as an existing palette file, TestStand merges the
 types from the Install_ prefixed file with the existing palette
 file and deletes the Install_ file.

#### Step Type
 Implementation

Complete the following steps to implement a step
 type.

1. Create a new step type in the Types window. The example step type is named
 HP34401aStepType, which you can view in the Types window for the
 Instrument Control Step Types - HP34401a.seq file.
2. Determine the data requirements for the step. Analyze the data inputs and
 outputs the step requires at run time.
3. Create input properties. Create a step subproperty for each data input. Select
 the appropriate data type and set the default value. The example step type uses
 the following data input properties:
 Step.LogicalName Step.Operation Step.SettingSource Step.Configuration.MeasFunction Step.Configuration.Range Step.Configuration.ACMinFreq Step.Configuration.ACMaxFreq Step.Configuration.Resolution Step.Configuration.TriggerSource Step.Configuration.TriggerDelay Step.Read.Dest Step.Read.Timeout Step.SelfTest.Dest Step.SelfTest.Message
4. Create output properties. Create a step subproperty for each data output. If you
 want an output property to automatically appear in the sequence result list,
 create the output property under the Step.Result property.
 The example step type uses the following data output properties:
 Step.Read.Dest Step.SelfTest.Dest Step.Result.SinglePoint Step.Result.SinglePoint.Type Step.Result.SinglePoint.Channel Step.Result.SinglePoint.Measurement
5. Designate an adapter, if appropriate. If the step is not designed to call
 user-written code, enable the Designate an Adapter option
 on the General tab of the Step Type Properties dialog box and select the
 <None> Adapter. The example step type does not require you to write any
 code to access the instrument. Thus, the example step type designates the
 <None> Adapter as the appropriate module adapter.
6. Define run-time functionality. Create a Pre- or Post-Step substep to call a code
 module you write. Each instance of the step type calls the code module when the
 step executes. The code module call is transparent to the user. If the step type
 calls user-written code, define a Pre- or Post-Step substep, depending on
 whether you want to call the code module before or after the step executes. If
 the step type does not call user-written code, you can use a Pre- or Post-Step
 substep to call the code module. The example step type defines a Post-Step
 substep that calls the ExecuteHP34401aStep DLL function
 when an instance of the step type executes. The
 ExecuteHP34401aStep DLL function accepts a
 SequenceContext parameter, which the function uses
 with the TestStand API to access the properties of the step. You can also define
 the function to accept a separate parameter for each step property the function
 uses.
7. Define an editing dialog box. Configure the Edit substep to call a code module
 that launches the dialog box, which shows step property values in a controlled
 and organized manner. When the user finishes editing, the dialog box stores the
 edited property values in the step and marks the sequence file that contains the
 step as modified. The Edit substep for the example step type calls the
 EditHP34401aStep DLL function to launch a dialog box in
 which the user selects the action the step executes at run time and configures
 the parameters the action requires. The ExecuteHP34401aStep 
 DLL function accepts a SequenceContext parameter, which
 the function uses with the TestStand API to access the properties of the step.
 You can also define the function to accept a separate parameter for each step
 property the function uses.
8. Configure built-in step type properties. Use the Step Type Properties dialog box
 to configure the default values of built-in step type properties and other
 settings. Typically, you configure the following settings for a step type:
  - Designate an Icon —If the step does not call
 user-written code, select an icon that represents its functionality. You
 can select from the icon files in the <TestStand
 Public>\Components\Icons and
 <TestStand>\Components\Icons directories.
 If the step calls user-written code, do not designate an icon. The step
 displays the icon that represents the adapter that calls the
 user-written code. The example step type specifies
 <TestStand
 Public>\Components\Icons\NI_Examples\Example_HP34401a.ico 
 as its icon file.
  - Default Step Name Expression —The default step
 name expression determines the name the sequence editor assigns to a new
 instance of the step type. You can use the ResStr 
 expression function in the default name expression to specify a name
 that changes depending on the selected language. The example step type
 specifies the following expression as its default step name expression:
 ResStr("HP34401_STEP_TYPE_EXAMPLE",
 "DEFAULT_NAME") If the step type does not need to account
 for the selected language, you can enter a default step name in quotes,
 such as "HP34401a Step" .
  - Step Description Expression —The step description
 expression determines the description that Description column on the
 Steps pane and the Description control on the General panel of the
 Properties tab of the Step Settings pane show for the step. The
 description expression can refer to and show the values of step
 properties. You can use the ResStr expression
 function in the description expression to specify a description that
 changes depending on the selected language. The example step type uses a
 lengthy expression to vary the description depending on the step
 configuration and the selected language. If the step type description
 does not need to account for the step configuration or the selected
 language, you can enter a fixed description in quotes, such as
 "HP33401a DMM Instrument Control" .
  - Menu Item Name —Use the Item Name
 Expression control on the Menu tab of the Step Type
 Properties dialog box to specify the item name expression for the step
 type. The expression determines the name of the menu item in the Insert
 Step submenu that inserts an instance of the step type into a sequence.
 You can use the ResStr expression function in the
 item name expression to specify an item name that changes depending on
 the selected language. The example step type specifies the following
 item name expression: ResStr("HP34401_STEP_TYPE_EXAMPLE",
 "MENU_NAME") If the menu item does not need to account for
 the selected language, you can enter an item name in quotes, such as
 "HP34401a" .
  - Other Items —Depending on the step type, you can
 also use the following features. The example step type does not
 configure any other step type settings.
    - Configure the default values of built-in properties, such as the
 run options or loop options.
    - Use the Disable Properties tab of the Step Type Properties
 dialog box to prevent users of the step type from editing the
 values of built-in properties you select.
    - Specify code templates to assist the user in creating code
 modules that you designed the step type to call.

#### Suggestions for Implementing
 Instrument Control Step Types

To increase performance, do not initialize
 and close the instrument driver each time the step executes. Instead, use DLL global
 variables or another method to maintain the instrument instance between
 steps.

One option is to use the Session Manager to initialize and share
 instrument driver handles between multiple instances of the step type. The example
 step type obtains an instrument session from the Session Manager and attaches the
 instrument session to the current TestStand execution object by dynamically creating
 an ActiveX reference subproperty. In this way, the driver for the session stays open
 for the duration of the execution and all steps that can run during the execution
 share the same driver instance handle. You can also use the Session Manager to
 obtain a list of available instrument connections from which the step user can
 select.

To increase the flexibility of the step type, allow the user to
 specify the values of important settings with an expression. The user can then store
 the setting value in a variable and alter it at run time. The example step type
 allows the user to specify almost all setting values with an expression.

For
 groups of related settings, consider allowing the user to load or store the values
 in a variable of a custom data type that you define. The user can then specify a
 group of settings in a variable and pass the variable as a parameter to subsequences
 that contain the steps that apply the setting values. The example step type allows
 the user to specify a setting source variable to which the step loads or stores the
 settings for the selected operation.

#### Suggestions for Implementing Step
 Type Editing Dialog Boxes in LabWindows/CVI

The
 <TestStand>\API\CVI\TSUtil.fp instrument driver
 contains the following functions to help create a step type editing dialog
 box:

- If the text labels that appear on the step type editing dialog box must appear
 in the selected language, call the
 TS_LoadPanelResourceStrings function to load the
 language-specific dialog strings.
- Call the TS_StartModalDialog and
 TS_EndModalDialog functions to ensure that the editing
 dialog box is modal to the sequence editing application.
- Call the TS_ExprCtrl_Create function to convert a string
 control into an expression editing control.
- Call the TS_ExchangePropertyAndCtrlVals function to
 transfer values between step properties and dialog box controls.
- Call the TS_IncSequenceFileChangeCount function if the
 editing dialog box modifies the step.

Parent topic:

Examples for Interfacing with Hardware

Related concepts:

- TestStand Directory Structure
- Built-In Step Types
- Creating Custom Step Types

<!--NI_TOPIC bundle=teststand path=instrument-drivers.html language=enus -->
## TOPIC 00471: Instrument Drivers

- bundle_id: `teststand`
- source_path: `instrument-drivers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrument-drivers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Visit the Instrument Driver Network at ni.com/idnet for more information about instrument drivers and for finding and downloading instrument drivers compatible with National Instruments software.

### Instrument Drivers

Visit the Instrument Driver Network at ni.com/idnet for more
 information about instrument drivers and for finding and downloading instrument drivers
 compatible with National Instruments software.

- [IVI Drivers](ivi-drivers.html)
- [Plug and Play Instrument Drivers](plug-and-play-instrument-drivers.html)
- [Route Specification Strings](route-specification-strings.html)

Parent topic:

TestStand Tools and Utilities

Related information:

- NI Instrument Driver Network

<!--NI_TOPIC bundle=teststand path=instrument-session-categories.html language=enus -->
## TOPIC 00472: Instrument Session Categories

- bundle_id: `teststand`
- source_path: `instrument-session-categories.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrument-session-categories.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each type of instrument session has a category name. You can prefix a session name with a category to distinguish sessions of different types that might have the same name. Separate the category from the session name with any of the following separators: ::, \, \\, \/, /, //, /\, :, :\, :/, ://, :/\

### Instrument Session Categories

Each type of instrument session has a category name. You can prefix a session name with a category to distinguish sessions of different types that might have the same name. Separate the category from the session name with any of the following separators: ::, \, \\, \/, /, //, /\, :, :\, :/, ://, :/\, :\/, :\\.

If you query Session Manager for the available logical names and specify that you want Session Manager to prefix the categories to the names, Session Manager uses :: as the category separator.

Session types can have subcategories, but only IVI sessions support subcategories. The IVI session subcategories are the IVI class prefixes. You do not have to specify the IVI subcategory in a logical name. However, when querying for logical names, you might want to specify the subcategory to restrict the set of names Session Manager returns to those that represent instruments of a specific IVI class.

#### Example Categories

- Custom
- IVI
- IVI::IviDMM
- IviDMM
- SE
- VXIPNP
- VISA

#### Example Instrument Session Names with Categories

- Custom::MyInstrument
- IVI::SampleDMM
- IVI::IviDMM::SampleDMM
- IviDMM::SampleDMM
- SE::SwitchExecutiveExample
- VXIPNP::LCLSA
- VISA::ASLR1::INSTR

Note

Parent topic:

Session Manager

Related concepts:

- Instrument Session Types
- Instrument Session Names

<!--NI_TOPIC bundle=teststand path=instrument-session-name-configuration.html language=enus -->
## TOPIC 00473: Instrument Session Name Configuration

- bundle_id: `teststand`
- source_path: `instrument-session-name-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrument-session-name-configuration.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The location in which you configure instrument session names depends on the type of session. For IVI sessions, configure the logical and virtual instrument names using a utility, such as Measurement & Automation Explorer (MAX). You can use all the IVI aliases for a session, including logical names a

### Instrument Session Name Configuration

The location in which you configure instrument session names depends on the type of session.
For IVI sessions, configure the logical and virtual instrument names using a utility, such as Measurement & Automation Explorer (MAX).

You can use all the IVI aliases for a session, including logical names and the virtual instrument name, with or without the VInstr prefix. For example, for the same session, you might use SampleDMM, VInstr->FL45, or FL45.

Session Manager maintains VXIplug&play and VISA configuration information in the NISessionMgr.ini file, located in the <VXIplug&play directory>\WinNT or Win64 directory (for example, C:\<Program Files>\IVI Foundation\VISA\WinNT\NISessionMgr.ini). The NISessionMgr.ini file defines the VXIplug&play logical and virtual instrument names and the VISA logical names. Session Manager calls the VISA function viFindRsrc("?*INSTR") to obtain the list of VISA resource names.

If you change the NISessionMgr.ini file or the IVI settings in MAX, Session Manager loads the changes the next time you query for the available session names or request a new session object. The settings of an existing session object do not change when you alter a configuration file. If you release all references to a session and then request the same session, Session Manager recreates the session with the new configuration settings.

#### NISessionMgr.ini Configuration File

NISessionMgr.ini is a session manager, virtual instrument, or configuration file that you use to associate a hardware resource with a VXIplug&play driver and assign a virtual instrument name to the combination of the hardware resource and VXIplug&play driver. You can also use this file to assign logical names to VXIplug&play virtual instruments and VISA resources.

If the NISessionMgr.ini file does not exist, Session Manager automatically regenerates it by scanning the contents of the IVI Foundation\VISA directory to create a default entry for each installed VXIplug&play driver. The generated file uses the following format:

[VXIPNP Logical Names]

<logical name> = <virtual instrument name>

<another logical name> = <another virtual instrument name>

[VISA Logical Names]

<logical name> = <VISA resource name>

<another logical name> = <another VISA resource name>

Session Manager ignores VXIplug&play virtual instruments that do not specify all the following fields:

[VPPVInstr-><virtual instrument name>]

ModulePath = <dll path>

Prefix = <instrument prefix>

Resource = <VISA hardware resource>

IDQuery = <True or False>

Reset = <True or False>

The following list shows examples of VXIplug&play virtual instruments that might occur in the generated file:

[VXIPNP Logical Names]

DMM1 = "VPPVInstr->FlukeDMM"

[VISA Logical Names]

Serial1 = "ASRL1::INSTR"

[VPPVInstr->FlukeDMM]

ModulePath = "C:\Program Files\IVI Foundation\VISA\WinNT\Bin\fl45_32.dll"

Prefix = "FL45"

Resource = "GPIB::14::INSTR"

IDQuery = True

Reset = True

When Session Manager generates the NISessionMgr.ini file, each VXIplug&play virtual instrument resource tag is an empty string. You must edit the file to specify the resource for each virtual instrument. Session Manager ignores virtual instruments that do not specify a resource.

Use the following guidelines to edit the NISessionMgr.ini configuration file:

- Each virtual instrument name defaults to the instrument prefix.
- Edit the section name to rename a virtual instrument.
- You can copy existing sections to create new virtual instruments.
- Session Manager does not create any default logical names.

Note

NISessionMgr.ini

NISessionMgr.ini

[VInstr->FL45]

Reset = True

IDQuery = False

Refer to the NISessionMgr.ini file in the IVI Foundation\VISA\WinNT or Win64 directory for more information about the contents of this file.

Parent topic:

Session Manager

Related concepts:

- Instrument Session Types

<!--NI_TOPIC bundle=teststand path=instrument-session-names.html language=enus -->
## TOPIC 00474: Instrument Session Names

- bundle_id: `teststand`
- source_path: `instrument-session-names.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrument-session-names.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each instrument session has one or more names. You can use any of the names to obtain an instrument session reference from Session Manager. The names consist of the following elements: IVI or VXIplug&play session—Virtual instrument name and any number of logical names. A VISA session has a resource

### Instrument Session Names

Each instrument session has one or more names. You can use any of the names to obtain an instrument session reference from Session Manager. The names consist of the following elements:

- IVI or VXIplug&play session —Virtual instrument name and any number of logical names. A VISA session has a resource name and any number of logical names.
- IVI or VXIplug&play virtual instrument name —Refers to the combination of a software driver, a hardware resource, and a set of configuration options.
- IVI or VXIplug&play logical name —Alias for a particular IVI or VXI plug&play virtual instrument name.
- VISA resource name —Identifies a serial port, GPIB address, or other hardware resource. A VISA logical name is an alias for a particular VISA resource name.
- Switch Executive Virtual Device —Refers to an NI Switch Executive virtual instrument name defined in Measurement & Automation Explorer (MAX).

Note

#### Example Instrument Session Names with Categories:

| IVI::SampleScope | IVI logical name |
| --- | --- |
| IVI::Hpe1463a | IVI virtual instrument name |
| VXIPNP::Digital Test Instrument 1 | VXIplug&play logical name |
| VXIPNP::Term9 | VXIplug&play virtual instrument name |
| VISA::Serial Port 1 | VISA logical name |
| VISA::ASRL1::INSTR | VISA resource name |

Note

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=instrument-session-types.html language=enus -->
## TOPIC 00475: Instrument Session Types

- bundle_id: `teststand`
- source_path: `instrument-session-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrument-session-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Session Manager supports the following instrument session types: IVI Sessions—Use an IVI session to obtain the C-based instance handle for an IVI logical or virtual instrument name. NI Session Manager does not support IVI-COM drivers. VXIplug&play Sessions—Use a VXIplug&play session to obtain a C-

### Instrument Session Types

Session Manager supports the following instrument session types:

- IVI Sessions —Use an IVI session to obtain the C-based instance handle for an IVI logical or virtual instrument name. 

 Note 

 NI Session Manager does not support IVI-COM drivers.
- VXIplug&play Sessions —Use a VXI plug&play session to obtain a C-based instance handle for a VXI plug&play logical or virtual instrument name. Configure VXI plug&play names in the NISessionMgr.ini file located in the <VXIplug&play directory>\WinNT or Win64 directory (for example, C:\<Program Files>\IVI Foundation\VISA\WinNT\NISessionMgr.ini ).
- VISA Sessions —Use a VISA instrument session to obtain a C-based viSession handle for a VISA resource or logical name. Configure VISA logical names in the NISessionMgr.ini file located in the <VXIplug&play directory>\WinNT or Win64 directory (for example, C:\<Program Files>\IVI Foundation\VISA\WinNT\NISessionMgr.ini ).
- Custom Sessions —Use a custom session to create a data container object that shares ActiveX objects you create or other data among software components you write. Use the Attach and Get methods to attach data to and retrieve data from a session. A custom session does not initialize, close, or own an instrument handle. The data you share with a custom session does not have to be instrumentation related. You can create a custom session with any name you request.

 Note 

 Always prefix custom session names with CUSTOM::.
- SE Sessions —Use an NI Switch Executive session to obtain the C-based instance handle for a virtual device.

 Note 

 The handles you obtain for IVI, VXIplug&play, and VISA are occasionally referred to as sessions. The instrument sessions Session Manager creates are smart sessions that manage IVI, VXIplug&play, and VISA sessions.

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=instrument-sessions.html language=enus -->
## TOPIC 00476: Instrument Sessions

- bundle_id: `teststand`
- source_path: `instrument-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrument-sessions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Instrument sessions are ActiveX objects that enable software modules to share one of the following types of instrument API handles easily: An instance handle for an instrument driver, such as an IVI-C or VXIplug&play driver An ActiveX reference for an instrument driver, such as an IVI-C driver Ses

### Instrument Sessions

Instrument sessions are ActiveX objects that enable software modules to share one of the following types of instrument API handles easily:

- An instance handle for an instrument driver, such as an IVI-C or VXI plug&play driver
- An ActiveX reference for an instrument driver, such as an IVI-C driver
 
 Note 

 Session Manager does not support IVI-COM drivers.
- An instance handle or ActiveX reference for an I/O library object, such as a VISA session
- An instance handle for a virtual device the NI Switch Executive defines

You can use an instrument session to obtain a single instrument API handle or the same API handle multiple times in different software components. The instrument session initializes the API handle when you first request the handle and closes the handle when you release the last reference to the session. Typically, you do not explicitly initialize or close the instrument API handle.

During configuration, you assign each instrument session a unique name. To reference an instrument session, specify the unique name of the session.

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=instrumentstudio.html language=enus -->
## TOPIC 00477: InstrumentStudio

- bundle_id: `teststand`
- source_path: `instrumentstudio.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/instrumentstudio.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Interfacing with Hardware\InstrumentStudio directory contains the following examples.

### InstrumentStudio

The <TestStand
 Public>\Examples\Interfacing with
 Hardware\InstrumentStudio directory contains the following
 examples.

- [Measure Efficiency](measure-efficiency.html)
- [Measure Quiescent Current](measure-quiescent-current.html)

Parent topic:

Examples for Interfacing with Hardware

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=integrating-model-plug-ins-with-a-custom-proc.html language=enus -->
## TOPIC 00478: Integrating Model Plug-ins with a Custom Process Model

- bundle_id: `teststand`
- source_path: `integrating-model-plug-ins-with-a-custom-proc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/integrating-model-plug-ins-with-a-custom-proc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Process models invoke model plug-in entry points at run time by calling the sequence with the corresponding name from ModelSupport.seq. For example, calling the Model Plugins – Pre UUT sequence in ModelSupport.seq invokes the Model Plugin – Pre UUT entry point in all enabled plug-in instances. Calli

### Integrating Model Plug-ins with a Custom Process Model

Process models invoke model plug-in entry points at run time by calling the sequence with the corresponding name from ModelSupport.seq. For example, calling the Model Plugins – Pre UUT sequence in ModelSupport.seq invokes the Model Plugin – Pre UUT entry point in all enabled plug-in instances. Calling the Model Plugins – Begin sequence in ModelSupport.seq invokes the Model Plugin – Initialize entry point and the Model Plug – Begin entry point in all enabled plug-in instances. The ModelSupport.seq file loads the configured plug-in instances when the process model calls the Initialize Execution Entry Point sequence.

A custom process model must call all the applicable sequences in ModelSupport.seq in the following order:

1. Initialize Execution Entry Point
2. Model Plugins – Begin
3. Model Plugins – Pre Batch (Batch controller thread only)
4. Model Plugins – Batch Start (Batch controller thread only)
5. Model Plugins – Pre UUT (Test socket thread only)
6. Model Plugins – UUT Start (Test socket thread only)
7. Model Plugins – OnTheFly Step Results (Call from the ProcessModelPostResults callback)
8. Model Plugins – UUT Done (Test socket thread only)
9. Model Plugins – Post UUT (Test socket thread only)
10. Model Plugins – Batch Done (Batch controller thread only)
11. Model Plugins – Post Batch (Batch controller thread only)
12. Model Plugins – End

Note

<TestStand>\Components\Models\TestStandModels

<TestStand Public>\Components\Models

A custom process model that creates a controller thread and multiple test socket threads like the Batch and Parallel process models must meet the following requirements:

#### All Models

- The Begin entry point in the controller thread must complete before any Begin entry point in any test socket thread starts.
- All End entry points in any test socket thread must complete before the End entry point in the controller thread starts.

#### Batch-Specific

- All Begin entry points in all test socket threads must complete before the Pre Batch entry point starts.
- The Pre Batch entry point must complete before any Pre UUT entry points start.
- All restarted test socket threads must reach the same sync point as the remaining, active test socket threads before any Pre UUT entry points start.
- All UUT Start entry points must complete before the Batch Done entry point starts.
- The Batch Start entry point must complete before any UUT Done entry points start.
- All Post UUT entry points must complete before the Post Batch entry point starts.

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- Model Plugin – Pre UUT
- Model Plugin – Initialize
- Model Plugin – Begin
- TestStand Directory Structure
- Process Model Thread Types
- Batch Controller and Test Socket Synchronization Architecture
- Avoid Batch Synchronization Sections in Process Model Plug-in Entry Points

<!--NI_TOPIC bundle=teststand path=interactive-executions.html language=enus -->
## TOPIC 00479: Interactive Executions

- bundle_id: `teststand`
- source_path: `interactive-executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/interactive-executions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you run steps in interactive mode, you can execute specific steps in a sequence. Use the Interactive Executions section on the Execution tab of the Station Options dialog box to control if an interactive execution records results, runs steps in the Setup and Cleanup step groups, and evaluates p

### Interactive Executions

When you run steps in interactive mode, you can execute specific steps in a sequence. Use the Interactive Executions section on the Execution tab of the Station Options dialog box to control if an interactive execution records results, runs steps in the Setup and Cleanup step groups, and evaluates preconditions. The options in the Interactive Executions section also determine how TestStand handles step failures, errors, and branching during interactive executions.

Note

<TestStand Public>\Tutorial\Solution

#### Running Selected Steps as a Separate Execution

Complete the following steps to run selected steps from a Sequence File window as a separate execution.

1. Open <TestStand Public>\Tutorial\Computer.seq .
2. Insert a breakpoint at the Power On step.
3. Press <Ctrl> and select the Power On , ROM , and ROM Diagnostics steps.
4. Select Execute»Run Selected Steps to start a root interactive execution. By default, when you run selected steps from a Sequence File window, TestStand also executes the Setup and Cleanup step groups. You enable or disable the Run Setup and Cleanup option on the Execution tab of the Station Options dialog box to control whether TestStand runs the Setup and Cleanup step groups as part of the root interactive execution.
5. Click Done in the Test Simulator dialog box. The execution stops at the Power On step breakpoint. The execution pointer for the interactive execution is a narrow yellow arrow.
6. Step over twice to step through the execution until you reach the ROM Diagnostics step. Only the steps you selected execute. TestStand dims the other steps.
7. Resume and complete the execution.
8. Close the Execution window.
9. Ensure that the Power On, ROM, and ROM Diagnostics steps are selected. Repeat steps 4 through 8, but select Execute»Run Selected Steps Using»Single Pass in step 4. TestStand executes the steps you selected using the Single Pass Execution entry point, which generates a UUT report.
10. Close the Execution window.

#### Running Selected Steps During an
 Execution

Complete the following steps to interactively execute selected
 steps in a sequence while suspended at a breakpoint during an execution.

1. Ensure that the Power On, ROM, and ROM Diagnostics steps are selected and select
 Execute»Single Pass .
2. Select the ROM test to fail and click
 Done . The execution stops at the breakpoint on the
 Power On step.
3. Step through the execution until you reach the RAM Diagnostics step. Notice that
 the ROM step failed.
4. Place a breakpoint at the ROM step in the Execution window and select the
 ROM and ROM Diagnostics 
 steps.
5. Right-click the ROM Diagnostics step and select
 Loop on Selected Steps from the context menu to
 launch the Loop on Selected Steps dialog box. Enter 100 in the
 Loop Count control and click OK . TestStand starts an
 interactive execution of 100 loops for the steps you selected and enters a
 suspended state at the breakpoint for the ROM step. The execution pointer for
 the normal execution remains on the RAM Diagnostics step, and an execution
 pointer for the new interactive execution points to the ROM step.
6. Step through the interactive execution. The interactive execution toggles only
 between the ROM step and the ROM Diagnostics step. The ROM step continues to
 fail.
7. Click the Terminate Interactive Execution button on the
 Execution pane toolbar. TestStand returns the execution to a suspended state on
 the RAM Diagnostics step.
8. Complete the following steps to force the execution to continue from a step
 other than the currently suspended step.
  1. Select the ROM step so it is the only highlighted
 step.
  2. Right-click the ROM step and select
 Set Next Step to Cursor from the context
 menu. The execution pointer moves from the RAM Diagnostics step to the
 ROM step. The execution continues from the ROM step when you resume or
 step through the sequence.
  3. Step over once. The ROM step executes instead of the RAM Diagnostics
 step.
9. Resume and complete the execution. The report contains entries for each step you
 executed interactively.
10. Remove the breakpoint from the Power On step in the Sequence File window.
11. Close all the windows in the sequence editor and do not save any changes.

Parent topic:

Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=interactively-executing-steps.html language=enus -->
## TOPIC 00480: Interactively Executing Steps

- bundle_id: `teststand`
- source_path: `interactively-executing-steps.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/interactively-executing-steps.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To interactively execute selected steps in a sequence, select Run Selected Steps or Loop On Selected Steps from the context menu or from the Execute menu. You can run steps the following two ways in interactive mode: Run steps interactively from a Sequence File window to create a new execution calle

### Interactively Executing Steps

To interactively execute selected steps in a sequence, select Run Selected Steps or Loop On Selected Steps from the context menu or from the Execute menu.

You can run steps the following two ways in interactive mode:

- Run steps interactively from a Sequence File window to create a new execution called a root interactive execution. You can specify station options to control whether the Setup and Cleanup step groups of the sequence run as part of a root interactive execution.
- Run steps interactively from an existing Execution window for a normal execution suspended at a breakpoint. The selected steps run in a nested interactive execution within the context of the normal execution.The steps you run interactively can access the variable values of the normal execution and add to the results. When you use the process model for the original execution, the report includes these results. When the selected steps complete, the execution returns to the originally suspended step. A configurable station option specifies whether step failures and errors propagate to the original execution.

In interactive mode, the selected steps run in the order in which they appear in the sequence. To configure TestStand to evaluate preconditions when executing interactively, select Configure»Station Options and enable the Evaluate Preconditions option in the Interactive Executions section on the Execution tab of the Station Options dialog box. You can also use the Branching Mode control in this dialog box to configure whether interactive executions branch to unselected steps.

Parent topic:

Executing Sequences

Related concepts:

- Step Groups

<!--NI_TOPIC bundle=teststand path=interfacing-with-ni-hardware-drivers-using-py.html language=enus -->
## TOPIC 00481: Interfacing with NI-Hardware drivers using Python Custom step and Python Adapter

- bundle_id: `teststand`
- source_path: `interfacing-with-ni-hardware-drivers-using-py.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/interfacing-with-ni-hardware-drivers-using-py.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the possibility of TestStand interfacing with NI device drivers through Python packages for the desired NI devices. The example will not use the actual device drivers. It will mimic the behaviour of the device drivers. You can modify the Python modules to interact w

### Interfacing with NI-Hardware drivers using Python Custom step and Python Adapter

#### Purpose

This example demonstrates the possibility of TestStand interfacing with NI device drivers through Python packages for the desired NI devices.

The example will not use the actual device drivers. It will mimic the behaviour of the device drivers. You can modify the Python modules to interact with actual Python drivers.

The example will call into a Python module that will use simulated Python drivers for accessing device.

#### Example File Location

<TestStand Public>Examples\Interfacing with Hardware\Interfacing Modular
 Instruments Using Python Custom Step
 Type\InterfacingModularInstrumentsUsingPyCustomStepType.seq

#### Highlighted Features

- Custom Step Types

#### Major API

None

#### Prerequisites

You must have a version of Python supported by your version of TestStand installed and
 added to your PATH variable.

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence sequence, review the steps in the Setup step group.
  - The Create Device Sessions step, which is a Sequence Call step, simulates the creation of device sessions for the NI-DMM and NI-DcPower devices.
2. On the Steps pane of the MainSequence sequence, review the steps in the Main step group.
  - The NI-DMM step, which is a Sequence Call step, simulates the interfacing with the NI-DMM Python package for the NI-DMM device.
  - The NI-SMU [DcPower] step, which is a Sequence Call step, simulates the interfacing with the NI-DcPower Python package for the NI-DCPower device.
3. On the Steps pane of the MainSequence sequence, review the steps in the Cleanup step group.
  - The Close Device Sessions step, which is a Sequence Call step, simulates the releasing of the device sessions for NI-DMM and NI-DcPower devices.
4. On the Steps pane of the CreateDeviceSessions subsequence, review the steps in the Main step group.
  - The New NI-DMM Session and the New NI-DCPower Session steps, which are instances of the Custom Step Types NIDMM_NewSession and NIDCPOWER_NewSession of the sequence file respectively, create new sessions.
  - The New NI-DMM Session step and the New NI-DCPower Session step open two separate Python interpreter sessions for the respective devices.
5. On the Steps pane of the NI-DMM subsequence, review the steps in the Main step group.
  - The Auto Schedule step, which is an Auto Schedule Synchronization step, performs auto scheduling (avoids multiple access) of the steps within the Use Auto Scheduled Resource block.
  - The Use Auto Scheduled Resource block, which is a Use Auto Scheduled Resource Synchronization step, defines the set of steps that needs to be considered for auto scheduling.
  - The Configure NI-DMM Session step, simulates the initialization of the NI-DMM device session by setting the Range, Rate, number of Points to measure and the measurement type properties in the NI-DMM device session object.
  - The Get DMM Measurements step simulates the collecting of measurement values from the NI-DMM device using the NI-DMM device session object.
  - The Average DMM Measurements, which is a Numeric Limit Test step, calculates the average of the measured values and validates it with a defined test range.
  - The Results step, which is an Additional Results step, displays the measurement values obtained from the NI-DMM session object.
6. On the Steps pane if the NI-SMU [DcPower] subsequence, review the steps in the Main step group.
  - The Auto Schedule step, which is an Auto Schedule Synchronization step, performs auto scheduling (avoids multiple access) of the steps within the Use Auto Scheduled Resource block.
  - The Use Auto Scheduled Resource block, which is a Use Auto Scheduled Resource Synchronization step, defines the set of steps that needs to be considered for auto scheduling.
  - The Configure NI-DCPower Session step, simulates the initialization of the NI-DCPower device session by setting the current and voltage Limits and Ranges and the number of Points to measure in the NI-DCPower device session object.
  - The Get DCPower Measurements [Voltage, Current] step simulates the collecting of voltage and current measurement values from the NI-DCPower device using the NI-DCPower device session object.
  - The Average DCPower Voltage Measurement in Channel 0 and 1 and the Average DCPower Current Measurement in Channel 0 and 1, which is an Action step, calculates the average of the measured values across channels 0 and 1.
  - The Validate Averaged Measurements, which is a Multiple Numeric Limit Test step, validates the average of the measured values with defined test ranges.
  - the Results step, which is an Additional Results step, displays the measurement values obtained from the NI-DCPower session object across channels 0 and 1.
7. On the Steps pane of the CloseDeviceSessions subsequence, review the steps in the Main step group.
  - The Close NI-DMM Session and the Close NI-DCPower Session steps, which are instances of the Custom Step Types NIDMM_CloseSession and NIDCPOWER_CloseSession respectively of the sequence file, simulate the releasing of the device sessions.
8. Select Execute»Single Pass to run the sequence.
9. When execution completes, review the report.

Parent topic:

Examples for Interfacing with Hardware

Related concepts:

- TestStand Directory Structure
- Custom Step Types
- Step Groups

Related information:

- TestStand Python Support

<!--NI_TOPIC bundle=teststand path=interoperating-with-other-processes-and-syste.html language=enus -->
## TOPIC 00482: Interoperating with Other Processes and Systems

- bundle_id: `teststand`
- source_path: `interoperating-with-other-processes-and-syste.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/interoperating-with-other-processes-and-syste.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many test systems integrate with an Enterprise Resource Planning (ERP) system or a Manufacturing Execution System (MES) that processes test system reports to provide business-critical data to other systems. In some cases, an engineer or technician might process the report for statistical analysis on

### Interoperating with Other Processes and Systems

Many test systems integrate with an Enterprise Resource Planning (ERP) system or a Manufacturing Execution System (MES) that processes test system reports to provide business-critical data to other systems. In some cases, an engineer or technician might process the report for statistical analysis on a separate computer. These post-processing requirements might dictate the report generation format for the test system.

TestStand saves the ATML and XML reports in structured XML file formats that are easily processed
 using an API for XML (SAX) or DOM parsers. TestStand saves the ASCII and HTML
 reports in unstructured ASCII file formats that are not as easy to post-process as
 XML file formats. NI defines the TSR file format, which requires the TestStand
 Engine and the TestStand Offline Results Processing Utility to generate another file
 in a format you can process directly.

#### Recommended Report
 Options

The following table summarizes the recommended options you
 configure in the Report Options dialog box when you optimize for interoperating with
 other processes and systems:

| Report Option | Value |
| --- | --- |
| Format | ATML, XML, ASCII, HTML, TSR* (best to worst) |
| Asynchronous | N/A |
| On-the-Fly Report | N/A |
| Only Display Latest Results | N/A |

Note

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for interoperating with other
 processes and systems:

- Maximize test system throughput
- Minimize report file size
- Include all necessary report content
- Support post-failure information recovery
- Generate reports immediately for the current UUT before testing the next
 one
- Generate multiple reports for each UUT

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Maximizing Test System Throughput
- Minimizing Report File Size
- Including All Necessary Report Content
- Supporting Post-Failure Information Recovery
- Generating the Report for the Current UUT before Testing the Next UUT
- Generating Multiple Reports for Each UUT

<!--NI_TOPIC bundle=teststand path=interpreter-session-management-in-python.html language=enus -->
## TOPIC 00483: Interpreter Session Management in Python

- bundle_id: `teststand`
- source_path: `interpreter-session-management-in-python.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/interpreter-session-management-in-python.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose The example will showcase how to use different Python interpreter sessions in a single execution. Example File Location <TestStand Public>Examples\Fundamentals\Python\Interpreter Session Management\Interpreter Session Management Sequence.seq Highlighted Features Python Interpreter Session Ma

### Interpreter Session Management in Python

#### Purpose

The example will showcase how to use different Python interpreter sessions in a single execution.

#### Example File
 Location

<TestStand
 Public>Examples\Fundamentals\Python\Interpreter Session
 Management\Interpreter Session Management Sequence.seq

#### Highlighted Features

- Python Interpreter Session Management

#### Major API

None

#### Prerequisites

You must have required version of CPython interpreter installed and added to your PATH variable. You must update the Python version to use in the Python adapter configuration dialog before using the example.

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence sequence, review the steps in the Setup step group.
  - The first step, Update Python version to use in all steps, updates the Python version in each step to use the version specified in Python adapter settings. You typically will not do this for an actual test and should instead directly specify the Python version to use in the steps that use the Python adapter. This example can't determine the Python version installed in the computer and therefore modifies the Python version of each step programmatically to match what is specified in the Python adapter settings.
2. On the Steps pane, review the steps in the Main step group.
  - The Global interpreter session step, which is a Sequence Call step, call the Global subsequence two times to demonstrate Python global interpreter session.
  - The Per Thread interpreter session, which is a Sequence Call step, call the Per Thread subsequence three times on a separate thread to demonstrate Python per thread interpreter session.
  - The Wait for Thread Return step, which is a Wait step, waits for execution completion of the Per Thread subsequence on a separate thread.
  - The Per Execution interpreter session, which is a Sequence Call step, call the Per Execution subsequence on a new execution instance to demonstrate Python per execution interpreter session.
  - The Wait for Executions to Return step, which is a Wait step, waits for execution completion of the Per Execution subsequence on a separate execution instance.
  - The Object Reference interpreter session step, which is a Sequence Call step, call the Object Reference subsequence to demonstrate Python object reference interpreter session.
3. The Global, Per Thread, Per Execution, and Object Reference subsequence gets and sets Python attribute in the code module.
4. The Result step in Global, Per Thread, Per Execution, and Object Reference subsequence, which is an Additional Results step, summarizes the results in the report.
5. Select Execute»Single Pass to run the sequence.
6. When execution completes, review the report to see the how different interpreter sessions maintain independence from each other.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=introduction-to-teststand.html language=enus -->
## TOPIC 00484: Introduction to TestStand

- bundle_id: `teststand`
- source_path: `introduction-to-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/introduction-to-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI TestStand is a flexible and open test management framework for building, customizing, and deploying a full-featured test management system. Creating a TestStand-Based System Creating a TestStand-based test solution is a process that includes designing the test system, developing test sequences fo

### Introduction to TestStand

NI TestStand is a flexible and open test management framework for building, customizing, and deploying a full-featured test management system.

#### Creating a TestStand-Based
 System

Creating a TestStand-based test solution is a process that includes
 designing the test system, developing test sequences for units under test (UUTs),
 customizing the TestStand framework, debugging the test sequences, and deploying the
 test system to test station computers.

#### Design

Learn about the components of the TestStand framework, learn how to use those features, and
 understand when to customize that behavior. Plan the system architecture of the proposed
 solution. Determine the development environments to use to develop user interfaces and code
 modules in the solution. Consider how to manage the development and deployment of the
 solution, including how to organize files under development, how to deploy the files, and
 how to debug and update systems you deploy.

Refer to the section of this tutorial for more information about the components and
 features of TestStand and how to customize those features. Refer to the NI TestStand
 Advanced Architecture Series for more advanced concept and architecture information. This
 series is a suite of documents TestStand architects and developers created to provide more
 detailed information for experienced TestStand users with complex projects.

Note

#### Develop

Write test sequences for use on a test station computer. A test sequence is a series of steps that initialize instruments, perform complex tests, or change the flow of executions. Use the sequence editor or a custom sequence editor to write and edit test sequences.

#### Customize

Edit the default behavior of the TestStand framework depending on the needs of the application you create. You can customize reporting, database logging, process models, callback sequences, and user interfaces to create a unique, robust test solution for an application.

#### Debug

Ensure that the test sequences and any customized features execute correctly before you deploy the test system. Use the TestStand Sequence Analyzer in the sequence editor or the stand-alone sequence analyzer application during development or before deployment to find errors and enforce custom development guidelines you establish.

TestStand provides multiple features in the sequence editor or a custom sequence editor for debugging sequences, including tracing, breakpoints, conditional breakpoints, stepping through code, and watch expressions. The TestStand system development cycle is an iterative process, and you might have to debug an application multiple times.

#### Deploy

After you develop, customize, and debug a TestStand system, you can deploy the system to multiple test stations. The TestStand Deployment Utility simplifies the complex process of deploying a TestStand system by automating many of the steps involved, including collecting sequence files, code modules, configuration data for instruments, and support files for the test system. You can also use the deployment utility to create an installer or patch distributions.

#### Major Software Components of TestStand

The major software components of TestStand include the TestStand Engine, sequence editor, user interfaces, module adapters, process models, and deployment utility.

#### TestStand Engine

The TestStand Engine is a set of DLLs that exports an ActiveX Automation server API. The sequence editor and TestStand User Interfaces use the TestStand API, which you can call from any programming environment that supports access to ActiveX servers, including code modules you write in LabVIEW and LabWindows/CVI. The NI TestStand Help includes detailed documentation for the TestStand API.

#### TestStand Sequence Editor

The sequence editor is a development environment in which you create, edit, execute, and debug sequences and the tests sequences call. Use the sequence editor to access all features, such as step types and process models. Refer to the Process Models section of this tutorial for more information about process models.

You can debug a sequence using the following techniques, similar to how you debug in application development environments (ADEs) such as LabVIEW, LabWindows/CVI (ANSI), and Microsoft Visual Studio:

- Setting breakpoints
- Stepping into, out of, or over steps
- Tracing through program executions
- Displaying variables
- Monitoring variables, expressions, and output messages during executions
- Performing static analysis of sequence files to locate errors and enforce coding guidelines

In the sequence editor, you can start multiple concurrent executions, execute multiple instances of the same sequence, or execute different sequences at the same time. Each execution instance opens an Execution window. In Trace Mode, the Execution window shows the steps in the currently executing sequence. If the execution suspends, the Execution window shows the next step to execute and provides debugging options.

In the sequence editor, you can fully customize the pane and tab layout to optimize development and debugging tasks. You can also customize the menus, toolbars, and keyboard shortcuts.

#### User Interfaces

A TestStand User Interface is an application you deploy to a development system or a
 production station to provide a custom GUI for executing, debugging, or editing sequences.
 Simple user interfaces might only support running sequences, and custom sequence editors
 might support editing, running, and debugging sequences.

TestStand includes separate user interface applications developed in LabVIEW,
 LabWindows/CVI, Microsoft Visual Basic, .NET, C#, and C++ (MFC). Because TestStand also
 includes the source code for each user interface, you can fully customize the user
 interfaces. You can create a custom user interface using any programming language that can
 host ActiveX controls or control ActiveX Automation servers.

TestStand ships with
 full-featured Custom Sequence Editor user interfaces. These interfaces can be found by
 default at C:\Users\Public\Documents\National Instruments\TestStand
 20XX\UserInterfaces\Full-Featured\, or by navigating to Start»All Programs»National Instruments»TestStand <Version>»User Interfaces from the Windows Start Menu.

With the user interfaces in Editor Mode, you can modify sequences and display sequence
 variables, sequence parameters, step properties, and so on. With the user interfaces in
 Operator Mode, you can start multiple concurrent executions, set breakpoints, and step
 through sequences.

#### Module Adapters

The TestStand Engine uses module adapters to invoke code modules that sequences call. A code module is a program module from an ADE or programming language and can contain one or more functions that perform a specific test or other action. Module adapters load and call code modules, pass parameters to code modules, and return values and status from code modules. The module adapters support the following types of code modules:

- LabVIEW VIs
- LabWindows/CVI functions in DLLs you create in LabWindows/CVI or other compilers
- C/C++ functions in DLLs
- .NET assemblies
- ActiveX Automation servers
- HTBasic subroutines
- Python modules

Adapters specific to an ADE can open the ADE, create source code for a new code module in the ADE, and display the source for an existing code module in the ADE. The adapters support stepping into the source code in the ADE while you execute the step from the TestStand Sequence Editor or a TestStand User Interface.

TestStand includes the following module adapters:

- LabVIEW Adapter—Calls LabVIEW VIs with a variety of connector panes. The VIs can exist in LLBs or in LabVIEW packed project libraries. You can also call VIs in the context of a LabVIEW project or call LabVIEW class member VIs.
- LabWindows/CVI Adapter—Calls C functions in a DLL with a variety of parameter types.
- C/C++ DLL Adapter—Calls C/C++ functions and static C++ class methods in a DLL with a variety of parameter types. You can call global static methods or static class methods in C++ DLLs. You can create the DLL code module with LabWindows/CVI, Visual Studio, or any other environment that can create a C/C++ DLL, including LabVIEW-built shared libraries.
- .NET Adapter—Calls .NET assemblies written in any .NET-compliant language, such as C# or Microsoft Visual Basic .NET.
- ActiveX/COM Adapter—Creates ActiveX/COM objects, calls methods, and accesses properties of those objects. When you create an object, you can assign the object reference to a variable or property for later use in other ActiveX/COM Adapter steps.
- HTBasic Adapter—Calls HTBasic subroutines without passing parameters directly to a subroutine. TestStand provides a library of CSUB routines that use the TestStand API to access TestStand variables and properties from an HTBasic subroutine. Note (64-bit TestStand) The HTBasic Adapter is not supported.
- Sequence Adapter—Calls a subsequence in the current sequence file, in another sequence file, or a sequence file on a remote system. You can also make recursive sequence calls.
- Python Adapter—Calls Python modules.

Refer to the following tutorials for more information about using LabVIEW and LabWindows/CVI with TestStand. Refer to the NI TestStand Help for more information about using the LabVIEW and LabWindows/CVI Adapters.

- Calling LabVIEW VIs
- Calling LabWindows/CVI Code Modules

#### Process Models

Testing a UUT requires more than just executing a set of tests. Usually, the test system must perform a series of operations before and after it executes the sequence that performs the tests. Common operations that define the testing process include identifying the UUT, notifying the operator of pass/fail status, logging results, and generating a report. The set of operations and the flow of execution is called a process model. A TestStand process model is a sequence file you can use to define standard testing operations so you do not have to re-implement the same operations in every sequence file you write.

TestStand includes predefined Sequential, Parallel, and Batch models you can modify or replace. Use the Sequential model to run a test sequence on one UUT at a time. Use the Parallel and Batch models to run the same test sequence on multiple UUTs simultaneously.

You can modify an existing TestStand process model or you can create a custom process model. The ability to modify a process model is essential because the testing process can vary depending on production lines, production sites, or company systems and practices. You can edit a process model in the same way you edit other sequence files. You can also use client sequence files to customize various model operations by overriding the callback sequences process models define.

#### Entry Points

A process model defines a set of entry points, and each entry point is a sequence in the process model file that invokes a test sequence file. Defining multiple entry points in a process model gives the test station operator different ways to invoke a Main sequence or configure the process model.

Execution entry points in a process model provide different ways for the test station operator to invoke a Main sequence. Execution entry points handle common operations, such as UUT identification and report generation. For example, the default Sequential process model provides the Test UUTs and Single Pass Execution entry points. The Test UUTs Execution entry point initiates a loop that repeatedly identifies and tests UUTs. The Single Pass Execution entry point tests a single UUT without identifying it.

Configuration entry points provide an interface for configuring the process model, typically through a GUI. For example, the default Batch model provides the Configure Model Options entry point. This entry point creates the Configure menu item.

#### TestStand Deployment Utility

Use
 the TestStand Deployment Utility to create a deployable image or a patch deployment of a
 TestStand system and an optional installer. The deployable image can contain sequence files,
 code modules, process models and supporting files, user interface applications,
 configuration files, and step types and supporting files the TestStand system uses. The
 installer can contain all files from a deployable image or contain only a subset of files to
 create a patch for a previously deployed image.

You can also use the deployment
 utility to include the TestStand Engine and supporting files, LabVIEW and LabWindows/CVI
 Run-Time Engines, and hardware drivers in the installer you create. The installer that the
 deployment utility creates can also register ActiveX servers, replace existing files on the
 target computer, and create program shortcuts. You can configure the deployment utility to
 remove VI block diagrams or to lock the VIs you deploy.

Parent topic:

Getting Started with TestStand

Related concepts:

- Deploying TestStand Systems
- Calling LabVIEW VIs
- Calling LabWindows/CVI Code Modules

Related information:

- TestStand Advanced Architecture Series

<!--NI_TOPIC bundle=teststand path=invalid-teststand-enumerations.html language=enus -->
## TOPIC 00485: Invalid TestStand Enumerations

- bundle_id: `teststand`
- source_path: `invalid-teststand-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/invalid-teststand-enumerations.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most TestStand API prevents enumeration instances from becoming invalid. Nevertheless,changing the type definition can make existing instances invalid. For example, if an enumerator is deleted from the type definition, any existing instances set to that enumerator become invalid. Changing the flags

### Invalid TestStand Enumerations

Most TestStand API prevents enumeration instances from becoming invalid. Nevertheless,changing the type definition can make existing instances invalid. For example, if an enumerator is deleted from the type definition, any existing instances set to that enumerator become invalid. Changing the flags and strict/loose setting can similarly render existing instances invalid.

Assigning new values to invalid enumerations is possible. Conceptually, this behavior is similar to initializing an uninitialized variable in a language like C++. It does not matter whatthe value used to be after you set the new one.

In most cases, attempting to obtain or use the value of an invalid enumeration results in a runtime error. Methods such as GetValString() and GetValNumber() fail when invoked on invalid enumerations. TestStand expression operations, such as the equality operator (==), result in runtime errors for invalid enumerations as well. Similarly, passing an invalid enumeration to a code module via the adapters results in a runtime error.

One exception to this rule is PropertyObject.GetDisplayNames. When you callPropertyObject.GetDisplayNames on an invalid enumeration, the output valueDisplayNamestring parameter indicates the internal state of the enumeration and that it is invalid.

Another exception is serialization methods. Property object files and sequence files can be saved or read even if they contain invalid enumerations. PropertyObject.GetXML orPropertyObject.SetXML work with invalid enumerations if you pass theXMLOption_AllowInvalidObjects option.

Parent topic:

Using Enumerations in TestStand

<!--NI_TOPIC bundle=teststand path=invoking-methods-in-labview.html language=enus -->
## TOPIC 00486: Invoking Methods in LabVIEW

- bundle_id: `teststand`
- source_path: `invoking-methods-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/invoking-methods-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand objects have methods you invoke to perform an operation or function. In LabVIEW, use the Invoke Node to invoke methods. The block diagram in the following figure shows how to invoke the Sequence.UnloadModules method to unload all code modules in the sequence.

### Invoking Methods in LabVIEW

TestStand objects have methods you invoke to perform an operation or function. In LabVIEW, use the Invoke Node to invoke methods. The block diagram in the following figure shows how to invoke the Sequence.UnloadModules method to unload all code modules in the sequence.

[IMAGE alt='image' src='GUID-9CBB28E7-2227-48D2-904E-AF1DE0C7F25F-a5.png']

Parent topic:

Programming with the TestStand API in LabVIEW

Related concepts:

- Setting the Preferred Execution System of LabVIEW VIs to Prevent Deadlock

<!--NI_TOPIC bundle=teststand path=invoking-methods-in-labwindows-cvi.html language=enus -->
## TOPIC 00487: Invoking Methods in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `invoking-methods-in-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/invoking-methods-in-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand objects have methods you invoke to perform an operation or function. In LabWindows/CVI, you invoke methods on TestStand objects using the functions the ActiveX driver for those objects defines. The following function shows how to access the number of steps in a sequence: int GetNumSteps(CA

### Invoking Methods in LabWindows/CVI

TestStand objects have methods you invoke to perform an operation or function. In LabWindows/CVI, you invoke methods on TestStand objects using the functions the ActiveX driver for those objects defines.

The following function shows how to access the number of steps in a sequence:

int GetNumSteps(CAObjHandle sequence)

{

int error = 0;

ErrMsg errMsg = "";

ERRORINFO errorInfo;

CAObjHandle engine = 0;

long numSteps = 0;

tsErrChk(TS_SequenceGetNumSteps (sequence, &errorInfo, TS_StepGroup_Main, &numSteps));

Error:

return error;

}

The errorInfo variable is a structure the LabWindows/CVI ActiveX Automation Library defines to hold information about errors that can occur in the operation of the function. The tsErrChk macro determines whether the function return value or the errorInfo variable indicates an error occurred and continues execution at the Error label when True.

Note

tsapicvi.fp

TS_

NI TestStand Help

Parent topic:

Programming with the TestStand API in LabWindows/CVI

Related concepts:

- Accessing Built-in Properties in LabWindows/CVI
- Accessing Dynamic Properties in LabWindows/CVI
- ActiveX Automation Server Concepts
- Using ActiveX Drivers in LabWindows/CVI
- Adding and Releasing References in LabWindows/CVI
- Programming with TestStand API Constants and Enumerations in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=invoking-model-callbacks.html language=enus -->
## TOPIC 00488: Invoking Model Callbacks

- bundle_id: `teststand`
- source_path: `invoking-model-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/invoking-model-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Process models define model callbacks that client sequence files can override, such as the PreUUT or TestReport callbacks. Because a model plug-in is a model file, it can also define model callbacks that client sequence files can override. The model plug-in sequence file must include the model callb

### Invoking Model Callbacks

Process models define model callbacks that client sequence files can override, such as the PreUUT or TestReport callbacks. Because a model plug-in is a model file, it can also define model callbacks that client sequence files can override.

The model plug-in sequence file must include the model callback sequence so the plug-in can invoke the callback sequence. The process model must also include a copy of the callback sequence for TestStand to display the callback sequence in the Sequence File Callbacks dialog box so you can conveniently override the process model callback sequences in client sequence files.

The following table outlines ways in which you can implement callbacks and the resulting behavior for each technique. The table uses the term defined to mean that the file contains the callback sequence and the term invoked to mean that other sequences in the file call the callback sequence. If TestStand recognizes the callback at edit time, the callback appears in the Sequence File Callbacks dialog box and uses a green icon in the Sequences pane.

| Description of Callback Configuration | Resulting Behavior |
| --- | --- |
| Defined and invoked only in the process model | Client sequence can override the callback, and the callback is recognized at edit time. |
| Defined and invoked only in the process model plug-in (Not Recommended) | Client sequence can override the callback, but the callback is not recognized at edit time. |
| Defined in the process model and the process model plug-in but invoked only in the plug-in | If the client sequence file defines the callback, the client sequence file overrides the plug-in implementation of the callback. Otherwise, TestStand invokes the plug-in definition of the callback. The process model definition of the callback does not override the plug-in definition. The callback is recognized by the client sequence file at edit time. |
| Defined and invoked in the process model and the process model plug-in | If the client sequence file defines the callback, the client sequence file overrides the process model and process model plug-in implementations. Sequences in the process model and the plug-in invoke the process model and plug-in instances of the callback, respectively. The process model definition of the callback does not override the plug-in definition or vice versa. The callback is recognized by the client sequence file at edit-time. |

Parent topic:

Model Plug in Client-File Callbacks

Related concepts:

- Callback Sequences

<!--NI_TOPIC bundle=teststand path=issues-with-using-the-msdasql-provider-in-dat.html language=enus -->
## TOPIC 00489: Issues with Using the MSDASQL Provider in Database Viewer

- bundle_id: `teststand`
- source_path: `issues-with-using-the-msdasql-provider-in-dat.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/issues-with-using-the-msdasql-provider-in-dat.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: MSDASQL is Microsoft's Object Linking and Embedding Database (OLE DB) provider for Open Database Connectivity (ODBC) drivers. MSDASQL allows OLE DB consumer applications to use ODBC drivers to connect to a data source. The provider converts incoming OLE DB calls into ODBC calls and passes them on to

### Issues with Using the MSDASQL Provider in Database Viewer

MSDASQL is Microsoft's Object Linking and Embedding Database (OLE DB) provider for Open Database Connectivity (ODBC) drivers. MSDASQL allows OLE DB consumer applications to use ODBC drivers to connect to a data source. The provider converts incoming OLE DB calls into ODBC calls and passes them on to the specified ODBC driver. The provider then retrieves results from the ODBC driver and formats the results into OLE DB specific structures, which the user can then access.

The Database Viewer application uses the ADO .NET database component, which does not support the MSDASQL provider. If the connection string specified in the New Data Link dialog box uses the MSDASQL provider, the Database Viewer application attempts to remove the MSDASQL provider and connect directly through the ODBC Driver/Data Source Name (DSN) specified in the connection string. If this connection fails, the Database Viewer application will display the following error message:

The following error occurred while attempting to connect to the specified database: The .Net Framework Data Provider for OLEDB (System.Data.OleDb) does not support the Microsoft OLE DB Provider for ODBC Drivers (MSDASQL). Use the .Net Framework Data Provider for ODBC (System.Data.Odbc). Database Viewer does not support the MSDASQL provider. For more information on how to resolve this error, refer to the TestStand help topic : Issues with Using the MSDASQL Provider in Database Viewer.

To resolve this error, you can modify the connection string to connect using the ODBC Driver/DSN directly using one of the two following strategies:

- Connect using a DSN —A data source name (DSN) is a data structure that contains information about a specific database that an OBDC driver needs in order to connect to the database. If an existing DSN is to be used to establish a connection with the database, you must simply specify the name of the DSN in the connection string, using the following format:
 DSN=MyDSNName; 
 To create a new DSN, use the Windows ODBC Data Source Administrator tool.
(64-bit Windows) Run, with administrator privileges, [WindowsDir]\SysWOW64\odbcad32.exe for 64-bit TestStand and [WindowsDir]\System32\odbcad32.exe for 32-bit TestStand.
(32-bit Windows) Run, with administrator privileges, [WindowsDir]\System32\odbcad32.exe for 32-bit TestStand.
- Connect without using a DSN —To specify a connection string that directly uses an ODBC driver, refer to the Configuring Connection Strings topic.

Parent topic:

Database Viewer Known Issues

Related concepts:

- Configuring Connection Strings

Related information:

- New Data Link Dialog Box

<!--NI_TOPIC bundle=teststand path=item-names.html language=enus -->
## TOPIC 00490: Item Names

- bundle_id: `teststand`
- source_path: `item-names.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/item-names.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Item Names For a code module, the item name is a description of the module call. For UUTs, Batches, and Lots the item name includes the serial number or lot id, if specified. If it is needed to distinguish separate items, the item name includes an index value. For Steps, the item name is the name of

### Item Names

#### Item Names

For a code module, the item name is a description of the module call. For UUTs, Batches, and Lots the item name includes the serial number or lot id, if specified. If it is needed to distinguish separate items, the item name includes an index value. For Steps, the item name is the name of the step. If multiple steps have the same name, the item name includes the unique identifier for the step.

If item names coincide for different types of operations, the profiler appends the type of operation to the item name, such as 'Lock' or 'Step'.

#### Locks and Other Synchronization Item Names

You typically name TestStand locks after the resources the locks protect, such as DMM1 or DC Power Supply. The profiler displays the name of the lock, or other synchronization object, as the profiler item name. Thus, if you follow the convention of naming your locks after the resources they protect, you can easily use the profiler to observe the usage of and contention for your physical and logical resources.

If you create a lock or another type of synchronization object with an empty name, TestStand names the object for you, such as Unnamed Synchronization Object N. TestStand also automatically selects an item name in the following cases:

- When you use the Use Lock to Allow Only One Thread at a Time to Execute the Step option on the Synchronization panel of the Properties tab of the Step Settings pane and not specifying an existing lock
- When you use the Batch Synchronization option on the Synchronization panel of the Properties tab of the Step Settings pane
- When you use a Wait step
- When you use a Use Auto Scheduled Resource step

In these cases, TestStand creates an item name by combining the unique ID of the step with the run-time ID of the file that contains the step. However, for readability, the profiler window shows the name of the step as the item name. If the step name is not a unique item name, the profiler appends the unique id for the step to the step name. For Use Auto Scheduled Resource steps that do not have unique names, the profiler first attempts to make the step name unique by appending a description of the locks the step acquires.

Parent topic:

Execution Profiler

Related information:

- Step Settings Pane
- Lock Step

<!--NI_TOPIC bundle=teststand path=item-usage-per-thread-graph.html language=enus -->
## TOPIC 00491: Item Usage per Thread Graph

- bundle_id: `teststand`
- source_path: `item-usage-per-thread-graph.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/item-usage-per-thread-graph.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Item Usage per Thread Graph Use this graph to view the items a thread uses over time. You can view how long the thread waits to acquire an item and how long it retains or uses each item. Along the vertical axis, each row in the graph represents a TestStand Thread. The thread name displays in a legen

### Item Usage per Thread Graph

#### Item Usage per Thread Graph

Use this graph to view the items a thread uses over time. You can view how long the thread waits to acquire an item and how long it retains or uses each item.

Along the vertical axis, each row in the graph represents a TestStand Thread. The thread name displays in a legend to the left of the graph time line. After the thread name, each row displays rectangles that represent the operations in that thread.

The horizontal axis represents time. Operations are positioned along the horizontal axis according to the times at which the operations begin and end. Each operation has a label that indicates the name of the item on which it operates. Hovering over an operation displays a tool tip with additional information.

Parent topic:

Profiler Window Graphs

<!--NI_TOPIC bundle=teststand path=ivi-drivers.html language=enus -->
## TOPIC 00492: IVI Drivers

- bundle_id: `teststand`
- source_path: `ivi-drivers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/ivi-drivers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Interchangeable Virtual Instrument (IVI) is an instrument driver standard that provides common programming interfaces for several classes of instruments. IVI drivers exist for a number of National Instruments devices and other popular instruments. Visit ni.com/ivi for more information about IVI. Vis

### IVI Drivers

Interchangeable Virtual Instrument (IVI) is an instrument driver standard that provides common programming interfaces for several classes of instruments. IVI drivers exist for a number of National Instruments devices and other popular instruments. Visit ni.com/ivi for more information about IVI. Visit the Instrument Driver Network at ni.com/idnet for more information about instrument drivers and for finding and downloading instrument drivers compatible with National Instruments software.

Two architectures exist for IVI drivers—IVI-C, based on ANSI C, and IVI-COM, based on Microsoft Component Object Model (COM) technology. The IVI step types support IVI-C class-compliant instrument drivers and support IVI-COM class-compliant instrument drivers when you install the IVI-COM Adapter component of the IVI Component Package included in the NI Device Driver DVD. TestStand does not install IVI class instrument drivers.

You can call IVI-C instrument class drivers and specific drivers from any development environment that supports calls into DLLs. Many IVI-C instrument drivers have native LabVIEW-generated wrappers. You can also convert an IVI-C instrument driver using the Create VI Interface to CVI Instrument Driver tool available from the Instrument Driver Network at ni.com/idnet. You can call IVI-COM instrument class drivers and specific drivers from any development environment that supports ActiveX. Use the ActiveX/COM Adapter to configure steps to access objects IVI-COM class instrument drivers define.

Parent topic:

Instrument Drivers

Related concepts:

- ActiveX/COM Adapter

Related information:

- Interchangeable Virtual Instrument Drivers
- NI Instrument Driver Network
- IVI Step Types

<!--NI_TOPIC bundle=teststand path=ivi-step-types.html language=enus -->
## TOPIC 00493: IVI Step Types

- bundle_id: `teststand`
- source_path: `ivi-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/ivi-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use IVI step types to configure and take measurements from IVI instruments with the following logical names: SampleDMM, SampleScope, SampleFGen, SamplePowerSupply, and SampleSwitch. This example contains Setup steps that initialize the logical names in simula

### IVI Step Types

#### Purpose

ni.com/ivi

Note

AdditionalInstallers

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\IVI Step Types\IVI Step
 Types.seq

#### Highlighted Features

- IVI step types
- NI Session Manager

#### Major API

None

#### Prerequisites

Complete the following steps to install the required software and IVI-compliant instrument drivers.

1. Install the following additional components from the NI Device Driver DVD that comes with
 TestStand:
  1. NI Measurement & Automation Explorer (MAX)
  2. IVI Compliance Package (ICP)
2. Refer to the Instrument Driver Network at ni.com/idnet to download and install IVI-compliant instrument drivers for each of the IVI classes this example uses. Search for the manufacturer or type of instrument you want to download. Some basic IVI-compliant instrument drivers you can use with this example include the following: In MAX, the driver installer automatically creates a driver session entry under the Driver Sessions item and populates the software module information under the Instrument Driver Software Module item in the Advanced folder.
  - Dmm —hp34401a
  - Scope —tkds30xx
  - Fgen —hp33120a
  - Switch —age1442a
  - PowerSupply —hp66xxbc
3. Complete the following steps to create a logical name for each instrument driver.
  1. In MAX, expand the IVI Drivers category to the left.
  2. Right-click the Logical Names item in the configuration tree and select Create New from the context menu.
  3. Complete the configuration panel for the new logical name. Logical names are case-sensitive.

Note

#### How to Use This Example

This example communicates with each type of instrument driver, one after the other. In each case, the sequence configures the instrument and takes a measurement. The sequence contains Label steps denote the beginning of steps that communicate with each type of IVI instrument.

Review the edit tabs on the Step Settings pane for each IVI step to see how the step configures the instrument and takes measurements.

TestStand stores the logical names the sequence expects as file global variables. Each variable name must match the logical name created for each driver in MAX.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure
- Session Manager

Related tasks:

- Installing TestStand

<!--NI_TOPIC bundle=teststand path=java-step-types.html language=enus -->
## TOPIC 00494: Java Step Types

- bundle_id: `teststand`
- source_path: `java-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/java-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates custom step types for calling methods in Java classes. The step types call compiled Java class files (.class) using the Java Native Interface (JNI) and permit the invocation of methods located within the classes. Example File Location <TestStand Public>\Examples\Cus

### Java Step Types

#### Purpose

This example demonstrates custom step types for calling methods in Java classes. The step types call compiled Java class files (.class) using the Java Native Interface (JNI) and permit the invocation of methods located within the classes.

#### Example File
 Location

<TestStand
 Public>\Examples\Custom Step Types\Java Step Types\Java Computer
 Motherboard Test.seq

#### Highlighted Features

Custom step types

#### Major API

Engine.UnloadAllModules

#### Prerequisites

Java Runtime Environment (JRE) version 6 update 16, which you can download from the Oracle website. The Java step types are likely compatible with earlier and later versions of the JRE but have not been tested in JRE versions other than version 6 update 16.

#### How to Use This Example

The example sequence file, Computer.seq, contains a SequenceFileLoad callback that TestStand automatically executes when you open the sequence file. The SequenceFileLoad callback copies the JavaCall.dll and JavaCall.uir files from the <TestStand Public>\Examples\Custom Step Types\Java Step Types directory to the <TestStand Public>\Components\StepTypes\Java directory. The Java step types call functions within JavaCall.dll, which must be located in a TestStand search directory for the step types to locate the DLL.

Note

The Java step types support the creation and cleanup of the Java virtual machine (JVM) and the manipulation of objects that exist within the JVM through method calls. The step types support the use of all Java primitive types and strings, which you can use to pass data between TestStand and Java objects. The step types rely on JavaCall.dll, which is a LabWindows/CVI library, for TestStand to interface with Java. The library communicates with TestStand using an ActiveX interface and communicates with Java through the JNI.

Java uses the JNI to call compiled code written in C/C++ and to access Java code from C/C++. Refer to the Java Native Interface website for more information about JNI technology.

When you open <TestStand Public>\Examples\Custom Step Types\Java Step Types\Java Computer Motherboard Test.seq in the TestStand Sequence Editor, the Java step types appear in the following groups on the Insertion Palette:

- StartStop —Contains steps that start and destroy the JVM.
- Methods —Contains steps that call a particular Java method in a specified class.
- Static Methods —Contains steps that call a particular static class method in a specified class.

The CallStaticJavaMethod and CallJavaMethod steps consist of Numeric Limit Test, String Value Test, Pass Fail Test, and Action steps.

Use a Java step type to call JavaCall.dll, which extracts information about the step type from TestStand using ActiveX calls and then calls the appropriate method in the JVM using the JNI. For example, use the CallJavaMethod step to call the InvokeJavaMethod function JavaCall.dll, which calls the TestStand Engine to extract the class, method, and parameter information and instantiate the class within the existing JVM. The step identifies and calls the method with parameter values retrieved from TestStand. The JavaCall.dll file then passes the return value back to TestStand.

#### StartStop Steps

Use the StartJVM and DestroyJVM steps, located under the StartStop group on the Insertion Palette, in pairs around other Java steps to call methods for the contained steps. A typical sequence structure begins with a StartJVM step, which you place in the Setup step group, followed by a number of Methods or Static Methods steps, which you place in the Main step group. Place the DestroyJVM step in the Cleanup step group.

Configure the StartJVM step to provide the class path, which is the path of the Java classes to access. Select the StartJVM step in a sequence and click the Edit Java Class Path Location button on the Step Settings pane to launch the Set Class Path dialog box, in which you can specify the class path. You must include all Java classes that are accessed in the path. If you leave the path empty, the JVM cannot locate the user-written Java classes. Click Browse in the Set Class Path dialog box to launch the Select Paths dialog box, in which you can add directories that contain the Java classes to call.

#### Methods and Static Methods Steps

The Static Methods steps call static class methods and the Methods steps call other methods of the class. The Methods steps automatically load the appropriate class and create new instances of the class before making the call to the method. The Static Methods steps do not create new instances of the class before making the call.

Methods and Static Methods steps include the following steps:

- Numeric Limit Test —Used to call methods that return a numeric value, such as a byte, integer, short, long, float, or double. You can compare the value returned to a set of limits to determine whether the step passed.
- String Value Test —Used with a method that returns a string value. The step compares the returned value to the expected value.
- Pass/Fail Test —Used with Boolean return values.
- Action —Used with any type of return value.

You can configure Methods and Static Methods steps by selecting a step in the sequence and clicking the Edit Call or Edit Static Call button on the Step Settings pane to launch the Edit Java Call dialog box, in which you can configure the step to call the appropriate Java method.

#### Tips for Using the Java Step Types

Keep the following tips in mind when you use Java step types in TestStand:

- Before calling any Java methods, you must create the JVM. Call the StartJVM step before you call any of the Methods or Static Methods steps.
- The Methods steps automatically load the appropriate class and allocate an object of that type. The Static Methods steps load only the appropriate class. Neither step type automatically calls the constructor of the class. The example does contain a sample .
- Because Java is case-sensitive, the class name and method names must use the same case as the Java class file specifies.

#### Compatible Types

The
 following table shows how data types in TestStand are compatible with certain data
 types in Java. The Java step types automatically handle the conversion between
 types.

| TestStand Type | Java Types |
| --- | --- |
| Number | byte, short, int, long, float, double |
| String | char, string |
| Boolean | Boolean |

#### Computer Motherboard Example

When you open the Computer.seq example sequence file, the SequenceFileLoad callback copies the required files to the appropriate directories. When TestStand executes the Setup step group of the MainSequence, the sequence first obtains the TestStand directory and locates the Java classes to call. The StartJVM step automatically sets the class path and passes it to the JVM. TestStand then calls a static Java method called Start, which creates a new computer object by calling the constructor of the Computer class, to launch a dialog box. You can dismiss the dialog box, and TestStand reads the tests you select to fail from the Java class one call at a time because Java supports only calls by value semantics.

When the calls are complete, the steps in the Main step group call the Java methods. The steps supply a value to the methods that determine whether the test passes or fails. Depending on the supplied value, the method returns a result. If a single step fails, TestStand skips all remaining steps.

The step in the Cleanup step group destroys the JVM.

#### Limitations

The following are the known limitations of the Java step types:

- The step types currently do not support Java reference types, such as arrays and objects.
- You cannot access the same instantiated object multiple times. Each time a step calls a method on an object, a new object is created. Therefore, all states must be maintained in class variables as static members.
- The step types cannot directly call constructors. The example does contain a sample .
- The step types are not thread-safe. Do not use the step types with the Parallel and Batch process models.

#### Known Issues

Because you cannot unload the JVM once you load it in a process without exiting the process, the DestroyJVM step does not actually destroy the JVM. Instead, the DestroyJVM step only detaches the current thread, which indicates that the JVM is no longer referenced, so that the JVM can unload in future versions, if required. Refer to the DestroyJavaVM API documentation on the Oracle website for more information about this issue.

You cannot unload the JVM once you load it in a process, and you cannot unload JavaCall.dll when you call the Engine.UnloadAllModules method of the TestStand API. You can unload JavaCall.dll only by exiting the process by closing the sequence editor or user interface. Once you load a Java class file, you must restart the process by restarting the sequence editor or user interface to force the JVM to load any changed or recompiled versions of the Java class.

You cannot change the class search path once TestStand loads the JVM. When TestStand calls the StartJVM step with a given class path, you cannot change the class search path by calling the StartJVM step again with a new class path. You can change the class path only by exiting the process by closing the sequence editor or user interface. You must set the required class paths in the first StartJVM step.

#### Error Codes and Descriptions

You might receive some error codes when using this example.

Parent topic:

Examples for Custom Step Types

Related concepts:

- TestStand Directory Structure
- Custom Step Types
- Edit Java Call Dialog Box
- Error Codes and Descriptions

<!--NI_TOPIC bundle=teststand path=keyboard-navigation.html language=enus -->
## TOPIC 00495: TestStand Sequence Editor Keyboard Navigation

- bundle_id: `teststand`
- source_path: `keyboard-navigation.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/keyboard-navigation.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Sequence Editor supports keyboard navigation between panes and windows, between panes in windows, between tabs in panes, and within tree and table controls. Navigating Between Panes and Windows Press <Ctrl-Tab> to display the Pane Navigation menu and hold the <Ctrl> key to prevent Test

### TestStand Sequence Editor Keyboard
 Navigation

The TestStand Sequence Editor supports keyboard navigation between panes and windows,
 between panes in windows, between tabs in panes, and within tree and table controls.

#### Navigating Between Panes and Windows

Press <Ctrl-Tab> to display the Pane Navigation menu and hold the <Ctrl>
 key to prevent TestStand from closing the menu. The Pane Navigation menu contains a
 Panes list and a Windows list which represent all the panes and windows currently
 visible in the sequence editor.

While you hold the <Ctrl> key you can use the arrow keys or <Tab> and
 <Shift-Tab> to select a new pane or window to activate when you release the
 <Ctrl> key.

You can also use the keyboard to activate any pane through the View menu and any
 window through the Window menu.

#### Navigating Between Panes within a Window

Press the <Tab> key to navigate between panes in a window, such as the
 Sequences pane, Steps pane, and Variables pane.

#### Navigating within Panes

Press the <Tab> key to navigate between controls within a pane. If a pane
 contains tabs, when you navigate to the tab, use the left and right arrow keys to
 change the visible tab.

#### Navigating within a List

For list controls that contain multiple columns, such as the following controls, use
 the arrow keys to navigate between rows and columns:

- Variables list on the Variables Pane
- Parameters Table on a module tab
- TestStand Sequence Analyzer rules, files, and analysis modules
- TestStand File Diff and Merge utility

When you navigate to the plus or minus icon for an expandable row in the list, press
 <Space> or <Enter> to expand or collapse the row. You can also press the
 <+> or <-> keys on the keypad to expand or collapse a selected row, or
 press the <*> key on the keypad to expand the selected row and all items
 within the row. Press <Ctrl-+> on the keypad to standardize the width of each
 column to the width of the widest column.

When you press <Enter> in a field of a Value column, the focus moves to the
 value field for the next row.

Press <Space> or <Ctrl-F4> to display the drop-down list for a combo box
 control, such as a Boolean value.

Note

Resize Array

Change
 Type

#### Navigating with the Insertion Palette

Press the <Tab> key to navigate between the expand/collapse buttons, the
 Adapter list, the Step Types list, and the Templates lists. Use the up and down
 arrows to move within the lists. Use the left and right arrow keys to expand and
 collapse folders within the lists.

In the Templates list, you can also press the <+> or <-> keys on the
 keypad to expand or collapse a selected row, or press the <*> key on the
 keypad to expand the selected row and all items within the row.

Parent topic:

TestStand Sequence Editor

Related concepts:

- Expressions

<!--NI_TOPIC bundle=teststand path=labview-adapter.html language=enus -->
## TOPIC 00496: LabVIEW Adapter

- bundle_id: `teststand`
- source_path: `labview-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/labview-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Adapter provides advanced functionality for calling VIs from TestStand. You can use the LabVIEW Adapter to complete the following tasks: Call VIs with arbitrary connector panes. Call VIs that exist on disk, in LLBs, or in LabVIEW packed project libraries. You can also call VIs in the con

### LabVIEW Adapter

The LabVIEW Adapter provides advanced functionality for calling VIs from TestStand. You can use the LabVIEW Adapter to complete the following tasks:

- Call VIs with arbitrary connector panes.
- Call VIs that exist on disk, in LLBs, or in LabVIEW packed project libraries. You can also call VIs in the context of a LabVIEW project or call LabVIEW class member VIs.
- Call member VIs from LabVIEW classes using LabVIEW dynamic dispatching, when required.
- Call VIs on remote computers.
- Configure and call LabVIEW Property Nodes using I/O References or LabVIEW classes.
 
 Note 

 You must have LabVIEW 2013 or later to configure and call LabVIEW Property Nodes in TestStand.
- Run VIs using the LabVIEW development system or a LabVIEW executable.
- Run VIs using the LabVIEW Run-Time Engine.
- Create and edit VIs from TestStand.
- Debug VIs (step in/step out) from TestStand.

Note

When you specify a module for a step, the TestStand Sequence Editor displays the LabVIEW Module tab and TestStand User Interfaces launch the Edit LabVIEW VI Call dialog box.

The LabVIEW Adapter can run VIs using the LabVIEW development system, the LabVIEW Run-Time Engine (RTE), or a LabVIEW executable built with an ActiveX Automation server enabled.

Use the LabVIEW Adapter Configuration dialog box to configure the LabVIEW Adapter to select a LabVIEW server, reserve loaded VIs for execution, establish a code template policy, change legacy VI settings, and specify behavior for deploying LabVIEW shared variables.

Parent topic:

Module Adapters

Related concepts:

- Adapter and Code Module Support for 64-bit TestStand
- Calling LabVIEW Class Member VIs from TestStand
- Calling VIs on Remote Computers
- Calling LabVIEW VIs
- Cross-Bitness Support using the LabVIEW Development System
- Driver Support for 64-bit TestStand
- Express VIs and Property Node Calls in 32-bit TestStand and 64-bit TestStand
- LabVIEW Code Module Support for 64-bit TestStand
- Module Adapter Parameter Mapping Guidelines
- Migrating LabVIEW Code Modules from 32-bit TestStand to 64-bit TestStand
- Organizing LabVIEW-Based TestStand Systems
- Programming with the TestStand API in LabVIEW
- Simultaneously Supporting 32-bit TestStand and 64-bit TestStand

Related information:

- LabVIEW User Manual

<!--NI_TOPIC bundle=teststand path=labview-code-module-support-for-64-bit-testst.html language=enus -->
## TOPIC 00497: LabVIEW Code Module Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `labview-code-module-support-for-64-bit-testst.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/labview-code-module-support-for-64-bit-testst.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you migrate LabVIEW code modules from 32-bit TestStand to 64-bit TestStand, you must consider the architectures you need to support, how to handle Express VIs and property node calls, and cross-bitness support using the LabVIEW development system.

### LabVIEW Code Module Support for 64-bit TestStand

When you migrate LabVIEW code modules from 32-bit TestStand to 64-bit TestStand, you must consider the architectures you need to support, how to handle Express VIs and property node calls, and cross-bitness support using the LabVIEW development system.

Parent topic:

Adapter and Code Module Support for 64-bit TestStand

Related concepts:

- Migrating LabVIEW Code Modules from 32-bit TestStand to 64-bit TestStand
- Simultaneously Supporting 32-bit TestStand and 64-bit TestStand
- Express VIs and Property Node Calls in 32-bit TestStand and 64-bit TestStand
- Cross-Bitness Support using the LabVIEW Development System

<!--NI_TOPIC bundle=teststand path=labview-data-types-in-teststand.html language=enus -->
## TOPIC 00498: LabVIEW Data Types in TestStand

- bundle_id: `teststand`
- source_path: `labview-data-types-in-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/labview-data-types-in-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand provides number, string, Boolean, and object reference built-in data types. TestStand also provides several standard named data types, including Path, Error, LabVIEWAnalogWaveform, and others. You can create container data types to hold any number of other data types. TestStand container d

### LabVIEW Data Types in TestStand

TestStand provides number, string, Boolean, and object reference built-in data types. TestStand also provides several standard named data types, including Path, Error, LabVIEWAnalogWaveform, and others. You can create container data types to hold any number of other data types. TestStand container data types are analogous to LabVIEW clusters. You can use references to external objects, such as ActiveX (Microsoft ActiveX) objects or VISA sessions, between different types of code modules.

LabVIEW includes a greater variety of built-in data types than TestStand does, so TestStand converts LabVIEW data types in certain ways when calling VIs.

#### Converting LabVIEW Numeric Representations

The following table shows how TestStand converts LabVIEW numeric representations:

| LabVIEW Numeric Representation | TestStand Data Type |
| --- | --- |
| Real number (U8, U16, U32, I8, I16, I32, SGL, DBL, or EXT) | Number TestStand does not support extended-precision, (EXT) floating-point numbers. TestStand converts any EXT numbers from LabVIEW into double-precision (DBL) numbers. |
| 64-bit integer numeric (I64) | Number {Signed 64-bit integer} |
| Unsigned 64-bit integer numeric (UI64) | Number {Unsigned 64-bit integer} |
| Fixed-point numeric | TestStand does not support calling VIs with fixed-point numeric indicators or controls. |
| Complex number (CSG, CDB, or CXT) | Number TestStand maps each part of the complex number to separate TestStand Number properties. |

#### Converting LabVIEW Controls and Indicators

The following table shows how TestStand converts LabVIEW controls or indicators:

| LabVIEW Control or Indicator | TestStand Data Type |
| --- | --- |
| Enum (U32, U16, or U8) | Enumeration |
| Ring control (Text Ring, Menu Ring, Text and Picture Ring, or Picture Ring) | Enumeration |
| String | String |
| Path | Path or string |
| ActiveX Control or Automation Refnum | Object reference |
| .NET Refnum | Object reference You can pass .NET references created in LabVIEW to TestStand and store the references in Object Reference variables in TestStand and then pass them to other VIs. You can also share objects that derive from MarshalByRefObject or that are serializable between LabVIEW and TestStand. In TestStand, you can use those references with the .NET Adapter. Similarly, in LabVIEW, you can directly use references you create with the TestStand .NET Adapter. Refer to Microsoft MSDN documentation for more information about MarshalByRefObject and serializable objects.Note Passing data between LabVIEW and TestStand is not supported in TestStand 2024 Q4 and subsequent versions. |
| Waveform | LabVIEWAnalogWaveform To create variables for I64 or UI64 Waveforms, you must create a new custom data type, because the representation of the Y element that corresponds to the standard LabVIEWAnalogWaveform data type is set to double-precision 64-bit floating-point. |
| Digital waveform | LabVIEWDigitalWaveform |
| Digital data | LabVIEWDigitalData |
| Picture | String You must select Binary String from the ring control in the Type column of the VI Parameter Table on the LabVIEW Module tab. |
| Refnum (File I/O, VI, Menu, Queue, TCP connection, and so on) | Number You cannot use references to internal LabVIEW objects inside TestStand or in other types of code modules. You can store only references to LabVIEW objects in TestStand properties and then pass the properties to other VIs. |
| Timestamp | String TestStand converts the LabVIEW Timestamp data type to a System Time data type and then to a string data type with the m/d/yyyy h:mm:ss.sss AM/PM format, where TestStand rounds fractions of a second to the nearest millisecond. |
| m | Month as number without leading zero |
| d | Day of the month as number without leading zero |
| yyyy | Four-digit year |
| h | Hour of the day, without leading zero (12-hour clock) |
| mm | Minute of the hour, with leading zero |
| ss | Second of the minute, with leading zero |
| sss | Milliseconds of the second, with leading zero |
| AM/PM | AM or PM uppercase |
| Error I/O | Error By default, when a VI uses the standard LabVIEW error out cluster as an output parameter, TestStand automatically passes that value into the Step.Result.Error property for the step. You can also update the value manually. If an error occurs during execution of the VI and the error out cluster is passed to Step.Result.Error, TestStand launches the Run-Time Error dialog box by default. |
| Array of x | Array of TestStand (x) |
| Variant | Any TestStand data type Note Passing LabVIEW I/O references (DAQmx Task Name, DAQmx Channel Name, VISA Resource Name, IVI Logical Name, FieldPoint IO Point, or Motion Resource) through TestStand as a variant is not supported. Use the LabVIEWIOControl instead. |
| LabVIEW Object | Object reference |
| Cluster | Container |
| I/O controls (DAQmx Task Name, DAQmx Channel Name, VISA Resource Name, IVI Logical Name, FieldPoint IO Point, or Motion Resource) | LabVIEWIOControl |
| IMAQ Session | Number |
| Other I/O controls (DAQmx Physical Channel Name, Terminal Name, Analog Trigger Source, Scale Name, Device Name, or Switch Name) | String |

Note

Parent topic:

LabVIEW Adapter

Related concepts:

- Code Modules
- Passing an Instance of a LabVIEW Class Object

Related information:

- PropertyObject

<!--NI_TOPIC bundle=teststand path=labview.html language=enus -->
## TOPIC 00499: LabVIEW

- bundle_id: `teststand`
- source_path: `labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use LabVIEW ActiveX Invoke and Property nodes to access the complete functionality of the Session Manager server. The following figure demonstrates how to use the TestStand Session Manager - Get Instrument Session VI to obtain an instrument API handle: Instance handles that an instrument s

### LabVIEW

You can use LabVIEW ActiveX Invoke and Property nodes to access the complete functionality of the Session Manager server.

The following figure demonstrates how to use the TestStand Session Manager - Get Instrument Session VI to obtain an instrument API handle:

[IMAGE alt='image' src='GUID-035CDAD3-1AA9-48B7-BB51-5110B87C31C4-a5.png']

Note

plug&play

Parent topic:

Using Instrument Sessions in a Development Environment

<!--NI_TOPIC bundle=teststand path=labwindows-cvi-adapter.html language=enus -->
## TOPIC 00500: LabWindows/CVI Adapter

- bundle_id: `teststand`
- source_path: `labwindows-cvi-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/labwindows-cvi-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabWindows/CVI Adapter provides advanced functionality for calling code modules from TestStand. You can use the LabWindows/CVI Adapter to complete the following tasks: Call code modules with arbitrary prototypes in DLL code module files. Create and edit code modules from TestStand. Debug code mo

### LabWindows/CVI Adapter

The LabWindows/CVI Adapter provides advanced functionality for calling code modules from TestStand. You can use the LabWindows/CVI Adapter to complete the following tasks:

- Call code modules with arbitrary prototypes in DLL code module files.
- Create and edit code modules from TestStand.
- Debug code modules (step in/step out) from TestStand.
- Run code modules in-process or out-of-process using the LabWindows/CVI development system.

When you specify a module for a step, the TestStand Sequence Editor displays the LabWindows/CVI Module tab and TestStand User Interfaces launch the Edit LabWindows/CVI Module Call dialog box.

Use the LabWindows/CVI Adapter Configuration dialog box to configure the LabWindows/CVI Adapter to show function arguments in step descriptions, set the default structure packing size, select where steps execute, and establish a code template policy.

Parent topic:

Module Adapters

Related concepts:

- Code Modules
- Adapter and Code Module Support for 64-bit TestStand
- Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces
- C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand
- Calling LabWindows/CVI Code Modules
- Debugging DLLs
- Driver Support for 64-bit TestStand
- Loading Subordinate DLLs
- Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand
- Module Adapter Parameter Mapping Guidelines
- Pointers and Handles in 32-bit TestStand and 64-bit TestStand
- Programming with the TestStand API in LabWindows/CVI
