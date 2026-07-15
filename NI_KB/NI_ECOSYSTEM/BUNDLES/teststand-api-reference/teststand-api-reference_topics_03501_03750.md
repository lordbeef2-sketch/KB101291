# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=3501 end=3750 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-use-auto-scheduled-resource-step-di.html language=enus -->
## TOPIC 03501: Configure Use Auto Scheduled Resource Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-use-auto-scheduled-resource-step-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-use-auto-scheduled-resource-step-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Use Auto Scheduled Resource in the context menu for the step to launch the Configure Use Auto Scheduled Resource Step dialog box from a TestStand User Interface . You can also the Configure Use Auto Scheduled Resource on the General tab of the Step Properties dialog box. The Configu

### Configure Use Auto Scheduled Resource Step Dialog Box

Select
 Configure Use Auto Scheduled Resource
 in the context menu for the step to launch the Configure Use Auto Scheduled Resource Step dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also the
 Configure Use Auto Scheduled Resource
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Configure Use Auto Scheduled Resource Step dialog box contains the following options:

- Resource Lock Name or Reference Expression 
 —The lock(s) to acquire before executing the steps within the Use Auto Scheduled Resource block. You can specify a single lock by name or by the object reference you receive when you create a lock using a Lock step. You can specify multiple locks using either a string array containing the names of the locks or an object reference array containing object references to the locks.
 Note 
 You can enter a string array constant in an expression with the following syntax:
 {"String1", "String2", "String3"}
- Alternative Locks 
 —A list of lock names or reference
 expressions 
 . The step attempts to acquire the first lock in the list. If the lock is not available, the step attempts to acquire the next lock, and so forth, until it successfully acquires a lock. If the step cannot acquire a lock, the step proceeds to the next Use Auto Scheduled Resource step in the same Auto Schedule block.
 You specify alternative locks if the steps in the Use Auto Scheduled Resource sub-block can execute with more than one set of resources. For example, you could specify alternative locks "
 DAQCard1
 " and "
 DAQCard2
 " if the steps can execute with either card, depending on which card is available.
  - Add 
 —Adds a new empty lock name or reference expression to the list after the currently selected item.
  - Delete 
 —Deletes the currently selected item.
  - Move Up 
 —Moves the currently selected item up one place in the list.
  - Move Down 
 —Moves the currently selected item down one place in the list.
- Acquired Lock (optional output string) 
 —An expression that specifies a string variable or property into which to store the lock alternative the step acquires during execution. To identify the alternative lock it selects, the step stores the unevaluated alternative lock expression, exactly as the expression appears in the list.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Use Auto Scheduled Resource Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-while-loop-dialog-box.html language=enus -->
## TOPIC 03502: Configure While Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-while-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-while-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure While Loop in the context menu for the step or click Configure While Loop on the General tab of the Step Properties dialog box to launch the Configure While Loop dialog box from a TestStand User Interface . The Configure While Loop dialog box contains the following option: Loop Cond

### Configure While Loop Dialog Box

Select
 Configure While Loop
 in the context menu for the step or click
 Configure While Loop
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure While Loop dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure While Loop dialog box contains the following option:

- Loop Condition 
 —The expression the step evaluates before executing steps within the block. If the expression evaluates to
 True 
 , execution proceeds to the first step in the block. If the expression evaluates to
 False 
 , the loop ends and execution proceeds to the End step for the While block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

While Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configuring-a-property-loader-source.html language=enus -->
## TOPIC 03503: Configuring a Property Loader Source

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configuring-a-property-loader-source.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configuring-a-property-loader-source.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configuring a Property Loader Source Use the following tabs in the Step Settings pane for the Property Loader step in the TestStand Sequence Editor to configure the Property Loader step to import properties from various sources: Step Settings —Specifies for each property loader source the type of pr

### Configuring a Property Loader Source

#### Configuring a Property Loader Source

Use the following tabs in the Step Settings pane for the Property Loader step in the TestStand Sequence Editor to configure the Property
Loader step to import properties from various sources:

- Step Settings 
 —Specifies for each property loader source the type of property loader
source format to be used, name of the source, location of the source along with various
other configuration options.
- Target File and Source Settings 
 —Specifies the various advanced options like target sequence
and target sequence file to which values will be imported, location of the alias file and
various other options which are specific to a particular type of plugin.

Parent topic:

Property Loader Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/connect-disconnect-operation-ivi-switching-mo.html language=enus -->
## TOPIC 03504: Connect/Disconnect Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/connect-disconnect-operation-ivi-switching-mo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/connect-disconnect-operation-ivi-switching-mo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect/Disconnect Operation (IVI Switching Mode) The Connect/Disconnect operation configures the paths for the IVI logical name the step specifies. The Connect/Disconnect operation contains the following options: Action —Specifies whether to connect or disconnect the path between the specified Sour

### Connect/Disconnect Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Connect/Disconnect Operation (IVI Switching Mode)

The Connect/Disconnect operation configures the paths for the IVI logical name the step specifies.

The Connect/Disconnect operation contains the following options:

- Action 
 —Specifies whether to connect or disconnect the path between the specified Source and Destination channels, or disconnect all previously connected paths. The Action operation returns as soon as the instrument is ready for another operation. This may be before or after the switches involved settle. Use the Wait operation when you want to wait until all switches have debounced.
 
 Supported Value
 DescriptionConnect (0)
 Creates a path between the specified Source and Destination channels.
 Disconnect (1)
 Destroys the path between the specified Source and Destination channels.
 Disconnect All (2)
 Disconnects all paths previously created.
- Source 
 —The name of the Source channel you are connecting or disconnecting. The string expression must evaluate to be a valid virtual channel name as the IVI configuration tool for the logical name being used defines.
- Destination 
 —The name of the Destination channel you are connecting or disconnecting. The string expression must evaluate to be a valid virtual channel name as the IVI configuration tool for the logical name being used defines.

Parent topic:

IVI Switching Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/connect-disconnect-operation-switch-executive.html language=enus -->
## TOPIC 03505: Connect/Disconnect Operation (Switch Executive Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/connect-disconnect-operation-switch-executive.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/connect-disconnect-operation-switch-executive.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect/Disconnect Operation (Switch Executive Mode) In Switch Executive mode, the Connect/Disconnect operation configures the routes for the virtual device name the step specifies. The Connect/Disconnect operation contains the following options: Action —Specifies whether to connect or disconnect th

### Connect/Disconnect Operation (Switch Executive Mode) - Edit IVI Switch Step Dialog Box

#### Connect/Disconnect Operation (Switch Executive Mode)

In Switch Executive mode, the Connect/Disconnect operation configures the routes for the virtual device name the step specifies.

The Connect/Disconnect operation contains the following options:

- Action 
 —Specifies whether to connect or disconnect the specified routes, or disconnect all previously connected routes. This operation returns as soon as the instrument is ready for another operation, which may be before or after the switches involved settle. Use the
 Wait for Debounce 
 option when you want to wait until all switches have debounced.
 
 Supported Value
 DescriptionConnect (0)
 Creates the paths for the specified routes in the Route(s) to Connect control.
 Disconnect (1)
 Destroys the paths the specified routes in the Route(s) to Disconnect control defines.
 Disconnect All (2)
 Disconnects all previously created paths.
 Connect/Disconnect (3)
 Creates the paths for the routes specified in the Route(s) to Connect control, and destroys the paths for the routes specified in the Route(s) to Disconnect control. Use the Operation Order control to specify whether the Disconnect operation occurs before or after the Connect operation.
- Route(s) to Connect 
 —The routes you are connecting. The expression must be a valid
 route specification string 
 as the NI Switch Executive configuration for the virtual device name being used defines. The string can be a combination of route group alias names, route names, and physical route paths. You can use the Switch Find Route expression function to dynamically determine a physical route path at run time.
- Route(s) to Disconnect 
 —The routes you are disconnecting. The expression must be a valid
 route specification string 
 as the NI Switch Executive configuration for the virtual device name being used defines. The string can be a combination of route group alias names, route names, and physical route paths. You can use the Switch Find Route expression function to dynamically determine a physical route path at run time.
- Multiconnect Mode 
 —The behavior when more than one connection operation occurs on a specific route.
 
 Supported Value
 DescriptionNo Multi-connect (0)
 A route can only connect once. Any attempt to reconnect an already connected route results in an error.
 Multi-connect Routes (1)
 A route can connect multiple times. The route must contain the same endpoints and path. NI Switch Executive automatically reference counts the routes. If you issue multiple Connect operations for a specific route, the route is not physically disconnected until an equal number of Disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The Disconnect All operation disconnects a route even if the route reference count is greater than one.
 Use Default Setting for Routes (-1)
 A route defaults to the multiconnect mode as predefined for each route in NI Switch Executive.
- Operation Order 
 —Specifies whether the Disconnect operation occurs before or after the Connect operation.
 
 Supported Value
 DescriptionDisconnect before Connect (1)
 Disconnect the specified routes before connecting any routes. This is the typical mode of operation.
 Connect before Disconnect (2)
 Connect the specified routes before disconnecting any routes. Use
 Connect Before Disconnect
 when you are switching current and want to ensure that a load is always connected to the source.
- Connection Lifetime 
 — The lifetime TestStand applies to the routes specified for the connect or connect/disconnect actions. You can specify whether you want the route to exist until manually disconnected later or until the step, sequence, thread, or execution completes. When you use the multiconnect route mode, a route can exist longer if another step specifies its own lifetime for the same route. Selecting a lifetime other than manual guarantees that the route stays connected as long as the step, sequence, thread, or execution in which you connect is executing. If you manually disconnect a route previously connected using a non-manual lifetime setting, TestStand releases the reference to the route for the last step that performed a connect action for the route.
- Wait for Debounce 
 —When you enable this option, the Action operation waits for all switches to debounce before returning to TestStand. The Wait for Debounce option occurs after both the Connect and Disconnect operations are complete.

Parent topic:

Switch Executive Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/connection-configuration-view.html language=enus -->
## TOPIC 03506: Connection Configuration View

- bundle_id: `teststand-api-reference`
- source_path: `tsref/connection-configuration-view.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/connection-configuration-view.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connection Configuration View The Connection Configuration View is shown when defining the connection configuration to the SCM server, or if the connection configuration for the current sequence file is invalid. If a valid connection configuration has already been defined for the current sequence fi

### Connection Configuration View

#### Connection Configuration View

The Connection Configuration View is shown when defining the connection configuration to the SCM server, or if the connection configuration for the current sequence file is invalid. If a valid connection configuration has already been defined for the current sequence file, the Connection Configuration View is not shown.

#### Server

The URL of the SCM server you are connecting to. The value is saved with the imported specifications as an SCM attribute. The default value is: https://specmanagement.io/

#### API Token

The alphanumeric API token value created in your SCM server to access SCM REST APIs. The Connection Configuration View encrypts the value when importing it to the sequence file as an SCM attribute. The encryption is directly associated with a Windows user and machine. Users must enter an API token value when using a sequence file with an existing saved SCM configuration on a new Windows user or machine, even if the saved configuration is valid.

#### Connect Button

Validates the Server and API Token values. The
 [Product Configuration View](product-configuration-view.html)
 is shown if the Server and API Token values are valid. Otherwise, the Connection Configuration View persists, and an error is reported. The Connect button is enabled after setting the API Token value.

#### See Also

[Import/Update from Specification Compliance Manager (SCM) Tool](import-update-from-specification-compliance-m.html)

[View Differences Dialog](view-differences-dialog.html)

[Specification Compliance Manager Report Options Dialog Box](specification-compliance-manager-report-optio.html)

Parent topic:

Import/Update from Specification Compliance Manager (SCM) Tool

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/connection-tab-data-link-properties-dialog-bo.html language=enus -->
## TOPIC 03507: Connection Tab - Data Link Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/connection-tab-data-link-properties-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/connection-tab-data-link-properties-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connection Tab The contents of the Connection tab vary for each OLE DB provider. If the connection requires a password, you must save the password in the connection string by enabling the Allow Saving Password control. If you want to use the Microsoft OLE DB Provider for ODBC drivers to connect to a

### Connection Tab - Data Link Properties Dialog Box

#### Connection Tab

The contents of the Connection tab vary for each OLE DB provider.

Note

- If the connection requires a password, you must save the password in the connection string by enabling the
 Allow Saving Password 
 control.
- If you want to use the Microsoft OLE DB Provider for ODBC drivers to connect to an
 ODBC data source 
 , you must first configure a data source name within the ODBC Administrator.

Click
 Help
 to launch the Microsoft online help for this tab.

#### See Also

[Database Known Issues](/csh?context=ts_tsfundamentals_database_known_issues)

[Database Logging](/csh?context=ts_tsfundamentals_database_connectivity)

[ODBC Data Source Administrator dialog box](/csh?context=ts_tsfundamentals_odbc_admindb)

Parent topic:

Data Link Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/constant-sweep-parameter-strategy.html language=enus -->
## TOPIC 03508: Constant Sweep Parameter Strategy

- bundle_id: `teststand-api-reference`
- source_path: `tsref/constant-sweep-parameter-strategy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/constant-sweep-parameter-strategy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Constant strategy with the Sweep Loop step to specify the value of a constant sweep parameter. At the beginning of each iteration, the sweep parameter is set to the value specified. When the Constant strategy is selected for a sweep parameter, the following additional option is available: Co

### Constant Sweep Parameter Strategy

Use the Constant strategy with the
 [Sweep Loop](sweep-loop-step.html)
 step to specify the value of a constant sweep parameter. At the beginning of each iteration, the sweep parameter is set to the value specified.

When the Constant strategy is selected for a sweep parameter, the following additional option is available:

- Constant 
 —The sweep parameter value. The value may be a number of any representation, string, Boolean, or enumeration.

Note

Parent topic:

Sweep Parameter Strategies

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/contents-tab-report-options-dialog-box.html language=enus -->
## TOPIC 03509: Contents Tab - Report Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/contents-tab-report-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/contents-tab-report-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contents Tab The Contents tab contains the following options: Report Format —The output format of the report file. Use this ring control to specify an HTML document ( .html ), an ASCII-text file ( .txt ), an XML document ( .xml ), or an Automatic Test Markup Language (ATML) report document ( .xml ).

### Contents Tab - Report Options Dialog Box

#### Contents Tab

The Contents tab contains the following options:

- Report Format 
 —The output format of the report file. Use this ring control to specify an HTML document (
 .html 
 ), an ASCII-text file (
 .txt 
 ), an
 XML document 
 (
 .xml 
 ), or an
 Automatic Test Markup Language (ATML) 
 report document (
 .xml 
 ). ATML reports validate against the approved version 6.01, non-finalized version 5.0, or approved version 2.02 of the
 Test Results and Session Information 
 schema the ATML standard defines.
 Note 
 No plans exist to approve version 5.0 of the ATML Test Results and Session
Information schema.
- Style Sheet 
 —The
 path 
 to an
 XML 
 or
 ATML 
 style sheet file TestStand stores in the processing instruction of an XML or ATML report. You can specify an absolute or relative pathname for the file. Report generation determines the absolute path to a style sheet file using the TestStand search directory paths. This option is available for the XML and ATML report document formats.
- Store Absolute Path 
 —When enabled, instructs TestStand to use the absolute path for the style sheet file when storing the path in the processing instructions of an
 XML 
 or
 ATML 
 report. The style sheet file path is determined using the
 
 Engine.FindFileEx 
 method in the TestStand API. Style sheet paths are relative with respect to the file path of the XML or ATML report.When you disable this option, the path specified in the
 Style Sheet 
 option is stored in the processing instructions of the XML or ATML report.
- Generate PDF 
 —Generates a copy of the report in PDF format in addition to the report format you select. TestStand generates the PDF in the same directory as the report with the same name. Refer to Generating PDF Reports
 
 for more information.
- Default Numeric Format 
 —Determines how the report formats numeric values for which you did not specify a numeric format. Click
 Edit Format 
 to launch the
 Numeric Format 
 dialog box.
- Report Colors 
 —The colors of the report. This option is available only for the HTML or XML Document formats.
- Include Step Results 
 —Displays the results of each step. Disable this option when you want to only include a header for each UUT. The header indicates the UUT status.
 
 Note 
 TestStand does not generate a report when you disable the Include Step Results option and you specify the report format as ATML in the Report Format ring control.
  - Result Filtering Expression 
 —Applies a filtering expression the report generator evaluates for each step result to determine which steps appear in the report. The report generator includes the step in the report when the expression evaluates to
 True 
 . Use the ring control to select predefined expressions for including all steps, failing steps only, or passing steps only.
 Alternatively, you can create a custom expression for this field or modify one of the predefined expressions. You can use any subproperty within the
 Step.Result
 container in the Result Filtering Expression, but you must use
 Result
 in place of
 Step.Result
 . For example, if you want to include only failing steps in the report, set the expression to
 Result.Status == "Failed"
 . 
 Note 
 This option is not available for XML reports. You can filter XML results by
 [modifying the XML style sheets](/csh?context=ts_tsreports_xml_custom)
 .
  - Include Test Limits 
 —Adds to the report all result properties that indicate that they contain test limits.
  - Include Attributes 
 —Adds to the report all attributes associated with result properties. This option is disabled by default.
  - Include TestStand Extension Elements 
 —Adds to the report TestStand extension elements. This option is disabled for XML reports because XML reports use style sheets to filter TestStand extension elements.
  - Include Measurements 
 —Adds to the report all result properties that indicate that they contain measurements.
  - Use the following options to configure how the report displays arrays:
    - Include Arrays 
 —Options for including or excluding arrays in reports. The following options are available in the ring control:
      - Do Not Include Arrays 
 —Array values do not appear in the report.
 Note 
 This option instructs the report generation to not include array data in HTML and TXT report files. Report generation always includes array data in ATML 6.01, ATML 5.0, and XML report files, and this option instructs the report stylesheets to not display array data.
      - Insert Table 
 —Array values appear in tables.
      - Insert Graph 
 —Numeric array values appear in
 graphs 
 . This option is available only for ATML 6.01, ATML 5.0, XML, and HTML reports.
 Note 
 ATML 6.01, ATML 5.0, and XML reports might display a
 [table of measurement data](/csh?context=ts_tsreports_xml_meas_data)
 instead of a graph under certain conditions.
    - Filter 
 —Options for limiting the amount of data the arrays add to the report. The following options are available in the ring control:
      - Include All 
 —All array elements appear in the report.
      - Include Up To Max 
 —The report truncates arrays to the maximum size in the Max Elements control.
      - Exclude If Larger Than Max 
 —The report does not display arrays that contain more than the number of elements in the Max Elements control.
      - Decimate If Larger Than Max 
 —The report samples and displays the specified maximum number of elements from arrays that contain more than the number of elements in the Max Elements control.
    - Max Elements 
 —The maximum array size that applies to options you select in the Filter control.
- Include Execution Times 
 —Adds to the report the time each step module takes to execute. This information includes the time the subsequence, LabVIEW VI, or C function requires to execute. It does not include the time the TestStand Engine requires to evaluate preconditions, load the step module, and so on.
- Append if File Already Exists 
 —Appends the report to the target file, if the target file already exists. When you disable this option, the report overwrites the target file.
 Note 
 If you create a separate report for each UUT and disable this option, the report for each UUT overwrites any existing target file.
- On-The-Fly Reporting 
 —Specifies whether TestStand generates reports after testing a UUT or
 generates reports concurrently with execution 
 . When you enable this option, the process model uses Post Result callback sequences to append new formatted results to the report. When you disable this option, the process model creates the report after testing each UUT.
 Note 
 Refer to the
 [Advanced Result Processing Settings](advanced-result-processing-settings-dialog-bo.html)
 dialog box help for more information about configuring additional on-the-fly result processing options.
- Only Display Latest Results 
 —When you enable this option, the report generator periodically purges results maintained in memory while generating on-the-fly reports. When you enable this option, the displayed report only contains results that have not been previously purged. The purged results are appended to the report file saved to disk. Typically, you use this option when executions run for a long period and you want to limit the size of the report in memory.
 Note 
 Enable the
 Discard Results or Disable Results when not Required by Model
 option in the
 [Model Options](model-options-dialog-box.html)
 dialog box to further reduce the amount of memory used during TestStand executions.
- Select a Report Generator for Producing the Report Body 
 —Contains options that direct TestStand to use a sequence or DLL to produce the body of the report. The report body is the section of the report between the header and footer that contains individual results for each sequence and step TestStand called. In the default process model, the TestReport callback determines whether TestStand builds the report body with a sequence call or with a DLL call.
 If you select the Sequence option to generate the report, the TestReport callback calls the AddReportBody sequence in either
 ReportGen_txt.seq 
 or
 ReportGen_html.seq 
 to build the report body. The sequence report generator uses a series of sequences with steps that recursively process the result list for the execution.
 If you select the DLL option to generate the report, the TestReport callback calls a function in a DLL to build the report body. The DLL report generator is a single call into a C-language DLL that processes the entire result list for the execution before returning. You can access the project and source code for the LabWindows/CVI-built DLL. When you select the DLL option, TestStand generates reports faster but does not call ModifyReportEntry callbacks.
 Note 
 The DLL option is not available for XML or ATML reports.

#### See Also

[Comparing Report Format Features](/csh?context=ts_tsreports_compare)

[Displaying Measurement Data as Graphs](/csh?context=ts_tsreports_measurement_data)

[Model Options dialog box](model-options-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

Parent topic:

Report Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/context-menu-workspace-pane.html language=enus -->
## TOPIC 03510: Context Menu - Workspace Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/context-menu-workspace-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/context-menu-workspace-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Workspace Context Menu The items in the Workspace context menu vary depending on the location you click on the Workspace pane. The Workspace context menu can contain the following items: Analyze Workspace —Launches the TestStand Sequence Analyzer to start analysis of the current workspace file. Inse

### Context Menu - Workspace Pane

#### Workspace Context Menu

The items in the Workspace context menu vary depending on the location you click on the
 [Workspace](workspace-pane.html)
 pane. The Workspace context menu can contain the following items:

- Analyze Workspace 
 —Launches the
 TestStand Sequence Analyzer 
 to start analysis of the current workspace file.
- Insert New Project into Workspace 
 —Creates a new project on disk and adds the project to the workspace. This option is available only when you click on the root workspace object.
- Add Existing Project to Workspace 
 —Adds an existing project to the workspace. This option is available only when you click on the root workspace object.
- Display File Hierarchy 
 —Displays a graph in the
 Sequence Hierarchy 
 window of the hierarchy of all sequences in the sequence file.
- Display Hierarchy Using 
 —Displays a graph in the Sequence Hierarchy window of the hierarchy of all sequence calls starting at the process model entry point you select. TestStand uses the station process model to populate the list of entry points. This option uses the current sequence file as a client sequence file.
- New Folder 
 —Adds a new folder to the selected project or sequence file.
- Insert Folder From Disk 
 —Adds a folder from disk to the selected project or sequence file. After you select the folder, a dialog box prompts you to add the files within the folder. Click
 Yes 
 to insert the folder you select and all the folder content so the content of the new folder in the Workspace matches the directory structure of the folder on disk. Click
 No 
 to insert the folder and subfolders without adding the files the folders contain.
 Note 
 Use
 Insert Code Modules
 from the context menu on the folder you insert to include
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 files in the workspace for each sequence file in the folder.
- Add Files to Folder/Project 
 —Adds the files you choose from a dialog box to the selected workspace folder or project.
- Insert Code Modules 
 —Adds code module files to the workspace. Under each sequence file, TestStand creates a folder called
 CodeModules 
 that contains the code modules the sequence file calls. The folder also includes any code module source files the sequence file references.
- Add to Source Code Control 
 —Adds the selected project or file to source code control.
- Remove from Source Code Control 
 —Removes the selected project or file from source code control.
- Get Latest Version 
 —Copies the latest version of the selected project or file from source control to the local computer. Click
 Advanced Options 
 to launch a dialog box that varies based on the SCC provider.
- Check Out <
 filename
 > 
 —Checks the selected files out of source control and places a writable copy of the files on the local computer. Click
 Advanced Options 
 to launch a dialog box that varies based on the SCC provider.
 Note 
 Before you make changes to a file, check the file out of source control. For a file checked into source control, if you make the local copy of the file writable and then make changes, TestStand asks you if you want to reload the file when you try to check the file out. If you reload the file, the version checked into source control overwrites the version on the local computer and any changes you have made to the local file.
- Check In <
 filename
 > 
 —Checks the selected file into source control.
- Undo Check Out 
 —Checks the selected file back into source control and discards any changes you have made to the file. Click
 Advanced Options 
 to launch a dialog box specific to the SCC provider.
- Show History 
 —Shows the SCC history of the selected file. The history gives you information about previous versions of the file.
- Show Differences 
 —Shows the differences between the two files you select to compare. For example, you could compare the local copy of a file with the same file checked into source control. If you select to compare sequence files and you have either Microsoft Visual SourceSafe or MKS Source Integrity as the default provider, the
 TestStand File Diff and Merge 
 utility shows the differences between the two sequence files. If you have a provider other than Microsoft Visual SourceSafe or MKS Source Integrity, the diff utility for the provider presents the differences between the two files in a new window. In this case, you can use the SCC provider diff window to diff the sequence files only as text files. Unless the files have only minor differences, it is not practical to diff sequence files as text files. Complete the following steps to diff the files as sequence files.
  1. To preserve the changes, make a copy of the local file.
  2. Undo checkout of the local file and recheck the file out to obtain the latest changes from source control.
  3. Load the local file and the copy that contains the changes into the
 TestStand Sequence Editor 
 .
  4. Use the TestStand File Diff and Merge utility to merge the changes from the copy into the local file you have checked out.
- Cut 
 —Removes the selected workspace object and places it on the clipboard.
- Copy 
 —Copies the selected workspace object to the clipboard.
- Paste 
 —Inserts a workspace object from the clipboard.
- Delete 
 —Deletes the workspace object.
- Rename 
 —Changes the name the Workspace window displays for the selected project or folder.
- Refresh All SCC Status 
 —Refreshes the SCC status of all files in the workspace and verifies that the files exist on disk.
- Properties 
 —The properties of the selected file. This command launches the
 Workspace Properties 
 dialog box, which can contain the following tabs:
  - General 
 —The path name of the file, the date the file was last modified, and the SCC status of the file.
  - Source Control 
 —Changes the source control project and launches the source control system. Click
 Advanced Options 
 to launch a dialog box specific to the SCC provider. For a workspace item, this tab also enables you to change and connect to a source control provider and to change the source control user name.
 Note 
 This tab is only visible for workspace and project items.

#### See Also

[Selecting a Source Code Control Provider](/csh?context=ts_tsfundamentals_scc_selecting)

[TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html)

[Workspace Pane](workspace-pane.html)

[Workspace Properties dialog box](workspace-object-properties-dialog-box.html)

Parent topic:

Workspace Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/continue-step.html language=enus -->
## TOPIC 03511: Continue Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/continue-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/continue-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Continue step to cause the next iteration of an enclosing For , For Each , While , or Do While loop block to begin. Configuring the Step Use the Properties tab of the Step Settings pane in the TestStand Sequence Editor or the Step Properties dialog box in a TestStand User Interface to configur

### Continue Step

Use a Continue step to cause the next iteration of an enclosing
 [For](for-step.html)
 ,
 [For Each](for-each-step.html)
 ,
 [While](while-step.html)
 , or
 [Do While](do-while-step.html)
 loop block to begin.

#### Configuring the Step

Use the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Step Properties](step-properties-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Continue step.

#### Step Properties

The Continue step type does not define any additional step properties other than
 [custom properties common to all steps](/csh?context=ts_tsfundamentals_custom_result_props)
 .

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/cpu-affinity-edit-tab.html language=enus -->
## TOPIC 03512: CPU Affinity Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/cpu-affinity-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/cpu-affinity-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit CPU Affinity Settings from the context menu for a CPU Affinity step to display the CPU Affinity Settings edit tab. All expression controls for affinity mask represent the affinity mask as a numeric value where each bit of the value specifies a CPU. You can use the 0b prefix to specify a

### CPU Affinity Edit Tab

Select
 Edit CPU Affinity Settings
 from the context menu for a CPU Affinity step to display the CPU Affinity Settings edit tab. All expression controls for affinity mask represent the affinity mask as a numeric value where each bit of the value specifies a CPU. You can use the
 0b
 prefix to specify a binary number. For example, a value of
 15
 (
 0b00001111
 ) represents the CPUs in a quad-core system and a value of
 10
 (
 0b00001010
 ) represents CPUs 2 and 4 in the quad-core system.

The following operations are available when you use the CPU Affinity step type:

- Get System Affinity 
 —Gets the default system affinity mask.
- Get Process Affinity 
 —Gets the current process affinity mask.
- Set Process Affinity 
 —Sets the affinity mask for the current process.
- Get Thread Affinity 
 —Gets the current thread affinity mask.
- Set Thread Affinity 
 —Sets the affinity mask for the current thread.

Refer to
 [Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

CPU Affinity Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/cpu-affinity-step-configuration-dialog-box.html language=enus -->
## TOPIC 03513: CPU Affinity Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/cpu-affinity-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/cpu-affinity-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure CPU Affinity in the context menu for the CPU Affinity step to launch the Configure CPU Affinity dialog box from a TestStand User Interface . You can also click the Configure CPU Affinity button on the General tab of the Step Properties dialog box. Use the Configure CPU Affinity dial

### CPU Affinity Step Configuration Dialog Box

Select
 Configure CPU Affinity
 in the context menu for the
 [CPU Affinity step](cpu-affinity-step.html)
 to launch the Configure CPU Affinity dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click the
 Configure CPU Affinity
 button on the
 [General tab of the Step Properties](general-tab-step-properties-dialog-box.html)
 dialog box.

Use the Configure CPU Affinity dialog box to select an operation for the CPU Affinity step to perform. All expression controls for affinity mask represent the affinity mask as a numeric value where each bit of the value specifies a CPU. You can use the
 0b
 prefix to specify a binary number. For example, a value of
 15
 (
 0b00001111
 ) represents the CPUs in a quad-core system and a value of
 10
 (
 0b00001010
 ) represents CPUs 2 and 4 in the quad-core system.

You can select from the following operations when you use the CPU Affinity step type:

- Get System Affinity 
 —Gets the default system affinity mask.
- Get Process Affinity 
 —Gets the current process affinity mask.
- Set Process Affinity 
 —Sets the affinity mask for the current process.
- Get Thread Affinity 
 —Gets the current thread affinity mask.
- Set Thread Affinity 
 —Sets the affinity mask for the current thread.

Refer to
 [Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.

#### See Also

[CPU Affinity step](cpu-affinity-step.html)

[General Tab - Step Properties dialog box](general-tab-step-properties-dialog-box.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

CPU Affinity Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/cpu-affinity-step.html language=enus -->
## TOPIC 03514: CPU Affinity Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/cpu-affinity-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/cpu-affinity-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a CPU Affinity step to adjust the CPU affinity of a process or thread to allow the process or thread to run on a given set of CPUs on the computer . You can also use the Default CPU Affinity For Threads option on the Preferences tab of the Station Options dialog box to determine which CPUs the u

### CPU Affinity Step

Use a CPU Affinity step to adjust the CPU affinity of a process or thread to allow the process or thread to
 [run on a given set of CPUs on the computer](/csh?context=ts_tsfundamentals_smp_clarification)
 .

You can also use the Default CPU Affinity For Threads option on the
 [Preferences](preferences-tab-station-options-dialog-box.html)
 tab of the
 [Station Options](station-options-dialog-box.html)
 dialog box to determine which CPUs the user interface thread uses and the default CPUs for new executions. Use the
 [Sequence Call Advanced Settings window](sequence-call-advanced-settings-window.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Thread Settings](thread-settings-dialog-box.html)
 dialog box or
 [Execution Settings](execution-settings-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to set which CPUs to use when executing a sequence in a new thread or execution.

#### Configuring the Step

Use the
 [CPU Affinity Settings](cpu-affinity-edit-tab.html)
 edit tab in the sequence editor and the
 [CPU Affinity Step Configuration](cpu-affinity-step-configuration-dialog-box.html)
 dialog box in a user interface to configure the CPU Affinity step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the CPU Affinity step type defines the following step properties:

- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Get System CPU Affinity,
 1 
 = Get Process CPU Affinity,
 2 
 = Set Process CPU Affinity,
 3 
 = Get Thread CPU Affinity, and
 4 
 = Set Thread CPU Affinity.
- Step.Expr 
 —An expression value that specifies or stores the CPU affinity for the system, process, or thread. For a
 Get 
 operation, the expression specifies a variable in which to store the value. For a
 Set 
 operation, the expression specifies a CPU affinity value. The CPU affinity is a numeric value where each bit represents a CPU. The lowest-order bit represents the first CPU. For example, a value of 
12
 (0b1100) 
 represents CPUs 3 and 4 on a quad-core system.

#### See Also

[CPU Affinity Step Type Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64cpuaffinitysteptype)

[Synchronization Step Types](synchronization-step-types.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-code-templates-dialog-box.html language=enus -->
## TOPIC 03515: Create Code Templates Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-code-templates-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-code-templates-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Create on the Code Templates tab of the Step Type Properties dialog box to launch the Create Code Templates dialog box. The Create Code Templates dialog box contains the following options: New Code Template Name —The name for the code template. TestStand uses this name to specify the subdirect

### Create Code Templates Dialog Box

Click
 Create
 on the
 [Code Templates](code-templates-tab-step-type-properties-dialo.html)
 tab of the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box to launch the Create Code Templates dialog box.

The Create Code Templates dialog box contains the following options:

- New Code Template Name 
 —The name for the code template. TestStand uses this name to specify the subdirectory under
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \CodeTemplates 
 where the code template files are created.
- New Code Template Description 
 —A brief description for the code template.
- New Code Template Type 
 —The type of code template. The code template type determines which adapter the
 code module 
 is associated with.
- Base the New Template on 
 —An existing code template for TestStand to copy.

#### See Also

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-columns-dialog-box.html language=enus -->
## TOPIC 03516: Create Columns Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-columns-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-columns-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Import/Export Properties dialog box, select Database in the Data Location ring control, and click Create Columns on the Properties tab to launch the Create Columns dialog box. The Create Columns dialog box contains the following options: Data Link Name —The name of the data link to create

### Create Columns Dialog Box

Launch the
 [Import/Export Properties](legacy-import-export-properties-dialog-box.html)
 dialog box, select
 Database
 in the Data Location ring control, and click
 Create Columns
 on the
 [Properties](import-export-properties-dialog-box2.html)
 tab to launch the Create Columns dialog box.

The Create Columns dialog box contains the following options:

- Data Link Name 
 —The name of the data link to create columns with. Click
 Select Data Link 
 to select a
 predefined data link 
 from a list.
- Columns 
 —The column names you selected in the
 Edit Legacy Property Loader 
 dialog box but do not exist in the specified SQL statement.
- Table 
 —The table in which to create the selected column.
- Data Type 
 —The data type for the selected column. TestStand maps TestStand data types to appropriate database data types or uses a
 '?' 
 value in the column type control to prompt you to select a column type value.
- Parameters 
 —Any parameter information for the data type of the selected column. For example, you can specify a size limit for a character data type by entering a number in the Parameters control.
- Create Columns 
 —Creates columns for the checked items in the Columns list control.

#### See Also

[Data Link Properties dialog box](data-link-properties-dialog-box.html)

[Edit Legacy Property Loader dialog box](edit-legacy-property-loader-dialog-box3.html)

[Import/Export Properties dialog box](legacy-import-export-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-csv-output-record-stream-dialog-box.html language=enus -->
## TOPIC 03517: Create CSV Output Record Stream Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-csv-output-record-stream-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-csv-output-record-stream-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Create CSV Output Record Stream dialog box in a TestStand User Interface to configure the Create CSV Output Record Stream step. The Create CSV Output Record Stream dialog box contains the following options: CSV File Path —Specify the path to the CSV file to write, either by browsing to the f

### Create CSV Output Record Stream Dialog Box

Use the Create CSV Output Record Stream dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Create CSV Output Record Stream step.

The Create CSV Output Record Stream dialog box contains the following options:

- CSV File Path 
 —Specify the path to the CSV file to write, either by browsing to the file or using an expression. To specify by expression, check the
 Specify by Expression 
 check box.
- File Open Mode 
 —Expression that specifies the file open mode for the underlying CSV file. The mode can be any of the following FileOpenModes constants:
  - FileOpenMode_NoOptions 
 —Create the file if it does not exist. Fail with a runtime error if the file exists.
  - FileOpenMode_Truncate 
 —If the file exists, overwrite it, deleting the previous contents. Create a new file if it does not exist.
  - FileOpenMode_Append 
 —If the file exists, append to the end of it, preserving the existing contents. Create a new file if it does not exist.
  - FileOpenMode_Uniquify 
 —Create a new file if it does not exist. If a file with the specified path exists, attempt to make the file name unique by appending “_” (underscore) plus a numeric suffix to the file name. For example, if AlreadyExists.csv already exists, AlreadyExists_2.csv is tried, then AlreadyExists_3.csv, etc. until a unique name has been found. If a unique name is not found after 10000 attempts, the operation fails with a runtime error.
- Flush After Every Write 
 —Sets the CsvFileOutputRecordStream.AutoFlush property on the CsvFileOutputRecordStream the step creates.
 Note 
 Enabling AutoFlush will adversely impact performance.
- Output Record Stream Reference (Optional) 
 —Expression that specifies where to store the reference to the CsvFileOutputRecordStream the step creates.
- Tag (Optional) 
 —Expression that specifies a string data tag to write to the CSV file before any headers or data.
- Field Headers (Optional) 
 —Expression that specifies the field names for the CsvFileOutputRecordStream. The specified headers are written immediately to the underlying CSV file. The expression may be either a container or an array of strings. If a container is specified, its subproperty names define the field headers. If an array is specified, the array elements define the field headers. In addition, if
 Attach to Execution 
 is checked, the field headers will be written to the Report View for the associated ExecutionOutputRecordStream.
  - Specify Prototype 
 —Writes both the field names and data types to the CSV file as a
 prototype 
 .
- Header Mapping (Optional) 
 —Specifies the mapping from elements (either subproperties or array elements) in the field headers to fields in the stream. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that elements 0, 3, 4, 5, 8, and 7 specify the field names. The final range in the list may be open-ended. For example, "2, 3-" indicates that elements 2, 3, and all elements beyond 3 specify the field names.
- Attach to Execution 
 —Check the
 Attach to Execution 
 checkbox to attach the newly created stream to the current execution.
  - Stream Name 
 —The name of the
 ExecutionOutputRecordStream 
 to associate the newly created CsvFileOutputRecordStream with. If an ExecutionOutputRecordStream with the specified name is already attached to the current execution, the existing one is used. Otherwise, a new ExecutionOutputRecordStream is created with the specified name. You can use the stream name directly with the
 Write Record step type 
 . You can also use it to retrieve the ExecutionOutputRecordStream by invoking ExecutionOutputRecordStreams.GetStream() via the Execution.OutputRecordStreams property of the current execution.
  - Execution Output Record Stream (Optional) 
 —Expression that specifies where to store the reference to the ExecutionOutputRecordStream the step creates or retrieves.
  - Report View 
 —These options control how the ExecutionOutputRecordStream displays information in the Report View.
    - Records to Display 
 —Specifies that value of the ExecutionOutputRecordStream.NumRecordsToDisplayInReportView property of the ExecutionOutputRecordStream. Specify -1 to indicate all records should be displayed. Specify 0 to indicate that no records should be displayed.
    - Set Active Report 
 —Check the Set Active Report checkbox to cause the ExecutionOutputRecordStream to become the active report displayed in the Report View for the current execution. If you leave the box unchecked, you can view the ExecutionOutputRecordStream in the Report View by selecting it manually from the Active Report menu item.

Parent topic:

New CSV Output Stream Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-custom-data-type-from-struct-dialog-bo.html language=enus -->
## TOPIC 03518: Create Custom Data Type from Struct Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-custom-data-type-from-struct-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-custom-data-type-from-struct-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Create Type from Struct button located next to a parameter in the Type column of the Parameters Table on the .NET Module tab of the Step Settings pane in the TestStand Sequence Editor or on the Module tab of the Edit .NET Call dialog box in a TestStand User Interface to launch the Create C

### Create Custom Data Type from Struct Dialog Box

Click the
 Create Type from Struct
 button located next to a parameter in the Type column of the Parameters Table on the
 [.NET Module](net-module-tab.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or on the
 [Module](module-tab-edit-net-call-dialog-box.html)
 tab of the
 [Edit .NET Call](edit-net-call-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to launch the Create Custom Data Type from Struct dialog box. The
 Create Type from Struct
 button is available only if the parameter type is a struct, such as a .NET value type.

The Create Custom Data Type from Struct dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- List Box 
 —The .NET element label for the struct, the .NET type of the element, and the property names to which the element will map in the new custom data type. If the type of struct element is object, you can use a combo box in the Type column to select the appropriate TestStand type for the property. The property name is customizable.
- Create Custom Data Type In File 
 —The location where TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

#### See Also

[.NET Module](net-module-tab.html)
 tab

[Edit .NET Call dialog box](edit-net-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-batch-settings-edit-tab.html language=enus -->
## TOPIC 03519: Create Operation - Batch Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-batch-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-batch-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation Enable the Create option on the left of the Batch Settings panel. The Create operation contains the following options: Batch Name Expression —A unique name for the Synchronization object using a literal string or an expression that evaluates to a string. You can use the name attribu

### Create Operation - Batch Settings Edit Tab

#### Create Operation

Enable the
 Create
 option on the left of the Batch Settings panel.

The Create operation contains the following options:

- Batch Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location to store a Boolean value that indicates whether the Synchronization object already exists.
- Batch Reference Lifetime 
 —The lifetime of the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Default Batch Synchronization 
 —The default method of batch synchronization to use with the Batch object. This setting affects the per-step batch synchronization setting when the Batch Synchronization setting on the
 Synchronization panel 
 on the
 Properties 
 tab of a step is set to
 Use model setting 
 or
 Use sequence file setting 
 and when the Batch Synchronization setting of a sequence file is set to
 Use model setting 
 . Per-step batch synchronization regards each step as if it is within its own synchronized section of the type you specify.

#### See Also

[Synchronization Panel](synchronization-panel-step-settings-pane.html)

[Properties Tab](properties-tab-step-settings-pane.html)

Parent topic:

Batch Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-batch-specification-step-con.html language=enus -->
## TOPIC 03520: Create Operation - Batch Specification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-batch-specification-step-con.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-batch-specification-step-con.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation The Create operation contains the following options: Batch Name Expression —A unique name for the Synchronization object using a literal string or an expression that evaluates to a string. You can use the name attribute of synchronization objects to perform synchronization operation

### Create Operation - Batch Specification Step Configuration Dialog Box

#### Create Operation

The Create operation contains the following options:

- Batch Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —A location to store a Boolean value that indicates whether the Synchronization object already exists.
- Batch Reference Lifetime 
 —The lifetime of the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Default Batch Synchronization 
 —The default method of batch synchronization to use with the Batch object. This setting affects the per-step batch synchronization setting when the Batch Synchronization setting on the
 Synchronization 
 tab of the
 Step Properties 
 dialog box of a step is set to
 Use model setting 
 or
 Use sequence file setting 
 and when the Batch Synchronization setting of the sequence file is set to
 Use model setting 
 . Per-step batch synchronization regards each step as if it is within its own synchronized section of the type you specify.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Batch Specification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-lock-settings-edit-tab.html language=enus -->
## TOPIC 03521: Create Operation - Lock Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-lock-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-lock-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation To use a lock, you must first create a reference to a new or existing Lock object. To create a reference, insert a Lock step and select Edit Lock Settings from the context menu for the step. Enable the Create option on the left of the Lock Settings panel. The Create operation contai

### Create Operation - Lock Settings Edit Tab

#### Create Operation

To use a lock, you must first create a reference to a new or existing Lock object. To create a reference, insert a Lock step and select
 Edit Lock Settings
 from the context menu for the step. Enable the
 Create
 option on the left of the Lock Settings panel.

The Create operation contains the following options:

- Lock Name Expression 
 —A name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location to store a Boolean value that indicates whether the Synchronization object already exists.
- Lock Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.

Parent topic:

Lock Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-lock-step-configuration-dial.html language=enus -->
## TOPIC 03522: Create Operation - Lock Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-lock-step-configuration-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-lock-step-configuration-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation To use a lock, you must first create a reference to a new or existing Lock object. To create a reference, insert a Lock step and select Configure Lock from the context menu for the step. Select Create from the Operation ring control in the Lock Step Configuration dialog box. The Cre

### Create Operation - Lock Step Configuration Dialog Box

#### Create Operation

To use a lock, you must first create a reference to a new or existing Lock object. To create a reference, insert a Lock step and select
 Configure Lock
 from the context menu for the step. Select
 Create
 from the Operation ring control in the Lock Step Configuration dialog box.

The Create operation contains the following options:

- Lock Name Expression 
 —A name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the Synchronization object already exists.
- Lock Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.

Parent topic:

Lock Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-notification-settings-edit-t.html language=enus -->
## TOPIC 03523: Create Operation - Notification Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-notification-settings-edit-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-notification-settings-edit-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation Enable the Create option on the left of the Notification Settings panel. The Create operation contains the following options: Notification Name Expression —A unique name for the Synchronization object using a literal string or an expression that evaluates to a string. You can use th

### Create Operation - Notification Settings Edit Tab

#### Create Operation

Enable the
 Create
 option on the left of the Notification Settings panel.

The Create operation contains the following options:

- Notification Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —A location to store a Boolean value that indicates if the Synchronization object already exists.
- Notification Reference Lifetime 
 —The lifetime of the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.

Parent topic:

Notification Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-notification-step-configurat.html language=enus -->
## TOPIC 03524: Create Operation - Notification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-notification-step-configurat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-notification-step-configurat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation The Create operation contains the following options: Notification Name Expression —A unique name for the Synchronization object using a literal string or an expression that evaluates to a string. You can use the name attribute of synchronization objects to perform synchronization op

### Create Operation - Notification Step Configuration Dialog Box

#### Create Operation

The Create operation contains the following options:

- Notification Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location for storing a Boolean value that indicates if the Synchronization object already exists.
- Notification Reference Lifetime 
 —The lifetime of the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.

Parent topic:

Notification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-queue-settings-edit-tab.html language=enus -->
## TOPIC 03525: Create Operation - Queue Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-queue-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-queue-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation To create a reference to a new or existing Queue object, insert a Queue step and select Edit Queue Settings from the context menu for the step. Enable the Create option on the left of the Queue Settings panel. The Create operation contains the following options: Queue Name Expressio

### Create Operation - Queue Settings Edit Tab

#### Create Operation

To create a reference to a new or existing Queue object, insert a Queue step and select
 Edit Queue Settings
 from the context menu for the step. Enable the
 Create
 option on the left of the Queue Settings panel.

The Create operation contains the following options:

- Queue Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —A location to store a Boolean value that indicates whether the Synchronization object already exists.
- Queue Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Maximum Number of Elements 
 —The maximum number of items the queue can store. A value less than or equal to zero specifies that the queue does not have a maximum number of elements. If you know the queue already exists, you may leave this option blank. If you specify a value different than the maximum number of elements for the existing queue, the step reports a run-time error.

Parent topic:

Queue Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-queue-step-configuration-dia.html language=enus -->
## TOPIC 03526: Create Operation - Queue Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-queue-step-configuration-dia.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-queue-step-configuration-dia.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation To create a reference to a new or existing Queue object, insert a Queue step and select Configure Queue from the context menu for the step. The Create operation contains the following options: Queue Name Expression —A unique name for the Synchronization object using a literal string

### Create Operation - Queue Step Configuration Dialog Box

#### Create Operation

To create a reference to a new or existing Queue object, insert a Queue step and select
 Configure Queue
 from the context menu for the step.

The Create operation contains the following options:

- Queue Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the Synchronization object already exists.
- Queue Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Maximum Number of Elements 
 —The maximum number of items the queue can store. A value less than or equal to zero specifies that the queue does not have a maximum number of elements. If you know the queue already exists, you may leave this setting blank. If you specify value different than the maximum number of elements for the existing queue, the step reports a run-time error.

Parent topic:

Queue Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-rendezvous-settings-edit-tab.html language=enus -->
## TOPIC 03527: Create Operation - Rendezvous Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-rendezvous-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-rendezvous-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation Enable the Create option on the left of the Rendezvous Settings panel. The Create operation contains the following options: Rendezvous Name Expression —A unique name for the Synchronization object using a literal string or an expression that evaluates to a string. You can use the na

### Create Operation - Rendezvous Settings Edit Tab

#### Create Operation

Enable the
 Create
 option on the left of the Rendezvous Settings panel.

The Create operation contains the following options:

- Rendezvous Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the Synchronization object already exists.
- Rendezvous Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Number of Threads Per Rendezvous 
 —The number of threads that must rendezvous before the step permits the threads to continue execution past the rendezvous point. This value must be greater than zero. If you know the rendezvous already exists, you may leave this setting blank. If you specify a value different than the setting in the existing rendezvous, the step reports a run-time error.

Parent topic:

Rendezvous Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-rendezvous-step-configuratio.html language=enus -->
## TOPIC 03528: Create Operation - Rendezvous Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-rendezvous-step-configuratio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-rendezvous-step-configuratio.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation The Create operation contains the following options: Rendezvous Name Expression —A unique name for the Synchronization object using a literal string or an expression that evaluates to a string. You can use the name attribute of synchronization objects to perform synchronization oper

### Create Operation - Rendezvous Step Configuration Dialog Box

#### Create Operation

The Create operation contains the following options:

- Rendezvous Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the Synchronization object already exists.
- Rendezvous Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Number of Threads Per Rendezvous 
 —The number of threads that must rendezvous before the step permits the threads to continue execution past the rendezvous point. This value must be greater than zero. If you know the rendezvous already exists, you may leave this setting blank. If you specify a value different than the setting in the existing rendezvous, the step reports a run-time error.

Parent topic:

Rendezvous Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-semaphore-settings-edit-tab.html language=enus -->
## TOPIC 03529: Create Operation - Semaphore Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-semaphore-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-semaphore-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation To use a semaphore, you must first create a reference to a new or existing Semaphore object. Enable the Create option on the left of the Semaphore Settings panel. The Create operation contains the following options: Semaphore Name Expression —A unique name for the Synchronization ob

### Create Operation - Semaphore Settings Edit Tab

#### Create Operation

To use a semaphore, you must first create a reference to a new or existing Semaphore object. Enable the
 Create
 option on the left of the Semaphore Settings panel.

The Create operation contains the following options:

- Semaphore Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the Synchronization object already exists.
- Semaphore Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Initial Semaphore Count 
 —The initial value for the count. This value must be greater than or equal to
 0 
 . If you know the semaphore already exists, you may leave this setting blank. If the semaphore already exists and you specify an initial count that differs from the existing initial count, the step reports a run-time error.

Parent topic:

Semaphore Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-operation-semaphore-step-configuration.html language=enus -->
## TOPIC 03530: Create Operation - Semaphore Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-operation-semaphore-step-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-operation-semaphore-step-configuration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create Operation To use a semaphore, you must first create a reference to a new or existing Semaphore object. The Create operation contains the following options: Semaphore Name Expression —A unique name for the Synchronization object using a literal string or an expression that evaluates to a strin

### Create Operation - Semaphore Step Configuration Dialog Box

#### Create Operation

To use a semaphore, you must first create a reference to a new or existing Semaphore object.

The Create operation contains the following options:

- Semaphore Name Expression 
 —A unique name for the
 Synchronization object 
 using a literal string or an expression that evaluates to a string. You can use the
 name attribute 
 of synchronization objects to perform synchronization operations between executions within a single process or between separate processes and computers.
- Already Exists? (optional output) 
 —A location to store a Boolean value that indicates whether the Synchronization object already exists.
- Semaphore Reference Lifetime 
 —A lifetime for the reference to the Synchronization object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Same as Execution 
 —Releases the object reference after the execution completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Initial Semaphore Count 
 —The initial value for the count. This value must be greater than or equal to
 0 
 . If you know the semaphore already exists, you may leave this setting blank. If the semaphore already exists and you specify an initial count that differs from the existing initial count, the step reports a run-time error.

Parent topic:

Semaphore Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-options-window.html language=enus -->
## TOPIC 03531: Create Options Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-options-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-options-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Create Options button on the ActiveX/COM Module tab to launch the Create Options window. The Create Options window contains the following options: Create New —Creates a new object and obtains a reference to the object. If the server application is already running, this option may or may no

### Create Options Window

Click the
 Create Options
 button on the
 [ActiveX/COM Module](activex-com-module-tab.html)
 tab to launch the Create Options window.

The Create Options window contains the following options:

- Create New 
 —Creates a new object and obtains a reference to the object. If the server application is already running, this option may or may not launch another copy of the application. The server application decides when to launch a new instance of the application.
- Attach To Active 
 —Obtains a reference to an active Application object. TestStand can obtain an active reference when the ActiveX Automation server registers the object in the Running Object Table (ROT) for the operating system. Typically ActiveX servers register objects as weak references, so when the last reference to the object is released, TestStand might not be able to attach to the active reference. To work around this limitation, ActiveX servers can create a strong reference in the ROT by locking the object. For example, LabWindows/CVI ActiveX servers can use the
 CA_ServerLockActiveObject 
 and
 CA_ServerUnlockActiveObject 
 functions to lock and unlock the object in the ROT.
- Create From File 
 —Loads an existing object from a file and obtains a reference to the object. If the server application is already running, this option may or may not launch another copy of the application. The server application decides when to launch a new instance of the application. When you enable this option, the Edit ActiveX/COM Call dialog box displays a File Selection control and a
 Browse 
 button. You can use these controls to specify the path of the file.
- Remote Host (optional) 
 —The
 remote system 
 where the object is created. This control dims when you select
 Attach to Active 
 .
- Specify Host By Expression 
 —Enable this option to specify that the Remote Host control contains an expression the ActiveX/COM Adapter evaluates at run time to determine the name of the remote host.
- Use Step Load/Unload To Specify Object Creation Time and Lifetime 
 —Controls the lifetime of an object the step creates. When you do not set this option, the step creates the object when the step begins and then releases the internal reference of the step to the object when the step completes. When you enable this option, the step creates the object when the step loads according to the Load option of the step and then holds an internal reference to the object until the step unloads according to the Unload option of the step. This option is dimmed when you enable the Specify Host By Expression control.

#### See Also

[ActiveX/COM Module Tab](activex-com-module-tab.html)

Parent topic:

ActiveX/COM Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-sessions-and-apply-configuration-edit.html language=enus -->
## TOPIC 03532: Create Sessions and Apply Configuration Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-sessions-and-apply-configuration-edit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-sessions-and-apply-configuration-edit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Create Sessions and Apply Configurations edit tab in the TestStand Sequence Editor to create IO sessions associated with the selected IO configuration and then apply the selected configuration on those IO sessions. The Create Sessions and Apply Configuration edit tab contains the following o

### Create Sessions and Apply Configuration Edit Tab

Use the Create Sessions and Apply Configurations edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to create IO sessions associated with the selected IO configuration and then apply the selected configuration on those IO sessions.

The Create Sessions and Apply Configuration edit tab contains the following options:

- Adapter 
 —Specifies the adapter to use to create the IO sessions.
- IO Configuration 
 —The name of the of IO Configuration that defines the names and number of IO sessions created, and that applies to the IO sessions. 
 Use the dropdown menu to select from one of the exported configurations. Selecting an IO configuration automatically creates the TestStand variables required to store the IO sessions for that configuration. This operation also deletes unused IO session variables used by the previous IO Configuration. Click
 Edit IO Configuration 
 to edit the selected IO configuration and view all the IO sessions contained within the configuration. The right pane displays additional information about the selected IO configuration and IO session, including a read-only list of instrument attributes. 
 You can modify settings for each IO session using the following controls:
  - Logical Names 
 —The logical name of the IO session.
 Note 
 The logical names of IO sessions are not editable.
  - Description 
 —The description about the session.
 Note 
 The session description is not editable.
  - Session Variable 
 —The TestStand variable used to store the IO session.

Parent topic:

Create sessions and Apply Configuration Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-sessions-and-apply-configuration-step.html language=enus -->
## TOPIC 03533: Create sessions and Apply Configuration Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-sessions-and-apply-configuration-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-sessions-and-apply-configuration-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Create sessions and Apply Configuration step to create IO sessions associated with the selected IO configuration and then apply the selected configuration on those IO sessions. Configuring the Step Use the Create sessions and Apply Configuration edit tab in the TestStand Sequence Editor and th

### Create sessions and Apply Configuration Step

Use a Create sessions and Apply Configuration step to create IO sessions associated with the selected IO configuration and then apply the selected configuration on those IO sessions.

#### Configuring the Step

Use the
 [Create sessions and Apply Configuration](create-sessions-and-apply-configuration-edit.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Create sessions and Apply Configurations](configure-create-sessions-and-apply-configura.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to create IO sessions associated with the selected IO configuration and then apply the selected configuration on those IO sessions.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Create sessions and Apply Configuration step type defines the following step properties:

- Step.IOConfigurations 
 —Specifies the list of IO sessions to create and the configuration to apply to the sessions.
- Step.StepDescription 
 —Specifies a brief description of the step.
- Step.Adapter 
 —Specifies the adapter to use to create the IO sessions.

Parent topic:

IO Configuration Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-update-custom-data-type-from-cluster-d.html language=enus -->
## TOPIC 03534: Create/Update Custom Data Type from Cluster Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-update-custom-data-type-from-cluster-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-update-custom-data-type-from-cluster-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Create/Update Custom Data Type located next to the parameter in the Type column on the LabVIEW Module / LabVIEW NXG Module tab or in the Edit LabVIEW VI Call / Edit LabVIEW NXG VI Call dialog box to launch the Create/Update Custom Data Type from Cluster dialog box. When you are creating a new

### Create/Update Custom Data Type from Cluster Dialog Box

Click
 Create/Update Custom Data Type
 located next to the parameter in the Type column on the
 [LabVIEW Module](labview-module-tab.html)
 /
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab or in the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 /
 [Edit LabVIEW NXG VI Call](edit-labview-nxg-vi-call-dialog-box.html)
 dialog box to launch the Create/Update Custom Data Type from Cluster dialog box.

When you are creating a new custom data type, the Create/Update Custom Data Type from Cluster dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- List Box 
 —Includes the following information:
  - Cluster Element Label 
 —The name of the element in the LabVIEW/LabVIEW NXG cluster.
  - Property Type 
 —The type associated with the element in the TestStand type. In the case of clusters, which are type definitions, this is the type name. If a cluster element uses a variant data type, use the combo box in this column to select the property for the TestStand type.
  - Property Name 
 —The name associated with the element in the TestStand type. You can customize the property name.
- Create Custom Data Type In File 
 —The location where TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

When you are updating an existing custom data type, the dialog box contains the following options:

- Type Name 
 —The names of the existing custom data types. Select a type to update.
- List Box 
 —Includes the following information:
  - Cluster Element Label 
 —The name of the element in the LabVIEW/LabVIEW NXG cluster.
  - Property Type 
 —The type associated with the element in the TestStand type. In the case of clusters, which are type definitions, this is the type name. If a cluster element uses a variant data type, use the combo box in this column to select the property for the TestStand type.
  - Property Name 
 —The name associated with the element in the TestStand type. You can customize the property name.
  - Update Action 
 —The action to take to update the element in the TestStand type. If the cluster element has been removed, you can ignore the property, remove the mapping from the TestStand type, or remove the element itself.
- Update Custom Data Type In File 
 —The locations of the custom data types to be updated.

Cluster Passing

Type Properties

Note

- This dialog box is available only for cluster and cluster array parameters.
- When you update a strict type definition in LabVIEW/LabVIEW NXG, you must also update all instances of the custom data type you created in TestStand from that LabVIEW/LabVIEW NXG strict type definition. TestStand does not automatically update custom data types with changes you make in LabVIEW/LabVIEW NXG.
- You cannot use the Create/Update Custom Data Type from Cluster dialog box to update an existing custom data type you use in C or .NET steps.

#### See Also

[Cluster Parameters](cluster-parameters-labview-vi-call-parameters.html)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Module Tab](labview-module-tab.html)

[Passing Existing TestStand Container Variables to LabVIEW](/csh?context=ts_tsref_labview_cluster_params_existing)

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-update-custom-data-type-from-cvi-and-c.html language=enus -->
## TOPIC 03535: Create/Update Custom Data Type from CVI and C/C++ Enum Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-update-custom-data-type-from-cvi-and-c.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-update-custom-data-type-from-cvi-and-c.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Create/Update Custom Data Type located next to the parameter in the Description column on the CVI or C/C++ Adapter to launch the Create/Update Custom Data Type from Enum dialog box. The Create/Update Custom Data Type button appears only when the Category is set to Enumeration . When you are cr

### Create/Update Custom Data Type from CVI and C/C++ Enum Dialog Box

Create/Update Custom Data Type

Note

Create/Update Custom Data Type

Category

Enumeration

When you are creating a new custom
 [enumeration data type](/csh?context=ts_tsfundamentals_usingenumerations)
 for an enumerated parameter, the Create tab of the
 [Create/Update Custom Data Type](create-update-custom-data-type-from-cluster-d.html)
 dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- List Box 
 —Includes the following information:
  - Items 
 —Lists the names of the elements in the C/C++ enumerated parameter.
  - Values 
 —Lists the numeric value of each item.
- Create Custom Data Type in File 
 —The file in which TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

When you are updating an existing custom enumeration data type, switch to the Update tab of the dialog box. It contains the following options:

- Select Type 
 —The names of the existing custom enumeration data types. Select a type to update.
- List Box 
 —Includes the following information:
  - Items 
 —Lists the names of the elements in the C/C++ enumerated parameter, as well as the elements in the TestStand enumeration data type. The items that are to be retained in the updated enumeration data type are displayed in black. Those items that are present in the TestStand type but absent in the C/C++ enum will be removed, and are displayed in red and struck out.
  - New Values 
 —Lists the new numeric value of each item that will be present in the updated type.
  - Old Values 
 —Lists the old numeric value of every item which will be retained or removed.

Note

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-update-custom-data-type-from-cvi-struc.html language=enus -->
## TOPIC 03536: Create/Update Custom Data Type from CVI Struct Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-update-custom-data-type-from-cvi-struc.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-update-custom-data-type-from-cvi-struc.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Create/Update Custom Data Type button located next to a parameter in the Type column on the Parameters Table on the LabWindows/CVI Module tab to launch the Create/Update Custom Data Type from Struct dialog box. This dialog box is available only for struct and struct array parameters. Selec

### Create/Update Custom Data Type from CVI Struct Dialog Box

Click the
 Create/Update Custom Data Type
 button located next to a parameter in the Type column on the Parameters Table on the
 [LabWindows/CVI Module](labwindows-cvi-module-tab.html)
 tab to launch the Create/Update Custom Data Type from Struct dialog box. This dialog box is available only for struct and struct array parameters.

Select the Create a New Type radio button to create a new TestStand type. When creating a new custom data type, the Create/Update Custom Data Type from Struct dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- Struct Member List Box 
 —Includes the following information:
  - C Label 
 —The name of the struct member specified in the LabWindows/CVI code module.
  - TestStand Name 
 —The name associated with the field in the TestStand type. You can customize the property name.
  - C Type 
 —The type of the struct member in the LabWindows/CVI code module.
  - TestStand Type 
 —The type associated with the field in the TestStand type.
- Create Custom Data Type In File 
 —The location where TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

Select the Update an Existing Type radio button to update an existing TestStand type. When updating an existing custom data type, the dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- Struct Member List Box 
 —Includes the following information:
  - C Label 
 —The name of the struct member specified in the LabWindows/CVI code module.
  - TestStand Name 
 —The name associated with the field in the TestStand type. You can customize the property name.
  - C Type 
 —The type of the struct member in the LabWindows/CVI code module.
  - TestStand Type 
 —The type associated with the field in the TestStand type.
  - Struct Mapping Action 
 —The action to take to update the field in the TestStand type. If the struct field has been removed, you can delete the property from the TestStand type or exclude it from struct passing.
- Create Custom Data Type In File(s) 
 —The locations of the custom data types to be updated.

#### Struct Import Behavior

Review the following import behaviors when importing structs from LabWindows/CVI.

- LabWindows/CVI enum struct members are mapped to TestStand numbers with 32-bit signed integer struct passing.
- Generally, struct member pointers to numeric types are mapped to TestStand array properties. By default, the array contains a single member. Leave the array length as-is to pass a single value by reference or pass an array of length one. (These two scenarios are equivalent in C.) Change the array length as needed to pass longer arrays. Make the array empty to pass a null pointer.
- Struct member IUnknown pointers, IDispatch pointers, and CAObjHandle are mapped to TestStand object reference types with appropriate struct passing settings. Pointers to void are mapped to TestStand numbers with struct passing settings appropriate to the size of the pointer: 32-bit unsigned integer in 32-bit TestStand and 64-bit unsigned integer in 64-bit TestStand.
- Struct member arrays of char and pointers to char are mapped to TestStand strings. TestStand sets the string buffer size to match the size of embedded character arrays. By default, TestStand sets the string buffer size for non-const string pointers to 1024. You must update this setting as appropriate for the code module.
- The Create Custom Data Type from Struct dialog box does not support struct members that are themselves structs.

#### See Also

[LabWindows/CVI Module Tab](labwindows-cvi-module-tab.html)

[Edit LabWindows/CVI Module Call Dialog Box](edit-labwindows-cvi-module-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-update-custom-data-type-from-cvi-struc_2.html language=enus -->
## TOPIC 03537: Create/Update Custom Data Type from CVI Struct Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-update-custom-data-type-from-cvi-struc_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-update-custom-data-type-from-cvi-struc_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Create/Update Custom Data Type button located next to a parameter in the Type column on the Parameters Table on the LabWindows/CVI Module tab to launch the Create/Update Custom Data Type from Struct dialog box. This dialog box is available only for struct and struct array parameters. Selec

### Create/Update Custom Data Type from CVI Struct Dialog Box

Click the
 Create/Update Custom Data Type
 button located next to a parameter in the Type column on the Parameters Table on the
 [LabWindows/CVI Module](labwindows-cvi-module-tab.html)
 tab to launch the Create/Update Custom Data Type from Struct dialog box. This dialog box is available only for struct and struct array parameters.

Select the Create a New Type radio button to create a new TestStand type. When creating a new custom data type, the Create/Update Custom Data Type from Struct dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- Struct Member List Box 
 —Includes the following information:
  - C Label 
 —The name of the struct member specified in the LabWindows/CVI code module.
  - TestStand Name 
 —The name associated with the field in the TestStand type. You can customize the property name.
  - C Type 
 —The type of the struct member in the LabWindows/CVI code module.
  - TestStand Type 
 —The type associated with the field in the TestStand type.
- Create Custom Data Type In File 
 —The location where TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

Select the Update an Existing Type radio button to update an existing TestStand type. When updating an existing custom data type, the dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- Struct Member List Box 
 —Includes the following information:
  - C Label 
 —The name of the struct member specified in the LabWindows/CVI code module.
  - TestStand Name 
 —The name associated with the field in the TestStand type. You can customize the property name.
  - C Type 
 —The type of the struct member in the LabWindows/CVI code module.
  - TestStand Type 
 —The type associated with the field in the TestStand type.
  - Struct Mapping Action 
 —The action to take to update the field in the TestStand type. If the struct field has been removed, you can delete the property from the TestStand type or exclude it from struct passing.
- Create Custom Data Type In File(s) 
 —The locations of the custom data types to be updated.

#### Struct Import Behavior

Review the following import behaviors when importing structs from LabWindows/CVI.

- LabWindows/CVI enum struct members are mapped to TestStand numbers with 32-bit signed integer struct passing.
- Generally, struct member pointers to numeric types are mapped to TestStand array properties. By default, the array contains a single member. Leave the array length as-is to pass a single value by reference or pass an array of length one. (These two scenarios are equivalent in C.) Change the array length as needed to pass longer arrays. Make the array empty to pass a null pointer.
- Struct member IUnknown pointers, IDispatch pointers, and CAObjHandle are mapped to TestStand object reference types with appropriate struct passing settings. Pointers to void are mapped to TestStand numbers with struct passing settings appropriate to the size of the pointer: 32-bit unsigned integer in 32-bit TestStand and 64-bit unsigned integer in 64-bit TestStand.
- Struct member arrays of char and pointers to char are mapped to TestStand strings. TestStand sets the string buffer size to match the size of embedded character arrays. By default, TestStand sets the string buffer size for non-const string pointers to 1024. You must update this setting as appropriate for the code module.
- The Create Custom Data Type from Struct dialog box does not support struct members that are themselves structs.

#### See Also

[LabWindows/CVI Module Tab](labwindows-cvi-module-tab.html)

[Edit LabWindows/CVI Module Call Dialog Box](edit-labwindows-cvi-module-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-update-custom-data-type-from-labview-e.html language=enus -->
## TOPIC 03538: Create/Update Custom Data Type from LabVIEW Enum Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-update-custom-data-type-from-labview-e.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-update-custom-data-type-from-labview-e.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Create/Update Custom Data Type located next to the parameter in the Type column on the LabVIEW Module tab / LabVIEW NXG Module tab or in the Edit LabVIEW VI Call / Edit LabVIEW NXG VI Call dialog boxes to launch the Create/Update Custom Data Type from Enum dialog box. When you are creating a n

### Create/Update Custom Data Type from LabVIEW Enum Dialog Box

Click
 Create/Update Custom Data Type
 located next to the parameter in the Type column on the
 [LabVIEW Module tab](labview-module-tab.html)
 /
 [LabVIEW NXG Module tab](labview-nxg-module-tab.html)
 or in the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 /
 [Edit LabVIEW NXG VI Call](edit-labview-nxg-vi-call-dialog-box.html)
 dialog boxes to launch the Create/Update Custom Data Type from Enum dialog box.

When you are creating a new custom
 [enumeration data type](/csh?context=ts_tsfundamentals_usingenumerations)
 for a LabVIEW/LabVIEW NXG enumerated parameter, the Create tab of the
 [Create/Update Custom Data Type from Cluster](create-update-custom-data-type-from-cluster-d.html)
 dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- List Box 
 —Includes the following information:
  - Items 
 —Lists the names of the elements in the LabVIEW/LabVIEW NXG enumerated parameter.
  - Values 
 —Lists the numeric value of each item.
- Create Custom Data Type in File 
 —The file in which TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

When you are updating an existing custom enumeration data type, switch to the Update tab of the dialog box. It contains the following options:

- Select Type 
 —The names of the existing custom enumeration data types. Select a type to update.
- List Box 
 —Includes the following information:
  - Items 
 —Lists the names of the elements in the LabVIEW/LabVIEW NXG enumerated parameter, as well as the elements in the TestStand enumeration data type. The items that are to be retained in the updated enumeration data type are displayed in black. Those items that are present in the TestStand type but absent in the LabVIEW/LabVIEW NXG enum will be removed, and are displayed in red and struck out.
  - New Values 
 —Lists the new numeric value of each item that will be present in the updated type.
  - Old Values 
 —Lists the old numeric value of every item which will be retained or removed.

Note

Edit Enumerators

Edit Enumerators

Note

- This dialog box is available only for enumerated LabVIEW/LabVIEW NXG parameters like enums, rings, tab controls, etc. and arrays of such enumerated parameters.
- When you update a strict type definition in LabVIEW/LabVIEW NXG, you must also update all instances of the custom data type you created in TestStand from that LabVIEW/Labview NXG strict type definition. TestStand does not automatically update custom data types with changes you make in LabVIEW/LabVIEW NXG.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-update-custom-data-type-from-net-enum.html language=enus -->
## TOPIC 03539: Create/Update Custom Data Type from .NET Enum Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-update-custom-data-type-from-net-enum.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-update-custom-data-type-from-net-enum.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Create/Update Custom Data Type located next to the parameter in the Description column on the .NET Adapter to launch the Create/Update Custom Data Type from Enum dialog box. When you are creating a new custom enumeration data type for an enumerated parameter, the Create tab of the Create/Updat

### Create/Update Custom Data Type from .NET Enum Dialog Box

Click
 Create/Update Custom Data Type
 located next to the parameter in the Description column on the .NET Adapter to launch the Create/Update Custom Data Type from Enum dialog box.

When you are creating a new custom
 [enumeration data type](/csh?context=ts_tsfundamentals_usingenumerations)
 for an enumerated parameter, the Create tab of the
 [Create/Update Custom Data Type](create-update-custom-data-type-from-cluster-d.html)
 dialog box contains the following options:

- Type Name 
 —The name of the new custom data type.
- List Box 
 —Includes the following information:
  - Items 
 —Lists the names of the elements in the .NET enumerated parameter.
  - Values 
 —Lists the numeric value of each item.
- Create Custom Data Type in File 
 —The file in which TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

When you are updating an existing custom enumeration data type, switch to the Update tab of the dialog box. It contains the following options:

- Select Type 
 —The names of the existing custom enumeration data types. Select a type to update.
- List Box 
 —Includes the following information:
  - Items 
 —Lists the names of the elements in the .NET enumerated parameter, as well as the elements in the TestStand enumeration data type. The items that are to be retained in the updated enumeration data type are displayed in black. Those items that are present in the TestStand type but absent in the .NET enum will be removed, and are displayed in red and struck out.
  - New Values 
 —Lists the new numeric value of each item that will be present in the updated type.
  - Old Values 
 —Lists the old numeric value of every item which will be retained or removed.

Note

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/create-update-custom-data-type-from-python-en.html language=enus -->
## TOPIC 03540: Create/Update Custom Data Type from Python Enum Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/create-update-custom-data-type-from-python-en.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/create-update-custom-data-type-from-python-en.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: On the Module tab for a Python step, click Create/Update Custom Data Type , located next to the parameter in the Type column of the Parameters table, to launch the Create/Update Custom Data Type from Enum dialog box. The Create/Update Custom Data Type button appears only when you set the step or Pyt

### Create/Update Custom Data Type from Python Enum Dialog Box

On the Module tab for a Python step, click
 Create/Update Custom Data Type
 , located next to the parameter in the Type column of the Parameters table, to launch the Create/Update Custom Data Type from Enum dialog box.

The
 Create/Update Custom Data Type
 button appears only when you set the step or Python Adapter to use Python 3 and configure a parameter to use the Enum parameter type.

The dialog box contains the following options:

- Path to Python Module 
 —The relative or absolute path to the Python module containing the enum definition. Click
 Browse 
 to browse for a Python module. Click
 View 
 to open the module in a text editor.
 TestStand uses the Python search paths when attempting to resolve relative paths. TestStand uses the Python version and virtual environment path you specify in the Python Adapter Configuration dialog box to determine the Python search paths unless you specify a version in the step settings.
- Select an enum from Python Module 
 —Displays enums defined in the Python module you specify. Depending on which enum you select, the list box in the Create and Update tabs updates to reflect the key-value pairs for the enum.

When you want to create a new custom enumeration data type for an enumerated parameter, select the
 Create
 tab. It contains the following options:

- Type Name 
 —The name of the new custom data type.
- List Box 
 —Includes the following information:
  - Items 
 —The names of the elements in the Python enum.
  - Values 
 —The numeric value of each item.
- Create Custom Data Type in File 
 —The file in which TestStand creates the new data type. By default, TestStand creates the new data type in the current sequence file.

When you want to update an existing custom enumeration data type, select the
 Update
 tab. It contains the following options:

- Select Type 
 —The names of the existing custom enumeration data types. Select a type to update.
- List Box 
 —Includes the following information:
  - Items 
 —The names of the elements in the Python enum, as well as the elements in the TestStand enumeration data type.
 Black text indicates that the updated enumeration data type will retain the item. Red strikethrough text indicates that the item is present in the TestStand type but absent in the specified Python enum, and updating the enumeration data type removes the item.
  - New Values 
 —The new numeric value of each item the updated type retains.
  - Old Values 
 —The old numeric value of every item the updated type retains or removes.

#### See Also

[Python Adapter Configuration Dialog Box](python-adapter-configuration-dialog-box.html)

[Search Directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)

[Using Enumerations in TestStand](/csh?context=ts_tsfundamentals_usingenumerations)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/creating-a-subsequence-from-selected-steps-se.html language=enus -->
## TOPIC 03541: Creating a Subsequence from Selected Steps - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/creating-a-subsequence-from-selected-steps-se.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/creating-a-subsequence-from-selected-steps-se.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creating a Subsequence from Selected Steps You can create a new subsequence from selected steps in a sequence file. TestStand will replace the steps you select in the parent sequence with a Sequence Call step to call the new subsequence. TestStand will also create variables and update expressions fo

### Creating a Subsequence from Selected Steps - Sequence File Window

#### Creating a Subsequence from Selected Steps

You can create a new subsequence from selected steps in a sequence file. TestStand will
replace the steps you select in the parent sequence with a
 [Sequence Call](sequence-call-step.html)
 step to call the new subsequence.
TestStand will also create variables and update expressions for the new subsequence and will
delete Local variables that are no longer referenced by the remaining steps in the parent
sequence.

Note

Note

In the
 [Steps Pane context menu](steps-pane-context-menu-sequence-file-window.html)
 , select
 New Subsequence from Steps
 . You can choose to
perform the operation
 With Preview
 or
 Without Preview
 . If you choose to preview the
operation, TestStand will launch the Preview dialog box, which contains the following options:

- Sequence Options 
 —The Preview dialog box contains the following sequence options:
  - Subsequence Name 
 —Specifies the name of the subsequence. A default name is
loaded when the dialog box launches.
  - Use Current Sequence File 
 —This option is selected by default. When you select this
option, a new subsequence will be created in the current sequence file. You can
select a different sequence file in which to create the subsequence by unselecting this
option.
  - Sequence File Path 
 —The pathname of the sequence file in which to create the new
subsequence.
  - Delete Locals No Longer Used In Parent Sequence 
 —Deletes Local variables that are
no longer referenced by the remaining steps in the parent sequence. This option is
selected by default.
- Subsequence Options 
 —The Preview dialog box contains the following subsequence options:
 
 Expanding a potential parameter displays auto-resolved references and/or possible
references:
  - Potential Parameters 
 —Lists the potential parameters that will be created in the new
 sequence. A variable is listed as a potential parameter if that variable is referenced
 by the remaining steps in the parent sequence or if that variable belongs to the Parameters variable group in the parent sequence. Unchecking
 Use Current
 Sequence File 
 and selecting a different sequence file path processes the variables in
 the File Globals variable group in the parent sequence and adds them as parameters
 if a variable is used by the selected steps.
  - Original Location 
 —Displays the location of the selected parameter in the parent sequence.
 Note 
 Unchecking a variable in the potential parameter list moves the
variable to the original variable group (original location). If a variable’s
original variable group is Parameters, then unchecking is not allowed for
that variable.
  - Auto-Resolved References 
 —Lists the references that can be resolved to the selected
variable at Edit time. The expressions in the referenced locations are updated to refer
to the selected variable.
  - Possible References 
 —Lists the references that cannot be resolved to the selected
variable at Edit time and can only be resolved during runtime. Expressions in the
Possible References are editable.
  - Selected Reference Expression 
 —Displays the expression in the selected location of
Auto-Resolved or Possible References.

Right-click on an auto-resolved reference or a possible reference to access the context menu. The context menu contains the following options, which are disabled by default:

- Revert 
 —When you edit an expression that is listed as a possible reference, this option is enabled for that reference and any other related reference. Selecting this option reverts the expression to its original state (the state immediately following the creation of the subsequence), regardless of the number of edits you have made.
- Redo 
 —This option is enabled if you choose to revert an edited expression. Selecting this option undoes the revert operation and restores the changes you made to the expression before you reverted to the original.

When you click
 OK
 , TestStand will create a sequence file for the new subsequence and move the steps you selected in the parent sequence into the subsequence. TestStand will also create any necessary variables and update expressions for the new subsequence. A Sequence Call step will be inserted in the parent sequence to call the new subsequence and pass appropriate parameters. If you selected the
 Delete Locals No Longer Used In Parent Sequence
 option, TestStand will delete Local variables in the parent sequence that are no longer referenced by the remaining steps.

Parent topic:

Steps Pane - Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/creating-data-type-instances-from-context-men.html language=enus -->
## TOPIC 03542: Creating Data Type Instances from Context Menus

- bundle_id: `teststand-api-reference`
- source_path: `tsref/creating-data-type-instances-from-context-men.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/creating-data-type-instances-from-context-men.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: With the exception of the Insert User and Insert Group items, all the context menu items in the following table provide a submenu from which you can select the following categories of data types: Simple data types TestStand defines, including the number, string, Boolean, and object reference data ty

### Creating Data Type Instances from Context Menus

With the exception of the Insert User and Insert Group items, all the context menu items in the following table provide a submenu from which you can select the following categories of data types:

- Simple data types TestStand defines, including the number, string, Boolean, and object reference data types.
- Container data types you use for a parameter when you want to pass an object of any type to the sequence, in which case you also must turn off type checking for the parameter.
- Named data types, including all the custom named data types in type palette files or in the files you are currently editing. The submenu also includes
 standard TestStand named data types 
 , such as Error, Path, Expression, and CommonResults.

| Context Menu Item | Location of Context Menu | Item Inserted |
| --- | --- | --- |
| Insert File Global | File Globals section of the Variables pane in the Sequence File window | Sequence file global variable |
| Insert Parameter | Parameters section of the Variables pane in the Sequence File window | Sequence parameter |
| Insert Local | Locals section of the Variables pane in the Sequence File window | Sequence local variable |
| Insert Station Global | Station Globals window | Station global variable |
| Insert User Insert Group | User Manager window | New object with the User data type |
| Insert Field | Variables pane in the Sequence File window, Station Globals window, and Types window | New element in an existing data type |

If the submenu does not contain the data type you require, create the data type in the
 [Types](types-window.html)
 window and then select the new data type from the Type submenu of the Insert context menu. When the data type already exists in another window or pane, copy or drag the data type to a type palette file or to the file you are editing.

To create a parameter with a complex data type, first create the data type in the Types window and then select the complex data type from the
 Insert Parameter»Type
 submenu.

#### See Also

[Types Window](types-window.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/csv-plugins.html language=enus -->
## TOPIC 03543: .CSV Plugins

- bundle_id: `teststand-api-reference`
- source_path: `tsref/csv-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/csv-plugins.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: .CSV Plugins TestStand supports RFC 4180 for representing Comma Delimited Text. CSV is a delimited data format that has fields/columns separated by the comma character and records/rows terminated by new lines. Any field may be optionally enclosed with double-quote characters. However, the following

### .CSV Plugins

#### .CSV Plugins

TestStand supports RFC 4180 for representing Comma Delimited Text. CSV is a delimited
data format that has fields/columns separated by the comma character and records/rows
terminated by new lines.

Any field may be optionally enclosed with double-quote characters. However, the following
fields must be enclosed in double-quote characters:

- Fields with embedded commas or double-quote characters
- Fields with embedded line breaks
- Fields with leading and trailing spaces

Note

See the
 [Property Loader Plugins - File Formats](/csh?context=ts_tsref_propertyloaderplugins_fileformat)
 topic for more information about the required file structure for this plugin.

#### Import Options

This plugin contains the following plugin-specific import options:

Decimal Point
 — Specifies what character should be used for the decimal point. You can
choose one of the following options:

- Use Period — Uses . character for the decimal point
- Use Comma — Uses , character for the decimal point
- Use Station Options — Use the Station Options localization preferences to determine the
decimal point

#### Export Options

This plugin contains the following plugin-specific export options:

Decimal Point
 — Specifies what character should be used for the decimal point. You can
choose one of the following options:

- Use Period — Uses . character for the decimal point
- Use Comma — Uses , character for the decimal point
- Use Station Options — Use the Station Options localization preferences to determine the
decimal point

File Format Type

- Default — Number of columns is not fixed. Ex: All the subproperties of a container will be
specified in one line. The number of columns will grow as the number of subproperties.
- Flattened — Number of columns is fixed. A line will contain the lookup of the property
along with its value.

Optional Information To Export

- Sequence — Add the sequence information containing the sequence name.
- Type — Add the type information containing the type name of the property.
- Category — Add the Category information containing where the property exists. The information is
not mandatory if all the property being exported contains alias names.

Parent topic:

Property Loader Plugins

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/csvfileinputrecordstream-and-csvfileoutputrec.html language=enus -->
## TOPIC 03544: CsvFileInputRecordStream and CsvFileOutputRecordStream

- bundle_id: `teststand-api-reference`
- source_path: `tsref/csvfileinputrecordstream-and-csvfileoutputrec.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/csvfileinputrecordstream-and-csvfileoutputrec.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: CsvFileInputRecordStream and CsvFileOutputRecordStream provide functionality relevant to working with comma separated values files. For example, their methods allow you to open and close the files, specify the separator character, and search for tags that indicate the beginning of the table. In addi

### CsvFileInputRecordStream and CsvFileOutputRecordStream

CsvFileInputRecordStream and CsvFileOutputRecordStream provide functionality relevant to working with comma separated values files. For example, their methods allow you to open and close the files, specify the separator character, and search for tags that indicate the beginning of the table. In addition, they also provide simple methods for reading or writing text without processing it as comma separated values:

- CsvFileInputRecordStream.ReadLine() — Reads one line of text to a string
- CsvFileOutputRecordStream.WriteLine() — Writes one line of text from a string

While the higher-level methods InputRecordStream.ReadRecord() and OutputRecordStream.WriteRecord() operate purely on records, ReadLine() and WriteLine()exploit the fact that a CSV file is actually a text file, allowing for less structured input and output.

Parent topic:

Data Streams API

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/current-sequence-analyzer-project-window.html language=enus -->
## TOPIC 03545: Current Sequence Analyzer Project Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/current-sequence-analyzer-project-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/current-sequence-analyzer-project-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Current Sequence Analyzer Project window to edit and save TestStand Sequence Analyzer projects and to perform analysis in the TestStand Sequence Editor . The sequence editor always has a project open in the background and launches the Current Sequence Analyzer Project window when you click t

### Current Sequence Analyzer Project Window

Use the Current Sequence Analyzer Project window to edit and save
 [TestStand Sequence Analyzer](/csh?context=ts_tsref_sequence_analyzer_overview)
 projects and to perform analysis in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 . The sequence editor always has a project open in the background and launches the Current Sequence Analyzer Project window when you click the
 Current Sequence Analyzer Project
 button on the
 [Sequence Analyzer toolbar](toolbar-buttons-and-shortcuts.html)
 , open an analyzer project, or use the
 [File](file-menu.html)
 menu to create a new analyzer project.

The sequence editor creates a default project (
 MyAnalyzerProject.tsaproj
 ) the first time you launch the sequence analyzer. The sequence editor launches the most recently opened analyzer project file each time you open the Current Sequence Analyzer Project window. Closing the Current Sequence Analyzer Project window does not unload the current analyzer project file from memory.

The Current Sequence Analyzer Project window contains the following panes. Click the corresponding tab located at the bottom of the Current Sequence Analyzer Project window to show each pane.

- Rules 
 —The rules to use for analysis. Use this tab to enable, disable, and configure rules for analysis in the current project, sequence file, or workspace file.
- Options 
 —Contains the project options that control the analysis and determine whether the sequence editor automatically saves the current analyzer project.
- Files 
 —The files and directories to analyze.

Use the
 [Analysis Results](analysis-results-pane.html)
 pane to view and resolve the messages for the most recent analysis of the current project, sequence file, or workspace file. The sequence analyzer overwrites the content of the Analysis Results pane each time you start an analysis session.

#### See Also

[File Menu](file-menu.html)

[Sequence Analyzer Messages Tab Context Menu](messages-tab-context-menu-teststand-sequence.html)

[TestStand Sequence Analyzer](/csh?context=ts_tsref_sequence_analyzer_overview)

[Toolbar Buttons and Shortcuts](toolbar-buttons-and-shortcuts.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/custom-commands-dialog-box.html language=enus -->
## TOPIC 03546: Custom Commands Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/custom-commands-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/custom-commands-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the TestStand Deployment Utility and click Custom Commands on the Installer Options tab to launch the Custom Commands dialog box. The options in this dialog box apply only to the type of deployment you create. Changing the type of deployment might change the options available in this dialog b

### Custom Commands Dialog Box

TestStand Deployment Utility

Custom Commands

Installer Options

Note

type of deployment

The Custom Commands dialog box contains the following options:

- Command List 
 —The current list of custom commands the installer will execute.
- Add 
 —Adds a new command to the Command List by duplicating the selected command in the list.
- Delete 
 —Deletes the selected command in the Command List.
- Move Up 
 —Moves the selected command up in the Command List.
- Move Down 
 —Moves the selected command down in the Command List.
- Command Directory 
 —The directory where the command is located for the selected command in the Command List.
- Command and Arguments 
 —The command and the command-line arguments for the selected command in the Command List. You can use the following case-insensitive directory macros in the command to avoid using fixed paths when you specify the command or the command arguments on different computers:
 Note 
 When you deploy on Windows 10/8.1/7, the name of the
 <
 user
 >
 subdirectory depends on the user account you use to elevate to administrator privileges. 
 Note 
 To execute command-line commands, a custom command must invoke the
 cmd.exe
 executable to execute the command. For example, to execute the
 del
 command, use the custom command
 cmd /c del
 <FilePath>
 . Command-line commands which call an executable in the system directory, such as
 xcopy
 , can be executed directly or through
 cmd.exe
 . 
 Macro
 Directory
 Example
 <ALLUSERSPROFILE>
 Profile directory for all users.
 (Windows 10/8.1/7)
 C:\ProgramData
 <DESKTOPDIR>
 Directory for the desktop of the current user.
 (Windows 10/8.1/7)
 C:\Users\<
 user
 >\Desktop
 <INSTALLATIONDIR>
 Destination directory the user selects in the installer.
 Note 
 Not all installers use this macro.
 C:\<Program Files>\Company Name\Project Name
 <INSTALLERDIR>
 Directory where the installer was started.
 D:\<Program Files>\<
 My Application
 >
 <NIDIR>
 Directory where National Instruments products reside. (64-bit TestStand) Refers to the 64-bit directory for deployments you build with the 64-bit TestStand deployment utility.
 C:\<Program Files>\National Instruments
 <PROGRAMFILES>
 System program files directory. (64-bit TestStand) Refers to the 64-bit directory for deployments you build with the 64-bit TestStand deployment utility.
 C:\<Program Files>
 <PROGRAMMENU>
 Directory where the Start menu entries reside.
 (Windows 10/8.1/7)
 C:\ProgramData\Microsoft\Windows\Start Menu\Programs
 <STARTUPDIR>
 Directory where the Startup menu entries reside.
 (Windows 10/8.1/7)
 C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
 <SYSTEMDRIVE>
 Disk where Microsoft Windows is installed.
 C:\
 <SysWOW64>
 Directory for 32-bit operating system DLLs on 64-bit Windows.
 Note 
 Applies only to 64-bit installers.
 C:\Windows\SysWOW64
 <TEMP>
 Temporary directory the
 GetTempPath
 Windows API function returns. Refer to Microsoft MSDN documentation for more information about the
 GetTempPath
 function.
 (Windows 10/8.1/7)
 C:\Users\<user>\AppData\Local\Temp
 <TESTSTAND>
 TestStand directory for the version that created the installer. (64-bit TestStand) Refers to the 64-bit directory for deployments you build with the 64-bit TestStand deployment utility.
 C:\<Program Files>\National Instruments\<TestStand>
 <TSAPPDATA>
 Directory that contains configuration files users generally do not edit but a program can edit. (64-bit TestStand) Refers to the 64-bit directory for deployments you build with the 64-bit TestStand deployment utility.
 (Windows 10/8.1/7)
 C:\ProgramData\National Instruments\<TestStand>
 <TSPUBLIC>
 Directory that contains user modifications and customizations. (64-bit TestStand) Refers to the 64-bit directory for deployments you build with the 64-bit TestStand deployment utility.
 (Windows 10/8.1/7)
 C:\Users\Public\Documents\National Instruments\<TestStand>
 <USERPROFILE>
 Profile directory for the current user.
 (Windows 10/8.1/7)
 C:\Users\<user>
 <WINDIR>
 Windows
 directory.
 C:\Windows
 <WINSYSTEM>
 Windows
 System
 directory.
 C:\Windows\System
 <WINSYSTEM32>
 Windows
 System32
 directory.
 C:\Windows\System32
- Request Reboot After All Commands Execute 
 —When you enable this option, the installer prompts the user to reboot after all custom commands execute, such as when National Instruments or third-party installers require the computer to reboot.
- Show Commands Progress Window 
 —When you enable this option, the installer opens a window that displays the currently executing custom command and previous command results. Use this option to troubleshoot the custom commands.
- Skip Custom Commands When Installing Silently 
 —When you enable this option, the installer does not execute custom commands when you run the installer executable with the
 /q 
 command-line argument to run the installer in silent mode. Use this option to skip custom commands that require user interaction.

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

[TestStand Deployment Utility](teststand-deployment-utility.html)

[TestStand Directories](/csh?context=ts_tsfundamentals_directories)

[Using Custom Commands to Execute Third-Party Installers](/csh?context=ts_tsdeploysystem_customcommands)

Parent topic:

Installer Options Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/customize-tools-menu-dialog-box.html language=enus -->
## TOPIC 03547: Customize Tools Menu Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/customize-tools-menu-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/customize-tools-menu-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Tools»Customize to launch the Customize Tools Menu dialog box. The Customize Tools Menu dialog box contains the following options: Tools Menu —A list of tools menu items. When you select an item in the list control, all other controls below the list display the settings for the selected item.

### Customize Tools Menu Dialog Box

Select
 Tools»Customize
 to launch the Customize Tools Menu dialog box.

The Customize Tools Menu dialog box contains the following options:

- Tools Menu 
 —A list of tools menu items. When you select an item in the list control, all other controls below the list display the settings for the selected item. The list control displays the following columns:
  - Item Text 
 —The result of evaluating the Item Text Expression.
  - Type 
 —The type of menu item, such as command, sequence, submenu, and sequence file.
- Add 
 —Inserts a new menu item above the selected item in the Tools menu list by launching the
 Add Tools Menu Item 
 dialog box. You can add the following types of menu items:
  - Command 
 —Invokes a Microsoft Windows executable.
  - Sequence 
 —Initiates an execution on a sequence in a sequence file. TestStand does not pre-load code modules for tool menu sequences. Steps that a sequence executes are loaded dynamically regardless of the load options specified by the sequence file and the step settings.
  - Submenu 
 —Additional menu items.
  - Sequence File 
 —Creates a submenu that lists all sequences in a sequence file as menu items. TestStand does not pre-load code modules for tool menu sequences. Steps that a sequence executes are loaded dynamically regardless of the load options specified by the sequence file and the step settings.
- Remove 
 —Deletes the selected menu item from the Tools menu.
- Move Up 
 —Moves the item up within the menu or submenus.
- Move Down 
 —Moves the item down within the menu or submenus.
- Expand 
 —Displays the tools menu items in a submenu.
- Collapse 
 —Steps out of an item in a submenu.
- Item Text Expression 
 —The expression that evaluates to the literal text to display for the tools menu item.
- Insert Separator Before Item 
 —When you enable this option, a menu separator precedes the tools menu item.
- Hidden Expression 
 —An expression that determines when a tools menu item is not visible. If the field is empty, TestStand treats the expression as
 False 
 .
 Note 
 TestStand evaluates the Hidden Expression in the
 [Engine.GetRunTimeToolMenuItems](../tsapiref/engine-getruntimetoolmenuitems.html)
 method. The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 constructs the Tools menu by calling this method each time you select the Tools menu in the sequence editor.
- Enable Expression 
 —Visible for Command and Sequence item types. This option lets you specify an expression that determines when the menu item is enabled. The expression must return
 True 
 to enable the menu item and
 False 
 to dim the menu item.
- Command 
 —The executable path. This option is only visible for the Command menu type.
- Arguments 
 —The command-line arguments. This option is only visible for the Command menu type.
- Use Arguments Expression 
 —If checked, the arguments field is a TestStand expression. If unchecked, the field is a string.
 Note 
 You may need to use the Arguments Expression to pass the current environment to the executable being launched.
- Initial Directory 
 —The initial working directory for the executable. This option is only visible for the Command menu type.
- Edits Selected File 
 —Visible for Sequence and Sequence File item types. Set this option for Tools menu items you add that edit the selected sequence file. This option advises the sequence editor to prompt the user to check out the selected file from source control if it is not already checked out.
- Sequence File 
 and
 Sequence 
 —The target for the Sequence File and Sequence menu item types.
- Restore Defaults 
 —Deletes existing items from all menus and submenus and loads the factory defaults.
- Export Items To File 
 —Launches the
 Export Tools Menu 
 dialog box, which contains a list of tools menu items.

#### See Also

[Add Tools Menu Item dialog box](add-tools-menu-item-dialog-box.html)

[Engine.GetRunTimeToolMenuItems](../tsapiref/engine-getruntimetoolmenuitems.html)

[Export Tools Menu dialog box](export-tools-menu-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/cvi-source-code-files-window.html language=enus -->
## TOPIC 03548: CVI Source Code Files Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/cvi-source-code-files-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/cvi-source-code-files-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Source Code Files button on the LabWindows/CVI Module tab to launch the CVI Source Code Files window. The LabWindows/CVI Source Code Files window contains the following options: Source File that Contains Function —The pathname of the source file. When you want to create a new source file,

### CVI Source Code Files Window

Click the
 Source Code Files
 button on the
 [LabWindows/CVI Module](labwindows-cvi-module-tab.html)
 tab to launch the CVI Source Code Files window.

The LabWindows/CVI Source Code Files window contains the following options:

- Source File that Contains Function 
 —The
 pathname 
 of the source file. When you want to create a new source file, you must enter an absolute pathname. When you are using an existing source file, you can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directories.
- CVI Project File to Open 
 —The pathname of the LabWindows/CVI project file. When the
 code module 
 is a DLL or static library, you must enter the name of the LabWindows/CVI project used to create the DLL or static library file. When the code module is an object module, you can also specify a project.If LabWindows/CVI 2019 or later is the active LabWindows/CVI installation, then the Module on the LabWindows/CVI Module Tab updates to the
 .dll 
 that the LabWindows/CVI project builds. If all the build configurations in the LabWindows/CVI project do not create the same
 .dll 
 file path, a dialog appears, and you can choose which
 .dll 
 to use as the Module path.

#### See Also

[LabWindows/CVI Module](labwindows-cvi-module-tab.html)
 tab

Parent topic:

LabWindows/CVI Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-grid.html language=enus -->
## TOPIC 03549: Data Grid

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-grid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-grid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many tabs and panes in the Database Viewer display database tables in a data grid. In the data grid, you can choose between the Grid, Card, and Layout views. Grid View The Grid View displays records in a tabular form and is the only view in which you can edit data. You can customize the grid in the

### Data Grid

Many tabs and panes in the Database Viewer display database tables in a data grid. In the data grid, you can choose between the Grid, Card, and Layout views.

#### Grid View

The Grid View displays records in a tabular form and is the only view in which you can edit data. You can customize the grid in the following ways:

- Customize columns to display 
 by right-clicking the column header and selecting one of the following options from the context menu:
  - Remove a column from the display.
  - Launch the Column Chooser window, into which you can drag and drop columns. Any columns that are placed in the Column Chooser window are removed from active display. You can drag a column back from the window to restore it in the grid view.
  - Resize the columns displayed by choosing the
 Best Fit 
 option.
- Group columns by value 
 by dragging a column into the GroupBy box. You can group by more than one column to establish a hierarchy. Drag the columns back onto the grid to undo the grouping or right-click in the GroupBy box and choose
 Clear Grouping 
 to undo all groupings.
- Filter columns by value 
 by hovering over a column header to activate a small arrow-shaped filter button that you can click to display a drop-down menu of all unique values in that column. Select a value to filter the column to show only the rows that contain the value you select. Select
 Custom 
 from the drop-down menu to launch the Custom AutoFilter dialog box, in which you can configure a custom filter condition for the column.

The Grid View also contains the following options:

- Show Find Panel 
 —Displays the
 Find 
 panel. You can also perform this command using the <Ctrl+F> keyboard shortcut.
- Show Filter Editor 
 —Launches the
 Filter Editor 
 dialog box.
- Show Auto-Filter Row 
 —Creates an auto-filter row at the top of the grid. You can enter values for each column in the auto-filter row, and the actual data (rows) displayed will be filtered based on these values.

#### Specifying null as the Value for a Column that Accepts null

You can modify the existing value of a cell to null or specify a null value in a new record by pressing <Ctrl+Delete> in that cell. Entering an empty string to specify null might result in a data type mismatch error for most column data types.

#### Card View

Card View represents records as cards consisting of fields (each column in the database table maps to one field) that are always arranged one below the other. The number of cards displayed at a time depends on the available space.

You can customize the card view by clicking on the
 Customize
 button, which displays a drop-down menu that lists all field names in the view. You can perform the following operations in the menu:

- Remove columns from view 
 by clicking on the tick mark next to a column.
- Filter cards by value 
 by clicking on the
 Filter 
 option next to each column that displays a drop-down menu of all unique values in the column. Choose one of these values to filter the column data such that the view displays only those cards that contain the selected value. Choose the
 Custom 
 option from the drop-down menu to launch the Custom AutoFilter dialog box.
 Note 
 Setting any filtering on the view will display the
 [Filter Expression](filter-expression-panel.html)
 panel at the bottom of the view.
 Using the keyboard shortcut <Ctrl+F> displays the Find Panel.

#### Layout View

Layout View displays records as cards, similar to Card View, but you can customize the layout of the cards in the following ways:

- Modify the number of cards displayed at a time 
 using the One Card, One Row, One Column, Multiple Rows, Multiple Columns and Carousel Mode buttons in the header panel.
- Hover over a column or field in a card 
 , which brings up the following controls:
  - Filter 
 —Displays a drop-down menu that lists all unique values in the column. Choose one of these values to display only those cards whose column matches the selected value. You can also choose the
 Custom 
 option from the drop-down menu, which will launch the Custom AutoFilter dialog box.
  - Sort 
 —Sorts the cards based on the values in that column or field.
 Note 
 Setting any filtering on the Layout View will display the
 [Filter Expression](filter-expression-panel.html)
 panel at the bottom of the view.
- Click the Customization button 
 , which launches the Layout View Customization dialog box. This dialog box allows you to customize the layout of the cards at run-time, which is the main difference between Card View and Layout View.
 Note 
 Using the keyboard shortcut <Ctrl+F> displays the Find Panel.
 The panning feature makes it easy to scroll through cards that are only partially visible in the data grid. Click the
 Panning
 button in the header panel to activate the panning feature. The mouse cursor will appear as a hand. You can scroll through the view by clicking and dragging.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-link-properties-dialog-box.html language=enus -->
## TOPIC 03550: Data Link Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-link-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-link-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or edit a connection string for a data link to launch the Data Link Properties dialog box, in which you can specify initialization properties for the OLE DB provider. The Data Link Properties dialog box contains the following tabs: Provider —Select the appropriate OLE DB provider for the type

### Data Link Properties Dialog Box

Create or edit a connection string for a data link to launch the Data Link Properties dialog box, in which you can specify initialization properties for the OLE DB provider.

The Data Link Properties dialog box contains the following tabs:

- Provider 
 —Select the appropriate OLE DB provider for the type of data you want to access.
- Connection 
 —Specifies how to connect to the data using the selected OLE DB provider.
- Advanced 
 —View and set other initialization properties for the data.
- All 
 —View and edit all initialization properties selected for the OLE DB provider.

Note

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-link-properties-dialog-box2.html language=enus -->
## TOPIC 03551: Data Link Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-link-properties-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-link-properties-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: All Tab The available properties vary depending on the OLE DB provider you select. The Property listbox displays all of the initialization properties for the type of data you have selected. To edit a value, select it and click Edit Value to launch the Edit Property Value dialog box. Click Help to la

### Data Link Properties Dialog Box

#### All Tab

The available properties vary depending on the OLE DB provider you select.

The Property listbox displays all of the initialization properties for the type of data you have selected. To edit a value, select it and click
 Edit Value
 to launch the
 [Edit Property Value](edit-property-value-dialog-box.html)
 dialog box.

Click
 Help
 to launch the Microsoft online help for this tab.

#### See Also

[Edit Property Value dialog box](edit-property-value-dialog-box.html)

Parent topic:

Data Link Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-link-tab-edit-open-database-dialog-box.html language=enus -->
## TOPIC 03552: Data Link Tab - Edit Open Database Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-link-tab-edit-open-database-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-link-tab-edit-open-database-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data Link Tab The Data Link tab specifies the information TestStand requires to connect to a database. The Data Link tab contains the following options: Select Data Link —Launches the Select Data Link dialog box. When you select a predefined data link from the list, TestStand updates the Connection

### Data Link Tab - Edit Open Database Dialog Box

#### Data Link Tab

The Data Link tab specifies the information TestStand requires to connect to a database. The Data Link tab contains the following options:

- Select Data Link 
 —Launches the
 Select Data Link 
 dialog box. When you select a predefined data link from the list, TestStand updates the Connection String control on the Data Link tab with the value of the data link.
- Database Handle (Number) 
 —The name of a Number variable or property to which the value of the database is assigned. You must release this handle by calling a Close Database step and using this handle value as the handle to close. Click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box.
- Connection String 
 —The connection string TestStand uses to open the data source. The Connection String control requires a string expression TestStand evaluates at run time. The expression can be a literal value or a string you build using variables or properties. When the value is a literal string, you must encapsulate the string value with quotes (
 "" 
 ).
 Note 
 Refer to the documentation for the database you use to determine whether and how you can communicate to the database securely. National Instruments recommends that you do not use a plain text password to connect to databases with sensitive information. 
 You can update the contents of the Connection String control as follows:
  - Expression Browse 
 —Launches an
 Expression Browser 
 dialog box, in which you can edit a connection string expression.
  - Find File 
 —Selects a Microsoft Data Link (
 .udl 
 ) filename as the connection string. When you select a Data Link file, TestStand updates the Connection String control with the name of the file, as in the following example:
 "FILE NAME=C:\\Program Files\\Common Files\\System\\OLE DB\\Data Links\\Access.udl"
  - View 
 —Launches the
 Database Viewer application 
 and opens the connection string within the viewer.
  - Build 
 —Constructs a connection string using the
 Data Link Properties 
 dialog box.

#### See Also

[Data Link Properties dialog box](data-link-properties-dialog-box.html)

[Database Known Issues](/csh?context=ts_tsfundamentals_database_known_issues)

[Database Logging](/csh?context=ts_tsfundamentals_database_connectivity)

[Database Viewer Application](database-viewer-application.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Select Data Link dialog box](select-data-link-dialog-box.html)

Parent topic:

Edit Open Database Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-operation-step.html language=enus -->
## TOPIC 03553: Data Operation Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-operation-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-operation-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Data Operation step to perform operations on an SQL statement you open with an Open SQL Statement step. Use the Data Operation step to fetch new records, retrieve values from a record, modify existing records, create new records, and delete records. For SQL statements that require parameters,

### Data Operation Step

Use a Data Operation step to perform operations on an SQL statement you open with an
 [Open SQL Statement](open-sql-statement-step.html)
 step. Use the Data Operation step to fetch new records, retrieve values from a record, modify existing records, create new records, and delete records. For SQL statements that require parameters, you can create parameters and specify input values, execute statements, close statements, and fetch output parameter values.

You cannot encapsulate data operations within a transaction because the current Database step types do not support transactions.

#### Configuring the Step

Use the
 [Edit Data Operation](edit-data-operation-dialog-box.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Data Operation step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Data Operation step type defines the following step properties:

- Step.StatementHandle 
 —A string expression that contains the name of the SQL statement on which to operate.
- Step.RecordToOperateOn 
 —The record on which to operate. Valid values are
 0 
 = New,
 1 
 = Current,
 2 
 = Next,
 3 
 = Previous, and
 4 
 = Index.
- Step.RecordIndex 
 —The index of the record on which to operate when you set the
 Step.RecordToOperateOn 
 property to fetch a specific index.
- Step.Operation 
 —The operation to perform on the record. Valid values are
 0 
 = Fetch only,
 1 
 = Set,
 2 
 = Get,
 3 
 = Put,
 4 
 = Delete,
 5 
 = Set and Put,
 6 
 = Execute, and
 7 
 = Close.
- Step.ColumnListSource 
 —The name of the DatabaseColumnValue array variable or property that stores the column-to-variable or column-to-property mappings. By default, the value is
 Step.ColumnList 
 .
- Step.ColumnList 
 —The column-to-variable or column-to-property mapping to perform on a Get or Set operation. The property must be an array of DatabaseColumnValue custom data types, which contain the following subproperties:
  - ColumnName 
 —The name or number of the column from which to obtain a value or to assign a value to.
  - Data 
 —Specifies the variable or property to which TestStand assigns the column value or the expression TestStand evaluates and assigns to the column.
  - FormatString 
 —An optional
 format string 
 for dates, times, and currencies. Use the empty string ("") to use the default format.
  - WriteNull 
 —Specifies whether TestStand writes
 NULL 
 to the column instead of the value in the Data expression property.
  - Status 
 —The error code TestStand returns for the Get or Set operation.
  - Direction 
 —An enumerated value that specifies the parameter direction as
 In 
 ,
 Out 
 ,
 In/Out 
 , or
 Return 
 .
  - Type 
 —An enumerated value that specifies the parameter value as
 String 
 ,
 Number 
 ,
 Boolean 
 , or
 Date/Time 
 .
  - Size 
 —The maximum size of a string parameter.
- Step.SQLStatement 
 —The SQL statement the
 Edit Data Operation 
 dialog box uses to populate the ring controls that contain column names.

#### See Also

[Database Step Types](database-step-types.html)

Parent topic:

Database Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-source-edit-tab.html language=enus -->
## TOPIC 03554: Data Source Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-source-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-source-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Data Source edit tab of the Pass/Fail Test step in the TestStand Sequence Editor to specify the data source for the Boolean value the Pass/Fail Test step uses to determine whether the step passes. The Data Source edit tab contains the following option: Data Source Expression —A Boolean expre

### Data Source Edit Tab

Use the Data Source edit tab of the Pass/Fail Test step in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify the data source for the Boolean value the Pass/Fail Test step uses to determine whether the step passes.

The Data Source edit tab contains the following option:

- Data Source Expression 
 —A Boolean expression the step uses to determine whether the step passes or fails. By default the step specifies the
 Step.Result.PassFail 
 property. You can customize this expression when you do not want to set the value of
 Step.Result.PassFail 
 in the
 code module 
 . For example, you can set the data source expression to refer to multiple variables and properties such as:
 RunState.PreviousStep.Result.Numeric * Locals.Attenuation > 12 
 .

#### See Also

[Test Step Types](test-step-types.html)

Parent topic:

Pass/Fail Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-source-tab-edit-multiple-numeric-limit-t.html language=enus -->
## TOPIC 03555: Data Source Tab - Edit Multiple Numeric Limit Test Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-source-tab-edit-multiple-numeric-limit-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-source-tab-edit-multiple-numeric-limit-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data Source Tab Use the Data Source tab to specify the data source for each measurement you configure. By default, the data source is the numeric array property Step.NumericArray . The code module the step calls can return multiple measurement values in one operation by setting the value of the Step

### Data Source Tab - Edit Multiple Numeric Limit Test Dialog Box

#### Data Source Tab

Use the Data Source tab to specify the data source for each measurement you configure. By default, the data source is the numeric array property
 Step.NumericArray
 . The
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 the step calls can return multiple measurement values in one operation by setting the value of the
 Step.NumericArray
 property. You can also specify an alternate numeric array from which the step obtains measurement values.

The Data Source tab contains the following options:

- Data Source Array Expression 
 —The data source for the selected measurement. For each measurement, you typically specify values or combinations of values you already store in variable or property values.
- Specify a Data Source for Each Measurement 
 —When you enable this option, the Data Source tab displays a list of measurements and the Data Source Array Expression control is dimmed.
- Measurement Table 
 —Lists the properties the step uses for each measurement when you enable the Specify a Data Source for each Measurement control.
- Reset All Data Sources to Default 
 —Resets the expression in the Data Source Expression control and the list of measurements in the Measurement Table to the default settings if you made changes to these options. The Reset All Data Sources to Default option is available only when you enable the Specify a Data Source for Each Measurement option.
- Data Source Array Options 
 —This section contains the following options:
  - If More Data Than Measurements 
 —If there is more data than measurements, you can choose from one of the following options:
    - Repeat One Measurement 
 —When you enable this option, the Repeat This Measurement control contains the list of measurements defined on the Limits tab. When you select one of these measurements, it is applied to the data that remains after the other measurements have been applied. For example, when three measurements (Meas 0, Meas 1, and Meas 2) exist, the data array contains six elements, and you select Meas 1 to repeat, the step compares the data to the limits using the following mode:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Meas[1]
 Data [4]
 ----------
 Meas[1]
 Data [5]
 ----------
 Meas[1]
    - Repeat Measurement Set 
 —Measurements are repeated as a set over the extra data. If the set does not fit evenly, the number of data elements is not a multiple of the number of measurements and the remaining measurements are not used. The step compares data and measurements using the following mode:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Meas[0]
 Data [4]
 ----------
 Meas[1]
 Data [5]
 ----------
 Meas[2] 
 If 8 data elements exist, the step compares them as follows: 
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Meas[0]
 Data [4]
 ----------
 Meas[1]
 Data [5]
 ----------
 Meas[2]
 Data [6]
 ----------
 Meas[0]
 Data [7]
 ----------
 Meas[1]
    - Run-time Error 
 —If there are more data elements than measurements, TestStand generates an error. This mode forces data and measurements to be exactly the same size.
    - Ignore Extra Data 
 —TestStand ignores any extra data. This was the default behavior in TestStand 2.0 and the default mode for this step type. The step compares data and measurements using the following mode:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Ignored
 Data [4]
 ----------
 Ignored
 Data [5]
 ----------
 Ignored
  - Repeat This Measurement 
 —TestStand repeats this measurement when you select
 Repeat One Measurement 
 in the
 If More Data Than Measurement 
 control.
  - If More Measurements Than Data 
 —If you have more measurements than data array elements, you can choose one of the following options:
    - Run-time Error 
 —TestStand always generates an error when you have more measurements than data.
    - Ignore Extra Measurements 
 —TestStand ignores any extra measurements. TestStand compares data and measurements using the following mode:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Ignored
 ----------
 Meas[3]
 Ignored
 ----------
 Meas[4]
 Ignored
 ----------
 Meas[5]

Parent topic:

Edit Multiple Numeric Limit Test Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-source-tab-edit-numeric-limit-test-dialo.html language=enus -->
## TOPIC 03556: Data Source Tab - Edit Numeric Limit Test Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-source-tab-edit-numeric-limit-test-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-source-tab-edit-numeric-limit-test-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data Source Tab Use the drop-down ring control to the right of the Data Source Expression control to quickly select measurement values in local variables or properties of previous steps.

### Data Source Tab - Edit Numeric Limit Test Dialog Box

#### Data Source Tab

Use the drop-down ring control to the right of the Data Source Expression control to quickly select measurement values in local variables or properties of previous steps.

Parent topic:

Edit Numeric Limit Test Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-source-tab-edit-string-value-dialog-box.html language=enus -->
## TOPIC 03557: Data Source Tab - Edit String Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-source-tab-edit-string-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-source-tab-edit-string-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data Source Tab The Data Source tab specifies a data source expression TestStand evaluates to obtain the string it compares against the expected string.

### Data Source Tab - Edit String Value Dialog Box

#### Data Source Tab

The Data Source tab specifies a data source expression TestStand evaluates to obtain the string it compares against the expected string.

Parent topic:

Edit String Value Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-source-tab-multiple-numeric-limit-test-e.html language=enus -->
## TOPIC 03558: Data Source Tab - Multiple Numeric Limit Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-source-tab-multiple-numeric-limit-test-e.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-source-tab-multiple-numeric-limit-test-e.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data Source Tab Use the Data Source tab to specify the data source for each measurement you configure. By default, the data source is the numeric array property Step.NumericArray . The code module the step calls can return multiple measurement values in one operation by setting the value of the Step

### Data Source Tab - Multiple Numeric Limit Test Edit Tabs

#### Data Source Tab

Use the Data Source tab to specify the data source for each measurement you configure. By default, the data source is the numeric array property
 Step.NumericArray
 . The
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 the step calls can return multiple measurement values in one operation by setting the value of the
 Step.NumericArray
 property. You can also specify an alternate numeric array from which the step obtains measurement values.

The Data Source tab of the Multiple Numeric Limit Test edit pane contains the following options:

- Data Source Expression 
 —A numeric array expression the step uses as the measurement values when performing the limit tests. You can customize this expression when you do not want to set the value of
 Step.NumericArray 
 . For example, you can set the data source expression to refer to variables and properties such as,
 Locals.MyLocalArray 
 .
- Specify Data Source for Each Measurement 
 —When you enable this option, the Data Source tab displays a list of measurements and the Data Source Expression control is dimmed.
- Measurement Table 
 —Lists the properties the step uses for each measurement when you enable the Specify Data Source for Each Measurement control.
- Reset All Data Sources to Default 
 —Resets the expression in the Data Source Expression control and the list of measurements in the Measurement Table to the default settings if you made changes to these options. The Reset All Data Sources to Default option is available only when you enable the Specify Data Source for Each Measurement option.
- Data Source Array Options 
 —This section contains the following options:
  - If More Data Than Measurements 
 —If more data than measurements exists, you can choose from one of the following options:
    - Repeat One Measurement 
 —When you enable this option, the Repeat This Measurement control contains the list of measurements defined on the Limits tab. When you select one of these measurements, it is applied to the data that remains after the other measurements have been applied. For example, when three measurements (Meas 0, Meas 1, and Meas 2) exist, the data array contains six elements, and you select Meas 1 to repeat, TestStand uses the following mode to compare the data to the limits:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Meas[1]
 Data [4]
 ----------
 Meas[1]
 Data [5]
 ----------
 Meas[1]
    - Repeat Measurement Set 
 —Measurements are repeated as a set over the extra data. If the set does not fit evenly, the number of data elements is not a multiple of the number of measurements, and the remaining measurements are not used. The step compares data and measurements using the following mode:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Meas[0]
 Data [4]
 ----------
 Meas[1]
 Data [5]
 ----------
 Meas[2] 
 If 8 data elements exist, the step compares them using the following mode: 
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Meas[0]
 Data [4]
 ----------
 Meas[1]
 Data [5]
 ----------
 Meas[2]
 Data [6]
 ----------
 Meas[0]
 Data [7]
 ----------
 Meas[1]
    - Run-time Error 
 —If you have more data elements than measurements, TestStand returns an error. This mode forces data and measurements to be exactly the same size.
    - Ignore Extra Data 
 —TestStand ignores any extra data. This was the default behavior in TestStand 2.0 and is the default mode for this step type. The step compares data and measurements using the following mode:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Data [3]
 ----------
 Ignored
 Data [4]
 ----------
 Ignored
 Data [5]
 ----------
 Ignored
  - Repeat This Measurement 
 —TestStand repeats this measurement when you select
 Repeat One Measurement 
 in the
 If More Data Than Measurement 
 control.
  - If More Measurements Than Data 
 —If you have more measurements than data array elements, you can choose one of the following options:
    - Run-time Error 
 —TestStand always generates an error if you have more measurements than data.
    - Ignore Extra Measurement 
 —Measurement -- TestStand ignores any extra measurements. TestStand compares data and measurements using the following mode:
 Data [0]
 ----------
 Meas[0]
 Data [1]
 ----------
 Meas[1]
 Data [2]
 ----------
 Meas[2]
 Ignored
 ----------
 Meas[3]
 Ignored
 ----------
 Meas[4]
 Ignored
 ----------
 Meas[5]

Parent topic:

Multiple Numeric Limit Test Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-source-tab-numeric-limit-test-edit-tabs.html language=enus -->
## TOPIC 03559: Data Source Tab - Numeric Limit Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-source-tab-numeric-limit-test-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-source-tab-numeric-limit-test-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data Source Tab The Data Source tab of the Numeric Limit Test contains the following option: Data Source Expression —A numeric expression the step uses as the measurement value when performing the limit test. By default the step specifies the Step.Result.Numeric property. You can customize this expr

### Data Source Tab - Numeric Limit Test Edit Tabs

#### Data Source Tab

The Data Source tab of the Numeric Limit Test contains the following option:

- Data Source Expression 
 —A numeric expression the step uses as the measurement value when performing the limit test. By default the step specifies the
 Step.Result.Numeric 
 property. You can customize this expression when you do not want to set the value of
 Step.Result.Numeric 
 in the
 code module 
 . For example, you can set the data source expression to refer to multiple variables and properties such as:
 RunState.PreviousStep.Result.Numeric * Locals.Attenuation.

Parent topic:

Numeric Limit Test Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-source-tab-string-value-test-edit-tabs.html language=enus -->
## TOPIC 03560: Data Source Tab - String Value Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-source-tab-string-value-test-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-source-tab-string-value-test-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data Source Tab The Data Source tab of the String Value Test contains the following option: Data Source Expression —A string expression the step uses to compare against the expected value. The default value is Step.Result.String property. You can customize this expression when you do not want to set

### Data Source Tab - String Value Test Edit Tabs

#### Data Source Tab

The Data Source tab of the String Value Test contains the following option:

- Data Source Expression 
 —A string expression the step uses to compare against the expected value. The default value is
 Step.Result.String 
 property. You can customize this expression when you do not want to set the value of
 Step.Result.String 
 in the
 code module 
 . For example, you can set the data source expression to refer to variables and properties such as,
 Locals.MyStringValue 
 .

Parent topic:

String Value Test Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/data-streams-api.html language=enus -->
## TOPIC 03561: Data Streams API

- bundle_id: `teststand-api-reference`
- source_path: `tsref/data-streams-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/data-streams-api.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: All functionality provided by the Data Streams step types is available through the TestStand API. The step types themselves are implemented directly on top of this API. If you encounter situations too complex for the built-in step types, you can supplement them with direct calls to the API. Alternat

### Data Streams API

All functionality provided by the Data Streams step types is available through the TestStand API. The step types themselves are implemented directly on top of this API. If you encounter situations too complex for the built-in step types, you can supplement them with direct calls to the API. Alternatively, you can forgo the built-in step types altogether, building your own custom step types or using the API directly.

For example, the built-in step types provide a convenient way to skip over metadata at the top of a CSV file, allowing you to read the main data table in a for each loop. Instead of skipping over the metadata, you can read it using the API. The API also supports custom separator characters, whereas the built-in step types do not expose this functionality.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-data-location-legacy-import-export-p.html language=enus -->
## TOPIC 03562: Database Data Location - Legacy Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-data-location-legacy-import-export-p.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-data-location-legacy-import-export-p.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database Data Location The Import/Export Properties dialog box contains the following tabs when you select Database from the Data Location ring control: Source/Destination Properties Additional Columns

### Database Data Location - Legacy Import/Export Properties Dialog Box

#### Database Data Location

The Import/Export Properties dialog box contains the following tabs when you select Database from the Data Location ring control:

- Source/Destination
- Properties
- Additional Columns

Parent topic:

Legacy Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-explorer.html language=enus -->
## TOPIC 03563: Database Explorer

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-explorer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-explorer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Database Explorer pane displays information about open database connections. The Database Explorer contains the following options: Connection List —Displays the names of all open database connections. All data shown in the Database Explorer and all supported operations are applied to the connect

### Database Explorer

The Database Explorer pane displays information about open database connections. The Database Explorer contains the following options:

- Connection List 
 —Displays the names of all open database connections. All data shown in the Database Explorer and all supported operations are applied to the connection selected from the drop-down list. Hovering over a connection displays the connection string.
- Database Object View 
 —Displays the database objects that exist in the currently selected database in the following hierarchical manner. The view displays only the database objects the current user has permission to access, as defined in the database connection string.
 
 The context menu includes the following options in different levels of the database object hierarchy:
  1. Databases—Lists the catalogs or schemas for the selected database. A "default" tag appended to a database name indicates the default database for the connection.
  2. System Databases—Lists all the system catalogs or schemas in the selected database.
 Note 
 For MySQL and Oracle databases, the application lists only the default user schema as defined by the connection string. For Sybase, the application lists only the schema present in the default catalog as defined by the connection string.
  3. Tables—Lists all the tables contained within a catalog or schema.
  4. System Tables—Lists all the system tables contained within a catalog or schema.
  5. Views—Lists all the views contained within a catalog or schema.
  6. System Views—Lists all the system views contained within a catalog or schema.
  7. Columns—Represents the columns in a Table or View. The node displays the name, data type, and whether the column is nullable.
  - View Data 
 —Launches a new
 Execute SQL 
 tab that contains a
 data grid 
 that displays the contents of the database table or view.
  - Edit Data 
 —Launches the
 Edit Data 
 tab that contains a data grid that displays the contents of the database table. You can edit the contents of the table and submit the changes to the database. This operation is supported only in user databases.
  - Delete All Data 
 —Deletes all the records present in the table. This operation is supported only in user databases.
  - Add Table 
 —Launches the
 Add Table 
 dialog box. This operation is supported only in user databases.
  - Add Column 
 —Launches the
 Add Column 
 dialog box. This operation is supported only in user databases.
  - Drop Column 
 —Deletes the selected column from the table. This operation is supported only in user databases.
  - Drop Table 
 —Deletes the selected table from the database. This operation is supported only in user databases.
  - Drop All Tables 
 —Deletes all tables from the selected database. This operation is supported only in user databases.
  - Describe Table 
 —Launches the
 Describe Table 
 dialog box.
  - Generate Query 
 —Generates the SQL query required to perform the chosen operation and creates a new Execute SQL tab with the SQL query set. You can execute the query to complete the operation.
 Note 
 Schema update operations that SQL queries execute from the Execute SQL tab do not update the Database Object View. The view updates the next time you refresh the connection.
 The Generate Query option applies only to the Delete All Data, Drop Column, Drop Table, and Drop All Tables operations.

The Database Explorer also contains the following options:

- New Data Link 
 —Launches the
 New Data Link 
 dialog box in which you specify a new database connection.
- Save Data Link 
 —Specifies a path to save the selected connection as a
 .udl 
 file.
- Disconnect 
 —When you close a connection, the Database Viewer removes the connection from the Connection List and closes any Execute SQL or Edit Data tabs associated with the connection. Any commands executing on the connection when you close it will be terminated or cancelled. For example, if you refresh a connection and then disconnect it, the Refresh command underway will be terminated.
- Refresh Connection 
 —Retrieves all the database objects for that connection again and updates the Database Object View. You can also press F5 to perform this command.
- View Connection Information 
 —Launches the
 View Connection Information 
 dialog box.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-options-dialog-box.html language=enus -->
## TOPIC 03564: Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Result Processing dialog box, click the icon in the Options column for the built-in database plug-in to launch the Database Options dialog box, in which you can customize the logging of results to a database. The settings you select in the Database Options dialog box apply to all executions t

### Database Options Dialog Box

Result Processing

Note

- If you are using the equivalent legacy TestStand 2010 process models, select
 Configure»Database Options 
 to launch the Database Options dialog box.
- National Instruments recommends storing reports, offline result files, and databases locally instead of over a network for reliability and performance concerns. If you require a network storage solution, configure TestStand to store data locally and use a separate process or application to transfer files to and from the network.

The Database Options dialog box contains the following tabs:

- Logging/Data Link Options 
 —Use this tab to set general options for database logging and to configure the data link information the TestStand process model requires to connect to a database and log data.
  - Logging Options 
 —General options for database logging, such as the type of data to log, whether TestStand logs to a database after testing a UUT, or whether TestStand logs concurrently with an execution.
  - Data Link Options 
 —Data link information the process model requires to connect to a database and log data.
- Schemas 
 —Use this tab to access the available database schemas, customize a schema, and specify the default schema the TestStand process model uses. If the configuration file
 TestStandDatabaseSchemas.ini 
 does not exist, or database schemas do not exist in the configuration file, TestStand will load the default installed schemas.

The Database Options dialog box also contains the following control:

- Apply 
 —Applies the changes made without closing the dialog box.

Note

Apply

OK

Cancel

Apply

Apply

Errors/Warnings in Database Options dialog box

#### See Also

[Database Known Issues](/csh?context=ts_tsfundamentals_database_known_issues)

[Database Logging](/csh?context=ts_tsfundamentals_database_connectivity)

[Result Processing dialog box](result-processing-dialog-box.html)

[Using the Database Options with TestStand 2013 or Earlier Process Models](using-the-database-options-with-teststand-201.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-plugins.html language=enus -->
## TOPIC 03565: Database Plugins

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-plugins.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database Plugins The database plugin supports the following databases: Access MySQL SQLServer Sybase Oracle (version 12c and later) The database stores all the required information in the following tables: Group Table Properties Table See the Property Loader Plugins - Database Table Schemas topic fo

### Database Plugins

#### Database Plugins

The database plugin supports the following databases:

- Access
- MySQL
- SQLServer
- Sybase
- Oracle (version 12c and later)

The database stores all the required information in the following tables:

- Group Table
- Properties Table

See the
 [Property Loader Plugins - Database Table Schemas](/csh?context=ts_tsref_propertyloaderplugins_dbformat)
 topic for more information about the required table schemas for this plugin.

The plugin contains the following plugin-specific import and export options:

- Import Options
- Export Options

#### Group Table

The Group Table is used to store information about a property loader group. The default name
for this table is ‘GROUP_DESC’. The Group table schema contains following columns:

GROUP_ID
 —Contains the id of the property loader group. It is the primary key of the
groups table and is of type VARCHAR and can contain 64 characters.

NAME
 —Contains the name of the property loader group. This column can contain null
values. The data-type for this column is as follows:

- Access – LONGTEXT
- MySQL –VARCHAR(8000)
- SQLServer –VARCHAR (8000)
- Sybase –VARCHAR(32767)
- Oracle – VARCHAR2(4000)

DESCRIPTION
 — Contains the description of the property loader group. This column can
contain null values. The data-type for this column is as follows:

- Access – LONGTEXT
- MySQL –VARCHAR(8000)
- SQLServer –VARCHAR (8000)
- Sybase –VARCHAR(32767)
- Oracle – VARCHAR2(4000)

#### Properties Table

The Properties Table is used to store information about various TestStand properties and their
corresponding values. The default name for this table is ‘PROPERTIES’. The Property table
schema contains following columns:

ID
 — This is an auto increment column and is used as primary key for the Property Table.

GROUP_ID
 — Specifies the id of the property loader group in which the property is present. It
is foreign key and references the ‘GROUP_ID’ column of the groups table. It is of type
VARCHAR and can contain 64 characters. This is a mandatory column and cannot contain
null values or empty strings.

SEQUENCE_FILE_NAME
 — Contains the name of the target sequence file. This column
can contain null values. It is of type VARCHAR and can contain a maximum of 255
characters.

SEQUENCE_NAME
 — Contains the name of the target sequence. This column can contain
null values. It is of type VARCHAR and can contain a maximum of 255 characters.

CATEGORY
 — Contains the property object category (StationGlobals, FileGlobals, Locals,
Parameters or Step[<UniqueStepId>]) for the TestStand property. All object category names must be enclosed in
 {}
 , expect Step. This is a mandatory column
and cannot contain null values or empty string. The data-type for this column in different
database is as follows:

- Access – LONGTEXT
- MySQL–VARCHAR(8000)
- SQLServer–VARCHAR(8000)
- Sybase –VARCHAR(32767)
- Oracle – VARCHAR2(4000)

PROPERTY_LOOKUP
 — Contains the lookup string of TestStand properties or alias names
within angular braces. This is a mandatory column and cannot contain null values or empty
strings. The data-type for this column in different database is as follows:

- Access – LONGTEXT
- MySQL–VARCHAR(8000)
- SQLServer–VARCHAR(8000)
- Sybase –VARCHAR(32767)
- Oracle – VARCHAR2(4000)

VALUE
 — Contains the value to which the specified of the TestStand property to whose value
is exported or to which value is being imported. This column can contain null values. The
data-type for this column in different database is as follows:

- Access – LONGTEXT
- MySQL–VARCHAR(8000)
- SQLServer–VARCHAR(8000)
- Sybase –VARCHAR(32767)
- Oracle – VARCHAR2(4000)

#### Import Options

The database plugin contains the following plugin-specific import options:

Table Names
 — Contains the following options:

- Group Table 
 — The name of the table in the database from which group information will
be used.
- Properties Table 
 — The name of the table in the database from which property
information will be used. The foreign key used in the table should refer to the primary
key of the Group table.

Filter Options
 — The column values that each row must match. Use New and Remove to
create a new item in the list and remove currently selected item from the list.

- Column Name 
 — Specify the name of the column.
- Expected Value 
 — Specify the expected value of the column.

Validate
 — Validates that the specified table names in the Group and Properties tables exist in the specified database.

#### Export Options

The database plugin contains the following plugin-specific export options:

Group Table
 — The name of the table in the database to which group information will be
exported.

Properties Table
 — The name of the table in the database from which property information
will be exported.

Optional Columns To Export
 — Specifies whether values will be exported to optional
columns or not. While performing export, values will be exported to all the optional columns
that were checked.

- Sequence File 
 — Exports the name of the target sequence file into the
SEQUENCE_FILE_NAME column in the selected properties table.
- Sequence 
 — Exports the name of the sequence into the SEQUENCE_NAME column of
the selected properties table.
- Type 
 — Exports the type of TestStand property in the TYPE column of the selected
properties table.

Overwrite Existing Records
 — Specifies if all values in the property table associated with the sequence file in the configured property loader group will be deleted before
performing export using the Import/Export tool. When enabled, all the properties which refer
to the current sequence file and property loader group will be deleted from the properties table and the new
properties will be exported. When disabled, none of the properties will be deleted, and if a
property already exists in the properties table in the database then its value will be overwritten.

Note

Sequence File

Optional Columns
to Export

Sequence File

Parent topic:

Property Loader Plugins

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-step-types.html language=enus -->
## TOPIC 03566: Database Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the built-in Database step types to communicate with a database. Use the Property Loader step type to import property and variable values from a file or database during an execution . A simple database operation includes the following steps: Use the Open Database step type to connect to a databa

### Database Step Types

Use the built-in Database step types to communicate with a database. Use the
 [Property Loader](property-loader-step.html)
 step type to import property and variable values from a file or database during an
 [execution](/csh?context=ts_tsfundamentals_executions)
 .

A simple database operation includes the following steps:

1. Use the
 Open Database 
 step type to connect to a database.
2. Use the
 Open SQL Statement 
 step type to perform an SQL query on tables in the database.
3. Use
 Data Operation 
 step types to create new records and to retrieve and update existing records.
4. Use the
 Close SQL Statement 
 step type to close the SQL query.
5. Use the
 Close Database 
 step type to disconnect from a database.

To edit a database step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , click
 Edit <
 Step Type Name
 >
 on the Edit tab of the
 [Step Settings](step-settings-pane.html)
 pane.

To edit a database step type from a
 [custom user interface](/csh?context=ts_tsfundamentals_uis)
 , select
 Edit
 from the context menu for the step or click
 Edit
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

#### See Also

[Databases (Example)](/csh?context=ts_8108)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-viewer-application.html language=enus -->
## TOPIC 03567: Database Viewer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-viewer-application.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-viewer-application.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand includes the Database Viewer application for viewing data in a database, editing table information, and executing SQL commands. You can access the Database Viewer application in the following ways: Select Tools»Database Viewer in the TestStand Sequence Editor . (Windows 8.1) Click the NI L

### Database Viewer Application

TestStand includes the Database Viewer application for viewing data in a database, editing table information, and executing SQL commands. You can access the Database Viewer application in the following ways:

- Select
 Tools»Database Viewer 
 in the
 TestStand Sequence Editor 
 .
- (Windows 8.1) Click the
 NI Launcher 
 tile on the Start screen and select
 TestStand»Tools»TestStand Database Viewer 
 .
- (Windows 10 or 7) Select
 Start»All Programs»National Instruments»TestStand»Tools»TestStand Database Viewer 
 .
- Run
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Tools\DatabaseView\DatabaseView.exe 
 .
- Run
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Tools\DatabaseView\DatabaseView.exe 
 from the
 command line 
 .

The Database Viewer supports the following functionality:

- Database Explorer 
 —The
 Database Explorer 
 pane displays information about open database connections. You can view and edit data, add or remove database tables, and open or close database connections.
- Database Viewer Tabs 
 —The Database Viewer contains
 Edit Data 
 and
 Execute SQL 
 tabs, which are associated with an open database connection. All operations performed in each tab execute on the database connection associated with that tab. The connection you select from the connection list when you create a tab becomes the connection associated with that tab.
- Binary Data Viewer 
 —The
 Binary Data Viewer 
 allows you to view binary data that has been logged to the database. You can view the data as a table, a graph, or as the layout in memory.

Note

#### See Also

[Command Line Arguments](command-line-arguments.html)

[Configuring Connection Strings](/csh?context=ts_tsref_dbviewer_connectionstrings)

[Customizing the Database Viewer User Interface](/csh?context=ts_tsref_dbviewer_uifeatures)

[Database Known Issues](/csh?context=ts_tsfundamentals_database_known_issues)

[Database Logging](/csh?context=ts_tsfundamentals_database_connectivity)

[Database Viewer Menu Bar](database-viewer-menu-bar.html)

[Edit Data Tab](edit-data-tab.html)

[Execute SQL Tab](execute-sql-tab.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-viewer-menu-bar.html language=enus -->
## TOPIC 03568: Database Viewer Menu Bar

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-viewer-menu-bar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-viewer-menu-bar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Database Viewer Menu Bar contains the following menu items: File —Contains the following options: Open —Opens a database file. Opening different types of database files leads to the following different actions. .accdb, .dbf, .mdb—Opens a database connection so you can access the database content

### Database Viewer Menu Bar

The Database Viewer Menu Bar contains the following menu items:

- File 
 —Contains the following options:
  - Open 
 —Opens a database file. Opening different types of database files leads to the following different actions.
    - .accdb, .dbf, .mdb—Opens a database connection so you can access the database content.
    - .sql—Loads the contents of the file into an
 Execute SQL 
 tab, where you can execute the commands against the selected database connection.
    - .udl—Opening a
 .udl 
 file allows you to specify parameters for creating a new database connection.
  - New Data Link 
 —Launches the
 New Data Link 
 dialog box, in which you can specify the parameters for a new database connections.
  - Save Data Link 
 —Saves the connection string of the selected connection as a
 .udl 
 file.
  - New Execute SQL Tab 
 —Creates a new Execute SQL tab for executing SQL queries. The Execute SQL tab will be associated with the connection selected in the connection list when the tab is created.
  - Open TestStand SQL Files 
 —Launches the
 Open TestStand SQL Files 
 dialog box.
  - Close 
 —Closes an open tab.
  - Export Document 
 —Launches the
 Export Document 
 dialog box after you select a file format for export from the sub-menu.
  - Print 
 —Launches the
 Print 
 dialog box, in which you can configure and print the contents of a data grid in an open tab.
  - Recent Files 
 —Lists the most recently used files.
  - Recent Connections 
 —Lists the most recently used connections.
  - Exit 
 —Closes the current Database Viewer session. The application closes all open windows automatically.
- Options 
 —Select
 Viewer Options 
 to launch the
 Viewer Options 
 dialog box, in which you can customize the behavior of the Database Viewer application.
- SQL 
 —The SQL menu items apply only to the
 Execute SQL 
 or
 Edit Data 
 tabs. All SQL menu operations are performed on the currently active tab.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/database-viewer-tabs.html language=enus -->
## TOPIC 03569: Database Viewer Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/database-viewer-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/database-viewer-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Database Viewer contains Edit Data and Execute SQL tabs, which are associated with an open database connection. All operations performed in each tab execute on the database connection associated with that tab. The connection you select from the connection list when you create a tab becomes the c

### Database Viewer Tabs

The Database Viewer contains
 [Edit Data](edit-data-tab.html)
 and
 [Execute SQL](execute-sql-tab.html)
 tabs, which are associated with an open database connection. All operations performed in each tab execute on the database connection associated with that tab. The connection you select from the connection list when you create a tab becomes the connection associated with that tab.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/debug-menu.html language=enus -->
## TOPIC 03570: Debug Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/debug-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/debug-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Debug menu in the TestStand Sequence Editor contains the following items, which control how TestStand single steps within an execution: Toggle Breakpoint —Sets or clears the breakpoint state for the selected steps. Run Mode —Sets the following run-mode values for the step: Force to Pass —The ste

### Debug Menu

The Debug menu in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 contains the following items, which control how TestStand single steps within an execution:

- Toggle Breakpoint 
 —Sets or clears the breakpoint state for the selected steps.
- Run Mode 
 —Sets the following run-mode values for the step:
  - Force to Pass 
 —The step does not execute. Instead, the
 step status 
 is set to
 Passed 
 .
  - Force to Fail 
 —The step does not execute. Instead, the step status is set to
 Failed 
 .
  - Skip 
 —The step does not execute. Instead, the step status is set to
 Skipped 
 .
  - Normal 
 —The step executes normally.
- Resume 
 —Continues execution when the sequence execution is in a suspended state.
- Step Into 
 —Enters and suspends within a function, VI, or sequence the step calls. If the step calls a
 code module 
 TestStand cannot suspend within, TestStand suspends the execution at the next step.
 Note 
 When you step into a VI from TestStand and then select
 Return to Caller
 without executing the VI, any values you change in the controls or indicators of the suspended VI are not returned to TestStand.
- Step Over 
 —Executes the step to which the execution pointer points when the sequence execution is in a breakpoint state. If the step is a call to another sequence, the Step Over command executes the entire sequence and enters a breakpoint state on the step following the
 Sequence Call 
 step. If the TestStand Engine encounters a breakpoint within the Sequence Call step, the Step Over command pauses at the breakpoint. If the Step Over command executes on an End step in a Pre-Step
 callback sequence 
 , TestStand attempts to step into the code module.
- Step Out 
 —Resumes execution through the end of the current sequence and suspends/pauses on the next step in the calling sequence.
 Note 
 When you use the Step Into, Step Over, or Step Out commands, TestStand does not suspend in Sequence callbacks or step groups where tracing is disabled unless TestStand is already suspended within the sequence.
- Set Next Step to Cursor 
 —TestStand starts from the selected step when you resume execution.
- Break 
 —Suspends the active execution after completing the execution of the current step in all threads of the execution. Because the
 Allow Break While in Code Modules 
 option on the
 Execution 
 tab of the
 Station Options 
 dialog box is enabled by default, TestStand suspends the execution even if some threads are executing code inside a code module. Using the
 Thread.ExternallySuspended 
 property in a code module results in the same behavior.
- Break All 
 —Suspends all running executions. Each execution suspends after completing the execution of the current step in all threads of the execution. Because the
 Allow Break While in Code Modules 
 option on the
 Execution 
 tab of the
 Station Options 
 dialog box is enabled by default, TestStand suspends the executions even if some threads are executing code inside a code module. Using the
 Thread.ExternallySuspended 
 property in a code module results in the same behavior.
- Terminate Execution 
 —Terminates a running or suspended execution that is active. A running execution terminates only after completing the currently executing step in all threads of the execution. When you terminate an execution, TestStand runs the Cleanup
 step groups 
 for all active sequences on the call stack.
- Abort (no cleanup) 
 —Aborts a running or suspended execution that is active. A running execution aborts only after completing the currently executing step in all threads of the execution. When an execution aborts, TestStand does not run any Cleanup step groups.
 Note 
 If a code module waits for user input or does not return quickly for any other reason, the code module can use the
 [Execution](../tsapiref/execution.html)
 class in the TestStand API to monitor for termination or abort requests.
- Terminate All 
 —Terminates all running executions. Each execution terminates after completing the execution of the current step in all threads of the execution.
- Abort All (no cleanup) 
 —Aborts all running executions. Each execution aborts after completing the execution of the current step in all threads of the execution.
- Resume All 
 —Continues all suspended executions.
- Breakpoints/Watches 
 —Launches the
 Edit Breakpoints/Watch Expressions 
 dialog box, in which you can edit breakpoints and watch expressions associated with the current workspace.
- Sequence Analyzer 
 —Contains the following options for use with the TestStand Sequence Analyzer:
  - Analyze <
 file or project name
 > 
 —Starts analysis. If the
 Current Sequence Analyzer Project 
 window is active, the sequence analyzer analyzes the project. If a sequence file or workspace file is active, the sequence analyzer analyzes the sequence file or workspace file using the rules and settings from the current sequence analyzer project.
  - Stop All Analysis 
 —Stops all analysis sessions in progress. The sequence analyzer waits for the currently executing analysis module to complete before stopping the analysis.
  - Toggle Analyze File Before Executing 
 —Enables or disables the Analyze File Before Executing option in the
 Sequence Analyzer Options 
 dialog box. When you enable this option, the sequence analyzer uses the rules and settings in the current sequence analyzer project to analyze the active sequence file when you initiate an execution. Enabling this option can help you find errors early during development.
  - Current Sequence Analyzer Project 
 —Shows the Current Sequence Analyzer Project window for the current sequence analyzer project.
  - Sequence Analyzer Options 
 —Launches the Sequence Analyzer Options dialog box, in which you edit settings the sequence analyzer uses to analyze the active sequence file.
 Note 
 The sequence editor requires an enabled
 [ConfigApp user privilege](user-and-group-privileges.html)
 to launch the Sequence Analyzer Options dialog box. The built-in TestStand Developer and Administrator user groups grant this privilege by default.

#### See Also

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[Edit Breakpoints/Watch Expressions dialog box](edit-breakpoints-watch-expressions-dialog-box.html)

[Execution](../tsapiref/execution.html)

[Sequence Analyzer Options dialog box](sequence-analyzer-options-dialog-box.html)

[Thread.ExternallySuspended](../tsapiref/thread-externallysuspended.html)

[User and Group Privileges](user-and-group-privileges.html)

Parent topic:

Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/debug-menu2.html language=enus -->
## TOPIC 03571: Debug Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/debug-menu2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/debug-menu2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Debug menu in a TestStand User Interface contains the following options for editing sequences and steps: Menu items marked with an asterisk ( * ) appear only in Editor Mode. Toggle Breakpoint —Sets or clears the breakpoint state for the selected steps. Run Mode —Sets the following run mode value

### Debug Menu

TestStand User Interface

Note

*

- Toggle Breakpoint 
 —Sets or clears the breakpoint state for the selected steps.
- Run Mode 
 —Sets the following run mode values for the step:
  - Force to Pass 
 —The step does not execute. Instead, the
 step status 
 is set to
 Passed 
 .
  - Force to Fail 
 —The step does not execute. Instead, the step status is set to
 Failed 
 .
  - Skip 
 —The step does not execute. Instead, the step status is set to
 Skipped 
 .
  - Normal 
 —The step executes normally.
- Resume 
 —Continues execution when the sequence execution is in a suspended state.
- Step Into 
 —Enters and suspends within a function, VI, or sequence the step calls. If the step calls a
 code module 
 TestStand cannot suspend within, TestStand suspends the execution at the next step.
 Note 
 When you step into a VI from TestStand and then select
 Return to Caller
 without executing the VI, any values you change in the controls or indicators of the suspended VI are not returned to TestStand.
- Step Over 
 —Executes the step to which the execution pointer points when the sequence execution is in a breakpoint state. If the step is a call to another sequence, the Step Over command executes the entire sequence and enters a breakpoint state on the step following the Sequence Call step. If the TestStand Engine encounters a breakpoint within the Sequence Call step, the Step Over command pauses at the breakpoint. If the Step Over command executes on an End step in a Pre-Step callback sequence, TestStand attempts to step into the code module.
- Step Out 
 —Resumes execution through the end of the current sequence and suspends/pauses on the next step in the calling sequence.
 Note 
 When you use the Step Into, Step Over, or Step Out commands, TestStand does not suspend in Sequence callbacks or step groups where tracing is disabled unless TestStand is already suspended within the sequence.
- Set Next Step to Cursor 
 —TestStand starts from the selected step when you resume execution.
- Break 
 —Suspends the active execution after completing the execution of the current step in all threads of the execution. Because the
 Allow Break While in Code Modules 
 option on the
 Execution 
 tab of the
 Station Options 
 dialog box is enabled by default, TestStand suspends the execution even if some threads are executing code inside a code module. Using the
 Thread.ExternallySuspended 
 property in a code module results in the same behavior.
- Terminate Execution 
 —Terminates a running or suspended execution that is active. A running execution terminates only after completing the currently executing step in all threads of the execution. When you terminate an execution, TestStand runs the Cleanup step groups for all active sequences on the call stack.
- Abort (no cleanup) 
 —Aborts a running or suspended execution that is active. A running execution aborts only after completing the currently executing step in all threads of the execution. When an execution aborts, TestStand does not run any Cleanup step groups.
 Note 
 If a code module waits for user input or does not return quickly for any other reason, the code module can use the
 [Execution](../tsapiref/execution.html)
 class in the TestStand API to monitor for termination or abort requests.
- Break All 
 —Suspends all running executions. Each execution suspends after completing the execution of the current step in all threads of the execution. If you enable the
 Allow Break While in Code Modules 
 option on the
 Execution 
 tab of the
 Station Options 
 dialog box or a code module uses the
 Thread.ExternallySuspended 
 property, TestStand suspends the executions even if some threads are executing code inside a code module.
- Terminate All 
 —Terminates all running executions. Each execution terminates after completing the execution of the current step in all threads of the execution.
- Abort All (no cleanup) 
 —Aborts all running executions. Each execution aborts after completing the execution of the current step in all threads of the execution.
- Resume All 
 —Continues all suspended executions.
- Breakpoints 
 —Launches the
 Edit Breakpoints/Watch Expressions 
 dialog box, in which you can edit breakpoints and watch expressions associated with the current workspace.

#### See Also

[Edit Breakpoints/Watch Expressions dialog box](edit-breakpoints-watch-expressions-dialog-box.html)

[Execution](../tsapiref/execution.html)

[Thread.ExternallySuspended](../tsapiref/thread-externallysuspended.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/debug-options-dialog-box.html language=enus -->
## TOPIC 03572: Debug Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/debug-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/debug-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Station Options dialog box and click Debug Options on the Preferences tab to launch the Debug Options dialog box. Use this dialog box to specify whether TestStand performs memory checking and other debug options. If a code module corrupts the memory within the TestStand process, TestStand

### Debug Options Dialog Box

Launch the
 [Station Options](station-options-dialog-box.html)
 dialog box and click
 Debug Options
 on the
 [Preferences](preferences-tab-station-options-dialog-box.html)
 tab to launch the Debug Options dialog box. Use this dialog box to specify whether TestStand performs memory checking and other debug options.

If a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 corrupts the memory within the TestStand process, TestStand can error or terminate. TestStand can only detect the types of memory corruption listed below. Some of these options can slow the execution of steps.

The Debug Options dialog box contains the following options:

- Stack Checking 
 —When you enable this option, adapters attempt to detect when code modules incorrectly alter the call stack. TestStand cannot detect stack corruption when the operating system marshals an ActiveX call to a different thread, or when calling an EXE ActiveX server.
 Note 
 This option applies only to the LabWindows/CVI (in-process), C/C++ DLL, and ActiveX Adapters when calling a DLL server.
- Buffer Checking 
 —When you enable this option, adapters detect changes to the memory surrounding buffer parameters passed to code modules. Adapters also detect when const string parameters are altered while calling code modules.
 Note 
 This option applies only to the LabWindows/CVI and C/C++ DLL Adapters.
 When you overwrite the last character in a string buffer, the LabWindows/CVI and C/C++ DLL Adapters automatically allocate an extra character to prevent memory corruption. Consequently, TestStand does not detect a buffer overrun error when you exceed a string buffer size by only one character.
- Report Object Leaks 
 —When you enable this option, TestStand launches a dialog box during shutdown of the TestStand Engine that contains a list of any top-level Property Objects with unreleased references.
- Send Output Messages to the Debugger 
 —When you enable this option, TestStand sends text for output messages to the debugger. Output messages are sent to the debugger even when the Output pane in the
 TestStand Sequence Editor 
 is disabled.
 Note 
 This option applies only to native (non-managed) debugging.
- Report Known OS and Component Problems 
 —When you enable this option, TestStand launches a dialog box, during shutdown of the TestStand Engine, that contains a list of any operating system issues or component-related issues that can cause leaks in memory, Graphics Device Interface (GDI), and
 User 
 object resources in TestStand.

Note

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/default-expressions-tab-step-type-properties.html language=enus -->
## TOPIC 03573: Default Expressions Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/default-expressions-tab-step-type-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/default-expressions-tab-step-type-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default Expressions Tab The initial expression settings for new steps you create from the step type. Refer to the Expressions panel of the Step Settings pane or the Expressions tab of the Step Properties dialog box for more information about expression settings. TestStand uses the values in this dia

### Default Expressions Tab - Step Type Properties Dialog Box

#### Default Expressions Tab

The initial expression settings for new steps you create from the step type. Refer to the
 [Expressions panel](expressions-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane or the
 [Expressions](expressions-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box for more information about expression settings.

Note

- TestStand uses the values in this dialog box as the initial values for new steps you create. Changes to these values do not automatically propagate to existing steps of this type. Enable the
 Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 option in the Step Type Properties Dialog Box to apply the changes to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- The
 Default Run Options 
 ,
 Default Post Actions 
 ,
 Default Loop Options 
 , Default Expressions,
 Default Switching 
 , and
 Default Synchronization 
 tabs display instance properties. These tabs have the same appearance and behavior as the Run Options, Loop Options, Expressions, and Synchronization tabs located on the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box for a step instance.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/default-loop-options-tab-step-type-properties.html language=enus -->
## TOPIC 03574: Default Loop Options Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/default-loop-options-tab-step-type-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/default-loop-options-tab-step-type-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default Loop Options Tab The initial loop option settings for new steps you create from the step type. Refer to the Looping panel of the Step Settings pane or the Loop Options tab of the Step Properties dialog box for more information about loop option settings. TestStand uses the values in this dia

### Default Loop Options Tab - Step Type Properties Dialog Box

#### Default Loop Options Tab

The initial loop option settings for new steps you create from the step type. Refer to the
 [Looping panel](looping-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane or the
 [Loop Options](loop-options-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box for more information about loop option settings.

Note

- TestStand uses the values in this dialog box as the initial values for new steps you create. Changes to these values do not automatically propagate to existing steps of this type. Enable the
 Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 option in the Step Type Properties Dialog Box to apply the changes to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- The
 Default Run Options 
 ,
 Default Post Actions 
 , Default Loop Options,
 Default Expressions 
 ,
 Default Switching 
 , and
 Default Synchronization 
 tabs display instance properties. These tabs have the same appearance and behavior as the Run Options, Loop Options, Expressions, and Synchronization tabs located on the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box for a step instance.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/default-post-actions-tab-step-type-properties.html language=enus -->
## TOPIC 03575: Default Post Actions Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/default-post-actions-tab-step-type-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/default-post-actions-tab-step-type-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default Post Actions Tab The initial post action settings for new steps you create from the step type. Refer to the Post Actions panel of the Step Settings pane or the Post Actions tab of the Step Properties dialog box for more information about post action settings. TestStand uses the values in thi

### Default Post Actions Tab - Step Type Properties Dialog Box

#### Default Post Actions Tab

The initial post action settings for new steps you create from the step type. Refer to the
 [Post Actions panel](post-actions-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane or the
 [Post Actions](post-actions-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box for more information about post action settings.

Note

- TestStand uses the values in this dialog box as the initial values for new steps you create. Changes to these values do not automatically propagate to existing steps of this type. Enable the
 Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 option in the Step Type Properties Dialog Box to apply the changes to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- The
 Default Run Options 
 , Default Post Actions,
 Default Loop Options 
 ,
 Default Expressions 
 ,
 Default Switching 
 , and
 Default Synchronization 
 tabs display instance properties. These tabs have the same appearance and behavior as the Run Options, Loop Options, Expressions, and Synchronization tabs located on the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box for a step instance.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/default-run-options-tab-step-type-properties.html language=enus -->
## TOPIC 03576: Default Run Options Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/default-run-options-tab-step-type-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/default-run-options-tab-step-type-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default Run Options Tab The initial run option settings for new steps you create from the step type. Refer to the Run Options panel of the Step Settings pane or the Run Options tab of the Step Properties dialog box for more information about run option settings. TestStand uses the values in this dia

### Default Run Options Tab - Step Type Properties Dialog Box

#### Default Run Options Tab

The initial run option settings for new steps you create from the step type. Refer to the
 [Run Options panel](run-options-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane or the
 [Run Options](run-options-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box for more information about run option settings.

Note

- TestStand uses the values in this dialog box as the initial values for new steps you create. Changes to these values do not automatically propagate to existing steps of this type. Enable the
 Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 option in the Step Type Properties Dialog Box to apply the changes to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- The Default Run Options,
 Default Post Actions 
 ,
 Default Loop Options 
 ,
 Default Expressions 
 ,
 Default Switching 
 , and
 Default Synchronization 
 tabs display instance properties. These tabs have the same appearance and behavior as the Run Options, Loop Options, Expressions, and Synchronization tabs located on the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box for a step instance.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/default-switching-tab-step-type-properties-di.html language=enus -->
## TOPIC 03577: Default Switching Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/default-switching-tab-step-type-properties-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/default-switching-tab-step-type-properties-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default Switching Tab The initial run switching settings for new steps you create from the step type. Refer to the Switching panel of the Step Settings pane or the Switching tab of the Step Properties dialog box for more information about run switching settings. TestStand uses the values in this dia

### Default Switching Tab - Step Type Properties Dialog Box

#### Default Switching Tab

The initial run switching settings for new steps you create from the step type. Refer to the
 [Switching panel](switching-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane or the
 [Switching](switching-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box for more information about run switching settings.

Note

- TestStand uses the values in this dialog box as the initial values for new steps you create. Changes to these values do not automatically propagate to existing steps of this type. Enable the
 Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 option in the Step Type Properties Dialog Box to apply the changes to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- The
 Default Run Options 
 ,
 Default Post Actions 
 ,
 Default Loop Options 
 ,
 Default Expressions 
 , Default Switching, and
 Default Synchronization 
 tabs display instance properties. These tabs have the same appearance and behavior as the Run Options, Loop Options, Expressions, and Synchronization tabs located on the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box for a step instance.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/default-synchronization-tab-step-type-propert.html language=enus -->
## TOPIC 03578: Default Synchronization Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/default-synchronization-tab-step-type-propert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/default-synchronization-tab-step-type-propert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default Synchronization Tab The initial synchronization settings for new steps you create from the step type. Refer to the Synchronization panel of the Step Settings pane or the Synchronization tab of the Step Properties dialog box for more information about synchronization settings. TestStand uses

### Default Synchronization Tab - Step Type Properties Dialog Box

#### Default Synchronization Tab

The initial synchronization settings for new steps you create from the step type. Refer to the
 [Synchronization panel](synchronization-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane or the
 [Synchronization](synchronization-tab-step-properties-dialog-bo.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box for more information about synchronization settings.

Note

- TestStand uses the values in this dialog box as the initial values for new steps you create. Changes to these values do not automatically propagate to existing steps of this type. Enable the
 Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 option in the Step Type Properties Dialog Box to apply the changes to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- The
 Default Run Options 
 ,
 Default Post Actions 
 ,
 Default Loop Options 
 ,
 Default Expressions 
 ,
 Default Switching 
 , and Default Synchronization tabs display instance properties. These tabs have the same appearance and behavior as the Run Options, Loop Options, Expressions, and Synchronization tabs located on the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box for a step instance.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/dependencies-dialog-box.html language=enus -->
## TOPIC 03579: Dependencies Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/dependencies-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/dependencies-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the TestStand Deployment Utility and click the Dependencies button on the package Distributions Options tab to launch the Dependencies dialog box, in which you can specify additional packages to reference from the deployment package. If the Dependencies dialog box does not list the package yo

### Dependencies Dialog Box

Launch the TestStand Deployment Utility and click the
 Dependencies
 button on the package Distributions Options tab to launch the Dependencies dialog box, in which you can specify additional packages to reference from the deployment package. If the Dependencies dialog box does not list the package you need, launch NI Package Manager to verify that the package is installed on the development computer. Refer to the documentation for the package to determine whether the package can be included in deployments.

The Dependencies dialog box contains the following options:

- Filter 
 —Determines which packages to display in NI Package Manager.
  - Runtime deployment packages only 
 —Displays only the runtime packages.
  - All visible packages 
 —Displays all user visible packages.
  - All packages (including hidden) 
 —Displays all packages, including hidden packages.
- Category 
 —Configures the category for the package, which is shown in NI Package Manager in the category column. If you select Infrastructure, the package will be hidden by default in NI Package Manager.
- Packages List 
 —Lists the Packages you can reference from the deployment package. You can filter which packages are visible using the package filter control.
- The following settings indicate the state of a component or subcomponent:
  - Unchecked 
 —The item is not selected and will not be included in the distribution.
  - Checked 
 —The item is selected and will always be included in the distribution.
  - Asterisk 
 —The item is already included in the baseline distribution and therefore cannot be included in a patch distribution.

The following options apply to the package you select in the Packages list. These options are configurable only if the package is checked.

- Description 
 —The description of the selected package. This field also includes the section, maintainer, and installed version attributes.
- Package name 
 —The unique package name of the selected package.
- Package Dependency Level 
 —Configure how the selected package will be referenced by the deployed package. This setting has the following options:
  - Required Dependency 
 —The selected package must be installed before the deployment package can be installed. If you select the Repository or Package installer build output, packages with this dependency level will be included in the package distribution.
  - Recommended Dependency 
 —If the selected package is available in a registered feed on the test station computer, NI Package Manager will recommend that the package be installed, but allow the user to deselect the package. If you select the Repository or Package installer build output, packages with this dependency level will not be included in the package distribution.
  - Optional Dependency 
 —If the selected package is available in a registered feed on the test station computer, NI Package Manager will suggest that the package be installed, and the user can select it to be included. If you select the Repository or Package installer build output, packages with this dependency level will not be included in the package distribution.
- Version Requirements 
 —Configure the version of the selected package which is referenced by the deployment package. This setting has the following options:
  - Any Version 
 —Do not require a specific version.
  - Specific Version 
 —Require the exact version number specified in the Version control.
  - Greater Than 
 —The required package version must be greater than the version specified in the Version control.
  - Less Than 
 —The required package version must be less than the version specified in the Version control.
  - In Range 
 —The required package version must be in a specified version range. When you enable this option, a second version control is available to enter the maximum range.
- Version 
 —Specify the version number which is applied to the Version Requirements setting to determine the specified version of the package.
 Note 
 Two version values are available in the
 In Range version requirements
 option (Minimum and Maximum).
- Inclusive 
 —Specify whether the specified version number is valid. Available for the Greater Than, Less than, or In Range Options.

- Automatically include required packages 
 —Enable this option to include any NI drivers or other product packages that are required by LabVIEW, LabVIEW NXG, and LabWindows/CVI code modules in the deployment. Items you select in the packages list will also be included. This option also includes the necessary LabVIEW NXG, LabVIEW, and LabWindows/CVI runtime engines required to run the code modules.Required products are determined when you build the deployment, and are not shown. After you build the deployment, the deployment summary message specifies the required installers. Dependencies are included for modules only when you disable the
 Include without Processing Item or Dependencies 
 option on the Distributed Files tab.To detect required products for LabVIEW code modules, you must use LabVIEW 2013 or later when building the deployment. To detect required products for LabWindows/CVI code modules, you must build the code modules in LabWindows/CVI 2015 or later.
 Note 
 For LabWindows/CVI modules, the module-specific build settings specified in LabWindows/CVI determine whether the shared runtime or the side-by-side runtime is included. If the module was built with a newer runtime engine than the one currently installed on the system, the TestStand Deployment Utility will issue a warning.
- Only display runtime and user-built packages 
 —Enable this option to display only runtime packages and user-built packages in the Packages to Include control.
 Note 
 If you have selected a product hidden by this setting, the product will still be included in the distribution.
- Include Hardware Configuration from Measurement & Automation Explorer 
 —Enable this option to include the hardware configuration, and any drivers required by the configuration file, in the package distribution. This option is available only if you select the Package Installer or Repository Output type on the Mode tab. If you select the Package output type, this option is disabled.Once you execute the custom installer on a target computer, and the system reboots, the installer attempts to import Measurement & Automation Explorer (MAX) settings automatically.
 Note 
 If you cancel the import process or the import fails, you can manually import the new configuration file once you correct the problem. Restart the import process by selecting
 FileImport
 from the menu within MAX.
- Hardware Configuration File 
 —The hardware configuration file to include with the package distribution. Click
 Browse 
 to select another file or click
 New 
 to export a new configuration file.
 Note 
 This control is disabled when the Include Hardware Configuration from Measurement & Automation Explorer option is disabled.
- Measurement & Automation Explorer Import Options 
 —Specifies how the installer merges the configuration information you include in the deployment with the configuration data defined in MAX on the test station computer. The following options are available:
  - Merge 
 —Updates without deleting the existing configuration information in MAX. Select this option when you want to modify configuration information for certain devices but leave other device information unchanged.
  - Replace 
 —Overwrites all the existing configuration information in MAX. Select this option only when the new configuration file contains all the configuration information the test station computer requires. You typically do not use this option when you run more than one test system on a single test station computer.
  - Preserve 
 —Adds new configuration information without changing the existing configuration in MAX.

Note

The Configure Package Attributes dialog box contains the following options:

- Version Number 
 —Current software version number that NI Package Manager uses to determine the action to perform when a package is already installed on a computer on which you want to deploy a test system. Increment the version number when you change the contents of the installer to ensure that the package overwrites previous versions of the package that exist on the test station computer.
 Note 
 This control is disables when the Auto Increment option is enabled.
  - Auto Increment 
 —Indicates whether the deployment utility automatically increases the version number when you build a package to ensure the package upgrades previous versions of the package on the test station computer. This control is enabled by default. Enabling this control disables the Version control.
 Note 
 You must save the deployment before closing the deployment utility to reain the new version number.
  - Lock to Deployment Version 
 —Forces the package to use the same version number as the software version number the deployment utility uses to identify the deployment. If you enable this option, the Version option on the Mode tab determines the installer version number, and the deployment utility automatically increments the package version number each time you build the installer.
- Filter 
 —Determines which packages to display in NI Package Manager.
  - Runtime deployment packages only 
 —Displays only the runtime packages.
  - All visible packages 
 —Displays all user visible packages.
  - All packages (including hidden) 
 —Displays all packages, including hidden packages.
- Company 
 —Name of the company that manufactured the software. The company name is used along with the product name to generate the package name, which uniquely identifies a package.
- Product 
 —Name of the software product. The product name is used along with the company name to generate the package name, which uniquely identifies a package.
- Package Name 
 —Displays the generated package name for the product. This field cannot be configured, and is generated based on the Company and Product Name fields. NI Package Manager uses this field to uniquely identify packages.
- Package Category 
 —Configures the category for the package, which is shown in NI Package Manager in the category column. If you select Infrastructure, the package will be hidden by default in NI Package Manager.
- Package Synopsis 
 —A single line summary of the package.
- Description 
 —A detailed multi-line description of the package.
- Maintainer Name 
 —The person, organization, or company responsible for maintaining the package.
- Contact Email 
 —The email address used to contact the package maintainer.
- Homepage 
 —Specifies a URL that provides more information about the package.
- Custom License Agreement 
 —Specify a rich text file (*.rtf) containing a custom license agreement. When installing the package, the user will be prompted to read and accept this agreement.
- Include NI Certificates Package 
 —Enable this option to include the NI Certificates package in the package distribution, which reduces the number of prompts during installation of the package. This option applies only to the Repository and package Installer output types, and is disabled for the Single Package output type.
- Display in the Runtime Deployment Packages List 
 —Configures whether the package is shown in package builders, which only display runtime packages. Typically, you enable this for packages you intend to redeploy as a dependency of other packages.

#### See Also

[Advanced Installer Options dialog box](advanced-installer-options-dialog-box.html)

[Custom Commands dialog box](custom-commands-dialog-box.html)

[Deploying TestStand Systems](/csh?context=ts_10203)

[Drivers and Components dialog box](drivers-and-components-dialog-box.html)

Licensing Options for TestStand Systems
 section of Chapter 1,
 Introduction to TestStand
 , of the
 [Getting Started with TestStand](/csh?context=ts_8010)
 manual

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Package Distribution Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/deploy-library-edit-tab.html language=enus -->
## TOPIC 03580: Deploy Library Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/deploy-library-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/deploy-library-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Deploy Library step and select Edit Deploy Library or Step Settings from the context menu to display the Deploy Library edit tab in the TestStand Sequence Editor . Use the Deploy Library edit tab to deploy or undeploy to the local computer the shared variables defined in a LabVIEW project l

### Deploy Library Edit Tab

Insert a Deploy Library step and select
 Edit Deploy Library
 or
 Step Settings
 from the context menu to display the Deploy Library edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

deploy or undeploy to the local computer the shared variables

project library

packed project library

LabVIEW project

Note

- The project library or packed project library must contain only shared variables and cannot contain any VI files.
- TestStand cannot auto-deploy shared variables defined in a LabVIEW packed project library specified in a LabVIEW project or in a LabVIEW project library saved in an LLB specified in a LabVIEW project.
- TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the
 LabVIEW Help 
 for more information about deploying shared variables and NI-PSP URLs.
- National Instruments recommends that you do not use a Deploy Library step to deploy or undeploy shared variables when steps in different threads or executions might access the shared variables.
- If the test system execute VIs in the context
 
 of a LabVIEW project, you can enable the
 Auto Deploy Shared Variables on First Load of any VI in a Project 
 option and the
 Auto Undeploy Shared Variables on Last Unload of all VIs in a Project 
 option in the
 LabVIEW Adapter Configuration 
 dialog box to automatically deploy and undeploy shared variables defined in the LabVIEW project.

The Deploy Library edit tab contains the following options:

- Operation 
 —Specifies whether to deploy or undeploy the shared variables defined in a LabVIEW project library or LabVIEW packed project library.
- Library or Project Path 
 —The path of the project library file, LabVIEW project file, or packed project library file on the local computer to deploy or undeploy. The project library or packed project library must define only shared variables and cannot contain any VI files. If you specify a project file, TestStand deploys all shared variables defined in each project library file specified in the project.
- Specify Library Path by Expression 
 —Enable this option to specify that the library path is an expression the step evaluates at run time. Click the
 Expression Browse 
 button to build an expression. When you disable this option, you can use a literal string to specify the library path. Click the
 File Browse 
 button to select the project library file.

#### See Also

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[Deploying TestStand Systems](/csh?context=ts_10203)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

Parent topic:

Deploy Library Step - LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/deploy-library-step-configuration-dialog-box.html language=enus -->
## TOPIC 03581: Deploy Library Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/deploy-library-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/deploy-library-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Deploy Library in the context menu for the step to launch the Deploy Library Step Configuration dialog box from a TestStand User Interface . You can also click Configure Deploy Library on the General tab of the Step Properties dialog box. Use the Deploy Library Step Configuration di

### Deploy Library Step Configuration Dialog Box

Select
 Configure Deploy Library
 in the context menu for the step to launch the Deploy Library Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Deploy Library
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

deploy or undeploy to the local computer the shared variables

project library

packed project library

LabVIEW project

Note

- The project library or packed project library must contain only shared variables and cannot contain any VI files.
- TestStand cannot auto-deploy shared variables defined in a LabVIEW packed project library specified in a LabVIEW project or in a LabVIEW project library saved in an LLB specified in a LabVIEW project.
- TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the
 LabVIEW Help 
 for more information about deploying shared variables and NI-PSP URLs.
- National Instruments recommends that you do not use a Deploy Library step to deploy or undeploy shared variables when steps in different threads or executions might access the shared variables.
- If the test system execute VIs in the context
 
 of a LabVIEW project, you can enable the
 Auto Deploy Shared Variables on First Load of any VI in a Project 
 option and the
 Auto Undeploy Shared Variables on Last Unload of all VIs in a Project 
 option in the
 LabVIEW Adapter Configuration 
 dialog box to automatically deploy and undeploy shared variables defined in the LabVIEW project.

The Deploy Library Step Configuration dialog box contains the following options:

- Operation 
 —Specifies whether to deploy or undeploy the shared variables defined in a LabVIEW project library or LabVIEW packed project library.
- Library or Project Path 
 —The path of the project library file, LabVIEW project file, or packed project library file on the local computer to deploy or undeploy. The project library or packed project library must define only shared variables and cannot contain any VI files. If you specify a project file, TestStand deploys all shared variables defined in each project library file specified in the project.
- Specify Library Path by Expression 
 —Enable this option to specify that the library path is an expression the step evaluates at run time. Click the
 Expression Browse 
 button to build an expression. When you disable this option, you can use a literal string to specify the library path. Click the
 File Browse 
 button to select the project library file.

#### See Also

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[Deploying TestStand Systems](/csh?context=ts_10203)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Deploy Library Step - LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/deploy-library-step-labview-utility-step-type.html language=enus -->
## TOPIC 03582: Deploy Library Step - LabVIEW Utility Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/deploy-library-step-labview-utility-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/deploy-library-step-labview-utility-step-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploy Library Step Use a Deploy Library step to deploy or undeploy to the local computer the shared variables defined in a LabVIEW project library file or packed project library file, or to deploy or undeploy shared variables defined in LabVIEW project libraries within a selected LabVIEW project .

### Deploy Library Step - LabVIEW Utility Step Types

#### Deploy Library Step

Use a Deploy Library step to
 [deploy or undeploy to the local computer the shared variables](/csh?context=ts_tslabview_variable)
 defined in a LabVIEW
 [project library](/csh?context=ts_tslabview_lvlib)
 file or
 [packed project library](/csh?context=ts_tslabview_ppl)
 file, or to deploy or undeploy shared variables defined in LabVIEW project libraries within a selected
 [LabVIEW project](/csh?context=ts_tslabview_project)
 .

Note

- The project library or packed project library must contain only shared variables and cannot contain any VI files.
- TestStand cannot auto-deploy shared variables defined in a LabVIEW packed project library specified in a LabVIEW project or in a LabVIEW project library saved in an LLB specified in a LabVIEW project.
- TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the
 LabVIEW Help 
 for more information about deploying shared variables and NI-PSP URLs.
- If the test system execute VIs in the context
 
 of a LabVIEW project, you can enable the
 Auto Deploy Shared Variables on First Load of any VI in a Project 
 option and the
 Auto Undeploy Shared Variables on Last Unload of all VIs in a Project 
 option in the
 LabVIEW Adapter Configuration 
 dialog box to automatically deploy and undeploy shared variables defined in the LabVIEW project.
- National Instruments recommends that you do not use a Deploy Library step to deploy or undeploy shared variables when steps in different threads or executions might access the shared variables.

#### Configuring the Step

Use the
 [Deploy Library](deploy-library-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Deploy Library Step Configuration](deploy-library-step-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Deploy Library step. You cannot deploy shared variables to another computer running Microsoft Windows.

#### Step Properties

In addition to the common custom properties, the Deploy Library step type defines the following step properties:

- Step.Operation 
 —Specifies whether the step deploys or undeploys shared variables. Valid values are
 0 
 = Deploy and
 1 
 = Undeploy.
- Step.Libraries 
 —An expression for the path of the LabVIEW packed project library file, LabVIEW library file, or LabVIEW project file on the local computer to deploy to or undeploy from the target computer. The packed project library must define only shared variables and cannot contain any VI files.

#### See Also

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[Deploying TestStand Systems](/csh?context=ts_10203)

[Deploying VIs in LabVIEW Packed Project Libraries](/csh?context=ts_tslabview_ppl_deploy)

[LabVIEW Adapter Configuration dialog box](labview-adapter-configuration-dialog-box.html)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

Parent topic:

LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/dequeue-operation-queue-settings-edit-tab.html language=enus -->
## TOPIC 03583: Dequeue Operation - Queue Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/dequeue-operation-queue-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/dequeue-operation-queue-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Dequeue Operation Use the Dequeue operation to remove an element and/or store the data from an element. Enable the Dequeue option on the left of the Queue Settings panel. The Dequeue operation contains the following options: Queue Name or Reference Expression —The queue on which to perform the opera

### Dequeue Operation - Queue Settings Edit Tab

#### Dequeue Operation

Use the Dequeue operation to remove an element and/or store the data from an element. Enable the
 Dequeue
 option on the left of the Queue Settings panel.

The Dequeue operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option. Specify multiple queues with a string array containing the names of the queues or with an object reference array containing ActiveX references to the queues. When you specify multiple queues, the Dequeue operation dequeues an element from the first queue you specify that has an element available. To determine which queue the operation dequeues from, use the Which Queue control to specify a location to store the array offset of the queue.
- Location to Store Element (optional output) 
 —The location in which to store the queue element. The type of the location must be compatible with the data the element stores. Leave this control blank when you do not want to store the data. 
 The following tables illustrate the outcomes depending on the type of the data in the queue and the data type of the storage location. In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.
 Table 1.
 Dequeue Behaviors for Data You Enqueue by ValueDequeue Type—Destination
 Enqueue Type (By Value)—Source
 Simple Type
 Structured Type
 Object ReferenceSimple Type
 If the types match, Dequeue copies the data to the location you specify. If types do not match, Dequeue reports a type mismatch error.
 Type mismatch error.
 Type mismatch error.
 Structured Type
 Type mismatch error.
 Replaces the property you specify as the dequeue location with a copy of the structured value the queue stores.
 Type mismatch error.
 Object Reference
 Type mismatch error.
 Stores an ActiveX reference to the structured value the queue stores.
 Copies the ActiveX reference the queue stores to the location you specify. 
 Table 2.
 Dequeue Behaviors for Data You Enqueue by ReferenceDequeue Type—Destination
 Enqueue Type (By Reference)—Source
 Simple Type
 Structured Type
 Object ReferenceSimple Type
 If the types match, Dequeue copies the data to the location you specify. If types do not match, Dequeue reports a type mismatch error.
 Type mismatch error.
 Type mismatch error.
 Structured Type
 Type mismatch error.
 Makes a copy of the structured value the queue stores by reference, and replaces the property you specify as the dequeue location with the copy.
 Type mismatch error.
 Object Reference
 Stores an ActiveX reference to the simple type as it is stored in the queue.
 Stores an ActiveX reference to the structured value the queue stores.
 Stores an ActiveX reference to the ActiveX reference the queue stores.
- Dequeue From 
 —Specifies where in the queue to dequeue from. The options are Front of Queue and Back of Queue.
- Remove Element 
 —When you enable this option, the operation removes the element from the queue. When you do not enable this option, the operation retrieves the value of the element without removing it from the queue.
- Which Queue? (optional output) 
 —Use this control when you are dequeuing from multiple queues to specify a location to store the array offset of the queue on which the dequeue operation occurs. Refer to the description for the Queue Name or Reference Expression control for this operation for more information about dequeuing with multiple queues.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior when waiting to dequeue an element. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Queue Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/dequeue-operation-queue-step-configuration-di.html language=enus -->
## TOPIC 03584: Dequeue Operation - Queue Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/dequeue-operation-queue-step-configuration-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/dequeue-operation-queue-step-configuration-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Dequeue Operation Use the Dequeue operation to remove an element and/or store the data from an element. The Dequeue operation contains the following options: Queue Name or Reference Expression —The queue on which to perform the operation. You can specify the queue by name or by the object reference

### Dequeue Operation - Queue Step Configuration Dialog Box

#### Dequeue Operation

Use the Dequeue operation to remove an element and/or store the data from an element.

The Dequeue operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option. You can specify multiple queues using either a string array containing the names of the queues, or an object reference array containing ActiveX references to the queues. When you specify multiple queues, the Dequeue operation dequeues an element from the first queue you specify that has an element available. You can ascertain which queue the operation dequeues from by using the Which Queue control to specify a location to store the array offset of the queue.
- Location to Store Element (optional output) 
 —The location in which to store the queue element. Leave this control blank when you do not want to store the data. The type of the location must be compatible with the data the element stores. The following tables illustrate the outcomes depending on the type of the data in the queue and the data type of the storage location. In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.
 Table 3.
 Dequeue Behaviors for Data You Enqueue by ValueDequeue Type—Destination
 Enqueue Type (By Value)—Source
 Simple Type
 Structured Type
 Object ReferenceSimple Type
 If the types match, Dequeue copies the data to the location you specify. If types do not match, Dequeue reports a type mismatch error.
 Type mismatch error.
 Type mismatch error.
 Structured Type
 Type mismatch error.
 Replaces the property you specify as the dequeue location with a copy of the structured value the queue stores.
 Type mismatch error.
 Object Reference
 Type mismatch error.
 Stores an ActiveX reference to the structured value the queue stores.
 Copies the ActiveX reference the queue stores to the location you specify. 
 Table 4.
 Dequeue Behaviors for Data You Enqueue by ReferenceDequeue Type—Destination
 Enqueue Type (By Reference)—Source
 Simple Type
 Structured Type
 Object ReferenceSimple Type
 If the types match, Dequeue copies the data to the location you specify. If types do not match, Dequeue reports a type mismatch error.
 Type mismatch error.
 Type mismatch error.
 Structured Type
 Type mismatch error.
 Makes a copy of the structured value the queue stores by reference, and replaces the property you specify as the dequeue location with the copy.
 Type mismatch error.
 Object Reference
 Stores an ActiveX reference to the simple type as it is stored in the queue.
 Stores an ActiveX reference to the structured value the queue stores.
 Stores an ActiveX reference to the ActiveX reference the queue stores.
- Dequeue From 
 —Specifies where in the queue to dequeue from. The options are Front of Queue and Back of Queue.
- Remove Element 
 —When you enable this option, the operation removes the element from the queue. When you do not enable this option, the operation retrieves the value of the element without removing it from the queue.
- Which Queue? (optional output) 
 —Use this control to specify a location to store the array offset of the queue on which the dequeue operation occurs. Typically, you do not use this control unless you are dequeuing from multiple queues. Refer to the description for the Queue Name or Reference Expression control for this operation for more information about dequeuing with multiple queues.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior when waiting to dequeue an element. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Queue Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/describe-table-dialog-box.html language=enus -->
## TOPIC 03585: Describe Table Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/describe-table-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/describe-table-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Describe Table in the Table context menu in the Database Object View to launch the Describe Table dialog box, in which you can view the details of a table. The dialog box title displays the name of the table you select. The Describe Table dialog box includes a data grid that displays a list o

### Describe Table Dialog Box

Select
 Describe Table
 in the Table context menu in the
 [Database Object View](database-explorer.html)
 to launch the Describe Table dialog box, in which you can view the details of a table. The dialog box title displays the name of the table you select.

The Describe Table dialog box includes a
 [data grid](data-grid.html)
 that displays a list of all the columns in the selected table, and the data type, size, precision, and scale of each column. The grid also indicates the primary key and nullable columns.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/destination-edit-tab.html language=enus -->
## TOPIC 03586: Destination Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/destination-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/destination-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Destination edit tab in the TestStand Sequence Editor to specify the target for the Goto step. You cannot select an Else or Else If step as the target of a Goto Step. The Destination Step control contains a list of all steps in the step group, as well as the following three additional target

### Destination Edit Tab

Use the Destination edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify the target for the Goto step. You cannot select an Else or Else If step as the target of a Goto Step.

The Destination Step control contains a list of all steps in the step group, as well as the following three additional targets:

- <
 End Group
 > 
 —Jumps to the end of the current step group.
- <
 Cleanup
 > 
 —Jumps to the Cleanup step group.
- <
 Specify By Expression
 > 
 —Defines an expression that specifies a name or unique ID of a step. If the expression evaluates to a step name, the destination is the first step in the step group with the same name. If the expression evaluates to a step ID the destination is the first step in the sequence with the same unique step ID.

By default, Goto steps do not pass or fail. After a Goto step executes, TestStand sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Done
 or
 Error
 .

The Goto step type does not define any additional step properties other than the custom properties common to all steps.

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

Goto Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/diff-selected-threads-dialog-box.html language=enus -->
## TOPIC 03587: Diff Selected Threads Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/diff-selected-threads-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/diff-selected-threads-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Diff Selected Threads Dialog Box Use the Diff Selected Threads Dialog Box to view the differences in time taken by two different iterations of a set of operations on the same items. For example, you can compare operations from different test sockets to determine which operations differ in performanc

### Diff Selected Threads Dialog Box

#### Diff Selected Threads Dialog Box

Use the Diff Selected Threads Dialog Box to view the differences in time taken by two different iterations of a set of operations on the same items. For example, you can compare operations from different test sockets to determine which operations differ in performance between the sockets. To selectively compare operations that are within the same thread, such as for different UUTs run sequentially in the same socket, you must first isolate the operations to compare in new pretend threads using the
 [Move Selected Operations](move-selected-operations-dialog-box.html)
 dialog box before diffing the threads.

When you select
 OK
 , the Diff Selected Threads dialog matches the operations that use the same item in both threads, in chronological order. For each match, it reduces the length of the longer operation by the length of the shorter operation and sets the length of the shorter operation to zero. This removes the operation time that is common to both threads, leaving the excess operation time in the thread that took longer to execute the operation. You can then look for operations that take significantly longer in one thread vs. the other and also view how the differences in times are distributed between the threads. Because this dialog alters the timestamps of the events in the matching operations, you should consider saving a copy of your profile before performing a diff.

The dialog contains the following controls:

- Mark with color/Do not mark 
 —Specify whether to mark the matched operations with a selected color so that they are visually distinguished as a group.
- Move to Unique Threads 
 —Specifies whether to move the matched operations to new pretend threads with unique IDs
so that the matched operations are easily distinguished from the unmatched operations left in the original threads.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/diff-tab-select-files-dialog-box.html language=enus -->
## TOPIC 03588: Diff Tab - Select Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/diff-tab-select-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/diff-tab-select-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Diff Tab The Diff tab contains the following options: File 1 —File path of the first sequence file or type palette file you want to compare. File 2 —File path of the second sequence file or type palette file you want to compare. Click the Switch Files button to reorder the files. You must specify bo

### Diff Tab - Select Files Dialog Box

#### Diff Tab

The Diff tab contains the following options:

- File 1 
 —File path of the first sequence file or type palette file you want to compare.
- File 2 
 —File path of the second sequence file or type palette file you want to compare.

Click the
 Switch Files
 button to reorder the files.

You must specify both files before you can click
 OK
 .

Parent topic:

Select Files Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/differences-table-context-menu-teststand-file.html language=enus -->
## TOPIC 03589: Differences Table Context Menu - TestStand File Diff and Merge Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/differences-table-context-menu-teststand-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/differences-table-context-menu-teststand-file.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Differences Table Context Menu Click the Editing Options or Merging Options button or right-click a property in the Differences table to launch the Differences table context menu. The Differences table context menu contains the following options when you are comparing two files: Accept Changes From

### Differences Table Context Menu - TestStand File Diff and Merge Utility

#### Differences Table Context Menu

Click the
 Editing Options
 or
 Merging Options
 button or right-click a property in the Differences table to launch the Differences table context menu.

The Differences table context menu contains the following options when you are comparing two files:

- Accept Changes From Other File 
 —Accepts all the changes from the corresponding property in the other file to the selected file.
- Accept Value From Other File 
 —Accepts the value for the corresponding property in the other file to the selected file.
- Apply Changes To Other File 
 —Applies all the changes within the selected property from the selected file to the other file.
- Clear Attributes 
 —Deletes all the attributes from the selected property. This option is available when the TestStand File Diff and Merge utility marks an Attributes element as an insertion.
- Copy Attributes From Other File 
 —Copies the attributes from the other file to the selected file. This option is available when you the selected property does not contain any attributes.
- Copy Item From Other File 
 —Copies the array element from the other file to the selected file. This option is available when the selected array element does not existing in the selected file. The utility inserts the array element at the end of the array in the selected file.
- Copy Property From Other File 
 —Copies the property from the other file to the selected file. This option is available when the selected property does not exist in the selected file.
- Copy Value To Other File 
 —Copies the value of the selected property from the selected file to the other file. This option is available for properties with a value the utility marks as changed.
- Delete Item In This File 
 —Deletes the selected array element from the selected file. This option is available only when the utility marks an array element as an insertion in the selected file.
- Delete Property In This File 
 —Deletes the selected property from the selected file. This option is available when the utility marks the property as an insertion in the selected file.
- Edit Value 
 —Launches a dialog box in which you can edit the value of the element. Depending on the element, this option launches the
 Array Bounds 
 dialog box,
 Attributes 
 dialog box,
 Edit Flags 
 dialog box,
 Numeric Format 
 dialog box, or
 View Change Details 
 dialog box.
- Launch External Diff Tool 
 or
 Launch External Merge Tool 
 —Launches the external tool specified on the External Diff/Merge Tool tab of the
 File Differ Options 
 dialog box for the selected string property or comment. The TestStand File Diff and Merge utility displays a cancelable waiting dialog box until you exit the external tool.
- Goto Location 
 —Opens the file and locates the property in the file. If you select this option in the Merged column and complete any edits to the merged file, the utility does not reload the merged file.

The Differences table context menu contains the following options when you are comparing three files:

- Accept From <
 base filename
 > 
 —Accepts all the changes within the selected property from the base file to the merged file.
- Accept Change From <
 filename
 > 
 —Accepts all the changes within the selected property from the selected file to the merged file.
- Goto Location 
 —Opens the file and locates the property in the file. If you select this option in the Merged column and complete any edits to the merged file, the utility does not reload the merged file.
- Use Custom Change 
 —Launches a dialog box in which you can edit the value of the element. Depending on the element, this option launches the Edit Flags dialog box, Numeric Format dialog box, or View Change Details dialog box.

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[File Differ Options dialog box](file-differ-options-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

[View Change Details dialog box](view-change-details-dialog-box.html)

Parent topic:

Differences Table - TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/differences-table-teststand-file-diff-and-mer.html language=enus -->
## TOPIC 03590: Differences Table - TestStand File Diff and Merge Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/differences-table-teststand-file-diff-and-mer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/differences-table-teststand-file-diff-and-mer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Differences Table The Differences table of the TestStand File Diff and Merge utility displays the property differences grouped by sequences, file global variables, file properties, and types for each specified file. The Differences table contains the following columns: Item —The union of all the pro

### Differences Table - TestStand File Diff and Merge Utility

#### Differences Table

The Differences table of the TestStand File Diff and Merge utility displays the property differences grouped by sequences, file global variables, file properties, and types for each specified file. The Differences table contains the following columns:

- Item 
 —The union of all the properties grouped by sequences, file global variables, file properties, and types for the files you are comparing. If an item moved to a different location in another file, click the
 Go To And Select Matching Moved Step 
 button to select the matching properties in each file.
- Base 
 —List of all the properties in the base file. This column is available only when you are comparing three files.
- File 1 
 —List of all the properties in the first file you select to compare.
- File 2 
 —List of all the properties in the second file you select to compare.
- Merged 
 —List of all the properties in the merged file. This column is available only when you are comparing three files.

For a property that has a difference, the property uses the same background color as the File column in the
 [file list](file-list-teststand-file-diff-and-merge-utili.html)
 . The property text displays differently depending on the type of difference the property represents, such as conflict, insertion, deletion, or ignored change. The utility
 [status bar](status-bar-teststand-file-diff-and-merge-util.html)
 contains a key that shows how the Differences table represents conflicts, insertions, deletions, or ignored changes.

For a property that has a difference when comparing two files, click the
 Editing Options
 button in the appropriate column and select an option from the
 [context menu](differences-table-context-menu-teststand-file.html)
 for accepting the difference from the other file. When comparing three files, click the
 Merging Options
 button in the Merged column and select an option from the context menu to manually select which version you want to accept in the final merged file. The background color of the Merged column changes depending on which version you accept.

Use the breadcrumb at the top of the Differences table to navigate the hierarchy of the properties you select.

Note

type attached to a file

TypeUsageList

#### See Also

[File List](file-list-teststand-file-diff-and-merge-utili.html)

[Status Bar](status-bar-teststand-file-diff-and-merge-util.html)

[TypeUsageList](../tsapiref/typeusagelist.html)

[TypeUsageList.GetIsTypeAttachedToFile](../tsapiref/typeusagelist-getistypeattachedtofile.html)

[TypeUsageList.SetIsTypeAttachedToFile](../tsapiref/typeusagelist-setistypeattachedtofile.html)

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/disable-properties-tab-step-type-properties-d.html language=enus -->
## TOPIC 03591: Disable Properties Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/disable-properties-tab-step-type-properties-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/disable-properties-tab-step-type-properties-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disable Properties Tab Use the Disable Properties tab to prevent sequence developers from modifying the settings of built-in instance step type properties in individual steps. Each option on the Disable Properties tab represents one built-in instance property or a group of built-in instance properti

### Disable Properties Tab - Step Type Properties Dialog Box

#### Disable Properties Tab

Use the Disable Properties tab to prevent sequence developers from modifying the settings of built-in instance step type properties in individual steps. Each option on the Disable Properties tab represents one built-in instance property or a group of built-in instance properties. When you enable an option, you prevent sequence developers from modifying the value of the corresponding property or group of properties for all step instances.

Note

Apply Changes in this Dialog Box to all Loaded Steps of this Type

Most of the options on the Disable Properties tab apply to a specific control in the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane or in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. The following items describe two exceptions—the Specify Module option and the Preconditions option.

- Specify Module 
 —If you enable this option, the sequence developer cannot access the
 Module 
 tab of the
 Step Settings 
 pane or in the
 Specify Module 
 dialog box on any steps that use the step type. You typically prevent the sequence developer from specifying the module for step types that do not call
 code modules 
 . For example, a sequence developer cannot specify a module for Statement steps. Refer to Chapter 3,
 Editing Steps in a Sequence 
 , of the
 Getting Started with TestStand 
 manual for more information about specifying a module adapter call for a step type.

If you disable the Specify Module option but enable the Edit Module Prototype option, a sequence developer can view the Specify Module dialog box but cannot modify any of the parameter information in the dialog box.

- Precondition 
 —If you enable this option, a sequence developer cannot edit preconditions for steps that use the step type.

#### See Also

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/distributed-files-tab-teststand-deployment-ut.html language=enus -->
## TOPIC 03592: Distributed Files Tab - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/distributed-files-tab-teststand-deployment-ut.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/distributed-files-tab-teststand-deployment-ut.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Distributed Files Tab Use the Distributed Files tab to view the list of files you specified to include in the deployment on the System Source tab, configure the installer destination location and settings for each file, and specify options for deploying LabVIEW files. This tab is not available when

### Distributed Files Tab - TestStand Deployment Utility

#### Distributed Files Tab

Use the Distributed Files tab to view the list of files you
 [specified to include in the deployment](/csh?context=ts_tsdeploysystem_customizecomponents)
 on the
 [System Source](system-source-tab-teststand-deployment-utilit.html)
 tab, configure the installer destination location and settings for each file, and specify options for deploying LabVIEW files.

Note

- This tab is not available when you disable the
 From TestStand Workspace File 
 and
 From TestStand Public Directories 
 options on the
 System Source 
 tab or when you create a
 patch 
 deployment and select
 None 
 in the
 User Files to Include 
 option on the
 Mode 
 tab.
- The options on this tab apply only to the
 type of deployment 
 you create. Changing the type of deployment might change the options available on this tab.

The Distributed Files tab contains the following options:

- Distributed Files 
 —The files the system includes.
 Note 
 The string
 <SubVIs: Save to
 destination
 >
 as part of the item text in the Distributed Files list always denotes subVIs. You can change the location the subVIs are saved to using the SubVI Location option on the
 [LabVIEW VI Options](labview-vi-options-dialog-box.html)
 dialog box. 
 The Distributed Files context menu contains the following options: 
 
 Note 
 The Distributed Files context menu options are disabled if the files do not exist, such as if the image directory is changed or if source files are moved.
  - Copy Source Path 
 —Copies the source path for the selected file. If the selected file is a file in the destination directory then it will copy the path of the source file used when the image was created.
  - Browse to Source Path 
 —Opens the selected file in Windows Explorer. If the selected file is a file in the destination directory then it will open the source file used when the image was created.
  - Copy Destination Path 
 —Copies the destination path for the selected file. If the selected file is a top-level source file then it will copy the destination where the file will go in the current deployment.
  - Browse to Destination Path 
 —Opens the selected file in Windows Explorer. If the selected file is a top-level source file then it will browse to the destination where the file will go in the current deployment.
- View 
 —Specifies how the distributed files are displayed. You can display the files with the following views:
  - View Workspace 
 —Displays the files as they appear in the workspace.
  - View Source 
 —Displays the source of the files on the development computer. Use this view to
 exclude files 
 from the full deployment.
  - View Build Preview 
 —Displays the destination for the files on the test station computer. Use this view to
 exclude files 
 from the full deployment or to modify the Installation Destination Subdirectory control to change the destination for top-level files in the directory.
 When you create a patch deployment, this view displays a list of the files included in the destination from the previous deployment and indicates the modification state of the file, such as
 Unknown 
 ,
 Not modified 
 ,
 Modified 
 ,
 New 
 ,
 Dependency 
 , or
 No longer required 
 . The modification state reflects the state of the source version of the file. Changes you make to the file during deployment might mean that the deployment utility includes in the patch deployment a file that has not been modified or excludes a modified file from the patch deployment. For example, if you add a file to a LabVIEW project but the file is not part of the deployed test system, the modification state of the file you added to the project is
 New 
 , but the deployment utility removes the unused file and does not include it in the patch deployment. Use the
 Build Status 
 tab of the deployment utility or the status log text files to determine which files the utility adds to the patch deployment and why the files were required.
  - View Dependency Destination 
 —Displays the destination of files the deployment utility created in the image directory of the dependency deployment. This read-only view is available only when you create a patch deployment.
  - View Previous Build Destination 
 —Displays the destination of the files the deployment utility created in the image directory of the previous deployment. This read-only view is available only when you create a patch deployment.
- File Properties tab 
 —Contains the following options:
  - File Status 
 —The file inclusion status for files in the deployment. Contains the following options:
    - Include in Patch if Required 
 —Includes new or modified files from the previous full or baseline patch deployment.
    - Force Include in Patch 
 —Always includes the file in the patch deployment, regardless of modification state.
    - Do not Include in Patch 
 —Does not include the file in the patch deployment. This option is available only when the top-level file is not modified or new or when you select
 Manual Mode 
 in the
 User Files to Include 
 control on the
 Mode 
 tab. You must always include dependencies.
    - Remove from Deployed System 
 —Deletes the file in the full deployment if it is no longer a dependency. This option is available only when you create a full deployment.
 Note 
 You cannot use a patch deployment to delete files from a deployed test system. You must create a full deployment to remove top-level files from a deployed test system.
  - Source Path 
 —The path of the selected file. This option is disabled when there is no file selected in the Distributed Files list.
  - Replacement Path 
 —The path of the file to use to replace the selected file. This option is enabled only when you create a patch deployment and select
 Manual Mode 
 in the
 User Files to Include 
 option on the Mode tab. This option is also enabled if you select the environment file that you specified in the
 Active Environment File 
 field on the
 System Source 
 tab, and you enable the
 Determine File Destinations Using Environment File 
 option. If you replace the active environment file with another environment file, the paths specified in the replacement file are used to determine the destination of deployed files.
  - Include without Processing Item or Dependencies 
 —When you enable this option, the deployment utility copies the selected file to the deployment image directory without any additional processing during the build.
 Note 
 You must ensure the files work correctly without modifications. The deployment utility does not attempt to find or include any dependencies of the file during analysis. 
 You must ensure the LabVIEW Run-Time Engine can run the VIs for which you enable this option. The deployment utility does not attempt to determine if VIs with this setting are broken but does check for broken VIs in the image directory after copying the VIs to warn you if VIs you do not process break processed code modules.
 The deployment utility returns a warning if it includes a file in a deployment image directory as a dependency and you enabled the Include without Processing Item or Dependencies option for the file.
  - Include All Files in LabVIEW Project 
 —When you enable this option, the deployment utility analyzes the specified LabVIEW project and lists all project files in the
 Distributed Files 
 control after analysis. If you do not enable this option, the
 Distributed Files 
 control lists only the project files that are called by sequence files in the deployment. This option is available only when you select a LabVIEW project in the
 Distributed Files 
 control. 
 When you enable this option for a LabVIEW project and select
 View Source 
 from the
 View 
 ring control on the Distributed Files tab, files appear as children of the LabVIEW project to which they belong. You can choose whether or not to include project files in the deployment by selecting or deselecting them in the
 Distributed Files 
 control. When you select
 View Build Preview 
 from the
 View 
 ring control on the Distributed Files tab, you can select the destination for the LabVIEW project, which determines the destination for all the files in the project.
 Note 
 Packed project libraries the deployment utility creates with LabVIEW 2011 or later always include all the files in a LabVIEW project.
  - Installer Properties 
 —Contains the following options:
    - Installation Destination 
 —Specifies a directory Microsoft Windows or National Instruments defines on the test station computer, such as the
 <Program Files> 
 directory or the
 <TestStand> 
 directory, to which the deployment utility copies the selected files. You can select from several
 installation destination options 
 . This option is dimmed when there is no file selected in the Distributed Files list.
By default, the
 deployment utility installs 
 files on the test station computer to the same location in which the file exists on the development computer. Use the Installation Destination option to install a file to a different location on the test station computer. For example, you can install custom configuration files for test station computer operators that are different from the configuration files test system developers use. You can save the custom configuration files for operators in a directory other than the default TestStand configuration directory on the development computer but install the files in the default TestStand configuration directory on the test station computer.
    - Installation Destination Subdirectory 
 —A subdirectory under the installation destination. This option is dimmed when there is no file selected in the Distributed Files list.
By default, the deployment utility installs files on the test station computer to the same location in which the file exists on the development computer. Use the Installation Destination Subdirectory option to install a file to a different location on the test station computer. For example, you can install custom configuration files for test station computer operators that are different from the configuration files test system developers use. You can save the custom configuration files for operators in a directory other than the default TestStand configuration directory on the development computer but install the files in the default TestStand configuration directory on the test station computer.
 Note 
 The deployment utility returns an error when a temporary path includes "
 .lvlibp
 ". You must disable the
 Output VIs to Packed Project Library
 option in the
 [LabVIEW VI Options](labview-vi-options-dialog-box.html)
 dialog box, change the
 Installation Destination
 option (and/or the
 Installation Destination Subdirectory
 option) on the Distributed Files tab of the TestStand Deployment Utility, enable the
 Output VIs to Packed Project Library
 option in the LabVIEW VI Options dialog box, and rebuild the deployment to resolve the error.
    - Register as ActiveX Server 
 —When you enable this option, the installer you build with the deployment utility registers the file you select as an ActiveX Automation server. Register ActiveX server executables or DLLs so that client applications on the test station computer can find the files. This option is dimmed when there is no file selected in the Distributed Files list.
 Note 
 This option is not available for package-based distributions.
    - Force File to Install 
 —Enabling this option overrides the
 default installer behavior 
 and always overwrites existing files on the test station computer with the files the installer includes. For example, you can overwrite the existing
 GeneralEngine.cfg 
 file on the test station computer with an updated version you include in the installer.
 Notice 
 When you use this technique, an installer can replace a newer version of a file with an older version of a file, which can be problematic with DLLs because components on the computer might rely on functionality available only in the newer version of the DLL and might break when the installer downgrades the DLL. To avoid this issue, create a later version of the file with the changes you want and include the file in the installer you build with the deployment utility to overwrite only earlier versions of the file. 
 Note 
 When you create a full deployment, the deployment utility disables this option for all files by default. When you create a patch deployment, the deployment utility enables this option for all files by default. If you manually enable or disable this option in a full deployment or in a patch deployment, the deployment utility applies the new setting to both types of deployment for all future deployments that include the selected file. 
 Note 
 This option is not available for package-based distributions. 
 This option is dimmed when you have not selected a file in the Distributed Files control.
    - Create Program Item 
 —When you enable this option, the deployment utility installer creates a Microsoft Windows Start menu item in the group that you specify in the Start Menu Item Group option on the Installer Options tab. For example, you can create a start menu item for a user interface. This option is dimmed when no file is selected in the Distributed Files list.
 Note 
 (Windows 8.1) When you install on Windows 8.1, you might need to right-click the Start screen and select
 All apps
 to locate the program item you created. You can pin the program item to the Start screen or Taskbar by right-clicking the program item and selecting
 Pin to Start
 or
 Pin to Taskbar
 , respectively. 
 Note 
 This option is not available for package-based distributions.
    - Shortcuts 
 —Launches the
 Shortcuts 
 dialog box, in which you can specify shortcuts for the deployment utility installer to create in multiple directories for the file you select. For example, you can create a shortcut to a user interface on the desktop and in the start menu.
- Call Hierarchy tab 
 —Contains a tree view of the selected file and all its callers.
- Analyze Source Files 
 —Causes the deployment utility to analyze the workspace and files in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components 
 ,
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \CodeTemplates 
 , and
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \TestStand
 version
 \UserInterfaces 
 directories.
- Expand All 
 —Expands all items in the Distributed Files list.
- Collapse All 
 —Collapses all items in the Distributed Files list.
- Add Patch File 
 —Adds a file to the patch deployment. This option is available only when you create a patch deployment and select
 Manual Mode 
 in the
 User Files to Include 
 option on the Mode tab.
 Note 
 You cannot add a new file with the same name and destination as a file already included in the deployment. To add the new file in this case, you must move the existing file to a new destination in the deployment. To replace a file that already exists in the deployment, select the file and use the Replacement Path control.
- Remove Patch File 
 —Removes the selected file from the deployment. This option is available only for files you added using the
 Add Patch File 
 button.
- LabVIEW Options 
 —Launches the
 LabVIEW VI Options 
 dialog box, which contains options specific to LabVIEW VIs.

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEW VI Options dialog box](labview-vi-options-dialog-box.html)

[Patching Deployments](/csh?context=ts_tsdeploysystem_createpatch)

[Shortcuts dialog box](shortcuts-dialog-box.html)

Parent topic:

TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/distributions-needed-dialog-box-teststand-dep.html language=enus -->
## TOPIC 03593: Distributions Needed Dialog Box - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/distributions-needed-dialog-box-teststand-dep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/distributions-needed-dialog-box-teststand-dep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TestStand Deployment Utility launches the Distributions Needed dialog box when you attempt to build an installer that includes additional drivers or components that the deployment utility cannot find. The dialog box lists the distributions required to build the installer and requests access to t

### Distributions Needed Dialog Box - TestStand Deployment Utility

The TestStand Deployment Utility launches the Distributions Needed dialog box when you attempt to build an installer that includes additional drivers or components that the deployment utility cannot find. The dialog box lists the distributions required to build the installer and requests access to these distributions.

The Distributions Needed dialog box contains the following options:

- Yes 
 —Select
 Yes 
 when you have access to the distribution, and navigate to the location of the distribution.
- No 
 —Select
 No 
 when you do not have access to the distribution. The deployment utility then searches for other distributions that might contain the required components. If the deployment utility does not find distributions that contain the required components, the deployment utility launches the No More Distributions dialog box. If the deployment utility finds distributions that include one or more of the required products, the deployment utility launches the All Distributions dialog box.

#### All Distributions Dialog Box

The All Distributions dialog box lists all known distributions that contain one or more of the products required to build the installer. Select the distributions that you can access and click
 OK
 to navigate to their original installation locations.

#### No More Distributions Dialog Box

The No More Distributions Dialog Box indicates that no known distributions contain the products required to build the installer.

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

Installer Options Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/dll-source-code-files-window.html language=enus -->
## TOPIC 03594: DLL Source Code Files Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/dll-source-code-files-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/dll-source-code-files-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Source Code Files button on the C/C++ DLL Module tab to launch the DLL Source Code Files window. The DLL Source Code Files window contains the following options: Create and Edit Code in Text File —Select this option when you want the C/C++ DLL Adapter to create and edit code using the defa

### DLL Source Code Files Window

Click the
 Source Code Files
 button on the
 [C/C++ DLL Module](c-c-dll-module-tab.html)
 tab to launch the DLL Source Code Files window.

The DLL Source Code Files window contains the following options:

- Create and Edit Code in Text File 
 —Select this option when you want the C/C++ DLL Adapter to create and edit code using the default application Microsoft Windows associates with the file extension. When you select this option, you can only specify the source file containing the function.
- Create and Edit Code in Visual Studio 
 —Select this option when you want the C/C++ DLL Adapter to create and edit code using a fully integrated interface with Microsoft Visual Studio. When you select this option, you must specify the source file and project file that contains the function. Optionally, you can also specify a Visual Studio solution file.
- Source File that Contains Function 
 —The pathname of the source file. You must specify an existing source file when creating code in Visual Studio. When you want to create a new source file in a text file, you must enter an absolute pathname. When you are using an existing source file, you can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand
 search directory paths 
 . Use the
 Edit Search Directories 
 dialog box to customize the search directory paths.
- Visual Studio Project File 
 —The pathname of the project file. You must specify an existing project file. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.
- Visual Studio Solution File (optional) 
 —The pathname of the solution file. You must specify an existing solution file. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.

#### See Also

[C/C++ DLL Module Tab](c-c-dll-module-tab.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

Parent topic:

C/C++ DLL Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/dmm-step.html language=enus -->
## TOPIC 03595: Dmm Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/dmm-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/dmm-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an IVI Dmm step to perform single-point and multipoint measurements using digital multimeters. Configuring the Step Use the Edit IVI Dmm Step dialog box in the TestStand Sequence Editor and in a TestStand User Interface to configure the IVI Dmm step. Step Operations The IVI Dmm step type support

### Dmm Step

Use an IVI Dmm step to perform single-point and multipoint measurements using digital multimeters.

#### Configuring the Step

Use the
 [Edit IVI Dmm Step](edit-ivi-dmm-step-dialog-box3.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the IVI Dmm step.

#### Step Operations

The IVI Dmm step type supports the following operations:

- Configure 
 —Configures the instrument to match the state the step specifies.
- Show Soft Front Panel 
 —Displays the soft front panel (SFP) for the instrument.
- Hide Soft Front Panel 
 —Hides the SFP for the instrument.
- Read 
 —Initiates and returns a measurement from the instrument.
- Initiate 
 —Initiates a measurement.
- Fetch 
 —Returns a measured value from a measurement the Initiate operation has started.
- Abort 
 —Cancels the wait for a trigger.
- Send Software Trigger 
 —Sends a software trigger command to trigger the instrument.
- Get Information 
 —Retrieves low-level status and information from the instrument.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the IVI Dmm step type defines the following step properties:

- Step.Result.Reading 
 —The measurement values for the Read and Fetch operations. The property data type is NI_IviSinglePoint or NI_IviWave.
- Step.LogicalName 
 —The logical name expression.
- Step.InstrOperation 
 —A value that specifies the operation you configured the step to perform.
- Step.SettingsSource 
 —The name of the property or variable where the step loads and stores the settings for the operation.
- Step.Configuration 
 —The settings for the
 Configure 
 operation. The data type of this property is NI_IviDmmConfig.
- Step.SoftFrontPanel 
 —The settings for the
 Show Soft Front Panel 
 operation. The data type of this property is NI_IviSoftFrontPanel.
- Step.Readings 
 —The settings for the
 Read 
 and
 Fetch 
 operations.
- Step.GetInfo 
 —The settings for the
 Get Information 
 operation.

#### See Also

[IVI Step Types](ivi-step-types.html)

Parent topic:

IVI Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/do-while-step.html language=enus -->
## TOPIC 03596: Do While Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/do-while-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/do-while-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Do While step to define a block of steps that execute once and then repeatedly while a condition is True . Configuring the Step Use the DoWhile Loop edit tab in the TestStand Sequence Editor and the Configure Do While Loop dialog box in a TestStand User Interface to configure the Do While step

### Do While Step

Use a Do While step to define a block of steps that execute once and then repeatedly while a condition is
 True
 .

#### Configuring the Step

Use the
 [DoWhile Loop](dowhile-loop-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Do While Loop](configure-do-while-loop-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Do While step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Do While step type defines the following step property:

- Step.CustomExpr 
 —The expression the step evaluates before executing the steps within the block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/dowhile-loop-edit-tab.html language=enus -->
## TOPIC 03597: DoWhile Loop Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/dowhile-loop-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/dowhile-loop-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DoWhile Loop edit tab in the TestStand Sequence Editor to configure the Do While step. The DoWhile Loop edit tab contains the following option: Loop Condition —The expression the step evaluates after executing steps within the block the first time. If the expression evaluates to True , execu

### DoWhile Loop Edit Tab

Use the DoWhile Loop edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the Do While step.

The DoWhile Loop edit tab contains the following option:

- Loop Condition 
 —The expression the step evaluates after executing steps within the block the first time. If the expression evaluates to
 True 
 , execution proceeds to the first step in the block again. If the expression evaluates to
 False 
 , the loop ends and execution proceeds to the End step for the While block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Do While Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/drivers-and-components-dialog-box.html language=enus -->
## TOPIC 03598: Drivers and Components Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/drivers-and-components-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/drivers-and-components-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the TestStand Deployment Utility and click Drivers and Components on the Installer Options tab to launch the Drivers and Components dialog box, in which you can include additional National Instruments installer components in the installer. If the Drivers and Components dialog box does not lis

### Drivers and Components Dialog Box

TestStand Deployment Utility

Drivers and Components

Installer Options

Note

type of deployment

The Drivers and Components dialog box contains the following options:

- Components to Include 
 —Lists the additional installer components you can include. To include or exclude a component, enable or disable the corresponding option. Some components may include optional subcomponents, which you can deselect to reduce the size of the distribution. When you select a component, all subcomponents are included by default.
 Note 
 Some subcomponents may be included in more than one component. When you deselect one of these subcomponents, it will be excluded from all other parent components. 
 The following settings indicate the state of a component or subcomponent:
 
 Note 
 The
 [additional NI installer(s) you have selected to include in the installer](/csh?context=ts_tsdeploysystem_includeinstallers)
 contain only the features currently installed on this computer and, therefore, might not be complete copies of the original product(s).
  - Unchecked 
 —The item is not selected and will not be included in the distribution.
  - Checked 
 —The item is selected and will always be included in the distribution.
  - Partially Checked 
 —The item is required by another component in the distribution. Select the item and view the Description field for more information about why the item is required.
  - Asterisk 
 —The item is already included in the baseline distribution and therefore cannot be included in a patch distribution.
- Install Type 
 —The different types of installs available for the selected component. Examples of install types are full and run time. This control is disabled when only one install type for the selected component exists.
- Description 
 —The description of the selected component. If a component is required by another item in the distribution, this field indicates the reason.
- Distribution Title 
 —The title of the product deployment that contains the selected component.
- Installer Source Location 
 —The path to the installer for the selected component. This is the root directory of the location from which you installed the product, usually on a DVD, CD, or network drive. Click
 Browse 
 to select a different installer location for the selected product.
- Automatically include required installers 
 —Enable this option to include any NI drivers or other products that are required by LabVIEW, LabVIEW NXG, and LabWindows/CVI code modules in the deployment. Items you select in the installer tree will also be included. This option also includes the necessary LabVIEW, LabVIEW NXG and LabWindows/CVI runtime engines required to run the code modules.
 Required products are determined when you build the deployment, and are not shown in the Additional Components tree. After you build the deployment, the deployment summary message specifies the required installers. Dependencies are included for modules only when you disable the
 Include without Processing Item or Dependencies 
 option on the
 Distributed Files 
 tab.
 To detect required products for LabVIEW code modules, you must use LabVIEW 2013 or later when building the deployment. To detect required products for LabWindows/CVI code modules, you must build the code modules in LabWindows/CVI 2015 or later.
 Note 
 For LabWindows/CVI modules, the module-specific build settings specified in LabWindows/CVI determine whether the shared runtime or the side-by-side runtime is included. If the module was built with a newer runtime engine than the one currently installed on the system, the TestStand Deployment Utility will issue a warning.
- Total Disk Cost 
 —The estimated size of all additional installers included in the distribution. This estimate does not consider the size of files you include in the deployment. For patch distributions, this estimate considers only components to be included in the patch itself.
- To minimize media prompts while building your installers, copy the selected installers and all future installers to this computer 
 —Enable this option to copy all necessary components from a deployment to a permanent location on the local computer before the deployment utility builds the deployment, and to copy all National Instruments installers from a deployment to a permanent location on the local computer when you run the installers.
- Only display runtime installers 
 —Enable this option to display only runtime products in the Components to Include control.
 Note 
 If you have selected a product hidden by this setting, the product will still be included in the distribution. In this instance, a warning indicates that some included products are not displayed.
- Include Hardware Configuration from Measurement & Automation Explorer 
 —Enable this option to include the hardware configuration, and any drivers required by the configuration file, in the installer. The Components to Include control indicates any required drivers.
 Once you execute the custom installer on a target computer, and the system reboots, the installer attempts to import Measurement & Automation Explorer (MAX) settings automatically. In many cases, this process occurs silently. However, certain configurations and import conditions require you to complete the import interactively using the following guidelines: 
 
 Note 
 If you cancel the import process or the import fails, you can manually import the new configuration file once you correct the problem. Restart the import process by selecting
 File»Import
 from the menu within MAX.
  - If the installer includes an NI device driver and you recently installed hardware on the target computer, you must complete the Add Hardware Wizard on the Microsoft Windows Control Panel before you import the MAX settings. The import process prompts you to wait until the Add Hardware Wizard completes before you proceed with the import.
  - If the installer is upgrading an existing NI device driver and the hardware was previously installed and operating properly on the target computer, the import process must complete automatically. The installer does not prompt you to complete the Add Hardware Wizard.
  - If the MAX import process encounters a conflict between the settings in your configuration file and the settings in the configuration file currently on the target computer, the installer prompts you to complete the import process interactively to resolve these differences.
- Hardware Configuration File 
 —The hardware configuration file to include with the installer. Click
 Browse 
 to select another file or click
 New 
 to export a new configuration file.
 Note 
 This control is disabled when the Include Hardware Configuration from Measurement & Automation Explorer option is disabled.
- Measurement & Automation Explorer Import Options 
 —Specifies how the installer merges the configuration information you include in the deployment with the configuration data defined in MAX on the test station computer
 
 . The following options are available:
  - Merge 
 —Updates without deleting the existing configuration information in MAX. Select this option when you want to modify configuration information for certain devices but leave other device information unchanged.
  - Replace 
 —Overwrites all the existing configuration information in MAX. Select this option only when the new configuration file contains all the configuration information the test station computer requires. You typically do not use this option when you run more than one test system on a single test station computer.
  - Preserve 
 —Adds new configuration information without changing the existing configuration in MAX.
- Display Dialog During Import 
 —When you enable this option, MAX launches a dialog box when the installer imports the hardware configuration file.

Note

ni.com

#### See Also

[TestStand Deployment Utility](teststand-deployment-utility.html)

[Distributions Needed Dialog Box](distributions-needed-dialog-box-teststand-dep.html)

[Including Additional NI Installers](/csh?context=ts_tsdeploysystem_includeinstallers)

Uninstalling a TestStand Deployment

Parent topic:

Installer Options Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/early-unlock-operation-lock-settings-edit-tab.html language=enus -->
## TOPIC 03599: Early Unlock Operation - Lock Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/early-unlock-operation-lock-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/early-unlock-operation-lock-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Early Unlock Operation To release the lock before the lock operation lifetime expires, insert a Lock step to perform the Early Unlock operation. Enable the Early Unlock option on the left of the Lock Settings panel. The Early Unlock operation contains the following option: Lock Name or Reference Exp

### Early Unlock Operation - Lock Settings Edit Tab

#### Early Unlock Operation

To release the lock before the lock operation lifetime expires, insert a Lock step to perform the Early Unlock operation. Enable the
 Early Unlock
 option on the left of the Lock Settings panel.

The Early Unlock operation contains the following option:

- Lock Name or Reference Expression 
 —The lock on which to perform the operation. You can specify the lock by name or by the object reference you receive when you create the lock using the Use Object Reference for the Lock Reference Lifetime option.

Parent topic:

Lock Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/early-unlock-operation-lock-step-configuratio.html language=enus -->
## TOPIC 03600: Early Unlock Operation - Lock Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/early-unlock-operation-lock-step-configuratio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/early-unlock-operation-lock-step-configuratio.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Early Unlock Operation To release the lock before the lock operation lifetime expires, insert a Lock step and select Configure Lock from the context menu for the step. Select Early Unlock from the Operation ring control in the Lock Step Configuration dialog box. The Early Unlock operation contains t

### Early Unlock Operation - Lock Step Configuration Dialog Box

#### Early Unlock Operation

To release the lock before the lock operation lifetime expires, insert a Lock step and select
 Configure Lock
 from the context menu for the step. Select
 Early Unlock
 from the Operation ring control in the Lock Step Configuration dialog box.

The Early Unlock operation contains the following option:

- Lock Name or Reference Expression 
 —The lock on which to perform the operation. You can specify the lock by name or by the object reference you receive when you create the lock using the Use Object Reference for the Lock Reference Lifetime option.

Parent topic:

Lock Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-activex-com-call-dialog-box.html language=enus -->
## TOPIC 03601: Edit ActiveX/COM Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-activex-com-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-activex-com-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the ActiveX/COM Adapter and select Specify Module from the context menu to launch the Edit ActiveX/COM Call dialog box from a TestStand User Interface . You can also select Properties from the context menu and then click Specify Module in the Step Properties dialog bo

### Edit ActiveX/COM Call Dialog Box

Insert a step configured to use the ActiveX/COM Adapter and select
 Specify Module
 from the context menu to launch the Edit ActiveX/COM Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu and then click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit ActiveX/COM Call dialog box.

The Edit ActiveX/COM Call dialog box contains the following options:

- Object Reference 
 —An Object Reference variable or property. When a step creates an object, the ActiveX/COM Adapter assigns the object reference to the variable or property, if specified. Otherwise, the ActiveX/COM Adapter automatically releases the object reference after executing the step. If the step does not create an object, but instead calls a method or accesses a property, the Object Reference control must contain the value of a valid ActiveX reference that refers to the object on which to call the method or access the property. Click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box.
- Automation Server 
 —The name of the server the step uses. The ActiveX/COM Adapter populates the ring control with the list of ActiveX Automation servers registered with Microsoft Windows. To select a server from the list, click the ring control or
 Browse 
 to load a type library file from disk for a specific server. If you want the ActiveX/COM Adapter to refresh the list of registered servers and type library information, click
 Reload 
 . You can also refresh the server type library information when you select
 File»Unload All Modules 
 . If the server has a help file associated with it, you can open it by clicking the
 ? 
 button.
 Note 
 TestStand registers the type library with Windows when you click the
 ?
 button.
- Object Class 
 —The name of the server class the step uses when it creates or invokes an object of the class. When you select a server, the ActiveX/COM Adapter populates this control with a list of objects defined for the server. The ring control separates the list of objects into two groups which are separated with a line. The upper group includes all top-level objects the ActiveX/COM Adapter can create. The lower group includes all other objects the server creates as a result of an invocation of a method or get property call. If a server type library contains help strings or links to a help file for a class, click the
 ? 
 button to access the help.
- Create Object 
 —When you enable this option, the step creates a new instance of the object class when the ActiveX/COM Adapter executes the step. When the step creates an object and you specify a property name in the Object Reference control, the ActiveX/COM Adapter assigns the value of the object handle to the property. Otherwise, the ActiveX/COM Adapter automatically releases the object reference after it executes the step.
 Note 
 Do not select Create Object when specifying an existing ActiveX object such as
 RunState.Engine
 or
 RunState.Sequence
 in the Object Reference control. 
 When you create an object, you can select one of the following options:
  - Create New 
 —Creates a new object and obtains a reference to the object. If the server application is already running, this option might launch another copy of the application. The server application decides when to launch a new instance of the application.
  - Attach to Active 
 —Obtains a reference to an active Application object. TestStand can obtain an active reference when the ActiveX server registers the object in the Running Object Table (ROT) for the operating system. Typically ActiveX servers register objects as weak references, so when the last reference to the object is released, TestStand might be unable to attach to the active reference. To work around this limitation, ActiveX servers can create a strong reference in the ROT by locking the object. For example, LabWindows/CVI ActiveX servers can use the
 CA_ServerLockActiveObject 
 and
 CA_ServerUnlockActiveObject 
 functions to lock and unlock the object in the ROT.
  - Create From File 
 —Loads an existing object from a file and obtains a reference to the object. If the server application is already running, this option might launch another copy of the application. The server application decides when to launch a new instance of the application. When you enable this option, the Edit ActiveX/COM Call dialog box displays a File Selection control and a
 Browse 
 button. You can use these controls to specify the path of the file.
  - Remote Host (optional) 
 —The
 remote system 
 where the object is created. This control dims when you select
 Attach to Active 
 .
  - Specify Expression for Host 
 —Specifies whether the Remote Host control contains an expression the ActiveX/COM Adapter evaluates at run time to determine the name of the remote host.
  - Use Step Load/Unload Options to Specify Object Creation Time and Lifetime 
 —Controls the lifetime of an object the step creates. When you do not set this option, the step creates the object when the step begins and then releases the internal reference of the step to the object when the step completes. When you enable this option, the step creates the object when the step loads according to the Load option for the step and then holds an internal reference to the object until the step unloads according to the Unload option for the step. This option is dimmed when you enable the Specify Host By Expression control.
- Call Method or Access Property 
 —Specifies if the step invokes a class method or accesses a class property when the ActiveX/COM Adapter executes the step. This control lists the types of access the server defines for the selected object class, including Call Method, Get Property, Set Property, and Set Property by Reference. If an object class does not have any methods, the control does not list the Call Method option.
 After you select the type of access, the ActiveX/COM Adapter populates the Method control with the method or property names the class defines for the access type. If a server type library contains help strings or links to a help file for a method or property, click the
 ?
 button to access the help.
- Parameters Table 
 —Contains the input and output parameters for the selected method or property. If the selected access type is Get Property, the control usually contains a single output parameter. If the access type is Set Property or Set Property by Reference, the control usually contains a single input parameter. When you call a method, the control can contain any number of input and output parameters. The ActiveX/COM Adapter automatically populates the Value field for parameters that have default values.
  - Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to access the
 [Parameters Table](for-specify-module-dialog-boxes-parameters-ta.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Type 
 —ActiveX data type for the parameter.
  - Direction 
 —Specifies whether the parameter is an input or an output.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name in the
 Additional Results 
 dialog box. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter in the Additional Results dialog box. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results dialog box specifies to log the [In] parameter value or the [Out] parameter value.
  - Default 
 —When you enable this option, TestStand uses the default value for the parameter.
  - Value 
 —A TestStand expression. For input parameters, TestStand passes the value of this expression. For output parameters, TestStand stores the data the method returns in the location this expression specifies. To help you enter an expression in the Value column, click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box. For enumerated types, a combo box displays all valid values for the type. You can use an expression with an enumerated type. Refer to the
 ActiveX/COM Call Parameters 
 topic for more information about using enumeration parameters.

Note

Q186273

support.microsoft.com/kb/186273

Out-of-process (EXE) servers do not have this problem.

#### See Also

[ActiveX/COM Code Module Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64activexcomcodemodules)

[Additional Results dialog box](additional-results-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[In-Process COM Servers Support in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64inprocesscomservers)

[Out-of-Process COM Servers in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64outprocesscomservers)

[Parameters Table Context Menu for Specify Module Dialog Boxes](for-specify-module-dialog-boxes-parameters-ta.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-analysis-module-dialog-box.html language=enus -->
## TOPIC 03602: Edit Analysis Module Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-analysis-module-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-analysis-module-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Double-click an analysis module specification, right-click an analysis module specification and select Edit Analysis Module from the context menu, or click the Edit Analysis Module button located to the right of the Module column on the Analysis Modules tab of the Configure Sequence Analyzer Availab

### Edit Analysis Module Dialog Box

Double-click an analysis module specification, right-click an analysis module specification and select
 Edit Analysis Module
 from the context menu, or click the
 Edit Analysis Module
 button located to the right of the Module column on the
 [Analysis Modules](analysis-modules-tab-configure-sequence-analy.html)
 tab of the
 [Configure Sequence Analyzer Available Rules](configure-sequence-analyzer-available-rules-d.html)
 dialog box to launch the Edit Analysis Module dialog box, in which you can view the settings for built-in analysis modules and edit the settings for custom analysis modules.

The Edit Analysis Module dialog box contains the following options:

- Module 
 —Path to the VI, LabVIEW NXG Project, or DLL module the TestStand Sequence Analyzer calls during analysis. For DLLs, use the Function control to specify the function in the DLL to call. Entering a VI path hides the Function control and shows the Run VI in LabVIEW Run-Time Engine control. 
 Entering a LabVIEW NXG project shows a Module Name control. Use the Module Name control to select a LabVIEW NXG VI to call during analysis. LabVIEW NXG VIs are called in the LabVIEW NXG Development System when executed by the Sequence Analyzer.
 National Instruments recommends that you save modules you create for custom rules in a custom subdirectory of the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Analyzer 
 directory.
 Note 
 National Instruments recommends that you also use a company name as part of the directory name to avoid potential conflicts with other custom analysis modules.
- Run VI in LabVIEW Run-Time Engine 
 —When you enable this option, you can always use a LabVIEW Run-Time Engine (RTE) to run the VI, regardless of the global
 LabVIEW Adapter 
 setting. This option specifies that the LabVIEW Adapter settings must be ignored and the VI must be loaded with the same version of the LabVIEW RTE in which the VI was last compiled. This guarantees that the VI will always be loaded with a specific version of the LabVIEW RTE, even if another version exists.
 
 When you disable this option, the sequence analyzer uses the LabVIEW Adapter settings to determine whether to run the VI in the LabVIEW RTE or in the LabVIEW development system.
- Allow Unload of .NET Assemblies 
 —Uncheck this option to load C++/CLI (mixed-mode) .NET assemblies as the analysis module. C++/CLI assemblies can't be unloaded. This control is visible only when you enter a path to a .NET assembly.
- Call Module for these Kinds of Objects 
 —Kinds objects for which the sequence analyzer calls the analysis module. Select the kinds of objects you want the analysis module to analyze. Enable the
 Subproperties of Above 
 item at the bottom of the object list to analyze subproperties of the objects you select.
- Call Module for Instances of these Types 
 —Types of objects for which the sequence analyzer calls the analysis module. Enter the type names in the list directly or click the
 Add Type From List 
 button to add types to the list.
 If the list is empty, the sequence analyzer calls the analysis module for all instances of types that correspond to the items you selected in the Call Module for these Kinds of Objects control. If the list contains one or more types, the sequence analyzer calls the analysis module only for instances of the types you specify. For example, if you select
 Steps 
 in the Call Module for these Kinds of Objects control, use the Call Module for Instances of these Types control to specify a specific step type to analyze. If you select Steps in the Call Module for these Kinds of Objects control and do not specify a type in the Call Module for Instances of these Types control, the sequence analyzer calls the analysis module for all steps, regardless of step type.
 Note 
 The sequence analyzer calls analysis modules only for objects that have associated
 [PropertyObjects](../tsapiref/propertyobject.html)
 . Because the elements in number, string, Boolean, and object reference arrays do not have associated
 PropertyObjects
 , the sequence analyzer does not call analysis modules for those array elements. To analyze those types of array elements, you must add the array type to the list, and the analysis module must iterate over the array elements.
- Call Module for these Transitions 
 —Analysis transitions on which the sequence analyzer calls the analysis module. Click the
 Add Transition From List 
 button to add transitions to the list.
 Each time the sequence analyzer transitions between analyzing one type of object to analyzing a different type of object, it calls analysis modules configured to be called for that type of transition. For example, an analysis module can count the number of steps in each analyzed sequence file if you select
 Steps 
 in the Call Module for these Kinds of Objects control and add the
 Before»Sequence File 
 and
 After»Sequence File 
 transitions. In this example, the analysis module resets a counter in the
 Before»Sequence File 
 transition, increments the counter for each step and reports the total count in the
 After»Sequence File 
 transition. Analysis modules can also use the
 Before»System 
 transition to perform initialization tasks and the
 After»System 
 transition to perform cleanup tasks for the analysis session.

#### See Also

[Configure Sequence Analyzer Available Rules dialog box](configure-sequence-analyzer-available-rules-d.html)

[Creating Custom Rules](/csh?context=ts_tsref_sa_creating_custom_rules)

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEW Adapter](/csh?context=ts_tsref_labview)

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-breakpoints-watch-expressions-dialog-box.html language=enus -->
## TOPIC 03603: Edit Breakpoints/Watch Expressions Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-breakpoints-watch-expressions-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-breakpoints-watch-expressions-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Debug»Breakpoints/Watches to launch the Edit Breakpoints/Watch Expressions dialog box, in which you can review and edit the breakpoints and watch expressions associated with the current workspace. TestStand saves and reloads breakpoints and watch expressions using an options file associated w

### Edit Breakpoints/Watch Expressions Dialog Box

Select
 Debug»Breakpoints/Watches
 to launch the Edit Breakpoints/Watch Expressions dialog box, in which you can review and edit the breakpoints and watch
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 associated with the current workspace. TestStand saves and reloads breakpoints and watch expressions using an options file associated with the current workspace or a default options file when no workspace is loaded.

The Edit Breakpoints/Watch Expressions dialog box contains the following tabs:

- Breakpoints 
 —Lists the breakpoints in currently open sequences and sequence files TestStand saved while the current workspace was loaded.
- Watch Expressions 
 —Lists the watch expressions previously defined in TestStand while the current workspace was loaded. User interfaces that do not support the display of watch expressions in their Execution window do not display this tab.

Note

#### See Also

[Engine.PersistBreakpoints](../tsapiref/engine-persistbreakpoints.html)

[Engine.PersistWatchExpressions](../tsapiref/engine-persistwatchexpressions.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-c-c-dll-call-dialog-box.html language=enus -->
## TOPIC 03604: Edit C/C++ DLL Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-c-c-dll-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-c-c-dll-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the C/C++ DLL Adapter and select Specify Module from the context menu to launch the Edit C/C++ DLL Call dialog box from a TestStand User Interface . You can also select Properties from the context menu and then click Specify Module in the Step Properties dialog box to

### Edit C/C++ DLL Call Dialog Box

Insert a step configured to use the C/C++ DLL Adapter and select
 Specify Module
 from the context menu to launch the Edit C/C++ DLL Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu and then click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit C/C++ Call dialog box.

The Edit C/C++ DLL Call dialog box contains the following tabs:

- Module 
 —The
 code module 
 the C/C++ DLL Adapter executes for the step and specifies the parameter information for the module.
- Source Code 
 —Additional information TestStand requires for creating and editing a code module in another application.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-close-database-dialog-box.html language=enus -->
## TOPIC 03605: Edit Close Database Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-close-database-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-close-database-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Close Database in the context menu for the step to launch the Edit Close Database dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit Close Database on the General tab of the Step Properties dialog box. The Edit Clo

### Edit Close Database Dialog Box

Select
 Edit Close Database
 in the context menu for the step to launch the Edit Close Database dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit Close Database
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Edit Close Database dialog box contains the following option:

- Database Handle (Number) 
 —The name of the variable or property that contains the database handle to be closed. The variable or property is of the Number data type. After closing the database handle, the step assigns a value of
 0 
 to the variable or property.

#### See Also

[Database Step Types](database-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Close Database Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-close-sql-statement-dialog-box.html language=enus -->
## TOPIC 03606: Edit Close SQL Statement Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-close-sql-statement-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-close-sql-statement-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Close SQL Statement in the context menu for the step to launch the Edit Close SQL Statement dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit Close SQL Statement on the General tab of the Step Properties dialog bo

### Edit Close SQL Statement Dialog Box

Select
 Edit Close SQL Statement
 in the context menu for the step to launch the Edit Close SQL Statement dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit Close SQL Statement
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Edit Close SQL Statement dialog box contains the following option:

- Statement Handle (Number) 
 —The name of the Number variable or property that contains which statement handle to be closed. After closing the statement handle, the step assigns a value of
 0 
 to the variable or property.

Databases might return an error when you use a Close SQL Statement step if the statement has pending record changes. Commit the pending record by using a Data Operation step type configured to do a Put Record operation to resolve this issue.

#### See Also

[Database Step Types](database-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Close SQL Statement Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-code-template-dialog-box.html language=enus -->
## TOPIC 03607: Edit Code Template Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-code-template-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-code-template-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Edit on the Code Templates tab of the Step Type Properties dialog box to launch the Edit Code Template dialog box. The Edit Code Template dialog box contains the following options: Description —The description string for the code template. Type —The code template type. Path —The code template

### Edit Code Template Dialog Box

Click
 Edit
 on the
 [Code Templates](code-templates-tab-step-type-properties-dialo.html)
 tab of the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box to launch the Edit Code Template dialog box.

The Edit Code Template dialog box contains the following options:

- Description 
 —The description string for the code template.
- Type 
 —The code template type.
- Path 
 —The code template file path.
- Edit Code 
 —Launches the application Microsoft Windows associates with the file extension of the code module.
- Require Sequence Context 
 —When you enable this option, the code template requires that the sequence context be passed. When you enable this control, TestStand completes the next step according to the environment the code template was created in.
 
 Note 
 Require Sequence Context is available only for legacy templates.
  - When you click
 Create Code 
 on the
 Source Code 
 tab of the
 Edit LabWindows/CVI Module Call 
 dialog box, TestStand enables the Pass Sequence Context option on the
 Module 
 tab.
  - When you click
 Create VI 
 in the
 Edit LabVIEW VI Call 
 dialog box, TestStand enables the Sequence Context ActiveX Pointer option.
- Parameter Name/Value Mappings 
 —The default parameter values to use on the Module tab of a Specify Module dialog box for the adapters. TestStand applies the default parameter values when you click
 Create Code 
 on the Source Code tab of the Specify Module dialog box.
 In a template code module, you can access step properties and sequence variables through the TestStand API or as parameters to the code module. If you access them as parameters, you must specify the parameter values in the appropriate Specify Module dialog box. Since the values you must specify are usually the same for most step instances, specify the default parameter values TestStand automatically populates in the dialog box when you click
 Create Code 
 or
 Create VI 
 .
 Note 
 The controls in the Parameter Name/Value Mappings section are not available when you are using legacy or HTBasic templates.
 The controls in the Parameter Name/Value Mappings section are only visible when you edit code templates for adapters that support parameter passing. 
 The Parameter Name/Value Mappings section contains the following options:
  - Add 
 —Inserts an empty entry at the end of the listbox.
  - Delete 
 —Deletes the currently selected entry in the listbox.
  - Parameter Name 
 —Sets the name of a parameter exactly as it will appear in the parameter list in the template code module. To specify the return value for LabWindows/CVI and C/C++ DLL templates, use
 %ReturnValue 
 .
  - Value Expression 
 —Sets the expression you want TestStand to insert into the Value control for the parameter on the Module tab of the appropriate Specify Module dialog box.
  - Result Action 
 —Selects the value you want to appear in the Result Action ring control of the Module tab. Use the ring control on the Module tab to instruct TestStand to automatically set the
 Error.Occurred 
 step property to
 True 
 when the return value or parameter value after the call is greater than zero, less than zero, equal to zero, or not equal to zero.
 Note 
 This option is available only for LabWindows/CVI and C/C++ DLL templates.
  - Set Error.Code to Value 
 —The state, enabled or disabled, of the Set Error.Code to Value option on the Module tab of the appropriate Specify Module dialog box, which is where you enter return values and reference parameters. Use this option to instruct TestStand to automatically assign the return value or the output value to the
 Error.Code 
 step property.
 Note 
 This option is available only for LabWindows/CVI and C/C++ DLL templates.

#### See Also

[Accessing Properties and Variables Using API (Example)](/csh?context=ts_tsexamples_accessing_prop_and_var)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[Edit LabWindows/CVI Module Call dialog box](edit-labwindows-cvi-module-call-dialog-box.html)

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-data-link-dialog-box.html language=enus -->
## TOPIC 03608: Edit Data Link Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-data-link-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-data-link-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Select Data Link dialog box and click New or Edit to launch the Edit Data Link dialog box. The Edit Data Link dialog box contains the following options: Data Link Name —A name for the data link. TestStand displays this name in the list control in the Select Data Link dialog box. Connectio

### Edit Data Link Dialog Box

Launch the
 [Select Data Link](select-data-link-dialog-box.html)
 dialog box and click
 New
 or
 Edit
 to launch the Edit Data Link dialog box.

The Edit Data Link dialog box contains the following options:

- Data Link Name 
 —A name for the data link. TestStand displays this name in the list control in the
 Select Data Link 
 dialog box.
- Connection String 
 —The connection information for the data link. The string specifies the data source and options to use when opening the data source. The contents of the string can include the name of the server where the data resides, the database or file that contains the data, and the user ID and permissions to use when connecting to the data source.
- File Browse 
 —Specifies a Microsoft Data Link file (
 .udl 
 ), which specifies the connection string. When you select a Microsoft Data Link file, TestStand updates the Connection String control with the pathname of the file.
- Build 
 —Constructs a connection string using the Data Link Properties dialog box.

#### See Also

[Select Data Link dialog box](select-data-link-dialog-box.html)

[Configuring Connection Strings](/csh?context=ts_tsref_dbviewer_connectionstrings)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-data-operation-dialog-box.html language=enus -->
## TOPIC 03609: Edit Data Operation Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-data-operation-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-data-operation-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Data Operation in the context menu for the step to launch the Edit Data Operation dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click the Edit Data Operation button on the General tab of the Step Properties dialog box. T

### Edit Data Operation Dialog Box

Select
 Edit Data Operation
 in the context menu for the step to launch the Edit Data Operation dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click the
 Edit Data Operation
 button on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Edit Data Operation dialog box contains the following tabs:

- Record/Operation 
 —The type of operation and which record to operate on.
- Column/Parameter 
 —A mapping between columns in the statement and TestStand variables or properties.

#### See Also

[Database Step Types](database-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Data Operation Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-data-tab.html language=enus -->
## TOPIC 03610: Edit Data Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-data-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-data-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edit Data Tab Right-click a user table in the Database Explorer and select Edit Data to launch the Edit Data tab. The data grid displays the records in the table. You can modify the values and submit the changes to the database. When you navigate away from the row you are editing, the Database Viewe

### Edit Data Tab

#### Edit Data Tab

Right-click a user table in the
 [Database Explorer](database-explorer.html)
 and select
 Edit Data
 to launch the Edit Data tab. The
 [data grid](data-grid.html)
 displays the records in the table. You can modify the values and submit the changes to the database. When you navigate away from the row you are editing, the Database Viewer submits the modified values to the database.

Note

You can modify the existing value of a cell to null or specify a null value in a new record by pressing <Ctrl+Delete> in that cell. Entering an empty string to specify null might result in a data type mismatch error for most column data types.

The Edit Data Tab contains the following options:

- Submit 
 —Submits the modified data to the database.
- Refresh 
 —Retrieves data for the table. You can also press <Ctrl+R> to perform this command.
- Print 
 —Launches the
 Print 
 dialog box. You can also press <Ctrl+P> to perform this command.
- Export Data 
 —Launches the
 Export Document 
 dialog box.
- Navigator Panel 
 —This panel contains arrow keys to navigate through records in the data grid. The panel also contains the following buttons for edit operations:
  - Add(+) 
 —Inserts a new row at the end of the data grid.
  - Delete 
 —Deletes the selected row.
 Note 
 A small arrowhead indicates the selected row in the data grid.
  - Edit 
 —Edits the selected cell.
  - End Edit 
 —Submits the change in the selected cell to the database.
  - Cancel Edit 
 —Reverts the changes in the selected cell.
  - Undo Row Errors 
 —Reverts all the changes made to a row that returned logical errors after submitting the modified data to the database.

The Edit Data tab also contains the following indicators:

- Errors on Submitting Data 
 —An error icon indicates when the submit operation returns errors, and a tooltip displays the exact error information. You cannot edit other rows in the grid until you resolve the existing error.
- Errors in a Cell 
 —If the data entered in a cell is incompatible with the column’s data type, an error icon indicates the error, and a tooltip displays the exact error information. You cannot edit other columns in the grid until you resolve this error.

The data grid context menu includes the following options:

- Add New Row 
 —Inserts a new row at the end of the last record in the table.
- Delete Selected Row 
 —Deletes the selected row from the database.
- Undo Row Errors 
 —Reverts all the changes made to a row that returned logical errors after submitting the modified data to the database.

Parent topic:

Database Viewer Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-data-type-flags-dialog-box.html language=enus -->
## TOPIC 03611: Edit Data Type Flags Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-data-type-flags-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-data-type-flags-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Edit Flags dialog box and click Type Flags to launch the Edit Data Type Flags dialog box. You can also launch this dialog box by launching the Step Type Properties dialog box, clicking Advanced , selecting Flags from the drop-down list, and then clicking the Type Flags . The Edit Data Typ

### Edit Data Type Flags Dialog Box

Launch the
 [Edit Flags](edit-flags-dialog-box.html)
 dialog box and click
 Type Flags
 to launch the Edit Data Type Flags dialog box. You can also launch this dialog box by launching the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box, clicking
 Advanced
 , selecting
 Flags
 from the drop-down list, and then clicking the
 Type Flags
 .

The Edit Data Type Flags dialog box contains the following listboxes:

- Type Flags 
 —Flags which are valid only for a property object that is a type definition. Type Flags do not exist in instances of the type.
- Instance Default Flags 
 —When TestStand creates a new instance of the type, the values in this listbox determine the initial flag values in the instance.
- Flags Not Editable in Instances 
 —When you set a flag in this listbox, the value of the flag the Instance Default Flags listbox specifies always determines the value of the flag that appears in instances of the type. In this case, instances of a type cannot change the value of the flag.

#### See Also

[Edit Flags dialog box](edit-flags-dialog-box.html)

[PropertyObjTypeFlags](../tsapiref/propertyobjtypeflags.html)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-enumeration-value-dialog-box.html language=enus -->
## TOPIC 03612: Edit Enumeration Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-enumeration-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-enumeration-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit from the enumeration drop-down menu of any enumeration variable in the Variables View, Execution View, Types Palette, Watch or Station Globals windows to launch the Edit Enumeration Value dialog box. The Edit Enumeration Value dialog box contains the following options: Enter value as str

### Edit Enumeration Value Dialog Box

Select
 Edit
 from the enumeration drop-down menu of any enumeration variable in the Variables View, Execution View, Types Palette, Watch or Station Globals windows to launch the Edit Enumeration Value dialog box.

The Edit Enumeration Value dialog box contains the following options:

- Enter value as string 
 —Edit the enumeration value by entering enumerator strings. If the enumerator has the flags attribute enabled, then you may enter multiple enumerators strings combined by an
 OR 
 operator.
- Enter value as number 
 —Edit the enumeration value by entering a number.
- Grid Control 
 —Edit the enumeration value by selecting one of the enumerators. If the enumerator has has the flags attribute enabled, then you may select multiple enumerators.

Note

Changes are not committed until you press
 OK
 . Press
 Cancel
 to revert changes.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-enumerators-dialog-box.html language=enus -->
## TOPIC 03613: Edit Enumerators Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-enumerators-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-enumerators-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Edit Enumerators button in the Types view to launch the Edit Enumerators dialog box, in which you can add, edit, or remove the enumerators of an enum type. You can perform the following tasks in the Edit Enumerators dialog box: To make the enumeration a flags type, enable the Flags Enumera

### Edit Enumerators Dialog Box

Click the
 Edit Enumerators
 button in the Types view to launch the Edit Enumerators dialog box, in which you can add, edit, or remove the enumerators of an enum type.

You can perform the following tasks in the Edit Enumerators dialog box:

- To make the enumeration a flags type, enable the
 
 Flags Enumeration 
 option.
- To make the enumeration a strict type, enable the
 Strict Enumeration 
 option.
- To add new enumerators, click on the last row in the table and begin typing.
- To edit existing enumerators, click on the corresponding cell in the table and make changes.
- To remove enumerators, click on the delete button to the right of the Value field in the row of the enumerator you want to remove.

No changes are committed until you press
 OK
 . Pressing
 Cancel
 reverts all changes.

#### Enumerator Names and Values

Enumerator names must be unique. You can use any string for non-flags enumerator names, but flags enumerator names are restricted to valid identifiers.

Enumerator values must be numbers that fit the representation of the enum type. Hexadecimal, octal, and binary values are accepted, but will be converted according to the numeric format of the enum type.

If the enum type had no enumerators, then adding new enumerators will set the default value to the first enumerator. If the default value was previously set to an enumerator and the value of that enumerator changed, the default value will be updated accordingly. If that enumerator was deleted, the default value will be set to the first enumerator. If all enumerators are deleted, the enum type will enter into an invalid state.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-flags-dialog-box.html language=enus -->
## TOPIC 03614: Edit Flags Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-flags-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-flags-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Type Properties dialog box and click Advanced to launch the Edit Flags dialog box. You can also launch this dialog box by launching the Step Type Properties dialog box, clicking Advanced , and selecting Flags from the drop-down list. Use this dialog box to change the values of the propert

### Edit Flags Dialog Box

Launch the
 [Type Properties](type-properties-dialog-box.html)
 dialog box and click
 Advanced
 to launch the Edit Flags dialog box. You can also launch this dialog box by launching the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box, clicking
 Advanced
 , and selecting
 Flags
 from the drop-down list.

Use this dialog box to change the values of the property flags for a property object. The list of flags corresponds to the available
 [property flag constants in the TestStand API](../tsapiref/propertyflags.html)
 . Checking an item in the listbox activates the corresponding flag in the object.

The property flags represent the state of the object. You can change the state of the object by enabling or disabling the corresponding flag in the listbox. For example, when you enable the PropFlags_NotEditable flag for an object, the property page for the object becomes read-only and you cannot change the value of the object. Each flag is a single bit in a 32-bit integer value. When you enable or disable a flag, the New Flags control displays the changes.

- Old Flags 
 —Shows the initial hexadecimal value of the flags for the object when the Edit Flags dialog box was initially opened.
- New Flags 
 —Shows you the combined hexadecimal value of all flags after the changes. This is the same value the
 PropertyObject.GetFlags 
 method returns. You can edit the value of this option directly by entering a decimal or hexadecimal value. When you edit this option directly, each flag list item reflects the changes. When you enable or disable a flag, the New Flags control displays the changes.
- Type Flags 
 —This option is visible only when you edit the properties of a type definition. Click
 Type Flags 
 to launch the
 Edit Data Type Flags 
 dialog box.
- Apply Changes to Flags and Type Flags in All Loaded Instances of the Type 
 —This option is visible only when you are editing the properties of a type definition. When you enable this option and click
 OK 
 , TestStand applies the changes you make to the flags in the Edit Flags dialog box to all instances of the type that are loaded. 
When TestStand updates the instances, TestStand updates only the flags you modified in the Edit Flags dialog box. The values specified in the Instance Default Flags control in the Edit Data Type Flags dialog box specify the initial flag values TestStand uses when it creates a new instance of the type. If you unset a flag in the Edit Flags dialog box but the same flag is set in the Instance Default Flags control in the Edit Data Type Flags dialog box, TestStand sets the flag in all instances of the type that are loaded because the set state of the flag is the state that the flag is configured to have for new instances of the type.
 Note 
 This option does not affect type instances saved to disk that are not currently loaded.

#### See Also

[Edit Data Type Flags dialog box](edit-data-type-flags-dialog-box.html)

[PropertyFlags](../tsapiref/propertyflags.html)

[PropertyObject.GetFlags](../tsapiref/propertyobject-getflags.html)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-goto-step-dialog-box.html language=enus -->
## TOPIC 03615: Edit Goto Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-goto-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-goto-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Destination in the context menu for the step or click Edit Destination on the General tab of the Step Properties dialog box to launch the Edit Goto Step dialog box from a TestStand User Interface . Use the Destination Step control to specify the target for the Goto step. You cannot selec

### Edit Goto Step Dialog Box

Select
 Edit Destination
 in the context menu for the step or click
 Edit Destination
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit Goto Step dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use the Destination Step control to specify the target for the Goto step. You cannot select an Else or Else If step as the target of a Goto Step. The control contains a list of steps in each step group, as well as the following three additional targets:

- <End Group> 
 —Jumps to the end of the current step group.
- <Cleanup> 
 —Jumps to the Cleanup step group.
- <Specify By Expression> 
 —Defines an expression that specifies a name or unique ID of a step. If the expression evaluates to a step name, the destination is the first step in the step group with the same name. If the expression evaluates to a step ID the destination is the first step in the sequence with the same unique step ID.

By default, Goto steps do not pass or fail. After a Goto step executes, TestStand sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Done
 or
 Error
 .

The Goto step type does not define any additional step properties other than the custom properties common to all steps.

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

Goto Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-htbasic-subroutine-call-dialog-box.html language=enus -->
## TOPIC 03616: Edit HTBasic Subroutine Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-htbasic-subroutine-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-htbasic-subroutine-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the HTBasic Adapter and select Specify Module from the context menu to launch the Edit HTBasic Subroutine Call dialog box from a TestStand User Interface . You can also select Properties from the context menu. When you select Properties , you must click Specify Module

### Edit HTBasic Subroutine Call Dialog Box

Insert a step configured to use the HTBasic Adapter and select
 Specify Module
 from the context menu to launch the Edit HTBasic Subroutine Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu. When you select
 Properties
 , you must click
 Specify Module
 on the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit HTBasic Subroutine Call dialog box.

The Edit HTBasic Subroutine Call dialog box contains the following options:

- Subroutine File Pathname 
 —The HTBasic program file that contains the subroutine the step calls. You can specify an absolute or relative path name for the HTBasic program file. Relative path names are relative to the TestStand search directory paths. Use the
 Edit Search Directories 
 dialog box to
 customize the search directory paths 
 .
 To load and call a subroutine, you must write the subroutine file to disk in the HTBasic application using the
 Store
 command instead of the
 Save
 command. HTBasic is only able to programmatically load and run stored subroutines.
- Subroutine Name 
 —The name of the subroutine the step calls. HTBasic requires that the subroutine name length cannot exceed 15 characters and the first character must be uppercase. The HTBasic Adapter interprets the first character as uppercase even when you specify lowercase.
- Show HTBasic Application When Called 
 —When the HTBasic Adapter executes a step that calls an HTBasic subroutine, it does not activate the HTBasic application. Enable this option when you want to activate the HTBasic application.
- HTBasic Working Directory 
 —Specifies the options for the HTBasic Adapter to set for the working directory of the HTBasic server before invoking the subroutine. Enable this option when the test code assumes a particular working directory path.
 The HTBasic Working Directory ring control contains the following five options: 
 
 The default value is Use adapter default. The
 Browse 
 button and edit box are available only when you select the Use specified directory option.
  - Use adapter default
  - Do not change working directory
  - HTBasic server directory
  - Subroutine file directory
  - Use specified directory

The following options are available only when you have installed an HTBasic development environment:

- Create Code 
 —Creates a code shell for a subroutine. If the HTBasic file you specify does not already exist, the HTBasic Adapter creates it. If the file already exists, the HTBasic Adapter prompts you to replace the file. If the HTBasic code template file exists for the step type you selected for this step, the HTBasic Adapter uses the template to create the new subroutine.
- Edit Subroutine 
 —Edits a subroutine that already exists.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-dmm-step-dialog-box.html language=enus -->
## TOPIC 03617: Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-dmm-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-dmm-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Basic Tab The Basic tab for the Configure operation contains the following options: Measurement Function —The measurement function. The value of this setting determines the units for the Range and Resolution settings and the measurement values the Read and Fetch operations return

### Edit IVI Dmm Step Dialog Box

#### Configure Operation

#### Basic Tab

The Basic tab for the Configure operation contains the following options:

- Measurement Function 
 —The measurement function. The value of this setting determines the units for the Range and Resolution settings and the measurement values the Read and Fetch operations return.
 
 Supported Value
 DescriptionDC Volts (1)
 Sets the DMM to measure DC voltage.
 AC Volts (2)
 Sets the DMM to measure AC voltage.
 DC Current (3)
 Sets the DMM to measure DC current.
 AC Current (4)
 Sets the DMM to measure AC current.
 Resistance 2-wire (5)
 Sets the DMM to measure 2-wire resistance.
 Resistance 4-wire (101)
 Sets the DMM to measure 4-wire resistance.
 AC Plus DC Volts (106)
 Sets the DMM to measure AC voltage plus DC voltage.
 AC Plus DC Current (107)
 Sets the DMM to measure AC current plus DC current.
- Resolution 
 —The measurement resolution in absolute units of precision. The Measurement Function setting determines the units for resolution. If the resolution value you specify does not exactly match a value an instrument driver supports, the instrument driver will coerce down to the next supported value. You can calculate the digits of precision from the Range and Resolution settings, as shown in the following example:
 Precision = Log10(Range/Resolution)
- Min AC Freq 
 —The minimum frequency component in hertz of the input signal for AC measurements. If Min AC Freq does not exactly match a value an instrument driver supports, the instrument driver will coerce down to the next supported value. The value of this setting only affects instrument behavior when the Measurement Function setting is set to an AC voltage or AC current measurement and the AC Measurement extension is enabled.
- Max AC Freq 
 —The maximum frequency component in hertz of the input signal for AC measurements. If Max AC Freq does not exactly match a value an instrument driver supports, the instrument driver will coerce up to the next supported value. The value of this setting only affects instrument behavior when the Measurement Function setting is set to an AC voltage or AC current measurement and the AC Measurement extension is enabled.
- Trigger Source 
 —The trigger source, which controls when the DMM takes a measurement. The Trigger Source setting defines the location of the trigger.
 
 Supported Value
 DescriptionImmediate (1)
 Specifies that the DMM does not wait for a trigger before taking a measurement.
 External (2)
 Specifies that the DMM waits for a trigger on the external trigger input before taking a measurement.
 Software (3)
 Specifies that the DMM waits for a trigger until the Send Software Trigger operation executes and then takes a measurement.
 TTL0 (111)
 Specifies that the DMM waits for a trigger on TTL0 before taking a measurement.
 TTL1 (112)
 Specifies that the DMM waits for a trigger on TTL1 before taking a measurement.
 TTL2 (113)
 Specifies that the DMM waits for a trigger on TTL2 before taking a measurement.
 TTL3 (114)
 Specifies that the DMM waits for a trigger on TTL3 before taking a measurement.
 TTL4 (115)
 Specifies that the DMM waits for a trigger on TTL4 before taking a measurement.
 TTL5 (116)
 Specifies that the DMM waits for a trigger on TTL5 before taking a measurement.
 TTL6 (117)
 Specifies that the DMM waits for a trigger on TTL6 before taking a measurement.
 TTL7 (118)
 Specifies that the DMM waits for a trigger on TTL7 before taking a measurement.
 ECL0 (119)
 Specifies that the DMM waits for a trigger on ECL0 before taking a measurement.
 ECL1 (120)
 Specifies that the DMM waits for a trigger on ECL1 before taking a measurement.
 PXI Star (131)
 Specifies that the DMM waits for a trigger on the PXI Star trigger bus before taking a measurement.
 RTSI0 (140)
 Specifies that the DMM waits for a trigger on RTSI0 before taking a measurement.
 RTSI1 (141)
 Specifies that the DMM waits for a trigger on RTSI1 before taking a measurement.
 RTSI2 (142)
 Specifies that the DMM waits for a trigger on RTSI2 before taking a measurement.
 RTSI3 (143)
 Specifies that the DMM waits for a trigger on RTSI3 before taking a measurement.
 RTSI4 (144)
 Specifies that the DMM waits for a trigger on RTSI4 before taking a measurement.
 RTSI5 (145)
 Specifies that the DMM waits for a trigger on RTSI5 before taking a measurement.
 RTSI6 (146)
 Specifies that the DMM waits for a trigger on RTSI6 before taking a measurement.
- Range 
 —The measurement range. Use this setting only when the Range Mode setting is set to Use Specified Range. If the range value you specify does not exactly match a value an instrument driver supports, the instrument driver will coerce up to the next supported value. The Measurement Function setting determines the units of Range. You can calculate the digits of precision from the Range and Resolution settings, as shown in the following example:
 Precision = Log10(Range/Resolution) 
 
 Supported Value
 DescriptionAuto Range On (-1)
 Sets the DMM to automatically calculate the range before each measurement.
 Auto Range Off (-2)
 Disables autoranging. The DMM sets the range to the value it most recently calculated.
 Auto Range Once (-3)
 Sets the DMM to calculate the range before the next measurement. The DMM uses this range value for all subsequent measurements.
 Use Specified Delay (0)
 Enables you to manually specify the measurement range.
- Trigger Delay 
 —The length of time in seconds between the DMM receiving the trigger and taking the measurement. Many DMMs have a small, nonzero value as the minimum value for trigger delay. To configure the instrument to use the shortest trigger delay, set this setting to
 0 
 . The driver will coerce any value between zero and the minimum Trigger Delay value you specify to the minimum supported value. Trigger Delay is only used when the Trigger Delay Mode setting is set to Use Specified Delay.
 
 Supported Value
 DescriptionAuto Delay On (-1)
 Sets the DMM to calculate the trigger delay before each measurement.
 Auto Delay Off (-2)
 Stops the DMM from calculating the trigger delay and sets the trigger delay to the last trigger delay the DMM calculated.
 Use Specified Delay (0)
 Enables you to manually specify the length of time, in seconds, between the DMM receiving the trigger and taking the measurement.

Parent topic:

Configure Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-dmm-step-dialog-box2.html language=enus -->
## TOPIC 03618: Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-dmm-step-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-dmm-step-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Temperature Tab The Temperature tab for the Configure operation contains the following options: Transducer Type —The device used to measure the temperature. The value of this setting only affects instrument behavior when the Temperature Measurement extension and the Measurement F

### Edit IVI Dmm Step Dialog Box

#### Configure Operation

#### Temperature Tab

The Temperature tab for the Configure operation contains the following options:

- Transducer Type 
 —The device used to measure the temperature. The value of this setting only affects instrument behavior when the Temperature Measurement extension and the Measurement Function setting are set to Temp.
 
 Supported Value
 DescriptionThermocouple (1)
 Sets the DMM to measure temperature using a thermocouple.
 Thermistor (2)
 Sets the DMM to measure temperature using a thermistor.
 2-Wire RTD (3)
 Sets the DMM to measure temperature using a 2-wire resistance temperature device (RTD).
 4-Wire RTD (4)
 Sets the DMM to measure temperature using a 4-wire resistance temperature device (RTD).
- Thermistor Resistance 
 —The resistance of the thermistor, in ohms. The value of this setting only affects instrument behavior when the Thermistor and Temperature Measurement extensions are enabled and the Transducer Type is set to Thermistor.
- Rtd Alpha 
 —The alpha parameter for a resistance temperature device (RTD). The value of this setting only affects instrument behavior when the RTD and Temperature Measurement extensions are enabled and the Transducer Type is set to 2-Wire RTD or 4-Wire RTD.
- Rtd Resistance 
 —The R0 parameter (resistance) for a RTD, in ohms. The RTD resistance is also known as the RTD reference value. The value of this setting only affects instrument behavior when the RTD and Temperature Measurement extensions are enabled and the Transducer Type is set to 2-Wire RTD or 4-Wire RTD.
- Thermocouple Type 
 —The type of thermocouple used to measure the temperature. The value of this setting only affects instrument behavior when the Thermocouple and Temperature Measurement extensions are enabled and the Transducer Type is set to Thermocouple.
 
 Supported Value
 DescriptionB (1)
 Measures temperature from a B-type thermocouple.
 C (2)
 Measures temperature from a C-type thermocouple.
 D (3)
 Measures temperature from a D-type thermocouple.
 E (4)
 Measures temperature from a E-type thermocouple.
 G (5)
 Measures temperature from a G-type thermocouple.
 J (6)
 Measures temperature from a J-type thermocouple.
 K (7)
 Measures temperature from a K-type thermocouple.
 N (8)
 Measures temperature from a N-type thermocouple.
 R (9)
 Measures temperature from a R-type thermocouple.
 S (10)
 Measures temperature from a S-type thermocouple.
 T (11)
 Measures temperature from a T-type thermocouple.
 U (12)
 Measures temperature from a U-type thermocouple.
 V (13)
 Measures temperature from a V-type thermocouple.
- Reference Junction Type 
 —The type of reference junction to be used in the reference junction compensation of a thermocouple measurement.
 
 Supported Value
 DescriptionInternal (1)
 Sets the DMM to use an internal sensor at the thermocouple junction for the junction compensation.
 Fixed (2)
 Sets the DMM to use a fixed value for the thermocouple junction compensation.

Parent topic:

Configure Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-dmm-step-dialog-box3.html language=enus -->
## TOPIC 03619: Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-dmm-step-dialog-box3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-dmm-step-dialog-box3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit IVI Dmm in the context menu for the step to launch the Edit IVI Dmm Step dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit IVI Dmm on the General tab of the Step Properties dialog box. In the Edit IVI Dmm dialog b

### Edit IVI Dmm Step Dialog Box

Select
 Edit IVI Dmm
 in the context menu for the step to launch the Edit IVI Dmm Step dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit IVI Dmm
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Edit IVI Dmm dialog box, select an operation for the step to perform.

The IVI Dmm step type supports the following options:

- Logical Name 
 —Selects a logical name or a virtual instrument name you configure in Measurement & Automation Explorer (MAX). You can use the buttons to the right of the control to launch the
 Expression Browser 
 dialog box and to launch MAX.
 Note 
 TestStand does not install IVI-compliant instrument drivers and does not configure any sample logical names in MAX. Refer to the application help for the IVI Instruments category in MAX for more information about where to obtain and how to install IVI-compliant instrument drivers, as well as how to create the logical names IVI step types use.
 All IVI names, such as logical names, virtual names, or channel names, are case-sensitive. If you use logical names, driver session names, or virtual names in the program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters in the name.
- Operation 
 —The operation the step performs. The following operations are available when you use the IVI Dmm step type:
  - Configure 
 —Configures the instrument to match the state the step specifies.
  - Show Soft Front Panel 
 —Displays the soft front panel (SFP) for the instrument.
  - Hide Soft Front Panel 
 —Hides the SFP for the instrument.
  - Read 
 —Initiates and returns a measurement from the instrument.
  - Initiate 
 —Initiates a measurement.
  - Fetch 
 —Returns a measured value from a measurement the Initiate operation has started.
  - Abort 
 —Cancels the wait for a trigger.
  - Send Software Trigger 
 —Sends a software trigger command to trigger the instrument.
  - Get Information 
 —Retrieves low-level status and information from the instrument.
- Validate 
 —Launches the
 Validate IVI Configuration 
 dialog box, in which you can validate the configuration of IVI steps.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[IVI Step Types](ivi-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Validate IVI Configuration dialog box](validate-ivi-configuration-dialog-box.html)

Parent topic:

Dmm Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-fgen-step-dialog-box.html language=enus -->
## TOPIC 03620: Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-fgen-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-fgen-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Basic Tab The Basic tab for the Configure operation contains the following options: Output Mode —Determines how the function generator produces waveforms. This setting determines the extension group that includes the functions and settings to use to configure the waveform the fun

### Edit IVI Fgen Step Dialog Box

#### Configure Operation

#### Basic Tab

The Basic tab for the Configure operation contains the following options:

- Output Mode 
 —Determines how the function generator produces waveforms. This setting determines the extension group that includes the functions and settings to use to configure the waveform the function generator produces.
 
 Supported Value
 DescriptionStandard Function (0)
 Uses standard function settings to configure the output signals of the function generator.
 Arb Waveform (1)
 Uses the settings on the Waveforms tab to configure the output signals of the function generator.
 Sequence (2)
 Uses the settings on the Sequences tab to configure the output signals of the function generator.
- Ref Clock Source 
 —The source of the reference clock. The function generator derives frequencies and sample rates it uses to generate waveforms from the reference clock.
 
 Supported Value
 DescriptionExternal (1)
 The source of the reference clock to be a signal from an external source.
 Internal (0)
 The source of the reference clock to be a signal generated internally.
 RTSI Clock (101)
 The source of the reference clock to be a signal from the RTSI clock source.
- Arb Sample Rate 
 —The sample rate of the arbitrary waveforms the function generator produces. The units are samples per second. For function generators with more than one channel, this setting affects all channels.
- Internal Trigger Rate 
 —The rate at which the internal trigger source of the function generator produces a trigger, in triggers per second. The Internal Trigger extension supports function generators that can generate output based on an internally generated trigger signal. You can configure the rate at which internal triggers are generated. This setting only affects instrument behavior when the Trigger Source setting is set to Internal Trigger.
- Auto Stop/Start 
 —Automates the stopping and starting of function generation during the Configure operation. When you enable this option, Abort is called before a Configure operation takes place, and Initiate is called at the end of a Configure operation.
- AM Modulation Internal Depth 
 —The extent of modulation the function generator applies to the carrier waveform. This setting affects the behavior of the instrument only when the AM Source setting for a channel is set to AM Internal. The internal depth for modulated waveforms is represented as a percentage.
- AM Modulation Internal Waveform 
 —The waveform of the internal modulating waveform source for AM. This setting only affects the behavior of the instrument when the AM Source setting for a channel is set to AM Internal.
 
 Supported Value
 DescriptionDC (6)
 A DC waveform as the AM internal modulating waveform source.
 Ramp Down (5)
 A negative ramp waveform as the AM internal modulating waveform source.
 Ramp Up (4)
 A positive ramp waveform as the AM internal modulating waveform source.
 Sine (1)
 A sine waveform as the AM internal modulating waveform source.
 Square (2)
 A square waveform as the AM internal modulating waveform source.
 Triangle (3)
 A triangle waveform as the AM internal modulating waveform source.
- AM Modulation Internal Frequency 
 —The frequency, in hertz, of the internal modulating waveform source for AM. This setting only affects the behavior of the instrument when the AM Source setting for a channel is set to AM Internal.
- FM Modulation Internal Deviation 
 —The maximum frequency deviation the function generator applies to the carrier waveform. This setting only affects the behavior of the instrument when the FM Source setting for a channel is set to FM Internal.
- FM Modulation Internal Waveform 
 —The waveform of the internal modulating waveform source for FM. This setting only affects the behavior of the instrument when the FM Source setting for a channel is set to FM Internal.
 
 Supported Value
 DescriptionDC (6)
 A DC waveform as the FM internal modulating waveform source.
 Ramp Down (5)
 A negative ramp waveform as the FM internal modulating waveform source.
 Ramp Up (4)
 A positive ramp waveform as the FM internal modulating waveform source.
 Sine (1)
 A sine waveform as the FM internal modulating waveform source.
 Square (2)
 A square waveform as the FM internal modulating waveform source.
 Triangle (3)
 A triangle waveform as the FM internal modulating waveform source.
- FM Modulation Internal Frequency 
 —The frequency, in hertz, of the internal modulating waveform source for FM. This setting only affects the behavior of the instrument when the FM Source setting for a channel is set to FM Internal.

Parent topic:

Configure Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-fgen-step-dialog-box2.html language=enus -->
## TOPIC 03621: Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-fgen-step-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-fgen-step-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Channels Tab The Channels tab contains a list control with the default channels for the selected logical name. Use the Add and Remove buttons to add new channels and remove existing channels from the list. You can specify whether the function generator outputs a signal for the ch

### Edit IVI Fgen Step Dialog Box

#### Configure Operation

#### Channels Tab

The Channels tab contains a list control with the default channels for the selected logical name. Use the
 Add
 and
 Remove
 buttons to add new channels and remove existing channels from the list. You can specify whether the function generator outputs a signal for the channel by enabling the channel in the list control.

- Preserve Existing Channels 
 —When you enable this option, the step adds to or modifies any existing channels previously configured. When you disable this option, the step deletes all previously configured channels before configuring the specified channels in the list.

The Channels tab for the Configure operation also contains the following channel-specific options:

- Name 
 —The name of the channel. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.
 Output Signal Tab 
 The Output Signal tab for the Configure operation contains the following channel-specific controls: 
 
 Operation Tab 
 The Operation tab for the Configure operation contains the following channel-specific controls: 
 
 Modulation Tab 
 The Modulation tab for the Configure operation contains the following channel-specific controls:
  - Type 
 —Specifies which standard waveform the function generator produces. The supported values vary depending on the Output Mode setting on the Basic tab.
 The following values are supported values when the Output Mode is set to Standard Function: 
 
 Supported Value
 DescriptionDC (6)
 A DC waveform as the waveform type.
 Ramp Down (5)
 A negative ramp waveform as the waveform type.
 Ramp Up (4)
 A positive ramp waveform as the waveform type.
 Sine (1)
 A sine waveform as the waveform type.
 Square (2)
 A square waveform as the waveform type.
 Triangle (3)
 A triangle waveform as the waveform type. 
 
 When Output Mode is set to Arb Waveform, the Type setting specifies the name of a waveform defined on the Waveforms tab. 
 When Output Mode is set to Sequence, the Type setting specifies the name of a sequence defined on the Sequences tab.
  - Frequency 
 —The frequency of the standard waveform, in hertz, the function generator produces, or specifies the rate, in hertz, at which an entire arbitrary waveform is generated.
  - Dc Offset 
 —The DC offset of the standard waveform the function generator produces, or specifies the offset of the arbitrary waveform, in volts, the function generator produces. For standard waveforms, when the Type setting is set to DC, this setting specifies the DC level the function generator produces.
  - Amplitude 
 —The amplitude, in volts, of the standard waveform the function generator produces. When the Type setting is set to DC, this setting does not affect signal output.
  - Gain 
 —The gain of the arbitrary waveform the function generator produces. This value has no units.
  - Duty Cycle High 
 —The duty cycle for a square waveform. The value is expressed as a percentage.
  - Start Phase 
 —The start phase of the standard waveform the function generator produces. When the Type setting is set to DC, this setting does not affect signal output. The units are degrees.
  - Output Impedance 
 —The impedance of the output channel in ohms.
  - Trigger Source 
 —The trigger source for the channel. The function generator produces a signal after it receives a trigger from the source.
 
 Supported Value
 DescriptionECL0 (119)
 Specifies that the function generator waits for a trigger on the ECL 0 line before producing an output signal.
 ECL1 (120)
 Specifies that the function generator waits for a trigger on the ECL 1 line before producing an output signal.
 External (1)
 Specifies that the function generator waits for a trigger on the external trigger input terminal before producing an output signal.
 Internal (3)
 Specifies that the function generator waits for a trigger from the internal trigger source before producing an output signal.
 PXI Star (131)
 Specifies that the function generator waits for a trigger on the PXI Star line before producing an output signal.
 RTSI0 (141)
 Specifies that the function generator waits for a trigger on the RTSI 0 line before producing an output signal.
 RTSI1 (142)
 Specifies that the function generator waits for a trigger on the RTSI 1 line before producing an output signal.
 RTSI2 (143)
 Specifies that the function generator waits for a trigger on the RTSI 2 line before producing an output signal.
 RTSI3 (144)
 Specifies that the function generator waits for a trigger on the RTSI 3 line before producing an output signal.
 RTSI4 (145)
 Specifies that the function generator waits for a trigger on the RTSI 4 line before producing an output signal.
 RTSI5 (146)
 Specifies that the function generator waits for a trigger on the RTSI 5 line before producing an output signal.
 RTSI6 (147)
 Specifies that the function generator waits for a trigger on the RTSI 6 line before producing an output signal.
 Software (2)
 Specifies that the function generator waits for the Send Software Trigger operation to execute before producing an output signal.
 TTL0 (111)
 Specifies that the function generator waits for a trigger on the TTL 0 line before producing an output signal.
 TTL1 (112)
 Specifies that the function generator waits for a trigger on the TTL 1 line before producing an output signal.
 TTL2 (113)
 Specifies that the function generator waits for a trigger on the TTL 2 line before producing an output signal.
 TTL3 (114)
 Specifies that the function generator waits for a trigger on the TTL 3 line before producing an output signal.
 TTL4 (115)
 Specifies that the function generator waits for a trigger on the TTL 4 line before producing an output signal.
 TTL5 (116)
 Specifies that the function generator waits for a trigger on the TTL 5 line before producing an output signal.
 TTL6 (117)
 Specifies that the function generator waits for a trigger on the TTL 6 line before producing an output signal.
 TTL7 (118)
 Specifies that the function generator waits for a trigger on the TTL 7 line before producing an output signal.
  - Operation Mode 
 —Specifies how the function generator produces output on a channel.
 
 Supported Value
 DescriptionBurst (1)
 Used when the function generator must produce a burst of waveform cycles based on a trigger condition.
 Continuous (0)
 Used when the function generator must produce output continuously.
  - Burst Count 
 —The number of waveform cycles the function generator produces after it receives a trigger. The Burst extension group supports function generators capable of generating a discrete number of waveform cycles based on a trigger. The trigger is configured with the Trigger extension group. You can specify the number of waveform cycles to generate when a trigger event occurs. For standard and arbitrary waveforms, a cycle is one period of the waveform. For arbitrary sequences, a cycle is one complete progression through the generation of all iterations of all waveforms in the sequence.
 Note 
 This setting only affects instrument behavior when you set the Operation Mode to Burst and when you enable the Burst extension.
  - AM Modulation Enabled 
 —When you enable this option, the function generator applies amplitude modulation to the carrier waveform. The function generator applies amplitude modulation to the signal the function generator produces. You must enable the Modulate AM extension in order to use this setting.
  - AM Modulation Source 
 —The source of the signal the function generator uses as the modulating waveform for AM. This setting only affects instrument behavior when the AM Modulation Enabled setting is set to
 True 
 . You must enable the Modulate AM extension in order to use this setting.
 
 Supported Value
 DescriptionExternal (1)
 A waveform from an external source as the modulating waveform for AM.
 Internal (0)
 An internally generated waveform as the modulating waveform for AM.
  - FM Modulation Enabled 
 —When you enable this option, the function generator applies frequency modulation to the carrier waveform. The function generator applies frequency modulation to the signal the function generator produces. You must enable the Modulate FM extension in order to use this setting.
  - FM Modulation Source 
 —The source of the signal the function generator uses as the modulating waveform for FM. This setting only affects instrument behavior when the FM Modulation Enabled setting is set to
 True 
 . You must enable the Modulate FM extension in order to use this setting.
 
 Supported Value
 DescriptionExternal (1)
 A waveform from an external source as the modulating waveform for FM.
 Internal (0)
 An internally generated waveform as the modulating waveform for FM.

Parent topic:

Configure Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-fgen-step-dialog-box3.html language=enus -->
## TOPIC 03622: Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-fgen-step-dialog-box3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-fgen-step-dialog-box3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Waveforms Tab The Waveforms tab contains a list control of defined waveforms. Use the Add and Remove buttons to add new waveforms and remove existing waveforms from the list. Preserve Existing Waveforms —When you enable this option, the step adds to or modifies any existing wavef

### Edit IVI Fgen Step Dialog Box

#### Configure Operation

#### Waveforms Tab

The Waveforms tab contains a list control of defined waveforms. Use the
 Add
 and
 Remove
 buttons to add new waveforms and remove existing waveforms from the list.

- Preserve Existing Waveforms 
 —When you enable this option, the step adds to or modifies any existing waveforms previously configured. When you disable this option, the step deletes all previously configured waveforms before configuring the specified waveform in the list.

The Waveforms tab for the Configure operation also contains the following waveform-specific options:

- Name 
 —The name of the arbitrary waveform.
- Source 
 —Selects the source of the arbitrary waveform. The waveform source can be a valid ASCII or binary file format, or a waveform returned from an expression TestStand evaluates. The Filename setting specifies the relative or absolute file path. The Data Source setting specifies the expression TestStand evaluates.
 
 Supported Value
 DescriptionUse Data Source
 The arbitrary waveform source as an expression TestStand evaluates.
 2-Byte Integer
 The arbitrary waveform source as a file with 2-byte integer data.
 4-Byte Integer
 The arbitrary waveform source as a file with 4-byte integer data.
 ASCII File
 The arbitrary waveform source as a file with delimited ASCII data.
- Data Source 
 —The expression TestStand evaluates when the Source setting is Use Data Source. When TestStand evaluates the expression at run time, the expression must return an array of number. When the expression specifies a variable or property name, click
 Load 
 to import data from a file into the variable or property. Click
 Clear 
 to set the specified array property to empty. Click
 View 
 to display the data in the array property in a graph.
 The default value for the Data Source setting is
 Step.Configuration.Waveforms
 , which is an array of waveforms. Each element of the array represents the data for the waveforms specified in the list control.
- Filename 
 —The source file for the arbitrary waveform when the Source setting is a file. Files can be ASCII files with values that a variety of characters including, but not limited to, the carriage return, comma, and semicolon delimit. Additionally, files can be 2-byte or 4-byte integer binary files. Valid binary files contain a different entry every
 x 
 bytes, where
 x 
 is 2- or 4-byte depending on the file. Nothing except space explicitly delimits these binary files. For instance, if you had a 4-byte integer file containing five points, the data may appear as follows:
 Address
 Value0x0000
 0x00000001
 0x0004
 0x00000002
 0x0008
 0x00000003
 0x000C
 0x00000004
 0x0010
 0x00000005
- Auto Normalize Mode 
 —Specifies how to normalize an arbitrary waveform, if at all. Normalizing a waveform transforms the waveform so the normalized points are between the values
 -1 
 and
 1 
 . If the offset is removed, the values of the normalized points span the interval
 -1 
 to
 1 
 .
 
 Supported Value
 DescriptionNo Auto Normalize (0)
 No automatic normalization of waveform data.
 Normalize (1)
 Automatic normalization of waveform data to be between -1 and 1.
 Normalize And Remove
 Automatic normalization of Offset (2) waveform data, which forces data points to span the interval -1 to 1.

Parent topic:

Configure Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-fgen-step-dialog-box4.html language=enus -->
## TOPIC 03623: Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-fgen-step-dialog-box4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-fgen-step-dialog-box4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit IVI Fgen in the context menu for the step to launch the Edit IVI Fgen Step dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit IVI Fgen on the General tab of the Step Properties dialog box. In the Edit IVI Fgen dial

### Edit IVI Fgen Step Dialog Box

Select
 Edit IVI Fgen
 in the context menu for the step to launch the Edit IVI Fgen Step dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit IVI Fgen
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Edit IVI Fgen dialog box, select an operation for the step to perform.

Use the IVI Fgen step type to instruct function generators to generate predefined waveforms or custom waveforms using arbitrary waveform generators. The IVI Fgen step type supports the following options:

- Logical Name 
 —Selects a logical name or a virtual instrument name you configure in Measurement & Automation Explorer (MAX). Use the buttons to the right of the control to launch the
 Expression Browser 
 dialog box and to launch MAX.
 Note 
 TestStand does not install IVI-compliant instrument drivers and does not configure any sample logical names in MAX. Refer to the application help for the IVI Instruments category in MAX for more information about where to obtain and how to install IVI-compliant instrument drivers, as well as how to create the logical names IVI step types use.
 All IVI names, such as logical names, virtual names, or channel names, are case-sensitive. When you use logical names, driver session names, or virtual names in the program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters in the name.
- Operation 
 —The operation the step performs. The following operations are available when you use the IVI Fgen step type:
  - Configure 
 —Configures the instrument to match the state the step specifies.
  - Show Soft Front Panel 
 —Displays the soft front panel (SFP) for the instrument.
  - Hide Soft Front Panel 
 —Hides the SFP for the instrument.
  - Initiate 
 —Initiates signal generation when the instrument is idle.
  - Abort 
 —Aborts a previously configured output and returns the function generator to an idle state.
  - Send Software Trigger 
 —Sends a software trigger command to trigger the instrument.
  - Get Information 
 —Retrieves low-level status and information from the instrument.
- Validate 
 —Launches the
 Validate IVI Configuration 
 dialog box, in which you can validate the configuration of IVI steps.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[IVI Step Types](ivi-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Validate IVI Configuration dialog box](validate-ivi-configuration-dialog-box.html)

Parent topic:

Fgen Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-power-supply-step-dialog-box.html language=enus -->
## TOPIC 03624: Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-power-supply-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-power-supply-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Channels Tab The Channels tab contains a list control with the default channels for the selected logical name. Use the Add and Remove buttons to add new channels and remove existing channels from the list. You can specify whether the power supply outputs a signal for the channel

### Edit IVI Power Supply Step Dialog Box

#### Configure Operation

#### Channels Tab

The Channels tab contains a list control with the default channels for the selected logical name. Use the
 Add
 and
 Remove
 buttons to add new channels and remove existing channels from the list. You can specify whether the power supply outputs a signal for the channel by enabling the channel using the check box within the list control.

- Preserve Existing Channels 
 —When you enable this option, the step adds to or modifies any previously configured channels. When you disable this option, the step deletes all previously configured channels before configuring the specified channels in the list.

The Channels tab for the Configure operation also contains the following channel-specific options:

- Name 
 —The name of the channel. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.
 Output Tab 
 The Output tab for the Configure operation contains the following channel-specific controls: 
 
 Limits Tab 
 The Limits tab for the Configure operation contains the following channel-specific controls: 
 
 Trigger Tab 
 The Trigger tab for the Configure operation contains the following channel-specific controls:
  - Voltage Level (V) 
 —The voltage level, in volts, the DC power supply attempts to generate.
  - Output Range Mode 
 —Specifies how to configure the output range of the power supply on a channel.
 
 Supported Value
 DescriptionAutomatic (-1)
 The Voltage Level setting to be used to configure the range of the instrument.
 Use Current Range (0)
 The Current Range setting to be used to configure the range of the instrument.
 Use Voltage Range (1)
 The Voltage Range setting to be used to configure the range of the instrument.
  - Voltage Range (V) 
 —The maximum voltage value, in volts, of the instrument if Output Range Mode is set to Automatic or Use Voltage Range. Setting a voltage range can invalidate a previously configured current range.
  - Current Range (A) 
 —The maximum current value, in amperes, of the instrument if Output Range Mode is set to Use Current Range. Setting a current range can invalidate a previously configured voltage range.
  - Current Limit Behavior 
 —The behavior of the power supply when the output current is equal to or greater than the value of the Current Limit setting.
 
 Supported Value
 DescriptionCurrent Regulate (0)
 Indicates the output voltage restriction. The power supply restricts the output voltage so the output current is not greater than the value of the Current Limit setting.
 Current Trip (1)
 Indicates the disabling output voltage. The power supply disables the output when the output current is equal to or greater than the value of the Current Limit setting.
  - Current Limit 
 —The output current limit, in amperes. The value of the Current Limit Behavior setting determines the behavior of the power supply when the output current is equal to or greater than the value of the Current Limit setting.
  - OVP Enabled 
 —When you enable this option, the power supply provides overvoltage protection. When this property is set to
 True 
 , the power supply disables the output when the output voltage is greater than or equal to the value of the OVP Limit setting.
  - OVP Limit 
 —The maximum voltage, in volts, the power supply allows. When the OVP Enabled setting is set to
 True 
 , the power supply disables the output when the output voltage is greater than or equal to the value of the OVP Limit setting. When the OVP Enabled setting is set to
 False 
 , the OVP Limit setting does not affect the behavior of the instrument.
  - Trigger Source 
 —The trigger source. After you call Initiate, the power supply waits for a trigger event from the source you specify with the Trigger Source setting. After a trigger event occurs, the power supply changes the voltage level to the value of the Triggered Voltage Level setting and the current limit to the value of the Triggered Current Limit setting.
 
 Supported Value
 DescriptionSoftware (2)
 Indicates the power supply waits for the Send Software Trigger operation to execute before changing the output signal.
 ECL0 (11)
 Indicates the power supply waits for a trigger on the ECL 0 line before changing the output signal.
 ECL1 (12)
 Indicates the power supply waits for a trigger on the ECL 1 line before changing the output signal.
 External (1)
 Indicates the power supply waits for an external trigger before changing the output signal.
 Immediate (0)
 Indicates the power supply does not wait for a trigger before changing the output signal.
 PXI Star (13)
 Indicates the power supply waits for a trigger on the PXI STAR line before changing the output signal.
 RTSI0 (14)
 Indicates the power supply waits for a trigger on the RTSI 0 line before changing the output signal.
 RTSI1 (15)
 Indicates the power supply waits for a trigger on the RTSI 1 line before changing the output signal.
 RTSI2 (16)
 Indicates the power supply waits for a trigger on the RTSI 2 line before changing the output signal.
 RTSI3 (17)
 Indicates the power supply waits for a trigger on the RTSI 3 line before changing the output signal.
 RTSI4 (18)
 Indicates the power supply waits for a trigger on the RTSI 4 line before changing the output signal.
 RTSI5 (19)
 Indicates the power supply waits for a trigger on the RTSI 5 line before changing the output signal.
 RTSI6 (20)
 Indicates the power supply waits for a trigger on the RTSI 6 line before changing the output signal.
 TTL0 (3)
 Indicates the power supply waits for a trigger on the TTL 0 line before changing the output signal.
 TTL1 (4)
 Indicates the power supply waits for a trigger on the TTL 1 line before changing the output signal.
 TTL2 (5)
 Indicates the power supply waits for a trigger on the TTL 2 line before changing the output signal.
 TTL3 (6)
 Indicates the power supply waits for a trigger on the TTL 3 line before changing the output signal.
 TTL4 (7)
 Indicates the power supply waits for a trigger on the TTL 4 line before changing the output signal.
 TTL5 (8)
 Indicates the power supply waits for a trigger on the TTL 5 line before changing the output signal.
 TTL6 (9)
 Indicates the power supply waits for a trigger on the TTL 6 line before changing the output signal.
 TTL7 (10)
 Indicates the power supply waits for a trigger on the TTL 7 line before changing the output signal.
  - Triggered Current Limit 
 —The value, in amperes, to which the power supply sets the current limit after a trigger event occurs. After you call Initiate, the power supply waits for a trigger event from the source you specify with the Trigger Source setting. After a trigger event occurs, the power supply sets the current limit to the value of the Triggered Current Limit setting. After a trigger occurs, the value of the Current Limit setting reflects the new value to which the current limit has been set.
  - Triggered Voltage Level 
 —The value, in volts, to which the power supply sets the voltage level after a trigger event occurs. After you call Initiate, the power supply waits for a trigger event from the source you specify with the Trigger Source setting. After a trigger event occurs, the power supply sets the voltage level to the value of the Triggered Voltage Level setting.
 After a trigger occurs, the value of the Voltage Level setting reflects the new value to which the voltage level has been set.

Parent topic:

Configure Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-power-supply-step-dialog-box2.html language=enus -->
## TOPIC 03625: Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-power-supply-step-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-power-supply-step-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation The Get Information operation retrieves low-level status and information from the power supply. You can determine whether an instrument is in constant current mode, or if an overcurrent, overvoltage, or unregulated condition exists in the instrument. You can also query the

### Edit IVI Power Supply Step Dialog Box

#### Get Information Operation

The Get Information operation retrieves low-level status and information from the power supply. You can determine whether an instrument is in constant current mode, or if an overcurrent, overvoltage, or unregulated condition exists in the instrument. You can also query the instrument for the maximum programmable voltage or current level the power supply accepts on a channel. You must specify an expression that contains a variable or property to which the step assigns the retrieved value.

The Get Information operation contains the following options:

- Channel Name 
 —The name of the channel to operate on. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.
- Query Max Current Limit 
 —Queries the maximum programmable current limit the power supply accepts for a particular voltage level on a channel.
  - Voltage Level (Input) 
 —The voltage level for which you want to find the maximum programmable current limit.
  - Max Current Limit (Output) 
 —A variable or property to which the step assigns the maximum programmable current limit.
- Query Max Voltage Level 
 —Queries the maximum programmable voltage level the power supply accepts for a particular current limit on a channel.
  - Voltage Level (Input) 
 —The current limit for which you want to find the maximum programmable voltage level.
  - Max Voltage Level (Output) 
 —A variable or property to which the step assigns the maximum voltage level.
- Query Output State 
 —Queries the value of a specified DC power supply output state.
  - Output State 
 —The output state to query.
 
 Supported Value
 DescriptionConstant Current (1)
 Determines whether an instrument is in constant current mode. A constant current condition occurs when the output current is equal to the value of the Current Limit setting and the Current Limit Behavior setting is set to Current Regulate.
 Constant Voltage (0)
 Determines whether an instrument is in constant voltage mode. A constant voltage condition occurs when the output voltage is equal to the value of the Voltage Level setting and the current is less than or equal to the value of the Current Limit setting.
 Over Current (3)
 Determines whether an overcurrent condition exists in the instrument. An overcurrent condition occurs when the output current is equal to or greater than the value of the Current Limit setting and the Current Limit Behavior property is set to Current Trip.
 Over Voltage (2)
 Determines whether an overvoltage condition exists in the instrument. An overvoltage condition occurs when the output voltage is equal to or greater than the value of the OVP Limit setting and the OVP Enabled setting is set to
 True
 .
 Unregulated (4)
 Determines whether an unregulated condition exists in the instrument. An unregulated condition occurs when the output voltage is less than the value of the Voltage Level setting and the current is less than the value of the Current Limit setting.
  - Value 
 —A Boolean variable or property to which the step assigns the output state.
 When either an overvoltage condition or an overcurrent condition occurs, the output protection of the power supply disables the output. When the power supply is in an overvoltage or overcurrent state, it does not produce power until the output protection is reset. The Reset Output Protection operation resets the output protection. Once the output protection is reset, the power supply resumes generating a power signal. 
 Note 
 Some drivers might not support the querying of all the output states. Reset Output Protection may not be supported with all drivers.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-power-supply-step-dialog-box3.html language=enus -->
## TOPIC 03626: Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-power-supply-step-dialog-box3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-power-supply-step-dialog-box3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measure Operation Channels Tab The Channels tab contains a list control with the default channels for the selected logical name. Use the Add and Remove buttons to add new channels and remove existing channels from the list. You can specify whether the power supply measures the output for the channel

### Edit IVI Power Supply Step Dialog Box

#### Measure Operation

#### Channels Tab

The Channels tab contains a list control with the default channels for the selected logical name. Use the
 Add
 and
 Remove
 buttons to add new channels and remove existing channels from the list. You can specify whether the power supply measures the output for the channel enabling the channel in the list control.

The Channels tab for the Measure operation also contains the following channel-specific options:

- Name 
 —The name of the channel to read. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.
- Measurement Type 
 —The type of data to retrieve from the oscilloscope.
 
 Supported Value
 DescriptionCurrent (0)
 Indicates the current is measured at the output terminals.
 Voltage (1)
 Indicates the voltage is measured at the output terminals.
- Measurement Destination 
 —A variable or property to which the step assigns the measurement value. The data type of the variable or property must be Number or NI_IviSinglePoint. The default configuration for the step specifies
 Step.Result.Reading 
 as the destination. This property is an array of container, and the size of the array is equal to the number of channels specified for the Measure operation. When you edit the step, the step automatically resizes the array.
 Note 
 If you do not specify
 Step.Result.Reading
 as the destination, TestStand copies the measurement value to the Data subproperty in each array element at run time.

Parent topic:

Measure Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-power-supply-step-dialog-box4.html language=enus -->
## TOPIC 03627: Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-power-supply-step-dialog-box4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-power-supply-step-dialog-box4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit IVI Power Supply in the context menu for the step to launch the Edit IVI Power Supply Step dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit IVI Power Supply on the General tab of the Step Properties dialog box. I

### Edit IVI Power Supply Step Dialog Box

Select
 Edit IVI Power Supply
 in the context menu for the step to launch the Edit IVI Power Supply Step dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit IVI Power Supply
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Edit IVI Power Supply dialog box, select an operation for the step to perform.

The IVI Power Supply step type supports the following options:

- Logical Name 
 —Selects a logical name or a virtual instrument name you configure in Measurement & Automation Explorer (MAX). You can use the buttons to the right of the control to launch the
 Expression Browser 
 dialog box and to launch MAX.
 Note 
 TestStand does not install IVI-compliant instrument drivers and does not configure any sample logical names in MAX. Refer to the application help for the IVI Instruments category in MAX for more information about where to obtain and how to install IVI-compliant instrument drivers, as well as how to create the logical names IVI step types use.
 All IVI names, such as logical names, virtual names, or channel names, are case-sensitive. When you use logical names, driver session names, or virtual names in the program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters in the name.
- Operation 
 —The operation the step performs. The following operations are available to you using the IVI Power Supply step type:
  - Configure 
 —Configures the instrument to match the state the step specifies.
  - Show Soft Front Panel 
 —Shows the soft front panel (SFP) for the instrument.
  - Hide Soft Front Panel 
 —Hides the SFP for the instrument.
  - Measure 
 —Takes a measurement on the output signal and returns the measured value.
  - Initiate 
 —Directs the power supply to wait for a trigger.
  - Abort 
 —Cancels the wait for a trigger.
  - Send Software Trigger 
 —Sends a software trigger command to trigger the instrument.
  - Reset Output Protection 
 —Resets the output protection feature after an overvoltage or overcurrent condition occurs.
  - Get Information 
 —Retrieves low-level status and information from the instrument.
- Validate 
 —Launches the
 Validate IVI Configuration 
 dialog box, in which you can validate the configuration of IVI steps.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[IVI Step Types](ivi-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Validate IVI Configuration dialog box](validate-ivi-configuration-dialog-box.html)

Parent topic:

Power Supply Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-scope-step-dialog-box.html language=enus -->
## TOPIC 03628: Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-scope-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-scope-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit IVI Scope in the context menu for the step to launch the Edit IVI Scope Step dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click the Edit IVI Scope button on the General tab of the Step Properties dialog box. In the Edit

### Edit IVI Scope Step Dialog Box

Select
 Edit IVI Scope
 in the context menu for the step to launch the Edit IVI Scope Step dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click the
 Edit IVI Scope
 button on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Edit IVI Scope dialog box, select an operation for the step to perform.

The IVI Scope step type supports the following options:

- Logical Name 
 —Selects a logical name or a virtual instrument name you configure in Measurement & Automation Explorer (MAX). Use the buttons to the right of the control to launch the
 Expression Browser 
 dialog box and to launch MAX.
 Note 
 TestStand does not install IVI-compliant instrument drivers and does not configure any sample logical names in MAX. Refer to the application help for the IVI Instruments category in MAX for more information about where to obtain and how to install IVI-compliant instrument drivers, as well as how to create the logical names IVI step types use.
 All IVI names, such as logical names or virtual names, are case-sensitive. When you use logical names, driver session names, or virtual names in the program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters in the name.
- Operation 
 —The operation the step performs. The following operations are available when you use the IVI Scope step type:
  - Configure 
 —Configures the instrument to match the state the step specifies.
  - Show Soft Front Panel 
 —Displays the soft front panel (SFP) for the instrument.
  - Hide Soft Front Panel 
 —Hides the SFP for the instrument.
  - Read 
 —Initiates and returns a measurement from the instrument.
  - Initiate 
 —Initiates a measurement.
  - Fetch 
 —Returns a measured value from a measurement the Initiate operation has started.
  - Abort 
 —Cancels the wait for a trigger.
  - Auto Setup 
 —Performs an automatic setup on the instrument.
  - Get Information 
 —Retrieves low-level status and information from the instrument.
- Validate 
 —Launches the
 Validate IVI Configuration 
 dialog box, in which you can validate the configuration of IVI steps.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[IVI Step Types](ivi-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Validate IVI Configuration dialog box](validate-ivi-configuration-dialog-box.html)

Parent topic:

Scope Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-switch-step-dialog-box.html language=enus -->
## TOPIC 03629: Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-switch-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-switch-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit IVI Switch in the context menu for the step to launch the Edit IVI Switch Step dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click the Edit IVI Switch button on the General tab of the Step Properties dialog box. Use the

### Edit IVI Switch Step Dialog Box

Select
 Edit IVI Switch
 in the context menu for the step to launch the Edit IVI Switch Step dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click the
 Edit IVI Switch
 button on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. Use the IVI Switch step type to connect and disconnect paths or routes, determine the connectivity of two switches or the state of the route, and query the state of the switch module or virtual device.

The IVI Switch step type also has the following two different modes:

- IVI Switching Mode
- Switch Executive Mode

The mode you select determines the operations available when you use the IVI Switch step type.

The IVI Switch step type supports the following options:

- Logical Name 
 —Selects a logical name or a virtual instrument name for an IVI Switch you configure in Measurement & Automation Explorer (MAX). Use the buttons to the right of the control to launch the
 Expression Browser 
 dialog box and to launch MAX. This control is available only when you are using the IVI Switching Mode.
 Note 
 TestStand does not install IVI-compliant instrument drivers and does not configure any sample logical names in MAX. Refer to the application help for the IVI Instruments category in MAX for more information about where to obtain and how to install IVI-compliant instrument drivers, as well as how to create the logical names IVI step types use.
 All IVI names, such as logical names, virtual names, or channel names, are case-sensitive. When you use logical names, driver session names, or virtual names in the program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters in the name.
- Virtual Device Name 
 —Selects a virtual device name you configure in NI Switch Executive within MAX. You can use the buttons to the right of the control to launch
 Expression Browser 
 dialog box and to launch MAX.
 Note 
 This control is available only when using Switch Executive Mode.
TestStand does not release an NI Switch Executive virtual device until all executions that use the device complete and close.
- Operation 
 —The operation the step performs.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[IVI Step Types](ivi-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Switch Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-ivi-tools-step-dialog-box.html language=enus -->
## TOPIC 03630: Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-ivi-tools-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-ivi-tools-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit IVI Tools in the context menu for the step to launch the Edit IVI Tools Step dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit IVI Tools on the General tab of the Step Properties dialog box. In the Edit IVI Tools

### Edit IVI Tools Step Dialog Box

Select
 Edit IVI Tools
 in the context menu for the step to launch the Edit IVI Tools Step dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit IVI Tools
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Edit IVI Tools dialog box, select an operation for the step to perform.

Use the IVI Tools step type to perform low-level operations on an instrument. The IVI Tools step type supports the following options:

- Logical Name 
 —Selects a logical name or a virtual instrument name you configure in Measurement & Automation Explorer (MAX). Use the buttons to the right of the control to launch the Browse for Expression dialog box and to launch MAX.
 Note 
 TestStand does not install IVI-compliant instrument drivers and does not configure any sample logical names in MAX. Refer to the application help for the IVI Instruments category in MAX for more information about where to obtain and how to install IVI-compliant instrument drivers, as well as how to create the logical names IVI step types use.
 All IVI names, such as logical names, virtual names, or channel names, are case-sensitive. When you use logical names, driver session names, or virtual names in the program, you must ensure the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters in the name.
- Operation 
 —The operation the step performs. The following operations are available when you use the IVI Tools step type:
  - Get Session Info 
 —Retrieve low-level session references and API class handles for the IVI instrument.
  - Show Soft Front Panel 
 —Displays the soft front panel (SFP) for the tool.
  - Hide Soft Front Panel 
 —Hides the SFP for the tool.
  - Init 
 —Initializes the driver or I/O resource for the session.
  - Close 
 —Closes the IVI session.
  - Reset 
 —Places the instrument in a known state.
  - Self Test 
 —Causes the instrument to perform a self test.
  - Revision Query 
 —Queries the instrument driver and instrument for revision information.
  - Error Query 
 —Returns instrument-specific error information.
  - Get Error Info 
 —Returns error information for the last IVI error for a session.
  - Set/Get/Check Attributes 
 —Sets, queries, or verifies the value of attributes.

#### See Also

[IVI Step Types](ivi-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Tools Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-label-step-dialog-box.html language=enus -->
## TOPIC 03631: Edit Label Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-label-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-label-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Label Step in the context menu for the step or click Edit Label Step on the General tab of the Step Properties dialog box to launch the Edit Label Step dialog box from a TestStand User Interface . The Edit Label Step dialog box contains the following options: Label Description —The descr

### Edit Label Step Dialog Box

Select
 Edit Label Step
 in the context menu for the step or click
 Edit Label Step
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit Label Step dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Edit Label Step dialog box contains the following options:

- Label Description 
 —The description for the step.
- Hide Icon 
 —When you enable this option, the Label step icon is not visible in the Step column.
- Hide Name 
 —When you enable this option, the step name is not visible in the Step column.
- Hide Status and Result 
 —When you enable this option, the
 step status 
 evaluates to a string containing a single white space character, and the step result is disabled.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Label Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-labview-nxg-vi-call-dialog-box.html language=enus -->
## TOPIC 03632: Edit LabVIEW NXG VI Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-labview-nxg-vi-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-labview-nxg-vi-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the LabVIEW Adapter and select Specify Module from the context menu to launch the Edit LabVIEW NXG VI Call dialog box from a TestStand User Interface . You can also select Properties from the context menu. When you select Properties , you must click Specify Module in

### Edit LabVIEW NXG VI Call Dialog Box

Insert a step configured to use the LabVIEW Adapter and select
 Specify Module
 from the context menu to launch the Edit LabVIEW NXG VI Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu. When you select
 Properties
 , you must click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit LabVIEW VI Call dialog box.

The Edit LabVIEW NXG VI Call dialog box contains the following tabs:

- Module 
 —Contains the same options and layout as the
 LabVIEW NXG Module 
 tab in the
 TestStand Sequence Editor 
 .
- Advanced Settings 
 —Contains the same options and layout as the
 LabVIEW NXG Advanced Settings 
 window in the sequence editor.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-labview-vi-call-dialog-box.html language=enus -->
## TOPIC 03633: Edit LabVIEW VI Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-labview-vi-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-labview-vi-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the LabVIEW Adapter and select Specify Module from the context menu to launch the Edit LabVIEW VI Call dialog box from a TestStand User Interface . You can also select Properties from the context menu. When you select Properties , you must click Specify Module in the

### Edit LabVIEW VI Call Dialog Box

Insert a step configured to use the LabVIEW Adapter and select
 Specify Module
 from the context menu to launch the Edit LabVIEW VI Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu. When you select
 Properties
 , you must click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit LabVIEW VI Call dialog box.

The Edit LabVIEW VI Call dialog box contains the following tabs:

- Module 
 —Contains the same options and layout as the
 LabVIEW Module 
 tab in the
 TestStand Sequence Editor 
 .
- Advanced Settings 
 —Contains the same options and layout as the
 LabVIEW Advanced Settings 
 window in the sequence editor.
- Override Module Settings 
 —Contains the same options and layout as the
 Override Module Settings 
 window in the sequence editor.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[Updating VI Dependencies](/csh?context=ts_tsref_updating_vi_dependencies)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-labwindows-cvi-module-call-dialog-box.html language=enus -->
## TOPIC 03634: Edit LabWindows/CVI Module Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-labwindows-cvi-module-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-labwindows-cvi-module-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the LabWindows/CVI Adapter and select Specify Module from the context menu to launch the Edit LabWindows/CVI Module Call dialog box from a TestStand User Interface . You can also select Properties from the context menu and then click Specify Module in the Step Propert

### Edit LabWindows/CVI Module Call Dialog Box

Insert a step configured to use the LabWindows/CVI Adapter and select
 Specify Module
 from the context menu to launch the Edit LabWindows/CVI Module Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu and then click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit LabWindows/CVI Module Call dialog box.

The Edit LabWindows/CVI Module Call dialog box contains the following tabs:

- Module 
 —The
 code module 
 the adapter executes for the step.
- Source Code 
 —Additional information TestStand requires for creating and editing a code module in LabWindows/CVI.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-legacy-property-loader-dialog-box.html language=enus -->
## TOPIC 03635: Edit Legacy Property Loader Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-legacy-property-loader-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-legacy-property-loader-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database Data The Edit Property Loader dialog box contains the following tabs when you select Database in the Data Location ring control: Properties —The mapping between step properties and column names of the statement in the database. Filtering —When you enable this option, TestStand filters the d

### Edit Legacy Property Loader Dialog Box

#### Database Data

The Edit Property Loader dialog box contains the following tabs when you select Database in the Data Location ring control:

- Properties 
 —The mapping between step properties and column names of the statement in the database.
- Filtering 
 —When you enable this option, TestStand filters the data returned from the database before loading values.

Parent topic:

Edit Legacy Property Loader Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-legacy-property-loader-dialog-box2.html language=enus -->
## TOPIC 03636: Edit Legacy Property Loader Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-legacy-property-loader-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-legacy-property-loader-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: File Data The Edit Property Loader dialog box contains the following tabs when you select File in the Data Location ring control: Properties —The mapping between step properties and column names in the file. Source —The file pathname and the format of the data in the file.

### Edit Legacy Property Loader Dialog Box

#### File Data

The Edit Property Loader dialog box contains the following tabs when you select File in the Data Location ring control:

- Properties 
 —The mapping between step properties and column names in the file.
- Source 
 —The file pathname and the format of the data in the file.

Parent topic:

Edit Legacy Property Loader Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-legacy-property-loader-dialog-box3.html language=enus -->
## TOPIC 03637: Edit Legacy Property Loader Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-legacy-property-loader-dialog-box3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-legacy-property-loader-dialog-box3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Property Loader in the context menu for the step to launch the Edit Property Loader dialog box from the TestStand Sequence Editor or a TestStand User Interface . For a user interface, you can also click Edit Property Loader on the General tab of the Step Properties dialog box. When the P

### Edit Legacy Property Loader Dialog Box

Select
 Edit Property Loader
 in the context menu for the step to launch the Edit Property Loader dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . For a user interface, you can also click
 Edit Property Loader
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

When the
 [Property Loader step](legacy-property-loader-step.html)
 imports property and variable values into the currently executing sequence, value changes apply only to the run-time copy of the sequence. If TestStand executes the sequence again, TestStand resets the local variables and might reset custom step properties back to the default values the edit-time copy of the sequence specifies. The Property Loader step must reinitialize values each time TestStand calls the sequence to ensure that TestStand uses the loaded values. Place a Property Loader step in the Setup
 [step group](/csh?context=ts_tsfundamentals_bldgblocks_stepgroups)
 of a sequence before any steps in the sequence execute so that the Property Loader step initializes the property and variable values TestStand uses in the sequence.

If the Property Loader step imports property and variable values into a specific sequence or multiple sequences in a sequence file, TestStand applies the new values to all subsequent invocations of the sequence in an execution. The Property Loader step must initialize values only once per execution. For example, a Property Loader step in the Test UUTs Process Model
 [entry point](/csh?context=ts_tsfundamentals_bldgblocks_entrypoints)
 sequence can import values into all sequences in the client sequence file once before executing multiple UUTs in a loop. When the specific sequence on which the step operates is the currently executing sequence, the step applies imported values to the running sequence and subsequence invocations of the sequence.

If you are loading from a database, TestStand selects the property and variable values from the statement an
 [Open SQL Statement](open-sql-statement-step.html)
 step returns. The SQL data the Open SQL Statement step returns is in table format, where each row pertains to a particular sequence step or to a variable scope. The column headings are the names of properties in the steps or variables in the scope. Not all columns apply to each row. Each row contains values for only the columns that define properties or variables defined within the step or variable scope for the row.

The Property Loader step can filter the data the SQL Statement step returns so you can load values only from rows that contain specific column values, such as those for a specific sequence.

Note

The Edit Property Loader Step Type dialog box contains the following tabs:

- File Data
  - Properties Tab
  - Source Tab
- Database Data
  - Properties Tab
  - Filtering Tab

Select
 Tools»Import/Export Properties
 to launch the
 [Import/Export Properties](legacy-import-export-properties-dialog-box.html)
 dialog box, in which you can export property and variable data in the appropriate table format.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Import/Export Properties dialog box](legacy-import-export-properties-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Legacy Property Loader Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-menu-execution-profiler.html language=enus -->
## TOPIC 03638: Edit Menu - Execution Profiler

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-menu-execution-profiler.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-menu-execution-profiler.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edit Menu The Edit menu contains the following options, some of which are also available in the context menus for the profiler window tables and profiler window graphs . Copy —If the active display is a graph, this option places the entire image of the graph on the clipboard, including the portions

### Edit Menu - Execution Profiler

#### Edit Menu

The Edit menu contains the following options, some of which are also available in the context menus for the
 [profiler window tables](profiler-window-tables.html)
 and
 [profiler window graphs](/csh?context=ts_tsref_resource_usage_profiler_graphs)
 .

- Copy 
 —If the active display is a graph, this option places the entire image of the graph on the clipboard, including the portions not currently visible because of the scroll position. If the active display is a table, this item copies the text of the selected rows to the clipboard along with the column headings for the table.
- Delete 
 —Deletes all profiler events associated with the current selection.
- Select All 
 —Selects all the rows in the active table, or all the operations in the active graph.
- Select Operations that Overlap the Selection 
 —Selects every operation that intersects with the range of time that encompasses the selected operations. You can use this command to help select operations that relate to a higher level operation such as a UUT, Batch, or Step.
- Select Operations within the Selection 
 —Selects every operation that is fully contained by the range of time that
encompasses the selected operations. You can use this command to help select operations that relate to a higher level
operation such as a UUT, Batch, or Step.
- Invert Selection 
 —This command deselects the selected operations and selects all unselected operations. You can use this command to select and then delete information you are not interested by first selecting the operations you want to keep and then inverting the selection before choosing to Delete.
- Move Selected Operations 
 —Displays the
 Move Selected Operations 
 dialog box.
- Diff Selected Threads 
 —Displays the
 Diff Selected Threads 
 dialog box.

#### See Also

[Profiler Window Graphs](/csh?context=ts_tsref_resource_usage_profiler_graphs)

[Profiler Window Tables](profiler-window-tables.html)

Parent topic:

Menus - Execution Profiler

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-menu.html language=enus -->
## TOPIC 03639: Edit Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Edit menu in the TestStand Sequence Editor contains the following items, which are used for editing sequences and steps: Undo —Removes the last edit you performed in the current document. Redo —Performs the last edit removed using the Undo command. the TestStand Sequence Editor maintains a list

### Edit Menu

The Edit menu in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 contains the following items, which are used for editing sequences and steps:

- Undo 
 —Removes the last edit you performed in the current document.
- Redo 
 —Performs the last edit removed using the Undo command.
 Note 
 the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 maintains a list of edits you previously performed on each file. If you edit a step type or data type a file uses, or if a custom tool menu performs edits to a file, the sequence editor clears the list of undoable edits for the file. If you want to be able to undo these types of change to a file, you must save the file before performing them.
 When you attempt to perform an undo or redo operation and an edit operation was performed that the sequence editor does not recognize, the sequence editor prompts you to inform you that the undo or redo operation could not be performed.
- Cut 
 —Removes the selected text or object and places it on the clipboard.
- Copy 
 —Copies the selected text or object to the clipboard.
- Paste 
 —Inserts text or an object from the clipboard.
- Delete 
 —Deletes the selected text or object.
- Rename 
 —Renames the text of the selected item.
- Select All 
 —Highlights all the objects in the active window or pane.
- Diff Sequence File Against 
 —Compares the selected sequence file with another sequence file. The
 TestStand File Diff and Merge 
 utility launches and shows the differences between the two files. As you view the differences, you can transfer individual changes between the files.
- Diff Against Saved Version 
 —Compares the current, in-memory version of the sequence file you select with the version last saved to disk. The TestStand File Diff and Merge utility launches and shows the differences.
- Find/Replace 
 —Launches the
 Find/Replace 
 dialog box, in which you can search for a string within a file or view in the sequence editor window.
- Find/Replace in Files 
 —Launches the
 Find/Replace in Files 
 dialog box, in which you can search for a string within one or more files.
- Find Previous 
 —Selects the previous match from the last active and open
 Find Results 
 pane. Use the <Ctrl+Shift+G>
 keyboard shortcut 
 for this command for increased efficiency when reviewing matches.
- Find Next 
 —Selects the next match from the last active and open Find Results pane. Use the <Ctrl+G> keyboard shortcut with this command for increased efficiency when reviewing matches.
- Sequence Properties 
 —Launches the
 Sequence Properties 
 dialog box, in which you can edit the properties for a selected sequence in the active Sequence File window.
- Sequence File Properties 
 —Launches the
 Sequence File Properties 
 dialog box, in which you can view the pathname, disk size, and disk date of the active sequence file. You can also use this dialog box to edit various properties of a sequence file, including the load and unload options, comment, and the sequence file type. If the sequence file type is normal, you can also specify a process model file for the sequence file.
- Sequence File Callbacks 
 —Launches the
 Sequence File Callbacks 
 dialog box, which displays all the callback sequences you can override in the sequence file. This includes the
 Engine callbacks 
 TestStand defines and the
 Model callbacks 
 the process model for the sequence file defines.

#### See Also

[Find/Replace dialog box](find-replace-dialog-box.html)

[Find/Replace in Files dialog box](find-replace-in-files-dialog-box.html)

[Sequence File Callbacks dialog box](select-sequence-file-callbacks-dialog-box.html)

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html)

Parent topic:

Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-menu2.html language=enus -->
## TOPIC 03640: Edit Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-menu2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-menu2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Edit menu in a TestStand User Interface contains the following options for editing sequences and steps: Menu items marked with an asterisk ( * ) appear only in Editor Mode. Undo* —Removes the last edit you performed in the current document. Redo* —Performs the last edit removed using the Undo co

### Edit Menu

TestStand User Interface

Note

*

- Undo* 
 —Removes the last edit you performed in the current document.
- Redo* 
 —Performs the last edit removed using the Undo command.
- Cut* 
 —Removes the selected text or object and places it on the clipboard.
- Copy 
 —Copies the selected text or object to the clipboard.
- Paste* 
 —Inserts text or an object from the clipboard.
- Delete* 
 —Deletes the selected text or object.
- Rename* 
 —Renames the text of the selected item.
- Select All 
 —Highlights all the objects in the active window or pane.
- Edit* 
 —The full name of the Edit menu item varies according to the type of the selected step. For example, the menu item name is Edit Message Settings for a Message Popup step, Edit Limits for a Numeric Limit Test step, and Edit Destination for a Goto step. For each step, the menu item invokes a dialog box in which you edit the settings that are unique to the type of the step. Some step types, such as the Label step and the Action step, do not have step-type-specific settings. For these step types, this menu item does not appear. A step type can provide more than one Edit menu item.
- Specify Module* 
 —Launches a
 Specify Module 
 dialog box for the selected step, depending on the module adapter for the step. Use the Specify Module dialog box to specify the
 code module 
 the step calls. You can also specify options TestStand uses when it calls the step.
- Edit Code* 
 —Displays the source code for the code module the step calls. TestStand uses the module adapter for the step to determine the appropriate application in which to display the source code.
- Preconditions* 
 —Launches the
 Preconditions 
 dialog box, in which you can specify the conditions that must be true for each step in the sequence to run.
- Sequence File Callbacks* 
 —Launches the
 Sequence File Callbacks 
 dialog box, which displays all the callback sequences you can override in the sequence file. This includes the Engine callbacks TestStand defines and the Model callbacks the process model for the sequence file defines.
- Step Properties* 
 —Launches the
 Step Properties 
 dialog box, in which you can view and edit the properties for the selected step.
- Sequence Properties* 
 —Launches the
 Sequence Properties 
 dialog box, in which you can edit the properties for the selected sequence.
- Sequence File Properties* 
 —Launches the
 Sequence File Properties 
 dialog box, in which you can view the pathname, disk size, and disk date of the active sequence file. You can also use this dialog box to edit various properties of a sequence file, including the load and unload options, comment, and the sequence file type. If the sequence file type is normal, you can also specify a process model file for the sequence file.

#### See Also

[Preconditions dialog box](preconditions-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Sequence File Callbacks dialog box](select-sequence-file-callbacks-dialog-box.html)

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Specify Module Tabs and Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-multiple-numeric-limit-test-dialog-box.html language=enus -->
## TOPIC 03641: Edit Multiple Numeric Limit Test Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-multiple-numeric-limit-test-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-multiple-numeric-limit-test-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Limits in the context menu for the step or click Edit Limits on the General tab of the Step Properties dialog box to launch the Edit Multiple Numeric Limit Test dialog box from a TestStand User Interface . Use this dialog box to customize the type of comparison and limits TestStand uses

### Edit Multiple Numeric Limit Test Dialog Box

Select
 Edit Limits
 in the context menu for the step or click
 Edit Limits
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit Multiple Numeric Limit Test dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to customize the type of comparison and limits TestStand uses to set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 .

The Edit Multiple Numeric Limit Test dialog box contains the following tabs:

- Limits 
 —Specifies for each measurement the type of limit comparison the step performs, the limit values the step uses, as well as the format and units of the value and limits.
- Data Source 
 —The data source for the measurement value the step compares to limit values.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Test Step Types](test-step-types.html)

Parent topic:

Multiple Numeric Limit Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-net-call-dialog-box.html language=enus -->
## TOPIC 03642: Edit .NET Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-net-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-net-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the .NET Adapter and select Specify Module from the context menu to launch the Edit .NET Call dialog box from a TestStand User Interface . You can also select Properties from the context menu. When you select Properties , you must click Specify Module in the Step Prop

### Edit .NET Call Dialog Box

Insert a step configured to use the .NET Adapter and select
 Specify Module
 from the context menu to launch the Edit .NET Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu. When you select
 Properties
 , you must click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch this dialog box.

The Edit .NET Call dialog box contains the following tabs:

- Module 
 —The
 code module 
 the .NET Adapter executes for the step and specifies the parameter information for the module.
- Source Code 
 —Additional information TestStand requires for creating and editing a code module in another application.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-numeric-limit-test-dialog-box.html language=enus -->
## TOPIC 03643: Edit Numeric Limit Test Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-numeric-limit-test-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-numeric-limit-test-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Limits in the context menu for the step or click Edit Limits on the General tab of the Step Properties dialog box to launch the Edit Numeric Limit Test dialog box from a TestStand User Interface . Use this dialog box to customize the type of comparison and limits TestStand uses to set th

### Edit Numeric Limit Test Dialog Box

Select
 Edit Limits
 in the context menu for the step or click
 Edit Limits
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit Numeric Limit Test dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to customize the type of comparison and limits TestStand uses to set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 .

The Edit Numeric Limit Test dialog box contains the following tabs:

- Limits 
 —The type of limit comparison the step performs, the limit values the step uses, as well as the format and units of the value and limits.
- Data Source 
 —The data source for the measurement value the step compares to limit values.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Test Step Types](test-step-types.html)

Parent topic:

Numeric Limit Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-open-database-dialog-box.html language=enus -->
## TOPIC 03644: Edit Open Database Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-open-database-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-open-database-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Open Database in the context menu for the step to launch the Edit Open Database dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit Open Database on the General tab of the Step Properties dialog box. The Edit Open D

### Edit Open Database Dialog Box

Select
 Edit Open Database
 in the context menu for the step to launch the Edit Open Database dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit Open Database
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Edit Open Database dialog box contains the following tab:

- Data Link 
 —The connection string TestStand uses to open a data source.

#### See Also

[Database Step Types](database-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Open Database Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-open-sql-statement-dialog-box.html language=enus -->
## TOPIC 03645: Edit Open SQL Statement Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-open-sql-statement-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-open-sql-statement-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Open SQL Statement in the context menu for the step to launch the Edit Open SQL Statement dialog box from the TestStand Sequence Editor or a TestStand User Interface . From a user interface, you can also click Edit Open SQL Statement on the General tab of the Step Properties dialog box.

### Edit Open SQL Statement Dialog Box

Select
 Edit Open SQL Statement
 in the context menu for the step to launch the Edit Open SQL Statement dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 . From a user interface, you can also click
 Edit Open SQL Statement
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Edit Open SQL Statement dialog box contains the following tabs:

- SQL Statement 
 —The SQL statement the step opens and whether parameters are required.
- Advanced 
 —Optional attributes on the opened SQL statement.

#### See Also

[Database Step Types](database-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Open SQL Statement Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-pass-fail-source-dialog-box.html language=enus -->
## TOPIC 03646: Edit Pass/Fail Source Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-pass-fail-source-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-pass-fail-source-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Pass/Fail Source in the context menu for the step or click Edit Pass/Fail Source on the General tab of the Step Properties dialog box to launch the Edit Pass/Fail Source dialog box from a TestStand User Interface . Use this dialog box to customize the Boolean expression that determines w

### Edit Pass/Fail Source Dialog Box

Select
 Edit Pass/Fail Source
 in the context menu for the step or click
 Edit Pass/Fail Source
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit Pass/Fail Source dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . Use this dialog box to customize the Boolean expression that determines whether the step passes.

The Edit Pass/Fail Source dialog box contains the following options:

- Data Source Expression 
 —A Boolean expression the step uses to determine whether the step passes or fails. The default value is
 Step.Result.PassFail 
 . You can customize this expression if you do not want to set the value of
 Step.Result.PassFail 
 in the
 code module 
 . For example, you can set the data source expression to refer to multiple variables and properties such as,
 RunState.PreviousStep.Result.Numeric * Locals.Attenuation > 12 
 .
- Set to Default 
 —Sets the value of the Data Source Expression control to
 Step.Result.PassFail 
 , which has the effect of using the value the code module sets.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Test Step Types](test-step-types.html)

Parent topic:

Pass/Fail Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-paths-dialog-box.html language=enus -->
## TOPIC 03647: Edit Paths Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-paths-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-paths-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Edit Paths in Files dialog box, double-click on a path, and click OK to launch the Edit Paths dialog box. Each entry in the listbox of this dialog box represents a property that has the Path data type. The listbox contains many columns of information for each entry. The Path column displa

### Edit Paths Dialog Box

Launch the
 [Edit Paths in Files](edit-paths-in-files-dialog-box.html)
 dialog box, double-click on a path, and click
 OK
 to launch the Edit Paths dialog box.

Each entry in the listbox of this dialog box represents a property that has the Path data type. The listbox contains many columns of information for each entry. The Path column displays the current value of the property. The current value can be a simple pathname, a relative pathname, or an absolute pathname. The Status column displays
 Empty
 when the current value of the property is an empty pathname. The Status column displays
 Not found
 when TestStand cannot find the pathname on disk. The File column displays the name of the file that contains the property. The Sequence column displays the name of the sequence, if any, that contains the property. The location column specifies the particular part of the sequence, such as a step type or one of the step groups, that contains the property. The Step column displays the name of the step or substep, if any, that contains the property. The Property column displays the name of the property.

- Full Path 
 —Shows the absolute pathname to which TestStand can resolve the current value of the selected path. TestStand searches for the file through the
 search paths you configure 
 using the
 Edit Search Directories 
 dialog box. If TestStand cannot find the file, the Full Path indicator shows
 Not 
 found 
 .
- Change 
 —Browses for the file to which you want the path value to refer.
- Revert 
 —Resets the selected path to the value it had when you initially opened the dialog box.
- Replace 
 —Launches the
 Replace Text in All Paths 
 dialog box, in which you can change a substring in one or more of the path values. This is particularly useful for path values that are absolute pathnames. For example, if several pathnames begin with
 c:\myfiles 
 , but the files are now in
 d:\testfiles 
 , you can click
 Replace 
 to change all instances of
 c:\myfiles 
 in the list to
 d:\testfiles 
 .

#### See Also

[Edit Paths in Files dialog box](edit-paths-in-files-dialog-box.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Replace Text in All Paths dialog box](replace-text-in-all-paths-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-paths-in-files-dialog-box.html language=enus -->
## TOPIC 03648: Edit Paths in Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-paths-in-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-paths-in-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call the Engine.DisplayEditPathsInFilesDialog method to launch the Edit Paths in Files dialog box. The listbox contains the station configuration files and sequence files currently in memory. For each of the sequence files in memory, the listbox shows the simple filename and the complete pathname. T

### Edit Paths in Files Dialog Box

Call the
 [Engine.DisplayEditPathsInFilesDialog](../tsapiref/engine-displayeditpathsinfilesdialog.html)
 method to launch the Edit Paths in Files dialog box.

The listbox contains the station configuration files and sequence files currently in memory. For each of the sequence files in memory, the listbox shows the simple filename and the complete pathname. The following are the symbolic tags and purposes of the station configuration files:

- Engine Settings 
 —File in which TestStand stores the station options.
- Station Globals 
 —File in which TestStand stores the names and values of the station global variables.
- User Manager 
 —File in which TestStand stores the information regarding the user manager.

To edit paths in one or more files in the listbox, place a checkmark for each file you want to edit and click
 OK
 . To edit the paths in a sequence file that are not in the listbox, click
 Add Files
 .

When you select one or more files to edit, the
 [Edit Paths](edit-paths-dialog-box.html)
 dialog box launches.

#### See Also

[Edit Paths dialog box](edit-paths-dialog-box.html)

[Engine.DisplayEditPathsInFilesDialog](../tsapiref/engine-displayeditpathsinfilesdialog.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-property-value-dialog-box.html language=enus -->
## TOPIC 03649: Edit Property Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-property-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-property-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Value on the All tab of the Data Link Properties dialog box to launch the Edit Property Value dialog box, in which you can edit the initialization property currently selected on the All tab. Refer to the documentation you received with the OLE DB provider for more information about provi

### Edit Property Value Dialog Box

Select
 Edit Value
 on the
 [All](data-link-properties-dialog-box2.html)
 tab of the
 [Data Link Properties](data-link-properties-dialog-box.html)
 dialog box to launch the Edit Property Value dialog box, in which you can edit the initialization property currently selected on the All tab.

Refer to the documentation you received with the OLE DB provider for more information about provider-specific properties.

#### See Also

[Data Link Properties dialog box](data-link-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-python-call-dialog-box.html language=enus -->
## TOPIC 03650: Edit Python Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-python-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-python-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the Python Adapter and select Specify Module from the context menu to launch the Edit Python Call dialog box from a TestStand User Interface . You can also select Properties from the context menu. When you select Properties , you must click Specify Module in the Step

### Edit Python Call Dialog Box

Insert a step configured to use the Python Adapter and select
 Specify Module
 from the context menu to launch the Edit Python Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu. When you select
 Properties
 , you must click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch this dialog box.

The Edit Python Call dialog box contains the following tabs:

- Module 
 —Code module the Python Adapter executes for the step. The tab also allows you to specifiy the operation and parameter information for the module.
- Advanced Settings 
 —Settings TestStand requires for using Python interpreter session.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-rule-dialog-box.html language=enus -->
## TOPIC 03651: Edit Rule Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-rule-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-rule-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Double-click a rule, right-click a rule and select Edit Rule from the context menu, or click the Edit Rule button located to the right of the Rule ID column on the Rules tab of the Configure Sequence Analyzer Available Rules dialog box to launch the Edit Rule dialog box, in which you can view genera

### Edit Rule Dialog Box

Double-click a rule, right-click a
 [rule](/csh?context=ts_tsref_sa_creating_custom_rules)
 and select
 Edit Rule
 from the context menu, or click the
 Edit Rule
 button located to the right of the Rule ID column on the
 [Rules](rules-tab-configure-sequence-analyzer-availab.html)
 tab of the
 [Configure Sequence Analyzer Available Rules](configure-sequence-analyzer-available-rules-d.html)
 dialog box to launch the Edit Rule dialog box, in which you can view general and advanced settings for built-in rules and create and edit general and advanced settings for custom rules.

The Edit Rule dialog box contains the following tabs:

- General 
 —Edits the ID, category, severity, name, and description of the rule.
- Advanced 
 —Edits the resource string category and configuration option of the rule.

#### See Also

[Configure Sequence Analyzer Available Rules dialog box](configure-sequence-analyzer-available-rules-d.html)

[Creating Custom Rules](/csh?context=ts_tsref_sa_creating_custom_rules)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-rule-settings-enumeration-items-dialog-b.html language=enus -->
## TOPIC 03652: Edit Rule Settings Enumeration Items Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-rule-settings-enumeration-items-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-rule-settings-enumeration-items-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Edit Items button in the Edit Rule Settings Enumerations dialog box to launch the Edit Rule Settings Enumeration Items dialog box, in which you edit the rule settings enumeration you selected in the Rule Settings Enumerations list. Use the Edit Rule Settings Enumerations dialog box to add,

### Edit Rule Settings Enumeration Items Dialog Box

Click the
 Edit Items
 button in the
 [Edit Rule Settings Enumerations](edit-rule-settings-enumerations-dialog-box.html)
 dialog box to launch the Edit Rule Settings Enumeration Items dialog box, in which you edit the rule settings enumeration you selected in the Rule Settings Enumerations list.

Use the Edit Rule Settings Enumerations dialog box to add, remove, and edit the items of a rule settings enumeration type for custom rule settings. Edit rule settings enumeration items by clicking the Name and Value columns of the Items control. Rule settings enumeration item values must be numbers.

The TestStand Sequence Analyzer uses the Resource String Category option on the
 [Advanced](advanced-tab-edit-rule-dialog-box.html)
 tab of the
 [Edit Rule](edit-rule-dialog-box.html)
 dialog box to localize rule settings enumeration item names.

#### See Also

[Edit Rule Settings Enumerations dialog box](edit-rule-settings-enumerations-dialog-box.html)

[Edit Rule dialog box](edit-rule-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-rule-settings-enumerations-dialog-box.html language=enus -->
## TOPIC 03653: Edit Rule Settings Enumerations Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-rule-settings-enumerations-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-rule-settings-enumerations-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you select Use Rule Settings for the Configuration Option on the Advanced tab of the Edit Rule dialog box, click the Enums button to launch the Edit Enumerations dialog box, in which you create new enumeration types to use for rule settings. Use the Edit Enumerations dialog box to add, remove,

### Edit Rule Settings Enumerations Dialog Box

When you select Use Rule Settings for the Configuration Option on the
 [Advanced](advanced-tab-edit-rule-dialog-box.html)
 tab of the
 [Edit Rule](edit-rule-dialog-box.html)
 dialog box, click the
 Enums
 button to launch the Edit Enumerations dialog box, in which you create new enumeration types to use for rule settings.

Use the Edit Enumerations dialog box to add, remove, and edit enumeration types for custom rule settings. Click the
 Edit Items
 button to launch the
 [Edit Enumeration Items](edit-rule-settings-enumeration-items-dialog-b.html)
 dialog box, in which you edit the enumeration you selected in the Enumerations list.

#### See Also

[Edit Rule Settings Enumeration Items dialog box](edit-rule-settings-enumeration-items-dialog-b.html)

[Edit Rule dialog box](edit-rule-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-search-directories-dialog-box.html language=enus -->
## TOPIC 03654: Edit Search Directories Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-search-directories-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-search-directories-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Search Directories to launch the Edit Search Directories dialog box, in which you can view the default list of search paths . The paths that appear first in the list take precedence over the paths that appear later in the list. When you first run TestStand, the list contains a defau

### Edit Search Directories Dialog Box

Select
 Configure»Search Directories
 to launch the Edit Search Directories dialog box, in which you can view the default list of
 [search paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

The paths that appear first in the list take precedence over the paths that appear later in the list. When you first run TestStand, the list contains a default set of directory paths. When you place a checkmark next to a path, TestStand includes the path in the overall search path. To reorder paths in the list, select a path and click
 Move Up
 or
 Move Down
 . Click
 Add
 to add a custom directory search path. TestStand stores the search directories in the SearchDirectories.cfg file in the TestStand configuration directory.

When you select a path, the following controls display the settings for the path:

- File Extension Restrictions 
 —Searches only for files with specific filename extensions. For example, to search for only DLLs and executable files, enter the following string:
 DLL, EXE 
 .
  - Exclude 
 —Searches for all files except those files with specific extensions. A tilde (
 ~ 
 ) is visible at the beginning of the File Extension Restrictions column for the row you have selected when this option is enabled.
- Search Subdirectories 
 —When you enable this option, TestStand includes all subdirectories within the selected path in the overall search path.
 Note 
 If you add a large directory tree to the search paths and specify the Search Subdirectories option, TestStand must search the entire tree each time it locates a file. You can improve performance by using the File Extension Restrictions control to limit the types of files for which TestStand searches a directory tree. For example, if a directory tree contains only VI files, specify
 VI
 in the File Extension Restrictions control to prevent TestStand from searching the directory tree for files of other types such as
 .seq
 and
 .dll
 .
 For best performance, move the following search paths to the end of the search path list: the search paths you add that refer to large directory trees, directories on network drives, and paths that contain files which you use infrequently.
- Exclude Hidden Subdirectories 
 —When you enable this option, TestStand does not search subdirectories of the directory you select when the subdirectories specify the Hidden attribute in the Windows file system. You can enable or disable the Exclude Hidden Subdirectories option for each directory listed in the Edit Search Directories dialog box. This option is disabled by default and is available only when you enable the Search Subdirectories option.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-sequence-call-dialog-box.html language=enus -->
## TOPIC 03655: Edit Sequence Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-sequence-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-sequence-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the Sequence Adapter and select Specify Module from the context menu to launch the Edit Sequence Call dialog box from a TestStand User Interface . You can also select Properties from the context menu. When you select Properties , you must click Specify Module in the S

### Edit Sequence Call Dialog Box

Insert a step configured to use the Sequence Adapter and select
 Specify Module
 from the context menu to launch the Edit Sequence Call dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also select
 Properties
 from the context menu. When you select
 Properties
 , you must click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Edit Sequence Call dialog box contains the following options:

- Specify Expressions for Pathname and Sequence 
 —Specifies whether you provide the sequence name and sequence file pathname using literal strings or
 expressions 
 TestStand evaluates at run time. When you use literal strings, you enter the actual pathname of the sequence file in the File Pathname control. When you enable this option, you cannot use the Use Prototype of Selected Sequence option. When you use expressions, you specify an expression in the Sequence control.
 Note 
 If the Sequence Call step specifies the
 Preload when opening sequence file
 or
 Preload when execution begins
 [load option](run-options-tab-step-properties-dialog-box.html)
 , and you enable the Specify By Expression option for the step or the step
 [calls a custom sequence file](/csh?context=ts_tsfundamentals_translators)
 , TestStand does not preload the code module and behaves as if you selected the
 Load dynamically
 load option for the step.
- Use Current File 
 —TestStand calls a sequence in the sequence file you are currently editing. The File Pathname/File Path or Reference Expression control dims when you enable this option.
- File Pathname/File Path or Reference Expression 
 —The pathname of the sequence file or a reference to a
 SequenceFile 
 object. When you use expressions, the File Path or Reference Expression control appears in place of the File Pathname control. Use this control to specify the expression for the sequence file pathname.
- Client Pathname/Path or References 
 —The pathname or reference of the client sequence filename when the step runs the sequence in a new execution and the
 Execution Settings 
 dialog box specifies to use a process model. When you use expressions, use this option to specify an expression for the client sequence file.
- Model Pathname/Path or Reference 
 —The pathname or reference of the model sequence file when the step runs the sequence in a new execution and the
 Execution Settings 
 dialog box specifies to use a process model. When you use expressions, use this option to specify an expression for the client sequence file.
- Sequence 
 —The name of the sequence in the sequence file you specify. When you use expressions, use this option to specify an expression for the sequence name.
- Entry Point 
 —The name of the entry point when the step runs the sequence in a new execution and the
 Execution Settings 
 dialog box specifies to use a process model. When you use expressions, use this option to specify an expression for the entry point name.
- Multithreading and Remote Execution 
 —Specifies whether the sequence you call runs in a separate thread, in a separate execution, or on a remote computer. The following options are available in the ring control:
 
 Note 
 When you specify that a sequence runs in a new thread or execution, the status of the sequence call is
 Done
 or
 Error
 . This status is independent of the status of the sequence you call. To determine the status of an asynchronous subsequence from a step in the calling sequence, use a Wait step to wait for the asynchronous sequence to complete. The status of the Wait step is the status of the asynchronous sequence.
  - None 
 —Specifies whether the sequence you call runs in the current thread.
  - Run Sequence in a New Thread 
 —The sequence runs in a new a thread within the current execution. Threads in the same execution share the same report and the same result tree. In addition, all threads in an execution suspend or terminate when the execution suspends or terminates.
  - Run Sequence in a New Execution 
 —The sequence runs in a new execution. Separate executions have separate reports and result trees. Suspending or terminating an execution does not affect other executions. Separate executions can also run under different process models.
  - Run Sequence on Remote Computer 
 —The sequence runs on the remote computer you specify. To execute the sequence remotely, the Sequence Adapter connects to an instance of the TestStand Engine on the remote computer.
- Settings 
 —Launches a dialog box in which you can configure multithreading and remote execution settings. The dialog box varies according to the option you select in the Multithreading and Remote Execution ring control. The following options are available in the ring control:
  - Thread Settings 
 —Specifies if the sequence you call runs in a new thread. Selecting this option launches the
 Thread Settings 
 dialog box.
  - Execution Settings 
 —Specifies if the sequence you call runs in a new execution. Selecting this option launches the
 Execution Settings 
 dialog box.
  - Remote Execution Settings 
 —Specifies if the sequence you call runs on a remote computer. Selecting this option launches the
 Remote Execution Settings 
 dialog box.
 Note 
 TestStand does not support remotely executing a sequence across different TestStand versions, for example, remotely executing a TestStand 2013 sequence from a computer running TestStand 2010.
- Parameters 
 —The Parameters section contains the following items:
 
 Note 
 When you call a sequence on a remote host, you can pass single-valued properties or arrays of number, Boolean, and string properties by value or by reference. You can also pass container properties or object reference properties to a remote sequence if the receiving parameter type is an object reference property.
  - Use Prototype of Selected Sequence 
 —Enable this option to specify to update the contents of the Parameters Table control whenever you select a different sequence from the Sequence ring control. This option is not available when you enable the Specify Expressions for Pathname and Sequence option. When this option is disabled, use the
 Load Prototype 
 button to update the contents of the Parameters Table by selecting the parameters from an existing sequence.
  - Load Prototype 
 —Loads a prototype from a sequence that has the same parameter list definition as the sequences the step might call. This button is available when you enable the Specify Expressions for Pathname and Sequence option. Use this button to update the contents of the Parameters Table when you enable the Specify Expressions for Pathname and Sequence option.
 Note 
 Load Prototype
 does not support parameters that have the
 shared
 flag set. Such parameters will be excluded. Enable
 Use Prototype of Sequence
 instead to also include parameters that have the
 shared
 flag set.
  - Parameters Table 
 —Displays the parameters the step passes to the sequence. The contents of the Parameters Table control must be consistent with the parameter definitions in the sequence the step calls. You must extract the parameter definitions from the sequence or from another sequence that has the same parameter list.
 The Parameters Table control contains the following columns: 
 
 Although the parameter list the step uses must be consistent with the parameter list the sequence defines, the step can specify fewer parameters than the sequence specifies. The data types for the parameters in the step must be compatible with the corresponding parameters in the sequence. The Sequence Adapter uses the default values for the parameters the step does not pass explicitly. 
 When you use the
 Load Prototype
 button on the Module tab of the Step Settings pane of a Sequence Call step to load prototype information from a different sequence and the sequence from which you load the prototype includes the same parameters as the original sequence plus additional parameters, TestStand passes the additional parameters to the sequence you call.
    - Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to access the
 [Parameters Table](for-specify-module-dialog-boxes-parameters-ta.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
    - Type 
 —The TestStand data type for the parameter.
    - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name in the
 Additional Results 
 dialog box. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter in the Additional Results dialog box. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results dialog box specifies to log the [In] parameter value or the [Out] parameter value.
    - Use Default 
 —When you enable this option, the step passes the default value the sequence defines for the parameter.
    - Value 
 —The argument the step passes for a parameter. You can specify an expression TestStand evaluates at run time.
 Note 
 When you pass an array to a sequence, the Sequence Adapter does not alter the array bounds. For example, if a sequence defines a parameter with bounds [
 0..2
 ] and a Sequence Call step passes an array with bounds [
 3..5
 ], the called sequence must access the array with bounds [
 3..5
 ], not [
 0..2
 ].
    - How Passed 
 —Specifies whether the step passes the parameter by value or by reference. When the step passes the parameter by reference, the subsequence can change the value of the parameter argument. The parameter definition in the sequence determines whether the step passes the argument by value or by reference.

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Built-In Step Types](built-in-step-types.html)

[Execution Settings dialog box](execution-settings-dialog-box.html)

[Parameters Table Context Menu for Specify Module Dialog Boxes](for-specify-module-dialog-boxes-parameters-ta.html)

[Remote Execution in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64remoteexecution)

[Remote Execution Settings dialog box](remote-execution-settings-dialog-box.html)

[Sequence File Translators](/csh?context=ts_tsfundamentals_translators)

[SequenceFile](../tsapiref/sequencefile.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Thread Settings dialog box](thread-settings-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-statement-dialog-box.html language=enus -->
## TOPIC 03656: Edit Statement Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-statement-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-statement-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Expression in the context menu for the step or click Edit Expression on the General tab of the Step Properties dialog box to launch the Edit Statement dialog box from a TestStand User Interface . Use this dialog box to specify expressions for a Statement step. The Edit Statement dialog b

### Edit Statement Dialog Box

Select
 Edit Expression
 in the context menu for the step or click
 Edit Expression
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit Statement dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to specify
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 for a Statement step.

The Edit Statement dialog box contains the following options:

- Expression 
 —The expression the step evaluates.
- Check Syntax 
 —Determines whether the expression syntax is valid.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Statement Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-step-list-configurations-dialog-box.html language=enus -->
## TOPIC 03657: Edit Step List Configurations Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-step-list-configurations-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-step-list-configurations-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Step List Configurations»Edit Step List Configurations from the Steps pane context menu in the Sequence File window or from the Steps pane context menu in the Execution window to launch the Edit Step List Configurations dialog box, in which you can create or modify step list configurations. Y

### Edit Step List Configurations Dialog Box

Select
 Step List Configurations»Edit Step List Configurations
 from the
 [Steps](steps-pane-context-menu-sequence-file-window.html)
 pane context menu in the
 [Sequence File](sequence-file-window.html)
 window or from the
 [Steps](steps-pane-context-menu-execution-window.html)
 pane context menu in the
 [Execution](execution-window.html)
 window to launch the Edit Step List Configurations dialog box, in which you can create or modify step list configurations. You can control how the Steps pane displays steps by setting various options that determine fonts, colors, visible columns, and other aspects of the Steps pane. A step list configuration stores a collection of settings you apply as a group when you enable the configuration.

Use the Edit Step List Configuration dialog box to create, edit, and select configurations for two different types of configurations. One list contains configurations that specify how Sequence File windows display steps and the other list contains configurations that specify how Execution windows display steps. You can enable one configuration in each list. The configuration you enable applies to all Sequence File windows or all Execution windows according to the list in which the configuration resides.

The Edit Step List Configurations Dialog Box contains the following controls:

- Select Configuration for Viewing Files 
 —The list of configurations you can apply to all step list views that display steps in sequence files. Enable a configuration to specify that all sequences files display their steps using the configuration you enable.
 Double-click a configuration name or click
 Edit 
 to launch the
 Configuration Properties 
 dialog box, in which you can edit the selected configuration. Click anywhere in the control to make it the active configuration list. When the list is the active list, the list border and label are highlighted. When the list is active, all editing operations in the dialog box apply to the list of configurations it displays and the Sample Step List control displays according to the selected configuration in the list.
- Select Configuration for Viewing Executions 
 —The list of configurations you can apply to all step list views that display steps in executions. Enable a configuration to specify that all executions display their steps using the configuration you enable. 
 Double-click a configuration name or click
 Edit 
 to launch the
 Configuration Properties 
 dialog box, in which you can edit the selected configuration. Click anywhere in the control to make it the active configuration list. When the list is the active list, the list border and label are highlighted. When the list is active, all editing operations in the dialog apply to the list of configurations it displays and the Sample Step List control displays according to the selected configuration in the list.
- Sample File Step List for: <
 Configuration Name
 > 
 —A sample list of steps using the configuration you select in the active configuration list.
- New 
 —Creates a new configuration in the active configuration list.
- Cut 
 —Removes the configuration you select from the active configuration list and places it on the clipboard.
- Copy 
 —Copies the configuration you select in the active configuration list to the clipboard.
- Paste 
 —Pastes the configuration on the clipboard into the active configuration list.
- Edit 
 —Launches the
 Configuration Properties 
 dialog box for the configuration you select in the active configuration list.
- Move Up 
 —Moves the configuration you select in the active configuration list up one position in the list. The position in the list only affects the order in which the configurations appear in menus.
- Move Down 
 —Moves the configuration you select in the active configuration list down one position in the list. The position in the list only affects the order in which the configurations appear in menus.

#### See Also

[Configuration Properties dialog box](configuration-properties-dialog-box.html)

[Execution Window](execution-window.html)

[Sequence File Window](sequence-file-window.html)

[Steps Pane Context Menu (Execution Window)](steps-pane-context-menu-execution-window.html)

[Steps Pane Context Menu (Sequence File Window)](steps-pane-context-menu-sequence-file-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/edit-string-value-dialog-box.html language=enus -->
## TOPIC 03658: Edit String Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/edit-string-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/edit-string-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Expected String in the context menu for the step or click Edit Expected String on the General tab of the Step Properties dialog box to launch the Edit String Value dialog box from a TestStand User Interface . Use this dialog box to specify the type of comparison and limits TestStand uses

### Edit String Value Dialog Box

Select
 Edit Expected String
 in the context menu for the step or click
 Edit Expected String
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Edit String Value dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to specify the type of comparison and limits TestStand uses to set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 and the string the step expects to receive.

The Edit String Value dialog box contains the following tabs:

- Limits 
 —The string comparison the step performs.
- Data Source 
 —The data source for the string value the step compares.

Note

\r

\n

\r

\n

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Test Step Types](test-step-types.html)

Parent topic:

String Value Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/else-if-step.html language=enus -->
## TOPIC 03659: Else If Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/else-if-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/else-if-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an Else If step to define a block of steps that execute if a condition is met and the conditions the preceding If step and any preceding Else If step define are not met. Configuring the Step Use the ElseIf Condition edit tab in the TestStand Sequence Editor and the Configure Else If Condition di

### Else If Step

Use an Else If step to define a block of steps that execute if a condition is met and the conditions the preceding
 [If](if-step.html)
 step and any preceding Else If step define are not met.

#### Configuring the Step

Use the
 [ElseIf Condition](elseif-condition-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Else If Condition](configure-else-if-condition-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Else If step. You cannot select an Else or Else If step as the target of a Goto Step or as the target of a post action.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Else If step type defines the following step property:

- Step.ConditionExpr 
 —The expression that must evaluate to
 True 
 for the steps within the Else If block to execute.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/else-step.html language=enus -->
## TOPIC 03660: Else Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/else-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/else-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an Else step to define a block of steps that execute if the condition the preceding If or Else If step defines is not met. Configuring the Step Use the Properties tab of the Step Settings pane in the TestStand Sequence Editor or the Step Properties dialog box in a TestStand User Interface to con

### Else Step

Use an Else step to define a block of steps that execute if the condition the preceding
 [If](if-step.html)
 or
 [Else If](else-if-step.html)
 step defines is not met.

#### Configuring the Step

Use the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Step Properties](step-properties-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Else step. You cannot select an Else or Else If step as the target of a Goto Step or as the target of a post action.

#### Step Properties

The Else step type does not define any additional step properties other than
 [custom properties common to all steps](/csh?context=ts_tsfundamentals_custom_result_props)
 .

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/elseif-condition-edit-tab.html language=enus -->
## TOPIC 03661: ElseIf Condition Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/elseif-condition-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/elseif-condition-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the ElseIf Condition edit tab in the TestStand Sequence Editor to configure the Else If step. The ElseIf Condition edit tab contains the following options: Conditional Expression —The expression that must evaluate to True for the steps within the Else If block to execute. If the expression evalu

### ElseIf Condition Edit Tab

Use the ElseIf Condition edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the Else If step.

The ElseIf Condition edit tab contains the following options:

- Conditional Expression 
 —The expression that must evaluate to
 True 
 for the steps within the Else If block to execute. If the expression evaluates to
 False 
 , the execution proceeds to the next Else If, Else, or End step for the If block.
- Condition Builder 
 —Launches the
 Condition Builder 
 dialog box, in which you build conditional
 expressions 
 that refer to the execution statuses of other steps.

#### See Also

[Condition Builder dialog box](preconditions-dialog-box.html)

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Else If Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/end-step.html language=enus -->
## TOPIC 03662: End Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/end-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/end-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an End step to define the end of any block steps. Configuring the Step Use the Properties tab of the Step Settings pane in the TestStand Sequence Editor or the Step Properties dialog box in a TestStand User Interface to configure the End step. Step Properties The End step type does not define an

### End Step

Use an End step to define the end of any block steps.

#### Configuring the Step

Use the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Step Properties](step-properties-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the End step.

#### Step Properties

The End step type does not define any additional step properties other than
 [custom properties common to all steps](/csh?context=ts_tsfundamentals_custom_result_props)
 .

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enqueue-operation-queue-settings-edit-tab.html language=enus -->
## TOPIC 03663: Enqueue Operation - Queue Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enqueue-operation-queue-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enqueue-operation-queue-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enqueue Operation Use the Enqueue operation to add new elements to the queue. Enable the Enqueue option on the left of the Queue Settings panel. The Enqueue operation contains the following options: Queue Name or Reference Expression —The queue on which to perform the operation. You can specify the

### Enqueue Operation - Queue Settings Edit Tab

#### Enqueue Operation

Use the Enqueue operation to add new elements to the queue. Enable the
 Enqueue
 option on the left of the Queue Settings panel.

The Enqueue operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option.
- New Element to Enqueue 
 —The data to insert into the queue. The data can be any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. When you dequeue the element you must specify a location with the appropriate type. By default, the queue stores a copy of the data you enqueue. However, when you enable the Store by Reference Instead of by Value option, the enqueue operation stores an object reference to the data value instead. When you dequeue this reference into an object reference variable, you can access the data using the TestStand API
 PropertyObject 
 interface and the ActiveX/COM Adapter.
- Insert At 
 —The location where TestStand stores the new queue element. The choices are Front of Queue and Back of Queue.
- Store by Reference Instead of by Value 
 —Specifies how to store the data you specify in the New Element to Enqueue control. Enable this option when you want to store an object reference to the data. Disable this option when you want to store a copy of the data.
- If the Queue is Full 
 —The action to use when the queue is full. The available options are Wait, Discard Front Element, Discard Back Element, and Do Not Enqueue. If you select Wait, the thread blocks until the queue is no longer full. All other options return immediately.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —The timeout behavior TestStand uses when the queue is full. The timeout applies only if you specify the Wait option for the If the Queue is Full setting. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Queue Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enqueue-operation-queue-step-configuration-di.html language=enus -->
## TOPIC 03664: Enqueue Operation - Queue Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enqueue-operation-queue-step-configuration-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enqueue-operation-queue-step-configuration-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enqueue Operation Use the Enqueue operation to add new elements to the queue. The Enqueue operation contains the following options: Queue Name or Reference Expression —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you creat

### Enqueue Operation - Queue Step Configuration Dialog Box

#### Enqueue Operation

Use the Enqueue operation to add new elements to the queue.

The Enqueue operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option.
- New Element to Enqueue 
 —The data to insert into the queue. The data can be any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. When you dequeue the element you must specify a location with the appropriate type. By default, the queue stores a copy of the data you enqueue. However, when you enable the Store by Reference Instead of by Value option, the enqueue operation stores an object reference to the data value instead. When you dequeue this reference into an object reference variable, you can access the data using the TestStand API
 PropertyObject 
 interface and the ActiveX/COM Adapter.
- Insert At 
 —Specifies where to store the new queue element. The choices are Front of Queue and Back of Queue.
- Store by Reference Instead of by Value 
 —Specifies how to store the data you specify in the New Element to Enqueue control. Enable this option when you want to store an object reference to the data. Disable this option when you want to store a copy of the data.
- If the Queue is Full 
 —Specifies what to do when the queue is full. The available options are Wait, Discard Front Element, Discard Back Element, and Do Not Enqueue. When you select Wait, the thread blocks until the queue is no longer full. All other options return immediately.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior for when the queue is full. The timeout applies only when you specify the Wait option for the If the Queue is Full setting. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Queue Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enter-synchronized-section-operation-batch-sy.html language=enus -->
## TOPIC 03665: Enter Synchronized Section Operation - Batch Synchronization Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enter-synchronized-section-operation-batch-sy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enter-synchronized-section-operation-batch-sy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter Synchronized Section Operation Use the Enter Synchronized Section operation to mark the beginning of a synchronized section and to define the type of synchronization for the section. Enable the Enter Synchronized Section option on the left of the Batch Synchronization Settings panel. The Enter

### Enter Synchronized Section Operation - Batch Synchronization Settings Edit Tab

#### Enter Synchronized Section Operation

Use the Enter Synchronized Section operation to mark the beginning of a
 [synchronized section](/csh?context=ts_tsref_sync_sections)
 and to define the type of synchronization for the section. Enable the
 Enter Synchronized Section
 option on the left of the Batch Synchronization Settings panel.

The Enter Synchronized Section operation contains the following options:

- Section Name 
 —A name for the synchronized section. Leave this control blank when you want TestStand to generate a unique name for you based on the step name.
- Section Type 
 —The type of synchronized section. Options include Serial, Parallel, and One Thread Only.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior for when a thread must wait at an Enter step. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Batch Synchronization Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enter-synchronized-section-operation-batch-sy2.html language=enus -->
## TOPIC 03666: Enter Synchronized Section Operation - Batch Synchronization Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enter-synchronized-section-operation-batch-sy2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enter-synchronized-section-operation-batch-sy2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter Synchronized Section Operation Use the Enter Synchronized Section operation to mark the beginning of a synchronized section and to define the type of synchronization for the section. The Enter Synchronized Section operation contains the following options: Section Name —A name for the synchroni

### Enter Synchronized Section Operation - Batch Synchronization Step Configuration Dialog Box

#### Enter Synchronized Section Operation

Use the Enter Synchronized Section operation to mark the beginning of a
 [synchronized section](/csh?context=ts_tsref_sync_sections)
 and to define the type of synchronization for the section.

The Enter Synchronized Section operation contains the following options:

- Section Name 
 —A name for the synchronized section. Leave this control blank when you want TestStand to generate a unique name for you based on the step name.
- Section Type 
 —The type of synchronized section. Options include Serial, Parallel, and One Thread Only.
  - Serial (One Thread at a Time) 
 —Ensures that each thread in a batch executes the section sequentially and in the order you specify when you create the batch. When all threads in a batch arrive at their respective instances of the Enter step, TestStand releases one thread at a time in ascending order according to the order number you assigned to the threads when you added them to the batch with the Batch Specification step type. As each thread executes the Exit step for the section, the next thread in the batch proceeds from the Enter step. After all threads in the batch arrive at the Exit step, they exit the section together.
  - Parallel (All Threads Enter Simultaneously) 
 —When all threads in the batch arrive at their respective instances of the Enter step, TestStand releases all threads at once. Each thread blocks after reaching the Exit step for the section until all threads can exit the section together.
  - One Thread Only (First Thread Enters, Remaining Threads Skip to Exit) 
 —Use a One-Thread-Only section to specify if only one thread in the batch executes the steps in the section. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of the Enter step, TestStand releases only the thread with the lowest order number. When that thread arrives at the Exit step for the section, all remaining threads in the batch jump from the Enter step to the Exit step, skipping steps within the section. The threads in the batch then exit the section together.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior for when a thread must wait at an Enter step. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Batch Synchronization Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enumeration-parameters-activex-com-call-param.html language=enus -->
## TOPIC 03667: Enumeration Parameters - ActiveX/COM Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enumeration-parameters-activex-com-call-param.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enumeration-parameters-activex-com-call-param.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumeration Parameters Use the ring control in the Value column of the Parameters Table on the ActiveX/COM Module tab of the Step Settings pane in the TestStand Sequence Editor or in the Edit ActiveX/COM Call dialog box in a TestStand User Interface to select one of the enumeration values, or enter

### Enumeration Parameters - ActiveX/COM Call Parameters

#### Enumeration Parameters

Use the ring control in the Value column of the Parameters Table on the
 [ActiveX/COM Module](activex-com-module-tab.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or in the
 [Edit ActiveX/COM Call](edit-activex-com-call-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to select one of the enumeration values, or enter an expression that evaluates to a number or a compatible TestStand enumeration data type.

To pass an enumeration parameter to an ActiveX/COM code module using a number, specify a TestStand expression that evaluates to a number. The number must have the numeric representation compatible with the underlying integer data type of the code module.

To pass an enumeration parameter using the TestStand enumeration data type, specify a TestStand expression that evaluates to an enumeration that is compatible with the underlying enum definition in the code module. To be compatible, the TestStand type and underlying enum type in the code module must have identical sets of enumerators. Both types must have the same number of enumerators matching in both name and numeric value, as well as compatible numeric representations. The order in which the enumerators are defined does not matter.

#### See Also

[Edit ActiveX/COM Call dialog box](edit-activex-com-call-dialog-box.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enumeration-parameters-c-c-dll-call-parameter.html language=enus -->
## TOPIC 03668: Enumeration Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enumeration-parameters-c-c-dll-call-parameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enumeration-parameters-c-c-dll-call-parameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumeration Parameters You can pass enumerations you create as named data types. When you create or edit an enumeration data type, you can specify whether the type can be a C structure argument and how the type represents itself in memory when you pass it to a structure parameter or array parameter.

### Enumeration Parameters - C/C++ DLL Call Parameters

#### Enumeration Parameters

You can pass enumerations you create as named data types. When you create or edit an enumeration data type, you can specify whether the type can be a C structure argument and how the type represents itself in memory when you pass it to a structure parameter or array parameter.

The following settings are available in the Data Type ring control when you select
 Enumeration
 for the category type.

| Numeric Data Type Setting | Equivalent C Data Type |
| --- | --- |
| Signed 8-bit Integer | char |
| Unsigned 8-bit Integer | unsigned char |
| Signed 16-bit Integer | short |
| Unsigned 16-bit Integer | unsigned short |
| Signed 32-bit Integer | long |
| Unsigned 32-bit Integer | unsigned long |
| Signed 64-bit Integer | long long, __int64 |
| Unsigned 64-bit Integer | unsigned long long, unsigned __int64 |
| 32-bit Real Number | float |
| 64-bit Real Number | double |

#### Enum Type

When you select the Enumeration category for a parameter, the C/C++ Adapter displays the Enum Type control. This control allows you to specify the Enumeration data type necessary for the parameter in the Value Expression control. Additionally, the Value Expression control becomes a combo box where you can select enumerators of the enumeration. You can also enter an enumeration name or the corresponding numeric value for the enumeration directly into the Value Expression or Function Call controls.

When you select an Enumeration parameter that accepts an enumerated type from a code module that has a type library, TestStand will automatically check if the Enumeration data type and the type library enumeration have exactly matching enumerators. If not, then the Enum Type chosen will be shown in red with a warning message regarding the detected mismatch.

Note

enum [tag] : __int64 {enum-list} [declarator];

unsigned __int64 {enum-list} [declarator];

#### Pass by Value or by Reference

When you select the Enumeration category for a parameter, the C/C++ DLL Adapter displays the Pass control. which specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Pointer (*)
 or
 By Reference (&)
 , the adapter passes a pointer to the argument value.

If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property. When you select the
 Enumeration
 category for the return value, you may leave the Value control empty or specify the name of a variable or property.

Note

NULL

Nothing

0

#### Result Actions

The C/C++ DLL Adapter displays the Result Action ring control and the Set Error.Code to Value option for return values and parameters you pass by pointer. Depending on the settings of these controls, TestStand can automatically set the
 Error.Occurred
 and
 Error.Code
 properties of the step according to the value in the enumeration argument when the function returns.

Use the Result Action ring control to configure TestStand to set the
 Error.Occurred
 property to
 True
 when the return value or parameter value after the call is greater than zero, less than zero, equal to zero, or not equal to zero. Use the Set Error.Code to Value option to request TestStand to assign the output value of the argument to the
 Error.Code
 property.

Note

Error.Code

Error.Code

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enumeration-parameters-labview-nxg-vi-call-pa.html language=enus -->
## TOPIC 03669: Enumeration Parameters - LabVIEW NXG VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enumeration-parameters-labview-nxg-vi-call-pa.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enumeration-parameters-labview-nxg-vi-call-pa.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumeration Parameters TestStand recognizes LabVIEW NXG Enum controls as a distinct type, Enumeration . When you select an enumerated parameter, the Value column of the VI Parameter Table on the LabVIEW Module tab displays a combo box from which you can select elements of the enumeration. The Type c

### Enumeration Parameters - LabVIEW NXG VI Call Parameters

#### Enumeration Parameters

TestStand recognizes LabVIEW NXG Enum controls as a distinct type,
 Enumeration
 . When you select an enumerated parameter, the Value column of the VI Parameter Table on the
 [LabVIEW Module](labview-module-tab.html)
 tab displays a combo box from which you can select elements of the enumeration. The Type column in the Module tab will indicate
 Enumeration (<numeric representation>)
 for all enumerated parameters.

Note

At edit time, TestStand stores the numeric value and the corresponding string label value of the enumeration you select.

When you pass an enumeration value as a parameter to TestStand at run time, TestStand stores only the numeric value. In addition, for input parameters at run time, TestStand passes the numeric value to LabVIEW NXG without checking whether the numeric value is within range.

Enumeration types in TestStand support specifying a TestStand
 [Enum](/csh?context=ts_tsfundamentals_usingenumerations)
 data type variable/expression in the Value column.

You can create an Enum data type that maps to the LabVIEW NXG enumerated parameter by clicking on the
 Create/Update Custom Data Type
 [IMAGE alt='image' src='../images/typedef.gif']
 button located in the Type column of the VI Parameter table next to any LabVIEW NXG enumerated parameter or an enumerated array parameter.
This action launches the
 [Create/Update Custom Data Type from Enum](create-update-custom-data-type-from-labview-e.html)
 dialog box, where you can create a custom Enum data type or update an existing Enum data type to match the LabVIEW NXG parameter. You can then create an instance of the Enum data type and specify that variable in the Value column of the VI Parameter table.

When specifying Enum, String, or Numeric variables as the value of an enumerated parameter, the following table describes the behavior:

| TestStand Type | Variable passed to a LabVIEW NXG input parameter | Variable receiving data from a LabVIEW NXG output parameter |
| --- | --- | --- |
| Custom Enum data type | The elements of a TestStand Enum data type should match the LabVIEW NXG parameter's enumerated elements exactly (name, case and value). Any mismatch will result in an edit-time error. Every enumerator specified in the TestStand enum value should have a matching enumerator in the LabVIEW NXG enum. Flag enums can have multiple enumerators combined together with an OR operator. The numeric value of the TestStand enumerator should match the numeric value of the corresponding LabVIEW NXG enumerator. If there are multiple flags combined with an OR operator, as in the case of a flag enum, their combined numeric value should match in TestStand and LabVIEW NXG.If the numeric representation of the TestStand Enum doesn't match the LabVIEW NXG Enum control, you will get a run-time error in all cases. | The elements of a TestStand Enum data type should match the LabVIEW NXG parameter's enumerated elements exactly (name, case and value). Any mismatch will result in an edit-time error. If the numeric representation of the TestStand Enum doesn't match the LabVIEW NXG Enum control, you will get a run-time error in all cases. |
| String | If the variable's value exactly matches any of the LabVIEW NXG enumerated parameter's elements, the numeric value of the element is passed to LabVIEW NXG. If there is no match, you will get a run-time error.Assigning a duplicate enumerator name (more than one element with the same name) will result in an error. | If the numeric value received from LabVIEW NXG matches any of the enumerated parameter's elements, then the matching element's name is stored in the string. If the numeric value does not match any element, its string representation surrounded by angular brackets is stored.Assigning a duplicate enumerator value to the string variable will result in an error. |
| Number | The numeric value is passed to the LabVIEW NXG Enum control. If the variable's numeric representation doesn't match that of the LabVIEW NXG enum control, you will get a run-time error. | The numeric value of the LabVIEW NXG Enum indicator is assigned to the TestStand number. If the variable's numeric representation doesn't match that of the LabVIEW NXG enum indicator, you will get a run-time error. |

#### See Also

[LabVIEW NXG Data Types in TestStand](labview-nxg-data-types-in-teststand.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Numeric Parameters](numeric-parameters-labview-vi-call-parameters.html)

Parent topic:

LabVIEW NXG Data Types in TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enumeration-parameters-labview-vi-call-parame.html language=enus -->
## TOPIC 03670: Enumeration Parameters - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enumeration-parameters-labview-vi-call-parame.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enumeration-parameters-labview-vi-call-parame.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumeration Parameters TestStand 2016 and later recognizes LabVIEW enumerated parameters as a distinct type, Enumeration . When you select an enumerated parameter, the Value column of the VI Parameter Table on the LabVIEW Module tab displays a combo box from which you can select elements of the enum

### Enumeration Parameters - LabVIEW VI Call Parameters

#### Enumeration Parameters

TestStand 2016 and later recognizes LabVIEW enumerated parameters as a distinct type,
 Enumeration
 . When you select an enumerated parameter, the Value column of the VI Parameter Table on the
 [LabVIEW Module](labview-module-tab.html)
 tab displays a combo box from which you can select elements of the enumeration. The Type column in the Module tab will indicate
 Enumeration (<numeric representation>)
 for all enumerated parameters.

At edit time, TestStand stores the numeric value and the corresponding string label value of the enumeration you select.

When you pass an enumeration value as a parameter to TestStand at run time, TestStand stores only the numeric value. In addition, for input parameters at run time, TestStand passes the numeric value to LabVIEW without
 [checking whether the numeric value is within range](/csh?context=ts_tsref_labview_enum_params_range)
 .

In addition to the existing behavior, Enumeration types in TestStand support specifying a TestStand
 [Enum](/csh?context=ts_tsfundamentals_usingenumerations)
 data type variable/expression in the Value column.

You can create an Enum data type that maps to the LabVIEW enumerated parameter by clicking on the
 Create/Update Custom Data Type
 [IMAGE alt='image' src='../images/typedef.gif']
 button located in the Type column of the VI Parameter table next to any LabVIEW enumerated parameter or an enumerated array parameter.
This action launches the
 [Create/Update Custom Data Type from Enum](create-update-custom-data-type-from-labview-e.html)
 dialog box, where you can create a custom Enum data type or update an existing Enum data type to match the LabVIEW parameter. You can then create an instance of the Enum data type and specify that variable in the Value column of the VI Parameter table.

When specifying Enum, String, or Numeric variables as the value of an enumerated parameter, the following table describes the behavior:

| TestStand Type | Variable passed to a LabVIEW input parameter | Variable receiving data from a LabVIEW output parameter |
| --- | --- | --- |
| Custom Enum data type | The elements of a TestStand Enum data type should match the LabVIEW parameter’s enumerated elements exactly (name, case and value). Any mismatch will result in an edit-time error. If a TestStand flag enum is passed to a LabVIEW ring parameter with a floating point representation (Double, Extended, or Single precision) it will result in an error at edit-time and run-time. Every enumerator specified in the TestStand enum value should have a matching enumerator in the LabVIEW enum. Flag enums can have multiple enumerators combined together with an OR operator. The numeric value of the TestStand enumerator should match the numeric value of the corresponding LabVIEW enumerator. If there are multiple flags combined with an OR operator, as in the case of a flag enum, their combined numeric value should match in TestStand and LabVIEW.If the numeric representation of the TestStand Enum doesn’t match the LabVIEW Enum or Ring control, you will get a run-time error in all cases. | The elements of a TestStand Enum data type should match the LabVIEW parameter’s enumerated elements exactly (name, case and value). Any mismatch will result in an edit-time error. If a TestStand flag enum is passed to a LabVIEW ring parameter with a floating point representation (Double, Extended, or Single precision) it will result in an error at edit-time and run-time. If the numeric representation of the TestStand Enum doesn’t match the LabVIEW Enum or Ring control, you will get a run-time error in all cases. |
| String | If the variable’s value exactly matches any of the LabVIEW enumerated parameter’s elements, the numeric value of the element is passed to LabVIEW. If there is no match, you will get a run-time error.Assigning a duplicate enumerator name (more than one element with the same name) will result in an error. | If the numeric value received from LabVIEW matches any of the enumerated parameter’s elements, then the matching element’s name is stored in the string. If the numeric value does not match any element, its string representation surrounded by angular brackets is stored.Assigning a duplicate enumerator value to the string variable will result in an error. |
| Number | The numeric value is passed to the LabVIEW Enum or Ring control. If the variable’s numeric representation doesn’t match that of the LabVIEW enumerator control, you will get a run-time error. | The numeric value of the LabVIEW Enum or Ring indicator is assigned to the TestStand number. If the variable’s numeric representation doesn’t match that of the LabVIEW enumerator control, you will get a run-time error. |

#### See Also

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Normalizing Numeric Values You Pass to Enumeration Parameter Values](/csh?context=ts_tsref_labview_enum_params_range)

[Numeric Parameters](numeric-parameters-labview-vi-call-parameters.html)

[References](references-labview-vi-call-parameters.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enumeration-parameters-labwindows-cvi-call-pa.html language=enus -->
## TOPIC 03671: Enumeration Parameters - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enumeration-parameters-labwindows-cvi-call-pa.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enumeration-parameters-labwindows-cvi-call-pa.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumeration Parameters You can pass enumerations you create as named data types. When you create or edit an enumeration data type, you can specify whether the type can be a C structure argument and how the type represents itself in memory when you pass it to a structure parameter or array parameter.

### Enumeration Parameters - LabWindows/CVI Call Parameters

#### Enumeration Parameters

You can pass enumerations you create as named data types. When you create or edit an enumeration data type, you can specify whether the type can be a C structure argument and how the type represents itself in memory when you pass it to a structure parameter or array parameter.

The following settings are available in the Data Type ring control when you select
 Enumeration
 for the category type:

| Numeric Data Type Setting | Equivalent C Data Type |
| --- | --- |
| Signed 8-bit Integer | char |
| Unsigned 8-bit Integer | unsigned char |
| Signed 16-bit Integer | short |
| Unsigned 16-bit Integer | unsigned short |
| Signed 32-bit Integer | long |
| Unsigned 32-bit Integer | unsigned long |
| Signed 64-bit Integer | long long, __int64 |
| Unsigned 64-bit Integer | unsigned long long, unsigned __int64 |
| 32-bit Real Number | float |
| 64-bit Real Number | double |

#### Enum Type

When you select the Enumeration category for a parameter, the LabWindows/CVI Adapter displays the Enum Type control. This control allows you to specify the Enumeration data type necessary for the parameter in the Value Expression control. Additionally, the Value Expression control becomes a combo box where you can select enumerators of the enumeration. You can also enter an enumeration name or the corresponding numeric value for the enumeration directly into the Value Expression or Function Call controls.

When you select an Enumeration parameter that accepts an enumerated type from a code module that has a type library, TestStand will automatically check if the Enumeration data type and the type library enumeration have exactly matching enumerators. If not, then the Enum Type chosen will be shown in red with a warning message regarding the detected mismatch.

#### Pass by Value or by Reference

When you select the Enumeration category for a parameter, the LabWindows/CVI Adapter displays the Pass control. This control specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Reference (by pointer)
 , the LabWindows/CVI Adapter passes a pointer to the argument value.

If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property. When you select the Enumeration category for the return value, you may leave the Value Expression control empty or specify the name of a variable or property.

Note

NULL

Nothing

0

#### Result Actions

The LabWindows/CVI Adapter displays the Result Action ring control and the Set Error.Code to Value option for return values and parameters you pass by pointer. Depending on the settings of these controls, TestStand can automatically set the
 Error.Occurred
 and
 Error.Code
 properties of the step according to the value in the enumeration argument when the function returns.

Use the Result Action ring control to configure TestStand to set the
 Error.Occurred
 property to
 True
 when the return value or parameter value after the call is greater than zero, less than zero, equal to zero, or not equal to zero. Use the Set Error.Code control to request TestStand to assign the output value of the argument to the
 Error.Code
 property.

Note

Error.Code

Error.Code

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/enumeration-parameters-python-call-parameters.html language=enus -->
## TOPIC 03672: Enumeration Parameters - Python Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/enumeration-parameters-python-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/enumeration-parameters-python-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumeration Parameters You can pass TestStand enumerations to Python module calls as Python enumerations. To pass the TestStand enumeration as a Python enumeration, specify a type mapping between the TestStand enumeration and the Python enumeration on the Python Parameter Passing tab of the Type Pro

### Enumeration Parameters - Python Call Parameters

#### Enumeration Parameters

You can pass TestStand enumerations to Python module calls as Python enumerations. To pass the TestStand enumeration as a Python enumeration, specify a type mapping between the TestStand enumeration and the Python enumeration on the Python Parameter Passing tab of the Type Properties dialog box.

Note

Python defines four categories of enumerations: Enum, Flag, IntEnum, and IntFlag. The following table lists how different TestStand enumeration types map to the corresponding Python enumeration types.

| TestStand Enumeration Type | Python Enumeration Type |
| --- | --- |
| Loose | IntFlag |
| Strict and not Flag | Enum/IntEnum |
| Strict and Flag | Flag |

#### See Also

[Type Properties Dialog Box](type-properties-dialog-box.html)

[Edit Enumerators Dialog Box](edit-enumerators-dialog-box.html)

Parent topic:

Python Call Parameters

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/error-dialog-box.html language=enus -->
## TOPIC 03673: Error Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/error-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/error-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Error dialog box when an error occurs while using the TestStand Sequence Editor or custom user interface. This dialog box displays a description of the error and error code. Certain errors include additional details. Click Expand/Collapse Details to view or hide these addition

### Error Dialog Box

TestStand launches the Error dialog box when an error occurs while using the TestStand Sequence Editor or custom user interface.

This dialog box displays a description of the error and error code. Certain errors include additional details. Click
 Expand/Collapse Details
 to view or hide these additional details. If there are no additional details, the button is hidden.

Some errors are related to a specific step in an open TestStand sequence file. If step location information is available, the dialog will ask if you want to go to the step in question. Click
 Yes
 to go to the step where the error occurred. Click
 No
 to dismiss the dialog without going to the step.

#### See Also

[Run-Time Error dialog box](run-time-error-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/error-out-cluster.html language=enus -->
## TOPIC 03674: Error Out Cluster

- bundle_id: `teststand-api-reference`
- source_path: `tsref/error-out-cluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/error-out-cluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand uses the content of the error out cluster to determine when a run-time error occurs and when to take appropriate action if necessary. When you create a VI, use the standard LabVIEW error out cluster. The following table lists the elements of the error out cluster, specifies the data type o

### Error Out Cluster

TestStand uses the content of the
 error out
 cluster to determine when a run-time error occurs and when to take appropriate action if necessary. When you create a VI, use the standard LabVIEW
 error out
 cluster.

The following table lists the elements of the
 error out
 cluster, specifies the data type of the cluster element, describes how the LabVIEW Adapter uses each cluster element, and specifies the TestStand property to which the adapter copies the cluster element value.

| Cluster Element | Data Type | Description | TestStand Property to Which the Adapter Copies the Value |
| --- | --- | --- | --- |
| status |  | The test VI must set this element to True when an error occurs. | Step.Result.Error.Occurred |
| code |  | The test VI can set this element to a non-zero value when an error occurs. | Step.Result.Error.Code |
| source |  | The test VI can set this element to a descriptive string when an error occurs. | Step.Result.Error.Msg |

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/error-query-operation-edit-ivi-tools-step-dia.html language=enus -->
## TOPIC 03675: Error Query Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/error-query-operation-edit-ivi-tools-step-dia.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/error-query-operation-edit-ivi-tools-step-dia.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Error Query Operation The Error Query operation queries the instrument and returns instrument-specific error information. Use this operation after another operation in the instrument driver returns the IVI_ERROR_INSTR_SPECIFIC error code. The driver returns IVI_ERROR_INSTR_SPECIFIC when the instrume

### Error Query Operation - Edit IVI Tools Step Dialog Box

#### Error Query Operation

The Error Query operation queries the instrument and returns instrument-specific error information. Use this operation after another operation in the instrument driver returns the
 IVI_ERROR_INSTR_SPECIFIC
 error code. The driver returns
 IVI_ERROR_INSTR_SPECIFIC
 when the instrument’s status register indicates the instrument’s error queue is not empty. The Error Query operation extracts the first error from the instrument’s error queue. For instruments that have status registers but no error queue, the driver simulates an error queue in software.

The Error Query operation contains the following options:

- Error Code 
 —A variable or property to which the step assigns the error code returned from the instrument error query.
- Error Message 
 —A variable or property to which the step assigns the readable description of the error code.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/errors-warnings-in-the-database-options-dialo.html language=enus -->
## TOPIC 03676: Errors/Warnings in the Database Options dialog box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/errors-warnings-in-the-database-options-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/errors-warnings-in-the-database-options-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click on Apply or OK in the Database Options dialog box to validate the options in the Logging/Data Link Options and the default (checked) schema, and to launch the Errors/Warnings in the Database Options dialog box if there is an error or warning. The Errors/Warnings in Database Options dialog box

### Errors/Warnings in the Database Options dialog box

Click on
 Apply
 or
 OK
 in the Database Options dialog box to validate the options in the Logging/Data Link Options and the default (checked) schema, and to launch the Errors/Warnings in the Database Options dialog box if there is an error or warning.

The Errors/Warnings in Database Options dialog box contains the following controls:

- Logging/Data Link Options 
 —Displays the list of errors in Logging/Data Link Options in the Database Options dialog box. Click
 Fix 
 to take the focus to the selected error/warning.
- Next 
 —Shows the tab displaying the errors/warnings in default (checked) schema options. This button is enabled only if there are errors/warnings in default schema options.
- Default Schema (Schema Name) 
 —Displays the list of errors/warnings in the default schema options in the Database Options dialog box. Click
 Fix 
 to take the focus to the selected error/warning.
- Back 
 —Shows the tab displaying the errors in Logging/Data Link Options. This button is enabled only if there are errors in Logging/Data Link Options in the Database Options dialog box.
- Filter 
 —Shows the filter level displayed in the grid of selected tab.
  - Errors and Warnings—Displays both errors and warnings on the grid.
  - Errors Only—Displays only errors on the grid.
  - Warnings Only—Displays only warnings on the grid.
- Status Bar 
 —Displays the number of errors each in Logging/Data Link Options and the default (checked) schema.
- Revalidate 
 —Validates the options in the Logging/Data Link Options and the default (checked) schema and updates the Errors/Warnings in the grids.
- Done 
 —Saves the options in the Database Options dialog in the current state and closes the dialog box. Click done to close the main dialog box if the dialog box is launched when clicking the OK button.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/events-table.html language=enus -->
## TOPIC 03677: Events Table

- bundle_id: `teststand-api-reference`
- source_path: `tsref/events-table.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/events-table.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Events Table The Events table displays a list of all the events the Execution Profiler has recorded. Each row in the table displays the following information about an event: Index —The zero-based index of the event. The profiler assigns indexes in the order in which it receives events. Event —The so

### Events Table

#### Events Table

The Events table displays a list of all the events the Execution Profiler has recorded. Each row in the table displays the following information about an event:

- Index 
 —The zero-based index of the event. The profiler assigns indexes in the order in which it receives events.
- Event 
 —The source of the operation, such as Step, UUT, Lock, Step Module, etc, followed by a description of the action performed. Examples:
 Step Module: Execute 
 ,
 Step Module: Load 
 ,
 Notification: Set 
 ,
 Queue: Enqueue 
 .
- State 
 —The current state of the operation the event belongs to. Possible states are Blocked, In Use, Aborted, Timed Out, and Completed. Events occur only to signal a change in the state of an operation. The Aborted state can indicate
 
 that a thread waiting on a Use Auto Scheduled Resource step has switched to a different Use Auto Scheduled Resource step that is available or has fewer threads waiting to acquire it.
- Item Name 
 —The name of the item to which the event applies.
- Time 
 —The time at which the event occurred. The time is relative to the first recorded event.
- Test Socket 
 —The zero-based test socket index, if any, for the thread in which the operation takes place. The test socket index indicates the UUT position or test fixture on which the thread operates.
- Thread 
 —The display name of the thread that generated the event.
- Step 
 —The name of the step that generated the event.
- Step Index 
 —The index in the step group of the step that generated the event.
- Step Group 
 —The step group of the step that generated the event.
- Sequence 
 —The name of the sequence that contains the step that generated the event.
- File 
 —The base name of the sequence file that contains the step that generated the event.
- Absolute Time 
 —The date and time at which the event occurred.
- Timeout Period 
 —The timeout period. This column is empty unless the event if from a synchronization operation that blocked and the operation specifies a timeout period. Because a Blocked event occurs after a thread is unable to immediately acquire a resource, the timeout value recorded is slightly after the actual timeout period begins, so the displayed timeout period might be somewhat less than the configured value.
- Resource Alternative Index 
 —The zero-based index of the resource alternative a Use Auto Scheduled Resource step selects. Use the Use Auto Scheduled Resource steps to specify alternative sets of resources. The resource set the step actually acquires varies according to the availability of resources at the time the step executes. This column is empty when the event is not for a Use Auto Scheduled Resource step or when the step specifies only one resource alternative.
- Operation Index 
 —The zero-based index of the operation that contains the event. You can sort by operation index to group events together according to operations to which the events belong.

#### See Also

[Profiler Window Tables](profiler-window-tables.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Profiler Window Tables

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/excel-plugins.html language=enus -->
## TOPIC 03678: Excel Plugins

- bundle_id: `teststand-api-reference`
- source_path: `tsref/excel-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/excel-plugins.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Excel Plugins Excel plugins will import data in the specified worksheet of an Excel file. Excel plugins support import/export to Excel Workbook (.xlsx) format. You will be able to import/export data from the Excel Workbook format even on a machine where Microsoft Excel is not installed. See the Prop

### Excel Plugins

#### Excel Plugins

Excel plugins will import data in the specified worksheet of an Excel file. Excel plugins
support import/export to Excel Workbook (.xlsx) format. You will be able to import/export
data from the Excel Workbook format even on a machine where Microsoft Excel is not
installed.

See the
 [Property Loader Plugins - File Formats](/csh?context=ts_tsref_propertyloaderplugins_fileformat)
 topic for more information about the required file structure for this plugin.

#### Import Options

This plugin contains the following plugin-specific import options:

Worksheet
 — Specifies the name of the worksheet in the workbook containing the data to
import.

#### Export Options

This plugin contains the following plugin-specific export options:

Worksheet
 — Specifies the name of the worksheet in the workbook to which to export the data.

Note

File Format Type
 — Specifies the format in which the data should be exported. You can
choose one of the following options:

- Default — Number of columns is not fixed. Ex: All the subproperties of a container will be
specified in one line. The number of columns will grow as the number of subproperties.
- Flattened — Number of columns is fixed. A line will contain the lookup of the property
along with its value.

Optional Information To Export
 — Specifies what optional information should be created in the
 property loader source. You can choose to export the following optional information:

- Sequence — Add the sequence information containing the sequence name.
- Type — Add the type information containing the type name of the property.
- Category — Add the Category information containing where the property exists. The information is
not mandatory if all the property being exported contains alias names.

Parent topic:

Property Loader Plugins

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execute-menu.html language=enus -->
## TOPIC 03679: Execute Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execute-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execute-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Each process model defines a set of Execution entry points . Each entry point is a sequence in the process model file that invokes a test sequence file. Execution entry points appear at the top of the Execute menu in the TestStand Sequence Editor . For example, the default process model provides the

### Execute Menu

Each process model defines a set of
 [Execution entry points](/csh?context=ts_tsfundamentals_using_exe_entry_points)
 . Each entry point is a sequence in the process model file that invokes a test sequence file.

Execution entry points appear at the top of the Execute menu in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 . For example, the default process model provides the Test UUTs and Single Pass Execution entry points. When you select an Execution entry point, you invoke an execution using the active sequence file as the client sequence file.

The Execute menu contains the following options:

- Test UUTs 
 —Initiates an execution using the active sequence file as the client sequence file for the Test UUTs Execution entry point in the process model. The first Execution entry point defined in the process model specifies the display name for the command.
- Single Pass 
 —Initiates an execution using the active sequence file as the client sequence file for the Single Pass Execution entry point in the process model. The second Execution entry point defined in the process model specifies the display name for the command.
- Run <
 Sequence
 > 
 —Initiates an execution of the active sequence without using a process model.
- Restart 
 —Initiates a restart of the execution in the active Execution window. The TestStand Sequence Analyzer does not reanalyze sequences when you restart an execution.
- Run Selected Steps 
 —Executes selected steps in a sequence
 interactively 
 . When you execute steps in a Sequence File window, you initiate the interactive execution as an independent, top-level execution. When you execute steps in an Execution window for a suspended sequence execution, you initiate the interactive execution as an extension of the suspended execution.
- Run Selected Steps Using 
 —Interactively executes selected steps using the entry point you select. When you execute the steps using an Execution entry point, such as Single Pass, the process model generates a report and logs the results to a database. The Run Selected Steps Using command is available only in a Sequence File window.
- Loop On Selected Steps 
 —Interactively loops on the selected steps without a Process Model entry point. The Loop on Selected Steps command is available only in a Sequence File window.
- Loop On Selected Steps Using 
 —Interactively loops on the selected steps using the entry point you select. When you loop on steps using an Execution entry point, such as Single Pass, the process model generates a report and logs the results to a database. The Loop on Selected Steps Using command is available only in a Sequence File window.
- Break on First Step 
 —Suspends execution on the first step TestStand executes whenever you initiate execution in the active sequence. When enabled, this command has a checkmark beside it in the menu.
- Break on Step Failure 
 —Suspends execution on steps that result in a step status of
 Failed 
 . When enabled, this command has a checkmark beside it in the menu. If a step in a process model sequence file causes the sequence to which the step belongs to fail, TestStand only suspends the execution if tracing for the sequence or if a previous suspend occurred within the sequence context.
- Break on Sequence Failure 
 —Suspends execution on steps that cause the sequence to fail. When enabled, this command has a checkmark beside it in the menu. If a step in a process model sequence file causes the sequence to which the step belongs to fail, TestStand only suspends the execution if tracing for the sequence or if a previous suspend occurred within the sequence context. TestStand also suspends an execution if the
 SequenceContext.SequenceFailed 
 property is set during the execution of a step even when the step does not fail.
- Tracing Enabled 
 —Highlights each step as it becomes the active step during execution. When you disable this feature, updates to the Execution window only occur when execution is suspended. When enabled, this command has a checkmark beside it in the menu.
- Clear LabVIEW Builder Cache 
 —Clears PPL data for the executed sequence files, when the
 Build Source Files and Execute 
 feature is enabled.
  - Clear Cache for Sequence File 
 —Clears the data for the PPLs generated for the active sequence file. On the next execution of the sequence file, the PPLs required are generated again. Use this option to reset the state of the LabVIEW Builder Cache for the active sequence file.
  - Globally 
 —Clears the PPL data for all sequence files that have been executed till now.

#### See Also

[SequenceContext.SequenceFailed](../tsapiref/sequencecontext-sequencefailed.html)

[Build Source Files and Execute](/csh?context=ts_tsref_build_and_execute)

Parent topic:

Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execute-menu2.html language=enus -->
## TOPIC 03680: Execute Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execute-menu2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execute-menu2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Each process model defines a set of Execution entry points . Each entry point is a sequence in the process model file that invokes a test sequence file. Execution entry points appear at the top of the Execute menu in a TestStand User Interface . For example, the default process model provides the Te

### Execute Menu

Each process model defines a set of
 [Execution entry points](/csh?context=ts_tsfundamentals_using_exe_entry_points)
 . Each entry point is a sequence in the process model file that invokes a test sequence file.

TestStand User Interface

Note

list bar

The Execute menu contains the following options:

- Test UUTs 
 —Initiates an execution using the active sequence file as the client sequence file for the Test UUTs Execution entry point in the process model. The first Execution entry point defined in the process model specifies the display name for the command.
- Single Pass 
 —Initiates an execution using the active sequence file as the client sequence file for the Single Pass Execution entry point in the process model. The second Execution entry point defined in the process model specifies the display name for the command.
- Run <Sequence> 
 —Initiates an execution of the active sequence without using a process model.
- Run Selected Steps 
 —Executes selected steps in a sequence
 interactively 
 . When you execute steps in a Sequence File window, you initiate the interactive execution as an independent, top-level execution. When you execute steps in an Execution window for a suspended sequence execution, you initiate the interactive execution as an extension of the suspended execution.
- Run Selected Steps Using 
 —Interactively executes selected steps using the entry point you select. When you execute the steps using an Execution entry point, such as Single Pass, the process model generates a report and logs the results to a database. The Run Selected Steps Using command is available only in a Sequence File window.
- Loop On Selected Steps 
 —Interactively loops on the selected steps without a Process Model entry point. The Loop on Selected Steps command is available only in a Sequence File window.
- Loop On Selected Steps Using 
 —Interactively loops on the selected steps using the entry point you select. When you loop on steps using an Execution entry point, such as Single Pass, the process model generates a report and logs the results to a database. The Loop on Selected Steps Using command is available only in a Sequence File window.
- Break on First Step 
 —Suspends execution on the first step TestStand executes whenever you initiate execution in the active sequence. When enabled, this command has a checkmark beside it in the menu.
- Break on Step Failure 
 —Suspends execution on steps that result in a
 step status 
 of
 Failed 
 . When enabled, this command has a checkmark beside it in the menu. If a step in a process model sequence file causes the sequence to which the step belongs to fail, TestStand only suspends the execution if tracing for the sequence or if a previous suspend occurred within the sequence context.
- Break on Sequence Failure 
 —Suspends execution on steps that cause the sequence to fail. When enabled, this command has a checkmark beside it in the menu. If a step in a process model sequence file causes the sequence to which the step belongs to fail, TestStand only suspends the execution if tracing for the sequence or if a previous suspend occurred within the sequence context. TestStand also suspends an execution if the
 SequenceContext.SequenceFailed 
 property is set during the execution of a step even when the step does not fail.
- Tracing Enabled 
 —Highlights each step as it becomes the active step during execution. When you disable this feature, updates to the Execution window only occur when execution is suspended. When enabled, this command has a checkmark beside it in the menu.
- Clear LabVIEW Builder Cache 
 —Clears PPL data for the executed sequence files, when the
 Build Source Files and Execute 
 feature is enabled.
  - Clear Cache for Sequence File 
 —Clears the data for the PPLs generated for the active sequence file. On the next execution of the sequence file, the PPLs required are generated again. Use this option to reset the state of the LabVIEW Builder Cache for the active sequence file.
  - Globally 
 —Clears the PPL data for all sequence files that have been executed till now.

#### See Also

[List Bar](list-bar.html)

[SequenceContext.SequenceFailed](../tsapiref/sequencecontext-sequencefailed.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execute-sql-tab.html language=enus -->
## TOPIC 03681: Execute SQL Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execute-sql-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execute-sql-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Execute SQL Tab Use the Execute SQL tab to execute SQL queries on a database connection. Select File»New Execute SQL Tab or press <Ctrl+E> to create a new Execute SQL tab. The Execute SQL tab contains the following options: SQL Editor Window —Contains a text editor in which you can enter SQL queries

### Execute SQL Tab

#### Execute SQL Tab

Use the Execute SQL tab to execute SQL queries on a database connection. Select
 File»New Execute SQL Tab
 or press <Ctrl+E> to create a new Execute SQL tab.

The Execute SQL tab contains the following options:

- SQL Editor Window 
 —Contains a text editor in which you can enter SQL queries to execute. The SQL queries you enter can contain a
 single command or multiple delimited commands 
 . Use the context menu options for formatting the text. Press <Ctrl+F> or launch the Find window from the context menu to perform find and replace operations.
- Data Grid 
 —Displays any table data the executed query returns. The Next Result and Previous Result buttons are available when multiple tables exist.
- Results Tab 
 —Contains a
 data grid 
 . If the SQL query does not return any table data, this tab is not visible.
- Output Tab 
 —Displays the executed SQL query, the status of the execution, and any errors that occur on execution. The Database Viewer appends the status of the latest execution to the end of the previous output.
- Status Bar 
 —Displays the status of the database connection and query execution. The status bar includes the following information:
  - Database Connection 
 —Displays the name of the connection associated with the tab.
  - Connection Status 
 —Indicates one of the following statuses of the database connection.
    - Connected 
 —An open connection to the database exists.
    - Disconnected 
 —The database connection is closed but still valid. The next time you perform an operation, the Database Viewer reopens the connection and uses the reopened connection.
    - Expired 
 —The database connection is broken, and the Database Viewer returns an error when you try to reconnect.
  - Query Execution Status 
 —Displays one of the following statuses of the last executed query.
    - None 
 —No executions have been completed.
    - Query Executed Successfully 
 —The SQL query was executed without errors.
    - Query Executed with Errors 
 —The SQL query execution resulted in errors.
  - Rows Affected 
 —Displays the number of rows the last executed query affects. Typically, only queries that perform insert, delete, or update operations affect rows in a table.
 Note 
 MySQL also returns the number of rows retrieved by a Select command as rows a query execution affects.
  - Auto-Refresh Status 
 —Indicates whether the Auto-Refresh option for the tab is enabled or disabled. If Auto-Refresh is enabled, the status bar also displays the user-specified time interval in seconds.

The Execute SQL tab also contains the following options:

- Execute 
 —Sets and executes the SQL query against the database connection associated with the tab. You can also press <Ctrl+F5> to perform this command.
 Note 
 Schema update operations that SQL queries execute from the Execute SQL tab do not update the Database Object View. The view updates the next time you refresh the connection.
- Refresh 
 —Executes the set SQL query again. This operation maintains any specified custom settings for displaying data in the data grid. You can also press <Ctrl+R> to perform this command.
- Stop Execution 
 —Cancels the execution of the query. You can also press <Shift+F5> to perform this command.
- Load from SQL File 
 —Launches an Open File dialog box in which you can specify a .sql file to load. The contents of the file replace any existing content in the SQL Editor window. You can also press <Ctrl+L> to perform this command.
- Save to SQL File 
 —Launches a Save File dialog box in which you can specify a path to save the current content of the SQL Editor as a .sql file.
- Auto-Refresh 
 —Updates the data the data grid displays in a user-specified time interval. When you enable Auto-Refresh, the query in the SQL editor executes and displays the returned data, if any. When the specified time interval elapses, the same query executes again.
 Note 
 If the specified time interval elapses when the current execution is in progress, the query executes again only after the time interval elapses a second time.
 If you add or remove any columns from a table after the SELECT query executes, the data grid does not display the updated columns even if you issue a Refresh or Auto-Refresh command. You must execute the query again to obtain the updates to the columns.
 If Auto-Refresh is disabled, clicking the
 Auto-Refresh
 button launches the Auto-Refresh Options dialog box.
 If Auto-Refresh is enabled, clicking the
 Auto-Refresh
 button disables Auto-Refresh.
- Print 
 —Launches the
 Print 
 dialog box.
- Export Data 
 —Launches the
 Export Document 
 dialog box.
- Clear Output 
 —Clears the execution history the output tab displays. You can also press <Ctrl+D> to perform this command.
- Save Output 
 —Launches a standard Save File dialog box, in which you can specify a path to save the current content of the Output window as a text file.

#### See Also

[Executing SQL Commands in the Execute SQL Window](/csh?context=ts_tsref_dbviewer_sqlwindow)

Parent topic:

Database Viewer Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execution-operation-wait-settings-edit-tab.html language=enus -->
## TOPIC 03682: Execution Operation - Wait Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execution-operation-wait-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execution-operation-wait-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Execution Operation Use the Execution operation to wait for the completion of a TestStand execution. Enable the Execution option on the left of the Wait Settings panel. The Execution operation contains the following options: Specify by Sequence Call —The execution to wait for by selecting a sequence

### Execution Operation - Wait Settings Edit Tab

#### Execution Operation

Use the Execution operation to wait for the completion of a TestStand execution. Enable the
 Execution
 option on the left of the Wait Settings panel.

The Execution operation contains the following options:

- Specify by Sequence Call 
 —The execution to wait for by selecting a sequence call within the same sequence as the Wait step. You can only specify sequence calls that run in the same sequence and in a new execution.
- Specify an Object Reference to the Execution 
 —An ActiveX reference to the TestStand execution on which to wait.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior when waiting for an execution. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Wait Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execution-operation-wait-step-configuration-d.html language=enus -->
## TOPIC 03683: Execution Operation - Wait Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execution-operation-wait-step-configuration-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execution-operation-wait-step-configuration-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Execution Operation Use the Execution operation to wait for the completion of a TestStand execution. The Execution operation contains the following options: Specify by Sequence Call —The execution to wait for by selecting a sequence call within the same sequence as the Wait step. You can only specif

### Execution Operation - Wait Step Configuration Dialog Box

#### Execution Operation

Use the Execution operation to wait for the completion of a TestStand execution.

The Execution operation contains the following options:

- Specify by Sequence Call 
 —The execution to wait for by selecting a sequence call within the same sequence as the Wait step. You can only specify sequence calls that run in a new execution.
- Specify an Object Reference to the Execution 
 —An ActiveX reference to the TestStand execution on which to wait.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior when waiting for an execution. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Wait Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execution-profiler-window.html language=enus -->
## TOPIC 03684: Execution Profiler Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execution-profiler-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execution-profiler-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The tabs in the top half of the profiler window display the profiler window graphs . The tabs in the bottom half of the profiler window display the profiler window tables . You can adjust the splitter bar that separates the graphs and tables. The profiler window includes menus you can use to control

### Execution Profiler Window

The tabs in the top half of the profiler window display the
 [profiler window graphs](/csh?context=ts_tsref_resource_usage_profiler_graphs)
 . The tabs in the bottom half of the profiler window display the
 [profiler window tables](profiler-window-tables.html)
 . You can adjust the splitter bar that separates the graphs and tables.

The profiler window includes
 [menus](menus-execution-profiler.html)
 you can use to control the operation and display of the profiler data. You can also right-click selections in the tables and graphs to display context menus.

The following controls at the bottom of the profiler window apply to all profiler graphs and tables:

- Update Display 
 —If this button is off, the profiler retains new information but does not display it so the tables and graphs remain static while you view them.
- Collect Profiling Information 
 —The profiler discards any events it receives when this button is off.
- Hide Completed Operations Shorter than 
 —If the value in this control is greater than zero, the profiler does not display complete operations with a duration shorter than the specified value.
- Clear 
 —Discards all profiler information.

#### See Also

[Execution Profiler](/csh?context=ts_9920)

[Comparing Resource Usage Strategies (Example)](/csh?context=ts_8130)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execution-settings-dialog-box.html language=enus -->
## TOPIC 03685: Execution Settings Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execution-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execution-settings-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Edit Sequence Call dialog box, select Run Sequence in a New Execution from the ring control in the Multithreading and Remote Execution section, and click Settings to launch the Execution Settings dialog box. The Execution Settings dialog box contains the following options: Initially Suspe

### Execution Settings Dialog Box

Launch the
 [Edit Sequence Call](edit-sequence-call-dialog-box.html)
 dialog box, select
 Run Sequence in a New Execution
 from the ring control in the Multithreading and Remote Execution section, and click
 Settings
 to launch the Execution Settings dialog box.

The Execution Settings dialog box contains the following options:

- Initially Suspended 
 —When you enable this option, TestStand creates the new execution in a suspended state. Call the
 Execution.Resume 
 method in the TestStand API to start the execution.
 Note 
 If you select
 Break
 or
 Resume
 in the
 [Debug](debug-menu.html)
 menu of the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , it does not affect an initially suspended execution.
- Initially Hidden and Disable Tracing 
 —When you enable this option, the window for the new execution is initially hidden and tracing is initially disabled.
 Note 
 If you enable the Initially Hidden and Disable Tracing option, TestStand ignores the Break on Entry option in this dialog box when calling new executions.
- Restartable 
 —When you enable this option, the execution can be restarted after it completes.
- Close Window when Done 
 —When you enable this option, TestStand closes the window for the execution when the execution completes.
- Use Single-Threaded Apartment 
 —Specifies whether the concurrency model of the thread is initialized as single-threaded apartment (STA) or multi-threaded apartment. By default, TestStand initializes new executions and threads to use the multi-threaded apartment model (MTA). A thread must use the single-threaded apartment model when the thread creates or launches a dialog box that contains ActiveX controls.
 If you use this option to launch a sequence that contains a step that displays an ActiveX control, you may need to set the Load Option in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to Load Dynamically. This ensures that TestStand loads the module the step in the thread initialized as STA calls.
- Wait for Execution to Complete 
 —When you enable this option, TestStand waits for the execution to complete. The following options are available in the ring control:
  - Do not wait 
 —Calling sequence does not wait for the execution to complete. Use this option and insert a Wait step in the sequence when you want to obtain the results, status, and error information from an asynchronous execution call.
  - Before executing next step 
 —Calling sequence waits for the execution to complete before executing another step.
  - At end of current sequence 
 —Calling sequence waits for the execution to complete before the calling sequence returns.
- Process Model Option 
 —Specifies which process model the new execution uses. The following options are available in the ring control:
  - Do not use a process model 
 —The new execution does not run under a process model.
  - Use process model of the specified client file 
 —The execution runs under the process model the sequence file you call specifies as the model of the sequence file. If the file you call does not specify a model, the execution runs under the default station model. When you select this option, you can use the
 Edit Sequence Call 
 dialog box to designate which entry point to call in the process model. Typically, the Process Model entry point calls
 MainSequence 
 in the client sequence file you specify.
  - Use a specific process model 
 —When you select this option, you can use the controls in the
 Edit Sequence Call 
 dialog box to specify the process model under which the new execution runs. When you select this option, you can use the
 Edit Sequence Call 
 dialog box to designate which entry point to call in the process model. Typically, the Process Model entry point calls
 MainSequence 
 in the client sequence file you specify.
- Additional Execution Type Mask Settings (optional) 
 —Passes a numeric value that specifies the
 execution mask settings 
 for the new execution. The settings you specify in this control are combined with any execution mask settings other options in the dialog box specify.
- Store an ActiveX Reference to the new Execution in (optional) 
 —Stores a reference to the new
 Execution 
 object in the ActiveX reference variable you specify. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in a Wait step to wait for the execution to complete.
- Break on Entry 
 —When you enable this option, TestStand suspends the execution before executing the first step.
 Note 
 If you enable the Initially Hidden and Disable Tracing option in this dialog box, TestStand ignores the Break on Entry option when calling new executions.
- CPU Affinity for Initial Thread of Execution 
 —Specifies the CPUs on which the initial thread of the execution executes. The following options are available in the ring control:
  - Use Station Option for CPU Affinity 
 —TestStand uses the
 Default CPU Affinity For Threads station option 
 on the Preferences tab of the Station Options dialog box as the CPU affinity of the initial thread.
  - Use CPU Affinity of Caller 
 —TestStand uses the CPU affinity of the calling sequence as the CPU affinity of the initial thread.
  - Use All CPUs 
 —TestStand uses all CPUs available to the process as the CPU affinity of the initial thread.
  - Use Custom CPU affinity 
 —TestStand determines the CPU affinity of the initial thread using an expression that evaluates to a numeric value, where each bit represents a CPU. The lowest order bit represents the first CPU. For example, a value of
 12 
 (
 1100 
 ) represents CPUs 3 and 4 on a quad-core computer. A value of
 -1 
 represents all CPUs available to the process.

#### See Also

[CPU Affinity Mask Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64cpuaffinitymask)

[Edit Sequence Call dialog box](edit-sequence-call-dialog-box.html)

[Execution](../tsapiref/execution.html)

[ExecutionTypeMask](../tsapiref/executiontypemask.html)

[Station Options dialog box](preferences-tab-station-options-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Edit Sequence Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execution-tab-station-options-dialog-box.html language=enus -->
## TOPIC 03686: Execution Tab - Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execution-tab-station-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execution-tab-station-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Execution Tab The Execution tab has options for breakpoints, tracing, and interactive execution. The Execution tab contains the following options: Enable Breakpoints —Enables all breakpoints. When you enable breakpoints, the following additional option is available: Honor Breakpoints while Terminati

### Execution Tab - Station Options Dialog Box

#### Execution Tab

The Execution tab has options for breakpoints, tracing, and interactive execution.

The Execution tab contains the following options:

- Enable Breakpoints 
 —Enables all breakpoints. When you enable breakpoints, the following additional option is available:
  - Honor Breakpoints while Terminating 
 —Honors breakpoints when terminating an execution.
- Allow Break While in Code Modules 
 —TestStand displays an execution as suspended so you can debug it even if one or more threads are executing code inside a code module, which can be useful when code modules take a long time to complete, are blocked waiting for something, or are running continuously in the background. While the execution is suspended, steps with running code modules show a status of
 Running 
 . If the code module completes while the execution is suspended, the thread suspends immediately after returning from the code module until you resume the execution. Because this option is enabled by default, you do not need to use the
 Thread.ExternallySuspended 
 property unless you disable this option. When you disable this option, TestStand displays an execution as suspended only when all threads are between steps or in a code module that uses the
 Thread.ExternallySuspended 
 property.
- Enable Tracing 
 —Enables tracing. When tracing is in effect, the
 TestStand Sequence Editor 
 or TestStand User Interface application displays each step as it executes. This is useful for debugging but adds significant performance overhead to the execution of the test programs. When you enable tracing, the following additional options are available:
 Note 
 You can also enable this option from the
 [Execute](execute-menu.html)
 menu using the Tracing Enabled command.
  - Speed 
 —TestStand inserts a delay between trace events sent to the sequence editor or any user interface. This delay applies only when tracing is enabled. Use this option to slow down the tracing so you can observe each step as it executes.
  - Allow Tracing into Setup/Cleanup 
 —Enables tracing of steps in the Setup and Cleanup step groups of each sequence.
  - Allow Tracing into Pre-/Post-Step Callbacks 
 —Enables tracing of steps in any of the Pre-Step and Post-Step Engine callback sequences.
  - Allow Tracing into Post Action Callbacks 
 —Enables tracing of steps in Post Action callbacks.
  - Allow Tracing into Sequence Calls Marked with Tracing "Disabled" 
 —Enables tracing into all subsequences when tracing for the calling sequence.
 On the
 [Run Options panel](run-options-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane, you can choose a setting that disables tracing when the step calls a subsequence. When you enable this option, TestStand ignores the step property setting and does not alter the tracing state when it calls the subsequence.
  - Allow Tracing While Terminating 
 —Enables tracing of steps that run while execution is terminating. Examples of steps that can run while an execution is terminating are steps in Cleanup step groups that run when you terminate execution in the middle of a sequence.
  - Trace into Separate Execution Callbacks 
 —Enables tracing in callbacks that run as executions separate from the top-level sequence execution. Examples include Front-End callbacks and callbacks you execute from the
 Tools 
 menu.
  - Trace into Entry Points 
 —Enables tracing of steps in Process Model entry point sequences, such as the Test UUTs and Single Pass entry points.
- Interactive Executions 
 —Use this section to set options that apply when you run steps interactively.
  - Record Results 
 —Records the results of steps you run interactively. When you run steps interactively from an Execution window when suspended in a normal execution, TestStand appends the results to the result list for the active sequence invocation so the results appear in the test report for the normal execution.
 When you run steps interactively from a Sequence File window, TestStand accumulates the results in a result list for the interactive execution. If the interactive execution uses a process model that generates a report, the interactive step results appear in the report. You can also access an interactive execution result list from an Engine post-interactive callback.
  - Run Setup and Cleanup 
 —TestStand runs the Setup and Cleanup step groups for the sequence that contains the selected steps. This option applies only when you run the steps from a Sequence File window.
  - Evaluate Preconditions 
 —TestStand evaluates the preconditions for steps that execute in interactive mode. When you disable this option, TestStand honors the Run Mode settings of steps.
  - Branching Mode 
 —Use this option to specify the action TestStand takes when it executes a Goto step or evaluates a post action that specifies a destination step while running an interactive execution. The Branching mode contains the following options:
 
 Note 
 Changes to the Branching Mode option affect only currently executing interactive executions.
    - Ignore All Branching 
 —The interactive execution ignores all branches. TestStand executes the selected steps in the order the sequence editor or user interface specifies.
    - Ignore Branches to Unselected Steps 
 —The interactive execution allows branching within the selected steps. TestStand ignores all branching to non-selected steps.
    - Go to End on Branches to Unselected Steps 
 —The interactive execution allows branching within the selected steps. TestStand ignores all branching to non-selected steps and terminates the current pass for the interactive execution instead.
    - Raise Error on Branches to Unselected Steps 
 —The interactive execution allows branching within selected steps. Branching to non-selected steps will cause a run-time error.
    - Allow All Branching 
 —The interactive execution allows branching to selected steps and non-selected steps. When TestStand executes a selected step and no branch occurs, the next step is the next selected step. When TestStand executes a non-selected step and no branch occurs, the next step is the step after the non-selected step.
- Propagate Failures and Errors from Nested Interactive Execution to Calling Execution 
 —When you enable this option, TestStand allows sequence failure, goto cleanup, and error settings from a nested interactive execution to propagate to the invoking execution.
 Note 
 When you enable this option, TestStand propagates the result status of the interactive execution, including results that pass and that do not error or go to cleanup, back to the main execution. Therefore, if the calling execution is currently in a failed state, running a nested interactive execution that finishes in a passed state causes the calling execution to finish in a passed state. Disable this option if you do not want the status of the interactive execution to affect the main execution.
- On Run-Time Error 
 —Use this option to specify the action TestStand takes when a run-time error occurs. The following options are available in the ring control:
  - Show Dialog Box 
 —Launches the
 Run-Time Error 
 dialog box when a run-time error occurs. The Run-Time Error dialog box lists the step and the cause of the error and then prompts you with options for handling the error. Options for handling the error include ignoring the error and continuing execution, retrying the step, jumping to the Cleanup step group, and aborting immediately. You can also choose to break at the current step and to suppress the Run-Time Error dialog box during the remainder of the current execution.
  - Run Cleanup 
 —Causes the execution to jump to the Cleanup step group. If the error propagates normally to the calling sequence, the calling sequence also jumps to the Cleanup step group so the cleanup steps run for all active sequences and the execution terminates.
  - Ignore 
 —Clears the error occurred flag for the step and execution proceeds at the next step in the sequence.
  - Abort Immediately (No Cleanup) 
 —Immediately halts execution without running cleanup steps.
- Immediately Goto Cleanup On Sequence Failure 
 —Causes the execution to jump to the Cleanup step group when a step sets the sequence status to
 Failed 
 . This option applies only to sequences for which you have set the On Step Failure option on the
 General 
 tab of the
 Sequence Properties 
 dialog box to
 Use Station Option 
 .
 Notice 
 This option applies to all sequence files, including process model files. Therefore, a Process Model entry point can jump to the Cleanup step group if the
 MainSequence
 callback step does not disable the Step Failure Causes Sequence Failure setting and if you set the On Step Failure sequence setting for the entry point sequence to either Use Station Option or Goto Cleanup. 
 Note 
 This setting takes precedence over Goto Destination post action settings.
 If this setting and the Branching Mode setting for interactive executions is not set to Ignore All Branching, when a step failure causes the interactive execution to fail, the interactive execution immediately stops executing the selected steps.
- Disable Result Recording for All Sequences 
 —When you disable result recording with this option, the process model does not generate a result report for sequence executions.

#### See Also

[Execute Menu](execute-menu.html)

[Run-Time Error dialog box](run-time-error-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Tools Menu](tools-menu.html)

Parent topic:

Station Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execution-tab.html language=enus -->
## TOPIC 03687: Execution Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execution-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execution-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A TestStand User Interface displays the Execution tab when you view the list of open executions in the list bar control. The Execution tab displays the state of the selected execution. The Execution tab contains the following panes: Steps —The steps in the currently executing sequence. Variables —Di

### Execution Tab

A
 [TestStand User Interface](teststand-user-interfaces.html)
 displays the Execution tab when you view the list of open executions in the
 [list bar](list-bar.html)
 control. The Execution tab displays the state of the selected execution.

The Execution tab contains the following panes:

- Steps 
 —The steps in the currently executing sequence.
- Variables 
 —Displays a sequence context from the selected execution. You can inspect and modify values of properties and variables.
- Call Stack 
 —The sequences in the call stack used in the current thread. Select an item in this control to display the steps in a specific sequence or subsequence in the call stack.
- Threads 
 —The threads in the current execution. Select a thread in this control to view the currently executing steps in the thread.

The following buttons appear along the bottom of the Execution tab:

- Break/Resume 
 —Click
 Break 
 to suspend the selected execution after the current step completes. Click
 Resume 
 to continue execution when in a breakpoint state.
- Terminate/Restart 
 —Click
 Terminate 
 to terminate a running or suspended execution. A running execution terminates only after completing the currently executing step. When you terminate an execution, TestStand runs the Cleanup step groups for all active sequences on the call stack. Click
 Restart 
 to rerun a completed execution.

#### See Also

[List Bar](list-bar.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/execution-window.html language=enus -->
## TOPIC 03688: Execution Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/execution-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/execution-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TestStand Sequence Editor launches a separate Execution window for each execution you start using the Execute menu. The Execution window contains the following panes: Steps —A list of steps in the step group currently executing for the sequence invocation currently selected in the Call Stack pan

### Execution Window

The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 launches a separate Execution window for each execution you start using the
 [Execute](execute-menu.html)
 menu. The Execution window contains the following panes:

- Steps 
 —A list of steps in the step group currently executing for the sequence invocation currently selected in the
 Call Stack 
 pane.
- Variables 
 —The sequence context for the sequence invocation currently selected in the Call Stack pane.
- Report 
 —The report for the current execution.

Use the tabs at the bottom of the Execution window to navigate between the panes you have open. You can float or dock these panes anywhere within the Execution window.

In addition to the panes on in the Execution window, the sequence editor window contains the following panes you can use when you select a running or suspended Execution window:

- Step Settings 
 —The module and settings for the selected step or steps on the Steps pane of the Execution window.
- Call Stack 
 —The call stack for the execution thread currently running in the Threads pane.
- Threads 
 —All threads running in the execution.
- Watch View 
 —The values of watch expressions you enter.
- Output 
 —The output messages posted to TestStand.

The
 [Status Bar](status-bar.html)
 displays information about the selected steps on the Steps pane of the Execution window.

#### Debugging

The sequence editor and
 [TestStand User Interfaces](teststand-user-interfaces.html)
 give you several methods for debugging, including the ability to step over or into steps, step out of sequences, and set the next step to execute. You can also terminate execution, abort execution, toggle tracing, and run or loop on selected steps. These commands are located in the
 [Execute](execute-menu.html)
 menu, in the
 [Debug](debug-menu.html)
 menu, and on the
 [Debug toolbar](toolbar-buttons-and-shortcuts.html)
 of the sequence editor and in the context menu for the
 [Steps](steps-pane-sequence-file-window.html)
 pane.

#### See Also

[Debug Menu](debug-menu.html)

[Execute Menu](execute-menu.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Toolbar Buttons and Shortcuts](toolbar-buttons-and-shortcuts.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/executionoutputrecordstream-and-executionoutp.html language=enus -->
## TOPIC 03689: ExecutionOutputRecordStream and ExecutionOutputRecordStreams

- bundle_id: `teststand-api-reference`
- source_path: `tsref/executionoutputrecordstream-and-executionoutp.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/executionoutputrecordstream-and-executionoutp.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: ExecutionOutputRecordStream and ExecutionOutputRecordStreams implement functionality related to attaching OutputRecordStream objects to executions. In addition to exposing methods similar to the OutputRecordStream interface for writing data, they also expose methods and properties to control how dat

### ExecutionOutputRecordStream and ExecutionOutputRecordStreams

ExecutionOutputRecordStream and ExecutionOutputRecordStreams implement functionality related to attaching OutputRecordStream objects to executions. In addition to exposing methods similar to the OutputRecordStream interface for writing data, they also expose methods and properties to control how data is displayed in the Report view. If you are running in a process model, the ExecutionOutputRecordStream.CloseAtNextUUTOrBatch property tells the process model to close streams automatically at the beginning of the next UUT or batch.

You can access the OutputRecordStream objects attached to an execution via Execution.OutputRecordStreams, which is a collection of ExecutionOutputRecordStream objects. An ExecutionOutputRecordStream object contains zero or more OutputRecordStream objects.

Parent topic:

Data Streams API

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/executions-table.html language=enus -->
## TOPIC 03690: Executions Table

- bundle_id: `teststand-api-reference`
- source_path: `tsref/executions-table.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/executions-table.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executions Table A TestStand execution is a grouping of one of more TestStand threads. The Executions table contains a list of all executions that contain threads for which the Execution Profiler recorded events. The profiler does not show executions that do not contain threads that perform profiled

### Executions Table

#### Executions Table

A TestStand execution is a grouping of one of more TestStand threads. The Executions table contains a list of all executions that contain threads for which the Execution Profiler recorded events. The profiler does not show executions that do not contain threads that perform profiled operations. Each row in the table displays the following information about an execution:

- Execution Id 
 —The TestStand execution Id. This value is unique to each execution.
- Execution 
 —The display name of the TestStand execution
- Threads 
 —The number of threads in the execution for which the profiler recorded events.
- Items 
 —The total number of profiled items that threads in the execution access.
- Operations 
 —The total number of operations that threads perform in the execution.

#### See Also

[Profiler Window Tables](profiler-window-tables.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Profiler Window Tables

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/exit-synchronized-section-operation-batch-syn.html language=enus -->
## TOPIC 03691: Exit Synchronized Section Operation - Batch Synchronization Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/exit-synchronized-section-operation-batch-syn.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/exit-synchronized-section-operation-batch-syn.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exit Synchronized Section Operation Use the Exit Synchronized Section operation to mark the end of a synchronized section. Enable the Exit Synchronized Section option on the left of the Batch Synchronization Settings panel. The Exit Synchronized Section operation contains the following options: Sect

### Exit Synchronized Section Operation - Batch Synchronization Settings Edit Tab

#### Exit Synchronized Section Operation

Use the Exit Synchronized Section operation to mark the end of a synchronized section. Enable the
 Exit Synchronized Section
 option on the left of the Batch Synchronization Settings panel.

The Exit Synchronized Section operation contains the following options:

- Section Name 
 —The name of the synchronized section to exit. Leave this control blank to refer to the most nested section.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior for when a thread must wait at an Exit step. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Batch Synchronization Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/exit-synchronized-section-operation-batch-syn2.html language=enus -->
## TOPIC 03692: Exit Synchronized Section Operation - Batch Synchronization Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/exit-synchronized-section-operation-batch-syn2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/exit-synchronized-section-operation-batch-syn2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exit Synchronized Section Operation Use the Exit Synchronized Section operation to mark the end of a synchronized section. The Exit Synchronized Section operation contains the following options: Section Name —The name of the synchronized section to exit. Leave this control blank to refer to the most

### Exit Synchronized Section Operation - Batch Synchronization Step Configuration Dialog Box

#### Exit Synchronized Section Operation

Use the Exit Synchronized Section operation to mark the end of a synchronized section.

The Exit Synchronized Section operation contains the following options:

- Section Name 
 —The name of the synchronized section to exit. Leave this control blank to refer to the most nested section.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior for when a thread must wait at an Exit step. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Batch Synchronization Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/export-data-to-csv-file-dialog-box.html language=enus -->
## TOPIC 03693: Export Data to CSV File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/export-data-to-csv-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/export-data-to-csv-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the Export Data to CSV File dialog box, navigate to the Test Vector and Value Summary Table View from the Sweep Parameters tab on the Sweep Loop step. Click Open Table View and click Export Test Vectors to CSV File from either the Edit or the Execution tab. You can use the Export Data to C

### Export Data to CSV File Dialog Box

To launch the Export Data to CSV File dialog box, navigate to the Test Vector and Value Summary Table View from the Sweep Parameters tab on the
 [Sweep Loop](sweep-loop-step.html)
 step. Click
 Open Table View
 and click
 Export Test Vectors to CSV File
 from either the Edit or the Execution tab. You can use the Export Data to CSV File dialog to generate the sweep parameter values specified by the step and export them to a CSV file.

The Export Data to CSV File dialog contains the following options:

- CSV Directory Path 
 —Specifies the path of the CSV file.
- File Name 
 —Specifies the file name under which to which TestStand saves the file.
- Data Tag 
 —Specifies the data tag for the CSV file. When exporting, this tag is written out before the prototype and data. When importing, TestStand searches the file for this tag and begins reading the prototype on the following line.
- File Open Mode 
 —Expression that specifies the file open mode for the underlying CSV file. The mode can be any of the following FileOpenModes constants:
  - FileOpenMode_NoOptions 
 —Create the file if it does not exist. Fail with a runtime error if the file exists.
  - FileOpenMode_Truncate 
 —If the file exists, overwrite it, deleting the previous contents. Create a new file if it does not exist.
  - FileOpenMode_Append 
 —If the file exists, append to the end of it, preserving the existing contents. Create a new file if it does not exist.
  - FileOpenMode_Uniquify 
 —Create a new file if it does not exist. If a file with the specified path exists, attempt to make the file name unique by appending “_” (underscore) plus a numeric suffix to the file name. For example, if AlreadyExists.csv already exists, AlreadyExists_2.csv is tried, then AlreadyExists_3.csv, etc. until a unique name has been found. If a unique name is not found after 10000 attempts, the operation fails with a runtime error.
- Automatically Launch Default External Viewer checkbox 
 —Select this option to automatically launch the default external value after you export the data to a CSV file.
- Export Button 
 —Generates the sweep parameter values defined by this step and saves them to the specified CSV file.

Parent topic:

Sweep Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/export-document-dialog-box.html language=enus -->
## TOPIC 03694: Export Document Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/export-document-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/export-document-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select File»Export Document or click the Export button in the Edit Data or Execute SQL tabs to launch the Export Document dialog box, in which you can export the table data displayed in the data grid of the currently active tab to a file. The Database Viewer supports the following file formats: CSV

### Export Document Dialog Box

Select
 File»Export Document
 or click the
 Export
 button in the
 [Edit Data](edit-data-tab.html)
 or
 [Execute SQL](execute-sql-tab.html)
 tabs to launch the Export Document dialog box, in which you can export the table data displayed in the
 [data grid](data-grid.html)
 of the currently active tab to a file.

The Database Viewer supports the following file formats:

- CSV
- HTML
- PDF
- RTF
- TXT
- XLS
- XLSX (Microsoft Excel 2007)

The Database Viewer supports the following image file formats:

- BMP
- EMF
- GIF
- JPEG
- PNG
- TIFF
- WMF

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/export-items-to-file-dialog-box.html language=enus -->
## TOPIC 03695: Export Items to File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/export-items-to-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/export-items-to-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Export button in the Configure Sequence Analyzer Available Rules dialog box to launch the Export Items to File dialog box, in which you export custom rules and analysis module specifications on the computer to a rules file. The Export Items to File dialog box contains the following items:

### Export Items to File Dialog Box

Click the
 Export
 button in the
 [Configure Sequence Analyzer Available Rules](configure-sequence-analyzer-available-rules-d.html)
 dialog box to launch the Export Items to File dialog box, in which you export custom rules and analysis module specifications on the computer to a rules file.

The Export Items to File dialog box contains the following items:

- Select Items to Export 
 —Lists the custom rules and analysis module specifications you can export. You cannot export built-in rules or analysis module specifications.
 When you export a custom rule that has a configuration module, you must manually copy the configuration module—a DLL or VI—and any supporting files, such as string files, the rule configuration module requires to the target computer.
 When you export a custom analysis module specification, you must manually copy the analysis module—a DLL or VI—and any supporting files, such as string files, the analysis module requires to the target computer.
- Export 
 —Launches a file dialog box, in which you create or browse for the rules file to use.

#### See Also

[Configure Sequence Analyzer Available Rules dialog box](configure-sequence-analyzer-available-rules-d.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/export-options-tab-import-export-properties-t.html language=enus -->
## TOPIC 03696: Export Options Tab - Import/Export Properties Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/export-options-tab-import-export-properties-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/export-options-tab-import-export-properties-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Export Options Tab The Export Options tab contains the following options: Destination Type —Specifies the type of the property loader source to which values of TestStand properties will be exported. Destination Location —Specifies location of the property loader source to which data will be exported

### Export Options Tab - Import/Export Properties Tool

#### Export Options Tab

The Export Options tab contains the following options:

- Destination Type 
 —Specifies the type of the property loader source to which values of TestStand
properties will be exported.
- Destination Location 
 —Specifies location of the property loader source to which data will be
exported. If property loader source is file, this specifies the file path and if property loader
source is database, this specifies the connection string.
- Alias Location 
 —Specifies the location of the alias. If property loader source is file, this
specifies the location of alias file and if property loader source is database, this specifies the
name of the alias table.
- Identify Steps By 
 —Specifies the lookup to uniquely identify a step in the
sequence file and is stored in the destination file/database by the plugin.

Parent topic:

Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/export-options-tab-import-export-properties-t_2.html language=enus -->
## TOPIC 03697: Export Options Tab - Import/Export Properties Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/export-options-tab-import-export-properties-t_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/export-options-tab-import-export-properties-t_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Export Options Tab The Export Options tab contains the following options: Destination Type —Specifies the type of the property loader source to which values of TestStand properties will be exported. Destination Location —Specifies location of the property loader source to which data will be exported

### Export Options Tab - Import/Export Properties Tool

#### Export Options Tab

The Export Options tab contains the following options:

- Destination Type 
 —Specifies the type of the property loader source to which values of TestStand
properties will be exported.
- Destination Location 
 —Specifies location of the property loader source to which data will be
exported. If property loader source is file, this specifies the file path and if property loader
source is database, this specifies the connection string.
- Alias Location 
 —Specifies the location of the alias. If property loader source is file, this
specifies the location of alias file and if property loader source is database, this specifies the
name of the alias table.
- Identify Steps By 
 —Specifies the lookup to uniquely identify a step in the
sequence file and is stored in the destination file/database by the plugin.

Parent topic:

Import/Export Properties Tool

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/export-tools-menu-dialog-box.html language=enus -->
## TOPIC 03698: Export Tools Menu Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/export-tools-menu-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/export-tools-menu-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Open the Customize Tools Menu dialog box and click Export Items to File to launch the Export Tools Menu dialog box. In this dialog box, select the items you want to export to a tool menu file. Use the Tools menu files to distribute tools menu items to other TestStand installations. Install tool menu

### Export Tools Menu Dialog Box

Open the
 [Customize Tools Menu](customize-tools-menu-dialog-box.html)
 dialog box and click
 Export Items to File
 to launch the Export Tools Menu dialog box. In this dialog box, select the items you want to export to a tool menu file. Use the Tools menu files to distribute tools menu items to other TestStand installations. Install tool menu files in
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Setup\ToolMenusToInstall
 and uninstall files in
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Setup\ToolMenusToUninstall
 .

When TestStand starts, it appends the items stored in all tool menu files in the install directory to the tools menu. TestStand then removes the items in the tool menu files in the uninstall directory. After processing the tools menu items, TestStand deletes the tool menu files.

The Export Tools Menu dialog box contains the following options:

- Check the Menu Items You Want to Export 
 —Listbox containing a list of menu items available for export. The Tools menu list on the
 Customize Tools Menu 
 dialog box populates this list.
- Move Up 
 and
 Move Down 
 —Changes the order of items within the menu.
- File Name 
 —The path to which TestStand saves the file. The file extension must be
 .ini 
 .

#### See Also

[Customize Tools Menu dialog box](customize-tools-menu-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/expression-browser-dialog-box.html language=enus -->
## TOPIC 03699: Expression Browser Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/expression-browser-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/expression-browser-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Expression Browse button in any dialog box which requires you to enter or edit an expression to launch the Expression Browser dialog box, in which you can interactively build an expression by selecting from lists of variables, properties, operators, functions, and the TestStand API. The Ex

### Expression Browser Dialog Box

Click the
 Expression Browse
 button in any dialog box which requires you to enter or edit an expression to launch the Expression Browser dialog box, in which you can interactively build an expression by selecting from lists of variables, properties, operators, functions, and the TestStand API.

The Expression Browser contains the following tabs for building
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 :

- Variables/Properties 
 —Select variables and properties from this tab.
- Operators/Functions 
 —Select operators and functions from this tab.
- TestStand API 
 —Select properties and methods from the TestStand API from this tab.

In addition to the Variables/Properties, Operators/Functions, and TestStand API tabs, the Expression Browser dialog box contains the following options:

- Expression 
 —The expression you build interactively using the tabs above. You can also type an expression directly into this control.
- Check Syntax 
 —Verifies the syntax of the expression in the Expression control.

The expression editor includes visual assistance for finding and manipulating nested delimiters such as parenthesis, brackets, and braces.

- Place your cursor to the left of a delimiter and the expression editor makes the matching pair bold.
- Type <Ctrl + ]> to toggle the cursor between the matching delimiters.
- Type <Ctrl + Shift + ]> to select the matching delimiters and everything between them.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/expression-edit-tab.html language=enus -->
## TOPIC 03700: Expression Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/expression-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/expression-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Expression edit tab in the TestStand Sequence Editor to specify expressions for a Statement step. The step can access objects, variables, and properties during an execution. The Expression edit tab contains the following option: Expression —The expression the step evaluates. Click the Expres

### Expression Edit Tab

Use the Expression edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 for a Statement step. The step can access
 [objects, variables, and properties](/csh?context=ts_tsfundamentals_seq_con)
 during an execution.

The Expression edit tab contains the following option:

- Expression 
 —The expression the step evaluates.

Click the
 Expression Browse
 button to launch the
 [Expression Browser](expression-browser-dialog-box.html)
 dialog box. Click the
 Check Expression for Errors
 button to determine whether the expression syntax is valid.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Sequence Context](/csh?context=ts_tsfundamentals_seq_con)

Parent topic:

Statement Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/expression-editing-options-dialog-box.html language=enus -->
## TOPIC 03701: Expression Editing Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/expression-editing-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/expression-editing-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Station Options dialog box and click Expression Editing Options on the Preferences tab or select Options from the context menu of an ExpressionEdit control to launch the Expression Editing Options dialog box. The Expression Editing Options dialog box contains the following options: Text E

### Expression Editing Options Dialog Box

Launch the
 [Station Options](station-options-dialog-box.html)
 dialog box and click
 Expression Editing Options
 on the
 [Preferences](preferences-tab-station-options-dialog-box.html)
 tab or select
 Options
 from the context menu of an ExpressionEdit control to launch the Expression Editing Options dialog box.

The Expression Editing Options dialog box contains the following options:

- Text Element 
 —Selects a text element. This section specifies the following font settings for each text element:
  - Color 
 —Color for the specified text element.
  - Bold 
 —Bold style for specified text element.
  - Italic 
 —Italic style for specified text element.
  - Underline 
 —Underline style for specified text element.
  - Strikethrough 
 —Strikethrough style for specified text element.
- Auto Completion 
 —Completes the current word or shows the contents of a container when typing. This section contains the following options:
  - On 
 —Enables Auto Completion.
  - Alphabetize Items 
 —Sorts items in the Auto Completion listbox alphabetically.
  - Categorize Items 
 —Groups items in the Auto Completion listbox categorically and then alphabetically within each category.
- Function Tip 
 —Tooltip-like help that appears when typing a function. This section contains the following options:
  - Prototype 
 —Display the function name and parameters in the help.
  - Summary 
 —Display a brief description of the function in the help.
  - Details 
 —Display a detailed description of the function in the help.
  - Show Automatically 
 —When you enable this option, the ExpressionEdit control automatically displays the function tip while typing. When you disable this option, you must use the defined hot key to display the function tip.
- Hot Keys 
 —Customizes the hot key for a specified menu item. This section contains the following options:
  - Menu Item 
 —Selects the menu item of the hot key to customize. You can customize the hot key for auto completion, function tip, check for errors, and browse.
  - Enter New Hotkey 
 —The hot key of the currently selected menu item.
- Other Options 
 —Additional options. This section contains the following options:
  - Word Wrap 
 —Causes lines too long to be displayed on one line to wrap to the next line.
 Note 
 This option applies only to ExpressionEdit controls in which the
 [WordWrap](../tsuiref/expressionedit-wordwrap.html)
 property is set to
 BooleanOrPreference_UsePreference
 .
  - Want Return 
 —When you enable this option, the ExpressionEdit control processes the Enter key.
 Note 
 This option applies only to ExpressionEdit controls in which the
 [WantReturn](../tsuiref/expressionedit-wantreturn.html)
 property is set to
 BooleanOrPreference_UsePreference
 .
  - Automatically Prefix Variables 
 —If you enable this option, when you type a variable name, the ExpressionEdit control automatically replaces the variable name with the full path of the variable. For example, if you type
 foo 
 and there is a local variable named
 foo 
 , the ExpressionEdit control replaces it with
 Locals.foo 
 . The ExpressionEdit control does not automatically prefix the variable name if the variable name is not unique. However, when you right-click a variable name, the context menu for the ExpressionEdit control lists the full path of every variable with the name and you can select a path to replace the variable name.
  - Undo Limit 
 —The maximum number of edits that can be undone. Enter
 -1 
 for no limit.
  - Font Size 
 —Specifies whether to use normal, large, or extra large font size when displaying text in an ExpressionEdit control.
- Reset Values to Defaults 
 —Restores all settings to their default values.
- Preview 
 —Displays sample expression text using the currently selected options.

#### See Also

[Station Options dialog box](station-options-dialog-box.html)

[WantReturn](../tsuiref/expressionedit-wantreturn.html)

[WordWrap](../tsuiref/expressionedit-wordwrap.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/expressions-panel-step-settings-pane.html language=enus -->
## TOPIC 03702: Expressions Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/expressions-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/expressions-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expressions Panel The Expressions panel specifies optional expressions TestStand evaluates before or after it calls the step module. It contains the following categories: Pre-Expression —An expression TestStand evaluates before it calls the code module . Use this expression to set the value of a cus

### Expressions Panel - Step Settings Pane

#### Expressions Panel

The Expressions panel specifies optional
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 TestStand evaluates before or after it calls the step module. It 
contains the following categories:

- Pre-Expression 
 —An expression TestStand evaluates before it calls the
 code module 
 . Use this expression to set the value of a custom step property from the values of other variables and properties.
- Post-Expression 
 —An expression TestStand evaluates after it calls the code module. Use this expression to set the value of one of the subproperties in the Result property of the step based on the values of other variables and properties.
- Status Expression 
 —Sets the Status property for the step. Because the status is a String property, this expression must evaluate to a string.
 If you leave an expression field empty, TestStand does not evaluate it. 
 Note 
 Certain types of steps, such as
 [Numeric Limit Test](numeric-limit-test-step.html)
 ,
 [Multiple Numeric Limit Test](multiple-numeric-limit-test-step.html)
 ,
 [String Value Test](string-value-test-step.html)
 ,
 [Pass/Fail Test](pass-fail-test-step.html)
 , and
 [Statement](statement-step.html)
 steps, reserve one or more of these expressions to perform operations specific to the type of step or a substep performs the operation. In these cases, you cannot use the expressions the step type reserves, which appear dimmed on the tab.

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/expressions-tab-step-properties-dialog-box.html language=enus -->
## TOPIC 03703: Expressions Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/expressions-tab-step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/expressions-tab-step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expressions Tab Use the Expressions tab to specify optional expressions TestStand evaluates before or after it calls the step module. The Expressions tab contains the following options: Pre-Expression —An expression TestStand evaluates before it calls the code module . Use this expression to set the

### Expressions Tab - Step Properties Dialog Box

#### Expressions Tab

Use the Expressions tab to specify optional expressions TestStand evaluates before or after it calls the step module.

The Expressions tab contains the following options:

- Pre-Expression 
 —An expression TestStand evaluates before it calls the
 code module 
 . Use this expression to set the value of a custom step property from the values of other variables and properties.
- Post-Expression 
 —An expression TestStand evaluates after it calls the code module. Use this expression to set the value of one of the subproperties in the Result property of the step based on the values of other variables and properties.
- Status Expression 
 —Sets the Status property for the step. Because the status is a String property, this expression must evaluate to a string.
 If you leave an expression field empty, TestStand does not evaluate it. 
 Note 
 Certain types of steps, such as Numeric Limit Tests, Multiple Numeric Limit Tests, String Value Tests, Pass/Fail Tests, and Statement steps, reserve one or more of these expressions to perform operations specific to the type of step or a substep performs the operation. In these cases, you cannot use the expressions the step type reserves, which appear dimmed on the tab.

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/external-diff-merge-tool-tab-file-differ-opti.html language=enus -->
## TOPIC 03704: External Diff/Merge Tool Tab - File Differ Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/external-diff-merge-tool-tab-file-differ-opti.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/external-diff-merge-tool-tab-file-differ-opti.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: External Diff/Merge Tool Tab Use the External Diff/Merge Tool tab to specify an external tool for showing the differences in string properties and comments. The External Diff/Merge Tool tab contains the following options: Use External Differ Tool —Enable this option when you want to specify an exter

### External Diff/Merge Tool Tab - File Differ Options Dialog Box

#### External Diff/Merge Tool Tab

Use the External Diff/Merge Tool tab to specify an external tool for showing the differences in string properties and comments.

The External Diff/Merge Tool tab contains the following options:

- Use External Differ Tool 
 —Enable this option when you want to specify an external tool for comparing string properties and comments in two files. When you enable this option, the following additional options become available:
  - Location 
 —The absolute file path to the external tool you want to use.
  - Arguments 
 —The arguments to pass to the external tool. The arguments must always begin with
 %1%2 
 .
- Use External Merge Tool 
 —Enable this option when you want to specify an external tool for comparing and merging differences in string properties and comments in three files. When you enable this option, the following additional options become available:
  - Location 
 —The absolute file path to the external tool you want to use.
  - Arguments 
 —The arguments to pass to the external tool. The arguments must always begin with
 %b%1%2%r 
 .

Click
 Launch External Diff/Merge Tool
 from the Differences Table context menu, from within the
 [TestStand File Diff and Merge](teststand-file-diff-and-merge-utility.html)
 utility for a selected value element or a comment element of a string property, or from the
 [View Change Details](view-change-details-dialog-box.html)
 dialog box. The TestStand File Diff and Merge utility launches a dialog box that remains visible until you close it or until you exit the external tool.

Parent topic:

File Differ Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/features-comparison-of-teststand-sequence-edi.html language=enus -->
## TOPIC 03705: Features Comparison of TestStand Sequence Editor and TestStand User Interfaces

- bundle_id: `teststand-api-reference`
- source_path: `tsref/features-comparison-of-teststand-sequence-edi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/features-comparison-of-teststand-sequence-edi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table illustrates the feature differences among the TestStand Sequence Editor , the TestStand User Interfaces in Editor Mode, and the TestStand User Interfaces in Operator Mode. Feature TestStand Sequence Editor User Interface Editor Mode User Interface Operator Mode Environment Dockin

### Features Comparison of TestStand Sequence Editor and TestStand User Interfaces

The following table illustrates the feature differences among the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , the
 [TestStand User Interfaces](teststand-user-interfaces.html)
 in Editor Mode, and the TestStand User Interfaces in Operator Mode.

| Feature | TestStand Sequence Editor | User Interface Editor Mode | User Interface Operator Mode |
| --- | --- | --- | --- |
| Environment |  |  |  |
| Docking, hiding, and floating panes |  | — | — |
| Configurable menus and toolbars |  | — | — |
| Navigation among sequences |  | — | — |
| Sequence Hierarchy window |  | — | — |
| Integrated sequence analysis |  | — | — |
| User management configuration |  | — | — |
| User privileges enforced |  |  |  |
| Configurable step list |  |  |  |
| Workspace support | Dockable pane | Modal dialog | Modal dialog |
| Source code control support | Integrated | Modal dialog | — |
| Configure report generation |  |  |  |
| Configure database logging |  |  |  |
| Configure station options |  |  |  |
| Editing |  |  |  |
| Edit sequence files |  |  | — |
| Insertion Palette |  |  | — |
| Edit steps and modules | Dockable panes | Modal dialogs | — |
| Integration with ADEs |  |  | — |
| Edit variables and station globals |  |  | — |
| Edit types |  | — | — |
| Edit process models |  |  | — |
| Multiple step editing |  | — | — |
| Undo and redo |  |  | — |
| Find and replace |  | — | — |
| Integrated file differ |  | — | — |
| Running |  |  |  |
| Multithreaded execution |  |  |  |
| Single-step debugging |  |  |  |
| Conditional breakpoints |  |  |  |
| Call stack and thread lists |  |  |  |
| Variables view |  |  |  |
| Watch view |  | — | — |
| Output messages view |  | — | — |
| Other |  |  |  |
| Can include in deployment |  |  |  |
| Source code available | — |  |  |
| Minimum license required | TestStand Development System License | TestStand Custom Sequence Editor License | TestStand Base Deployment License |

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/fetch-operation-edit-ivi-dmm-step-dialog-box.html language=enus -->
## TOPIC 03706: Fetch Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/fetch-operation-edit-ivi-dmm-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/fetch-operation-edit-ivi-dmm-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetch Operation The Fetch operation returns the measured value from a measurement the Initiate operation started. If the Trigger Count is greater than 1 and the Multi Point extension is enabled, the Fetch operation returns an array of values. Otherwise, the Fetch operation returns a single value. Ty

### Fetch Operation - Edit IVI Dmm Step Dialog Box

#### Fetch Operation

The Fetch operation returns the measured value from a measurement the Initiate operation started. If the Trigger Count is greater than
 1
 and the Multi Point extension is enabled, the Fetch operation returns an array of values. Otherwise, the Fetch operation returns a single value.

Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the
 [Initiate](initiate-operation-edit-ivi-dmm-step-dialog-b.html)
 operation. Before issuing a Fetch operation, use the Initiate operation in a separate step to initiate a measurement.

Note

The Fetch operation contains the following options:

- Data Type 
 —Specifies whether the step expects a single value or array of values. The step coerces the data type of the
 Step.Result.Reading 
 property to
 NI_IviSinglePoint 
 or
 NI_IviWave 
 , respectively.
- Measurement Destination 
 —A variable or property, as the following table describes, to which the step assigns the measurement value.
 Value Type
 Data Type of the Variable or PropertySingle values
 Number or
 NI_IviSinglePoint
 Array of values
 Array of Number or
 NI_IviWave 
 The default configuration for the step specifies
 Step.Result.Reading 
 as the destination. When you edit the step, the step automatically coerces the data type of the
 Step.Result.Reading 
 property to
 NI_IviSinglePoint 
 or
 NI_IviWave 
 , based on the value of the Data Type control. If you do not specify
 Step.Result.Reading 
 as the destination, TestStand copies the measurement value to the
 Step.Result.Reading.Data 
 property at run time unless the Copy Data to Execution Results option is disabled.
- Timeout (ms) 
 —The timeout, in milliseconds, for the operation. The Timeout setting applies to the length of time between initializing a call to Read and completing the data acquisition, not the time the DMM requires for computations or to transfer data across the instrumentation bus. To set an infinite timeout, set Timeout to
 -1 
 .
- Set Status on Timeout 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step ignores timeout conditions.
- Set Status if Over-Range 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step does not check for an over-range condition.
- Copy Data To Execution Results 
 —When you enable this option, TestStand copies the measurement value stored in the property
 Step.Result.Reading.Data 
 to the step result. When you enable this control, TestStand cannot include the measurement in a report or log the measurement to a database. This setting is always enabled for single-point measurements.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/fetch-operation-edit-ivi-scope-step-dialog-bo.html language=enus -->
## TOPIC 03707: Fetch Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/fetch-operation-edit-ivi-scope-step-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/fetch-operation-edit-ivi-scope-step-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetch Operation Channels Tab The Channels tab contains a list control with the default channels for the selected logical name. Use the Add and Remove buttons to add new channels and remove existing channels from the list. You can specify whether the oscilloscope acquires a waveform for the channel b

### Fetch Operation - Edit IVI Scope Step Dialog Box

#### Fetch Operation

#### Channels Tab

The Channels tab contains a list control with the default channels for the selected logical name. Use the
 Add
 and
 Remove
 buttons to add new channels and remove existing channels from the list. You can specify whether the oscilloscope acquires a waveform for the channel by enabling the channel in the list control.

The Channels tab for the Read operation also contains the following channel-specific options:

- Name 
 —The name of the channel to read. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.
- Waveform Type 
 —The type of data to retrieve from the oscilloscope. Depending on this value, the returned data is a single value (for a measurement), a one-dimensional array (Waveform), or a two-dimensional array (Waveform Min Max).
 
 Supported Value
 DescriptionAmplitude (15)
 High Voltage less the Low Voltage, in volts, over the entire waveform.
 Negative Duty Cycle (13)
 Ratio of the Negative Width to the Period of an integer number of cycles in the waveform, expressed as a percentage.
 Positive Duty Cycle (14)
 Ratio of the Positive Width to the Period of an integer number of cycles in the waveform, expressed as a percentage.
 Fall Time (1)
 Length of time, in seconds, for a falling edge of the signal to fall from the high reference level to the low reference level.
 Frequency (2)
 Frequency, in hertz, of one complete cycle in the waveform.
 Overshoot (18)
 Relative waveform distortion that follows an edge transition.
 Period (3)
 Length of time, in seconds, of one complete cycle in the waveform.
 Preshoot (19)
 Relative waveform distortion that precedes an edge transition.
 Rise Time (0)
 Length of time, in seconds, for a rising edge of the signal to rise from the low reference level to the high reference level.
 Average Voltage (10)
 Arithmetic average, in volts, measured over the entire waveform.
 Cycle Average Voltage (17)
 Arithmetic average, in volts, over an integer number of cycles in the waveform.
 Cycle Rms Voltage (16)
 True root-mean-square (RMS) voltage over an integer number of cycles in the waveform.
 High Voltage (8)
 Voltage that corresponds to 100% when using the reference levels. The oscilloscope calculates this value using either the min/max or histogram methods. The min/max method uses the maximum value found. The histogram method uses a common value found above the middle of the waveform.
 Low Voltage (9)
 Voltage that corresponds to 0% when using the reference levels. The oscilloscope calculates this value using either the min/max or histogram methods. The min/max method uses the minimum value found. The histogram method uses a common value found below the middle of the waveform.
 Max Voltage (6)
 Maximum amplitude, in volts, found in the entire waveform.
 Min Voltage (7)
 Minimum amplitude, in volts, found in the entire waveform.
 Peak To Peak Voltage (5)
 Absolute difference, in volts, between the Max Voltage and the Min Voltage.
 Rms Voltage (4)
 True root-mean-square (RMS) voltage of the entire waveform.
 Negative Width (11)
 Length of time, in seconds, between the mid-reference level points of a negative pulse in the waveform.
 Positive Width (12)
 Length of time, in seconds, between the mid-reference level points of a positive pulse in the waveform.
 Waveform (-1)
 Specifies that the Read or Fetch operation acquires a waveform with the current configuration. If specified, Read returns a one-dimensional array of points.
 Min/Max (-2)
 Specifies that the
 [Read](read-operation-edit-ivi-scope-step-dialog-box2.html)
 or Fetch operation acquires a min-max waveform that is a two-dimensional array. This constant is valid only when
 Acquisition Type
 is set to Peak Detect or Envelope.
- Data Type 
 —Specifies whether the step expects a single value, an array of values, or a wave pair. The step coerces the data type of the elements in the array property,
 Step.Result.Reading 
 , to
 NI_IviSinglePoint 
 ,
 NI_IviWave 
 , or
 NI_IviWavePair 
 , respectively.
- Measurement Destination 
 —A variable or property to which the step assigns the measurement value. For single values, the data type of the variable or property must be Number or
 NI_IviSinglePoint 
 . For an array of values, the data type of the variable or property must be array of Number or
 NI_IviWave 
 . For a wave pair, the data type of the variable or property must be a two-dimensional array of Number or
 NI_IviWavePair 
 . The default configuration for the step specifies
 Step.Result.Reading 
 as the destination. This property is an array of container where the size of the array is equal to the number of channels specified for the Read or Fetch operation. When you edit the step, the step automatically resizes the array and coerces the data type of each element of the array to
 NI_IviSinglePoint 
 ,
 NI_IviWave 
 , or
 NI_IviWavePair 
 , based on the value of the Data Type control for each channel. If you do not specify
 Step.Result.Reading 
 as the destination, TestStand copies the measurement value to the Data subproperty in each array element at run time unless the Copy Data to Execution Results option is disabled.
- Set Status if Over-Range 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step does not check for an over-range condition.
- Copy Data to Execution Results 
 —When you enable this option, the TestStand copies the measurement value stored in the property
 Step.Result.Reading.Data 
 to the step result. When you enable this control, TestStand does not include the measurement in a report or log the measurement to a database. This setting is always enabled for single-point measurements.
- Timeout (mS) 
 —The timeout, in milliseconds, for the operation. The Timeout setting applies to the length of time between initializing a call to Read and completing the data acquisition, not the time the instrument requires for computations or to transfer data across the instrumentation bus. To set an infinite timeout, set Timeout to
 -1 
 .
- Set Status on Timeout 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step ignores timeout conditions.

Parent topic:

Fetch Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/fetch-operation-edit-ivi-scope-step-dialog-bo2.html language=enus -->
## TOPIC 03708: Fetch Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/fetch-operation-edit-ivi-scope-step-dialog-bo2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/fetch-operation-edit-ivi-scope-step-dialog-bo2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetch Operation The Fetch operation retrieves the measured value(s) from a previously started acquisition for the listed channels. Before calling the Fetch operation, use the Initiate or Read operation on any channel to initiate a measurement. You can use the Fetch operation multiple times on a chan

### Fetch Operation - Edit IVI Scope Step Dialog Box

#### Fetch Operation

The Fetch operation retrieves the measured value(s) from a previously started acquisition for the listed channels. Before calling the Fetch operation, use the Initiate or Read operation on any channel to initiate a measurement. You can use the Fetch operation multiple times on a channel to retrieve different types of data from the same acquisition. Typically, the Fetch operation is called only in a sequence of calls to other low-level driver operations, such as the Initiate operation.

Note

The Edit IVI Scope Step dialog box for the Fetch operation contains the following tabs:

- Channels 
 —Specifies which channel data to retrieve, the type of data, and where to store the data.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/fetch-operation-edit-ivi-scope-step-dialog-bo3.html language=enus -->
## TOPIC 03709: Fetch Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/fetch-operation-edit-ivi-scope-step-dialog-bo3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/fetch-operation-edit-ivi-scope-step-dialog-bo3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetch Operation Operation Settings Tab The Operation Settings tab for the Fetch operation contains the following channel-specific option: Settings Property/Variable —Specifies the property or variable to which the step saves the operation settings when closing the Edit IVI Scope Step dialog box, and

### Fetch Operation - Edit IVI Scope Step Dialog Box

#### Fetch Operation

#### Operation Settings Tab

The Operation Settings tab for the Fetch operation contains the following channel-specific option:

- Settings Property/Variable 
 —Specifies the property or variable to which the step saves the operation settings when closing the Edit IVI Scope Step dialog box, and reloads the operation settings when launching the Edit IVI Scope Step dialog box.

Parent topic:

Fetch Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/fgen-step.html language=enus -->
## TOPIC 03710: Fgen Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/fgen-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/fgen-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an IVI Fgen step to generate predefined or custom waveforms using arbitrary waveform generators. Configuring the Step Use the Edit IVI Fgen Step dialog box in the TestStand Sequence Editor and in a TestStand User Interface to configure the IVI Fgen step. Step Operations The IVI Fgen step type su

### Fgen Step

Use an IVI Fgen step to generate predefined or custom waveforms using arbitrary waveform generators.

#### Configuring the Step

Use the
 [Edit IVI Fgen Step](edit-ivi-fgen-step-dialog-box4.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the IVI Fgen step.

#### Step Operations

The IVI Fgen step type supports the following operations:

- Configure 
 —Configures the instrument to match the state the step specifies.
- Show Soft Front Panel 
 —Launches the soft front panel (SFP) for the instrument.
- Hide Soft Front Panel 
 —Hides the SFP for the instrument.
- Initiate 
 —Initiates signal generation when the instrument is idle.
- Abort 
 —Aborts a previously configured output and returns the function generator to the idle state.
- Send Software Trigger 
 —Sends a software command to trigger the instrument.
- Get Information 
 —Retrieves low-level status and information from the instrument.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the IVI Fgen step type defines the following step properties:

- Step.LogicalName 
 —The logical name expression.
- Step.InstrOperation 
 —A value that specifies the operation you configured the step to perform.
- Step.SettingsSource 
 —The name of the property or variable where the step loads and stores the settings for the operation.
- Step.Configuration 
 —The settings for the
 Configure 
 operation. The data type of this property is NI_IviFgenConfig.
- Step.SoftFrontPanel 
 —The settings for the Show Soft Front Panel operation. The data type of this property is NI_IviSoftFrontPanel.
- Step.GetInfo 
 —The settings for the Get Information operation.

Parent topic:

IVI Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-conflict-dialog-box.html language=enus -->
## TOPIC 03711: File Conflict Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-conflict-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-conflict-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the File Conflict dialog box when you specify a file in the Open File dialog box without selecting the Use Absolute Path option and when a file with the same name as the one you selected was found in the TestStand search paths . The File Conflict dialog box contains the following

### File Conflict Dialog Box

TestStand launches the File Conflict dialog box when you specify a file in the
 [Open File](open-file-dialog-box.html)
 dialog box without selecting the Use Absolute Path option and when a file with the same name as the one you selected was found in the
 [TestStand search paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

The File Conflict dialog box contains the following options:

- Use a relative path for the file shown above 
 —TestStand uses a relative path for the file found in the TestStand search paths.
- Use an absolute path for the file you selected 
 —TestStand uses an absolute path instead of a relative path.
- Use a relative path for the file you selected 
 —TestStand uses a relative path file even though it cannot locate the file within the TestStand search paths.
- Substitute Path Macros 
 —Enable this option to substitute the
 $(Platform)
 macro 
 for the last directory in a path that matches the current platform. For example, 64-bit TestStand replaces
 C:\bin\x64\module.dll 
 with
 C:\bin\$(Platform)\module.dll 
 . This option applies to absolute paths and to relative paths TestStand finds through non-recursive search directories. This option is not available for files TestStand finds by searching subdirectories.

#### See Also

[Open File dialog box](open-file-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-differ-options-dialog-box.html language=enus -->
## TOPIC 03712: File Differ Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-differ-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-differ-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Options button in the Select Files dialog box or on the TestStand File Diff and Merge utility toolbar or select Edit»Options to launch the File Differ Options dialog box, in which you can configure settings for the utility. The File Differ Options dialog box contains the following tabs: Ge

### File Differ Options Dialog Box

Click the
 Options
 button in the
 [Select Files](select-files-dialog-box.html)
 dialog box or on the
 [TestStand File Diff and Merge](teststand-file-diff-and-merge-utility.html)
 utility
 [toolbar](toolbar-buttons-and-shortcuts-teststand-file.html)
 or select
 Edit»Options
 to launch the File Differ Options dialog box, in which you can configure settings for the utility.

The File Differ Options dialog box contains the following tabs:

- General 
 —Options for configuring the utility.
- External Diff/Merge Tool 
 —Options for specifying an external tool for showing the differences in string properties and comments.

#### See Also

[Select Files dialog box](select-files-dialog-box.html)

[TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html)

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-format-options-dialog-box.html language=enus -->
## TOPIC 03713: File Format Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-format-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-format-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Station Options dialog box, click the File tab, and click File Format Options to launch the File Format Options dialog box, in which you can specify the file format for new files, the station globals file, the users file, the templates file, and type palette files. Choose from one of the

### File Format Options Dialog Box

Launch the
 [Station Options](station-options-dialog-box.html)
 dialog box, click the
 [File](file-tab-station-options-dialog-box.html)
 tab, and click
 File Format Options
 to launch the File Format Options dialog box, in which you can specify the file format for new files, the station globals file, the users file, the templates file, and type palette files.

Choose from one of the following formats:

- INI (format available in TestStand 3.
 x 
 or earlier)
 Note 
 The File Format Options dialog box no longer provides the option to change from another file format to INI. Reading INI files is still supported. Saving files in the INI format will be deprecated in a future release of TestStand.
- XML (most readable, largest)
 Note 
 National Instruments reserves the right to change the XML file format in future releases to support new features and to improve usability.
- Binary (fastest and smallest)

Notice

The File Format Options dialog box contains the following options:

- New Format for New Files 
 —The format in which TestStand saves new sequence files.
- File List 
 —Selects a TestStand file the Format setting for file control modifies.
- Format setting for file <
 selected file
 > 
 —The format in which TestStand saves the selected file in the file list.

You can also change the format of an existing sequence file by opening the
 [Sequence File Properties](sequence-file-properties-dialog-box.html)
 dialog box and changing the File Format option.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-globals-context-menu-sequence-file-tab.html language=enus -->
## TOPIC 03714: File Globals Context Menu - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-globals-context-menu-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-globals-context-menu-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: File Globals Context Menu To access the context menu, right-click the FileGlobals item on the Variables pane. The items in the context menu vary depending on whether you right-click a global variable or global variable subproperty. The File Globals context menu can contain the following items: Inser

### File Globals Context Menu - Sequence File Tab

#### File Globals Context Menu

To access the context menu, right-click the FileGlobals item on the
 [Variables](variables-pane-sequence-file-tab.html)
 pane. The items in the context menu vary depending on whether you right-click a global variable or global variable subproperty.

The File Globals context menu can contain the following items:

- Insert File Global 
 —A submenu from which you select the data type for the sequence file global variable you want to insert.
 If you want to insert a sequence file global variable with a
 custom data type 
 , you must first create a named data type.
 After you create the named data type, it appears in the Type submenu of the Insert File Global submenu.
 If you insert an array, the
 Array Bounds 
 dialog box launches.
- Cut 
 —Removes the selected sequence file global variable and places it on the clipboard.
- Copy 
 —Copies the selected sequence file global variable to the clipboard.
- Paste 
 —Inserts the sequence file global variable from the clipboard.
- Delete 
 —Deletes the sequence file global variable.
- Copy Value 
 —Copies the value of the selected property to the clipboard.
- Rename 
 —Edits the name of the selected global variable or subproperty.
- Advanced 
 —Launches a submenu that contains the following options:
  - Edit Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the global variable or subproperty.
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the global variable or subproperty.
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property. This control is available only for numeric properties and numeric array properties.
- Representation 
 —The numeric data type standard to use for a number variable or parameter.
  - Double Precision 64-bit Floating Point (default) 
 —Specifies double-precision, 64-bit floating-point representation.
  - Signed 64-bit Integer 
 —Specifies signed 64-bit integer representation.
  - Unsigned 64-bit Integer 
 —Specifies unsigned 64-bit integer representation.

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

[Variables Pane](variables-pane-sequence-file-tab.html)

Parent topic:

Variables Pane - Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-globals-context-menu-sequence-file-windo.html language=enus -->
## TOPIC 03715: File Globals Context Menu - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-globals-context-menu-sequence-file-windo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-globals-context-menu-sequence-file-windo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: File Globals Context Menu To access the context menu, right-click the FileGlobals item on the Variables pane. The items in the context menu vary depending on whether you right-click a global variable or global variable subproperty. The File Globals context menu can contain the following items: Inser

### File Globals Context Menu - Sequence File Window

#### File Globals Context Menu

To access the context menu, right-click the FileGlobals item on the
 [Variables](variables-pane-sequence-file-window4.html)
 pane. The items in the context menu vary depending on whether you right-click a global variable or global variable subproperty.

The File Globals context menu can contain the following items:

- Insert File Global 
 —A submenu from which you select the data type for the sequence file global variable you want to insert.
 If you want to insert a sequence file global variable with a
 custom data type 
 , you must first create a named data type. You can create a named data type in the
 Types 
 window. 
 After you create the named data type, it appears in the Type submenu of the Insert File Global submenu.
 If you insert an array, the
 Array Bounds 
 dialog box launches.
- Cut 
 —Removes the selected sequence file global variable and places it on the clipboard.
- Copy 
 —Copies the selected sequence file global variable to the clipboard.
- Paste 
 —Inserts the sequence file global variable from the clipboard.
- Delete 
 —Deletes the sequence file global variable.
- Copy Value 
 —Copies the value of the selected property to the clipboard.
- Rename 
 —Edits the name of the selected global variable or subproperty.
- Advanced 
 —Displays a submenu with the following items:
  - Edit Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the global variable or subproperty.
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the global variable or subproperty.
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property. This control is available only for numeric properties and numeric array properties.
- Representation 
 —The numeric data type standard to use for a number variable or parameter.
  - Double-Precision 64-bit Floating Point (default) 
 —Specifies double-precision, 64-bit floating-point representation.
  - Signed 64-bit Integer 
 —Specifies signed 64-bit integer representation.
  - Unsigned 64-bit Integer 
 —Specifies unsigned 64-bit integer representation.
- View 
 —Lists the available panes or windows for a sequence file. These commands are available only when a Sequence File window is active.
  - Steps 
 —Displays the
 Steps 
 pane where you edit the steps in the Setup, Main, and Cleanup step groups for the sequence file.
  - Sequences 
 —Displays the
 Sequences 
 pane where you edit the sequences in the sequence file.
  - Variables 
 —Displays the
 Variables 
 pane where you edit the locals, parameters, and file globals for the sequence file and station globals.
  - Types 
 —Displays the
 Types 
 window where you can edit step types, custom data types, and built-in data types. The
 TestStand Sequence Editor 
 selects the active sequence file in the Type Palettes window.

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

[Sequences Pane](sequences-pane-sequence-file-window.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Types Window](types-window.html)

[Variables Pane](variables-pane-sequence-file-window4.html)

Parent topic:

Variables Pane - Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-list-teststand-file-diff-and-merge-utili.html language=enus -->
## TOPIC 03716: File List - TestStand File Diff and Merge Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-list-teststand-file-diff-and-merge-utili.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-list-teststand-file-diff-and-merge-utili.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: File List The file list of the TestStand File Diff and Merge utility contains the following columns: File —Lists the files you are comparing. The background color associated with each file represents the color the Differences table uses when that file contains a difference. When comparing two files,

### File List - TestStand File Diff and Merge Utility

#### File List

The file list of the TestStand File Diff and Merge utility contains the following columns:

- File 
 —Lists the files you are comparing. The background color associated with each file represents the color the
 Differences table 
 uses when that file contains a difference. When comparing two files, you can click the
 Save Modified File 
 button to save a file. You can click the
 Select Files to Diff 
 button to specify a new file to compare in the Differences control. If a file you want to compare is locked, click the
 Unlock File 
 button to unlock the file. The tooltip displays the full file path when you hover the cursor over the File column.
- Changes 
 —The number of value changes in each file compared to the base file. When you compare two files against each other and you disable the When Diffing Two Files, Treat First File As The Base File option in the
 File Differ Options 
 dialog box, this value is the same for both files.
- Insertions 
 —The number of insertions in each file compared to the base file. When you compare two files against each other and you disable the When Diffing Two Files, Treat First File As The Base File option in the File Differ Options dialog box, the utility counts deletions in one file as insertions in the other file.
- Deletions 
 —The number of deletions in each file compared to the base file. When you compare two files against each other and you disable the When Diffing Two Files, Treat First File As The Base File option in the File Differ Options dialog box, this column is not available.
- Ignored Changes 
 —The number of ignored changes in each file compared to the base file. Ignored changes can include insertions, deletions, or value changes. When all
 Ignore Options 
 on the
 Filters Tab 
 are disabled, this column is not displayed.
- File Format Version 
 —Specifies the file format version of the property object file, typically the version of the TestStand Engine in which the sequence file is saved.

#### See Also

[Differences Table](differences-table-teststand-file-diff-and-mer.html)

[File Differ Options dialog box](file-differ-options-dialog-box.html)

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-menu-execution-profiler.html language=enus -->
## TOPIC 03717: File Menu - Execution Profiler

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-menu-execution-profiler.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-menu-execution-profiler.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: File Menu The File menu contains the following options. Open —Launches the Open Profile dialog box, in which you can load an existing profile file. Loading a profile discards any existing profile information and pauses the profiler data collection. If you resume the profile display to show new event

### File Menu - Execution Profiler

#### File Menu

The File menu contains the following options.

- Open 
 —Launches the Open Profile dialog box, in which you can load an existing profile file. Loading a profile discards any existing profile information and pauses the profiler data collection. If you resume the profile display to show new events after loading a file created in the past, the profiler shows the corresponding gap in absolute time between the loaded events and the new events. You can reposition events on the timeline with the
 Edit»Move Selected Operations 
 command.
 Note 
 If you restart TestStand after saving a profile file, the thread and execution IDs in the saved profile might not necessarily be distinct from the thread and execution IDs for new events.
- Merge 
 —Launches the Merge Profile dialog box, from which you can select a profile file to merge into memory with the current profile data. After you select a file, the profiler displays the Merge Profiling Data dialog box in which you can specify where on the timeline to place the loaded data and whether to mark the loaded operations with a selected color.
- Save 
 —Launches the Save Profile dialog box, in which you can save the recorded information to a file for viewing at a later time.
- Configure Data Collection 
 —Launches the
 Configure Data Collection 
 dialog box, in which you can select the information you want the profiler to collect. You can increase execution speed by reducing the amount of information the profiler collects.
- Exit 
 —Closes the profiler and discards all profile data.

Note

Parent topic:

Menus - Execution Profiler

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-menu.html language=enus -->
## TOPIC 03718: File Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The File menu in the TestStand Sequence Editor contains the following items, which are used for basic file operations, such as opening, closing, saving, and printing files: Login —Launches the Login dialog box and prompts you for a login name and password. When you click Cancel , TestStand gives you

### File Menu

The File menu in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 contains the following items, which are used for basic file operations, such as opening, closing, saving, and printing files:

- Login 
 —Launches the Login dialog box and prompts you for a login name and password. When you click
 Cancel 
 , TestStand gives you no privileges. Use the Login command to log in as a different user. Each user can have different
 privilege settings 
 , so logging in as a different user can change the privileges.
- Logout 
 —Logs out the current user and launches the Login dialog box.
- New 
 —Displays a submenu that contains the following options for creating a new file:
  - Sequence File 
 —Creates a new Sequence File window.
  - Workspace File 
 —Creates a new workspace and displays the
 Workspace 
 pane. Only one workspace can be open at a time. If a workspace is already open, TestStand closes it before creating a new workspace.
  - Analyzer Project 
 —Creates a new TestStand Sequence Analyzer project, which becomes the current sequence analyzer project, and opens the
 Current Sequence Analyzer Project 
 window. If an analyzer project is already open, TestStand closes it before creating the new project.
- Open File 
 —Opens existing TestStand files. Use this command to open sequence files, a workspace file, or a sequence analyzer project. When you select this option, the
 Open File 
 dialog box launches and prompts you to choose files to load into the sequence editor. You can select multiple sequence files but only one workspace file or analyzer project. If you open a workspace file and a workspace file is already open, TestStand closes it before opening a different workspace. If you choose an analyzer project and an analyzer project is already open, TestStand closes it before opening a different analyzer project.
- Close <
 filename
 > 
 —Closes the active window. When you select this option, TestStand might launch a dialog box that prompts you to save any changes before closing the window. If the
 Workspace 
 pane is active, you can leave the workspace file open in the Workspace pane so you can directly open a sequence file, or you can close the Workspace pane and use the options in the File menu to open a sequence file.
- Close Workspace File 
 —Closes the active workspace file. When you select this option, TestStand might launch a dialog box that prompts you to save any changes before closing the window. Click
 No 
 if TestStand prompts you to save the changes.
- Add <
 filename
 > to Workspace 
 —Adds the file associated with the active window to the workspace. When you select this menu option, TestStand launches a dialog box that prompts you to specify where to insert the file in the workspace.
- Save <
 filename
 > 
 —Writes the contents of the active window or pane to disk. You can save sequence files, type palette files, users, station global variables, or the current workspace.
- Save <
 filename
 > As 
 —Writes the contents of the active Sequence File window or current workspace in the Workspace pane to disk using a new name you enter. The title bar on the Sequence File window or the Workspace pane displays the new name.
 To save a sequence file using a file format from a previous version of TestStand, select
 File»Save <
 filename
 > As 
 and select the appropriate TestStand version option from the
 Files of Type 
 control. You can save sequence files as TestStand 4.0 or later. Saving a sequence file to a previous version of TestStand saves the new copy to a location that is different than the location of the most recent version of the sequence file. If you try to overwrite a sequence file you previously saved for a version of TestStand that is different than the one for which you are currently saving, TestStand prompts you to save a back-up copy.
 Note 
 If the sequence file contains step types not present in previous versions of TestStand, or if the sequence file uses TestStand features previous versions of TestStand do not support, the sequence file you save in that format will not function correctly. TestStand does not warn you if the file you save cannot load or run in a previous version of TestStand.
- Save All 
 —Saves all open files to disk, including sequence files, global variables, type palettes, users, the current workspace, the current sequence analyzer project, and configuration information.
- Unload All Modules 
 —Removes from memory all step
 code modules 
 , all code modules substeps call, and all sequence files not currently in a window. You can only use this command when there are no active executions. This command is useful when you want to rebuild a DLL after an execution but the DLL is loaded. The application development environment you use to build the DLL cannot write out the new contents of the DLL until TestStand unloads it.
 Note 
 The .NET Adapter cannot unload .NET code module assemblies when Microsoft Visual Studio is debugging managed code in the TestStand process.
 The ActiveX/COM Adapter cannot always unload DLL ActiveX Automation servers. When TestStand requests the operating system to unload the ActiveX server, the operating system ignores the request and keeps the ActiveX server in memory. You must exit the TestStand application to release the ActiveX DLL server.
- Most Recently Used Sequence Files 
 —Lists the most recently opened sequence files.
- Most Recently Used Workspace Files 
 —Lists the most recently opened workspace files.
- Exit 
 —Closes the current sequence editor session. If TestStand is running any executions, the sequence editor prompts you to terminate or abort them. If you have modified any open files since the last save, or if any windows contain unnamed files, the sequence editor prompts you to save them.

#### See Also

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[Open File dialog box](open-file-dialog-box.html)

[Workspace Pane](workspace-pane.html)

Parent topic:

Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-menu2.html language=enus -->
## TOPIC 03719: File Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-menu2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-menu2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The File menu in a TestStand User Interface contains the following options: Menu items marked with an asterisk ( * ) appear only in Editor Mode. Login —Launches the Login dialog box and prompts you for a login name and password. When you click Cancel , TestStand gives you no privileges. Use the Logi

### File Menu

TestStand User Interface

Note

*

- Login 
 —Launches the Login dialog box and prompts you for a login name and password. When you click
 Cancel 
 , TestStand gives you no privileges. Use the Login command to log in as a different user. Each user can have different
 privilege settings 
 , so logging in as a different user can change the privileges.
- Logout 
 —Logs out the current user.
- New Sequence File* 
 —Creates a new sequence file window.
- Open Sequence File 
 —Opens an existing sequence file. Use the
 Open File 
 dialog box to select a file to load.
- Close Sequence File/Close Execution 
 —Closes the selected sequence file or execution.
- Close All Sequence Files and Executions 
 —Closes all open files and executions. For any execution that is currently running, the user interface prompts you to select whether to terminate, abort, or automatically close the execution when it completes.
- Close Completed Executions 
 —Closes all open executions that have completed.
- Browse Workspace 
 —Launches the
 Workspace Browser 
 dialog box, in which you can load and unload workspaces, open sequence files that reside in a workspace, and perform source code control operations on files that reside in the workspace. You can open only one workspace file at a time. If a workspace file is already open, TestStand closes it before opening a new workspace.
- Save* 
 —Writes the contents of the active Sequence File window to disk.
- Save As* 
 —Writes the contents of the active Sequence File window to disk using a new name you enter.
- Save All* 
 —Saves all open files to disk, including sequence files, global variables, templates, and the workspace.
- Unload All Modules 
 —Removes from memory all step
 code modules 
 , all code modules substeps call, and all sequence files not currently open in the list bar control. You can only use this command when there are no active executions. This command is useful when you want to rebuild a DLL after an execution but the DLL is loaded in TestStand. The application development environment you use to build the DLL cannot write out the new contents of the DLL until TestStand unloads it.
 Note 
 The .NET Adapter cannot unload .NET code module assemblies when Microsoft Visual Studio is debugging managed code in the TestStand process.
 The ActiveX/COM Adapter cannot always unload DLL ActiveX Automation servers. When TestStand requests the operating system to unload the ActiveX server, the operating system ignores the request and keeps the ActiveX server in memory. You must exit the TestStand application to release the ActiveX DLL server.
- Most Recently Used Files 
 —Lists the most recently opened files.
- Exit 
 —Closes the user interface. Before exiting, the user interface closes all files and executions. For any execution that is currently running, the user interface prompts you to select whether to terminate, abort, or automatically close the execution when it completes. The user interface does not close until all executions are complete.

#### See Also

[Open File dialog box](open-file-dialog-box.html)

[Workspace Browser dialog box](workspace-browser-dialog-box.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-not-found-dialog-box.html language=enus -->
## TOPIC 03720: File Not Found Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-not-found-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-not-found-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the File Not Found dialog box when you specify a file in the Open File dialog box without selecting the Use Absolute Path option and that file cannot be found within the TestStand search paths . The File Not Found dialog box contains the following options: Add the directory contai

### File Not Found Dialog Box

TestStand launches the File Not Found dialog box when you specify a file in the
 [Open File](open-file-dialog-box.html)
 dialog box without selecting the Use Absolute Path option and that file cannot be found within the
 [TestStand search paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

The File Not Found dialog box contains the following options:

- Add the directory containing the file you selected to the list of search directories 
 —Adds the directory in which the file is located to a list of directories TestStand searches when the file is not found in the original location. Once you have added a specific directory as a search directory, if the file cannot be found in the directory you specified, TestStand searches the directories listed in the Search Directories list. You can specify whether to also search within subdirectories.
- Use an absolute path for the file you selected 
 —Uses the exact path of the file so the file is not searched for when it is needed. If you move the file after you select this option, the file will not be found. If you move the file, change the Module Pathname option in the Specify Module dialog box to reflect the new location.
- Use a relative path for the file you selected 
 —Indicates whether the current directory of the file is relative to a current search directory that has already been specified. TestStand uses a shortened path that the difference between the current path and the associated search directory path to find the file defines. When you enable this option, you can move the file to other directories that are relative to the search directories.
- Substitute Path Macros 
 —Enable this option to substitute the
 $(Platform)
 macro 
 for the last directory in a path that matches the current platform. For example, 64-bit TestStand replaces
 C:\bin\x64\module.dll 
 with
 C:\bin\$(Platform)\module.dll 
 . This option applies to absolute paths and to relative paths TestStand finds through non-recursive search directories. This option is not available for files TestStand finds by searching subdirectories.

#### See Also

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Open File dialog box](open-file-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-or-clipboard-data-location-legacy-import.html language=enus -->
## TOPIC 03721: File or Clipboard Data Location - Legacy Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-or-clipboard-data-location-legacy-import.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-or-clipboard-data-location-legacy-import.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: File or Clipboard Data Location The Import/Export Properties dialog box contains the following tabs when you select File or Clipboard in the Data Location ring control: Source/Destination Properties

### File or Clipboard Data Location - Legacy Import/Export Properties Dialog Box

#### File or Clipboard Data Location

The Import/Export Properties dialog box contains the following tabs when you select File or Clipboard in the Data Location ring control:

- Source/Destination
- Properties

Parent topic:

Legacy Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/file-tab-station-options-dialog-box.html language=enus -->
## TOPIC 03722: File Tab - Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/file-tab-station-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/file-tab-station-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: File Tab The File tab specifies options for TestStand files, types, and version numbers. The File tab contains the following options: Allow Automatic Type Conflict Resolution —Specifies when you want TestStand to automatically resolve type conflicts. TestStand normally resolves type conflicts when i

### File Tab - Station Options Dialog Box

#### File Tab

The File tab specifies options for TestStand files, types, and version numbers.

The File tab contains the following options:

- Allow Automatic Type Conflict Resolution 
 —Specifies when you want TestStand to automatically resolve type conflicts. TestStand normally resolves type conflicts when it loads a file with a version of a type that differs from the version of the type currently in memory and when you enable the
 Use the definition that has the highest version number 
 option on the
 Version 
 tab of the
 Type Properties 
 dialog box or on the
 Version 
 tab of the
 Step Type Properties 
 dialog box for both versions of the type. In this case, TestStand updates the file with the lower version of the type to use the higher version. 
 The Allow Automatic Type Conflict Resolution ring control contains the following options:
  - Always (same as TestStand 4.0.x or earlier) 
 —Always allows automatic type conflict resolution by using version numbers, which can cause unintended propagation of types between files. For example, if you open a sequence file with a version of a type later than the version of the type currently in a type palette file, TestStand updates the type palette file and every file you subsequently open to use the later version. The updated type propagates to other files without warning or notifying you.
  - Only if Type Palette Files will not be Modified (default) 
 —Disallows automatic type conflict resolution when the outcome of the resolution modifies a type palette file. This ensures that the application never uses a version of a type that is different than the version of the type in the type palette file without an explicit confirmation through the
 Type Conflict in File 
 dialog box.
  - Only if a Type Palette File has the Higher Version 
 —Further restricts automatic type conflict resolution. This option includes the same restrictions as the Only if Type Palette Files will not be Modified (default) option and includes the restriction that the type must be in a type palette file for automatic type conflict resolution to occur. Effectively, this option allows automatic type conflict resolution only in the case in which a type palette file has the later version of the type and a non-type palette file has the earlier version of the type.
 For example, this option does not allow automatic type conflict resolution between two sequence files for types that are not in type palette files. The Only if Type Palette Files will not be Modified (default) option does allow this.
  - Never 
 —Disallows all automatic type conflict resolution. When TestStand loads two different versions of a type, TestStand always prompts you or
 reports a type conflict error 
 . When you select this option, opening files from TestStand versions earlier than the current version almost always results in type conflict prompts. Use this option only for debugging purposes or to ensure that all files have exactly the same version of every type.
- Auto Increment Sequence File Version 
 —Automatically increments the specified portion of the sequence file version number when you save a sequence file that contains modifications.
  - Version Number to Increment 
 —Use this control to choose the portion of the number you want to increment. A version number consists of four numbers with separating periods. The numbers are named from left to right in the following order: Major, Minor, Revision, and Build.
- Before Saving Modified Types 
 —Specifies how the
 TestStand Sequence Editor 
 increments the version of types marked as modified before saving a file that contains the type. The following options are available in the ring control:
  - Auto Increment Type Versions 
 —Instructs TestStand to automatically increment the version of types.
    - Version Number to Increment 
 —Use this control to choose the portion of the number you want to increment. A version number consists of four numbers with separating periods. The numbers are named from left to right in the following order: Major, Minor, Revision, and Build.
  - Prompt to Increment Type Versions 
 —Instructs TestStand to launch the
 Modified Types Warning 
 dialog box.
  - Do Not Increment Type Versions 
 —Instructs TestStand to save the types without incrementing the version of types.
- Do Not Mark Files as Modified if Modification is Caused Only by Automatic TestStand Version Upgrade 
 —Specifies when TestStand marks files as modified. Enable this option when you do not want TestStand to mark files as modified when the only changes to the file are the result of the automatic conversions TestStand makes when you open files from an older version of TestStand in a newer version of TestStand. These automatic conversions occur when TestStand upgrades older versions of built-in, National Instruments-created types and step types and then resolves data format changes that exist between the versions.
 This option is disabled by default. When you enable this option, TestStand marks as modified only the files with user-defined changes so you can avoid resaving and revalidating files you did not directly modify. Enabling or disabling this option does not change how TestStand loads the file into memory or saves the file to disk.
 Note 
 This option applies only to National Instruments-created types, step types, and file modifications. Use this option to prevent TestStand from prompting to resave upgraded files, which might require revalidation. When you enable this setting, TestStand marks files as modified when type conflict resolution results in updates to user-defined types and step types in the file. Resave files in the version of TestStand you are using to optimize performance when opening files. 
 Regardless of the value of this option, opening files from a TestStand version older than the version you are using requires TestStand to perform an in-memory conversion. Resave files in the version of TestStand you are using to optimize file loading performance.
- Max Number of Backups Saved for Station Globals File on Startup 
 or
 Max Number of Backups Saved for Station Globals File When Saved 
 —Enter a non-zero value for one or both of these options to automatically save up to the specified number of backup files for the station global variables file at startup, on station globals file save, or both. If the most recent backup file is the same as the current file, TestStand does not create an additional backup file. Enter
 0 
 in one or both controls to disable the backup file option. TestStand creates the backup files in the TestStand <
 config 
 > directory, the same location as
 StationGlobals.ini 
 , and uses the file extension
 OnStartBackup# 
 or
 OnSaveBackup# 
 , where
 # 
 is the number between 1 and the value you specify, with 1 being the most recently saved backup file.
- File Format Options 
 —Launches the
 File Format Options 
 dialog box, in which you can specify the file format for new files, the station globals file, the users file, the templates file, and type palette files.

#### See Also

[File Format Options dialog box](file-format-options-dialog-box.html)

[Modified Types Warning dialog box](modified-types-warning-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

[Type Conflict in File dialog box](type-conflict-in-file-dialog-box.html)

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

Station Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/files-pane-current-sequence-analyzer-project.html language=enus -->
## TOPIC 03723: Files Pane - Current Sequence Analyzer Project Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/files-pane-current-sequence-analyzer-project.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/files-pane-current-sequence-analyzer-project.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Files Pane Use the Files pane to specify which files to analyze. The Files pane contains the following sections: Workspace File to Analyze —Path of the workspace file to analyze. The TestStand Sequence Analyzer analyzes all the sequence files in the workspace file. Use the Sequence Files to Analyze

### Files Pane - Current Sequence Analyzer Project Window

#### Files Pane

Use the Files pane to specify which files to analyze. The Files pane contains the following sections:

- Workspace File to Analyze 
 —Path of the workspace file to analyze. The
 TestStand Sequence Analyzer 
 analyzes all the sequence files in the workspace file. Use the Sequence Files to Analyze section to select individual sequence files to analyze. You can analyze only one workspace file at a time.
- Sequence Files to Analyze 
 —List of paths of sequence files to analyze in the order listed. You can drag and drop files to reorder them. The sequence analyzer ignores duplicate entries. When you use
 expressions 
 in
 Sequence Call steps 
 to call sequence files, you must add each file to the Sequence Files to Analyze section separately.
- Directories to Analyze 
 —List of directories to analyze. The sequence analyzer analyzes all the sequence files in each directory. Place a checkmark in the option in the
 Analyze Files in Subdirectories 
 column located to the right of the directory path to analyze all the sequence files in all subdirectories.
- TestStand Files to Analyze 
 —Additional files to analyze. This section contains the following options:
  - NI Type Palettes 
 —Enable this option to analyze the NI type palettes located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\TypePalettes 
 directory in the same order as they appear in the
 Types 
 window in the
 TestStand Sequence Editor 
 .
  - Public Type Palettes 
 —Enable this option to analyze the public type palettes located in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\TypePalettes 
 directory in the same order as they appear in the Types window in the sequence editor.
  - Station Globals 
 —Enable this option to analyze the
 StationGlobals.ini 
 file, located in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 directory.
  - Templates File 
 —Enable this option to analyze the
 Templates.ini 
 file, located in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 directory.
  - Users File 
 —Enable this option to analyze the
 Users.ini 
 file, located in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 directory.

#### See Also

[Sequence Call Step](sequence-call-step.html)

[Types Window](types-window.html)

Parent topic:

Current Sequence Analyzer Project Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/files-tab-teststand-sequence-analyzer-applica.html language=enus -->
## TOPIC 03724: Files Tab - TestStand Sequence Analyzer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/files-tab-teststand-sequence-analyzer-applica.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/files-tab-teststand-sequence-analyzer-applica.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Files Tab Use the Files tab to specify which files to analyze. The Files pane contains the following sections: Workspace File to Analyze —Path of the workspace file to analyze. The TestStand Sequence Analyzer analyzes all the sequence files in the workspace file. Use the Sequence Files to Analyze se

### Files Tab - TestStand Sequence Analyzer Application

#### Files Tab

Use the Files tab to specify which files to analyze. The Files pane contains the following sections:

- Workspace File to Analyze 
 —Path of the workspace file to analyze. The TestStand Sequence Analyzer analyzes all the sequence files in the workspace file. Use the Sequence Files to Analyze section to select individual sequence files to analyze. You can analyze only one workspace file at a time.
- Sequence Files to Analyze 
 —List of paths of sequence files to analyze in the order listed. You can drag and drop files to reorder them. The sequence analyzer ignores duplicate entries. When you use
 expressions 
 in
 Sequence Call steps 
 to call sequence files, you must add each file to the Sequence Files to Analyze section separately.
- Directories to Analyze 
 —List of directories to analyze. The sequence analyzer analyzes all the sequence files in each directory. Place a checkmark in the option in the
 Analyze Files in Subdirectories 
 column located to the right of the directory path to analyze all the sequence files in all subdirectories.
- TestStand Files to Analyze 
 —Additional files to analyze. This section contains the following options:
  - NI Type Palettes 
 —Enable this option to analyze the NI type palettes located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\TypePalettes 
 directory in the same order as they appear in the
 Types 
 window in the
 TestStand Sequence Editor 
 .
  - Public Type Palettes 
 —Enable this option to analyze the public type palettes located in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\TypePalettes 
 directory in the same order as they appear in the Types window in the sequence editor.
  - Station Globals 
 —Enable this option to analyze the
 StationGlobals.ini 
 file, located in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 directory.
  - Templates File 
 —Enable this option to analyze the
 Templates.ini 
 file, located in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 directory.
  - Users File 
 —Enable this option to analyze the
 Users.ini 
 file, located in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 directory.

#### See Also

[Sequence Call Step](sequence-call-step.html)

[Types Window](types-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/files-to-update-tab-update-vi-calls-dialog-bo.html language=enus -->
## TOPIC 03725: Files To Update Tab - Update VI Calls Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/files-to-update-tab-update-vi-calls-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/files-to-update-tab-update-vi-calls-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Files To Update Tab The Files To Update tab contains the following options: Files To Update —The files to update. Active Sequence File —Updates the active sequence file. This option is available only when a sequence file is active. All Sequence Files under Directory —Updates all the sequence files l

### Files To Update Tab - Update VI Calls Dialog Box

#### Files To Update Tab

The Files To Update tab contains the following options:

- Files To Update 
 —The files to update.
  - Active Sequence File 
 —Updates the active sequence file. This option is available only when a sequence file is active.
  - All Sequence Files under Directory 
 —Updates all the sequence files located in the directory you specify and any subdirectories.
  - Specific Sequence Files 
 —Updates all the sequence files listed in the list control. Use the
 Add Files 
 ,
 Remove 
 , and
 Remove All 
 options to edit the list of files to search.
  - All Sequence Files in Current Workspace 
 —Updates all the sequence files the currently open workspace contains. This option is available only when a workspace is open.
  - Ignore Locked Files 
 —Skips all locked files. TestStand sets this option by default.
- Type Of Calls To Update 
 —The type of VI/LabVIEW NXG VI calls to update.
  - Process Express VI Calls 
 —TestStand checks all LabVIEW step instances that call an Express VI. The ring control contains the following options:
    - Report Problems Only (No Changes Will Be Made) 
 —TestStand does not update sequence files, but instead lists suggested changes in the log report.
    - Reload Prototype If Modified 
 —If the Express VI has changed, TestStand recreates the Express VI instance using the active LabVIEW version in order to use the new prototype.
    - Force Prototype Reload 
 —TestStand always recreates the Express VI instance using the active LabVIEW version.
- Process Standard VI Calls 
 —TestStand checks all LabVIEW step instances that call a Standard VI. The ring control contains the following options:
  - Report Problems Only (No Changes Will Be Made) 
 —TestStand does not update the sequence files, but instead lists suggested changes in the log report.
  - Reload Prototype If Modified 
 —TestStand uses the new VI prototype if you have modified the VI since the prototype was last read.
  - Force Prototype Reload 
 —TestStand always reloads the prototype of the VI, even if the prototype has not changed since the prototype was last read.
  - Ignore VI Namespace 
 —TestStand will not use the VI namespace when finding the absolute path of a VI. When you enable this option, TestStand uses the same behavior to find a VI as in TestStand 2012 or earlier.
- Process LV NXG VI Calls 
 —TestStand checks all LabVIEW NXG step instances that call a LabVIEW NXG VI. The ring control contains the following options:
 
 Note 
 TestStand will skip read-only sequence files if you select the
 Reload Prototype If Modified
 or
 Force Prototype Reload
 options for Express, Standard VI or LabVIEW NXG VI calls.
  - Report Problems Only (No Changes Will Be Made) 
 —TestStand does not update the sequence files, but instead lists suggested changes in the log report.
  - Reload Prototype If Modified 
 —TestStand uses the new LabVIEW NXG VI prototype if you have modified the LabVIEW NXG VI since the prototype was last read.
  - Force Prototype Reload 
 —TestStand always reloads the prototype of the LabVIEW NXG VI, even if the prototype has not changed since the prototype was last read.
- Log Results 
 —The location of the log file and what information to log.
  - Destination 
 —The location of the log file. TestStand saves the log data the Status tab displays to this location. If you specify a file that already exists, TestStand overwrites the file.
  - Report Steps With Errors Only 
 —Logs only the step instances that fail to update or any other problem that prevents the step instance from executing.
  - Report Parameter Changes 
 —Logs the parameters TestStand adds or deletes if the VI/ LabVIEW NXG VI prototype changed. This option is available only when you set the Update Express VIs option or the Reload Prototype If Changed option.

The Files to Update tab also contains the following button:

- Passwords 
 —Launches the
 Configuration VI Passwords To Use 
 dialog box, in which you can specify the configuration VI passwords.
 Note 
 If none of the passwords can open a Configuration VI, the attempt to update the corresponding step will timeout, and TestStand will add a timeout message to the report.

Note

#### See Also

[Configuration VI Passwords To Use dialog box](configuration-vi-passwords-to-use-dialog-box.html)

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

Effectively Using LabVIEW NXG with TestStand

Parent topic:

Update VI/LV NXG VI Calls Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/filter-editor-dialog-box.html language=enus -->
## TOPIC 03726: Filter Editor Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/filter-editor-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/filter-editor-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select the Show Filter Editor option from the context menu of the grid view in a data grid to launch the Filter Editor dialog box, in which you can create custom filters, or logical expressions, to apply to the data. You can group multiple expressions together to form more complex expressions. Click

### Filter Editor Dialog Box

Select the
 Show Filter Editor
 option from the context menu of the grid view in a
 [data grid](data-grid.html)
 to launch the Filter Editor dialog box, in which you can create custom filters, or logical expressions, to apply to the data. You can group multiple expressions together to form more complex expressions. Click a value and select from a drop-down menu of available options to change the logical operator, the column name, and the condition.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/filter-expression-panel.html language=enus -->
## TOPIC 03727: Filter Expression Panel

- bundle_id: `teststand-api-reference`
- source_path: `tsref/filter-expression-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/filter-expression-panel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filter Expression Panel Setting any filtering condition in the data grid displays a Filter Expression panel at the bottom of the data grid view. The panel indicates the current filtering expression to apply to the data. Click Remove to remove the expression. Click Edit Filter to launch the Filter Ed

### Filter Expression Panel

#### Filter Expression Panel

Setting any filtering condition in the data grid displays a Filter Expression panel at the bottom of the data grid view. The panel indicates the current filtering expression to apply to the data. Click
 Remove
 to remove the expression. Click
 Edit Filter
 to launch the
 [Filter Editor](filter-editor-dialog-box.html)
 dialog box, in which you can modify the current filter expression. Click the expression itself to display a drop-down menu, in which you can select from a list of previously used filter expressions.

Parent topic:

Data Grid

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/filter-tab-find-replace-in-files-dialog-box.html language=enus -->
## TOPIC 03728: Filter Tab - Find/Replace in Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/filter-tab-find-replace-in-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/filter-tab-find-replace-in-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filter Tab The Filter tab contains the following options: Elements to Search —Use these controls to specify the parts of properties in which to search. Names —TestStand searches in the names of properties. Comments —TestStand searches in the comments of properties. Attributes —TestStand searches the

### Filter Tab - Find/Replace in Files Dialog Box

#### Filter Tab

The Filter tab contains the following options:

- Elements to Search 
 —Use these controls to specify the parts of properties in which to search.
  - Names 
 —TestStand searches in the names of properties.
  - Comments 
 —TestStand searches in the comments of properties.
  - Attributes 
 —TestStand searches the attributes of variables and properties and type attributes of type properties.
  - Type Names 
 —TestStand searches the type names of root type instance properties. Enable this option to find all of the instances of a particular type definition.
  - Values 
 —TestStand searches in the values of properties of the type you indicate by enabling one of the following options:
    - String 
 —Searches the string values of properties.
    - Number 
 —Searches the numeric values of properties. The numeric format of a property is taken into account when the
 TestStand Sequence Editor 
 performs the search. For example, if the numeric format of a property displays a number in hex as
 0xFA 
 , the search string must match the string
 "0xFA" 
 .
    - Boolean 
 —Searches Boolean values of properties. When the Boolean value of a property is
 True 
 , the search must match the string "
 True 
 ". When it is
 False 
 , the search string must match the string "
 False 
 ".
- Objects to Search 
 —Use the following controls to specify the kinds of properties in which to search:
  - Variables 
 —TestStand searches the sequence file variables of the type you indicate by enabling the following options:
    - Locals 
 —Searches the local variables of sequences.
    - Sequence Parameters 
 —Searches the parameters of sequences.
    - File Globals 
 —Searches the sequence file globals of sequences.
  - Steps 
 —TestStand searches steps and their subproperties as you indicate by enabling the following options:
    - Custom Properties 
 —Searches the custom properties of steps. These properties are those the step type for the step specifies. For example, the Numeric Limit Test step type specifies
 Limits.High 
 and
 Limits.Low 
 .
    - Module Properties 
 —Searches the module properties of steps. These properties are where the adapter stores the information about the
 code module 
 the step calls, such as the file path of the code module. Module properties are not visible in the sequence editor unless you enable the
 Show Hidden Properties 
 station option in the
 Station Options 
 dialog box.
    - Other Built-in Properties 
 —Searches other non-module, built-in properties of steps. These properties are where TestStand stores the standard step property information such as the pre, post, and status
 expressions 
 of a step. Like Module properties, these built-in properties are not visible in the sequence editor Variables pane unless you enable the
 Show Hidden Properties 
 station option in the
 Station Options 
 dialog box.
    - Adapter 
 —Select an adapter to limit the search to only steps that use the adapter.
  - Type Definitions 
 —TestStand searches type definitions and their subproperties as you indicate by enabling the following options:
    - Step Types 
 —Searches step types.
    - Custom Data Types 
 —Searches custom data types.
    - Standard Data Types 
 —Searches standard data types.
- Built-in Sequence and Sequence File Properties 
 —Searches built-in sequence and sequence file properties. These properties are where TestStand stores the sequence and sequence file settings you set using the
 Sequence Properties 
 dialog box and
 Sequence File Properties 
 dialog box in the sequence editor.
- Search Only Within Objects that have the Following Names 
 —Enter a comma-separated list of names in the text box beneath this option to limit the search to properties with the names you specify. The sequence editor also searches the subproperties of such properties. To specify a name that contains commas, surround the name with quotes as follows:
 "Name,With,Commas." 
 If the name contains quotes, surround the name with and escape the quotes in the name with a backslash (
 \ 
 ) character as follows:
 "Name\"With\"Quotes."
- Search Only Within Objects that are Instances of the Following Types 
 —Enter a comma-separated list of names in the text box beneath it to limit the search to objects that are instances of the types you specify by name. Click
 Select 
 to launch the
 Select Types 
 dialog box, in which you can select from all of the types currently loaded in memory or enter the names of the types you wish to specify directly in the text box. The types you specify can be any kind of type, such as step types, custom data types, or standard data types.
- Reset to Defaults 
 —Returns the settings on the Filter tab to their default states.

#### See Also

[Select Types dialog box](select-types-dialog-box.html)

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

Find/Replace in Files Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/filtering-tab-edit-legacy-property-loader-dia.html language=enus -->
## TOPIC 03729: Filtering Tab - Edit Legacy Property Loader Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/filtering-tab-edit-legacy-property-loader-dia.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/filtering-tab-edit-legacy-property-loader-dia.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filtering Tab Use the Filtering tab of the Edit Property Loader dialog box to filter the data the SQL statement returns so you load values only from rows that contain specific column values. The Filtering tab contains the following options when you select Database in the Data Location ring control:

### Filtering Tab - Edit Legacy Property Loader Dialog Box

#### Filtering Tab

Use the Filtering tab of the Edit Property Loader dialog box to filter the data the SQL statement returns so you load values only from rows that contain specific column values.

The Filtering tab contains the following options when you select Database in the Data Location ring control:

- Column List Source 
 —The name of the variable or property in which to store the list of column value comparisons. The variable or property must be a
 DatabaseColumnValue 
 array.
- Only Import Rows that Match the Specified Column Values 
 —When you enable this option, the step loads only the rows that match the specific column values. When you disable this control, the Column Values section is dimmed.
- Values 
 —The column values that each row must match. The Name/Number, Value, and Format String controls specify the settings for the currently selected mapping. Use
 New 
 ,
 Cut 
 ,
 Copy 
 , and
 Paste 
 to create a new item in the list, remove items from the list, and rearrange the items in the list.
  - Name/Number 
 —An expression TestStand evaluates at run time to determine the name of the column. To refer to a column by the order of the column in the SQL statement, specify an expression that returns a one-based number without surrounding quotes.
  - Value 
 —An expression TestStand evaluates at run time to determine the filter value of a column. Include the
 <FILE> 
 or
 <SEQUENCE> 
 tag within a value expression to instruct TestStand to automatically substitute the name of the sequence or file on which the step operates. To insert the
 <FILE> 
 or
 <SEQUENCE> 
 tag, select it from the drop-down list.
  - Format String 
 —Specifies how to
 convert a string value 
 when comparing a column value to a string expression. Typically, you use this control when comparing data from a column that is of the date-time or currency type.
- Create Columns 
 —Launches the
 Create Columns 
 dialog box, in which you can add new columns to a database table. TestStand automatically populates the dialog box with the list of any column names that you specify and that the SQL statement does not return.

Use the
 Expression Browse
 button to launch the
 [Expression Browser](expression-browser-dialog-box.html)
 dialog box for controls which contain TestStand
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 .

#### See Also

[Create Columns dialog box](create-columns-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Format Strings for Database Date Values](/csh?context=ts_tsfundamentals_strings_format)

Parent topic:

Edit Legacy Property Loader Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/filters-tab-teststand-file-diff-and-merge-uti.html language=enus -->
## TOPIC 03730: Filters Tab - TestStand File Diff and Merge Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/filters-tab-teststand-file-diff-and-merge-uti.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/filters-tab-teststand-file-diff-and-merge-uti.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters Tab You can use the Filters tab of the TestStand File Diff and Merge utility to hide properties with ignored differences or no differences in the Differences table . The Filters tab contains the following options: All —Hides all items with ignored differences or no differences. When you enab

### Filters Tab - TestStand File Diff and Merge Utility

#### Filters Tab

You can use the Filters tab of the TestStand File Diff and Merge utility to hide properties with ignored differences or no differences in the
 [Differences table](differences-table-teststand-file-diff-and-mer.html)
 . The Filters tab contains the following options:

- All 
 —Hides all items with ignored differences or no differences. When you enable this option, the Step Properties and Element options are disabled.
- Step Properties 
 —Hides all the properties under a step with ignored differences or no differences.
- Element 
 —Hides all the elements of a property with ignored differences or no differences.
- Condense Nested Differences 
 —Hides the subelements of a property that have ignored differences or no differences and shows only the subproperty that does have a difference. When a property condenses, the parent item of the property replaces the property in the Differences table with the only subelement of the property that has a difference. The utility replaces the name of the subelement in the Differences table with a lookup string, such as
 Locals.Container.Number 
 , that represents the path from the parent element of the property to the only subelement of the property that has a difference.
- Ignore Options 
 —Options to ignore types of differences. The utility treats ignored differences as a separate difference type with its own difference count. Ignored differences do appear in the Differences table; however, the navigation shortcut buttons skip ignored differences. The filter options to hide or condense will remove any ignored differences from the Differences table.
  - Variables with Shared Flag 
 —Ignores differences in variables in the File Globals, Sequence Locals, and Sequence Parameters subtrees when they have either the Shared or Shared at Runtime flag enabled.
    - Auto Resolve Ignored Conflicts 
 —Automatically resolves any conflicts that result from ignoring variables with the Shared flag. This option is available only when you are comparing three files and the Variables with Shared Flag option is enabled.
  - Minor Module Differences 
 —Ignores minor differences in the module properties of a step. The list of properties ignored is Connector Pane Checksum, VI Description, Connector Number, DefaultArraySize, and a LabVIEWIOControl’s SessionNumber when the DeviceName is set for both LabVIEW and LabVIEW NXG modules.
    - Auto Resolve Ignored Conflicts 
 —Automatically resolves any conflicts that result from ignoring minor module differences. This option is available only when you are comparing three files and the Minor Module Differences option is enabled.

Click the
 Apply
 button to apply the filter options you select.

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/find-panel.html language=enus -->
## TOPIC 03731: Find Panel

- bundle_id: `teststand-api-reference`
- source_path: `tsref/find-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/find-panel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find Panel The Database Viewer searches for any value you enter in the Find Panel in all database records. The data grid view displays only those records for which a match is found.

### Find Panel

#### Find Panel

The Database Viewer searches for any value you enter in the Find Panel in all database records. The data grid view displays only those records for which a match is found.

Parent topic:

Data Grid

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/find-replace-dialog-box.html language=enus -->
## TOPIC 03732: Find/Replace Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/find-replace-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/find-replace-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit»Find/Replace or press <Ctrl-F> to launch the Find/Replace dialog box and begin a search. Use the Find/Replace feature of the sequence editor to search sequence files, type palette files, users, station globals, and the context of an execution. The sequence editor performs the search in t

### Find/Replace Dialog Box

Select
 Edit»Find/Replace
 or press <Ctrl-F> to launch the Find/Replace dialog box and begin a search.

Use the Find/Replace feature of the sequence editor to search sequence files, type palette files, users, station globals, and the context of an execution. The sequence editor performs the search in the background and displays the results in the Find Results 1 or Find Results 2 pane of the sequence editor. Use the
 [Find Results](find-results-pane.html)
 pane to perform replace operations and to display the variable or property in a pane or dialog box.

The Find/Replace dialog box contains the following options:

- Find 
 —The string or regular expression to search for. When the Regular Expression option is enabled, you can specify a regular expression. This control contains a ring control in which you can select a previously used string.
  - Match Case 
 —Specifies whether the matching of characters is case-sensitive or case-insensitive. For example, if
 CHR 
 is the specified text and you enable the Match Case option, TestStand finds
 CHR 
 but not
 Chr 
 .
  - Match Whole Word Only 
 —Finds the specified text only when the characters surrounding it are spaces, punctuation marks, or other characters not considered parts of a word. TestStand treats the following characters as part of a word:
 A 
 through
 Z 
 ,
 a 
 through
 z 
 ,
 0 
 through
 9 
 , and the underscore (
 _ 
 ).
  - Regular Expression 
 —If you enable this option, TestStand treats certain characters in the Find text box as
 regular expression characters 
 instead of literal characters.
- Elements to Search 
 —Use the following controls to specify the parts of variables and properties in which to search:
  - Names 
 —TestStand searches in the names of variables and properties.
  - Comments 
 —TestStand searches in the comments of variables and properties.
  - Attributes 
 —TestStand searches the attributes of variables and properties and type attributes of type properties.
  - Type Names 
 —TestStand searches the type names of root type instance properties. Enable this option to find all of the instances of a particular type definition.
  - Values 
 —TestStand searches in the values of variables and properties of the type you indicate by enabling one of the following options:
    - String 
 —Searches the string values of variables and properties.
    - Number 
 —Searches the numeric values of variables and properties. The numeric format of a variable or property is taken into account when the sequence editor performs the search. For example, if the numeric format of a property displays a number in hex as
 0xFA 
 , the search string must match the string
 "0xFA" 
 and "FA", but not
 "250" 
 .
    - Boolean 
 —Searches Boolean values of variables and properties. When the Boolean value of a property is
 True 
 , the search must match the string "
 True 
 ". When the Boolean value is
 False 
 , the search string must match the string "
 False 
 ".
- Limit Search to 
 —Limits the search to a particular view you select in the current document.
- Display in Find Results 2 
 —TestStand displays the results of the search in the Find Results 2 pane of the sequence editor.

#### See Also

[Find Results Pane](find-results-pane.html)

[Regular Expressions](regular-expressions.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/find-replace-in-files-dialog-box.html language=enus -->
## TOPIC 03733: Find/Replace in Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/find-replace-in-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/find-replace-in-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit»Find/Replace In Files or click on the Environment toolbar to launch the Find/Replace in Files dialog box and begin a search. Use the Find/Replace in Files feature of the TestStand Sequence Editor to search one or more sequence files, type palette files, users, and station globals. The se

### Find/Replace in Files Dialog Box

Select
 Edit»Find/Replace In Files
 or click
 [IMAGE alt='image' src='../images/FindRep.gif']
 on the
 [Environment toolbar](toolbar-buttons-and-shortcuts.html)
 to launch the Find/Replace in Files dialog box and begin a search.

Use the Find/Replace in Files feature of the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to search one or more sequence files, type palette files, users, and station globals. The sequence editor performs the search in the background and displays the results in the Find Results 1 or Find Results 2 pane of the sequence editor. When TestStand searches unopened files on disk, the sequence editor closes the files after searching each file. Use the
 [Find Results](find-results-pane.html)
 pane to perform replace operations and to display the variable or property in a pane or dialog box. When you perform a replace operation on an unopened file, TestStand opens the file in the sequence editor but does not automatically save the change.

The Find/Replace in Files dialog box contains the following tabs:

- Search For 
 —The string to search for and the files to search.
- Filter 
 —The filtering options to apply to limit objects within the files to search.

#### See Also

[Find Results Pane](find-results-pane.html)

[Environment Toolbar](toolbar-buttons-and-shortcuts.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/find-results-pane.html language=enus -->
## TOPIC 03734: Find Results Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/find-results-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/find-results-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TestStand Sequence Editor displays the Find Results pane after you initiate a Find or Find in Files operation. Select Edit»Find/Replace or Edit»Find/Replace in Files or use the corresponding toolbar buttons to initiate a find operation. While the search executes in the background, the sequence e

### Find Results Pane

The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 displays the Find Results pane after you initiate a Find or Find in Files operation. Select
 Edit»Find/Replace
 or
 Edit»Find/Replace in Files
 or use the corresponding toolbar buttons to initiate a find operation.

While the search executes in the background, the sequence editor adds matches to the pane as soon as they are found. Cancel the search at any time by clicking the
 Stop
 button, which is located at the bottom left of the pane.

#### Match List View and Matched Text

The two main views of the Find Results pane are the Match List view at the top of the pane and the Matched Text view below it. The Match List view shows a separate list entry for each match TestStand finds. The Matched Text view shows the exact location of the match in the string for the entry you select in the Match List view. In the Match List view you can use the up and down arrow keys to navigate to the previous and next match in the view.

#### Match List View Columns

The Match List view contains the following columns:

- File 
 —The filename and full path of the file that contains the match for the Find in Files operation.
- Location 
 —The lookup string that shows the location of the property that contains the match. When this column displays a type icon, the match is within a type. When this column does not display an icon, the match is within the data property of the file.
- Value 
 —The value of the property that contains the match. However, this does not mean the match was inside the value of the property. This column is always shown, even if the match was within the name or the comment.
- Found In 
 —Describes the part of the property that contains the match. This column displays Value, Name, or Comment to indicate in which of those locations the match exists.

You can select one or more matches in the Match List view using the keyboard or mouse. You can also select
 Edit»Select All
 to select all of the matches in a view. You can also copy the results to the clipboard.

#### Match List View Context Menu

The Match List view context menu contains the following items:

- Goto Location in File 
 —Opens the file that contains the selected match and goes to the property that contains the match in the document window of the file and opens a dialog box, in which you can edit the value if possible. You can also perform this operation by double-clicking a match entry in the list view.
- Find Previous 
 —Selects the previous match and goes to the location it specifies. Use the <Ctrl+Shift+G>
 keyboard shortcut 
 for this command for increased efficiency when reviewing matches. The shortcut locates the match as long as the Find Results pane is open, regardless of whether the pane is active.
- Find Next 
 —Selects the next match and goes to the location it specifies. Use the <Ctrl+G> keyboard shortcut with this command for increased efficiency when reviewing matches. The shortcut locates the match as long as the Find Results pane is open, regardless of whether the pane is active.
- Show Name for Indices 
 —Toggles to show the names instead of the indexes for those array elements that have names.

#### Additional Controls on the Find Results Pane

The Find Results pane also contains the following options:

- Stop 
 —Cancels a search currently in progress.
- Replace With 
 ,
 Replace Found Text 
 ,
 Skip to Next 
 and
 Replace Value 
 —Use the Replace With control to specify a string to replace the matched text or value with and then click
 Replace Found Text 
 or the
 Replace Value 
 button to perform a Replace operation on all of the currently selected matches in the Match List view. Click the
 Skip to Next 
 button to move the selection to the next match. Select
 Edit»Select All 
 to select all of the matches.
- Apply Replacements in Types to Type Instances 
 —Enable this option when you want the Replace operation to update all instances of a type when a Replace is done on the value of a type property. Normally, changes to the value of a type property do not affect existing instances of a type.

#### See Also

[Edit Menu](edit-menu.html)

Parent topic:

Panes

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/flow-control-step-types.html language=enus -->
## TOPIC 03735: Flow Control Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/flow-control-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/flow-control-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand provides several step types to implement common programming constructs. TestStand includes the following Flow Control step types: If Else Else If For For Each While Do While Break Continue Select Case Goto End The Steps pane automatically inserts steps that complete the flow control block,

### Flow Control Step Types

TestStand provides several step types to implement common programming constructs. TestStand includes the following Flow Control step types:

- If
- Else
- Else If
- For
- For Each
- While
- Do While
- Break
- Continue
- Select
- Case
- Goto
- End

The Steps pane automatically inserts steps that complete the flow control block, such as inserting a Case and End step when you insert a Select step. The Steps pane also indents flow control blocks and highlights errors in flow control.

To edit a Flow Control step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , use the tabs on the
 [Step Settings](step-settings-pane.html)
 pane. The tabs available update based on the type of step you select.

To edit a Flow Control step type when you use a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select
 Edit
 from the context menu for the step or click
 Configure
 <Step Name>
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Using Flow Control Steps to Control Sequence Flow (Example)](/csh?context=ts_8180)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/flush-operation-queue-settings-edit-tab.html language=enus -->
## TOPIC 03736: Flush Operation - Queue Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/flush-operation-queue-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/flush-operation-queue-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Flush Operation Use the Flush operation to empty the queue and optionally retrieve all the elements from the queue. Enable the Flush option on the left of the Queue Settings panel. The Flush operation contains the following options: Queue Name or Reference Expression —The queue on which to perform t

### Flush Operation - Queue Settings Edit Tab

#### Flush Operation

Use the Flush operation to empty the queue and optionally retrieve all the elements from the queue. Enable the
 Flush
 option on the left of the Queue Settings panel.

The Flush operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option.
- Location to Store Array of Queue Elements (optional output) 
 —An array property in which to store the elements of the queue. All queue elements must be of the same data type as the array you specify and no queue element can be an array. The step reports a run-time error if you specify a value in this control and the queue items do not meet these conditions.

Parent topic:

Queue Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/flush-operation-queue-step-configuration-dial.html language=enus -->
## TOPIC 03737: Flush Operation - Queue Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/flush-operation-queue-step-configuration-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/flush-operation-queue-step-configuration-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Flush Operation Use the Flush operation to empty the queue and optionally retrieve all the elements from the queue. The Flush operation contains the following options: Queue Name or Reference Expression —The queue on which to perform the operation. You can specify the queue by name or by the object

### Flush Operation - Queue Step Configuration Dialog Box

#### Flush Operation

Use the Flush operation to empty the queue and optionally retrieve all the elements from the queue.

The Flush operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option.
- Location to Store Array of Queue Elements (optional output) 
 —An array property in which to store the elements of the queue. All queue elements must be of the same data type as the array you specify and no queue element can be an array. The step reports a run-time error if you specify a value in this control and the queue items do not meet these conditions.

Parent topic:

Queue Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/fonts-and-colors-tab-configuration-properties.html language=enus -->
## TOPIC 03738: Fonts and Colors Tab - Configuration Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/fonts-and-colors-tab-configuration-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/fonts-and-colors-tab-configuration-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fonts and Colors Tab The Fonts and Colors tab contains the following options: Colors —The default colors for the control. Step Comments —The color of step comments. Step Names —The color of step names. Background —The background color. Lines —The color of the lines, if you enabled the Horizontal or

### Fonts and Colors Tab - Configuration Properties Dialog Box

#### Fonts and Colors Tab

The Fonts and Colors tab contains the following options:

- Colors 
 —The default colors for the control.
  - Step Comments 
 —The color of step comments.
  - Step Names 
 —The color of step names.
  - Background 
 —The background color.
  - Lines 
 —The color of the lines, if you enabled the Horizontal or Vertical Grid Lines option on the
 Appearance 
 tab of the
 Configuration Properties 
 dialog box.
- Color Expressions 
 —Use these
 expressions 
 to customize the colors of a step at run time.
  - Step Text Color 
 —An expression that returns a
 number 
 . The number you specify is used at run time to paint the text. If an expression returns
 -1 
 , the default color specified in the Step Names option is used.
  - Step Background Color 
 —An expression that returns a
 number 
 . The number you specify is used at run time to paint the background of the
 Steps 
 pane. If an expression returns
 -1 
 , the default color specified in the Background option is used.
- Fonts 
 —Specifies different fonts for different portions of the Steps pane.
  - Font for the Item 
 —The item on the Steps pane for which you are changing the font.
    - Text 
 —The font used for text.
    - Comments 
 —The font used for comments.
    - Header 
 —The font used for the column header.
  - Font to Use 
 —The system font to use for the item you select in the Font for the Item control. If you select Use Custom Font for Font to Use, the Custom Font control specifies the font to use.
  - Custom Font 
 —The custom font specified for the item you select in the Font for the Item control. Click
 Change 
 to launch the Font dialog box. The Custom Font option is available only when you select Use Custom Font in the Font to Use control.
 Note 
 The Font dialog box includes a Script ring-control. If you change the system language or apply your font selection on a computer with a different language setting, some of the characters in that language might not display in the font you select if the language uses a different script.

#### See Also

[Color](../tsapiref/color.html)

[Configuration Properties dialog box](configuration-properties-dialog-box.html)

[Steps Pane](steps-pane-sequence-file-window.html)

Parent topic:

Configuration Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/for-each-step.html language=enus -->
## TOPIC 03739: For Each Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/for-each-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/for-each-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a For Each step to define a block of steps that execute once for each element in an array. Configuring the Step Use the ForEach Loop edit tab in the TestStand Sequence Editor and the Configure For Each Loop dialog box in a TestStand User Interface to configure the For Each step. Step Properties

### For Each Step

Use a For Each step to define a block of steps that execute once for each element in an array.

#### Configuring the Step

Use the
 [ForEach Loop](/csh?context=ts_9200)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure For Each Loop](configure-for-each-loop-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the For Each step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the For Each step type defines the following step properties:

- Step.ArrayExpr 
 —The expression that determines the array over which the loop iterates.
- Step.ArrayElementExpr 
 —The expression that determines the variable into which to store the current element of the array during each iteration of the loop.
- Step.OffsetExpr 
 —The expression that determines the variable into which to store the current offset of the array during each iteration of the loop.
- Step.SubscriptExpr 
 —The expression that determines the variable into which to store the subscript of the current element in the array during each iteration of the loop.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/for-loop-edit-tab.html language=enus -->
## TOPIC 03740: For Loop Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/for-loop-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/for-loop-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the For Loop edit tab in the TestStand Sequence Editor to configure the For step. The For Loop edit tab contains the following options: Fixed Number of Iterations —Specifies if the steps within the For block execute repeatedly for a fixed number of loops. Number of Loops —The numeric expression

### For Loop Edit Tab

Use the For Loop edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the For step.

The For Loop edit tab contains the following options:

- Fixed Number of Iterations 
 —Specifies if the steps within the For block execute repeatedly for a fixed number of loops.
  - Number of Loops 
 —The numeric expression that determines the number of iterations for the For block.
  - Loop Variable 
 —The numeric expression that determines the variable or property into which to store the current iteration number for the For block.
- Custom Loop 
 —A custom looping behavior for the steps within the For block.
  - Initialization 
 —The expression the step evaluates before executing the steps within the block for the first time.
  - Condition 
 —The expression the step evaluates each time before executing the steps within the block. If the expression evaluates to
 True 
 , execution proceeds to the first step in the block. If the expression evaluates to
 False 
 , execution proceeds to the End step for the For block.
  - Increment 
 —The expression the step evaluates after each execution of the steps within the block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

For Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/for-module-tabs-parameters-table-context-menu.html language=enus -->
## TOPIC 03741: For Module Tabs - Parameters Table Context Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/for-module-tabs-parameters-table-context-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/for-module-tabs-parameters-table-context-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an item in the Parameters Table on a Module tab of the Step Settings pane in the TestStand Sequence Editor to launch the Parameters Table context menu, which contains the following items: Advanced Logging —Displays the Additional Results panel of the Properties tab of the Step Settings p

### For Module Tabs - Parameters Table Context Menu

Right-click an item in the Parameters Table on a
 [Module](specify-module-tabs-and-dialog-boxes.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to launch the Parameters Table context menu, which contains the following items:

- Advanced Logging 
 —Displays the
 Additional Results panel 
 of the
 Properties 
 tab of the Step Settings pane. Use the Additional Results panel to configure more settings for parameter additional results.
- Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the parameter.

#### See Also

[ActiveX/COM Module Tab](activex-com-module-tab.html)

[C/C++ DLL Module Tab](c-c-dll-module-tab.html)

[LabVIEW Module Tab](labview-module-tab.html)

[LabWindows/CVI Module Tab](labwindows-cvi-module-tab.html)

[.NET Module Tab](net-module-tab.html)

[Sequence Call Module Tab](sequence-call-module-tab.html)

[Specify Module Tabs and Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/for-specify-module-dialog-boxes-parameters-ta.html language=enus -->
## TOPIC 03742: For Specify Module Dialog Boxes - Parameters Table Context Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/for-specify-module-dialog-boxes-parameters-ta.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/for-specify-module-dialog-boxes-parameters-ta.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an item in the Parameters Table in a Specify Module dialog box in a TestStand User Interface to launch the Parameters Table context menu, which contains the following items: Advanced Logging —Launches the Additional Results dialog box, in which you can configure additional more settings

### For Specify Module Dialog Boxes - Parameters Table Context Menu

Right-click an item in the Parameters Table in a
 [Specify Module](specify-module-tabs-and-dialog-boxes.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to launch the Parameters Table context menu, which contains the following items:

- Advanced Logging 
 —Launches the
 Additional Results 
 dialog box, in which you can configure additional more settings for parameter additional results. You cannot edit the custom additional results in the Additional Results dialog box.
- Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the parameter.

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Edit ActiveX/COM Call dialog box](edit-activex-com-call-dialog-box.html)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[Edit Sequence Call dialog box](edit-sequence-call-dialog-box.html)

[Module Tab - Edit C/C++ DLL Call dialog box](module-tab-edit-c-c-dll-call-dialog-box.html)

[Module Tab - Edit LabWindows/CVI Module Call dialog box](module-tab-edit-labwindows-cvi-module-call-di.html)

[Module Tab - Edit .NET Call dialog box](module-tab-edit-net-call-dialog-box.html)

[Specify Module Tabs and Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/for-step.html language=enus -->
## TOPIC 03743: For Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/for-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/for-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a For step to define a block of steps that execute repeatedly for a number of iterations. Configuring the Step Use the For Loop edit tab in the TestStand Sequence Editor and the Configure For Loop dialog box in a TestStand User Interface to configure the For step. Step Properties In addition to

### For Step

Use a For step to define a block of steps that execute repeatedly for a number of iterations.

#### Configuring the Step

Use the
 [For Loop](for-loop-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure For Loop](configure-for-loop-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the For step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the For step type defines the following step properties:

- Step.InitializationExpr 
 —The expression the step evaluates before executing the steps within the block the first time. The expression typically initializes a count variable.
- Step.ConditionExpr 
 —The expression that must evaluate to
 True 
 for the steps within the For block to execute.
- Step.IncrementExpr 
 —The expression the step evaluates after each execution of the steps within the block. The expression typically increments a count variable.
- Step.CustomLoop 
 —The step uses custom
 expressions 
 to define the looping behavior for the steps within the For block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/foreach-loop-edit-tab.html language=enus -->
## TOPIC 03744: ForEach Loop Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/foreach-loop-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/foreach-loop-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the ForEach Loop edit tab in the TestStand Sequence Editor to configure the ForEach step. The ForEach Loop edit tab contains the following options: Array/InputRecordStream to Interate Over —The expression that determines the array or InputRecordStream over which the loop iterates. The steps with

### ForEach Loop Edit Tab

Use the ForEach Loop edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the ForEach step.

The ForEach Loop edit tab contains the following options:

- Array/InputRecordStream to Interate Over 
 —The expression that determines the array or InputRecordStream over which the loop iterates. The steps within the block execute once for each element in the array or stream. Choose whether to iterate over an array or a stream by selecting the appropriate option from the
 Iterate Over Array / Iterate Over Stream 
 dropdown.
- Loop Variables (Optional) 
 —
 Expressions 
 that determine the location to store information about the current loop interation.
  - Current Element 
 —An expression that determines the variable or property in which to reference the current element in the array or to store the next record from the InputRecordStream during each iteration of the loop.
    - Interating Over Arrays 
 —The location the expression specifies must be of the same type as the element type for the
 Array to Iterate Over 
 option. Typically, you specify a local variable so the steps in the block can read or modify the current array element by referring to the local variable. The current element reference is valid only while the loop executes, and the reference resets after the loop completes. If the loop prematurely exits, the current element references the array element of the exiting iteration.
    - Interating Over Streams 
 — Current Element must refer to a container or array. Each iteration of the loop updates the value of the Current Element.
  - Current Offset 
 —An expression that determines the numeric variable or property into which to store current offset during each iteration of the loop. For zero-based one-dimensional arrays, the offset is equal to the index of the array. For multi-dimensional arrays, the offset is the linearized index of the array. For streams, the offset is a zero-based counter of the number of loop iterations.
  - Current Subscript 
 —An expression that determines the string variable or property into which to store the subscript of the current element in the
 Array to Iterate Over 
 option. Examples of the subscripts include [23] and [1][3]. Current Subscript is disabled when
 Iterate Over Stream 
 is selected.
- Interate Over Array/Interate Over Stream 
 —Specifies if this For Each loop iterates over an array or an InputRecordStream.
- Stream Options 
 —Settings that specify options specific to iterating over streams. These settings are hidden if
 Iterate Over Array 
 is selected.
  - Field Mapping (Optional) 
 —Specifies which container subproperties or array elements of the Current Element to store fields from the InputRecordStream to.
  - Auto Close at End of File 
 —Check this box to automatically clean up the InputRecordstream being read at the end of the loop. When this box is checked, upon terminating the loop, the For Each step closes the stream and sets the object reference in the
 InputRecordStream to Iterate Over 
 expression to Nothing.
 Note 
 Automatic cleanup only occurs if the loop terminates normally by encountering end of file (EOF). Cleanup does not occur if execution flow exits the loop for some other reason, for example via a Goto step.

Parent topic:

For Each Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/format-strings-for-database-date-values.html language=enus -->
## TOPIC 03745: Format Strings for Database Date Values

- bundle_id: `teststand-api-reference`
- source_path: `tsref/format-strings-for-database-date-values.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/format-strings-for-database-date-values.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Format control on the Column/Parameter section of the Database Options dialog box and the Format String control on the Column/Parameter Values tab of the Edit Data Operation dialog box support the following format strings when reading date values from a database and writing date values to a data

### Format Strings for Database Date Values

The Format control on the
 
 [Column/Parameter](schemas-tab-database-options-dialog-box2.html)
 section of the
 
 [Database Options](database-options-dialog-box.html)
 dialog box and the Format String control on the
 
 [Column/Parameter Values tab](column-parameter-values-tab-edit-data-operati.html)
 of the
 
 [Edit Data Operation](edit-data-operation-dialog-box.html)
 dialog box support the following format strings when reading date values from a database and writing date values to a database. A format string consists of symbols that describe how to convert a date value read from a database to a string value, or how to interpret a string value when writing a date value to a database.

| Format String | Value | Formatted Value |
| --- | --- | --- |
| Symbol | Description | Example Output |
| mm/dd/yy | Oct 20, 2010 | 10/20/10 |
| dd.mm.yy | Oct 20, 2010 | 20.10.10 |
| 'Jane Doe, born' Mmmm d, yyyy | Oct 20, 2010 | Jane Doe, born October 20, 2010 |
| hh:mm:ss | 3:47:42 PM | 15:47:42 |
| hh:mm:ss AM/PM | 3:47:42 PM | 03:47:42 PM |
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
| GD | General format for dates is the Short Date Format in the Regional Options section of the Microsoft Windows Control Panel. Note Do not combine other format symbols with GD except [US] . | — |
| GDT | General format for dates with times. The Time Format control in the Regional Options section of the Windows Control Panel is appended to the Short Date Style. This is the default when no format string is given. Note Do not combine other format symbols with GDT except [US] . | — |
| GL | General long format for dates. The Long Date Style control in the Regional Options section of the Windows Control Panel. Note Do not combine other format symbols with GL except [US] . | — |
| GLT | General long format for dates with times. The Time Style control in the Regional Options section of the Windows Control Panel is appended to the Long Date Format. Note Do not combine other format symbols with GLT except [US] . | — |
| GT | General format for time. The Time Style control in the Regional Options section of the Windows Control Panel. Note Do not combine other format symbols with GT except [US] . | — |
| [US] | Combine with GD , GDT , GL , GLT , or GT to override the Regional Options section of the Windows Control Panel and use the United States defaults instead. | — |

#### See Also

[Database Options dialog box](database-options-dialog-box.html)

[Edit Data Operation dialog box](edit-data-operation-dialog-box.html)

Parent topic:

Schemas Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/ftp-files-edit-tab.html language=enus -->
## TOPIC 03746: FTP Files Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/ftp-files-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/ftp-files-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FTP Files edit tab in the TestStand Sequence Editor to specify what files to download to or upload from a remote system. The FTP Files edit tab contains the following options: Remote System —Contains the following options: Hostname —The remote computer. Specify Remote Host by Expression —Ena

### FTP Files Edit Tab

Use the FTP Files edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify what files to download to or upload from a remote system.

The FTP Files edit tab contains the following options:

- Remote System 
 —Contains the following options:
  - Hostname 
 —The remote computer.
  - Specify Remote Host by Expression 
 —Enable this option to specify that the Hostname control contains an expression the step evaluates at run time to determine the name of the remote host.
  - FTP Username 
 —The user name to use to log into the FTP server on the remote system.
  - FTP Password 
 —The password to use to log into the FTP server on the remote system.
- Files to FTP 
 —Lists the files to download or upload. Click
 Add file to FTP 
 to add a new file to the list. Click
 Remove file to FTP 
 to remove the selected file from the list. Use the
 Copy and Paste file to FTP 
 button to duplicate the selected file in the list. To modify an entry, select the entry and use the following controls:
  - Direction 
 —Specifies whether to download or upload the file.
  - Overwrite 
 —When you enable this option, TestStand overwrites the file if it already exists.
  - Local Path 
 —The local path of the file to download when the Direction control is set to Download to Remote System. The local directory to upload the file to when the Direction control is set to Upload from Remote System. When you upload a file, the directory must exist and the path must be absolute.
  - Remote Path 
 —The remote path of the file to upload when the Direction control is set to Upload from Remote System, or the local directory to upload the file to when the Direction control is set to Download to Remote System. When you download a file, the directory must exist and the path must be absolute.

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

FTP Files Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/ftp-files-step-configuration-dialog-box.html language=enus -->
## TOPIC 03747: FTP Files Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/ftp-files-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/ftp-files-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure FTP Files in the context menu for the step or click Configure FTP Files on the General tab of the Step Properties dialog box to launch the FTP Files Step Configuration dialog box from a TestStand User Interface . Use this dialog box to specify what files to download to or upload fro

### FTP Files Step Configuration Dialog Box

Select
 Configure FTP Files
 in the context menu for the step or click
 Configure FTP Files
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the FTP Files Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to specify what files to download to or upload from a remote system.

The FTP Files Step Configuration dialog box contains the following options:

- Hostname 
 —The remote computer.
- Specify Remote Host by Expression 
 —Enable this option to specify that the Hostname control contains an expression the step evaluates at run time to determine the name of the remote host.
- FTP Username 
 —The user name to use to log into the FTP server on the remote system.
- FTP Password 
 —The password to use to log into the FTP server on the remote system.
- Files to FTP 
 —Lists the files to download or upload. Click
 Add 
 to add new files to the list. Click
 Remove 
 to remove the selected file from the list. Click
 Copy and Paste 
 to duplicate the selected file in the list. To modify an entry, select the entry and use the following controls:
  - Direction 
 —Specifies whether to download or upload the file.
  - Local File Path 
 —The local path of the file to download. This option is available only when you download a file.
  - Remote Directory 
 —The remote directory to download the file to. The directory must be either an absolute path or a relative path from the default login directory. The directory must already exist. This option is available only when you download a file.
  - Local Directory 
 —The local directory to upload the file to. The directory must be an absolute path. The directory must already exist. This option is available only when you upload a file.
  - Remote File Path 
 —The remote path of the file to upload. This option is available only when you upload a file.
  - Overwrite Existing File 
 —TestStand overwrites the file if it already exists.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

FTP Files Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/ftp-files-step.html language=enus -->
## TOPIC 03748: FTP Files Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/ftp-files-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/ftp-files-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a FTP Files step to download files to and upload files from a remote system. This step is particularly useful when you are using a real-time system that uses LabVIEW. Configuring the Step Use the FTP Files edit tab in the TestStand Sequence Editor and the FTP Files Step Configuration dialog box

### FTP Files Step

Use a FTP Files step to download files to and upload files from a remote system. This step is particularly useful when you are using a real-time system that uses LabVIEW.

#### Configuring the Step

Use the
 [FTP Files](ftp-files-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [FTP Files Step Configuration](ftp-files-step-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify what files to download to or upload from a remote system.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the FTP Files step type defines the following step properties:

- Step.RemoteHost 
 —The computer name or IP address of the remote computer. The
 Step.RemoteHostByExpr 
 property specifies whether the step interprets this property value as an expression or as a string.
- Step.RemoteHostByExpr 
 —When this property is
 True 
 , the step interprets the
 Step.RemoteHost 
 property value as an expression. When this property is
 False 
 , the step interprets the value as a string.
- Step.FTPUsername 
 —The login name to use when connecting to the server.
- Step.FTPPassword 
 —The password to use when connecting to the server.
- Step.FilesToFTP 
 —The local and remote file paths, the direction to transfer the file, and whether to overwrite a file when it exists.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Configuring a LabVIEW Step to Run Remotely](/csh?context=ts_tslabview_remote_step)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-panel-step-settings-pane.html language=enus -->
## TOPIC 03749: General Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Panel The General panel contains the following options: Name —The name of the step. Type —The type for the step. You can change the type by clicking the Change Step Type button, which displays a submenu from which you select the type of step you want TestStand to convert the existing step to

### General Panel - Step Settings Pane

#### General Panel

The General panel contains the following options:

- Name 
 —The name of the step.
- Type 
 —The type for the step. You can change the type by clicking the
 Change Step Type 
 button, which displays a submenu from which you select the type of step you want TestStand to convert the existing step to. TestStand discards any values in properties of the current step type that do not exist in the new step type. TestStand uses the default values for properties in the new step type that do not exist in the current step type.
- Adapter 
 —The adapter the step uses. You can change the adapter by selecting a different adapter in the ring control. TestStand discards module and parameter information unless you are changing the adapter from the LabWindows/CVI Adapter to the C/C++ DLL Adapter or vice versa.
- Icon 
 —The icon of the step. You can change the icon by selecting a different icon in the ring control.
- Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the step.
- Description 
 —A description of the step that varies according to the type of step and the adapter the step uses.
- Comment 
 —The comment for the step the
 TestStand Sequence Editor 
 displays in the
 Steps 
 pane. The comment of the step also appears in the documentation TestStand generates for the sequence file.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Steps Pane](steps-pane-execution-window.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-edit-rule-dialog-box.html language=enus -->
## TOPIC 03750: General Tab - Edit Rule Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-edit-rule-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-edit-rule-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Rule ID —Unique identifier for the rule . Choose an identifier that is unique to the rules on your computer and unique to the rules on computers to which you might deploy the rule. National Instruments recommends that you add a company name

### General Tab - Edit Rule Dialog Box

#### General Tab

The General tab contains the following options:

- Rule ID 
 —Unique identifier for the
 rule 
 . Choose an identifier that is unique to the rules on your computer and unique to the rules on computers to which you might deploy the rule. National Instruments recommends that you add a company name as a prefix to the rule ID to avoid potential conflicts with other custom rule IDs. The TestStand Sequence Analyzer shows the rule ID only in the Edit Rule dialog box and on the
 Rules 
 tab of the
 Configure Sequence Analyzer Available Rules 
 dialog box.
- Category 
 —Category to which the rule belongs. The
 Rules 
 pane of the
 Current Sequence Analyzer Project 
 window in the
 TestStand Sequence Editor 
 and the
 Rules 
 tab of the stand-alone
 TestStand Sequence Analyzer application 
 group rules by categories. You can select a built-in category or create a custom category. Specify subcategories by separating category names with a period. For example, the category
 NI.General 
 specifies a
 General 
 subcategory within the top-level
 NI 
 category. Add strings to the
 ANALYZER_RULE_CATEGORIES 
 section in a string resource file to localize category names.
- Severity 
 —Default severity level of the rule. Use this ring control to specify the severity level of a custom rule on the Rules pane of the Current Sequence Analyzer Project window and on the Rules tab of the sequence analyzer application. Sequence analyzer projects store the severity level of all rules. When you change the severity level of a rule on the Rules pane of the Current Sequence Analyzer Project window and on the Rules tab of the sequence analyzer application, the severity level changes to bold text to indicate that the severity level of the rule is a non-default value for the project. In general, use the Information severity level for statistical or descriptive information.
 When the sequence analyzer generates a message with an Error severity level before you execute a sequence in the
 TestStand Sequence Editor 
 , the sequence editor launches a dialog box to prompt you to view the errors.
- Name 
 —Short descriptive name that appears on the Rules pane of the Current Sequence Analyzer Project window, on the
 Analysis Results 
 pane, and on the Rules tab and
 Messages 
 tab of the sequence analyzer application.
- Description 
 —Detailed description of the rule that appears on the Rules pane of the Current Sequence Analyzer Project window, on the Analysis Results pane, and on the Rules tab and Messages tab of the sequence analyzer application. Include a description of the issue that generates a message, the motivation for the rule, and an explanation of how to fix the issue. Including information about the setting values prevents users from having to launch a dialog box to review the settings and includes the settings used for analysis in sequence analyzer reports you save. When you add the text
 %(
 SettingName
 ) 
 to this control, the sequence analyzer replaces each instance of the string
 %(
 SettingName
 ) 
 in the rule description with the value for the setting named SettingName.

#### See Also

[Analysis Results Pane](analysis-results-pane.html)

[Configure Sequence Analyzer Available Rules dialog box](configure-sequence-analyzer-available-rules-d.html)

[Creating Custom Rules](/csh?context=ts_tsref_sa_creating_custom_rules)

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[TestStand Sequence Analyzer Application](teststand-sequence-analyzer-application.html)

Parent topic:

Edit Rule Dialog Box
