# NI DOCUMENT BUNDLE: lvdct-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvdct-api-ref start=1 end=97 -->
<!--NI_TOPIC bundle=lvdct-api-ref path=dct_intro.html language=enus -->
## TOPIC 00001: LabVIEW Database Connectivity Toolkit Programming Reference Manual

- bundle_id: `lvdct-api-ref`
- source_path: `dct_intro.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/dct_intro.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Database Connectivity Toolkit LabVIEW Release Notes Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.To comment on National Instruments documentation, refer to the National Instruments website.

### LabVIEW Database Connectivity Toolkit Programming Reference Manual

The LabVIEW Database Connectivity Toolkit

[LabVIEW Release Notes](https://www.ni.com/en-us/support/documentation/release-notes/product.labview.html) 
Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.

To comment on National Instruments documentation, refer to the National Instruments website.

<!--NI_TOPIC bundle=lvdct-api-ref path=menus/categories/computer/database-mnu.html language=enus -->
## TOPIC 00002: Database

- bundle_id: `lvdct-api-ref`
- source_path: `menus/categories/computer/database-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/menus/categories/computer/database-mnu.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Database VIs and function to access databases from LabVIEW. With the Database VIs and function, you can perform the most common database tasks, including the following: Work with any provider that adheres to the Microsoft ActiveX Data Object (ADO) standard. Work with any database driver that

### Database

Use the Database VIs and function to access databases from LabVIEW.

With the Database VIs and function, you can perform the most common database tasks, including the following:

- Work with any provider that adheres to the Microsoft ActiveX Data Object (ADO) standard.
- Work with any database driver that complies with ODBC or OLE DB.
- Maintain a high level of portability. In many cases, you can port your application to another database by changing the connection string you pass to the DB Tools Open Connection VI.
- Convert database column values from native data types to standard LabVIEW Database Connectivity Toolkit data types.
- Use SQL statements with all supported database systems, including non-SQL systems, using the default ADO ODBC provider.
- Retrieve the name and data type of a column returned by a SELECT statement.
- Create tables and select, insert, update, and delete records without using SQL statements.

The VIs and function on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes).

[IMAGE alt='icon' src='database-mnu.png']

- [DB Tools Open Connection VI](../../../vi-lib/addons/database/connection-llb/db-tools-open-connection-vi.html) Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Close Connection VI](../../../vi-lib/addons/database/connection-llb/db-tools-close-connection-vi.html) Closes a database connection by destroying its associated connection reference .
- [DB Tools Insert Data VI](../../../vi-lib/addons/database/auxilliary-llb/db-tools-insert-data-vi.html) Inserts a new row into the table in the database identified by the connection reference .
- [DB Tools Select Data VI](../../../vi-lib/addons/database/auxilliary-llb/db-tools-select-data-vi.html) Selects data from the table in the database identified by connection reference using the columns supplied in the columns array.
- [DB Tools Update Data VI](../../../vi-lib/addons/database/auxilliary-llb/db-tools-update-data-vi.html) Updates the data in a database identified by connection reference .
- [DB Tools Delete Data VI](../../../vi-lib/addons/database/auxilliary-llb/db-tools-delete-data-vi.html) Deletes data from a database identified by connection reference .
- [DB Tools Create Table VI](../../../vi-lib/addons/database/auxilliary-llb/db-tools-create-table-vi.html) Creates a new table in the database identified by connection reference . The table and column information inputs describe the name of the table and the properties of each column in the table, respectively.
- [DB Tools Drop Table VI](../../../vi-lib/addons/database/auxilliary-llb/db-tools-drop-table-vi.html) Deletes the specified table from the database identified by connection reference .
- [Database Variant To Data](../../../vi-lib/addons/database/db-variant-to-data/database-variant-to-data-xnode.html) Converts a database variant to the LabVIEW data type specified in type so you can use the data in another function or subVI.
- [Utility](../../../menus/categories/computer/database/db-util-mnu.html) Use the Utility VIs for a variety of operations, including getting table and column information, getting and setting database properties, formatting data and time data, performing database transactions, and writing and reading data files.
- [Advanced](../../../menus/categories/computer/database/db-adv-mnu.html) Use the Advanced VIs to perform advanced database operations such as executing SQL statements and fetching data. You might need to use SQL when you use these VIs.

<!--NI_TOPIC bundle=lvdct-api-ref path=menus/categories/computer/database/db-adv-mnu.html language=enus -->
## TOPIC 00003: Advanced

- bundle_id: `lvdct-api-ref`
- source_path: `menus/categories/computer/database/db-adv-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/menus/categories/computer/database/db-adv-mnu.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Advanced VIs to perform advanced database operations such as executing SQL statements and fetching data. You might need to use SQL when you use these VIs. The VIs on this palette can return general LabVIEW error codes. icon

### Advanced

Use the Advanced VIs to perform advanced database operations such as executing SQL statements and fetching data. You might need to use SQL when you use these VIs.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes).

[IMAGE alt='icon' src='db-adv-mnu.png']

- [DB Tools Execute Query VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-execute-query-vi.html) Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Fetch Recordset Data VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-fetch-recordset-data-vi.html) Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Fetch Element Data VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-fetch-element-data-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Fetch Next Recordset VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-fetch-next-recordset-vi.html) Retrieves the next recordset in a multi-recordset query identified by recordset reference . When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Free Object VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-free-object-vi.html) Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Move To Next Record VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-move-to-next-record-vi.html) Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Move To Previous Record VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-move-to-previous-record-vi.html) Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Move To Record N VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-move-to-record-n-vi.html) Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Create Parameterized Query VI](../../../../vi-lib/addons/database/command-llb/db-tools-create-parameterized-query-vi.html) Creates a parameterized SQL query and returns a command reference that you must free eventually. Unless you are detecting the parameters automatically, the number of elements in the parameters array must match the number of parameters you specify in SQL query . For stored procedures, set stored procedure to TRUE and SQL query to the name of the procedure you want to execute.
- [DB Tools Set Parameter Value VI](../../../../vi-lib/addons/database/command-llb/db-tools-set-parameter-value-vi.html) Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Get Parameter Value VI](../../../../vi-lib/addons/database/command-llb/db-tools-get-parameter-value-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools NULL VI](../../../../vi-lib/addons/database/command-llb/db-tools-null-vi.html) Returns a database variant that contains a NULL value.

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=menus/categories/computer/database/db-util-mnu.html language=enus -->
## TOPIC 00004: Utility

- bundle_id: `lvdct-api-ref`
- source_path: `menus/categories/computer/database/db-util-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/menus/categories/computer/database/db-util-mnu.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Utility VIs for a variety of operations, including getting table and column information, getting and setting database properties, formatting data and time data, performing database transactions, and writing and reading data files. The VIs on this palette can return general LabVIEW error code

### Utility

Use the Utility VIs for a variety of operations, including getting table and column information, getting and setting database properties, formatting data and time data, performing database transactions, and writing and reading data files.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes).

[IMAGE alt='icon' src='db-util-mnu.png']

- [DB Tools List Tables VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-list-tables-vi.html) Lists the tables in the database identified by connection reference .
- [DB Tools List Columns VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-list-columns-vi.html) Lists the columns present in table . The column information includes the name, the data type, and the defined size of the column.
- [DB Tools Set Properties VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-set-properties-vi.html) Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Get Properties VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-get-properties-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Format Datetime String VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-vi.html) Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Database Transaction VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-database-transaction-vi.html) Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Save Recordset To File VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-save-recordset-to-file-vi.html) Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Load Recordset From File VI](../../../../vi-lib/addons/database/recordset-llb/db-tools-load-recordset-from-file-vi.html) Loads a recordset from a file and returns a recordset reference that identifies this recordset. You can retrieve data from this recordset like any other recordset, but some properties might not be available on this recordset.

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-create-table-vi.html language=enus -->
## TOPIC 00005: DB Tools Create Table VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-create-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-create-table-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new table in the database identified by connection reference. The table and column information inputs describe the name of the table and the properties of each column in the table, respectively. icon Inputs/Outputs ci32.png primary key (-1) primary key specifies the column that is going to

### DB Tools Create Table VI

Creates a new table in the database identified by **connection reference**. The **table** and **column information** inputs describe the name of the table and the properties of each column in the table, respectively.

[IMAGE alt='icon' src='db-tools-create-table-vi.png']

#### Inputs/Outputs

| primary key (-1) — primary key specifies the column that is going to be the primary key for the table. The default is -1, which means the table does not have a primary key. connection reference — connection reference specifies a reference to an ADO Connection object. table — table is the name of the table in the database to create. column information — column information specifies an array of clusters that describe each column to be created. column name — column name is the name of column in database. data type — data type of column. size — size of column in database. Only used for string data type. allow null? — allow null? is a switch to indicate if the column allows NULL values. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. use file? (F) — use file? specifies whether to use a user-supplied file to determine native database types. The default is FALSE. connection reference out — connection reference out returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| column name — column name is the name of column in database. data type — data type of column. size — size of column in database. Only used for string data type. allow null? — allow null? is a switch to indicate if the column allows NULL values. |

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-database-transaction-vi.html language=enus -->
## TOPIC 00006: DB Tools Database Transaction VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-database-transaction-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-database-transaction-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Database Transaction VI

Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-database-transaction-vi.png']

- [Connection](../../../../vi-lib/addons/database/connection-llb/conn-transaction-vi.html) Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Command (C).vi](../../../../vi-lib/addons/database/command-llb/cmd-transaction-c-vi.html) Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Command (CR).vi](../../../../vi-lib/addons/database/command-llb/cmd-transaction-cr-vi.html) Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-delete-data-vi.html language=enus -->
## TOPIC 00007: DB Tools Delete Data VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-delete-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-delete-data-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes data from a database identified by connection reference. icon Inputs/Outputs cstr.png condition condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of a delete statement. For example, where (col1 > 10). If you wire an e

### DB Tools Delete Data VI

Deletes data from a database identified by **connection reference**.

[IMAGE alt='icon' src='db-tools-delete-data-vi.png']

#### Inputs/Outputs

| condition — condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of a delete statement. For example, where (col1 > 10). If you wire an empty string to this input, this VI deletes all data from table. connection reference — connection reference specifies a reference to an ADO Connection object. table — table specifies the name of the table whose data you want to delete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-drop-table-vi.html language=enus -->
## TOPIC 00008: DB Tools Drop Table VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-drop-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-drop-table-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the specified table from the database identified by connection reference. icon Inputs/Outputs cdlrn.png connection reference connection reference specifies a reference to an ADO Connection object. cstr.png table table is the name of the table in the database to delete. cerrcodeclst.png error

### DB Tools Drop Table VI

Deletes the specified **table** from the database identified by **connection reference**.

[IMAGE alt='icon' src='db-tools-drop-table-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. table — table is the name of the table in the database to delete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-execute-query-vi.html language=enus -->
## TOPIC 00009: DB Tools Execute Query VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-execute-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-execute-query-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Execute Query VI

Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-execute-query-vi.png']

- [Connection](../../../../vi-lib/addons/database/connection-llb/conn-execute-vi.html) Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Command](../../../../vi-lib/addons/database/command-llb/cmd-execute-vi.html) Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-seconds-vi.html language=enus -->
## TOPIC 00010: DB Tools Format Datetime String (Seconds) VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-seconds-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-seconds-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cu32.png seconds (now)

### DB Tools Format Datetime String (Seconds) VI

Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-format-datetime-string-seconds-vi.png']

#### Inputs/Outputs

| seconds (now) — seconds specifies the seconds to convert to a date/time string. The value of this input is the time-zone-independent number of seconds that have elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time. The default value is 0, which returns the current date and time. date/time string — date/time string returns the formatted date/time string. |
| --- |

Parent topic:

DB Tools Format Datetime String VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-time-stamp-vi.html language=enus -->
## TOPIC 00011: DB Tools Format Datetime String (Time Stamp) VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-time-stamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-time-stamp-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs catrn.png time stamp ti

### DB Tools Format Datetime String (Time Stamp) VI

Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-format-datetime-string-time-stamp-vi.png']

#### Inputs/Outputs

| time stamp — time stamp specifies the time stamp that you want to convert to a date/time string. The default is an empty time stamp, which returns the current date and time. date/time string — date/time string returns the formatted date/time string. |
| --- |

Parent topic:

DB Tools Format Datetime String VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-vi.html language=enus -->
## TOPIC 00012: DB Tools Format Datetime String VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Format Datetime String VI

Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-format-datetime-string-vi.png']

- [DB Tools Format Datetime String (Time Stamp) VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-time-stamp-vi.html) Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Format Datetime String (Seconds) VI](../../../../vi-lib/addons/database/auxilliary-llb/db-tools-format-datetime-string-seconds-vi.html) Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-free-object-vi.html language=enus -->
## TOPIC 00013: DB Tools Free Object VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-free-object-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-free-object-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Free Object VI

Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-free-object-vi.png']

- [Command](../../../../vi-lib/addons/database/command-llb/cmd-delete-vi.html) Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Recordset](../../../../vi-lib/addons/database/recordset-llb/rec-destroy-connection-vi.html) Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Command-Recordset](../../../../vi-lib/addons/database/recordset-llb/rec-destroy-command-vi.html) Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-get-properties-vi.html language=enus -->
## TOPIC 00014: DB Tools Get Properties VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-get-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-get-properties-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Get Properties VI

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-get-properties-vi.png']

- [Connection](../../../../vi-lib/addons/database/connection-llb/conn-get-properties-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Recordset (R)](../../../../vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-r-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Recordset (CR).vi](../../../../vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-cr-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Column (R)](../../../../vi-lib/addons/database/recordset-llb/rec-get-column-properties-r-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Column (CR)](../../../../vi-lib/addons/database/recordset-llb/rec-get-column-properties-cr-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Command (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-command-properties-c-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Command (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-command-properties-cr-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Parameter (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-parameter-properties-c-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Parameter (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-parameter-properties-cr-vi.html) Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-insert-data-vi.html language=enus -->
## TOPIC 00015: DB Tools Insert Data VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-insert-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-insert-data-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a new row into the table in the database identified by the connection reference. icon Inputs/Outputs cbool.png create table? (F) create table? creates a table if a table does not exist. This VI creates the table with column names provided in the columns input. If the columns input is empty,

### DB Tools Insert Data VI

Inserts a new row into the table in the database identified by the **connection reference**.

[IMAGE alt='icon' src='db-tools-insert-data-vi.png']

#### Inputs/Outputs

| create table? (F) — create table? creates a table if a table does not exist. This VI creates the table with column names provided in the columns input. If the columns input is empty, this VI names the columns Col0, Col1, and so on. This VI determines the type information of the columns created using the data input. If the data input is a cluster, each item in the cluster corresponds to a column that is created in the table. Note For string column types, the size is set equal to the size of the data. data — data specifies the data you want to insert in the database. If data is a cluster, this VI inserts each item in the cluster to each element in the columns input. The item order of the cluster determines the order how this VI inserts the items to the table. For example, this VI inserts the 0th item to the 0th element of the columns input. If the columns input is empty, this VI inserts the 0th item of the cluster to the first column in table. If data is not a cluster, this VI inserts the data to the column specified by the columns input. connection reference — connection reference specifies a reference to an ADO Connection object. table — table specifies the name of the table in the database in which to insert data. If the create table? input is TRUE, the VI attempts to create the table if it does not already exist. columns — columns is the column in the table to insert data into. Wiring an empty array to this input assumes that all columns in the table are to be used. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. flatten cluster? (F) — flatten cluster? specifies whether to insert a cluster that you wire to data as a binary value. If the value is TRUE, this VI updates the column that you specify in the columns input with the flattened binary value of the cluster. If the value is FALSE, this VI updates each column that you specify in the columns input with the corresponding item in the cluster. The default is FALSE. Note This input is valid only if you wire a cluster to the data input. use file? (F) — use file? instructs the VI to use a user-supplied file to determine database types. If you set use file? to FALSE, this VI uses a user-specified file to determine database types. If you set use file? to TRUE, this VI uses the dbtypes.ini file, located in the labview\\Database directory, to determine database types. This VI uses use file? only when create table? is TRUE. connection reference out — connection reference out returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-list-columns-vi.html language=enus -->
## TOPIC 00016: DB Tools List Columns VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-list-columns-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-list-columns-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Lists the columns present in table. The column information includes the name, the data type, and the defined size of the column. icon Inputs/Outputs cdlrn.png connection reference connection reference specifies a reference to an ADO Connection object. cstr.png table table specifies the name of the t

### DB Tools List Columns VI

Lists the columns present in **table**. The column information includes the name, the data type, and the defined size of the column.

[IMAGE alt='icon' src='db-tools-list-columns-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. table — table specifies the name of the table to search. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. column information — column information returns an array containing information about the columns in the database table. name — name returns the name of the column. database data type — database data type returns the type of data in the column. defined size — defined size returns the defined size of the column. columns — columns returns an array of strings containing the names of each column in a database table. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| name — name returns the name of the column. database data type — database data type returns the type of data in the column. defined size — defined size returns the defined size of the column. |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-list-tables-vi.html language=enus -->
## TOPIC 00017: DB Tools List Tables VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-list-tables-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-list-tables-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Lists the tables in the database identified by connection reference. icon Inputs/Outputs cdlrn.png connection reference connection reference specifies a reference to an ADO Connection object. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. T

### DB Tools List Tables VI

Lists the tables in the database identified by **connection reference**.

[IMAGE alt='icon' src='db-tools-list-tables-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. tables — tables returns an array of table names found in the database. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-select-data-vi.html language=enus -->
## TOPIC 00018: DB Tools Select Data VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-select-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-select-data-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects data from the table in the database identified by connection reference using the columns supplied in the columns array. This VI returns the data as a 2D array of variants. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. i

### DB Tools Select Data VI

Selects data from the **table** in the database identified by **connection reference** using the columns supplied in the **columns** array.

This VI returns the data as a 2D array of variants. You can convert each element in the array to its native LabVIEW data type using the [Database Variant To Data](../db-variant-to-data/database-variant-to-data-xnode.html) function.

[IMAGE alt='icon' src='db-tools-select-data-vi.png']

#### Inputs/Outputs

| condition — condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of a select statement. For example, where (col1 > 10). connection reference — connection reference specifies a reference to an ADO Connection object. table — table is the name of the table in the database from which to select data. You can specify multiple tables by using commas as the delimiter. columns — columns specifies the columns in table from which to select data. If this array is empty, all columns in the table are returned. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. data — data returns a 2D array of database variants that contains the selected data. Use the Database Variant To Data function to convert this data to its native LabVIEW data type. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-set-properties-vi.html language=enus -->
## TOPIC 00019: DB Tools Set Properties VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-set-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-set-properties-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Set Properties VI

Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-set-properties-vi.png']

- [Connection](../../../../vi-lib/addons/database/connection-llb/conn-set-properties-vi.html) Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.
- [Command (CR)](../../../../vi-lib/addons/database/command-llb/cmd-set-command-properties-cr-vi.html) Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.
- [Parameter (CR)](../../../../vi-lib/addons/database/command-llb/cmd-set-parameter-properties-cr-vi.html) Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.
- [Command (C)](../../../../vi-lib/addons/database/command-llb/cmd-set-command-properties-c-vi.html) Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.
- [Parameter (C)](../../../../vi-lib/addons/database/command-llb/cmd-set-parameter-properties-c-vi.html) Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/auxilliary-llb/db-tools-update-data-vi.html language=enus -->
## TOPIC 00020: DB Tools Update Data VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/auxilliary-llb/db-tools-update-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/auxilliary-llb/db-tools-update-data-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the data in a database identified by connection reference. icon Inputs/Outputs cstr.png condition condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of an update statement. For example, where (col1 > 10). If you do not

### DB Tools Update Data VI

Updates the data in a database identified by **connection reference**.

[IMAGE alt='icon' src='db-tools-update-data-vi.png']

#### Inputs/Outputs

| condition — condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of an update statement. For example, where (col1 > 10). If you do not specify a value for this input or if the input is an empty string, this VI updates all rows in table. data — data specifies the new data you want to update in the database. If data is a cluster and flatten cluster? is FALSE, this VI updates the columns specified by the columns input with the items in the cluster. The order of each item in the cluster determines the order this VI updates the items in the table. For example, this VI updates the column specified by the 0th element of the columns input with the 0th item in the cluster. If the columns input is empty, this VI updates table from the first column with the 0th item in the cluster. If data is a cluster and flatten cluster? is TRUE, this VI flattens the cluster to a binary value and updates the column specified by the columns input with the binary value. If data is not a cluster, this VI updates the column specified by the columns input with the input data. connection reference — connection reference specifies a reference to an ADO Connection object. table — table specifies the name of the table whose data you want to update. columns — columns specifies the names of the columns that you want to update. If you do not specify a value for this input or if the input is an empty array, this VI updates all columns in table. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. flatten cluster? (F) — flatten cluster? specifies whether to insert a cluster that you wire to data as a binary value. If the value is TRUE, this VI updates the column that you specify in the columns input with the flattened binary value of the cluster. If the value is FALSE, this VI updates each column that you specify in the columns input with the corresponding item in the cluster. The default is FALSE. Note This input is valid only if you wire a cluster to the data input. connection reference out — connection reference out returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-delete-vi.html language=enus -->
## TOPIC 00021: Command

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-delete-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-delete-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command reference command reference specifies a reference to a

### Command

Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-delete-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference — connection reference returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Free Object VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-execute-vi.html language=enus -->
## TOPIC 00022: Command

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-execute-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-execute-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ci32.png cache size (1) cache size specifies the

### Command

Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-execute-vi.png']

#### Inputs/Outputs

| cache size (1) — cache size specifies the number of records to store in local memory. After you retrieve the number of records in local memory and you request the next record, the current set of records is discarded from local memory and the next set are retrieved into local memory. The default is 1. command reference — command reference specifies a reference to an ADO Command object. cursor type — cursor type specifies the method for navigating the recordset. Some providers and/or databases do not support all cursors. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference — command-recordset reference returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Execute Query VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-c-vi.html language=enus -->
## TOPIC 00023: Binary (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Binary (C)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-binary-parameter-value-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-cr-vi.html language=enus -->
## TOPIC 00024: Binary (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Binary (CR)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-binary-parameter-value-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-command-properties-c-vi.html language=enus -->
## TOPIC 00025: Command (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-command-properties-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-command-properties-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command reference comm

### Command (C)

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-command-properties-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. command properties — command properties returns the following properties that define the most recent SQL query. parameter count — parameter count returns the number of parameters. command text — command text returns the parameterized SQL command. command timeout (s) — command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| parameter count — parameter count returns the number of parameters. command text — command text returns the parameterized SQL command. command timeout (s) — command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-command-properties-cr-vi.html language=enus -->
## TOPIC 00026: Command (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-command-properties-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-command-properties-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset refe

### Command (CR)

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-command-properties-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. command properties — command properties returns the following properties that define the most recent SQL query. parameter count — parameter count returns the number of parameters. command text — command text returns the parameterized SQL command. command timeout (s) — command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| parameter count — parameter count returns the number of parameters. command text — command text returns the parameterized SQL command. command timeout (s) — command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-c-vi.html language=enus -->
## TOPIC 00027: Date/Time (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Date/Time (C)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-datetime-parameter-value-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-cr-vi.html language=enus -->
## TOPIC 00028: Date/Time (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Date/Time (CR)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-datetime-parameter-value-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-c-vi.html language=enus -->
## TOPIC 00029: Double (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Double (C)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-double-parameter-value-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-cr-vi.html language=enus -->
## TOPIC 00030: Double (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Double (CR)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-double-parameter-value-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-c-vi.html language=enus -->
## TOPIC 00031: Integer (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Integer (C)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-integer-parameter-value-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-cr-vi.html language=enus -->
## TOPIC 00032: Integer (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Integer (CR)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-integer-parameter-value-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-parameter-properties-c-vi.html language=enus -->
## TOPIC 00033: Parameter (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-parameter-properties-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-parameter-properties-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command reference comm

### Parameter (C)

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-parameter-properties-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. parameter properties — parameter properties returns the following properties that define the query parameters. name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-parameter-properties-cr-vi.html language=enus -->
## TOPIC 00034: Parameter (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-parameter-properties-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-parameter-properties-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset refe

### Parameter (CR)

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-parameter-properties-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. parameter properties — parameter properties returns the following properties that define the query parameters. name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-c-vi.html language=enus -->
## TOPIC 00035: Single (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Single (C)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-single-parameter-value-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-cr-vi.html language=enus -->
## TOPIC 00036: Single (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### Single (CR)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-single-parameter-value-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-c-vi.html language=enus -->
## TOPIC 00037: String (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### String (C)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-string-parameter-value-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-cr-vi.html language=enus -->
## TOPIC 00038: String (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### String (CR)

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-get-string-parameter-value-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. type — type specifies the data type of parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. value — value returns the value of the parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Get Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-set-command-properties-c-vi.html language=enus -->
## TOPIC 00039: Command (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-set-command-properties-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-set-command-properties-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command reference command reference specifies a reference to an ADO Command object.

### Command (C)

Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-set-command-properties-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. command properties — command properties specifies the following properties that define the most recent SQL query. parameter count — parameter count specifies the number of parameters. This property is read-only. command text — command text specifies the parameterized SQL command. command timeout (s) — command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| parameter count — parameter count specifies the number of parameters. This property is read-only. command text — command text specifies the parameterized SQL command. command timeout (s) — command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. |

Parent topic:

DB Tools Set Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-set-command-properties-cr-vi.html language=enus -->
## TOPIC 00040: Command (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-set-command-properties-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-set-command-properties-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset reference command-recordset reference specifies a reference that c

### Command (CR)

Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-set-command-properties-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. command properties — command properties specifies the following properties that define the most recent SQL query. parameter count — parameter count specifies the number of parameters. This property is read-only. command text — command text specifies the parameterized SQL command. command timeout (s) — command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| parameter count — parameter count specifies the number of parameters. This property is read-only. command text — command text specifies the parameterized SQL command. command timeout (s) — command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. |

Parent topic:

DB Tools Set Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-set-parameter-properties-c-vi.html language=enus -->
## TOPIC 00041: Parameter (C)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-set-parameter-properties-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-set-parameter-properties-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command reference command reference specifies a reference to an ADO Command object.

### Parameter (C)

Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-set-parameter-properties-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. parameter properties — parameter properties contains the following properties that define the query parameters. name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) |

Parent topic:

DB Tools Set Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-set-parameter-properties-cr-vi.html language=enus -->
## TOPIC 00042: Parameter (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-set-parameter-properties-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-set-parameter-properties-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset reference command-recordset reference specifies a reference that c

### Parameter (CR)

Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-set-parameter-properties-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. parameter properties — parameter properties contains the following properties that define the query parameters. name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| name — Name of the parameter This property is read-only. SQL data type — This control is an enum that contains all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction — The direction of the parameter value (Input, Output, Input/Output, or Return value) |

Parent topic:

DB Tools Set Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-set-parameter-value-c-vi.html language=enus -->
## TOPIC 00043: Set Parameter Value (C).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-set-parameter-value-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-set-parameter-value-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually

### Set Parameter Value (C).vi

Sets the value of the parameter at **parameter index** in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-set-parameter-value-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. value — value specifies the parameter value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Set Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-set-parameter-value-cr-vi.html language=enus -->
## TOPIC 00044: Set Parameter Value (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-set-parameter-value-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-set-parameter-value-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually

### Set Parameter Value (CR).vi

Sets the value of the parameter at **parameter index** in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-set-parameter-value-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. parameter index — parameter index specifies either the ordinal index of the parameter or the name of the parameter. value — value specifies the parameter value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Set Parameter Value VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-transaction-c-vi.html language=enus -->
## TOPIC 00045: Command (C).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-transaction-c-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-transaction-c-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command reference command reference specifies a reference to an ADO Command object. cen

### Command (C).vi

Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-transaction-c-vi.png']

#### Inputs/Outputs

| command reference — command reference specifies a reference to an ADO Command object. operation (begin) — operation specifies the operation you want to perform on the transaction. isolation level (chaos) — isolation level specifies the isolation level used for the transaction. You only need to set isolation level if other transactions might be pending at this same time. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference out — command reference out returns a reference to an ADO Command object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Database Transaction VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/cmd-transaction-cr-vi.html language=enus -->
## TOPIC 00046: Command (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/cmd-transaction-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/cmd-transaction-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset reference command-recordset reference specifies a reference that comb

### Command (CR).vi

Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='cmd-transaction-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. operation (begin) — operation specifies the operation you want to perform on the transaction. isolation level (chaos) — isolation level specifies the isolation level used for the transaction. You only need to set isolation level if other transactions might be pending at this same time. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Database Transaction VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/db-tools-create-parameterized-query-vi.html language=enus -->
## TOPIC 00047: DB Tools Create Parameterized Query VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/db-tools-create-parameterized-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/db-tools-create-parameterized-query-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a parameterized SQL query and returns a command reference that you must free eventually. Unless you are detecting the parameters automatically, the number of elements in the parameters array must match the number of parameters you specify in SQL query. For stored procedures, set stored proce

### DB Tools Create Parameterized Query VI

Creates a parameterized **SQL query** and returns a **command reference** that you must free eventually. Unless you are detecting the parameters automatically, the number of elements in the **parameters** array must match the number of parameters you specify in **SQL query**. For stored procedures, set **stored procedure** to TRUE and **SQL query** to the name of the procedure you want to execute.

[IMAGE alt='icon' src='db-tools-create-parameterized-query-vi.png']

#### Inputs/Outputs

| auto-detect parameters? (F) — auto-detect parameters? if TRUE, this VI attempts to detect the parameters automatically using the SQL query or the stored procedure name. Note Automatically detecting parameters can be a time-consuming process and is not supported by all databases and/or database providers/drivers. connection reference — connection reference specifies a reference to an ADO Connection object. SQL query — SQL query specifies a parameterized SQL query or stored procedure name. parameters — parameters specifies the parameter information. parameter name — parameter name is the name of parameter. type — type is the data type of parameter. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary direction — direction of the parameter value (Input, Output, Input/Output, or Return value). 0Input (default)1Output2Input/Output3Return Value value — value a variant that contains the parameter value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. stored procedure? (F) — stored procedure? specifies that this query is a stored procedure call. command reference — command reference returns a reference to an ADO Command object. parameters out — parameters out returns an array of clusters of parameter information. 0Input1Output2Input/Output3Return Value parameter name — parameter name is the name of parameter. type — type is the data type of parameter. direction — direction of the parameter value (Input, Output, Input/Output, or Return value). value — value a variant that contains the parameter value. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| parameter name — parameter name is the name of parameter. type — type is the data type of parameter. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary direction — direction of the parameter value (Input, Output, Input/Output, or Return value). 0Input (default)1Output2Input/Output3Return Value value — value a variant that contains the parameter value. |  |
| 0 | String |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
| 0 | Input (default) |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
| 0 | Input |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
| parameter name — parameter name is the name of parameter. type — type is the data type of parameter. direction — direction of the parameter value (Input, Output, Input/Output, or Return value). value — value a variant that contains the parameter value. |  |

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/db-tools-get-parameter-value-vi.html language=enus -->
## TOPIC 00048: DB Tools Get Parameter Value VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/db-tools-get-parameter-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/db-tools-get-parameter-value-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance

### DB Tools Get Parameter Value VI

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-get-parameter-value-vi.png']

- [String (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-c-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [String (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-string-parameter-value-cr-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Integer (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-c-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Integer (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-integer-parameter-value-cr-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Single (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-c-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Single (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-single-parameter-value-cr-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Double (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-c-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Double (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-double-parameter-value-cr-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Date/Time (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-c-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Date/Time (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-datetime-parameter-value-cr-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Binary (C)](../../../../vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-c-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Binary (CR)](../../../../vi-lib/addons/database/command-llb/cmd-get-binary-parameter-value-cr-vi.html) Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/db-tools-null-vi.html language=enus -->
## TOPIC 00049: DB Tools NULL VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/db-tools-null-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/db-tools-null-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a database variant that contains a NULL value. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ifxdt.png NULL NULL returns a database variant that contains a NU

### DB Tools NULL VI

Returns a database variant that contains a NULL value.

[IMAGE alt='icon' src='db-tools-null-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. NULL — NULL returns a database variant that contains a NULL value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/command-llb/db-tools-set-parameter-value-vi.html language=enus -->
## TOPIC 00050: DB Tools Set Parameter Value VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/command-llb/db-tools-set-parameter-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/command-llb/db-tools-set-parameter-value-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually

### DB Tools Set Parameter Value VI

Sets the value of the parameter at **parameter index** in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-set-parameter-value-vi.png']

- [Set Parameter Value (CR).vi](../../../../vi-lib/addons/database/command-llb/cmd-set-parameter-value-cr-vi.html) Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Set Parameter Value (C).vi](../../../../vi-lib/addons/database/command-llb/cmd-set-parameter-value-c-vi.html) Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/conn-execute-vi.html language=enus -->
## TOPIC 00051: Connection

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/conn-execute-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/conn-execute-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ci32.png cache size (1) cache size specifies the

### Connection

Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='conn-execute-vi.png']

#### Inputs/Outputs

| cache size (1) — cache size specifies the number of records to store in local memory. After you retrieve the number of records in local memory and you request the next record, the current set of records is discarded from local memory and the next set are retrieved into local memory. The default is 1. connection reference — connection reference specifies a reference to an ADO Connection object. SQL query — SQL query specifies the SQL statement to execute. cursor type — cursor type specifies the method for navigating the recordset. Some providers and/or databases do not support all cursors. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference — recordset reference returns a reference to an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Execute Query VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/conn-get-properties-vi.html language=enus -->
## TOPIC 00052: Connection

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/conn-get-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/conn-get-properties-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png connection reference c

### Connection

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='conn-get-properties-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. connection properties — connection properties returns the following properties that define the database connection. command timeout (s) — command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. connection string — connection string returns the connection string that the VI used to make the database connection. default database — default database returns the default database the VI used for the connection. Some providers might not support this use of this property. provider — provider returns the provider this VI used to make the database connection. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| command timeout (s) — command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. connection string — connection string returns the connection string that the VI used to make the database connection. default database — default database returns the default database the VI used for the connection. Some providers might not support this use of this property. provider — provider returns the provider this VI used to make the database connection. |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/conn-set-properties-vi.html language=enus -->
## TOPIC 00053: Connection

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/conn-set-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/conn-set-properties-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png connection reference connection reference specifies a reference to an ADO Connection

### Connection

Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='conn-set-properties-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. connection properties — connection properties contains the following properties that define the database connection. command timeout (s) — command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. connection string — connection string specifies the connection string that was used to make the database connection. This property is read-only. default database — default database is the default database to use for the connection. Some providers may not support this use of this property. provider — provider is the provider used to make the database connection. This property is read-only. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| command timeout (s) — command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. connection string — connection string specifies the connection string that was used to make the database connection. This property is read-only. default database — default database is the default database to use for the connection. Some providers may not support this use of this property. provider — provider is the provider used to make the database connection. This property is read-only. |

Parent topic:

DB Tools Set Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/conn-transaction-vi.html language=enus -->
## TOPIC 00054: Connection

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/conn-transaction-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/conn-transaction-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png connection reference connection reference specifies a reference to an ADO Connection ob

### Connection

Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='conn-transaction-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. operation (begin) — operation specifies the operation you want to perform on the transaction. isolation level (chaos) — isolation level specifies the isolation level used for the transaction. You only need to set isolation level if other transactions might be pending at this same time. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference out — connection reference out returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Database Transaction VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/db-tools-close-connection-vi.html language=enus -->
## TOPIC 00055: DB Tools Close Connection VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/db-tools-close-connection-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/db-tools-close-connection-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a database connection by destroying its associated connection reference. icon Inputs/Outputs cdlrn.png connection reference connection reference specifies a reference to an ADO Connection object. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this n

### DB Tools Close Connection VI

Closes a database connection by destroying its associated **connection reference**.

[IMAGE alt='icon' src='db-tools-close-connection-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/db-tools-open-connec-path-vi.html language=enus -->
## TOPIC 00056: DB Tools Open Connec (Path) VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/db-tools-open-connec-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/db-tools-open-connec-path-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the i

### DB Tools Open Connec (Path) VI

Opens a database connection using the connection information path and returns a connection reference. If **prompt?** is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the **connection information** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-open-connec-path-vi.png']

#### Inputs/Outputs

| userID — userID specifies the user ID needed to access the database. You might not need to specify a userID. connection information — connection information is the absolute path of the file that stores the connection information. For a Microsoft Data Link file, this path must have a .udl extension. A File DSN must have a .dsn extension. prompt? (F) — prompt? If TRUE, LabVIEW prompts you to determine connection parameters. Using this input is an alternative to using a connection string. If prompt? is TRUE, LabVIEW ignores the connection string and uses the prompt instead. connection timeout (15) — connection timeout determines the length of time (in seconds) to wait while attempting to make a connection to a database before quitting and returning an error. The default is 15. Setting this value to 0 instructs the VI to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. password — password specifies the password required to access the database for security purposes. You might not need to specify a password. connection reference — connection reference returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Open Connection VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/db-tools-open-connec-string-vi.html language=enus -->
## TOPIC 00057: DB Tools Open Connec (String) VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/db-tools-open-connec-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/db-tools-open-connec-string-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the i

### DB Tools Open Connec (String) VI

Opens a database connection using the connection information path and returns a connection reference. If **prompt?** is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the **connection information** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-open-connec-string-vi.png']

#### Inputs/Outputs

| userID — userID specifies the user ID needed to access the database. You might not need to specify a userID. connection information — connection information specifies the connection string to use to connect to the database. For User and System ODBC Data Sources, provide the name of the data source as configured in the Windows ODBC Administrator. You also can specify a path to a UDL or DSN file by prefixing the path with file name= or filedsn=, respectively. prompt? (F) — prompt? If TRUE, LabVIEW prompts you to determine connection parameters. Using this input is an alternative to using a connection string. If prompt? is TRUE, LabVIEW ignores the connection string and uses the prompt instead. connection timeout (15) — connection timeout determines the length of time (in seconds) to wait while attempting to make a connection to a database before quitting and returning an error. The default is 15. Setting this value to 0 instructs the VI to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. password — password specifies the password required to access the database for security purposes. You might not need to specify a password. connection reference — connection reference returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Open Connection VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/connection-llb/db-tools-open-connection-vi.html language=enus -->
## TOPIC 00058: DB Tools Open Connection VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/connection-llb/db-tools-open-connection-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/connection-llb/db-tools-open-connection-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the i

### DB Tools Open Connection VI

Opens a database connection using the connection information path and returns a connection reference. If **prompt?** is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the **connection information** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-open-connection-vi.png']

- [DB Tools Open Connec (Path) VI](../../../../vi-lib/addons/database/connection-llb/db-tools-open-connec-path-vi.html) Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the instance.
- [DB Tools Open Connec (String) VI](../../../../vi-lib/addons/database/connection-llb/db-tools-open-connec-string-vi.html) Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/db-variant-to-data/database-variant-to-data-xnode.html language=enus -->
## TOPIC 00059: Database Variant To Data

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/db-variant-to-data/database-variant-to-data-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/db-variant-to-data/database-variant-to-data-xnode.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a database variant to the LabVIEW data type specified in type so you can use the data in another function or subVI. icon Inputs/Outputs cfxdt.png type specifies the data type into which you want to convert variant data. cfxdt.png database variant specifies the variant data you want to conve

### Database Variant To Data

Converts a **database variant** to the LabVIEW data type specified in **type** so you can use the data in another function or subVI.

[IMAGE alt='icon' src='database-variant-to-data-xnode.png']

#### Inputs/Outputs

| type — specifies the data type into which you want to convert variant data. database variant — specifies the variant data you want to convert to the data type specified in type. You can wire a variant, a 1D array of variants, or a 2D array of variants to this input. Refer to the Details section of this topic for more information about using this input. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. data — returns the resulting data type. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Database Variant To Data Details

You can wire a variant, a 1D array of variants, or a 2D array of variants to the **database variant** input. Depending on the data type that you wire to the **type** and **database variant** inputs, this function performs the following different conversions:

| Data Type of "database variant" | Data Type of "type" |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Cluster | 1D Array of Non-Clusters | 1D Array of Clusters | 2D Array | Others |  |
| Variant | This function converts the variant to the LabVIEW data type specified in type. |  |  |  |  |
| 1D Array of Variants | Each element in the cluster defines a column. This function converts each element of the 1D array to a column in sequence. The output is a cluster. | This function converts each element of the 1D array to the element data type specified in type. The output is a 1D array. | This function converts each element of the 1D array to a cluster. The output is a 1D array of clusters. | The wire of database variant is broken. | The wire of database variant is broken. |
| 2D Array of Variants | The wire of database variant is broken. | The wire of database variant is broken. | This function converts each row of the 2D array to a cluster. The output is a 1D array of clusters. | This function converts each element of the 2D array to the element data type specified in type. The output is a 2D array. | The wire of database variant is broken. |
| Others | The wire of database variant is broken. |  |  |  |  |

#### Examples

Refer to the following VIs for examples of using the Database Variant To Data function:

- Convert Database Variant to Data VI: labview\examples\database
- Sixtypes Select VI: labview\examples\database
- Playback VI: labview\examples\database

Parent topic:

Database

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-fetch-element-data-vi.html language=enus -->
## TOPIC 00060: DB Tools Fetch Element Data VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-fetch-element-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-fetch-element-data-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### DB Tools Fetch Element Data VI

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-fetch-element-data-vi.png']

- [String (R)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-string-data-r-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [String (CR)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-string-data-cr-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Integer (R)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-r-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Integer (CR)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-cr-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Single (R)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-single-data-r-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Single (CR)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-single-data-cr-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Double (R)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-double-data-r-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Double (CR)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-double-data-cr-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Date/Time (R)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-r-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Date/Time (CR)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-cr-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Binary (CR)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-cr-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.
- [Binary (R)](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-r-vi.html) Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-fetch-next-recordset-vi.html language=enus -->
## TOPIC 00061: DB Tools Fetch Next Recordset VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-fetch-next-recordset-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-fetch-next-recordset-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the next recordset in a multi-recordset query identified by recordset reference. When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select t

### DB Tools Fetch Next Recordset VI

Retrieves the next recordset in a multi-recordset query identified by **recordset reference**. When the current recordset is no longer available, the **recordset reference** is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-fetch-next-recordset-vi.png']

- [Fetch Next Recordset (R).vi](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-r-vi.html) Retrieves the next recordset in a multi-recordset query identified by recordset reference . When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Fetch Next Recordset (CR).vi](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-cr-vi.html) Retrieves the next recordset in a multi-recordset query identified by recordset reference . When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-fetch-recordset-data-vi.html language=enus -->
## TOPIC 00062: DB Tools Fetch Recordset Data VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-fetch-recordset-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-fetch-recordset-data-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the

### DB Tools Fetch Recordset Data VI

Retrieves the data in the recordset identified by the **recordset reference** input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-fetch-recordset-data-vi.png']

- [Fetch Recordset Data (R).vi](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-r-vi.html) Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Fetch Recordset Data (CR).vi](../../../../vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-cr-vi.html) Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-load-recordset-from-file-vi.html language=enus -->
## TOPIC 00063: DB Tools Load Recordset From File VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-load-recordset-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-load-recordset-from-file-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a recordset from a file and returns a recordset reference that identifies this recordset. You can retrieve data from this recordset like any other recordset, but some properties might not be available on this recordset. icon Inputs/Outputs cdlrn.png connection reference connection reference sp

### DB Tools Load Recordset From File VI

Loads a recordset from a file and returns a **recordset reference** that identifies this recordset. You can retrieve data from this recordset like any other recordset, but some properties might not be available on this recordset.

[IMAGE alt='icon' src='db-tools-load-recordset-from-file-vi.png']

#### Inputs/Outputs

| connection reference — connection reference specifies a reference to an ADO Connection object. file name — file name specifies the file path to the file from which you want to read the data. cache size (1) — cache size determines how many records to store in local memory. After the number of records kept in local memory are visited and the next record is requested, the current set of records are discarded from local memory, and the next set are retrieved into local memory. The default is 1. Adjusting this setting might improve performance when fetching records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference — recordset reference returns a reference to an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-move-to-next-record-vi.html language=enus -->
## TOPIC 00064: DB Tools Move To Next Record VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-move-to-next-record-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-move-to-next-record-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Move To Next Record VI

Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-move-to-next-record-vi.png']

- [Move To Next Record (CR).vi](../../../../vi-lib/addons/database/recordset-llb/rec-move-to-next-record-cr-vi.html) Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Move To Next Record (R).vi](../../../../vi-lib/addons/database/recordset-llb/rec-move-to-next-record-r-vi.html) Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-move-to-previous-record-vi.html language=enus -->
## TOPIC 00065: DB Tools Move To Previous Record VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-move-to-previous-record-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-move-to-previous-record-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Move To Previous Record VI

Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-move-to-previous-record-vi.png']

- [Move To Previous Record (R).vi](../../../../vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-r-vi.html) Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Move To Previous Record (CR).vi](../../../../vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-cr-vi.html) Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-move-to-record-n-vi.html language=enus -->
## TOPIC 00066: DB Tools Move To Record N VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-move-to-record-n-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-move-to-record-n-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon

### DB Tools Move To Record N VI

Moves the cursor to point to record **n** in the recordset. To move the cursor to the last record, set **n** to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-move-to-record-n-vi.png']

- [Move To Record N (R).vi](../../../../vi-lib/addons/database/recordset-llb/rec-move-to-record-n-r-vi.html) Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Move To Record N (CR).vi](../../../../vi-lib/addons/database/recordset-llb/rec-move-to-record-n-cr-vi.html) Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Advanced

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/db-tools-save-recordset-to-file-vi.html language=enus -->
## TOPIC 00067: DB Tools Save Recordset To File VI

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/db-tools-save-recordset-to-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/db-tools-save-recordset-to-file-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into Lab

### DB Tools Save Recordset To File VI

Saves the recordset identified by the **recordset reference** to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI.

Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='db-tools-save-recordset-to-file-vi.png']

- [Save Recordset To File (R).vi](../../../../vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-r-vi.html) Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.
- [Save Recordset To File (CR).vi](../../../../vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-cr-vi.html) Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-destroy-command-vi.html language=enus -->
## TOPIC 00068: Command-Recordset

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-destroy-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-destroy-command-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset reference command-recordset reference specif

### Command-Recordset

Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-destroy-command-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command reference — command reference returns a reference to an ADO Command object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Free Object VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-destroy-connection-vi.html language=enus -->
## TOPIC 00069: Recordset

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-destroy-connection-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-destroy-connection-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png recordset reference recordset reference specifies a reference

### Recordset

Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-destroy-connection-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. connection reference — connection reference returns a reference to an ADO Connection object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Free Object VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-cr-vi.html language=enus -->
## TOPIC 00070: Binary (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Binary (CR)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-binary-data-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. data — data returns the data retrieved from the recordset. Use the Database Variant To Data function to convert this data to its native LabVIEW data type. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-r-vi.html language=enus -->
## TOPIC 00071: Binary (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-binary-data-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Binary (R)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-binary-data-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. data — data returns the data retrieved from the recordset. Use the Database Variant To Data function to convert this data to its native LabVIEW data type. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-cr-vi.html language=enus -->
## TOPIC 00072: Date/Time (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Date/Time (CR)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-datetime-data-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-r-vi.html language=enus -->
## TOPIC 00073: Date/Time (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-datetime-data-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Date/Time (R)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-datetime-data-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-double-data-cr-vi.html language=enus -->
## TOPIC 00074: Double (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-double-data-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-double-data-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Double (CR)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-double-data-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-double-data-r-vi.html language=enus -->
## TOPIC 00075: Double (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-double-data-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-double-data-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Double (R)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-double-data-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-cr-vi.html language=enus -->
## TOPIC 00076: Integer (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Integer (CR)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-integer-data-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-r-vi.html language=enus -->
## TOPIC 00077: Integer (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-integer-data-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Integer (R)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-integer-data-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-cr-vi.html language=enus -->
## TOPIC 00078: Fetch Next Recordset (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the next recordset in a multi-recordset query identified by recordset reference. When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select t

### Fetch Next Recordset (CR).vi

Retrieves the next recordset in a multi-recordset query identified by **recordset reference**. When the current recordset is no longer available, the **recordset reference** is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-next-recordset-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Next Recordset VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-r-vi.html language=enus -->
## TOPIC 00079: Fetch Next Recordset (R).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-next-recordset-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the next recordset in a multi-recordset query identified by recordset reference. When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select t

### Fetch Next Recordset (R).vi

Retrieves the next recordset in a multi-recordset query identified by **recordset reference**. When the current recordset is no longer available, the **recordset reference** is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-next-recordset-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Next Recordset VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-cr-vi.html language=enus -->
## TOPIC 00080: Fetch Recordset Data (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the

### Fetch Recordset Data (CR).vi

Retrieves the data in the recordset identified by the **recordset reference** input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-recordset-data-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. recordset data — recordset data returns an array of database variants that contains the selected data. Use the Database Variant To Data function to convert this data type to its native LabVIEW data type. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Recordset Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-r-vi.html language=enus -->
## TOPIC 00081: Fetch Recordset Data (R).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-recordset-data-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the

### Fetch Recordset Data (R).vi

Retrieves the data in the recordset identified by the **recordset reference** input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-recordset-data-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. recordset data — recordset data returns an array of database variants that contains the selected data. Use the Database Variant To Data function to convert this data type to its native LabVIEW data type. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Recordset Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-single-data-cr-vi.html language=enus -->
## TOPIC 00082: Single (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-single-data-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-single-data-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Single (CR)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-single-data-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-single-data-r-vi.html language=enus -->
## TOPIC 00083: Single (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-single-data-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-single-data-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### Single (R)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-single-data-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-string-data-cr-vi.html language=enus -->
## TOPIC 00084: String (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-string-data-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-string-data-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### String (CR)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-string-data-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-fetch-string-data-r-vi.html language=enus -->
## TOPIC 00085: String (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-fetch-string-data-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-fetch-string-data-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic ins

### String (R)

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-fetch-string-data-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. column index — column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. type — type specifies the type of data in the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. data — data returns the data retrieved from the recordset. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Fetch Element Data VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-get-column-properties-cr-vi.html language=enus -->
## TOPIC 00086: Column (CR)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-get-column-properties-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-get-column-properties-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset refe

### Column (CR)

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-get-column-properties-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. column index — column index specifies either the ordinal index of the column or the name of the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. column properties — column properties returns the following properties defined for a column. name — This property is read-only. database data type — This property is read-only. defined size — This property is read-only. actual size — This property is read-only. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| name — This property is read-only. database data type — This property is read-only. defined size — This property is read-only. actual size — This property is read-only. |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-get-column-properties-r-vi.html language=enus -->
## TOPIC 00087: Column (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-get-column-properties-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-get-column-properties-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png recordset reference re

### Column (R)

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-get-column-properties-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. column index — column index specifies either the ordinal index of the column or the name of the column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. column properties — column properties returns the following properties defined for a column. name — This property is read-only. database data type — This property is read-only. defined size — This property is read-only. actual size — This property is read-only. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| name — This property is read-only. database data type — This property is read-only. defined size — This property is read-only. actual size — This property is read-only. |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-cr-vi.html language=enus -->
## TOPIC 00088: Recordset (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset refe

### Recordset (CR).vi

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-get-recordset-properties-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. recordset properties — recordset properties returns the various properties associated with a recordset object. column count — column count returns the number of columns in the recordset. record index — record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of -2 means that the property is not supported. Values of -3 and -4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. record count — record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns -1. bof? — bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. eof? — eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. cursor type — cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. cache size — cache size returns how many records are kept in local memory. state — state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| column count — column count returns the number of columns in the recordset. record index — record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of -2 means that the property is not supported. Values of -3 and -4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. record count — record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns -1. bof? — bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. eof? — eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. cursor type — cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. cache size — cache size returns how many records are kept in local memory. state — state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-r-vi.html language=enus -->
## TOPIC 00089: Recordset (R)

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-get-recordset-properties-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png recordset reference re

### Recordset (R)

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-get-recordset-properties-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. recordset properties — recordset properties returns the various properties associated with a recordset object. column count — column count returns the number of columns in the recordset. record index — record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of -2 means that the property is not supported. Values of -3 and -4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. record count — record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns -1. bof? — bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. eof? — eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. cursor type — cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. cache size — cache size returns how many records are kept in local memory. state — state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| column count — column count returns the number of columns in the recordset. record index — record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of -2 means that the property is not supported. Values of -3 and -4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. record count — record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns -1. bof? — bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. eof? — eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. cursor type — cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. cache size — cache size returns how many records are kept in local memory. state — state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. |

Parent topic:

DB Tools Get Properties VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-move-to-next-record-cr-vi.html language=enus -->
## TOPIC 00090: Move To Next Record (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-move-to-next-record-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-move-to-next-record-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset reference command-recordset reference specifies a

### Move To Next Record (CR).vi

Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-move-to-next-record-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Move To Next Record VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-move-to-next-record-r-vi.html language=enus -->
## TOPIC 00091: Move To Next Record (R).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-move-to-next-record-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-move-to-next-record-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png recordset reference recordset reference specifies a reference to an

### Move To Next Record (R).vi

Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-move-to-next-record-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Move To Next Record VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-cr-vi.html language=enus -->
## TOPIC 00092: Move To Previous Record (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png command-recordset reference command-recor

### Move To Previous Record (CR).vi

Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-move-to-previous-record-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Move To Previous Record VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-r-vi.html language=enus -->
## TOPIC 00093: Move To Previous Record (R).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-move-to-previous-record-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png recordset reference recordset reference s

### Move To Previous Record (R).vi

Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-move-to-previous-record-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Move To Previous Record VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-move-to-record-n-cr-vi.html language=enus -->
## TOPIC 00094: Move To Record N (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-move-to-record-n-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-move-to-record-n-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png

### Move To Record N (CR).vi

Moves the cursor to point to record **n** in the recordset. To move the cursor to the last record, set **n** to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-move-to-record-n-cr-vi.png']

#### Inputs/Outputs

| command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. n (0) — n specifies to which recordset to move the cursor. To move the cursor to point to the last record, set n to -1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Move To Record N VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-move-to-record-n-r-vi.html language=enus -->
## TOPIC 00095: Move To Record N (R).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-move-to-record-n-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-move-to-record-n-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdlrn.png

### Move To Record N (R).vi

Moves the cursor to point to record **n** in the recordset. To move the cursor to the last record, set **n** to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-move-to-record-n-r-vi.png']

#### Inputs/Outputs

| recordset reference — recordset reference specifies a reference to an ADO Recordset object. n (0) — n specifies to which recordset to move the cursor. To move the cursor to point to the last record, set n to -1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Move To Record N VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-cr-vi.html language=enus -->
## TOPIC 00096: Save Recordset To File (CR).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-cr-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-cr-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into Lab

### Save Recordset To File (CR).vi

Saves the recordset identified by the **recordset reference** to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI.

Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-save-recordset-to-file-cr-vi.png']

#### Inputs/Outputs

| overwrite? (F) — overwrite? determines whether to overwrite the file specified in file name if the file already exists. command-recordset reference — command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. file name — file name specifies the path where you want to save the file. You can click the Browse button to navigate to the correct file path. save format (XML) — save format specifies the format to use when saving a recordset to file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. command-recordset reference out — command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Save Recordset To File VI

<!--NI_TOPIC bundle=lvdct-api-ref path=vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-r-vi.html language=enus -->
## TOPIC 00097: Save Recordset To File (R).vi

- bundle_id: `lvdct-api-ref`
- source_path: `vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-r-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdct-api-ref/raw/resource/enus/vi-lib/addons/database/recordset-llb/rec-save-recordset-to-file-r-vi.html
- document_id: `lvdct-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into Lab

### Save Recordset To File (R).vi

Saves the recordset identified by the **recordset reference** to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI.

Wire data to the reference input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='rec-save-recordset-to-file-r-vi.png']

#### Inputs/Outputs

| overwrite? (F) — overwrite? determines whether to overwrite the file specified in file name if the file already exists. recordset reference — recordset reference specifies a reference to an ADO Recordset object. file name — file name specifies the path where you want to save the file. You can click the Browse button to navigate to the correct file path. save format (XML) — save format specifies the format to use when saving a recordset to file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. recordset reference out — recordset reference out returns a reference to an ADO Recordset object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DB Tools Save Recordset To File VI
