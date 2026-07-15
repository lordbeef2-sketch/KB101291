# NI DOCUMENT BUNDLE: labview-datafinder-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-datafinder-toolkit start=1 end=15 -->
<!--NI_TOPIC bundle=labview-datafinder-toolkit path=accessing-datafinder-server-edition.html language=enus -->
## TOPIC 00001: Accessing DataFinder Server Edition

- bundle_id: `labview-datafinder-toolkit`
- source_path: `accessing-datafinder-server-edition.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/accessing-datafinder-server-edition.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In the DataFinder Server Edition, by defining individual DataFinder Servers you can search specified fields on your computer network for files with technical data and you can provide clients with the indexed information. The NI DataFinder Server Edition is a ready-to-use solution for the centralized

### Accessing DataFinder Server Edition

In the DataFinder Server Edition, by defining individual DataFinder Servers you can
 search specified fields on your computer network for files with technical data and you can
 provide clients with the indexed information.

The NI DataFinder Server Edition is a ready-to-use solution for the centralized management of
 large data stores with measurement data and simulation data in different file
 formats.

For example, to access a DataFinder Server with LabVIEW, complete the following steps:

1. Copy the file which contains the connection settings of the DataFinder Server (*.urf) onto the LabVIEW computer. 
 Note Click Export Client Configuration to create a file
 with the connection settings in the DataFinder Manager of the DataFinder
 Server Edition.
2. Double-click the urf-file to register the connection settings and the
 DataPlugins which the DataFinder Server uses on the client computer. 
 Note If you use the urf file to
 import DataPlugins that are already registered on this computer, you can
 specify whether, in the future, the client uses the imported DataPlugins or
 the DataPlugins that are already on the computer. 
 A message indicates that the client configuration and the new
 DataPlugins are registered.
3. Open LabVIEW with an empty VI.
4. Open the controls palette in the front panel and select Modern»I/O»DataFinder to add a DataFinder Name Control.
5. Select the previously registered DataFinder from the list of registered
 DataFinders, for example, to execute a search on this DataFinder server.

Note

Manage DataFinders

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=building-an-application-using-the-datafinder.html language=enus -->
## TOPIC 00002: Components of a DataFinder Toolkit Application

- bundle_id: `labview-datafinder-toolkit`
- source_path: `building-an-application-using-the-datafinder.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/building-an-application-using-the-datafinder.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A DataFinder Toolkit Application is composed of the LabVIEW DataFinder Toolkit Run-Time, the LabVIEW Run-Time Engine, and NI DataFinder Desktop Edition. If you want to create an application with the DataFinder Toolkit, you need the following components: LabVIEW 2018 DataFinder Toolkit Run-Time—Conta

### Components of a DataFinder Toolkit
 Application

A DataFinder Toolkit Application is composed of the LabVIEW DataFinder Toolkit Run-Time,
 the LabVIEW Run-Time Engine, and NI DataFinder Desktop Edition.

If you want to create an application with the DataFinder Toolkit, you need the following
 components:

- LabVIEW 2018 DataFinder Toolkit Run-Time—Contains libraries and files to connect to a DataFinder
 Desktop Edition or to a DataFinder Server Edition. Requires LabVIEW 2018 Run-Time
 Engine and optionally NI DataFinder Desktop Edition.
- LabVIEW 2018 Run-Time Engine—Contains libraries and other files necessary to execute LabVIEW
 2018-built applications and shared libraries.
- NI DataFinder Desktop Edition 2018 (optional)—Component for mining and managing data from
 multiple sources and different formats for a single client. Installs "My
 DataFinder".

Note

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=datafinder-and-datafinder-server.html language=enus -->
## TOPIC 00003: DataFinder and DataFinder Server

- bundle_id: `labview-datafinder-toolkit`
- source_path: `datafinder-and-datafinder-server.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/datafinder-and-datafinder-server.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: DataFinder searches for data files in the search areas you specify. Search areas are file system folders that are on your local computer or on the network. The DataFinder searches for data files in the search areas you specify. Search areas are file system folders that are on your local computer or

### DataFinder and DataFinder Server

DataFinder searches for data files in the search areas you specify. Search areas are file
 system folders that are on your local computer or on the network.

DataFinder configuration

Configure

Search Areas

DataFinder
 configuration

Note

Show hidden icons

For the DataFinder to search for data in the search areas, the indexer must first
 index the data. DataPlugins enable the DataFinder to index many different file
 formats and to browse in these files. Click the DataPlugins
 tab in the DataFinder configuration dialog box to specify which
 filename extensions the DataFinder recognizes when searching for data.

You can search for data on the desktop DataFinder "My DataFinder" and on a DataFinder
 server. Use "My DataFinder" to run a search with the desktop DataFinder on your
 computer or on the network. The DataFinder index is on your computer. You cannot
 delete or export the MyDataFinder DataFinder and you cannot create an additional
 desktop DataFinder. You can specify which search areas this DataFinder uses for a
 search.

In addition to your desktop DataFinder, you also can use any number of DataFinder
 servers that are usually on other computers on your network. A DataFinder server is
 a DataFinder from the DataFinder Server Edition. The DataFinder Server Edition
 enables you to configure a DataFinder and to make the DataFinder available to
 multiple users on the network. In the DataFinder Server Edition configuration you
 can assign rights to clients.

You can also use federations to combine several DataFinder servers. This means that
 you can receive data on the central federation server from many DataFinder servers
 from different locations.

Parent topic:

General

Related information:

- DataPlugins

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=distributing-datafinder-default-configuration.html language=enus -->
## TOPIC 00004: Distributing DataFinder Default Configuration

- bundle_id: `labview-datafinder-toolkit`
- source_path: `distributing-datafinder-default-configuration.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/distributing-datafinder-default-configuration.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can save the DataFinder configuration in a file and distribute the configuration to other clients. A DataFinder configuration file contains all DataFinder settings, for example, the search areas, the index path, or the indexing schedule. DataFinder configuration files have the filename extension

### Distributing DataFinder Default Configuration

You can save the DataFinder configuration in a file and distribute the configuration
 to other clients.

A DataFinder configuration file contains all DataFinder settings, for example, the search areas,
 the index path, or the indexing schedule. DataFinder configuration files have the
 filename extension *.dfc. For example, to export your DataFinder
 configuration in LabVIEW and to import the DataFinder configuration into a different
 client computer complete the following steps:

1. Open LabVIEW with an empty VI.
2. Open the controls palette in the front panel and select Modern»I/O»DataFinder. This adds a DataFinder Name Control.
3. Select Manage DataFinders from the context menu of the controls.
4. Select My DataFinder and click Configure.
5. Select the settings you want on the different tabs to configure your DataFinder.
6. Click the Export button. 
 Note You also can use the Export Configuration method to
 export your configuration.
7. Save your configuration in a dfc-file.
8. Close all dialog boxes.
9. Create a VI with which you can import configurations and make user-defined
 settings. 
 Note You can find information on creating VIs with which you can import a
 configuration and make user-defined settings, in the example
 DataFinder_DistributeConfiguration. This example
 imports a DataFinder configuration and then adds the LabVIEW default data
 folder to the search areas.
10. Save the newly created VI. 
 For example, use the Application Builder to transfer the configuration file
 and the VI or the application for the configuration import to the client.
11. Execute the VI or the application for the configuration import on the
 client. 
 Note If you import
 an exported DataFinder configuration to a different computer, the DataFinder
 automatically adjusts the index path. However, if the index path in a
 configuration file that is to be exported was previously changed manually,
 the index path folder must exist on the client computer exactly as the
 changed index path specifies.
 Note The DataFinder does not adjust the path of a search area. Search areas
 that point to user specific directories have to be added on the client
 computer as described in the
 DataFinder_DistributeConfiguration example. This
 does not apply to federations.

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=general.html language=enus -->
## TOPIC 00005: General

- bundle_id: `labview-datafinder-toolkit`
- source_path: `general.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/general.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI LabVIEW DataFinder Toolkit to work with the DataFinder in LabVIEW, which helps you search for simple texts in indexed data or to execute advanced queries for any data properties. For information about the LabVIEW DataFinder Toolkit's basic features, read the following:

### General

Use the NI LabVIEW DataFinder Toolkit to work with the DataFinder in LabVIEW, which
 helps you search for simple texts in indexed data or to execute advanced queries for any
 data properties.

For information about the LabVIEW DataFinder Toolkit's basic features, read the
 following:

- [DataFinder and DataFinder Server](datafinder-and-datafinder-server.html) DataFinder searches for data files in the search areas you specify. Search areas are file system folders that are on your local computer or on the network.
- [Search Text or Execute Query](search-text-or-execute-query.html) The DataFinder Toolkit enables you to search for text when only partial information is available or when unsure of the data's location. Queries allow for targeted searches within specific file, group, or channel properties, supporting complex search conditions.
- [Indexing the Search Areas](indexing-the-search-areas.html) For the DataFinder to run a search for data from the search area, the indexer must index the data first.
- [Network Drives, CD ROM, and Deleted Folders](netword-drives-cdroms-deleted-folders.html) If you specify temporary locations as search areas, their data will remain in the index even once they are removed from your device.

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=indexing-the-search-areas.html language=enus -->
## TOPIC 00006: Indexing the Search Areas

- bundle_id: `labview-datafinder-toolkit`
- source_path: `indexing-the-search-areas.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/indexing-the-search-areas.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: For the DataFinder to run a search for data from the search area, the indexer must index the data first. Click the Indexer tab in the DataFinder configuration dialog box to specify when and how often the DataFinder indexes the search areas. The DataFinder does not start indexing until the time you s

### Indexing the Search Areas

For the DataFinder to run a search for data from the search area, the indexer must index
 the data first.

Click the Indexer tab in the DataFinder
 configuration dialog box to specify when and how often the DataFinder
 indexes the search areas. The DataFinder does not start indexing until the time you
 specified in the dialog box elapses without a mouse movement or a key action.

- Indexing and the indexing update run automatically at the time you set on
 the Indexer tab in the DataFinder
 configuration dialog box.
- Indexing or the indexing update run automatically when contents of the local
 search areas change, when you delete a file, or when you create a new
 file.
- To start indexing or reindexing: Open the Configure My
 DataFinder dialog box, click the
 Indexer tab, and click the Start
 Now button.

Note

Update Search Area

Index File

Index Folder

Get Statistics

Parent topic:

General

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=netword-drives-cdroms-deleted-folders.html language=enus -->
## TOPIC 00007: Network Drives, CD ROM, and Deleted Folders

- bundle_id: `labview-datafinder-toolkit`
- source_path: `netword-drives-cdroms-deleted-folders.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/netword-drives-cdroms-deleted-folders.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you specify temporary locations as search areas, their data will remain in the index even once they are removed from your device. If the search areas refer to transient folders, for example, network drives, CD or DVD drives, or memory sticks, the contents of these folders remain in the index alth

### Network Drives, CD ROM, and Deleted
 Folders

If you specify temporary locations as search areas, their data will remain in the index
 even once they are removed from your device.

If the search areas refer to transient folders, for example, network drives, CD or DVD
 drives, or memory sticks, the contents of these folders remain in the index although the
 folders are no longer available. In this case you can search for files, groups, and
 channels of these folders but you cannot navigate in the folders or load search results
 from the folders. The file browser identifies folders that are no longer available in a
 certain search area with a red exclamation mark.

If you delete a search area from the DataFinder, the DataFinder deletes the associated entry from
 the index. If you delete files or folders from a search area, the DataFinder updates the
 index. If you delete a folder from the search area while the DataFinder is not active,
 the DataFinder treats the folder like a transient folder. If you restore a deleted
 folder of a search area or if the transient folder is available again, the DataFinder
 updates the search area and you can load files from the folder.

Note

Note

Note

Parent topic:

General

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00008: LabVIEW DataFinder Toolkit New Features and Changes

- bundle_id: `labview-datafinder-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates—including new features and behavior changes—introduced in each version of LabVIEW DataFinder Toolkit. Discover what's new in the latest releases of LabVIEW DataFinder Toolkit.If you cannot find new features and changes for your version, it may not include user-facing updates. How

### LabVIEW DataFinder Toolkit
 New Features and Changes

Learn about updates—including new features and behavior changes—introduced in each
 version of LabVIEW DataFinder Toolkit.

LabVIEW DataFinder Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW DataFinder Toolkit 2018
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW DataFinder
 Toolkit 2018.

- As of LabVIEW 2018 DataFinder Toolkit, you cannot create a new DataFinder server
 connection to a DataFinder with an empty string as the name or with the name "My
 DataFinder".
- The Logos communication protocol (communication via UDP) used by older DataFinder
 Toolkit versions will no longer be supported as of My DataFinder version 2019. This
 means that earlier clients no longer communicate with DataFinder Server 2019 or My
 DataFinder 2019. In future, you can only use Logos XT (communication via TCP) for
 communication with DataFinder. This applies to the and LabVIEW DataFinder Toolkit
 clients.

#### LabVIEW DataFinder Toolkit 2017
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW DataFinder
 Toolkit 2017.

- With this release, DataFinder Toolkit 2017 drops support for Microsoft Windows 7 RTM
 (with no service pack), Windows Vista, Windows XP, and Windows Server 2003. DataFinder
 Toolkit 2017 a will not install or run on an unsupported OS. You cannot deploy or
 distribute applications that use DataFinder Toolkit 2017 to an unsupported OS.
 Additionally, after installing DataFinder Toolkit 20 cannot use any installers built on
 this computer with any version of LabVIEW.

LabVIEW DataFinder Toolkit 2017 also includes bug fixes. Refer to the Release Notes for a
 list of bug fixes.

Related information:

- Release Notes

#### LabVIEW DataFinder Toolkit 2016
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW DataFinder
 Toolkit 2016.

LabVIEW DataFinder Toolkit 2016 includes only bug fixes. Refer to the Release Notes for a
 list of bug fixes.

Related information:

- Release Notes

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=notes-on-searching-for-data-with-the-datafind.html language=enus -->
## TOPIC 00009: Notes on Searching for Data with the DataFinder Toolkit

- bundle_id: `labview-datafinder-toolkit`
- source_path: `notes-on-searching-for-data-with-the-datafind.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/notes-on-searching-for-data-with-the-datafind.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: DataFinder offers two main options: text search and query search. Users can combine multiple search conditions and use wildcards for text properties, while numeric and date/time properties have specific operators and operands for searching. Refer to the following sections for more information.

### Notes on Searching for Data with the DataFinder Toolkit

DataFinder offers two main options: text search and query search. Users can combine
 multiple search conditions and use wildcards for text properties, while numeric and
 date/time properties have specific operators and operands for searching.

Refer to the following sections for more information.

- [Text Search or Query](text-search-or-query.html) DataFinder offers a text search for partial information or uncertain locations within files, groups, or channels, and a query search for specific files, groups, or channels, allowing for complex searches with combined conditions.
- [Special Features of the Text Search](special-features-of-text-search.dota.html) Use special characters, wildcards, and other features to get the most out of DataFinder's text searches.
- [Special Features of a Query](special-features-of-query.html) A query in DataFinder involves specifying one or more search conditions comprising properties like file, channel group, or channel, along with operators and values for comparison. Users can use logical operators, wildcards, and specified properties to improve search conditions.

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=search-text-or-execute-query.html language=enus -->
## TOPIC 00010: Search Text or Execute Query

- bundle_id: `labview-datafinder-toolkit`
- source_path: `search-text-or-execute-query.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/search-text-or-execute-query.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DataFinder Toolkit enables you to search for text when only partial information is available or when unsure of the data's location. Queries allow for targeted searches within specific file, group, or channel properties, supporting complex search conditions. Search TextSearch for text if you only

### Search Text or Execute Query

The DataFinder Toolkit enables you to search for text when only partial information is
 available or when unsure of the data's location. Queries allow for targeted searches within
 specific file, group, or channel properties, supporting complex search
 conditions.

#### Search Text

Search for text if you only have parts of the
 information you are searching for, or if you do not know whether the
 information you are searching for is in a file, a group, or a
 channel property.

#### Execute Query

Execute a query if you want to search in
 specific file, group, or channel properties. You can specify, for
 example, that you want to search for channels or files named Time.
 You can run more complex search queries if you combine several query
 conditions. If all search areas are completely indexed, executing a
 query returns reproducible results.

The entries involved in searching for text and executing a query are not
 case-sensitive.

Parent topic:

General

Related concepts:

- Notes on Searching for Data with the DataFinder Toolkit

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=special-features-of-query.html language=enus -->
## TOPIC 00011: Special Features of a Query

- bundle_id: `labview-datafinder-toolkit`
- source_path: `special-features-of-query.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/special-features-of-query.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A query in DataFinder involves specifying one or more search conditions comprising properties like file, channel group, or channel, along with operators and values for comparison. Users can use logical operators, wildcards, and specified properties to improve search conditions. A query consists of o

### Special Features of a Query

A query in DataFinder involves specifying one or more search conditions comprising
 properties like file, channel group, or channel, along with operators and values for
 comparison. Users can use logical operators, wildcards, and specified properties to improve
 search conditions.

A query consists of one or more search conditions. A search condition comprises the file
 property, either the channel group property or the channel property the DataFinder
 searches for, the operator, and the value with which the DataFinder compares the
 property. Before the search starts you can specify whether the DataFinder returns files,
 channel groups, or channels as the search results.

By default the DataFinder connects all search conditions with an AND operator. However,
 you can specify a logical operator yourself and connect the search conditions with AND
 and OR as you like. Use parentheses to specify the order of evaluation.

Please note the following characteristics of a query:

- By default, the DataFinder executes a logical AND operation on the search conditions
 of an advanced search. This means that, for example, the search for groups that
 contain channels with the name Channel1 AND channels that contain the name Channel2,
 can never return a result.
- You can execute OR operations on single values of a search condition, or on entire
 search conditions, for example, to search for several filenames. Enter the values in
 the Value column of the search input area and insert an OR
 between these values. Alternatively, click the ... button multiple times and
 double-click another value each time, to select the value. DataFinder then
 automatically executes an OR operation on the selected values. You must select the =
 sign to connect values with OR.
- You also can create OR operations in the logical operations line. Create a search
 condition in the search input area, click the logical operations line, and then
 enter OR.
- You only can use wildcards (* and ?) when you search for text properties. If you
 search for text that contains spaces, you must enter a question mark (?) as a
 wildcard for each space, in the search.
- Use the operators =, <>, <, <=, >, and >= to search for numeric
 properties.
- When you search for text properties, you can use only the operators = and
 <>.
- In the advanced search for date/time properties, for example, for the file property
 Modify date, the DataFinder provides the following operators: =, >=, <=, and #.
 If you select the # operator in the DataFinder interface, you can use the following
 operands: Today, Yesterday, Last 7 days, Last 14 days, Last 30 days. If you execute
 a search with the # operator in a script, use the following operands: Today,
 Yesterday, LastSevenDays, LastFourteenDays, or LastThirtyDays. The DataFinder
 executes the search in relation to the current date. For example, if you use the
 operator # to search for the creation date Today, and you save the search, the
 search uses the current date if you run the search again at a later date.If you want
 to search for DataTypeDate type custom properties, you must first optimize this
 custom property.
- If you use the = operator when you search for date and time properties, you can
 search for the exact date, otherwise for the exact second.
- If you search for the text Or, you must enter /Or as the search text, instead of
 Or.
- If you search for a text property, the property must not be longer than 256
 characters.
- The search results are listed in ascending order of the values of the property of
 the first search condition, according to the following conditions: The property must
 be a base property or an optimized custom property. DataFinder must be able to
 clearly evaluate this property for the search result. DataFinder can clearly
 evaluate only file properties when it searches for files. DataFinder can clearly
 evaluate only file properties and channel group properties when it searches for
 channel groups.

Parent topic:

Notes on Searching for Data with the DataFinder Toolkit

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=special-features-of-text-search.dota.html language=enus -->
## TOPIC 00012: Special Features of the Text Search

- bundle_id: `labview-datafinder-toolkit`
- source_path: `special-features-of-text-search.dota.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/special-features-of-text-search.dota.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use special characters, wildcards, and other features to get the most out of DataFinder's text searches. If you work with the Text Search VI, separate the search terms with spaces. After you execute the text search, the DataFinder returns all files that contain these search terms regardless of wheth

### Special Features of the Text Search

Use special characters, wildcards, and other features to get the most out of DataFinder's
 text searches.

If you work with the Text Search VI, separate the search terms with spaces.
 After you execute the text search, the DataFinder returns all files that contain these
 search terms regardless of whether the DataFinder found the search term in the property
 of a file, a group, or a channel. The text search also searches for parts of search
 terms. The part of the search term must be at the beginning of the search term, for
 example, exa*.

Note the following characteristics of the quick search:

- If you enter quotation marks within a search term, DataFinder replaces the quotation
 marks with a space.
- If the wildcards (* and ?) are at the beginning of a search term, the text search
 does not take them into account.
- If a search is too unspecific, for example, a search for te* , the
 DataFinder might not be able to return any results although many files match this
 query. In this case you should specify the query more accurately to limit the search
 results.

Parent topic:

Notes on Searching for Data with the DataFinder Toolkit

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=text-search-or-query.html language=enus -->
## TOPIC 00013: Text Search or Query

- bundle_id: `labview-datafinder-toolkit`
- source_path: `text-search-or-query.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/text-search-or-query.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: DataFinder offers a text search for partial information or uncertain locations within files, groups, or channels, and a query search for specific files, groups, or channels, allowing for complex searches with combined conditions. Use the text search if you only have parts of the information you are

### Text Search or Query

DataFinder offers a text search for partial information or uncertain locations within
 files, groups, or channels, and a query search for specific files, groups, or channels,
 allowing for complex searches with combined conditions.

Use the text search if you only have parts of the information you are searching for, or
 if you do not know whether the information you are searching for is in a file, a group,
 or a channel.

Use the query if you want to search for specific files, groups, or channels. In a query
 you can specify, for example, that you want to search for channels or files named Time.
 You can run more complex queries if you combine several search conditions.

The text search and the query are not case-sensitive.

Parent topic:

Notes on Searching for Data with the DataFinder Toolkit

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=the-tdm-data-model.html language=enus -->
## TOPIC 00014: The TDM Data Model

- bundle_id: `labview-datafinder-toolkit`
- source_path: `the-tdm-data-model.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/the-tdm-data-model.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TDM format is designed to capture and manage all the important information surrounding a measurement or simulation, assuring that the data is self-explanatory, reusable, and requires no additional explanation to recreate the conditions under which it was captured. Hierarchy Levels The TDM data m

### The TDM Data Model

The TDM format is designed to capture and manage all the important information
 surrounding a measurement or simulation, assuring that the data is self-explanatory, reusable, and
 requires no additional explanation to recreate the conditions under which it was
 captured.

#### Hierarchy Levels

The TDM data model defines 3
 hierarchy levels: Root objects, Group objects, and Channel objects. Each file has a single root
 object, and any number of group and channel objects. For example, in one file you can save the
 original data in group 1 named “raw data”, and create a second group called “analyzed results”
 to separate the analyzed results from the original data. Within each group the measurement or
 simulation data is saved in channels which are waveforms or 1D arrays of numeric, date/time or
 string data types.

#### About
 Properties

Each of the three levels has a set of predefined properties. You can
 add an unlimited number of freely definable properties of data type string, numeric,
 integer, and time. For example, you may want to save the sensor id as a property associated
 with each channel, and save the UUT number at the root level.

The following characters
 are not supported for custom property names throughout the whole TDM platform: ., :, ,, ;,
 ', \, @, <, >, #, [, ], %, (, ), {, }, |, *, ?, =, !, ", ^, $, &, +, -, /, and a
 space.

These characters may be replaced with "_" in the property name.

#### Property
 Restrictions

The following property names are reserved and may not be used for
 creating custom properties on file level: author, channelgroups, children, datestring,
 datetime, description, environment, external_references, id, instance_attributes, mime_type,
 name, objecttype, parent, registercomments, registertxt1, registertxt2, registertxt3,
 timestring, title, version, version_date.

The DataFinder has the following property
 names reserved on file level: createTime, dataPluginName, fileName, folder, indexStatus,
 modifyTime.

The following property names are reserved and may not be used on group
 level: channels, children, description, equipments, external_references, id, index,
 instance_attributes, measurement_begin, measurement_end, measurement_quantities, mime_type,
 name, objecttype, parent, registertxt1, registertxt2, registertxt3, root, sequences,
 submatrices, submatrices, test, units_under_test, version, version_date.

The following
 property names are reserved and may not be used on channel level: average, channel,
 children, datatype, deletebehaviour, description, dimension, displaytype, empty,
 external_references, flagkey, group, groupindex, id, implicit_increment, implicit_start,
 instance_attributes, internal_params, internal_res1, internal_res2, interpolation,
 is_scaled_by, length, lengthmax, local_columns, maximum, measurement, mime_type, minimum,
 monotony, name, novaluekey, number, objecttype, parent, quantity, rank, registerint1,
 registerint2, registerint3, registerint4, registerint5, registerint6, registertxt1,
 registertxt2, registertxt3, registerval1, registerval2, registerval3, registerval4,
 registerval5, registerval6, representation, scales, sourcedatafilename, sourcedatafilepath,
 sourcegenparam1, sourcegenparam2, sourcehandle, sourceinstancekey, sourcename,
 sourceparentname, sourcerepresentation, sourcetype, sourcevalue, standard_deviation, status,
 type_size, unit, unit_string, valuetype, version, version_date, waveform.

<!--NI_TOPIC bundle=labview-datafinder-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00015: LabVIEW DataFinder Toolkit User Manual

- bundle_id: `labview-datafinder-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-datafinder-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-datafinder-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW DataFinder Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Informatio

### LabVIEW DataFinder Toolkit
 User Manual

The LabVIEW DataFinder Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Release Notes
- Software and Driver Downloads
- License Setup and Activation
- LabVIEW User Manual
- OS Compatibility
- NI Learning Center
