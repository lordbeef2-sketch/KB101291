# NI DOCUMENT BUNDLE: lvdfc-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvdfc-api-ref start=1 end=53 -->
<!--NI_TOPIC bundle=lvdfc-api-ref path=dfc_intro.html language=enus -->
## TOPIC 00001: LabVIEW Data Finder Connectivity Toolkit Programming Reference Manual

- bundle_id: `lvdfc-api-ref`
- source_path: `dfc_intro.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/dfc_intro.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Data Finder Connectivity Toolkit LabVIEW Release Notes Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.To comment on National Instruments documentation, refer to the National Instruments website.

### LabVIEW Data Finder Connectivity Toolkit Programming Reference Manual

The LabVIEW Data Finder Connectivity Toolkit

[LabVIEW Release Notes](https://www.ni.com/en-us/support/documentation/release-notes/product.labview.html) 
Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.

To comment on National Instruments documentation, refer to the National Instruments website.

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/children-property.html language=enus -->
## TOPIC 00002: Children (Property)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/children-property.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/children-property.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Class: Search Result Returns the child elements of a search result. If the search result is a channel element, an empty search result array and a warning are returned. Data Type 1D array of search result refnums

### Children (Property)

**Owning Class:**Search Result

Returns the child elements of a search result. If the search 
result is a channel element, an empty search result array and a warning are returned.

#### Data Type

1D array of search result refnums

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/datafinder-info-property.html language=enus -->
## TOPIC 00003: DataFinder Info (Property)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/datafinder-info-property.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/datafinder-info-property.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Class: Search Result Returns the name of a DataFinder server and the name of the computer on which this DataFinder server is running as DataFinderName@Server if the search result originates from a federation server. Data Type Search result refnum

### DataFinder Info (Property)

**Owning Class:**Search Result

Returns the name of a DataFinder server and the name of the 
computer on which this DataFinder server is running as DataFinderName@Server if the search result originates from a federation 
server.

#### Data Type

Search result refnum

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/datafinder-properties.html language=enus -->
## TOPIC 00004: DataFinder Properties

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/datafinder-properties.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/datafinder-properties.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: DataFinderRequires: LabVIEW DataFinder Use the following properties to configure the DataFinder. PropertyDescriptionServer VersionReturns the version number of the DataFinder server used. DetailsIndexer StatusDetermines the indexer status of a DataFinder. Details

### DataFinder Properties

**Owning Palette**: 
DataFinder

**Requires:** LabVIEW DataFinder

Use the following properties to configure the DataFinder.

| Property | Description |
| --- | --- |
| Server Version | Returns the version number of the DataFinder server used. Details |
| Indexer Status | Determines the indexer status of a DataFinder. Details |

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/indexer-status-property.html language=enus -->
## TOPIC 00005: Indexer Status (Property)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/indexer-status-property.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/indexer-status-property.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the indexer status of a DataFinder. For real-time or time critical measurements it might make sense to pause the DataFinder indexer. This avoids timing influences that are caused by indexing activities. The property does not support DataFinder federations. Data Type Ring with the followin

### Indexer Status (Property)

Determines the indexer status of a DataFinder. For real-time or 
time critical measurements it might make sense to pause the DataFinder indexer. 
This avoids timing influences that are caused by indexing activities. The 
property does not support DataFinder federations.

#### Data Type

Ring with the following value range:

| 1 | Running |
| --- | --- |
| 2 | Paused |

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/invoke-node-datafinder.html language=enus -->
## TOPIC 00006: Invoke Node (DataFinder)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/invoke-node-datafinder.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/invoke-node-datafinder.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods that you use to configure the DataFinder. The node operates in the same way as a standard Invoke Node. reference is the refnum associated with the object on which you want to invoke a method or perform an action. If the Invoke Node class is Application or VI, you do not have to wire

### Invoke Node (DataFinder)

Provides methods that you use to configure the DataFinder.

The node operates in the same way as a standard [Invoke Node](/csh?context=lvcore_glang_invoke_node).

[IMAGE alt='image' src='invoknod.gif']

|  | reference is the refnum associated with the object on which you want to invoke a method or perform an action. If the Invoke Node class is Application or VI, you do not have to wire a refnum to this input. For the Application class, the default is the current application instance. For the VI class, the default is the VI containing the Invoke Node. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | input 1..n are example input parameters of a method. |
|  | reference out returns reference unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | return value is an example return value of a method. |
|  | output 1..n are example output parameters of a method. |

#### Example

Refer to the DataFinder_Configure VI in the labview\examples\DataFinder\DataFinder_Examples.lvproj for an example of using the
Invoke Node.

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/name-property.html language=enus -->
## TOPIC 00007: Name (Property)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/name-property.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/name-property.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Class: Search Result Returns the name value of a search result element. Data Type String

### Name (Property)

**Owning Class:**Search Result

Returns the name value of a search result element.

#### Data Type

String

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/parent-property.html language=enus -->
## TOPIC 00008: Parent (Property)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/parent-property.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/parent-property.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Class: Search Result Returns the parent element of a search result. If the search result is a file element, an empty search result refnum and a warning are returned. Data Type Search result refnum

### Parent (Property)

**Owning Class:**Search Result

Returns the parent element of a search result. If the search 
result is a file element, an empty search result refnum and a warning are 
returned.

#### Data Type

Search result refnum

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/property-node-datafinder.html language=enus -->
## TOPIC 00009: Property Node (DataFinder)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/property-node-datafinder.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/property-node-datafinder.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties that you use to configure the DataFinder. The node operates in the same way as a standard Property Node. reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refn

### Property Node (DataFinder)

Provides properties that you use to configure the DataFinder.

The node operates in the same way as a standard [Property Node](/csh?context=lvcore_glang_property_node).

[IMAGE alt='image' src='propnode.gif']

|  | reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For the Application class, the default is the current application instance. For the VI class, the default is the VI containing the Property Node. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | property 2..n are examples of properties you want to set (write). |
|  | reference out returns reference unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | property 1..n are examples of properties you want to get (read). |

#### Example

Refer to the DataFinder_Configure VI in the labview\examples\DataFinder\DataFinder_Examples.lvproj for an example of using the
Property Node.

<!--NI_TOPIC bundle=lvdfc-api-ref path=functions/server-version-property.html language=enus -->
## TOPIC 00010: Server Version (Property)

- bundle_id: `lvdfc-api-ref`
- source_path: `functions/server-version-property.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/functions/server-version-property.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the version number of the DataFinder server used. The property does not support DataFinder federations. Data Type Double value with read access.

### Server Version (Property)

Returns the version number of the DataFinder server used. The 
property does not support DataFinder federations.

#### Data Type

Double value with read access.

<!--NI_TOPIC bundle=lvdfc-api-ref path=menus/categories/computer/datafinder-mnu.html language=enus -->
## TOPIC 00011: DataFinder

- bundle_id: `lvdfc-api-ref`
- source_path: `menus/categories/computer/datafinder-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/menus/categories/computer/datafinder-mnu.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DataFinder VIs to open a DataFinder connection, create and execute queries in indexed data, and access search results. You can also search for text and get information about the indexed properties and values. Use the DataFinder property and invoke nodes to index files and folders, and read t

### DataFinder

Use the DataFinder VIs to open a DataFinder connection, create and execute queries in indexed data, and access search results. You can also search for text and get information about the indexed properties and values. 
Use the DataFinder property and invoke nodes to index files and folders, and read the DataFinder configuration.

[IMAGE alt='icon' src='datafinder-mnu.png']

- [Search Text Ex VI](../../../vi-lib/datafinder/search-text-ex-vi.html) Uses the DataFinder to search in all of the text properties of the indexed files.
- [Results to Waveforms VI](../../../vi-lib/datafinder/results-to-waveforms-vi.html) Extracts the signals from the results of a DataFinder search. To select the polymorphic instance, connect data to the Data type input or select the instance manually.
- [Create Query VI](../../../vi-lib/datafinder/create-query-vi.html) Creates a query. You can search for text, paths, numeric values, and time/date values. Use the instance Order by only to sort search results according to a property without searching for this particular property. Use the Merge Queries VI to query conditions to each other. Use the Execute Query VI to execute a query that consists of one or more search conditions. To select the polymorphic instance, connect data to the appropriate input or select the instance manually.
- [Merge Queries VI](../../../vi-lib/datafinder/merge-queries-vi.html) Uses an operator to combine several queries into one query. For example, you can generate queries as "C1 AND C2 AND C3", "(C1 AND C2) OR C3", or "(C1 AND C2) OR (C3 AND C4).
- [Execute Query Ex VI](../../../vi-lib/datafinder/execute-query-ex-vi.html) Uses the DataFinder to search the specified properties of the indexed data.
- [Get Property Values VI](../../../vi-lib/datafinder/get-property-values-vi.html) Determines from the result references the values of one or more properties that are the same data type. To select the polymorphic instance, connect data to the Data Type input or to the Property input or select the instance manually.
- [Get Indexed Properties VI](../../../vi-lib/datafinder/get-indexed-properties-vi.html) Determines for files, groups, or channels, the list of all the indexed properties in which you can execute a search with the DataFinder.
- [Get Indexed Value List VI](../../../vi-lib/datafinder/get-indexed-value-list-vi.html) Returns a list of strings which contains all indexed values for the specified string property. You can restrict the list of values by setting a prefix. The list is also restricted by the given query.
- [Get Indexed Value Limits VI](../../../vi-lib/datafinder/get-indexed-value-limits-vi.html) Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions.
- [Open Server VI](../../../vi-lib/datafinder/open-server-vi.html) Connects a DataFinder or a DataFinder federation with the specified connection parameters.
- [Close Reference VI](../../../vi-lib/datafinder/close-reference-vi.html) Closes a DataFinder connection, a reference to a query, or references to search results. To select the polymorphic instance, connect data to the appropriate input or select the instance manually.
- [DataFinder Property Node VI](../../../vi-lib/datafinder/datafinder-property-node-vi.html) Provides properties that you use to configure the DataFinder.
- [Create Index Job File VI](../../../vi-lib/datafinder/create-index-job-file-vi.html) Creates a job file for indexing certain files or folders from the search areas of a DataFinder server.

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/close-reference-datafinder-vi.html language=enus -->
## TOPIC 00012: Close Reference (DataFinder) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/close-reference-datafinder-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/close-reference-datafinder-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a DataFinder connection. icon Inputs/Outputs cgenclassrntag.png DataFinder reference DataFinder reference is the reference to the DataFinder to be closed. cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this VI or function runs.The default

### Close Reference (DataFinder) VI

Closes a DataFinder connection.

[IMAGE alt='icon' src='close-reference-datafinder-vi.png']

#### Inputs/Outputs

| DataFinder reference — DataFinder reference is the reference to the DataFinder to be closed. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Close Reference VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/close-reference-query-vi.html language=enus -->
## TOPIC 00013: Close Reference (Query) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/close-reference-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/close-reference-query-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a reference to a query. icon Inputs/Outputs cgenclassrn.png query reference query reference is the reference to the query to be closed. cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an

### Close Reference (Query) VI

Closes a reference to a query.

[IMAGE alt='icon' src='close-reference-query-vi.png']

#### Inputs/Outputs

| query reference — query reference is the reference to the query to be closed. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Close Reference VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/close-reference-result-vi.html language=enus -->
## TOPIC 00014: Close Reference (Result) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/close-reference-result-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/close-reference-result-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a reference to a search result. icon Inputs/Outputs cgenclassrn.png result reference result reference is the reference to a search result to be closed. cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this VI or function runs.The default is

### Close Reference (Result) VI

Closes a reference to a search result.

[IMAGE alt='icon' src='close-reference-result-vi.png']

#### Inputs/Outputs

| result reference — result reference is the reference to a search result to be closed. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Close Reference VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/close-reference-results-vi.html language=enus -->
## TOPIC 00015: Close Reference (Results) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/close-reference-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/close-reference-results-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes references to search results. icon Inputs/Outputs c1dgenclassrn.png result references result references is the array of search result references to be closed. cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this VI or function runs.The def

### Close Reference (Results) VI

Closes references to search results.

[IMAGE alt='icon' src='close-reference-results-vi.png']

#### Inputs/Outputs

| result references — result references is the array of search result references to be closed. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Close Reference VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/close-reference-vi.html language=enus -->
## TOPIC 00016: Close Reference VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/close-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/close-reference-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a DataFinder connection, a reference to a query, or references to search results. To select the polymorphic instance, connect data to the appropriate input or select the instance manually. icon

### Close Reference VI

Closes a DataFinder connection, a reference to a query, or references to search results. To select the polymorphic instance, connect data to the appropriate input or select the instance manually.

[IMAGE alt='icon' src='close-reference-vi.png']

- [Close Reference (DataFinder) VI](../../vi-lib/datafinder/close-reference-datafinder-vi.html) Closes a DataFinder connection.
- [Close Reference (Query) VI](../../vi-lib/datafinder/close-reference-query-vi.html) Closes a reference to a query.
- [Close Reference (Result) VI](../../vi-lib/datafinder/close-reference-result-vi.html) Closes a reference to a search result.
- [Close Reference (Results) VI](../../vi-lib/datafinder/close-reference-results-vi.html) Closes references to search results.

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/create-index-job-file-vi.html language=enus -->
## TOPIC 00017: Create Index Job File VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/create-index-job-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/create-index-job-file-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a job file for indexing certain files or folders from the search areas of a DataFinder server. icon Inputs/Outputs cpath.png job file location c1dpath.png paths to be indexed cenum.png path type (files) cerrcodeclst.png error in (no error) error in describes error conditions that occur befor

### Create Index Job File VI

Creates a job file for indexing certain files or folders from the search areas of a DataFinder server.

[IMAGE alt='icon' src='create-index-job-file-vi.png']

#### Inputs/Outputs

| job file location — paths to be indexed — path type (files) — error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. job file location out — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/create-query-date-vi.html language=enus -->
## TOPIC 00018: Create Query (Date) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/create-query-date-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/create-query-date-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a query for time/date values. icon Inputs/Outputs cu16.png order by (none) Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} cu16.png object type object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} cst

### Create Query (Date) VI

Creates a query for time/date values.

[IMAGE alt='icon' src='create-query-date-vi.png']

#### Inputs/Outputs

| order by (none) — Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} object type — object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — property name specifies the property that the DataFinder searches for the specified value. comparison operator (=) — comparison operator (=)specifies the operator that the DataFinder searches for. You can use the operators =, <>, <, >=, >, and >= when you search for numeric properties. When you search for text properties, you can use only the operators = and <>. In the search for date/time properties, for example, for the file property Modify date, the DataFinder provides the following operators: =, >=, <=, and #. If you select the # operator, you can use the following operands: Today, Yesterday, LastSevenDays, LastFourteenDays, LastThirtyDays. The DataFinder executes the search in relation to the current date. For example, if you use the operator # to search for the creation date Today, and you save the search, the search uses the current date if you execute the search again at a later date. value — value specifies the value of the property to be searched for. You also can execute OR operations on single values. If you search for the text OR, you must mask the OR with a backslash. To search for date/time properties, you must explicitly select the date/time data type in the VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. query reference out — query reference out is the reference to the new query condition. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Query VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/create-query-numeric-vi.html language=enus -->
## TOPIC 00019: Create Query (Numeric) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/create-query-numeric-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/create-query-numeric-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a query for numeric values. icon Inputs/Outputs cu16.png order by (none) Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} cu16.png object type object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} cstr.

### Create Query (Numeric) VI

Creates a query for numeric values.

[IMAGE alt='icon' src='create-query-numeric-vi.png']

#### Inputs/Outputs

| order by (none) — Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} object type — object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — property name specifies the property that the DataFinder searches for the specified value. comparison operator (=) — comparison operator (=)specifies the operator that the DataFinder searches for. You can use the operators =, <>, <, >=, >, and >= when you search for numeric properties. When you search for text properties, you can use only the operators = and <>. In the search for date/time properties, for example, for the file property Modify date, the DataFinder provides the following operators: =, >=, <=, and #. If you select the # operator, you can use the following operands: Today, Yesterday, LastSevenDays, LastFourteenDays, LastThirtyDays. The DataFinder executes the search in relation to the current date. For example, if you use the operator # to search for the creation date Today, and you save the search, the search uses the current date if you execute the search again at a later date. value — value specifies the value of the property to be searched for. You also can execute OR operations on single values. If you search for the text OR, you must mask the OR with a backslash. To search for date/time properties, you must explicitly select the date/time data type in the VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. query reference out — query reference out is the reference to the new query condition. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Query VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/create-query-order-by-only-vi.html language=enus -->
## TOPIC 00020: Create Query (Order by only) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/create-query-order-by-only-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/create-query-order-by-only-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sorts the search results according to a property without searching for this particular property. icon Inputs/Outputs cu16.png order by Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} cu16.png object type object type Enumeration for the o

### Create Query (Order by only) VI

Sorts the search results according to a property without searching for this particular property.

[IMAGE alt='icon' src='create-query-order-by-only-vi.png']

#### Inputs/Outputs

| order by — Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} object type — object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — property name specifies the property that the DataFinder searches for the specified value. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. query reference out — query reference out is the reference to the new query condition. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Query VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/create-query-path-vi.html language=enus -->
## TOPIC 00021: Create Query (Path) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/create-query-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/create-query-path-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a query for paths. icon Inputs/Outputs cu16.png order by (none) Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} cu16.png object type object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} cstr.png prope

### Create Query (Path) VI

Creates a query for paths.

[IMAGE alt='icon' src='create-query-path-vi.png']

#### Inputs/Outputs

| order by (none) — Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} object type — object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — property name specifies the property that the DataFinder searches for the specified value. comparison operator (=) — comparison operator (=)specifies the operator that the DataFinder searches for. You can use the operators =, <>, <, >=, >, and >= when you search for numeric properties. When you search for text properties, you can use only the operators = and <>. In the search for date/time properties, for example, for the file property Modify date, the DataFinder provides the following operators: =, >=, <=, and #. If you select the # operator, you can use the following operands: Today, Yesterday, LastSevenDays, LastFourteenDays, LastThirtyDays. The DataFinder executes the search in relation to the current date. For example, if you use the operator # to search for the creation date Today, and you save the search, the search uses the current date if you execute the search again at a later date. value — value specifies the value of the property to be searched for. You also can execute OR operations on single values. If you search for the text OR, you must mask the OR with a backslash. To search for date/time properties, you must explicitly select the date/time data type in the VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. query reference out — query reference out is the reference to the new query condition. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Query VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/create-query-string-vi.html language=enus -->
## TOPIC 00022: Create Query (String) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/create-query-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/create-query-string-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a query for texts. icon Inputs/Outputs cu16.png order by (none) Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} cu16.png object type object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} cstr.png prope

### Create Query (String) VI

Creates a query for texts.

[IMAGE alt='icon' src='create-query-string-vi.png']

#### Inputs/Outputs

| order by (none) — Specifies whether a condition is used for order by and in which direction. {none:0, ascending:1, descending:2} object type — object type Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — property name specifies the property that the DataFinder searches for the specified value. comparison operator (=) — comparison operator (=)specifies the operator that the DataFinder searches for. You can use the operators =, <>, <, >=, >, and >= when you search for numeric properties. When you search for text properties, you can use only the operators = and <>. In the search for date/time properties, for example, for the file property Modify date, the DataFinder provides the following operators: =, >=, <=, and #. If you select the # operator, you can use the following operands: Today, Yesterday, LastSevenDays, LastFourteenDays, LastThirtyDays. The DataFinder executes the search in relation to the current date. For example, if you use the operator # to search for the creation date Today, and you save the search, the search uses the current date if you execute the search again at a later date. value — value specifies the value of the property to be searched for. You also can execute OR operations on single values. If you search for the text OR, you must mask the OR with a backslash. To search for date/time properties, you must explicitly select the date/time data type in the VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. query reference out — query reference out is the reference to the new query condition. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Query VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/create-query-vi.html language=enus -->
## TOPIC 00023: Create Query VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/create-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/create-query-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a query. You can search for text, paths, numeric values, and time/date values. Use the instance Order by only to sort search results according to a property without searching for this particular property. Use the Merge Queries VI to query conditions to each other. Use the Execute Query VI to

### Create Query VI

Creates a query. You can search for text, paths, numeric values, and time/date values. Use the instance Order by only to sort search results according to a property without searching for this particular property. Use the Merge Queries VI to query conditions to each other. Use the Execute Query VI to execute a query that consists of one or more search conditions. To select the polymorphic instance, connect data to the appropriate input or select the instance manually.

[IMAGE alt='icon' src='create-query-vi.png']

- [Create Query (String) VI](../../vi-lib/datafinder/create-query-string-vi.html) Creates a query for texts.
- [Create Query (Numeric) VI](../../vi-lib/datafinder/create-query-numeric-vi.html) Creates a query for numeric values.
- [Create Query (Date) VI](../../vi-lib/datafinder/create-query-date-vi.html) Creates a query for time/date values.
- [Create Query (Path) VI](../../vi-lib/datafinder/create-query-path-vi.html) Creates a query for paths.
- [Create Query (Order by only) VI](../../vi-lib/datafinder/create-query-order-by-only-vi.html) Sorts the search results according to a property without searching for this particular property.

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/datafinder-property-node-vi.html language=enus -->
## TOPIC 00024: DataFinder Property Node VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/datafinder-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/datafinder-property-node-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties that you use to configure the DataFinder. icon Inputs/Outputs cgenclassrntag.png DataFinder cerrcodeclst.png error in (no error) igenclassrntag.png NI DataFinder ierrcodeclst.png error out ipoly.png Property

### DataFinder Property Node VI

Provides properties that you use to configure the DataFinder.

[IMAGE alt='icon' src='datafinder-property-node-vi.png']

#### Inputs/Outputs

| DataFinder — error in (no error) — NI DataFinder — error out — Property — |
| --- |

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/execute-query-ex-vi.html language=enus -->
## TOPIC 00025: Execute Query Ex VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/execute-query-ex-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/execute-query-ex-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the DataFinder to search the specified properties of the indexed data. icon Inputs/Outputs cu16.png result object type (file) result object type (file) Enumeration for the object type. {File:0, Channel Group:1, Channel:2} cgenclassrntag.png DataFinder reference DataFinder reference (My DataFind

### Execute Query Ex VI

Uses the DataFinder to search the specified properties of the indexed data.

[IMAGE alt='icon' src='execute-query-ex-vi.png']

#### Inputs/Outputs

| result object type (file) — result object type (file) Enumeration for the object type. {File:0, Channel Group:1, Channel:2} DataFinder reference — DataFinder reference (My DataFinder) is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. query reference — query reference is the reference to the query for the search. DataPlugin name — DataPlugin name specifies whether the DataFinder searches only for files that are loaded with a specific DataPlugin. By default, the DataFinder searches in all files. You can connect several DataPlugin names with OR. Note If you are connected to a federation, DataFinder ignores the DataPlugin name. The error out connector then shows a warning. fill results elements? (F) — incomplete results? is TRUE if more search results exist than the maximum number of search results that are requested. If you want to display more search results, you must increase the value of the Max results count parameter. The more search results that are to be displayed, the lower the search performance. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. max results count (200) — max results count (200) specifies the maximum number of search results that the DataFinder determines. You can enter values from 1 to 16,384. The default maximum number of determined search results is 200. DataFinder reference out — DataFinder reference out is the reference to the DataFinder that is also at the respective input of the VI. query reference out — query reference out is the reference to the query that was used for the search. result references out — result references out is the array of the references that the query returns. results elements — Identification of search results. for files: fullpath array and DataPlugin name array for channel groups: file identification and channel group name array for channels: channel group identification and channel name array fullpaths — DataPlugin names — channel group names — channel names — error out — error out contains error information. This output provides standard error out functionality. incomplete results? — incomplete results? is TRUE if more search results exist than the maximum number of search results that are requested. If you want to display more search results, you must increase the value of the Max results count parameter. The more search results that are to be displayed, the lower the search performance. |
| --- |
| fullpaths — DataPlugin names — channel group names — channel names — |

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-indexed-properties-vi.html language=enus -->
## TOPIC 00026: Get Indexed Properties VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-indexed-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-indexed-properties-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines for files, groups, or channels, the list of all the indexed properties in which you can execute a search with the DataFinder. icon Inputs/Outputs cgenclassrntag.png DataFinder reference DataFinder reference is the reference to the DataFinder used. To connect a registered DataFinder, selec

### Get Indexed Properties VI

Determines for files, groups, or channels, the list of all the indexed properties in which you can execute a search with the DataFinder.

[IMAGE alt='icon' src='get-indexed-properties-vi.png']

#### Inputs/Outputs

| DataFinder reference — DataFinder reference is the reference to the DataFinder used. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. object type — object type specifies whether the indexed properties of a channel, a group, or a file, are returned. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. DataFinder reference out — DataFinder reference out is the reference to the DataFinder that is also at the respective input of the VI. properties — object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-indexed-value-limits-date-vi.html language=enus -->
## TOPIC 00027: Get Indexed Value Limits (Date) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-indexed-value-limits-date-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-indexed-value-limits-date-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions. icon Inputs/Outputs catrn.png data type cgenclassrntag.png DataFinder reference DataFinder

### Get Indexed Value Limits (Date) VI

Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions.

[IMAGE alt='icon' src='get-indexed-value-limits-date-vi.png']

#### Inputs/Outputs

| data type — DataFinder reference — DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. property — Represents a certain property object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} query reference — query reference is the reference to the query for the search. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. DataFinder reference out — DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. minimum — maximum — query reference out — query reference is the reference to the query for the search. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Indexed Value Limits VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-indexed-value-limits-numeric-vi.html language=enus -->
## TOPIC 00028: Get Indexed Value Limits (Numeric) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-indexed-value-limits-numeric-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-indexed-value-limits-numeric-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions. icon Inputs/Outputs cdbl.png data type cgenclassrntag.png DataFinder reference DataFinder r

### Get Indexed Value Limits (Numeric) VI

Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions.

[IMAGE alt='icon' src='get-indexed-value-limits-numeric-vi.png']

#### Inputs/Outputs

| data type — DataFinder reference — DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. property — Represents a certain property object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} query reference — query reference is the reference to the query for the search. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. DataFinder reference out — DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. minimum — maximum — query reference out — query reference is the reference to the query for the search. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Indexed Value Limits VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-indexed-value-limits-vi.html language=enus -->
## TOPIC 00029: Get Indexed Value Limits VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-indexed-value-limits-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-indexed-value-limits-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions. icon

### Get Indexed Value Limits VI

Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions.

[IMAGE alt='icon' src='get-indexed-value-limits-vi.png']

- [Get Indexed Value Limits (Numeric) VI](../../vi-lib/datafinder/get-indexed-value-limits-numeric-vi.html) Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions.
- [Get Indexed Value Limits (Date) VI](../../vi-lib/datafinder/get-indexed-value-limits-date-vi.html) Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions.

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-indexed-value-list-vi.html language=enus -->
## TOPIC 00030: Get Indexed Value List VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-indexed-value-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-indexed-value-list-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of strings which contains all indexed values for the specified string property. You can restrict the list of values by setting a prefix. The list is also restricted by the given query. icon Inputs/Outputs cgenclassrntag.png DataFinder reference DataFinder reference is the reference to

### Get Indexed Value List VI

Returns a list of strings which contains all indexed values for the specified string property. You can restrict the list of values by setting a prefix. The list is also restricted by the given query.

[IMAGE alt='icon' src='get-indexed-value-list-vi.png']

#### Inputs/Outputs

| DataFinder reference — DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. property — Represents a certain property object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} prefix — query reference — query reference is the reference to the query for the search. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. max value count (200) — max results count (200) specifies the maximum number of search results that the DataFinder determines. You can enter values from 1 to 16,384. The default maximum number of determined search results is 200. DataFinder reference out — DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. property values — property values specifies the values of the properties. query reference out — query reference is the reference to the query for the search. error out — error out contains error information. This output provides standard error out functionality. incomplete values? — incomplete results? is TRUE if more search results exist than the maximum number of search results that are requested. If you want to display more search results, you must increase the value of the Max results count parameter. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-date-properties-vi.html language=enus -->
## TOPIC 00031: Get Property Values (Date Properties) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-date-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-date-properties-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of time/date properties. icon Inputs/Outputs c2datrn.png data type data type specifies which data type the property values are returned in. c1dcclst.png properties properties cu16.png object type Enumeration for the object type. {File:0, Channel Group

### Get Property Values (Date Properties) VI

Determines from the result references the values of time/date properties.

[IMAGE alt='icon' src='get-property-values-date-properties-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. properties — properties object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-date-property-vi.html language=enus -->
## TOPIC 00032: Get Property Values (Date Property) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-date-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-date-property-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of a time/date property. icon Inputs/Outputs c1datrn.png data type data type specifies which data type the property values are returned in. ccclst.png property Represents a certain property cu16.png object type Enumeration for the object type. {File:0

### Get Property Values (Date Property) VI

Determines from the result references the values of a time/date property.

[IMAGE alt='icon' src='get-property-values-date-property-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. property — Represents a certain property object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-numeric-properties-vi.html language=enus -->
## TOPIC 00033: Get Property Values (Numeric Properties) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-numeric-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-numeric-properties-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of numeric properties. icon Inputs/Outputs c2ddbl.png data type data type specifies which data type the property values are returned in. c1dcclst.png properties properties cu16.png object type Enumeration for the object type. {File:0, Channel Group:1,

### Get Property Values (Numeric Properties) VI

Determines from the result references the values of numeric properties.

[IMAGE alt='icon' src='get-property-values-numeric-properties-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. properties — properties object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-numeric-property-vi.html language=enus -->
## TOPIC 00034: Get Property Values (Numeric Property) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-numeric-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-numeric-property-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of a numeric property. icon Inputs/Outputs c1ddbl.png data type data type specifies which data type the property values are returned in. ccclst.png property Represents a certain property cu16.png object type Enumeration for the object type. {File:0, C

### Get Property Values (Numeric Property) VI

Determines from the result references the values of a numeric property.

[IMAGE alt='icon' src='get-property-values-numeric-property-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. property — Represents a certain property object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-path-properties-vi.html language=enus -->
## TOPIC 00035: Get Property Values (Path Properties) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-path-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-path-properties-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of path properties. icon Inputs/Outputs c2dpath.png data type data type specifies which data type the property values are returned in. c1dcclst.png properties properties cu16.png object type Enumeration for the object type. {File:0, Channel Group:1, C

### Get Property Values (Path Properties) VI

Determines from the result references the values of path properties.

[IMAGE alt='icon' src='get-property-values-path-properties-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. properties — properties object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-path-property-vi.html language=enus -->
## TOPIC 00036: Get Property Values (Path Property) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-path-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-path-property-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of a path property. icon Inputs/Outputs c1dpath.png data type data type specifies which data type the property values are returned in. ccclst.png property Represents a certain property cu16.png object type Enumeration for the object type. {File:0, Cha

### Get Property Values (Path Property) VI

Determines from the result references the values of a path property.

[IMAGE alt='icon' src='get-property-values-path-property-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. property — Represents a certain property object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-string-properties-vi.html language=enus -->
## TOPIC 00037: Get Property Values (String Properties) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-string-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-string-properties-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of string properties. icon Inputs/Outputs c2dstr.png data type data type specifies which data type the property values are returned in. c1dcclst.png properties properties cu16.png object type Enumeration for the object type. {File:0, Channel Group:1,

### Get Property Values (String Properties) VI

Determines from the result references the values of string properties.

[IMAGE alt='icon' src='get-property-values-string-properties-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. properties — properties object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-string-property-vi.html language=enus -->
## TOPIC 00038: Get Property Values (String Property) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-string-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-string-property-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of a string property. icon Inputs/Outputs c1dstr.png data type data type specifies which data type the property values are returned in. ccclst.png property Represents a certain property cu16.png object type Enumeration for the object type. {File:0, Ch

### Get Property Values (String Property) VI

Determines from the result references the values of a string property.

[IMAGE alt='icon' src='get-property-values-string-property-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. property — Represents a certain property object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. property values — property values specifies the values of the properties. result references out — result references out is the array of the references of which the property values were determined. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| object type — Enumeration for the object type. {File:0, Channel Group:1, Channel:2} property name — data type — Data type of a property indexed by the DataFinder. {Unknown:0, String:23, Int32:3, Double:10, Time stamp:30} |

Parent topic:

Get Property Values VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/get-property-values-vi.html language=enus -->
## TOPIC 00039: Get Property Values VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/get-property-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/get-property-values-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines from the result references the values of one or more properties that are the same data type. To select the polymorphic instance, connect data to the Data Type input or to the Property input or select the instance manually. icon

### Get Property Values VI

Determines from the result references the values of one or more properties that are the same data type. To select the polymorphic instance, connect data to the Data Type input or to the Property input or select the instance manually.

[IMAGE alt='icon' src='get-property-values-vi.png']

- [Get Property Values (String Property) VI](../../vi-lib/datafinder/get-property-values-string-property-vi.html) Determines from the result references the values of a string property.
- [Get Property Values (String Properties) VI](../../vi-lib/datafinder/get-property-values-string-properties-vi.html) Determines from the result references the values of string properties.
- [Get Property Values (Numeric Property) VI](../../vi-lib/datafinder/get-property-values-numeric-property-vi.html) Determines from the result references the values of a numeric property.
- [Get Property Values (Numeric Properties) VI](../../vi-lib/datafinder/get-property-values-numeric-properties-vi.html) Determines from the result references the values of numeric properties.
- [Get Property Values (Date Property) VI](../../vi-lib/datafinder/get-property-values-date-property-vi.html) Determines from the result references the values of a time/date property.
- [Get Property Values (Date Properties) VI](../../vi-lib/datafinder/get-property-values-date-properties-vi.html) Determines from the result references the values of time/date properties.
- [Get Property Values (Path Property) VI](../../vi-lib/datafinder/get-property-values-path-property-vi.html) Determines from the result references the values of a path property.
- [Get Property Values (Path Properties) VI](../../vi-lib/datafinder/get-property-values-path-properties-vi.html) Determines from the result references the values of path properties.

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/merge-queries-vi.html language=enus -->
## TOPIC 00040: Merge Queries VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/merge-queries-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/merge-queries-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses an operator to combine several queries into one query. For example, you can generate queries as "C1 AND C2 AND C3", "(C1 AND C2) OR C3", or "(C1 AND C2) OR (C3 AND C4). icon Inputs/Outputs cgenclassrn.png query reference in 1 query reference in 1 is the first query that is to be connected to ot

### Merge Queries VI

Uses an operator to combine several queries into one query. For example, you can generate queries as "C1 AND C2 AND C3", "(C1 AND C2) OR C3", or "(C1 AND C2) OR (C3 AND C4).

[IMAGE alt='icon' src='merge-queries-vi.png']

#### Inputs/Outputs

| query reference in 1 — query reference in 1 is the first query that is to be connected to other queries. query reference in 2 — query reference in 2 is the second query that is to be connected to other queries. query reference array in — query reference array in is an array of queries that are to be connected to each other or to other queries. operation (AND) — Operator to connect query conditions. {AND:0, OR:1} error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. query reference out — query reference is the reference to the new query. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/open-datafinder-vi.html language=enus -->
## TOPIC 00041: Open DataFinder VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/open-datafinder-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/open-datafinder-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects a DataFinder with the specified connection parameters. icon Inputs/Outputs cstr.png DataFinder name DataFinder name is the name of the DataFinder on the other computer. cstr.png server name (localhost) server name (localhost) is the name of the computer where the remote DataFinder is locate

### Open DataFinder VI

Connects a DataFinder with the specified connection parameters.

[IMAGE alt='icon' src='open-datafinder-vi.png']

#### Inputs/Outputs

| DataFinder name — DataFinder name is the name of the DataFinder on the other computer. server name (localhost) — server name (localhost) is the name of the computer where the remote DataFinder is located. connection timeout in s (5) — connection timeout in s (5) specifies how long it takes to connect the two computers. If the specified time elapses, an error message appears. query timeout in s (20) — query timeout in s (20) specifies the maximum length of time that the client waits for the results of a query. If the specified time elapses, an error message appears. error in (no error) — error in (no error) error in describes error conditions occurring before the function executes. DataFinder reference out — DataFinder reference out is the reference to the open DataFinder. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

Open Server VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/open-federation-vi.html language=enus -->
## TOPIC 00042: Open Federation VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/open-federation-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/open-federation-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects a DataFinder federation with the specified connection parameters. icon Inputs/Outputs cu64.png port (2809) connection timeout in s (5) specifies how long it takes to connect the two computers. If the specified time elapses, an error message appears. cstr.png DataFinder name DataFinder name

### Open Federation VI

Connects a DataFinder federation with the specified connection parameters.

[IMAGE alt='icon' src='open-federation-vi.png']

#### Inputs/Outputs

| port (2809) — connection timeout in s (5) specifies how long it takes to connect the two computers. If the specified time elapses, an error message appears. DataFinder name — DataFinder name (My DataFinder) is the name of the DataFinder on the other computer. server name (localhost) — server name (localhost) is the name of the computer where the remote DataFinder is located. user name — server name (localhost) is the name of the computer where the remote DataFinder is located. password — server name (localhost) is the name of the computer where the remote DataFinder is located. error in (no error) — error in (no error) error in describes error conditions occurring before the function executes. authentication mode (no security) — DataFinder reference out — DataFinder reference out is the reference to the open DataFinder. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

Open Server VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/open-server-vi.html language=enus -->
## TOPIC 00043: Open Server VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/open-server-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/open-server-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects a DataFinder or a DataFinder federation with the specified connection parameters. icon

### Open Server VI

Connects a DataFinder or a DataFinder federation with the specified connection parameters.

[IMAGE alt='icon' src='open-server-vi.png']

- [Open DataFinder VI](../../vi-lib/datafinder/open-datafinder-vi.html) Connects a DataFinder with the specified connection parameters.
- [Open Federation VI](../../vi-lib/datafinder/open-federation-vi.html) Connects a DataFinder federation with the specified connection parameters.

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-array-of-doubles-vi.html language=enus -->
## TOPIC 00044: Results to Waveforms (array of doubles) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-array-of-doubles-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-array-of-doubles-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs c2ddbl.png data type data type specifies which data type the property values are returned in. c1dgenclassrn.png result references result references are the result references from which the VI takes the property values.

### Results to Waveforms (array of doubles) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-array-of-doubles-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the array of the references of which the property values were determined. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-array-of-i16-vi.html language=enus -->
## TOPIC 00045: Results to Waveforms (array of I16) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-array-of-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-array-of-i16-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs c2di16.png data type data type specifies which data type the signals are returned in. c1dgenclassrn.png result references result references is the reference to DataFinder search results, from which the waveforms are ex

### Results to Waveforms (array of I16) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-array-of-i16-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the signals are returned in. result references — result references is the reference to DataFinder search results, from which the waveforms are extracted. You receive the Result references when you execute the "Search Text" VI or the "Execute Search" VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the reference to the search results from which the waveforms are extracted. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-array-of-i32-vi.html language=enus -->
## TOPIC 00046: Results to Waveforms (array of I32) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-array-of-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-array-of-i32-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs c2di32.png data type data type specifies which data type the signals are returned in. c1dgenclassrn.png result references result references is the reference to DataFinder search results, from which the waveforms are ex

### Results to Waveforms (array of I32) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-array-of-i32-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the signals are returned in. result references — result references is the reference to DataFinder search results, from which the waveforms are extracted. You receive the Result references when you execute the "Search Text" VI or the "Execute Search" VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the array of the references of which the property values were determined. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-array-of-strings-vi.html language=enus -->
## TOPIC 00047: Results to Waveforms (array of strings) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-array-of-strings-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-array-of-strings-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs c2dstr.png data type data type specifies which data type the signals are returned in. c1dgenclassrn.png result references result references is the reference to DataFinder search results, from which the waveforms are ex

### Results to Waveforms (array of strings) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-array-of-strings-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the signals are returned in. result references — result references is the reference to DataFinder search results, from which the waveforms are extracted. You receive the Result references when you execute the "Search Text" VI or the "Execute Search" VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the reference to the search results from which the waveforms are extracted. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-array-of-timestamps-vi.html language=enus -->
## TOPIC 00048: Results to Waveforms (array of timestamps) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-array-of-timestamps-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-array-of-timestamps-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs c2datrn.png data type data type specifies which data type the property values are returned in. c1dgenclassrn.png result references result references are the result references from which the VI takes the property values

### Results to Waveforms (array of timestamps) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-array-of-timestamps-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the property values are returned in. result references — result references are the result references from which the VI takes the property values. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the reference to the search results from which the waveforms are extracted. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-array-of-u8-vi.html language=enus -->
## TOPIC 00049: Results to Waveforms (array of U8) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-array-of-u8-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-array-of-u8-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs c2du8.png data type data type specifies which data type the signals are returned in. c1dgenclassrn.png result references result references is the reference to DataFinder search results, from which the waveforms are ext

### Results to Waveforms (array of U8) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-array-of-u8-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the signals are returned in. result references — result references is the reference to DataFinder search results, from which the waveforms are extracted. You receive the Result references when you execute the "Search Text" VI or the "Execute Search" VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the reference to the search results from which the waveforms are extracted. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-array-of-waveforms-vi.html language=enus -->
## TOPIC 00050: Results to Waveforms (array of waveforms) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-array-of-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-array-of-waveforms-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs c1dmsdt.png data type data type specifies which data type the signals are returned in. c1dgenclassrn.png result references result references is the reference to DataFinder search results, from which the waveforms are e

### Results to Waveforms (array of waveforms) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-array-of-waveforms-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the signals are returned in. result references — result references is the reference to DataFinder search results, from which the waveforms are extracted. You receive the Result references when you execute the "Search Text" VI or the "Execute Search" VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the array of the references of which the property values were determined. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-ddt-vi.html language=enus -->
## TOPIC 00051: Results to Waveforms (ddt) VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-ddt-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-ddt-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. icon Inputs/Outputs cexpdynwdt.png data type data type specifies which data type the signals are returned in. c1dgenclassrn.png result references result references is the reference to DataFinder search results, from which the waveforms ar

### Results to Waveforms (ddt) VI

Extracts the signals from the results of a DataFinder search.

[IMAGE alt='icon' src='results-to-waveforms-ddt-vi.png']

#### Inputs/Outputs

| data type — data type specifies which data type the signals are returned in. result references — result references is the reference to DataFinder search results, from which the waveforms are extracted. You receive the Result references when you execute the "Search Text" VI or the "Execute Search" VI. error in (no error) — error in (no error) describes error conditions that occur before this VI or function runs.The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally even if an error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use exception control to treat what is normally an error as no error or to treat a warning as an error. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. signals out — signals out specifies the array of the outgoing signals. The files can be DDT, Waveforms, Doubles, I32, I16, U8, Strings, and Date/Time types. result references out — result references out is the array of the references of which the property values were determined. error out — error out error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Results to Waveforms VI

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/results-to-waveforms-vi.html language=enus -->
## TOPIC 00052: Results to Waveforms VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/results-to-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/results-to-waveforms-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the signals from the results of a DataFinder search. To select the polymorphic instance, connect data to the Data type input or select the instance manually. icon

### Results to Waveforms VI

Extracts the signals from the results of a DataFinder search. To select the polymorphic instance, connect data to the Data type input or select the instance manually.

[IMAGE alt='icon' src='results-to-waveforms-vi.png']

- [Results to Waveforms (ddt) VI](../../vi-lib/datafinder/results-to-waveforms-ddt-vi.html) Extracts the signals from the results of a DataFinder search.
- [Results to Waveforms (array of waveforms) VI](../../vi-lib/datafinder/results-to-waveforms-array-of-waveforms-vi.html) Extracts the signals from the results of a DataFinder search.
- [Results to Waveforms (array of doubles) VI](../../vi-lib/datafinder/results-to-waveforms-array-of-doubles-vi.html) Extracts the signals from the results of a DataFinder search.
- [Results to Waveforms (array of I32) VI](../../vi-lib/datafinder/results-to-waveforms-array-of-i32-vi.html) Extracts the signals from the results of a DataFinder search.
- [Results to Waveforms (array of I16) VI](../../vi-lib/datafinder/results-to-waveforms-array-of-i16-vi.html) Extracts the signals from the results of a DataFinder search.
- [Results to Waveforms (array of U8) VI](../../vi-lib/datafinder/results-to-waveforms-array-of-u8-vi.html) Extracts the signals from the results of a DataFinder search.
- [Results to Waveforms (array of strings) VI](../../vi-lib/datafinder/results-to-waveforms-array-of-strings-vi.html) Extracts the signals from the results of a DataFinder search.
- [Results to Waveforms (array of timestamps) VI](../../vi-lib/datafinder/results-to-waveforms-array-of-timestamps-vi.html) Extracts the signals from the results of a DataFinder search.

Parent topic:

DataFinder

<!--NI_TOPIC bundle=lvdfc-api-ref path=vi-lib/datafinder/search-text-ex-vi.html language=enus -->
## TOPIC 00053: Search Text Ex VI

- bundle_id: `lvdfc-api-ref`
- source_path: `vi-lib/datafinder/search-text-ex-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdfc-api-ref/raw/resource/enus/vi-lib/datafinder/search-text-ex-vi.html
- document_id: `lvdfc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the DataFinder to search in all of the text properties of the indexed files. icon Inputs/Outputs cgenclassrntag.png DataFinder reference DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder fr

### Search Text Ex VI

Uses the DataFinder to search in all of the text properties of the indexed files.

[IMAGE alt='icon' src='search-text-ex-vi.png']

#### Inputs/Outputs

| DataFinder reference — DataFinder reference is the reference to the DataFinder that is to be used to execute the search. To connect a registered DataFinder, select the DataFinder from the DataFinder named control. search text — search text is the text to be searched for. When you search for text properties, you can use the wildcard ? for one letter and the wildcard * for any number of letters. The text search ignores wildcards at the beginning of a search term. If you search for extracts of search terms, the extract must be at the beginning of the term, for example, exa*. If you enter quotation marks within a search term, DataFinder replaces the quotation marks with a space. DataPlugin name — DataPlugin name specifies whether the DataFinder searches only for files that are loaded with a specific DataPlugin. By default, the DataFinder searches in all files. You can connect several DataPlugin names with OR. Note If you are connected to a federation, DataFinder ignores the DataPlugin name. The error out connector then shows a warning. fill results elements? (F) — incomplete results? is TRUE if more search results exist than the maximum number of search results that are requested. If you want to display more search results, you must increase the value of the Max results count parameter. The more search results that are to be displayed, the lower the search performance. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. max results count (200) — max results count (200) specifies the maximum number of search results that the DataFinder determines. You can enter values from 1 to 16,384. The default maximum number of determined search results is 200. DataFinder reference out — DataFinder reference out is the reference to the DataFinder that is also at the respective input of the VI. result references out — result references out is the array of the references of which the property values were determined. results elements — Identification of search results. for files: fullpath array and DataPlugin name array for channel groups: file identification and channel group name array for channels: channel group identification and channel name array fullpaths — DataPlugin names — channel group names — channel names — error out — error out contains error information. This output provides standard error out functionality. incomplete results? — incomplete results? is TRUE if more search results exist than the maximum number of search results that are requested. If you want to display more search results, you must increase the value of the Max results count parameter. The more search results that are to be displayed, the lower the search performance. |
| --- |
| fullpaths — DataPlugin names — channel group names — channel names — |

Parent topic:

DataFinder
