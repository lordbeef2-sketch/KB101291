# NI DOCUMENT BUNDLE: labview-database-connectivity-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-database-connectivity-toolkit-api-ref start=1 end=32 -->
<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/database_variant_to_data.html language=enus -->
## TOPIC 00001: Database Variant To Data Function

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/database_variant_to_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/database_variant_to_data.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Database Variant To Data Function

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Converts a **database variant** to the LabVIEW data type specified in **type** so you can use the data in another function or VI.

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='database_variant_to_data.gif']

|  | type specifies the data type into which you want to convert variant data. |
| --- | --- |
|  | database variant specifies the variant data you want to convert to the data type specified in type. You can wire a variant, a 1D array of variants, or a 2D array of variants to this input. Refer to the Details section of this topic for more information about using this input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | data returns the resulting data type. |
|  | error out contains error information. This output provides standard error out functionality. |

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

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/database_vis.html language=enus -->
## TOPIC 00002: Database VIs and Function

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/database_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/database_vis.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Database VIs and Function

**Requires:** Database Connectivity Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Database VIs and function to access databases from LabVIEW.

With the Database VIs and function, you can perform the most common database tasks, including the following:

- Work with any provider that adheres to the Microsoft ActiveX Data Object (ADO) standard.
- Work with any database driver that complies with ODBC or OLE DB.
- Maintain a high level of portability. In many cases, you can port your application to another database by changing the connection string you pass to the DB Tools Open Connection VI.
- Convert database column values from native data types to standard LabVIEW Database Connectivity Toolkit data types.
- Use SQL statements with all supported database systems, including non-SQL systems, using the default ADO ODBC provider.
- Retrieve the name and data type of a column returned by a SELECT statement.
- Create tables and select, insert, update, and delete records without using SQL statements.

The VIs and function on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Database Variant To Data | Converts a database variant to the LabVIEW data type specified in type so you can use the data in another function or VI. |
| DB Tools Close Connection | Closes a database connection by destroying its associated connection reference. |
| DB Tools Create Table | Creates a new table in the database identified by connection reference. The table and column information inputs describe the name of the table and the properties of each column in the table, respectively. |
| DB Tools Delete Data | Deletes data from a database identified by connection reference. |
| DB Tools Drop Table | Deletes the specified table from the database identified by connection reference. |
| DB Tools Insert Data | Inserts a new row into the table in the database identified by the connection reference. |
| DB Tools Open Connection | Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Select Data | Selects data from the table in the database identified by connection reference using the columns supplied in the columns array. |
| DB Tools Update Data | Updates the data in a database identified by connection reference. |

| Subpalette | Description |
| --- | --- |
| Advanced VIs | Use the Advanced VIs to perform advanced database operations such as executing SQL statements and fetching data. You might need to use SQL when you use these VIs. |
| Utility VIs | Use the Utility VIs for a variety of operations, including getting table and column information, getting and setting database properties, formatting data and time data, performing database transactions, and writing and reading data files. |

© 1999–2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_advanced_vis.html language=enus -->
## TOPIC 00003: Advanced VIs

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_advanced_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_advanced_vis.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Advanced VIs

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Advanced VIs to perform advanced database operations such as executing SQL statements and fetching data. You might need to use SQL when you use these VIs.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| DB Tools Create Parameterized Query | Creates a parameterized SQL query and returns a command reference that you must free eventually. Unless you are detecting the parameters automatically, the number of elements in the parameters array must match the number of parameters you specify in SQL query. For stored procedures, set stored procedure to TRUE and SQL query to the name of the procedure you want to execute. |
| DB Tools Execute Query | Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Fetch Element Data | Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference. The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Fetch Next Recordset | Retrieves the next recordset in a multi-recordset query identified by recordset reference. When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Fetch Recordset Data | Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Free Object | Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Get Parameter Value | Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Move To Next Record | Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Move To Previous Record | Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Move To Record N | Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to –1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Null | Returns a database variant that contains a NULL value. |
| DB Tools Set Parameter Value | Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_load_recordset_from_file.html language=enus -->
## TOPIC 00004: DB Tools Load Recordset From File VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_load_recordset_from_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_load_recordset_from_file.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Load Recordset From File VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Loads a recordset from a file and returns a **recordset reference** that identifies this recordset. You can retrieve data from this recordset like any other recordset, but some properties might not be available on this recordset.

[IMAGE alt='image' src='db_tools_load_recordset_from_file.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | file name specifies the file path to the file from which you want to read the data. |
|  | cache size determines how many records to store in local memory. After the number of records kept in local memory are visited and the next record is requested, the current set of records are discarded from local memory, and the next set are retrieved into local memory. The default is 1. Adjusting this setting might improve performance when fetching records. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference returns a reference to an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_open_connec.html language=enus -->
## TOPIC 00005: DB Tools Open Connection VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_open_connec.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_open_connec.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Open Connection VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Opens a database connection using the connection information path and returns a connection reference. If **prompt?** is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the **connection information** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### DB Tools Open Connec (Path)

[IMAGE alt='image' src='db_tools_open_connec_(path).gif']

|  | userID specifies the user ID needed to access the database. You might not need to specify a userID. |
| --- | --- |
|  | connection information is the absolute path of the file that stores the connection information. For a Microsoft Data Link file, this path must have a .udl extension. A File DSN must have a .dsn extension. |
|  | prompt? If TRUE, LabVIEW prompts you to determine connection parameters. Using this input is an alternative to using a connection string. If prompt? is TRUE, LabVIEW ignores the connection string and uses the prompt instead. |
|  | connection timeout determines the length of time (in seconds) to wait while attempting to make a connection to a database before quitting and returning an error. The default is 15. Setting this value to 0 instructs the VI to wait indefinitely. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | password specifies the password required to access the database for security purposes. You might not need to specify a password. |
|  | connection reference returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### DB Tools Open Connec (String)

[IMAGE alt='image' src='db_tools_open_connec_(string).gif']

|  | userID specifies the user ID needed to access the database. You might not need to specify a userID. |
| --- | --- |
|  | connection information specifies the connection string to use to connect to the database. For User and System ODBC Data Sources, provide the name of the data source as configured in the Windows ODBC Administrator. You also can specify a path to a UDL or DSN file by prefixing the path with file name= or filedsn=, respectively. |
|  | prompt? If TRUE, LabVIEW prompts you to determine connection parameters. Using this input is an alternative to using a connection string. If prompt? is TRUE, LabVIEW ignores the connection string and uses the prompt instead. |
|  | connection timeout determines the length of time (in seconds) to wait while attempting to make a connection to a database before quitting and returning an error. The default is 15. Setting this value to 0 instructs the VI to wait indefinitely. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | password specifies the password required to access the database for security purposes. You might not need to specify a password. |
|  | connection reference returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Open Connection VI:

- Connect to ACCDB Database VI: labview\examples\database
- Database Connection VI: labview\examples\database
- Telecommunications Parametric Testing VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_close_connection.html language=enus -->
## TOPIC 00006: DB Tools Close Connection VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_close_connection.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_close_connection.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Close Connection VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Closes a database connection by destroying its associated **connection reference**.

[Examples](#examples)

[IMAGE alt='image' src='db_tools_close_connection.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Close Connection VI:

- Connect to ACCDB Database VI: labview\examples\database
- Database Connection VI: labview\examples\database
- Telecommunications Parametric Testing VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_create_param_query.html language=enus -->
## TOPIC 00007: DB Tools Create Parameterized Query VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_create_param_query.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_create_param_query.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Create Parameterized Query VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Creates a parameterized **SQL query** and returns a **command reference** that you must free eventually. Unless you are detecting the parameters automatically, the number of elements in the **parameters** array must match the number of parameters you specify in **SQL query**. For stored procedures, set **stored procedure** to TRUE and **SQL query** to the name of the procedure you want to execute.

[Examples](#examples)

[IMAGE alt='image' src='db_tools_create_parameterized_query.gif']

|  | auto-detect parameters? if TRUE, this VI attempts to detect the parameters automatically using the SQL query or the stored procedure name. Note Automatically detecting parameters can be a time-consuming process and is not supported by all databases and/or database providers/drivers. |
| --- | --- |
|  | Note Automatically detecting parameters can be a time-consuming process and is not supported by all databases and/or database providers/drivers. |
|  | connection reference specifies a reference to an ADO Connection object. |
|  | SQL query specifies a parameterized SQL query or stored procedure name. |
|  | parameters specifies the parameter information. parameter name specifies the name of parameter. type specifies the data type of parameter. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary direction specifies the direction of the parameter value. 0Input (default)1Output2Input/Output3Return Value value specifies the parameter value. |
|  | parameter name specifies the name of parameter. |
|  | type specifies the data type of parameter. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary |
| 0 | String |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
|  | direction specifies the direction of the parameter value. 0Input (default)1Output2Input/Output3Return Value |
| 0 | Input (default) |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
|  | value specifies the parameter value. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | stored procedure? specifies that this query is a stored procedure call. |
|  | command reference returns a reference to an ADO Command object. |
|  | parameters out returns an array of clusters of parameter information. parameter name returns the name of parameter. type returns the data type of parameter. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary direction returns the direction of the parameter value. 0Input1Output2Input/Output3Return Value value returns the parameter value. |
|  | parameter name returns the name of parameter. |
|  | type returns the data type of parameter. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary |
| 0 | String |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
|  | direction returns the direction of the parameter value. 0Input1Output2Input/Output3Return Value |
| 0 | Input |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
|  | value returns the parameter value. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Create Parameterized Query VI:

- Database Insert VI: labview\examples\database
- Database Logging (parameterized) VI: labview\examples\database
- Parameterized VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_create_table.html language=enus -->
## TOPIC 00008: DB Tools Create Table VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_create_table.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_create_table.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Create Table VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Creates a new table in the database identified by **connection reference**. The **table** and **column information** inputs describe the name of the table and the properties of each column in the table, respectively.

[Examples](#examples)

[IMAGE alt='image' src='db_tools_create_table.gif']

|  | primary key specifies the column that is going to be the primary key for the table. The default is –1, which means the table does not have a primary key. |
| --- | --- |
|  | connection reference specifies a reference to an ADO Connection object. |
|  | table is the name of the table in the database to create. |
|  | column information specifies an array of clusters that describe each column to be created. column name specifies the name of column in database. data type specifies the data type of the column. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary size specifies the size of the column in the database. This VI uses this parameter for string data types only. If you specify a size of 0, the database provider specifies the maximum string size. allow null? specifies if the column allows NULL values. |
|  | column name specifies the name of column in database. |
|  | data type specifies the data type of the column. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary |
| 0 | String |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
|  | size specifies the size of the column in the database. This VI uses this parameter for string data types only. If you specify a size of 0, the database provider specifies the maximum string size. |
|  | allow null? specifies if the column allows NULL values. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | use file? specifies whether to use a user-supplied file to determine native database types. The default is FALSE. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Create Table VI:

- Create DatabaseTable VI: labview\examples\database
- Sixtypes Insert VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_database_transaction.html language=enus -->
## TOPIC 00009: DB Tools Database Transaction VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_database_transaction.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_database_transaction.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Database Transaction VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### Connection

[IMAGE alt='image' src='db_tools_database_transaction.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | operation specifies the operation you want to perform on the transaction. beginStarts a transaction.commitCommits the transaction to the database.rollbackDiscards the changes made to the database and restores the state of the database to the point when the transaction began. |
| begin | Starts a transaction. |
| commit | Commits the transaction to the database. |
| rollback | Discards the changes made to the database and restores the state of the database to the point when the transaction began. |
|  | isolation level specifies the isolation level used for the transaction. You only need to set isolation level if other transactions might be pending at this same time. chaosTransactions can overwrite each other.read committedThis transaction cannot see changes made by other transactions until they are committed. Dirty reads are not possible, but non-repeatable reads and phantom reads are possible.read uncommittedYou cannot see uncommitted records from another transaction. Dirty reads, non-repeatable reads, and phantom reads are all possible.repeatable readYou cannot see any changes in records without requerying the database. Dirty reads and non-repeatable reads are not possible, but phantom reads are possible.serializableThe transaction occurs in complete isolation. Dirty reads, non-repeatable reads, and phantom reads are not possible. |
| chaos | Transactions can overwrite each other. |
| read committed | This transaction cannot see changes made by other transactions until they are committed. Dirty reads are not possible, but non-repeatable reads and phantom reads are possible. |
| read uncommitted | You cannot see uncommitted records from another transaction. Dirty reads, non-repeatable reads, and phantom reads are all possible. |
| repeatable read | You cannot see any changes in records without requerying the database. Dirty reads and non-repeatable reads are not possible, but phantom reads are possible. |
| serializable | The transaction occurs in complete isolation. Dirty reads, non-repeatable reads, and phantom reads are not possible. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command (C)

[IMAGE alt='image' src='cmd_transaction_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | operation specifies the operation you want to perform on the transaction. beginStarts a transaction.commitCommits the transaction to the database.rollbackDiscards the changes made to the database and restores the state of the database to the point when the transaction began. |
| begin | Starts a transaction. |
| commit | Commits the transaction to the database. |
| rollback | Discards the changes made to the database and restores the state of the database to the point when the transaction began. |
|  | isolation level specifies the isolation level used for the transaction. You only need to set isolation level if other transactions might be pending at this same time. chaosTransactions can overwrite each other.read committedThis transaction cannot see changes made by other transactions until they are committed. Dirty reads are not possible, but non-repeatable reads and phantom reads are possible.read uncommittedYou cannot see uncommitted records from another transaction. Dirty reads, non-repeatable reads, and phantom reads are all possible.repeatable readYou cannot see any changes in records without requerying the database. Dirty reads and non-repeatable reads are not possible, but phantom reads are possible.serializableThe transaction occurs in complete isolation. Dirty reads, non-repeatable reads, and phantom reads are not possible. |
| chaos | Transactions can overwrite each other. |
| read committed | This transaction cannot see changes made by other transactions until they are committed. Dirty reads are not possible, but non-repeatable reads and phantom reads are possible. |
| read uncommitted | You cannot see uncommitted records from another transaction. Dirty reads, non-repeatable reads, and phantom reads are all possible. |
| repeatable read | You cannot see any changes in records without requerying the database. Dirty reads and non-repeatable reads are not possible, but phantom reads are possible. |
| serializable | The transaction occurs in complete isolation. Dirty reads, non-repeatable reads, and phantom reads are not possible. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command (CR)

[IMAGE alt='image' src='cmd_transaction_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | operation specifies the operation you want to perform on the transaction. beginStarts a transaction.commitCommits the transaction to the database.rollbackDiscards the changes made to the database and restores the state of the database to the point when the transaction began. |
| begin | Starts a transaction. |
| commit | Commits the transaction to the database. |
| rollback | Discards the changes made to the database and restores the state of the database to the point when the transaction began. |
|  | isolation level specifies the isolation level used for the transaction. You only need to set isolation level if other transactions might be pending at this same time. chaosTransactions can overwrite each other.read committedThis transaction cannot see changes made by other transactions until they are committed. Dirty reads are not possible, but non-repeatable reads and phantom reads are possible.read uncommittedYou cannot see uncommitted records from another transaction. Dirty reads, non-repeatable reads, and phantom reads are all possible.repeatable readYou cannot see any changes in records without requerying the database. Dirty reads and non-repeatable reads are not possible, but phantom reads are possible.serializableThe transaction occurs in complete isolation. Dirty reads, non-repeatable reads, and phantom reads are not possible. |
| chaos | Transactions can overwrite each other. |
| read committed | This transaction cannot see changes made by other transactions until they are committed. Dirty reads are not possible, but non-repeatable reads and phantom reads are possible. |
| read uncommitted | You cannot see uncommitted records from another transaction. Dirty reads, non-repeatable reads, and phantom reads are all possible. |
| repeatable read | You cannot see any changes in records without requerying the database. Dirty reads and non-repeatable reads are not possible, but phantom reads are possible. |
| serializable | The transaction occurs in complete isolation. Dirty reads, non-repeatable reads, and phantom reads are not possible. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Database Transaction VI in the labview\examples\database directory for an example of using the DB Tools Database Transaction VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_delete_data.html language=enus -->
## TOPIC 00010: DB Tools Delete Data VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_delete_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_delete_data.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Delete Data VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Deletes data from a database identified by **connection reference**.

[Example](#examples)

[IMAGE alt='image' src='db_tools_delete_data.gif']

|  | condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of a delete statement. For example, where (col1 > 10). If you wire an empty string to this input, this VI deletes all data from table. |
| --- | --- |
|  | connection reference specifies a reference to an ADO Connection object. |
|  | table specifies the name of the table whose data you want to delete. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Database Delete VI in the labview\examples\database directory for an example of using the DB Tools Delete Data VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_drop_table.html language=enus -->
## TOPIC 00011: DB Tools Drop Table VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_drop_table.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_drop_table.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Drop Table VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Deletes the specified **table** from the database identified by **connection reference**.

[Examples](#examples)

[IMAGE alt='image' src='db_tools_drop_table.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | table is the name of the table in the database to delete. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Drop Table VI:

- Database Transaction VI: labview\examples\database
- Sixtypes Insert VI: labview\examples\database
- Telecommunications Parametric Testing VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_execute_query.html language=enus -->
## TOPIC 00012: DB Tools Execute Query VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_execute_query.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_execute_query.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Execute Query VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Executes an SQL query and returns a recordset reference that you must eventually free with the [DB Tools Free Object](../lvdatabase/db_tools_free_object.html) VI. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### Connection

[IMAGE alt='image' src='db_tools_execute_query.gif']

|  | cache size specifies the number of records to store in local memory. After you retrieve the number of records in local memory and you request the next record, the current set of records is discarded from local memory and the next set are retrieved into local memory. The default is 1. Adjusting this setting might improve performance when fetching records. However, if the cursor type input is set to forward-only, you must use the default cache size of 1. If you select a different cursor type, you can set cache size to any value greater than 0. |
| --- | --- |
|  | connection reference specifies a reference to an ADO Connection object. |
|  | SQL query specifies the SQL statement to execute. |
|  | cursor type specifies the method for navigating the recordset. Some providers and/or databases do not support all cursors. dynamicAllows forward and backward navigation. You are able to see all changes other users make to the database.forward-onlyPermits only forward movement through the recordset. Any changes other users make to the database during navigation are not visible. This method provides the highest performance.keysetAllows forward and backward navigation. You are able to see records that other users add, but records deleted by other users are not removed from view.staticAllows forward and backward navigation with no ability to see any changes that other users make during navigation. |
| dynamic | Allows forward and backward navigation. You are able to see all changes other users make to the database. |
| forward-only | Permits only forward movement through the recordset. Any changes other users make to the database during navigation are not visible. This method provides the highest performance. |
| keyset | Allows forward and backward navigation. You are able to see records that other users add, but records deleted by other users are not removed from view. |
| static | Allows forward and backward navigation with no ability to see any changes that other users make during navigation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference returns a reference to an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command

[IMAGE alt='image' src='cmd_execute.gif']

|  | cache size specifies the number of records to store in local memory. After you retrieve the number of records in local memory and you request the next record, the current set of records is discarded from local memory and the next set are retrieved into local memory. The default is 1. Adjusting this setting might improve performance when fetching records. However, if the cursor type input is set to forward-only, you must use the default cache size of 1. If you select a different cursor type, you can set cache size to any value greater than 0. |
| --- | --- |
|  | command reference specifies a reference to an ADO Command object. |
|  | cursor type specifies the method for navigating the recordset. Some providers and/or databases do not support all cursors. dynamicAllows forward and backward navigation. You are able to see all changes other users make to the database.forward-onlyPermits only forward movement through the recordset. Any changes other users make to the database during navigation are not visible. This method provides the highest performance.keysetAllows forward and backward navigation. You are able to see records that other users add, but records deleted by other users are not removed from view.staticAllows forward and backward navigation with no ability to see any changes that other users make during navigation. |
| dynamic | Allows forward and backward navigation. You are able to see all changes other users make to the database. |
| forward-only | Permits only forward movement through the recordset. Any changes other users make to the database during navigation are not visible. This method provides the highest performance. |
| keyset | Allows forward and backward navigation. You are able to see records that other users add, but records deleted by other users are not removed from view. |
| static | Allows forward and backward navigation with no ability to see any changes that other users make during navigation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Database Fetching VI in the labview\examples\database directory for an example of using the DB Tools Execute Query VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_fetch_element_data.html language=enus -->
## TOPIC 00013: DB Tools Fetch Element Data VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_fetch_element_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_fetch_element_data.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Fetch Element Data VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Retrieves the data located at the **column index** of the current record in the recordset identified by the **recordset reference**. The **column index** can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the **type** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### String (R)

[IMAGE alt='image' src='db_tools_fetch_element_data.gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### String (CR)

[IMAGE alt='image' src='rec_fetch_string_data_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Integer (R)

[IMAGE alt='image' src='rec_fetch_integer_data_(r).gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Integer (CR)

[IMAGE alt='image' src='rec_fetch_integer_data_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Single (R)

[IMAGE alt='image' src='rec_fetch_single_data_(r).gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Single (CR)

[IMAGE alt='image' src='rec_fetch_single_data_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Double (R)

[IMAGE alt='image' src='rec_fetch_double_data_(r).gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Double (CR)

[IMAGE alt='image' src='rec_fetch_double_data_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Date/Time (R)

[IMAGE alt='image' src='rec_fetch_datetime_data_(r).gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Date/Time (CR)

[IMAGE alt='image' src='rec_fetch_datetime_data_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Binary (CR)

[IMAGE alt='image' src='rec_fetch_binary_data_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. Use the Database Variant To Data function to convert this data to its native LabVIEW data type. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Binary (R)

[IMAGE alt='image' src='rec_fetch_binary_data_(r).gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | column index specifies the column from which to retrieve the data. column index can be either an integer, which represents the column position in the table (zero-indexed), or a string, which identifies the column by its name. |
|  | type specifies the type of data in the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | data returns the data retrieved from the recordset. Use the Database Variant To Data function to convert this data to its native LabVIEW data type. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Fetch Element Data VI:

- Database Fetching VI: labview\examples\database
- Playback (fetching) VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_fetch_next_recordset.html language=enus -->
## TOPIC 00014: DB Tools Fetch Next Recordset VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_fetch_next_recordset.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_fetch_next_recordset.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Fetch Next Recordset VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Retrieves the next recordset in a multi-recordset query identified by **recordset reference**. When the current recordset is no longer available, the **recordset reference** is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Fetch Next Recordset (R)

[IMAGE alt='image' src='db_tools_fetch_next_recordset.gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Fetch Next Recordset (CR)

[IMAGE alt='image' src='rec_fetch_next_recordset_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_fetch_recordset_data.html language=enus -->
## TOPIC 00015: DB Tools Fetch Recordset Data VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_fetch_recordset_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_fetch_recordset_data.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Fetch Recordset Data VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Retrieves the data in the recordset identified by the **recordset reference** input. You can convert each element in the array to its native LabVIEW data type using the [Database Variant To Data](../lvdatabase/database_variant_to_data.html) function. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Fetch Recordset Data (R)

[IMAGE alt='image' src='db_tools_fetch_recordset_data.gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | recordset data returns an array of database variants that contains the selected data. Use the Database Variant To Data function to convert this data type to its native LabVIEW data type. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Fetch Recordset Data (CR)

[IMAGE alt='image' src='rec_fetch_recordset_data_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | recordset data returns an array of database variants that contains the selected data. Use the Database Variant To Data function to convert this data type to its native LabVIEW data type. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_format_datetime_str.html language=enus -->
## TOPIC 00016: DB Tools Format Datetime String VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_format_datetime_str.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_format_datetime_str.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Format Datetime String VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### DB Tools Format Datetime String (Time Stamp)

[IMAGE alt='image' src='db_tools_format_datetime_str_time_stamp.gif']

|  | time stamp specifies the time stamp that you want to convert to a date/time string. The default is an empty time stamp, which returns the current date and time. |
| --- | --- |
|  | date/time string returns the formatted date/time string. |

#### DB Tools Format Datetime String (Seconds)

[IMAGE alt='image' src='db_tools_format_datetime_str_seconds.gif']

|  | seconds specifies the seconds to convert to a date/time string. The value of this input is the time-zone-independent number of seconds that have elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time. The default value is 0, which returns the current date and time. |
| --- | --- |
|  | date/time string returns the formatted date/time string. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Format Datetime String VI:

- Parameterized VI: labview\examples\database
- Sixtypes Insert VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_free_object.html language=enus -->
## TOPIC 00017: DB Tools Free Object VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_free_object.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_free_object.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Free Object VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### Command

[IMAGE alt='image' src='db_tools_free_object.gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Recordset

[IMAGE alt='image' src='rec_destroy_-_connection.gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command-Recordset

[IMAGE alt='image' src='rec_destroy_-_command.gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference returns a reference to an ADO Command object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Free Object VI:

- Using Connection Strings VI: labview\examples\database\EXE
- Database Fetching VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_get_param_val.html language=enus -->
## TOPIC 00018: DB Tools Get Parameter Value VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_get_param_val.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_get_param_val.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Get Parameter Value VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Retrieves the value of the parameter specified by the **parameter index** input in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the **type** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### String (C)

[IMAGE alt='image' src='cmd_get_string_parameter_value_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### String (CR)

[IMAGE alt='image' src='cmd_get_string_parameter_value_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Integer (C)

[IMAGE alt='image' src='cmd_get_integer_parameter_value_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Integer (CR)

[IMAGE alt='image' src='cmd_get_integer_parameter_value_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Single (C)

[IMAGE alt='image' src='cmd_get_single_parameter_value_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Single (CR)

[IMAGE alt='image' src='cmd_get_single_parameter_value_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Double (C)

[IMAGE alt='image' src='cmd_get_double_parameter_value_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Double (CR)

[IMAGE alt='image' src='cmd_get_double_parameter_value_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Date/Time (C)

[IMAGE alt='image' src='cmd_get_datetime_parameter_value_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Date/Time (CR)

[IMAGE alt='image' src='cmd_get_datetime_parameter_value_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Binary (C)

[IMAGE alt='image' src='cmd_get_binary_parameter_value_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Binary (CR)

[IMAGE alt='image' src='cmd_get_binary_parameter_value_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | type specifies the data type of parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | value returns the value of the parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_get_properties.html language=enus -->
## TOPIC 00019: DB Tools Get Properties VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_get_properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_get_properties.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Get Properties VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### Connection

[IMAGE alt='image' src='db_tools_get_properties.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | connection properties returns the following properties that define the database connection. command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. connection string returns the connection string that the VI used to make the database connection. default database returns the default database the VI used for the connection. Some providers might not support this use of this property. provider returns the provider this VI used to make the database connection. |
|  | command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. |
|  | connection string returns the connection string that the VI used to make the database connection. |
|  | default database returns the default database the VI used for the connection. Some providers might not support this use of this property. |
|  | provider returns the provider this VI used to make the database connection. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Recordset (R)

[IMAGE alt='image' src='rec_get_recordset_properties_(r).gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | recordset properties returns the various properties associated with a recordset object. column count returns the number of columns in the recordset. record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of –2 means that the property is not supported. Values of –3 and –4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns –1. bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. dynamicAllows forward and backward navigation. You are able to see all changes other users made to the database.forward-onlyAllows only forward movement through the recordset. Any changes other users made to the database during navigation are not visible. This method provides the highest performance.keysetAllows forward and backward navigation. You are able to see records that other users added, but records deleted by others are not removed from view.staticAllows forward and backward navigation with no ability to see any changes that other users made during navigation. cache size returns how many records are kept in local memory. state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. 0closed1open |
|  | column count returns the number of columns in the recordset. |
|  | record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of –2 means that the property is not supported. Values of –3 and –4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. |
|  | record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns –1. |
|  | bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. |
|  | eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. |
|  | cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. dynamicAllows forward and backward navigation. You are able to see all changes other users made to the database.forward-onlyAllows only forward movement through the recordset. Any changes other users made to the database during navigation are not visible. This method provides the highest performance.keysetAllows forward and backward navigation. You are able to see records that other users added, but records deleted by others are not removed from view.staticAllows forward and backward navigation with no ability to see any changes that other users made during navigation. |
| dynamic | Allows forward and backward navigation. You are able to see all changes other users made to the database. |
| forward-only | Allows only forward movement through the recordset. Any changes other users made to the database during navigation are not visible. This method provides the highest performance. |
| keyset | Allows forward and backward navigation. You are able to see records that other users added, but records deleted by others are not removed from view. |
| static | Allows forward and backward navigation with no ability to see any changes that other users made during navigation. |
|  | cache size returns how many records are kept in local memory. |
|  | state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. 0closed1open |
| 0 | closed |
| 1 | open |
|  | error out contains error information. This output provides standard error out functionality. |

#### Recordset (CR)

[IMAGE alt='image' src='rec_get_recordset_properties_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | recordset properties returns the various properties associated with a recordset object. column count returns the number of columns in the recordset. record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of –2 means that the property is not supported. Values of –3 and –4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns –1. bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. dynamicAllows forward and backward navigation. You are able to see all changes other users made to the database.forward-onlyAllows only forward movement through the recordset. Any changes other users made to the database during navigation are not visible. This method provides the highest performance.keysetAllows forward and backward navigation. You are able to see records that other users added, but records deleted by others are not removed from view.staticAllows forward and backward navigation with no ability to see any changes that other users made during navigation. cache size returns how many records are kept in local memory. state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. 0closed1open |
|  | column count returns the number of columns in the recordset. |
|  | record index returns the zero-indexed position of the current record in the recordset. Some providers or cursor types do not support this property. A value of –2 means that the property is not supported. Values of –3 and –4 indicate that the index is located at Beginning Of File (BOF) and End Of File (EOF), respectively. |
|  | record count returns the number of records in the recordset. Some providers or cursor types do not support this property. If this property is not supported, record count returns –1. |
|  | bof? if TRUE, the cursor points at the Beginning Of File (BOF). BOF is defined as the position before the first record in the recordset. If both BOF and End Of File (EOF) are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. |
|  | eof? if TRUE, the cursor points at the End Of File (EOF). EOF is defined as the position after the last record in the recordset. If both Beginning Of File (BOF) and EOF are TRUE at the same time, records do not exist in the recordset, and navigation of the recordset returns an error. |
|  | cursor type returns the method used to navigate the recordset. Some providers and/or databases do not support all types of cursors. dynamicAllows forward and backward navigation. You are able to see all changes other users made to the database.forward-onlyAllows only forward movement through the recordset. Any changes other users made to the database during navigation are not visible. This method provides the highest performance.keysetAllows forward and backward navigation. You are able to see records that other users added, but records deleted by others are not removed from view.staticAllows forward and backward navigation with no ability to see any changes that other users made during navigation. |
| dynamic | Allows forward and backward navigation. You are able to see all changes other users made to the database. |
| forward-only | Allows only forward movement through the recordset. Any changes other users made to the database during navigation are not visible. This method provides the highest performance. |
| keyset | Allows forward and backward navigation. You are able to see records that other users added, but records deleted by others are not removed from view. |
| static | Allows forward and backward navigation with no ability to see any changes that other users made during navigation. |
|  | cache size returns how many records are kept in local memory. |
|  | state returns the state of the recordset. If the recordset is closed, the recordset does not contain any records. A non-row-returning query returns a closed recordset. Many fetching functions return errors if the functions are performed on closed recordsets, so check for errors. 0closed1open |
| 0 | closed |
| 1 | open |
|  | error out contains error information. This output provides standard error out functionality. |

#### Column (R)

[IMAGE alt='image' src='rec_get_column_properties_(r).gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | column index specifies either the ordinal index of the column or the name of the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | column properties returns the following properties defined for a column. name returns the name of the column. database data type returns the type of data in the column. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary defined size returns the defined size of the column. actual size returns the actual size of the column. |
|  | name returns the name of the column. |
|  | database data type returns the type of data in the column. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary |
| 0 | String |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
|  | defined size returns the defined size of the column. |
|  | actual size returns the actual size of the column. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Column (CR)

[IMAGE alt='image' src='rec_get_column_properties_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | column index specifies either the ordinal index of the column or the name of the column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | column properties returns the following properties defined for a column. name returns the name of the column. database data type returns the type of data in the column. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary defined size returns the defined size of the column. actual size returns the actual size of the column. |
|  | name returns the name of the column. |
|  | database data type returns the type of data in the column. 0String1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary |
| 0 | String |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
|  | defined size returns the defined size of the column. |
|  | actual size returns the actual size of the column. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command (C)

[IMAGE alt='image' src='cmd_get_command_properties_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | command properties returns the following properties that define the most recent SQL query. parameter count returns the number of parameters. command text returns the parameterized SQL command. command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. |
|  | parameter count returns the number of parameters. |
|  | command text returns the parameterized SQL command. |
|  | command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command (CR)

[IMAGE alt='image' src='cmd_get_command_properties_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | command properties returns the following properties that define the most recent SQL query. parameter count returns the number of parameters. command text returns the parameterized SQL command. command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. |
|  | parameter count returns the number of parameters. |
|  | command text returns the parameterized SQL command. |
|  | command timeout (s) returns the length of time, in seconds, the VI waited while attempting to execute a command before quitting and returning an error. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parameter (C)

[IMAGE alt='image' src='cmd_get_parameter_properties_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | parameter properties returns the following properties that define the query parameters. name returns the name of the parameter. SQL data type returns all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction returns the direction of the parameter value. 0Input1Output2Input/Output3Return Value |
|  | name returns the name of the parameter. |
|  | SQL data type returns all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. |
|  | direction returns the direction of the parameter value. 0Input1Output2Input/Output3Return Value |
| 0 | Input |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parameter (CR)

[IMAGE alt='image' src='cmd_get_parameter_properties_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | parameter properties returns the following properties that define the query parameters. name returns the name of the parameter. SQL data type returns all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. direction returns the direction of the parameter value. 0Input1Output2Input/Output3Return Value |
|  | name returns the name of the parameter. |
|  | SQL data type returns all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. |
|  | direction returns the direction of the parameter value. 0Input1Output2Input/Output3Return Value |
| 0 | Input |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Get Properties VI:

- Database Fetching VI: labview\examples\database
- Playback (fetching) VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_insert_data.html language=enus -->
## TOPIC 00020: DB Tools Insert Data VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_insert_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_insert_data.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Insert Data VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Inserts a new row into the table in the database identified by the **connection reference**.

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='db_tools_insert_data.gif']

|  | create table? creates a table if a table does not exist. This VI creates the table with column names provided in the columns input. If the columns input is empty, this VI names the columns Col0, Col1, and so on. This VI determines the type information of the columns created using the data input. If the data input is a cluster, each item in the cluster corresponds to a column that is created in the table. Note For string column types, the size is set equal to the size of the data. |
| --- | --- |
|  | Note For string column types, the size is set equal to the size of the data. |
|  | data specifies the data you want to insert in the database. If data is a cluster, this VI inserts each item in the cluster to each element in the columns input. The item order of the cluster determines the order how this VI inserts the items to the table. For example, this VI inserts the 0th item to the 0th element of the columns input. If the columns input is empty, this VI inserts the 0th item of the cluster to the first column in table. If data is not a cluster, this VI inserts the data to the column specified by the columns input. |
|  | connection reference specifies a reference to an ADO Connection object. |
|  | table specifies the name of the table in the database in which to insert data. If the create table? input is TRUE, the VI attempts to create the table if it does not already exist. |
|  | columns is the column in the table to insert data into. Wiring an empty array to this input assumes that all columns in the table are to be used. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | flatten cluster? specifies whether to insert a cluster that you wire to data as a binary value. If the value is TRUE, this VI updates the column that you specify in the columns input with the flattened binary value of the cluster. If the value is FALSE, this VI updates each column that you specify in the columns input with the corresponding item in the cluster. The default is FALSE. Note This input is valid only if you wire a cluster to the data input. |
|  | Note This input is valid only if you wire a cluster to the data input. |
|  | use file? instructs the VI to use a user-supplied file to determine database types. If you set use file? to FALSE, this VI uses a user-specified file to determine database types. If you set use file? to TRUE, this VI uses the dbtypes.ini file, located in the labview\\Database directory, to determine database types. This VI uses use file? only when create table? is TRUE. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### DB Tools Insert Data Details

The insert is performed on the columns in the **columns** array, or if the **columns** array is empty, all columns in **table** are used. The **data** input can either be a single element or a cluster with each cluster element corresponding to a column in the **table**. The order of the elements in the cluster determines which column each element is inserted into. Thus, the number of items in the cluster must equal the number of elements in the **columns** array, or if the **columns** array is empty, the number of items in the cluster must equal the number of columns in the **table**. In the case where data is a single element, the **columns** array must have one element, or there must be one column in the **table**.

#### Examples

Refer to the following VIs for examples of using the DB Tools Insert Data VI:

- Create DatabaseTable VI: labview\examples\database
- Database Insert VI: labview\examples\database
- Database Logging VI: labview\examples\database
- Sixtypes Insert VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_list_columns.html language=enus -->
## TOPIC 00021: DB Tools List Columns VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_list_columns.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_list_columns.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools List Columns VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Lists the columns present in **table**. The column information includes the name, the data type, and the defined size of the column.

[Example](#examples)

[IMAGE alt='image' src='db_tools_list_columns.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | table specifies the name of the table to search. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | column information returns an array containing information about the columns in the database table. name returns the name of the column. database data type returns the type of data in the column. defined size returns the defined size of the column. |
|  | name returns the name of the column. |
|  | database data type returns the type of data in the column. |
|  | defined size returns the defined size of the column. |
|  | columns returns an array of strings containing the names of each column in a database table. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Get Database Information VI in the labview\examples\database directory for an example of using the DB Tools List Columns VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_list_tables.html language=enus -->
## TOPIC 00022: DB Tools List Tables VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_list_tables.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_list_tables.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools List Tables VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Lists the tables in the database identified by **connection reference**.

[Examples](#examples)

[IMAGE alt='image' src='db_tools_list_tables.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | tables returns an array of table names found in the database. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools List Tables VI:

- Get Database Information VI: labview\examples\database
- Sixtypes Insert VI: labview\examples\database
- Telecommunications Parametric Testing VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_move_to_next_record.html language=enus -->
## TOPIC 00023: DB Tools Move To Next Record VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_move_to_next_record.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_move_to_next_record.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Move To Next Record VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### Move To Next Record (CR)

[IMAGE alt='image' src='rec_move_to_next_record_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Move To Next Record (R)

[IMAGE alt='image' src='db_tools_move_to_next_record.gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Move To Next Record VI:

- Database Fetching VI: labview\examples\database
- Playback (fetching) VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_move_to_previous.html language=enus -->
## TOPIC 00024: DB Tools Move To Previous Record VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_move_to_previous.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_move_to_previous.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Move To Previous Record VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### Move To Previous Record (R)

[IMAGE alt='image' src='db_tools_move_to_previous_record.gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Move To Previous Record (CR)

[IMAGE alt='image' src='rec_move_to_previous_record_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Move To Previous Record VI:

- Database Fetching VI: labview\examples\database
- Playback (fetching) VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_move_to_record_n.html language=enus -->
## TOPIC 00025: DB Tools Move To Record N VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_move_to_record_n.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_move_to_record_n.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Move To Record N VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Moves the cursor to point to record **n** in the recordset. To move the cursor to the last record, set **n** to –1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### Move To Record N (R)

[IMAGE alt='image' src='db_tools_move_to_record_n.gif']

|  | recordset reference specifies a reference to an ADO Recordset object. |
| --- | --- |
|  | n specifies to which recordset to move the cursor. To move the cursor to point to the last record, set n to –1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Move To Record N (CR)

[IMAGE alt='image' src='rec_move_to_record_n_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | n specifies to which recordset to move the cursor. To move the cursor to point to the last record, set n to –1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Using Connection Strings VI in the labview\examples\database\EXE directory for an example of using the DB Tools Move To Record N VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_null.html language=enus -->
## TOPIC 00026: DB Tools Null VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_null.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_null.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Null VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Returns a database variant that contains a NULL value.

[Example](#examples)

[IMAGE alt='image' src='db_tools_null.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | NULL returns a database variant that contains a NULL value. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Database Test Null VI in the labview\examples\database directory for an example of using the DB Tools Null VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_save_recordset_to_file.html language=enus -->
## TOPIC 00027: DB Tools Save Recordset To File VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_save_recordset_to_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_save_recordset_to_file.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Save Recordset To File VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Saves the recordset identified by the **recordset reference** to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the [DB Tools Load Recordset From File](../lvdatabase/db_load_recordset_from_file.html) VI.

Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### Save Recordset To File (R)

[IMAGE alt='image' src='db_tools_save_recordset_to_file.gif']

|  | overwrite? determines whether to overwrite the file specified in file name if the file already exists. |
| --- | --- |
|  | recordset reference specifies a reference to an ADO Recordset object. |
|  | file name specifies the path where you want to save the file. You can click the Browse button to navigate to the correct file path. |
|  | save format specifies the format to use when saving a recordset to file. ADTGA smaller, proprietary file format that only the Database Connectivity Toolkit can interpret.XMLA text-based format that any text viewer can interpret. |
| ADTG | A smaller, proprietary file format that only the Database Connectivity Toolkit can interpret. |
| XML | A text-based format that any text viewer can interpret. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | recordset reference out returns a reference to an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Save Recordset To File (CR)

[IMAGE alt='image' src='rec_save_recordset_to_file_(cr).gif']

|  | overwrite? determines whether to overwrite the file specified in file name if the file already exists. |
| --- | --- |
|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
|  | file name specifies the path where you want to save the file. You can click the Browse button to navigate to the correct file path. |
|  | save format specifies the format to use when saving a recordset to file. ADTGA smaller, proprietary file format that only the Database Connectivity Toolkit can interpret.XMLA text-based format that any text viewer can interpret. |
| ADTG | A smaller, proprietary file format that only the Database Connectivity Toolkit can interpret. |
| XML | A text-based format that any text viewer can interpret. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Telecommunications Parametric Testing VI in the labview\examples\database directory for an example of using the DB Tools Save Recordset To File VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_select_data.html language=enus -->
## TOPIC 00028: DB Tools Select Data VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_select_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_select_data.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Select Data VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Selects data from the **table** in the database identified by **connection reference** using the columns supplied in the **columns** array.

This VI returns the data as a 2D array of variants. You can convert each element in the array to its native LabVIEW data type using the [Database Variant To Data](../lvdatabase/database_variant_to_data.html) function.

[Example](#examples)

[IMAGE alt='image' src='db_tools_select_data.gif']

|  | condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of a select statement. For example, where (col1 > 10). |
| --- | --- |
|  | connection reference specifies a reference to an ADO Connection object. |
|  | table is the name of the table in the database from which to select data. You can specify multiple tables by using commas as the delimiter. |
|  | columns specifies the columns in table from which to select data. If this array is empty, all columns in the table are returned. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | data returns a 2D array of database variants that contains the selected data. Use the Database Variant To Data function to convert this data to its native LabVIEW data type. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Connect to ACCDB Database VI in the labview\examples\database directory for an example of using the DB Tools Select Data VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_set_param_value.html language=enus -->
## TOPIC 00029: DB Tools Set Parameter Value VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_set_param_value.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_set_param_value.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Set Parameter Value VI

**Owning Palette:** [Advanced VIs](../lvdatabase/db_advanced_vis.html)

**Requires:** Database Connectivity Toolkit

Sets the value of the parameter at **parameter index** in the command or command-recordset. The **parameter index** can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### Set Parameter Value (CR)

[IMAGE alt='image' src='db_tools_set_parameter_value.gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | value specifies the parameter value. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Parameter Value (C)

[IMAGE alt='image' src='cmd_set_parameter_value_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | value specifies the parameter value. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the DB Tools Set Parameter Value VI:

- Database Insert VI: labview\examples\database
- Database Logging (parameterized) VI: labview\examples\database
- Parameterized VI: labview\examples\database

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_set_properties.html language=enus -->
## TOPIC 00030: DB Tools Set Properties VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_set_properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_set_properties.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Set Properties VI

**Owning Palette:** [Utility VIs](../lvdatabase/db_utility_vis.html)

**Requires:** Database Connectivity Toolkit

Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Connection

[IMAGE alt='image' src='db_tools_set_properties.gif']

|  | connection reference specifies a reference to an ADO Connection object. |
| --- | --- |
|  | connection properties contains the following properties that define the database connection. command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. connection string specifies the connection string that was used to make the database connection. This property is read-only. default database is the default database to use for the connection. Some providers may not support this use of this property. provider is the provider used to make the database connection. This property is read-only. |
|  | command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. |
|  | connection string specifies the connection string that was used to make the database connection. This property is read-only. |
|  | default database is the default database to use for the connection. Some providers may not support this use of this property. |
|  | provider is the provider used to make the database connection. This property is read-only. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command (CR)

[IMAGE alt='image' src='cmd_set_command_properties_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | command properties specifies the following properties that define the most recent SQL query. parameter count specifies the number of parameters. This property is read-only. command text specifies the parameterized SQL command. command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. |
|  | parameter count specifies the number of parameters. This property is read-only. |
|  | command text specifies the parameterized SQL command. |
|  | command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parameter (CR)

[IMAGE alt='image' src='cmd_set_parameter_properties_(cr).gif']

|  | command-recordset reference specifies a reference that combines an ADO Command object and an ADO Recordset object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | parameter properties contains the following properties that define the query parameters. name specifies the name of the parameter. This property is read-only. SQL data type specifies all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. 0String (default)1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary direction specifies the direction of the parameter value. 0Input (default)1Output2Input/Output3Return Value |
|  | name specifies the name of the parameter. This property is read-only. |
|  | SQL data type specifies all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. 0String (default)1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary |
| 0 | String (default) |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
|  | direction specifies the direction of the parameter value. 0Input (default)1Output2Input/Output3Return Value |
| 0 | Input (default) |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command-recordset reference out returns a reference that combines an ADO Command object and an ADO Recordset object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Command (C)

[IMAGE alt='image' src='cmd_set_command_properties_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | command properties specifies the following properties that define the most recent SQL query. parameter count specifies the number of parameters. This property is read-only. command text specifies the parameterized SQL command. command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. |
|  | parameter count specifies the number of parameters. This property is read-only. |
|  | command text specifies the parameterized SQL command. |
|  | command timeout (s) specifies the length of time (in seconds) to wait in attempting to execute a command before quitting and returning an error. Setting this value to 0 instructs the VI to wait indefinitely. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parameter (C)

[IMAGE alt='image' src='cmd_set_parameter_properties_(c).gif']

|  | command reference specifies a reference to an ADO Command object. |
| --- | --- |
|  | parameter index specifies either the ordinal index of the parameter or the name of the parameter. |
|  | parameter properties contains the following properties that define the query parameters. name specifies the name of the parameter. This property is read-only. SQL data type specifies all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. 0String (default)1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary direction specifies the direction of the parameter value. 0Input (default)1Output2Input/Output3Return Value |
|  | name specifies the name of the parameter. This property is read-only. |
|  | SQL data type specifies all the data types used in databases. Because each specific database application supports different data types, the options in this control have been condensed and named for the data types as they are represented in the LabVIEW Database Connectivity Toolkit. 0String (default)1Long (I32)2Single (SGL)3Double (DBL)4Date/Time5Binary |
| 0 | String (default) |
| 1 | Long (I32) |
| 2 | Single (SGL) |
| 3 | Double (DBL) |
| 4 | Date/Time |
| 5 | Binary |
|  | direction specifies the direction of the parameter value. 0Input (default)1Output2Input/Output3Return Value |
| 0 | Input (default) |
| 1 | Output |
| 2 | Input/Output |
| 3 | Return Value |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | command reference out returns a reference to an ADO Command object. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_tools_update_data.html language=enus -->
## TOPIC 00031: DB Tools Update Data VI

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_tools_update_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_tools_update_data.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DB Tools Update Data VI

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit

Updates the data in a database identified by **connection reference**.

[Example](#examples)

[IMAGE alt='image' src='db_tools_update_data.gif']

|  | condition specifies an SQL clause that this VI uses to filter the selection criteria. This VI appends this clause to the end of an update statement. For example, where (col1 > 10). If you do not specify a value for this input or if the input is an empty string, this VI updates all rows in table. |
| --- | --- |
|  | data specifies the new data you want to update in the database. If data is a cluster and flatten cluster? is FALSE, this VI updates the columns specified by the columns input with the items in the cluster. The order of each item in the cluster determines the order this VI updates the items in the table. For example, this VI updates the column specified by the 0th element of the columns input with the 0th item in the cluster. If the columns input is empty, this VI updates table from the first column with the 0th item in the cluster. If data is a cluster and flatten cluster? is TRUE, this VI flattens the cluster to a binary value and updates the column specified by the columns input with the binary value. If data is not a cluster, this VI updates the column specified by the columns input with the input data. |
|  | connection reference specifies a reference to an ADO Connection object. |
|  | table specifies the name of the table whose data you want to update. |
|  | columns specifies the names of the columns that you want to update. Note If data is a cluster and flatten cluster? is TRUE, you can specify only one column name. This VI updates the column you specify with the flattened binary value. If you do not wire this input, this VI updates the first column with the flattened binary value. If data is a cluster and flatten cluster? is FALSE, the array size of columns must equal the number of elements in the cluster. |
|  | Note If data is a cluster and flatten cluster? is TRUE, you can specify only one column name. This VI updates the column you specify with the flattened binary value. If you do not wire this input, this VI updates the first column with the flattened binary value. If data is a cluster and flatten cluster? is FALSE, the array size of columns must equal the number of elements in the cluster. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | flatten cluster? specifies whether to insert a cluster that you wire to data as a binary value. If the value is TRUE, this VI updates the column that you specify in the columns input with the flattened binary value of the cluster. If the value is FALSE, this VI updates each column that you specify in the columns input with the corresponding item in the cluster. The default is FALSE. Note This input is valid only if you wire a cluster to the data input. |
|  | Note This input is valid only if you wire a cluster to the data input. |
|  | connection reference out returns a reference to an ADO Connection object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Database Update VI in the labview\examples\database directory for an example of using the DB Tools Update Data VI.

<!--NI_TOPIC bundle=labview-database-connectivity-toolkit-api-ref path=lvdatabase/db_utility_vis.html language=enus -->
## TOPIC 00032: Utility VIs

- bundle_id: `labview-database-connectivity-toolkit-api-ref`
- source_path: `lvdatabase/db_utility_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-database-connectivity-toolkit-api-ref/raw/resource/enus/lvdatabase/db_utility_vis.html
- document_id: `labview-database-connectivity-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Utility VIs

**Owning Palette:** [Database VIs and Function](../lvdatabase/database_vis.html)

**Requires:** Database Connectivity Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Utility VIs for a variety of operations, including getting table and column information, getting and setting database properties, formatting data and time data, performing database transactions, and writing and reading data files.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| DB Tools Database Transaction | Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Format Datetime String | Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Get Properties | Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools List Columns | Lists the columns present in table. The column information includes the name, the data type, and the defined size of the column. |
| DB Tools List Tables | Lists the tables in the database identified by connection reference. |
| DB Tools Load Recordset From File | Loads a recordset from a file and returns a recordset reference that identifies this recordset. You can retrieve data from this recordset like any other recordset, but some properties might not be available on this recordset. |
| DB Tools Save Recordset To File | Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| DB Tools Set Properties | Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. |
