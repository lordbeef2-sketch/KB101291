# NI DOCUMENT BUNDLE: systemlink-server

<!--NI_BUNDLE_CHUNK bundle=systemlink-server start=1 end=212 -->
<!--NI_TOPIC bundle=systemlink-server path=access-control-glossary.html language=enus -->
## TOPIC 00001: Role-Based Access Control Concepts

- bundle_id: `systemlink-server`
- source_path: `access-control-glossary.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/access-control-glossary.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Understand workspaces, roles, and privileges in SystemLink to organize your data and tailor SystemLink Web Application to different types of users. Automatic data encapsulation The process of data being stored in the same workspace as the system that produces it. Along with defining roles and privil

### Role-Based Access Control Concepts

Understand workspaces, roles, and privileges in SystemLink to organize your data and
 tailor SystemLink Web Application to different types of users.

Automatic data encapsulation

Workspace

Default workspace

- Data from clients using AMQP
- Data from pre-2020 R1 clients using HTTP
- OPC UA and Cloud Connector sessions
- File moving rules
- Health tag data

Role

User

Privilege

Mapping

Parent topic:

Managing Access to SystemLink

Related tasks:

- Managing Access to SystemLink
- Creating a Workspace
- Configuring a Role and Privileges

<!--NI_TOPIC bundle=systemlink-server path=acquiring-test-results.html language=enus -->
## TOPIC 00002: Acquiring Test Results

- bundle_id: `systemlink-server`
- source_path: `acquiring-test-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/acquiring-test-results.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create test steps to record your tests and measurement data. What to Use You can find the SystemLink Test Monitor and Configuration APIs on the Data Communication palette in LabVIEW 2018 or later.The SystemLink Configuration API is available in LabVIEW 2016 or later. What to Do On the client, comple

### Acquiring Test Results

Create test steps to record your tests and measurement data.

#### What to Use

Data
 Communication

Note

#### What to Do

1. Create a VI to build test results and steps.
2. Run a test sequence.
3. Structure your data to render correctly in the Test Monitor UI.
4. Acquire results.

Note

Customize the gray sections for your
 unique programming goals.

1. Add the following code to initialize and create test results on the server. [IMAGE alt='image' src='GUID-217D45F1-3701-4D4D-8E05-A03D5794C38C-a5.png'] 

 1
 Open Configuration initiates a
 connection to the server.
 2
 Initialize Test Result configures a
 local reference of the new test result on the client test system. Note The local reference does not
 exist on the server until you wire this VI to Create Test
 Result.
 3
 The Property Node sets properties to
 the test result. You can see these properties in the Test Monitor UI.
 4
 Create Test Result adds the local test
 result reference to the server with the properties you set.
 5
 Initialize Test Step From Result
 configures and associates a local reference of a test step to the test result
 you created. Note You must add
 the test result to the server before you can associate any test steps.
 Therefore, call this VI after you call Create Test
 Result. This VI only creates a local reference to the test step.
 You must call Create Test Step after this VI to add the VI to the
 server.
2. Add the following code to the diagram to initialize and create test steps associated
 with the test results. This code also generates named values to format test data. [IMAGE alt='image' src='GUID-0C75DBDF-8138-4D5E-843F-B532145ECF08-a5.png'] 

 6
 Generate Named Value converts the data you want to add
 to the test step as a named value object. Wire
 Build Array to the named value this
 VI generates to format the test data.
 7
 The Property Node sets the inputs for
 the test step using the named values the Build Array
 returns.
 8
 Create Test Step adds the local test
 step reference to the server with the properties you set. You can run a test
 VI after Create Test Step. Note In a more advanced test
 sequence, you might determine a standard VI prototype and load test VIs from
 a directory on disk.
3. Add the following code to collect data, update the test step data, and update the test results. [IMAGE alt='image' src='GUID-2B7813F3-030B-436E-A0A5-1A40F95BFF6F-a5.png'] 

 9
 Build a cluster structure for the TestStand data model so
 data displays correctly in the Test Monitor UI. Refer to *Structuring
 Your Test Data* to create the subVI you need to display your data
 correctly in Test Monitor.
 10
 Generate Named Value converts the test
 data into outputs. Wire Build Array to the named
 value this VI generates to format the test data.
 11
 The Property Node reads the outputs and
 data for the test step. Note You must set the Data Model as TestStand for your
 data to display correctly in the Test Monitor UI.
 12
 Update Test Step modifies the test step
 with the properties and data that the Property Node sets.
 13
 Update Test Result sets the result
 status that is based on the result of the test step. You can see the results
 in the Test Monitor UI.

#### Troubleshooting

- If test data does not display correctly in the Test Monitor UI, verify the cluster
 structure of the object for the TestStand Data Model. Refer to Structuring Your
 Test Data for more information.

Parent topic:

Connecting to LabVIEW and DIAdem

Related tasks:

- Structuring Your Test Data

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=adding-analysis-automation-procedures.html language=enus -->
## TOPIC 00003: Adding Analysis Automation Procedures

- bundle_id: `systemlink-server`
- source_path: `adding-analysis-automation-procedures.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-analysis-automation-procedures.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload analysis automation procedures to automatically analyze data. Create an analysis automation procedure (.anp) in DIAdem, Python, or Jupyter and save it to a folder which you can access from the SystemLink server. In Analysis Automation, click Instance on the dashboard. Click Procedures Add and

### Adding Analysis Automation Procedures

Upload analysis automation procedures to automatically analyze data.

.anp

1. In Analysis Automation, click
 Instance on the dashboard.
2. Click Procedures»Add and choose an analysis automation procedure.
3. Choose a workspace to determine which users can work with this procedure. 
 Note SystemLink always saves the analysis results to the default
 workspace.
4. Click OK.
5. Click Apply to accept the settings. 
 The analysis automation procedure displays under Procedures.
 Note If you don't have
 sufficient privileges, the Approved column displays
 this icon [IMAGE alt='image' src='GUID-7B4AFC35-EAFC-4233-A917-3BD21B4425BE-a5.svg'] indicating the procedure is pending
 approval. A user with permissions to approve or reject procedures needs to
 click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Approve to approve the procedure.

To execute analysis automation procedures, you need to add tasks.

Parent topic:

Analyzing Data

Related tasks:

- Adding or Editing Tasks for Analysis Automation Procedures

<!--NI_TOPIC bundle=systemlink-server path=adding-editing-search-areas.html language=enus -->
## TOPIC 00004: Adding and Editing Search Areas

- bundle_id: `systemlink-server`
- source_path: `adding-editing-search-areas.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-editing-search-areas.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit or add search areas to specify the folders on network computers where clients, such as Data Navigation, DIAdem, or LabVIEW, can search for data. Instances dedicated to the SystemLink file service do not have search areas. In Data Indexing, click DataFinder Instances. Select an instance and clic

### Adding and Editing Search Areas

Edit or add search areas to specify the folders on network computers where clients, such
 as Data Navigation, DIAdem, or LabVIEW, can search for data.

Note

1. In Data Indexing, click DataFinder
 Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. Click [IMAGE alt='image' src='GUID-240AE4D6-DBF9-477F-B7B2-CE427637128A-a5.svg']Add.
4. Specify a name and the path to the search area. Use a UNC path to specify the
 folder. An example UNC path is \\Server\MyFolder.
5. Choose a workspace to determine which users can access this search area in Data
 Navigation.
6. Click OK.
7. Optional: 
 Configure indexer settings to overwrite the global DataFinder indexing schedule
 for the selected search area. For the global indexing schedule, go to Index»Indexing Schedule in the DataFinder instance configuration.
8. Optional: 
 Select a search area and click Exclude Subfolders to
 exclude subfolders from indexing and searching.
9. Optional: 
 Use the arrows to determine the order in which the DataFinder instance searches
 for data in the search areas.
10. Click Apply to accept the settings.

DataFinder indexes the search areas according to your
 configuration.

Parent topic:

Creating a DataFinder Instance

<!--NI_TOPIC bundle=systemlink-server path=adding-editing-tasks-for-analysis-automation-procedures.html language=enus -->
## TOPIC 00005: Adding or Editing Tasks for Analysis Automation Procedures

- bundle_id: `systemlink-server`
- source_path: `adding-editing-tasks-for-analysis-automation-procedures.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-editing-tasks-for-analysis-automation-procedures.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use tasks to analyze data with analysis automation procedures. In Analysis Automation, click Instance on the dashboard. Click Tasks and select the task type. To determine the proper task type, refer to the following table. Task Type Description Manual Tasks User starts analysis automation tasks manu

### Adding or Editing Tasks for Analysis Automation Procedures

Use tasks to analyze data with analysis automation procedures.

1. In Analysis Automation, click
 Instance on the dashboard.
2. Click Tasks and select the task type. To determine the proper
 task type, refer to the following table. 
 Task Type
 DescriptionManual Tasks
 User starts analysis automation tasks manually.
 Triggered Tasks
 Analysis automation tasks start automatically when new or changed files
 become available. The DataFinder instance defined as the data source for a
 task notifies Analysis Automation about new or changed files.
 SystemLink automatically enables the checkbox Notify Analysis
 Automation about new or changed files on the
 Index tab in Data Indexing
 when you select a data source.
 Scheduled Tasks
 Analysis automation procedures start according to the configured schedule.
3. Click [IMAGE alt='image' src='GUID-240AE4D6-DBF9-477F-B7B2-CE427637128A-a5.svg']Add.
4. On the General tab, specify the following information. 
 A task name.
 A data source.
 The analysis automation procedure.
5. On the Access Control tab, specify the user context to
 define who can work with tasks. 
 Analysis Automation uses this setting in the following ways.Executing a query.
 Uploading results.
 Updating tags.Note The search results depend on the
 privileges the user has in one or more workspaces. The workspaces determine the data
 pool. 
 User ContextDescriptionAdvanced Analysis Privileges
 SystemLink executes the task with the following privileges.To update, upload, and query all data files in all workspaces.
 To create, update, and query tags.Note Analysis scripts written in
 DIAdem using the REST API run with the user context of the user specified in the
 script.Logged-in user
 SystemLink executes the task with the privileges of the logged-in user.Restricted Analysis Privileges
 SystemLink executes the task with the privileges to query all data files and tags
 in all workspaces. SystemLink restricts the following privileges to one output
 workspace.
 Updating and uploading data files.
 Creating and updating tags.Role
 SystemLink executes the task with the privileges of the service role you choose
 from the dropdown menu. In addition, the service role can only access the data
 within the workspace you configure in the next step.
6. Choose a workspace to determine which users can execute this task. This choice also
 affects the privileges with which Analysis Automation executes the task. 
 If you are working within the Role user context, the workspace
 determines which data the service role can access. Within the Restricted
 Analysis Privileges user context, the workspace determines to which
 workspace the task writes results.
7. Optional: 
 Modify any parameters on the Parameters tab, like the
 output folder.
8. To configure a scheduled task, select the
 Scheduler tab to decide when and how often the task runs.
9. Click OK.
10. Click Apply to accept the settings.
11. To edit a task, choose a task and select [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Edit.

Parent topic:

Adding Analysis Automation Procedures

Related reference:

- Role-Based Access Control Concepts

<!--NI_TOPIC bundle=systemlink-server path=adding-file-name-extensions.html language=enus -->
## TOPIC 00006: Adding File Extensions to a Registered DataPlugin

- bundle_id: `systemlink-server`
- source_path: `adding-file-name-extensions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-file-name-extensions.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add new file extensions to a registered DataPlugin to enable DataFinder instances to index files with these extensions and Data Preprocessor instances to scan and process files with these extensions. Select DataPlugins. Click of the DataPlugin for which you want to add a file extension. Click Add. E

### Adding File Extensions to a Registered DataPlugin

Add new file extensions to a registered DataPlugin to enable DataFinder instances to index files with these extensions and Data Preprocessor instances to scan and process files with these extensions.

1. Select 
 DataPlugins.
2. Click 
 [IMAGE alt='image' src='GUID-36BC81B5-7EEC-4A10-8E6F-D6843D8601DD-a5.png'] of the DataPlugin for which you want to add a file extension.
3. Click [IMAGE alt='image' src='GUID-15687469-27AA-4B72-9EDD-FCB86A920CBF-a5.svg']Add.
4. Enter the file extension that you want to add to the selected DataPlugin and click 
 OK.

Parent topic:

Accessing Your Files with DataPlugins

Related tasks:

- Registering DataPlugins to Index and Process New File Types

<!--NI_TOPIC bundle=systemlink-server path=adding-files-to-file-service.html language=enus -->
## TOPIC 00007: Uploading Files to SystemLink

- bundle_id: `systemlink-server`
- source_path: `adding-files-to-file-service.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-files-to-file-service.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: The File Service tab in Data Navigation displays all files stored in SystemLink. Upload files to the file service to enable clients to search for these files using a DataFinder instance that indexes the SystemLink file service. In Data Navigation, select an instance which indexes the SystemLink file

### Uploading Files to SystemLink

The File Service tab in Data Navigation
 displays all files stored in SystemLink. Upload files to the file service to enable
 clients to search for these files using a DataFinder instance that indexes the
 SystemLink file service.

1. In Data Navigation, select an instance
 which indexes the SystemLink file service, like the
 FileIndex instance, and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect.
2. Click the File Service tab. 
 SystemLink shows the files that are stored on the
 SystemLink server. The number of files displayed depends on
 the setting at the bottom right of the window.
3. Click Upload.
4. Click Browse.
5. Select a file and click Open.
6. Click Close. 
 The uploaded file now appears at the top of the file
 overview.

Parent topic:

Retrieving Data from Your Data Stores

<!--NI_TOPIC bundle=systemlink-server path=adding-meta-data-file-service-files.html language=enus -->
## TOPIC 00008: Adding and Editing Metadata of SystemLink File Service Files

- bundle_id: `systemlink-server`
- source_path: `adding-meta-data-file-service-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-meta-data-file-service-files.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add and edit metadata of SystemLink file service files to identify these files and to make it easier to find these files within a search. Before you begin, optimize the metadata to allow you to search for it. In Data Navigation, select an instance that indexes the SystemLink file service, like the F

### Adding and Editing Metadata of SystemLink File
 Service Files

Add and edit metadata of SystemLink file service files to identify these files and to
 make it easier to find these files within a search.

Before you begin, optimize the metadata
 to allow you to search for it.

1. In Data Navigation, select an instance
 that indexes the SystemLink file service, like the FileIndex
 instance, and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect.
2. Click the File Service tab. 
 SystemLink shows the files that are stored on the
 SystemLink server. The number of files displayed depends on
 the setting at the bottom right of the window.
3. Select a file and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Edit metadata properties.
4. Click Add Property.
5. Enter the name and value of the new metadata property. 
 Note You can
 also add metadata to a SystemLink file service file
 in the search results list.
6. Click OK.

Parent topic:

Retrieving Data from Your Data Stores

Related tasks:

- Making Custom Properties Searchable

<!--NI_TOPIC bundle=systemlink-server path=adding-properties-to-tag-to-display-on-dashboard-tile.html language=enus -->
## TOPIC 00009: Automatically Displaying Properties on a Dashboard Tile

- bundle_id: `systemlink-server`
- source_path: `adding-properties-to-tag-to-display-on-dashboard-tile.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-properties-to-tag-to-display-on-dashboard-tile.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add properties, or key-value pairs, to a tag or notebook (.ipynb) to automatically populate them on a dashboard tile when you add the data source to a tile. Adding Properties to a Tag Manually add properties to a tag so they display on a tile containing the tag. In Tags, double-click the tag you wan

### Automatically Displaying Properties on a
 Dashboard Tile

Add properties, or key-value pairs, to a tag or notebook (.ipynb) to
 automatically populate them on a dashboard tile when you add the data source to a
 tile.

#### Adding Properties to a Tag

Manually add properties to a tag so they display on a tile containing the tag.

1. In Tags, double-click the tag you want to use as a data source for the dashboard
 tile.
2. Click Add Property and define the property you want to
 automatically populate on the tile when you add the tag as a data source. Refer
 to the following table to determine which properties you want to add. Property on the tileDescriptionKeyExample valueTitleName you want the tile to displaydisplayNameFailed testsUnitsUnit of measurement, quantity, or classification of the
 dataunitsTestskm/sNavigationLink to data source in the SystemLink web applicationhyperlink#tagviewer/tag/d725064a-b04a/f00.bar Note These are the only
 properties you can define to automatically display on a tile for a
 tag.
3. Repeat step 2 to add more properties.
4. Click Save .

#### Adding Properties to a Notebook

Manually add properties to a notebook (.ipynb) so they display on a tile
 containing the notebook.

1. In Jupyter, double-click the notebook you want to use as a data source for a
 dashboard tile.
2. Define the properties in a code cell of the notebook. Refer to the following
 table to determine how you want to define the style of your tile. Property on the tileDescriptionProperty typeKeyExample valueX LabelY LabelName for the X and Y axes on a graph tileGlobalaxis_labels['x index', 'Day']Tick labelName for a data point on the graphGlobaltick_labels[{'x': 0, 'label': 'January'}, {'x': 1, 'label':
 'February'}]OrientationLayout of the tileGlobalorientationVERTICALPlot colorsColors you want to add to differentiate data plots on the
 graphPlotplot_colorCSS color name (e.g. blue)Hex string (e.g. #0000ff)RGB string (e.g. rgb(0,0,255))Plot styleType of graph you want to use to display the dataPlotplot_styleLINEBARPOINTSCATTER For example, your code cell may look like the
 following: # Result
sb.glue('navigation', '#testmonitor/testresults/config/...')
sb.glue('title', 'Image')
sb.glue('axis_labels', ['x index', 'Value'])
sb.glue('tick_labels', ticks)
sb.glue('orientation', 'VERTICAL')
sb.glue('result', result) Note The result
 in sb.glue('result', result) is an array of objects. For
 example, your code cell may look like the
 following:{
 plot_style: "BAR",
 plot_color: "rbg(0,0,255)"
 data_format: "XY",
 data_frame: {,…}}
}
3. Click Save .

Visualizing Data on a Tile Dashboard

Parent topic:

Visualizing Data on a Tile Dashboard

<!--NI_TOPIC bundle=systemlink-server path=adding-shared-scripts-to-dashboard.html language=dede -->
## TOPIC 00010: Wiederverwenden von Skripten in einem Dashboard

- bundle_id: `systemlink-server`
- source_path: `adding-shared-scripts-to-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/dede/adding-shared-scripts-to-dashboard.html
- source_language: `dede`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Sie können ein gemeinsam genutztes Python-Skript hinzufügen, das auf jedes Widget in Ihrem Dashboard angewendet werden kann. Öffnen Sie unter Dashboards das Dashboard, dem das Python-Skript hinzugefügt werden soll. Klicken Sie auf Bearbeiten. Klicken Sie dazu im Konfigurationsbereich für Gemeinsam S

### Wiederverwenden von Skripten in einem Dashboard

Sie können ein gemeinsam genutztes Python-Skript hinzufügen, das auf jedes Widget in Ihrem Dashboard angewendet werden kann.

1. Öffnen Sie unter Dashboards das Dashboard, dem das Python-Skript hinzugefügt werden soll.
2. Klicken Sie auf [IMAGE alt='image' src='GUID-0BBB5DF7-2F3D-4E09-AF49-E49EF12C2574-a5.png']»Bearbeiten.
3. Klicken Sie dazu im Konfigurationsbereich für Gemeinsam Skripte auf +. Daraufhin öffnet sich das Skript-Fenster.
4. Geben Sie einen eindeutigen Namen für Ihr Skript ein.
5. Fügen Sie Ihren Python-Code zum Skript-Fenster hinzu.
6. Wenn Sie damit fertig sind, klicken Sie auf OK. Unter "Dashboards" werden die gemeinsam genutzten Skripte im Konfigurationsbereich aufgelistet.
7. Klicken Sie auf Speichern und Wiedergabe, um Ihr Dashboard anzuzeigen.
8. Um Änderungen am gemeinsam genutzten Skript vorzunehmen, klicken Sie doppelt auf das entsprechende Skript im Konfigurationsfenster.

Übergeordnetes Thema:

Erweitern des Dashboard-Funktionsumfangs mit Python und JavaScript

<!--NI_TOPIC bundle=systemlink-server path=adding-users-without-idp.html language=enus -->
## TOPIC 00011: Adding Users to a Workspace Without Using an Identity Provider

- bundle_id: `systemlink-server`
- source_path: `adding-users-without-idp.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/adding-users-without-idp.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: As a workspace owner, add users to workspaces and manually specify roles without creating a mapping to an identity provider (IdP). This increases flexibility when managing workspace membership and roles. To add users to a workspace, ensure each user has successfully logged in to SystemLink Web Appli

### Adding Users to a Workspace Without Using an
 Identity Provider

As a workspace owner, add users to workspaces and manually specify roles without creating
 a mapping to an identity provider (IdP). This increases flexibility when managing workspace
 membership and roles.

To add users to a workspace, ensure each user
 has successfully logged in to SystemLink Web Application at least once.

1. Under Access Control, click
 Workspaces.
2. Click the workspace you want to add a user to.
3. Click Members. 
 This tab shows members who have logged in to SystemLink Web Application and
 who are not part of an IdP role mapping.
4. Click +Members to add a new member to this
 workspace.
5. Enter the name or email of the user you want to add to the workspace.
6. Select the user that matches your query from the list.
7. Click the role drop-down menus to select the appropriate roles for the
 user.
8. Click Update.

The user you added will receive an email inviting them to
 the workspace.

Parent topic:

Managing Access to SystemLink

<!--NI_TOPIC bundle=systemlink-server path=analysis-automation.html language=enus -->
## TOPIC 00012: Analyzing Data

- bundle_id: `systemlink-server`
- source_path: `analysis-automation.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/analysis-automation.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analysis Automation runs data analyses you define in analysis automation procedures. The procedures can save the result data in new TDM files or export management reports as a PDF or graphic. Reports provide in-depth insights on the tests you run and the results they produce. You can configure multi

### Analyzing Data

Analysis Automation runs data analyses you define in analysis automation procedures.
 The procedures can save the result data in new TDM files or export management reports as a
 PDF or graphic. Reports provide in-depth insights on the tests you run and the results they
 produce. You can configure multiple analyses to run concurrently and analyze different
 aspects of your test setup.

[IMAGE alt='image' src='GUID-BF4CE0EA-2DE4-43CB-BC52-B49A930AA5F3-a5.svg']

The following table highlights tasks in Analysis Automation to meet common data analysis
 goals.

| Goals | Analysis Automation Task |
| --- | --- |
| Configure your analyses, and specify data types, data sources, and report format according to your requirements. | Create analysis automation procedures in DIAdem, Python, or a Jupyter notebook. |
| Run analysis automation procedures. | Add your analysis automation procedures to the Analysis Automation instance. Configure manual, triggered, or scheduled tasks to determine when to run procedures and which data source to use. |

Parent topic:

Generating Actionable Data Insights

Related tasks:

- Creating Analysis Automation Procedures in DIAdem
- Creating, Editing, Testing, and Uploading Analysis Procedures in Jupyter
- Adding Analysis Automation Procedures
- Adding or Editing Tasks for Analysis Automation Procedures

<!--NI_TOPIC bundle=systemlink-server path=analysis-script-structure.html language=enus -->
## TOPIC 00013: Analysis Script Structure

- bundle_id: `systemlink-server`
- source_path: `analysis-script-structure.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/analysis-script-structure.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can create analysis scripts for Analysis Automation using Visual Basic Script or Python. The analysis automation procedure contains a script (Main.vbsa or Main.py), in which you define your analyses. In this script, you can include additional scripts that you must add to the analysis automation

### Analysis Script Structure

You can create analysis scripts for Analysis Automation using Visual Basic Script or Python. The analysis automation procedure contains a script (Main.vbsa or 
 Main.py), in which you define your analyses. In this script, you can include additional scripts that you must add to the analysis automation procedure. The analysis script 
 Main.vbsa or 
 Main.py contains the following elements by default.

| Script Code | Description |
| --- | --- |
| On_Initialize(oContext) | Initializes parallel evaluation. This method is called once before data processing. |
| On_RunAnalysisProcedure(oContext) | Performs the actual evaluation of the retrieved data elements. Parallel evaluation: The method is called once for each retrieved data element. Only one data element is available in the DataLinks collection. Comparative evaluation: The method is called only once. All retrieved data elements are available in the DataLinks collection. |
| On_Finalize(oContext) | Ends the parallel evaluation. The method is called once after data processing has finished. |

The 
 oContext transfer parameter exchanges information between analysis automation and the analysis script and gives access to the retrieved data elements.

The analysis script 
 main.py also contains the following elements.

| Script Code | Description |
| --- | --- |
| Import DIAdem dd = DIAdem.Application | Enables access to DIAdem commands, variables, and objects. You can use most DIAdem commands in the Python environment, but not all DIAdem commands have been tested in Python. |

The following table lists the most important DIAdem commands and methods for processing data.

| Script Code | Description |
| --- | --- |
| ApplicationSetLocale("english") | Sets country-specific variables and quantities, such as time format, paper size, and margins. |
| oContext.DataLinks | Contains the retrieved data elements. |
| Navigator.LoadData | Loads data. |
| ChannelsToArray | Converts DIAdem channels to arrays for processing in Python. |
| ArrayToChannels | Converts Python arrays to DIAdem channels. |
| DataFileSave | Saves data. |

You may not use the following commands in analysis scripts:

- Commands that require interaction.
- Commands that control the DIAdem interface.
- Commands that control the VIEW module.
- Commands that control Microsoft Office or other applications.

The following shows an example of an analysis script in Visual Basic Script. The 
 On_Initialize procedure checks whether the result path from the transfer parameter exists. The 
 On_Run_AnalysisProcedure procedure loads the elements for analyses, performs the analyses, and outputs the results in a PDF. The 
 On_Finalize procedure checks whether the procedures 
 On_Initialize and 
 On_Run_AnalysisProcedure were successful:

```text
Sub On_Initialize(oContext) 
  Call ApplicationSetLocale("english")
  Dim ResultsPath
  If oContext.Procedure.Arguments.Exists("ResultsPath") Then
    ResultsPath = oContext.Procedure.Arguments.Item("ResultsPath").Value
    Call oContext.LogResult("Results path: " & ResultsPath)
  Else
    Call oContext.LogError("Results path missing")
  End If
End Sub 
  
Sub On_Run_AnalysisProcedure(oContext) 
  Call ApplicationSetLocale("english")
  Dim ResultsPath
  ResultsPath = oContext.Procedure.Arguments.Item("ResultsPath").Value
  Dim oMyDataLinks, iCount
  Set oMyDataLinks = oContext.DataLinks
  For iCount = 1 To oMyDataLinks.Count
    Call Navigator.LoadData(oContext.DataLinks.Item(iCount))
    ' Enter your analysis commands    
  Next
  Call Report.LoadLayout(oContext.Procedure.ScriptPath & "MyLayout.tdr")
  Call Report.Sheets.ExportToPDF(ResultsPath & & "MyResult.pdf",FALSE)
End Sub 

Sub On_Finalize(oContext) 
    Call oContext.LogResult("Init ok: " & oContext.Status.On_Initialize_Succeeded)
    Call oContext.LogResult("Analysis ok: " & oContext.Status.On_Run_AnalysisProcedure_Succeeded)
End Sub
```

Parent topic:

Creating Analysis Automation Procedures in DIAdem

<!--NI_TOPIC bundle=systemlink-server path=analyze-tdms-test-files.html language=enus -->
## TOPIC 00014: Analyze TDMS Files from a Test Result

- bundle_id: `systemlink-server`
- source_path: `analyze-tdms-test-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/analyze-tdms-test-files.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Select TDMS files from a test result and execute a Data Analysis task using the selected files. Before you begin, ensure that you have test results that contain at least one TDMS file attachment. Navigate directly to Data Analysis to execute a task using one or more TDMS files from a test result. In

### Analyze TDMS Files from a Test Result

Select TDMS files from a test result and execute a Data Analysis task using the
 selected files.

Before you begin, ensure that you have
 test results that contain at least one TDMS file attachment.

Navigate directly to Data Analysis to
 execute a task using one or more TDMS files from a test result.

1. In Test Insights, select a result that contains one or more TDMS file
 attachments.
2. Click Attachments and select the TDMS files you want to
 analyze.
3. Select Analyze»Analyze TDMS Files. 
 SystemLink automatically navigates to Data Analysis while retaining the
 selections you made in Test Insights.
4. Select and execute the test you want to run on the TDMS files from one test
 result.

Parent topic:

Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-server path=analyzing-test-data-jupyter.html language=enus -->
## TOPIC 00015: Analyzing and Interacting with Test Results

- bundle_id: `systemlink-server`
- source_path: `analyzing-test-data-jupyter.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/analyzing-test-data-jupyter.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Filter, generate, and visualize test results to analyze your test and measurement data. There are many ways to analyze and interact with test results in Test Insights. Complete the tasks that best suit your test monitoring needs.

### Analyzing and Interacting with Test
 Results

Filter, generate, and visualize test results to analyze your test and measurement data.

There are many ways to analyze and interact with test results in Test Insights.
 Complete the tasks that best suit your test monitoring needs.

- [Filtering Test Results](filtering-test-results.html) Query test results to gain specific insights about your test data.
- [Generating Test Execution Reports](generating-test-execution-reports.html) Create detailed test reports for analysis using predefined Jupyter notebooks that install with NI SystemLink Test Module.
- [Adding TDMS Files to the Data Cart for Analysis](data-cart-analysis.html) Select and add TDMS file references from Test Insights Results to the Data Cart for use in a task in Analysis Automation. Use the Data Cart when you want to execute more than one test for different batches of TDMS files.
- [Analyze TDMS Files from a Test Result](analyze-tdms-test-files.html) Select TDMS files from a test result and execute a Data Analysis task using the selected files.

Parent topic:

Monitoring Tests

Related tasks:

- Monitoring Tests
- Visualizing Your Test Result Metadata
- Visualizing Product Information Associated with Test Results
- Visualizing the Parametric Data Trends of Your Test Results

<!--NI_TOPIC bundle=systemlink-server path=applying-custom-metadata-to-assets.html language=enus -->
## TOPIC 00016: Applying Custom Metadata to Assets

- bundle_id: `systemlink-server`
- source_path: `applying-custom-metadata-to-assets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/applying-custom-metadata-to-assets.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Assign properties or keywords to your assets to facilitate searching and filtering in your workspace. In the SystemLink web application, click Systems Assets . Double-click the asset to which you want to assign the property or keyword. Click to edit the asset. Specify a keyword or property for the a

### Applying Custom Metadata to Assets

Assign properties or keywords to your assets to facilitate searching and filtering in
 your workspace.

1. In the SystemLink web application, click Systems»Assets.
2. Double-click the asset to which you want to assign the property or keyword.
3. Click [IMAGE alt='image' src='GUID-5149C9B2-1BE6-4CEF-8FFB-19682559663A-a5.png'] to edit the asset.
4. Specify a keyword or property for the asset. The following table describes
 different use cases for keywords and properties. 
 Use Case
 Metadata TypeYou want to associate an asset with a
 string.
 Keyword
 You want to create key-value pairs for an
 asset.
 Property
5. Click 
 Update.

You can now filter the Assets list to show only assets that match
 the keywords or properties you assigned.

Parent topic:

Managing Your Assets

<!--NI_TOPIC bundle=systemlink-server path=archiving-workspaces.html language=enus -->
## TOPIC 00017: Archiving Your Workspaces

- bundle_id: `systemlink-server`
- source_path: `archiving-workspaces.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/archiving-workspaces.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Store your workspaces when your organization is no longer using them. If you archive a workspace, only users with the Server Administrator role can access it. No user, including an administrator, can edit its resources. Archiving a workspace also clears all active alarms associated with the workspac

### Archiving Your Workspaces

Store your workspaces when your organization is no longer using them.

If you archive a workspace, only users with the Server Administrator role can access it. No
 user, including an administrator, can edit its resources. Archiving a workspace also clears
 all active alarms associated with the workspace.

When the SystemLink Server Enterprise
 License expires, SystemLink automatically archives all workspaces except the default
 workspace.

1. In Access Control, click the
 Workspaces tab.
2. Click the [IMAGE alt='Workspace actions menu icon (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png'] button of the workspace you want to archive and click
 Archive workspace.
3. Click Archive. 
 Your workspace is now archived.
4. If your license is valid and you want to reenable a workspace, click the
 [IMAGE alt='Workspace actions menu icon (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png'] button of the workspace you want to enable and select
 Unarchive workspace.
5. If your enterprise license has expired, you can duplicate
 resources in the web application where the option is available and transfer them
 from an archived workspace to the default workspace.
  1. Select the resource you want to duplicate and click
 Duplicate.
  2. Select the workspace to which you want to duplicate and click
 OK.

Parent topic:

Managing Access to SystemLink

Related tasks:

- Creating a Workspace
- Purchasing SystemLink Licenses

Related reference:

- Role-Based Access Control Concepts

<!--NI_TOPIC bundle=systemlink-server path=assigning-user-claims-to-roles-in-a-workspace.html language=enus -->
## TOPIC 00018: Assigning User Claims to Roles in a Workspace

- bundle_id: `systemlink-server`
- source_path: `assigning-user-claims-to-roles-in-a-workspace.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/assigning-user-claims-to-roles-in-a-workspace.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create custom experiences for each type of user on the server by specifying which role a user has and which workspaces they can access. Refer to Assigning Users to Roles in a Workspace for more details about role mapping. In Access Control, click Workspaces. Find the workspace you want to add users

### Assigning User Claims to Roles in a
 Workspace

Create custom experiences for each type of user on the server by specifying
 which role a user has and which workspaces they can access. Refer to
 *Assigning Users to Roles in a Workspace* for more details about role
 mapping.

1. In Access Control, click
 Workspaces.
2. Find the workspace you want to add users to and click [IMAGE alt='Actions menu (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png']»Edit workspace.
3. Click Role mappings.
4. Click +Mapping and enter any claim as the attribute and
 the return value for the claim as the value for the mapping. 
 Figure 1.Example Response from
 userinfo_endpoint
 
 {
 "email": "jane.doe@ni.com",
 "family_name": "Doe",
 "given_name": "Jane",
 "name": "Jane Doe",
 "ni_employee": "2670",
 "sub": "jdoe"
}
 
[IMAGE alt="Edit workspace dialog showing a role mapping for the attribute 'ni_employee.'" src='GUID-A82C2D07-9D1A-4AA4-825A-D532D1B85646-a5.png']
 Note 
 All string values are case sensitive.
 If the claim value is a scalar, it must exactly match the value you
 specify in the role mapping .
 If the claim value is an array, one of the array elements must
 exactly match the value you specify in the role mappings.
 If the claim value contains quotes, you must escape the quotation
 marks with a backslash. Refer to the following example and the
 following figure.
 Figure 2.Example response from
 userinfo_endpoint with quotation marks
 
 {
 "userinfo": {
 "sub": "88442211",
 "country": "US",
 "name": "Bob Smith",
 "http://www.example.come/roles": [
 "user",
 "a\"b"
 ]
 }
}
 
[IMAGE alt='Edit workspace dialog. Role mappings tab, showing a value with an escaped quote (a\\"b).' src='GUID-0F823F0A-2049-401E-9D1A-E97EFD3912DF-a5.png']
5. Select the role you want to assign to the user.
6. Click Update. 
 Log out and log back in for the new mappings to take
 effect.

Parent topic:

Managing Access with OpenID Connect

<!--NI_TOPIC bundle=systemlink-server path=associating-test-results-with-a-product.html language=enus -->
## TOPIC 00019: Associating Test Results with a Product

- bundle_id: `systemlink-server`
- source_path: `associating-test-results-with-a-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/associating-test-results-with-a-product.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Specify a part number in test result metadata to associate the result with a product. Right-click the Sequences pane and select Sequence File Callbacks. Select the PreUUT callback and click OK. Insert a Statement step in the PreUUT sequence. To assign the UUT PartNumber parameter, update the Express

### Associating Test Results with a
 Product

Specify a part number in test result metadata to associate the result with a
 product.

1. Right-click the Sequences pane and select
 Sequence File Callbacks.
2. Select the PreUUT callback and click
 OK.
3. Insert a Statement step in the PreUUT
 sequence.
4. To assign the UUT PartNumber parameter, update the
 Expression. For example,
 Parameters.UUT.PartNumber="YourPartNumber".

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-server path=batch-indexing-datafinder.html language=enus -->
## TOPIC 00020: Batch Indexing Folders or Files

- bundle_id: `systemlink-server`
- source_path: `batch-indexing-datafinder.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/batch-indexing-datafinder.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use job files as an option to prioritize the indexing of new files in a batch process. The following task enables the processing of job files and specifies their location. You cannot use job files with DataFinder instances that index the SystemLink file service, like the FileIndex instance. Open a t

### Batch Indexing Folders or Files

Use job files as an option to prioritize the indexing of new files in a batch process.
 The following task enables the processing of job files and specifies their location. You
 cannot use job files with DataFinder instances that index the SystemLink file service, like
 the FileIndex instance.

1. Open a text editor and create a job file. For more information, refer to
 *Properties and Structure of Job Files*.
2. Save the job file using .dfij to a path which the DataFinder
 instance can access.
3. In 
 Data Indexing, click 
 DataFinder Instances.
4. Select an instance and click 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Index»Job Files.
5. Enable the processing of job files.
6. Select the folder to which you saved the job files. Use a UNC path to specify
 the folder. An example UNC path is \\Server\MyFolder. Click
 OK.
7. Click Apply to accept the settings. 
 A DataFinder instance processes all job files in the specified folder
 and deletes them after indexing.
8. Review any errors that occurred during the indexing process and make changes to
 your files if necessary. The Errors folder is located below the
 folder that contains the job files.

Create Index Job File VI

DataFinder Toolkit
 VIs

DataFinder Connectivity VIs

Parent topic:

Configuring File Indexing for a DataFinder Instance

Related reference:

- Properties and Structure of Job Files

<!--NI_TOPIC bundle=systemlink-server path=batch-processing-datapreprocessor.html language=enus -->
## TOPIC 00021: Batch Processing Folders or Files

- bundle_id: `systemlink-server`
- source_path: `batch-processing-datapreprocessor.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/batch-processing-datapreprocessor.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use job files to prioritize the harmonization of new files in a batch process. Enable the processing of job files and specify their location. Open a text editor and create the job file. Refer to Properties and Structure of Job Files for more information on how to create job files. Save the job file

### Batch Processing Folders or Files

Use job files to prioritize the harmonization of new files in a batch process. Enable
 the processing of job files and specify their location.

1. Open a text editor and create the job file. Refer to *Properties and Structure of
 Job Files* for more information on how to create job files.
2. Save the job file using *.dfpj as the file extension to a path
 which the Data Preprocessor instance can access.
3. In 
 Data Preparation, click 
 Data Preprocessor Instances.
4. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Monitoring»Job Files.
5. Enable the processing of job files.
6. Select the folder to which you saved the job files. Use a UNC path to specify
 the folder. An example UNC path is \\Server\MyFolder. Click
 OK.
7. Click Apply to accept the settings. 
 A Data Preprocessor instance processes all job files in the specified
 folder and deletes them after processing.
8. Review any errors that occurred during the harmonization process and make
 changes to your files if necessary. The Errors folder is
 located below the folder that contains the job files.

Parent topic:

Configuring a Data Preprocessor Instance

Related reference:

- Properties and Structure of Job Files

<!--NI_TOPIC bundle=systemlink-server path=binding-language-syntax.html language=dede -->
## TOPIC 00022: Bindungs-Syntax

- bundle_id: `systemlink-server`
- source_path: `binding-language-syntax.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/dede/binding-language-syntax.html
- source_language: `dede`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Um das Anzeigen von Daten in einem Dashboard zu ermöglichen, werden Eigenschaftswerte von Bedien- oder Anzeigeelementen an andere Eigenschafts- oder Tag-Werte angebunden. Die folgende Tabelle zeigt, welche Syntax in der Eigenschaft des Bedien- oder Anzeigeelements zum Binden an unterschiedliche Wert

### Bindungs-Syntax

Um das Anzeigen von Daten in einem Dashboard zu ermöglichen, werden Eigenschaftswerte von Bedien- oder Anzeigeelementen an andere Eigenschafts- oder Tag-Werte angebunden. Die folgende Tabelle zeigt, welche Syntax in der Eigenschaft des Bedien- oder Anzeigeelements zum Binden an unterschiedliche Wertetypen verwendet wird.

| Wertetyp | Art der auszuwählenden Bindung | Bindungs-Syntax | Beispiel |
| --- | --- | --- | --- |
| Tag | Tag | Tag-Name | ni.tag |
| Tag-Eigenschaft | Tag | Tag-Name gefolgt von einem Doppelpunkt und dem Eigenschaftsnamen | ni.tag:min |
| Wert einer anderen Bedien- oder Anzeigeelementeigenschaft | Widget | Name des Bedien- oder Anzeigeelements gefolgt von einem Doppelpunkt und dem Eigenschaftsnamen | vSlider1:value |
| Parameter | Widget | Fragezeichen gefolgt vom Namen des Parameters, den Sie erstellen möchten | ?parameterName |
| Tag oder System, dessen Pfad durch den Wert eines Parameters im Dashboard festgelegt wird | Tag oder System | Parametername in Klammern innerhalb des Namens des Tags oder Systems | ni.(parameterName).tag |
| System-Grain | System | Host-Name des Systems, gefolgt vom Grain-Namen | hostnameOfSystem.grainName |

Übergeordnetes Thema:

Darstellen von Tag-Daten in einem Dashboard mit freiem Layout

Zugehörige Tasks:

- Überwachen von Daten mit Hilfe von Tags
- Angeben von Werten für Objektelemente

Zugehörige Verweise:

- Datentypen zur Darstellung von Tag-Daten

<!--NI_TOPIC bundle=systemlink-server path=binding-virtual-tags-to-widgets.html language=dede -->
## TOPIC 00023: Binden von virtuellen Tags an Widgets

- bundle_id: `systemlink-server`
- source_path: `binding-virtual-tags-to-widgets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/dede/binding-virtual-tags-to-widgets.html
- source_language: `dede`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Fügen Sie Ihrem Dashboard mit freiem Layout ein virtuelles Tag-Skript hinzu, um virtuelle Tags für die Bindung an ein Widget zu generieren. Mit virtuellen Tags können Sie Ihre Tag-Daten auf individuelle Weise visuell darstellen und analysieren.Dieser Dashboard-Typ ist veraltet. Es wird empfohlen, Ka

### Binden von virtuellen Tags an Widgets

Fügen Sie Ihrem Dashboard mit freiem Layout ein virtuelles Tag-Skript hinzu, um virtuelle Tags für die Bindung an ein Widget zu generieren. Mit virtuellen Tags können Sie Ihre Tag-Daten auf individuelle Weise visuell darstellen und analysieren.

Hinweis

Ein virtuelles Tag verwendet echte Tags von Ihrem SystemLink-Server als Parameter. Wenn diese Parameter (reale Tags) Werte an die Hauptfunktion Ihres Skripts übergeben, wird der Wert des virtuellen Tags aktualisiert. Daher können Sie nur Werte von virtuellen Tags in Ihrem Dashboard anzeigen.

1. Öffnen Sie unter "Dashboards" das Dashboard, für das Sie einem Widget ein Ereignisskript hinzugefügt haben.
2. Klicken Sie auf [IMAGE alt='image' src='GUID-0BBB5DF7-2F3D-4E09-AF49-E49EF12C2574-a5.png']»Bearbeiten.
3. Klicken Sie im Konfigurationsbereich unter Skripte auf +, um ein virtuelles Tag hinzuzufügen. Daraufhin öffnet sich das Skript-Fenster.
4. Geben Sie den Namen der Hauptfunktion des Ereignisskripts ein, das Sie zuvor zu einem Widget im Dashboard hinzugefügt haben.
5. Fügen Sie Ihrem Skript Eingabe-Tags hinzu. Die von Ihnen angegebenen Tags werden automatisch zu Parametern, die an das Skript übertragen werden.
  1. Klicken Sie auf +.
  2. Geben Sie den Pfad des Tags an, der auf Ihrem SystemLink-Server vorhanden ist.
6. Fügen Sie Ausgabe-Tags hinzu, die das Skript erstellen soll.
  1. Klicken Sie auf +.
  2. Geben Sie den Pfad des virtuellen Tags an, das Sie erstellen möchten.
7. Geben Sie im "Skript"-Fenster def ein und drücken Sie <Strg + Leertaste>, um die Funktionsdefinition automatisch zu generieren und die Anweisung auszugeben.
8. Fügen Sie Ihren Python-Code hinzu, mit dem die Logik des Skripts ausgeführt wird.
9. Wenn Sie damit fertig sind, klicken Sie auf OK. Unter "Dashboards" werden die Skripte im Konfigurationsbereich aufgelistet.
10. Klicken Sie auf Speichern und Wiedergabe, um Ihr Dashboard anzuzeigen.
11. Um Änderungen am Skript des virtuellen Tags vorzunehmen, klicken Sie doppelt auf das entsprechende Skript im Konfigurationsfenster.

Übergeordnetes Thema:

Erweitern des Dashboard-Funktionsumfangs mit Python und JavaScript

<!--NI_TOPIC bundle=systemlink-server path=building-a-package-of-your-web-application-g-web.html language=enus -->
## TOPIC 00024: Creating a Package of Your Web Application in G Web Development Software or LabVIEW NXG Web Module

- bundle_id: `systemlink-server`
- source_path: `building-a-package-of-your-web-application-g-web.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/building-a-package-of-your-web-application-g-web.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Build a package (.nipkg) of your web application to host it on SystemLink. Before you build a package (.nipkg) of your web application, you must complete the following tasks: Create a web application you want to host. Remove the API key from the panel and the diagram to maximize the security of your

### Creating a Package of Your Web Application
 in G Web Development Software or LabVIEW NXG Web Module

Build a package (.nipkg) of your web application to host it on
 SystemLink.

.nipkg

- Create a web application you want to host.
- Remove the API key from the panel and the diagram to
 maximize the security of your web application. Refer to the Hosting Authentication
 Credentials Securely section of Security in NI Web Technology for more
 information.

1. Click 
 File»New»Package/Installer. 
 The Package document opens in the project.
2. Drag your web application from the Project Files tab to
 the Files section. 
 You can include applications and other support files. 
 The Package document automatically calculates the package dependencies
 that your application requires.
3. Review the contents of the 
 Package Dependencies section, which displays package dependencies your application requires. 
 You can include additional dependencies by clicking 
 Dependencies and selecting packages under 
 Add Dependencies.
4. In the 
 Information section, confirm that the Package document filled the text boxes with information you want. 
 The Package document automatically gathers information from the project and your NI User Account to complete the 
 Information section. The values in the text boxes become metadata in the package. NI Package Manager reads the metadata of packages to sort them and display information about them to users.
5. On the Document tab, select Web
 Server as the Build target.
6. Select Package as the Output
 type.
7. Click File»Save all.
8. Click 
 Build. 
 The Build Queue tab shows the status of the
 build process.

Parent topic:

Hosting a WebVI in SystemLink

Related information:

- Create a web application
- Security in NI Web Technology

<!--NI_TOPIC bundle=systemlink-server path=building-alarms-to-manage-systems-assets-tests.html language=enus -->
## TOPIC 00025: Generating Custom Alarms

- bundle_id: `systemlink-server`
- source_path: `building-alarms-to-manage-systems-assets-tests.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/building-alarms-to-manage-systems-assets-tests.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Build alarms to notify you when an issue occurs in your system. What to Use You can find the SystemLink Alarm and Utilities APIs on the Data Communication palette in LabVIEW.The Utilities API is not supported in LabVIEW NXG. What to Do On the client, create the following diagram in a VI to create al

### Generating Custom Alarms

Build alarms to notify you when an issue occurs in your system.

#### What to Use

Note

#### What to Do

1. On the client, create the following diagram in a VI to create alarms to implement rules
 and manage conditions affecting your systems, tests, or assets.

[IMAGE alt='LabVIEW block diagram that computes deadband and creates a SystemLink alarm when DC value is above normal.' src='GUID-88D0E435-68B6-40A9-9CED-9A435EF77CF3-a5.png']

| 1 | Get System Name obtains the name of the system you want to monitor so you can receive alerts if alarm conditions occur. |
| --- | --- |
| 2 | Build Alarm Set Transition creates a set transition, which describes the state and severity level of the alarm instance, to apply to a notification strategy. |
| 3 | Set Alarm triggers an alarm instance on the server. If Build Set Alarm has a notification strategy wired to it, then a notification is sent to subscribers if the alarm instances are new. The subscriber then verifies and fixes the issue before acknowledging it. After the application determines the current state of the alarm is below the defined alarm threshold, the application clears the alarm with Clear Alarm. |

#### Troubleshooting

- If you need to review active and inactive alarm instances, use the Alarms and
 Notifications UI in the SystemLink web application.
- If Set Alarm only returns True the
 first time you set an alarm and then always returns
 False, verify you or another operator acknowledged
 the alarm. If the alarm is not acknowledged, it will
 remain active.
- If you specify a notification strategy and do not
 receive an email to notify you about an active alarm
 instance, verify the following things.
  - If the alarm is new or not. A notification is
 only sent when a new alarm instance occurs.
  - If you configured a notification strategy in the SystemLink web application.
  - If you configured an SMTP service in NI
 SystemLink Server Configuration.

#### Examples

- Alarms

Parent topic:

Connecting to LabVIEW and DIAdem

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=checking-status-analysis-automation-tasks.html language=enus -->
## TOPIC 00026: Checking the Status of Analysis Automation Tasks

- bundle_id: `systemlink-server`
- source_path: `checking-status-analysis-automation-tasks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/checking-status-analysis-automation-tasks.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the task overview in Analysis Automation to check the status of current and completed tasks. In Analysis Automation, click Instances on the dashboard. Click History. Filter the task list to show a subset of tasks. Choose a status filter or enter a task name. Filtering tasks is case-insensitive.

### Checking the Status of Analysis Automation Tasks

Use the task overview in Analysis Automation to check the status of current and
 completed tasks.

1. In Analysis Automation, click
 Instances on the dashboard.
2. Click History.
3. Optional: 
 Filter the task list to show a subset of tasks. Choose a status filter or enter a task name. 
 Note Filtering tasks is case-insensitive.
4. To view subtasks of tasks, click [IMAGE alt='image' src='GUID-D5A7C916-A93F-4A08-BB71-3DF56CFC3740-a5.png']. The evaluation mode you chose
 when defining the analysis automation procedure in DIAdem creates the following
 subtasks: 
 Evaluation Mode
 ResultComparative evaluation
 Analysis Automation processes all incoming data files in the same subtask.
 Therefore, each task contains one subtask.
 Parallel evaluation
 Analysis Automation processes all incoming data files concurrently in separate
 subtasks. Therefore, a task always contains the subtasks
 On_Initialize and
 On_Finalize plus a subtask for each
 analyzed data element from the data source.

Parent topic:

Analyzing Data

<!--NI_TOPIC bundle=systemlink-server path=choosing-a-mongodb-deployment.html language=enus -->
## TOPIC 00027: Choosing a MongoDB Deployment

- bundle_id: `systemlink-server`
- source_path: `choosing-a-mongodb-deployment.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/choosing-a-mongodb-deployment.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Most of the SystemLink services use MongoDB as the primary database. You can use MongoDB on the same server hosting SystemLink or set up a remote MongoDB instance. Use the following table to choose the MongoDB deployment that best suits your use case. Deployment Description When to Use Single node w

### Choosing a MongoDB Deployment

Most of the SystemLink services use MongoDB as the primary database. You can use MongoDB
 on the same server hosting SystemLink or set up a remote MongoDB instance.

Use the following table to choose the MongoDB deployment that best suits your
 use case.

| Deployment | Description | When to Use |
| --- | --- | --- |
| Single node with defaults | This is the default installation where you have one server that hosts both SystemLink and MongoDB Community Edition. | During evaluation When working with less than 10 managed nodes In deployments that do not use the Asset Manager module Note If you increase the index cache, you can use this deployment with up to 25 managed nodes. |
| Multi-node with standalone MongoDB instance | You have two different servers hosting SystemLink and MongoDB. | When the MongoDB Windows service is consuming enough CPU, memory, and disk space to impact the operation of SystemLink services. |
| Multi-node with MongoDB replica sets | You have one server hosting SystemLink and three or more servers hosting MongoDB. NI Recommends the configuration for all production deployments. | When working with more than 50 nodes When you want to mitigate data loss. |
| Multi-node with MongoDB Atlas | You have one server hosting SystemLink and are connecting to a MongoDB Atlas cluster. | When working with more than 200 nodes When you want to simplify database provisioning, operation, backup, and restore. |

Note

- [Decreasing CPU Usage for Single Node Deployments](decreasing-cpu-usage-for-single-node-deployments.html) Increase the index cache size to process more data, avoid high CPU usage, and enable the Asset Management module in a single-node deployment. NI recommends increasing the available memory for the index to 8GB.
- [Connecting to a Standalone Remote Mongo Database](remote-mongo-database.html) Configure SystemLink to access a remote Mongo database to enhance scalability and fault tolerance.
- [Connecting to a Remote Mongo Database with Replica Sets](connecting-to-a-remote-mongo-database-with-replica-sets.html) Connect to a remote MongoDB instance with replica sets to create redundancy in your database and mitigate data loss.
- [Connecting to a Remote Mongo Database with MongoDB Atlas](connecting-to-a-remote-mongo-database-with-mongodb-atlas.html) Connect to a MongoDB Atlas account for simpler database setup and administration compared to other deployments.
- [MongoDB Support Limitations](mongodb-support-limitations.html) Learn about the limitations that might prevent SystemLink from connecting to your MongoDB instance.
- [Connection String Format](connection-string-format.html) Consider the following guidelines when formatting your connection string to connect to a MongoDB instance.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related information:

- MongoDB documentation

<!--NI_TOPIC bundle=systemlink-server path=combining-search-conditions.html language=enus -->
## TOPIC 00028: Combining Search Conditions in an Advanced Search

- bundle_id: `systemlink-server`
- source_path: `combining-search-conditions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/combining-search-conditions.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Combine several search conditions to receive only specific search results. Data Navigation writes the operators for the individual search conditions in the operator line. The following table contains examples for combined search conditions. Objective Search Parameters Find files containing channels

### Combining Search Conditions in an Advanced Search

Combine several search conditions to receive only specific search results. Data Navigation writes the operators for the individual search conditions in the operator line. The following table contains examples for combined search conditions.

| Objective | Search Parameters |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Find files containing channels with the channel name MyChannel. |  | Level | Property | Operator | Value |
| C1 | Channel | Name | = | MyChannel |  |
| Operator line: C1 |  |  |  |  |  |
|  |  |  |  |  |  |
| Find files with the filename MyData and the description My Test data. |  | Level | Property | Operator | Value |
| C1 | File | Filename | = | MyData |  |
| C2 | File | Description | = | My Test data |  |
| Operator line: C1 AND C2 |  |  |  |  |  |
|  |  |  |  |  |  |
| Find files with the filename MyData1 and a channel group named MyGroup1. |  | Level | Property | Operator | Value |
| C1 | File | Filename | = | MyData1 |  |
| C2 | Group | Name | = | MyGroup1 |  |
| Operator line: C1 AND C2 |  |  |  |  |  |
|  |  |  |  |  |  |
| Find files with the filename MyData1 that contain channel groups named MyGroup1 and channels with the unit m/s. |  | Level | Property | Operator | Value |
| C1 | File | Filename | = | MyData1 |  |
| C2 | Group | Name | = | MyGroup1 |  |
| C3 | Channel | Unit | = | m/s |  |
| Operator line: C1 AND C2 AND C3 |  |  |  |  |  |
|  |  |  |  |  |  |
| Find files where the property DataPlugin name contains the values TDM or TDMS. |  | Level | Property | Operator | Value |
| C1 | File | DataPlugin name | = | TDM OR TDMS |  |
| Operator line: C1 |  |  |  |  |  |
| Note You can also create two individual search conditions and combine them with the OR operator. |  |  |  |  |  |
|  |  |  |  |  |  |
| Find files where the file property DataPlugin name contains the value TDM or TDMS or the channel property Name contains the value MyChannel1. |  | Level | Property | Operator | Value |
| C1 | File | DataPlugin name | = | TDM OR TDMS |  |
| C2 | Channel | Name | = | MyChannel1 |  |
| Operator line: C1 OR C2 |  |  |  |  |  |
|  |  |  |  |  |  |
| Find files last edited on 10/29/2007 that contain either a channel named MyChannel1 or were edited by the author Tom. |  | Level | Property | Operator | Value |
| C1 | File | Modify date | = | 10/29/2007 |  |
| C2 | Channel | Name | = | MyChannel1 |  |
| C3 | File | Author | = | Tom |  |
| Operator line: C1 AND (C2 OR C3) |  |  |  |  |  |
|  |  |  |  |  |  |
| Find files with the filename MyData* and the file description Test* and sort the search results in ascending order by filename. |  | Level | Property | Operator | Value |
| C1 | File | Name | = | MyData* |  |
| C2 | File | Description | = | Test* |  |
| Operator line: C1 AND C2 Order By: C1 |  |  |  |  |  |
| Note Click next to a search condition to specify whether the respective search results are returned in ascending or descending order. Data Navigation displays the sort order of the search results in the operator line. Search results from a federation cannot be returned in a specified order. |  |  |  |  |  |

Parent topic:

Finding Data with Advanced Search

<!--NI_TOPIC bundle=systemlink-server path=communicating-data-with-tags.html language=enus -->
## TOPIC 00029: Communicating Data with Tags

- bundle_id: `systemlink-server`
- source_path: `communicating-data-with-tags.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/communicating-data-with-tags.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Communicate and manage data from your test and measurement systems with tags. Tags in SystemLink transmit and store slow-moving measurement data like system status or health. Use tags to track measurements, monitor system health, create alarms, and visualize data on dashboards.

### Communicating Data with Tags

Communicate and manage data from your test and measurement systems with tags. Tags in
 SystemLink transmit and store slow-moving measurement data like system status or health.
 Use tags to track measurements, monitor system health, create alarms, and visualize data
 on dashboards.

- [Transferring Data Using Tags](transfer-tags.html) Use tags to send and receive data from one system to other systems.
- [Monitoring and Visualizing Data with Tags](monitoring-data-with-tags.html) Create and configure a tag to track the value of scalar data.
- [Verifying Your Tag Data in Tags](troubleshooting-tag-data.html) Troubleshoot your test and measurement data in Tags to verify your system returns tag data as expected.

Parent topic:

Sharing Data

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=comparing-asset-availability.html language=enus -->
## TOPIC 00030: Comparing Asset Connection History

- bundle_id: `systemlink-server`
- source_path: `comparing-asset-availability.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/comparing-asset-availability.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Visualize the connection history for different assets to make maintenance decisions and analyze performance. In the SystemLink web application, click Systems Assets . Check the box next to the assets you want to compare. You can select up to 10 assets. Click Compare Connection History. Under Timespa

### Comparing Asset Connection History

Visualize the connection history for different assets to make maintenance decisions and analyze performance.

1. In the SystemLink web application, click Systems»Assets.
2. Check the box next to the assets you want to compare. 
 You can select up to 10 assets.
3. Click Compare Connection History.
4. Under 
 Timespan, select the length of time you want the comparison to include. 
 The graph updates to show the relative availability of the assets.

Parent topic:

Managing Your Assets

Related tasks:

- Viewing Calibration Data for Hardware
- Tracking Asset Connection History

<!--NI_TOPIC bundle=systemlink-server path=comparing-system-states.html language=enus -->
## TOPIC 00031: Comparing Software across Systems

- bundle_id: `systemlink-server`
- source_path: `comparing-system-states.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/comparing-system-states.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Compare installed packages, or system states, to facilitate decisions about deployment and maintenance. System states are software package sets you can define and deploy to multiple systems. Refer to the help for creating and deploying a state for more information about system states. In the SystemL

### Comparing Software across Systems

Compare installed packages, or system states, to facilitate decisions about deployment and maintenance.

System states are software package sets you can define and deploy to multiple systems. Refer to the help for creating and deploying a state for more information about system states.

1. In the SystemLink web application, click Systems»States.
2. Select up to 2 states and click Compare.
3. If you want to compare software installed on a specific system, select 
 System from the 
 Type menu. 
 You can compare a system to a state or to another system of the same type.

The comparison view shows all differences between the states or systems you selected.

Parent topic:

Deploying Applications to Clients on a Server

Related tasks:

- Deploying System States to Clients
- Deploying Packages to Clients

<!--NI_TOPIC bundle=systemlink-server path=configuring-advanced-security-settings.html language=enus -->
## TOPIC 00032: Configuring Advanced Security Settings

- bundle_id: `systemlink-server`
- source_path: `configuring-advanced-security-settings.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-advanced-security-settings.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: To add an extra layer of security, provide a custom prime number value to the Diffie-Hellman algorithm that TLS protocol uses as part of the connection handshake. By default, NI Web Server uses a set of prime values defined by the Apache Web Server. This default is sufficient for most cases. Longer

### Configuring Advanced Security Settings

To add an extra layer of security, provide a custom prime number value to the
 Diffie-Hellman algorithm that TLS protocol uses as part of the connection handshake. By
 default, NI Web Server uses a set of prime values defined by the Apache Web Server. This
 default is sufficient for most cases.

Longer parameters increase the computational
 cost of handling each TLS connection to the server. Additionally, older TLS client
 applications may not support longer keys. Ensure you test before you deploy to
 production.

1. On the SystemLink Server machine, open Command Prompt and run the following
 command. 
 Note The following command uses the copy of OpenSSL installed with SystemLink
 23.5 or later. You can substitute a different copy of
 OpenSSL."c:\Program Files\National
 Instruments\Shared\Skyline\OpenSSL\openssl.exe" dhparam -outform PEM -out
 dhparam.txt numbitsWherenumbits is the bit length for the
 prime. You can specify 1024, 2048, 3072, 4096, 7680, or 8192 bits. NI
 recommends using a length of at least 3072 bits. 
 The command creates a file called dhparam.txt in
 the current directory.
2. Run a text editor as an administrator and open the NI Web Server certificate
 located at C:\Program Files\National Instruments\Shared\Web
 Server\certs\. If there are multiple certificate files in this
 directory, open C:\Program Files\National Instruments\Shared\Web
 Server\conf\defines.d\50_httpd-defines.conf and use the file
 specified for the TLS_CERTIFICATE_PATH
 variable.
3. Open dhparam.txt and copy and paste the contents into the
 certificate file on a new line after the last -----END
 CERTIFICATE-----.
4. Save and close the certificate file.
5. Open NI Web Server Configuration and click Restart on
 the Control tab.

Repeat this process whenever you update the configured
 HTTP certificate in the NI Web Sever Configuration tool.

Related information:

- Cryptographic Key Length Recommendation

<!--NI_TOPIC bundle=systemlink-server path=configuring-file-export.html language=enus -->
## TOPIC 00033: Configuring the File Export for Data Navigation

- bundle_id: `systemlink-server`
- source_path: `configuring-file-export.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-file-export.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure the download area of Data Navigation to keep it uncluttered and to distribute resources. In Data Indexing, click Global SettingsData Navigation Environment Settings. Configure the download area. Parameter Description Files expire after Time in hours after which Data Navigation deletes the

### Configuring the File Export for Data Navigation

Configure the download area of Data Navigation to keep it uncluttered and to distribute resources.

1. In 
 Data Indexing, click 
 Global Settings»Data Navigation Environment Settings.
2. Configure the download area. 
 Parameter
 DescriptionFiles expire after
 Time in hours after which Data Navigation deletes the files from the download area.
 Timeout per export
 Time in seconds after which Data Navigation stops exporting files to the download area.
 Number of parallel requests to the compute nodes
 Number of requests that Data Navigation can process in parallel when converting data
 and exporting files to the download center.

Parent topic:

Indexing Data

<!--NI_TOPIC bundle=systemlink-server path=configuring-file-indexing-for-searching.html language=enus -->
## TOPIC 00034: Configuring File Indexing for a DataFinder Instance

- bundle_id: `systemlink-server`
- source_path: `configuring-file-indexing-for-searching.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-file-indexing-for-searching.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Index the data in the search areas or in the SystemLink file service to allow you to manually or automatically search for data with Data Navigation, DIAdem, or LabVIEW. In Data Indexing, click DataFinder Instances. Select an instance and click Manage. On the Index tab, use the settings in the follow

### Configuring File Indexing for a DataFinder Instance

Index the data in the search areas or in the SystemLink file service to allow you to
 manually or automatically search for data with Data Navigation, DIAdem, or
 LabVIEW.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Index tab, use the settings in the following
 table to configure your indexing process. 
 Setting
 DescriptionNotify Analysis Automation instances about new or changed
 files*
 Notifies an Analysis Automation instance about new or
 changed data in the data source of a task. This is the
 default when you select a DataFinder instance in
 Analysis Automation as the data
 source for event-driven analysis automation procedures. If
 you disable this checkbox to reduce data traffic on the
 server, Analysis Automation can no
 longer perform the triggered tasks that use this DataFinder
 instance.
 Changes in Search Areas*
 Updates the index when files are new or modified. Note The
 operating system notifies SystemLink about every new or
 modified file. Therefore, you should not use this
 setting if you expect a large amount of new files or
 file changes.
 Indexing Schedule*
 Creates a data indexing schedule.
 Continuous Scan*
 Checks in the specified interval whether data has been
 added or deleted.
 Index Optimization Schedule
 Optimizes the index at the specified times.
 Use Optimized Background Processes
 Optimizes the background processes which the DataFinder
 instance applies to the index. For example, if you have
 deleted a search area or disabled a DataPlugin, the
 DataFinder instance only deletes the associated data from
 the index when computer resources are available.
 Number of Parallel Indexers
 Number of indexers which simultaneously index the data in
 the search areas. By default, a DataFinder instance uses
 four parallel indexers. You can use a maximum of eight
 parallel indexers. Using several parallel indexers can
 considerably impact the speed of your server.
 Index Adaptor
 Configures the index adaptor. Adaptors connect the
 DataFinder instance to a database, where they store the
 index. The connected databases may differ in performance and
 functionality.
 *not available for instances that index the SystemLink file service, like the
 FileIndex instance.
4. Click Apply to accept the settings.

Parent topic:

Preparing Data for Searching

<!--NI_TOPIC bundle=systemlink-server path=configuring-monitoring-processing-raw-data.html language=enus -->
## TOPIC 00035: Configuring the Monitoring and Processing of Raw Data

- bundle_id: `systemlink-server`
- source_path: `configuring-monitoring-processing-raw-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-monitoring-processing-raw-data.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: A Data Preprocessor instance scans the raw data areas to detect new files, file changes, or deleted files, and processes the data according to processing rules. In Data Preparation, click Data Preprocessor Instances. Select an instance and click Manage. On the Monitoring tab, configure scanning and

### Configuring the Monitoring and Processing of Raw Data

A Data Preprocessor instance scans the raw data areas to detect new files, file
 changes, or deleted files, and processes the data according to processing rules.

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Monitoring tab, configure scanning and processing
 with the following options. 
 Setting
 DescriptionChanges in Raw Data Areas
 Scans and processes the data in the raw data areas when
 files are created, modified, or deleted. Note The
 operating system notifies SystemLink about every new,
 modified, or deleted file. Therefore you should not use
 this setting if you expect a very large amount of files
 or file changes.
 File Scan Schedule
 Creates a raw data scanning schedule.
 Continuous Scan
 Checks in regular intervals whether data has been added
 or changed in the raw data area.
 Job Files
 Batch processes specific files or folders.
 Processing Rules
 Specifies the reaction to file changes.
 Timeout per File
 Maximum amount of time, in seconds, for processing a
 file.
 Number of Parallel Requests to the Compute Nodes
 Number of requests that the Data Preprocessor instance
 sends to the compute nodes for execution. The maximum value
 for this setting is 64. The default setting for a new Data
 Preprocessor instance is 4. Incrementing this number leads
 to more throughput and increases processing resource
 utilization on the machine.
 Index Adaptor
 Configures the adaptor. Adaptors connect the Data
 Preprocessor instance with a database, where they store the
 instance data. The connected databases may differ in
 performance and functionality. Note This
 setting only displays if the Data Preprocessor instance
 uses a different database than the standard
 database.

Parent topic:

Configuring a Data Preprocessor Instance

Related tasks:

- Specifying the Reaction to File Changes
- Continuously Scanning Raw Data Areas for New or Deleted Files
- Scanning and Processing Files Manually
- Batch Processing Folders or Files

<!--NI_TOPIC bundle=systemlink-server path=configuring-proxy-settings.html language=enus -->
## TOPIC 00036: Configuring Proxy Settings for SystemLink

- bundle_id: `systemlink-server`
- source_path: `configuring-proxy-settings.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-proxy-settings.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure SystemLink for a network that uses a proxy server to ensure that your systems can access feeds from NI Package Manager. You can only configure proxy settings for Windows systems. Ensure both the server and the client machines have Internet Explorer installed. A proxy sits between a client

### Configuring Proxy Settings for
 SystemLink

Configure SystemLink for a network that uses a proxy server to ensure that your systems
 can access feeds from NI Package Manager.

Internet
 Explorer

A *proxy* sits between a client machine and a server. Instead of the client
 connecting directly to the server, the client sends all requests to the proxy. The proxy
 forwards the requests to the server. The proxy also receives responses for the client.

Using a proxy enhances privacy and improves security. Proxies control what systems can
 access the network. The proxy can also limit the ability of the server to reach outside the
 local network. Configuring the proxy settings allows SystemLink to work within existing
 protections.

1. Clear any existing proxy settings on your system in the following files: 
 C:\Program Files\National Instruments\NI Package
 Manager\Settings\nipkg.ini
 %localappdata%\National Instruments\NI Package
 Manager\nipkg.ini
2. On your SystemLink server, download Sysinternals PSTools and extract the ZIP
 archive.
3. Open the command line utility as an administrator and navigate to the extracted
 folder.
4. Enter one of the following commands: 
 psexec64 -u "nt authority\network service" -i cmd.exe for the
 network service user, which handles Systems Management
 psexec64 -u "nt authority\system" -i cmd.exe for the system
 user, which handles Package Repository 
 A new command prompt opens running as the corresponding
 user.
5. In the new command prompt, enter whoami to verify the
 user.
6. Enter C:\Program Files (x86)\Internet Explorer\iexplore.exe to
 launch Internet Explorer.
7. In Internet Explorer, under Settings, click Internet Options»Connections»LAN Settings.
8. Enable the Use a proxy server for your LAN checkbox and
 enter your proxy server information.
9. Enable the Bypass proxy server for local addresses
 checkbox.
10. If you configured the client to connect to the server using an IP address or
 fully qualified domain name (FQDN), click Advanced and
 add an exception for the hostname for your server.
11. If the command prompt asks for additional proxy credentials, enter
 cmdkey /generic: <proxy-server-ip> /user:<username>
 /pass:<password>.
12. Complete these steps for both the system and the network service user.
13. On each client machine, complete these steps for the system user.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related information:

- Download Sysinternals PSTools

<!--NI_TOPIC bundle=systemlink-server path=configuring-roles-privileges.html language=enus -->
## TOPIC 00037: Configuring a Role and Privileges

- bundle_id: `systemlink-server`
- source_path: `configuring-roles-privileges.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-roles-privileges.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a role and assign privileges to the role to customize how users can interact with each SystemLink application and service. Before you create a role and assign it privileges, create a workspace or use the default workspace. A role is any set of permissions you want to assign to a group of user

### Configuring a Role and Privileges

Create a role and assign privileges to the role to customize how users can interact
 with each SystemLink application and service.

Before you create a role and assign it privileges, create a
 workspace or use the default workspace.

A *role* is any set of permissions you want to assign to a group of users
 or services. There is no limit to how many roles a workspace can contain or how many
 roles a user or service can have. You can use the same role in multiple workspaces.

1. In Access Control, on the Roles tab, click
 Create Role.
2. Enter a name for the role.
3. If you plan to assign this role to services, not users, activate the
 Service role toggle. 
 Use service roles to define which resources an analysis routine can
 access.
4. On the Privileges tab, under Applications and
 services, select the application or service you want to assign
 privileges for. 
 NI recommends selecting the minimum number of privileges that users in a role
 will need to perform their work.
5. Optional: 
 For Tags or Messages, under
 Privilege Specificity, specify prefixes or suffixes
 to restrict which tag or message paths the role can access. 
 The default value is a wildcard character (*), meaning
 this role can access all tag or message data.
6. Check the box for each privilege type you want the role to have. 
 Note Checking Allow
 all privileges grants this role any new privileges that
 future versions of SystemLink will include.
7. Click Create.
8. Repeat steps 3–5 for each application or service this role interacts
 with. 
 It can take up to 5 minutes for privilege changes to take effect.
9. To add another administrator role, click [IMAGE alt='Gear icon' src='GUID-F365AA0A-76E7-445B-BF21-BD366FEDA5D4-a5.png'] and create a server administrator mapping.

After you configure a role, assign users or
 analysis routines in any workspace to the role. You can modify roles at any
 time.

Parent topic:

Managing Access to SystemLink

Related tasks:

- Assigning Users to Roles in a Workspace

Related reference:

- Role-Based Access Control Concepts
- Predefined Roles in SystemLink

<!--NI_TOPIC bundle=systemlink-server path=configuring-systemlink-server-clients.html language=enus -->
## TOPIC 00038: Installing and Configuring SystemLink Server and Clients

- bundle_id: `systemlink-server`
- source_path: `configuring-systemlink-server-clients.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-systemlink-server-clients.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Install and configure SystemLink on a host and one or more targets to begin managing your systems and deploying packages. If you need to run test and measurement systems on an isolated network with no external Internet access, you can still install and use SystemLink Server as long as the managed no

### Installing and Configuring SystemLink Server and Clients

Install and configure SystemLink on a host and one or more targets to begin managing your systems and deploying packages.

If you need to run test and measurement systems on an isolated network with no external
 Internet access, you can still install and use SystemLink Server as long as the managed nodes
 have network access to the server. NI offers product installers on physical media for
 customers who require isolated network installations.

You can also run SystemLink Server in a public or private cloud computing environment such
 as Amazon Web Services (AWS) or Microsoft Azure. In these use cases, you are responsible for
 installing and managing the server instance in the cloud or for contracting a business partner
 to provide this service.

- [SystemLink Quick Installation Guide](installation-guide.html) Install and configure a SystemLink instance with a single-seat license. You can use this instance to begin managing systems and working with data.
- [Purchasing SystemLink Licenses](licensing-systemlink.html) Choose a SystemLink licensing option based on your goals and assign those licenses to your systems.
- [Setting Up a SystemLink Server](setting-up-systemlink-server.html) Install and configure SystemLink Server on your host to begin managing systems and working with data. SystemLink Server includes the SystemLink web application and SystemLink APIs.
- [Licensing and Activating SystemLink Products](licensing-and-activating-systemlink-products.html) License and activate your SystemLink products.
- [Setting Up SystemLink Network Security](setting-up-systemlink-network-security.html) Complete the following steps to ensure your interactions with SystemLink are secure.
- [Connecting a Windows Target to Your SystemLink Server](setting-up-systemlink-client-windows.html) Establish a connection between your SystemLink server and a remote Windows target.
- [Connecting an NI Linux Real-Time Target to Your SystemLink Server](setting-up-systemlink-client-linux.html) Establish a connection between your SystemLink server and an NI Linux Real-Time target.
- [Configuring Proxy Settings for SystemLink](configuring-proxy-settings.html) Configure SystemLink for a network that uses a proxy server to ensure that your systems can access feeds from NI Package Manager .
- [Configuring FileIngestion Storage Options](remote-file-share.html) Configure SystemLink to store files on a remote network drive.
- [Choosing a MongoDB Deployment](choosing-a-mongodb-deployment.html) Most of the SystemLink services use MongoDB as the primary database. You can use MongoDB on the same server hosting SystemLink or set up a remote MongoDB instance.
- [Connecting to a Remote PostgreSQL Database](remote-postgres-databse.html) Configure SystemLink to access a remote PostgreSQL database to enhance scalability and fault tolerance in Test Monitor.

Related concepts:

- Components of a SystemLink Server System

Related tasks:

- Purchasing SystemLink Licenses
- Setting Up a SystemLink Server
- Troubleshooting System Connection Issues

<!--NI_TOPIC bundle=systemlink-server path=configuring-systemlink-to-connect-to-your-openid-connect-provider.html language=enus -->
## TOPIC 00039: Configuring SystemLink to Connect to Your OpenID Connect Provider

- bundle_id: `systemlink-server`
- source_path: `configuring-systemlink-to-connect-to-your-openid-connect-provider.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-systemlink-to-connect-to-your-openid-connect-provider.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create the configuration files SystemLink uses to connect to your OpenID Connect provider. Make a note of your issuer URI. You can find the issuer URI by viewing the issuer property at the OpenID Connect configuration endpoint for your provider. For example, if the URI is https://example.com:9999/v2

### Configuring SystemLink to Connect to Your
 OpenID Connect Provider

Create the configuration files SystemLink uses to connect to your OpenID Connect
 provider.

1. Make a note of your issuer URI. 
 Note You can find the issuer URI
 by viewing the issuer property at the OpenID Connect configuration endpoint
 for your provider. For example, if the URI is
 https://example.com:9999/v2 you can name your file
 example.com%3A9999%2Fv2.conf.
2. Log into the server running SystemLink and navigate to C:\Program
 Files\National Instruments\Shared\Web Server\conf\openidc.
3. Create a file named
 provider-issuer-uri.conf. This file
 is the URL-encoded, fully qualified domain name of the provider.
4. Use the following example to populate the .conf
 file. 
 {
 "scope": "openid email profile",
 "ni-attributes": {
 "displayName": "Log in with PingFederate",
 "iconUri": "/login/assets/pf.png"
 },
 "keys": [
 {
 "p": "...",
 "kty": "RSA",
 "q": "...",
 "d": "...",
 "e": "AQAB",
 "use": "enc",
 "kid": "2020-11-20",
 "qi": "...",
 "dp": "...",
 "dq": "...",
 "n": "..."
 }
 ]
}
 scope – Contains claims you can map to roles within
 SystemLink workspaces. You must include the profile and
 email scopes. These scopes populate the first name,
 last name, and email fields in the SystemLink user preferences. These
 fields come from the given_name,
 family_name, and email claims
 respectively. Consult the documentation for your provider for more
 information about exposing scopes to clients.
 ni-attributes – Determines the text and icon you
 want to show on the SystemLink login page. iconUri is
 relative to C:\Program Files\National Instruments\Shared\Web
 Server\htdocs. Your icon must be 16x16 px.
 keys – Contains the private keys as a JWK Set.
 These keys are for providers that use asymmetric encryption to manage
 the ID token keys. You must register the corresponding public keys with
 the provider. use – Must have a value of
 enc to indicate the key is used for
 encryption.
 kid – Must match the kid property of the
 corresponding public key on the identity provider.Remove this section if the provider uses symmetric encryption or
 no encryption to manage the ID token key.
5. Save and close the file.
6. Create a file named
 provider-issuer-uri.client. NI Web
 Server uses this file to authenticate with the provider.
7. Use the following example to populate the .client
 file. 
 {
 "client_id": "slserver",
 "client_secret": "4vFm89u07xaredactedredactedredactede2tjtsEGQhlLreLVjcyLA0"
}You can obtain values for client_id and
 client_secret from your provider. Depending on the
 provider, client_id might be user defined.
8. Save and close the file.
9. Use the following curl command to create the
 provider-issuer-uri.provider
 file. This file tells SystemLink which endpoints the provider exposes during a
 login attempt. 
 curl
 https://provider-issuer-uri/.well-known/openid-configuration
 -o provider-issuer-uri.providerprovider-issuer-uri represents the
 URL-encoded, fully qualified domain name of your provider.
10. Save the resulting .provider file in C:\Program
 Files\National Instruments\Shared\Web Server\conf\openidc.
11. If you have multiple OpenID Connect providers, create a
 .conf, .client, and
 .provider file for each provider. The user ID in
 SystemLink must be unique across providers. This ID uses the format
 [sub_claim]@issuer. You can see the ID SystemLink associates with a user in the
 user details in SystemLink Access Control.
12. If you require a proxy, create a file named
 60_openidc_proxy.conf at C:\Program
 Files\National Instruments\Shared\Web Server\conf\conf.d. Use the
 following example to populate the file and replace
 host and
 port with the address of the
 proxy. 
 <IfDefine AUTH_OIDC_ENABLED>
 OIDCOutgoingProxy host:port
</IfDefine>
13. Restart NI Web Server to apply the changes.

Parent topic:

Managing Access with OpenID Connect

Related information:

- Setting up OpenID Connect in SystemLink with Azure Active Directory
- PingFederate Server
- Using OAuth 2.0 to Access Google APIs
- okta Find your application credentials
- Migrate applications to the Microsoft Authentication Library (MSAL)

<!--NI_TOPIC bundle=systemlink-server path=configuring-the-systemlink-username-for-openid-connect-users.html language=enus -->
## TOPIC 00040: Configuring the SystemLink Username for OpenID Connect Users

- bundle_id: `systemlink-server`
- source_path: `configuring-the-systemlink-username-for-openid-connect-users.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-the-systemlink-username-for-openid-connect-users.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Assign a more readable username to OpenID Connect users. Before you begin, follow the steps in Viewing Claims for OpenID Connect Users to obtain user claims. SystemLink creates a unique username for each user using OpenID Connect claims. SystemLink uses the sub and iss claims by default to ensure th

### Configuring the SystemLink Username for OpenID
 Connect Users

Assign a more readable username to OpenID Connect users.

Viewing Claims
 for OpenID Connect Users

Notice

1. Log into the server running SystemLink, navigate to C:\Program
 Files\National Instruments\Shared\Web Server\conf\defines.d\, and
 open 50_mod_auth_openidc-defines.conf in a text
 editor.
2. Change the configuration UnDefine AUTH_OIDC_USER_CLAIM
 to Define AUTH_OIDC_USER_CLAIM and append the name of the
 claim you want SystemLink to use as the username. Your file should look similar
 to the following example. 
 Note The username must be unique across all enabled providers including OpenID
 Connect, LDAP, Windows, and Web Server.
 #
# Defined OpenID-Connect configuration for the Windows Apache installation.
#

# The name of the JSON map containing metadata about each identity provider.
Define AUTH_OIDC_ATTRIBUTES_KEY ni-attributes

# CA bundle to use when making requests to an identity provider.
Define AUTH_OIDC_BUNDLE ../nicurl/ca-bundle.crt

# Override the OIDCCacheShmEntrySizeMax to mitigate claim size issues
Define AUTH_OIDC_CACHE_ENTRY_SIZE 66065

# Path to OIDC provider configuration.
Define AUTH_OIDC_PROVIDER_DIR ${HTCONF_PATH}/openidc

# The location to redirect when performing an OpenID-Connect login.
Define AUTH_OIDC_REDIRECT_URI /login/openidc-redirect

#
# User-editable variables.
#

# Whether OIDC is enabled.
Define AUTH_OIDC_ENABLED

# The claim that will be used as the SystemLink user name.
# If not defined, a combination of the sub and iss claims will be used.
Define AUTH_OIDC_USER_CLAIM email

# When enabled, /login/openidc-redirect?info=json and
# /login/openidc-redirect?info=html will return the claims for the currently
# logged in user.
UnDefine AUTH_OIDC_ENABLE_CLAIM_INFO
3. Save the file and restart NI Web Server.

Parent topic:

Managing Access with OpenID Connect

Related tasks:

- Viewing Claims for OpenID Connect Users

<!--NI_TOPIC bundle=systemlink-server path=configuring-user-account-settings.html language=enus -->
## TOPIC 00041: Viewing and Editing User Account Settings

- bundle_id: `systemlink-server`
- source_path: `configuring-user-account-settings.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-user-account-settings.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the SystemLink web interface to complete tasks such as modifying the language settings, picking an application color theme, and viewing account information. In the top-right corner, click User profile icon. Welcome, <User Name> Account . In the Edit account slide-out, achieve the following goals

### Viewing and Editing User Account
 Settings

Use the SystemLink web interface to complete tasks such as modifying the language
 settings, picking an application color theme, and viewing account information.

1. In the top-right corner, click [IMAGE alt='User profile icon.' src='GUID-6887DBEC-A1FD-4B61-8AD0-69B8BC5F40D6-a5.png']Welcome, <User Name>»Account.
2. In the Edit account slide-out, achieve the following goals. 
 Goal
 DescriptionSet the language
 Click the Language drop-down and select from the
 following languages:Note By default, the language
 selector matches the langauge of the browser.English—English language setting
 Français—French language setting
 Deutsch—German language setting
 日本語—Japanese language setting
 中文—Chinese language setting
 The chosen language determines the decimal separator type and the locale to
 use for dates.
 Set the color theme
 Click the Theme drop-down and select from the
 following themes:Light—A theme with light background and UI
 elements and dark text
 Dark—A theme with dark background and UI elements
 and light text
 Device default—SystemLink matches the default
 theme of the device or browserNote SystemLink remembers the theme preference
 across browsers. Your chosen theme applies wherever you log in.
 View information on your user account
 View the following account information:Note You cannot
 edit these properties. Your organization provides this information through
 an identity management system such as Microsoft Azure AD, Okta, or Google
 Workspace.First name—The first name of the user
 Last name—The last name of the user
 Username—The unique identifier SystemLink uses
 for your account
 Email—The email address SystemLink sends
 notifications
 Phone—The phone number of the userNote If any of the account information is
 incorrect, contact your server administrator or IT support team to request
 an update.
3. Click OK.

<!--NI_TOPIC bundle=systemlink-server path=configuring-your-openid-connect-provider-to-connect-to-systemlink.html language=enus -->
## TOPIC 00042: Configuring Your OpenID Connect Provider to Connect to SystemLink

- bundle_id: `systemlink-server`
- source_path: `configuring-your-openid-connect-provider-to-connect-to-systemlink.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/configuring-your-openid-connect-provider-to-connect-to-systemlink.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Specify the redirect URL that the client configuration for your provider will use at login. Locate the settings for your OpenID Connect provider. Use the following format to configure the login redirect URL for your provider. protocol://systemlink-dns:port/login/openidc-redirectWhere protocol is htt

### Configuring Your OpenID Connect Provider to
 Connect to SystemLink

Specify the redirect URL that the client configuration for your provider will use at
 login.

1. Locate the settings for your OpenID Connect provider.
2. Use the following format to configure the login redirect URL for your
 provider. 
 protocol://systemlink-dns:port/login/openidc-redirectWhereprotocol is
 https:// or http://.
 systemlink-dns is the DNS name of
 the SystemLink server.
 port is the port the web server is
 listening on. You can omit the port and the leading colon if you are
 using port 80 or 443.Note NI recommends the DNS
 name in the redirect URI match the preferred hostname set in NI Web
 Server Configuration on the SystemLink server.
3. Use the following format to configure the front channel logout URL for your
 provider. 
 protocol://systemlink-dns:port/login/openidc-redirect?logout=get

Parent topic:

Managing Access with OpenID Connect

Related information:

- Setting up OpenID Connect in SystemLink with Azure Active Directory
- PingFederate Server
- Using OAuth 2.0 for Web Server Applications
- okta Sign users in to your web app using the redirect model

<!--NI_TOPIC bundle=systemlink-server path=connecting-data-navigator-to-data-index.html language=enus -->
## TOPIC 00043: Connecting Data Navigation to a DataFinder Instance

- bundle_id: `systemlink-server`
- source_path: `connecting-data-navigator-to-data-index.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/connecting-data-navigator-to-data-index.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable web access for a DataFinder or Federation instance to allow Data Navigation to access the shared data. In Data Indexing, click DataFinder Instances or Federation Instances. Select an instance and click Manage. Click ConnectRemote AccessWeb Access. Enable Allow access to DataFinder through web

### Connecting Data Navigation to a DataFinder Instance

Enable web access for a DataFinder or Federation instance to allow Data Navigation to
 access the shared data.

1. In Data Indexing, click DataFinder
 Instances or Federation Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. Click [IMAGE alt='image' src='GUID-A2DAEE93-CE77-45A0-ABEE-9B9F2BBACA6F-a5.png']»Connect»Remote Access»Web Access.
4. Enable Allow access to DataFinder through web
 connections to allow Data Navigation to access the shared data
 of the DataFinder instance.
5. Select 
 Stop if the instance is running.
6. Click Apply to accept the settings.
7. In the breadcrumbs ribbon, click DataFinders or Federation to return to the
 instance overview. Select your DataFinder instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Start to start the DataFinder instance.
8. Click [IMAGE alt='image' src='GUID-37C82BEA-D9B2-4525-A84A-E93F091DE43E-a5.svg'] and open Data
 Navigation.
9. On the Instance Overview tab, select the DataFinder
 instance you enabled and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect to display the shared data of the instance.

You can now retrieve data from the data stores indexed by the
 DataFinder or Federation instance.

Parent topic:

Configuring the File Export for Data Navigation

Related tasks:

- Retrieving Data from Your Data Stores

<!--NI_TOPIC bundle=systemlink-server path=connecting-labview-and-diadem.html language=enus -->
## TOPIC 00044: Connecting to LabVIEW and DIAdem

- bundle_id: `systemlink-server`
- source_path: `connecting-labview-and-diadem.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/connecting-labview-and-diadem.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Exchange data between clients like LabVIEW or DIAdem and SystemLink Server using SystemLink data services. Access these data services through the Data Communication palette in LabVIEW and LabVIEW NXG, or the DataFinder connection in DIAdem NAVIGATOR.

### Connecting to LabVIEW and DIAdem

Exchange data between clients like LabVIEW or DIAdem and SystemLink Server using
 SystemLink data services. Access these data services through the Data Communication
 palette in LabVIEW and LabVIEW NXG, or the DataFinder connection in DIAdem NAVIGATOR.

- [Finding Data from DIAdem and LabVIEW Clients](connecting-with-data-index.html) Connect client software, such as DIAdem or LabVIEW, to a DataFinder instance on SystemLink Server to browse and search in the data of this instance. To do so, save the connection parameters in a client configuration file ( .urf ) and enable the connection on the client computer.
- [Transferring Files from Disk to the Server](transferring-files-from-disk-to-server.html) Send files stored on disk from a client to the server to save, process, or enable access for others.
- [Transferring Files from Memory to the Server](transferring-files-from-memory-to-server.html) Send files stored in memory from a client to the server to save, process, or enable access for others.
- [Acquiring Test Results](acquiring-test-results.html) Create test steps to record your tests and measurement data.
- [Sending Messages Between Systems](transfer-messages.html) Use messages to send commands, status updates, or data, such as JSON, between systems and applications.
- [Reading Measurement Data from TDMS Files](reading-tdm-data.html) Query TDMS files to read measurement data.
- [Tracking Asset Utilization with LabVIEW](tracking-asset-utilization.html) Record utilization information about the assets performing test and measurement tasks.
- [Storing Historical Tag Values](storing-historical-tag-values.html) Configure how long or how many historical tag values you store on your SystemLink server account.
- [Generating Custom Alarms](building-alarms-to-manage-systems-assets-tests.html) Build alarms to notify you when an issue occurs in your system.

Parent topic:

Sharing Data

<!--NI_TOPIC bundle=systemlink-server path=connecting-to-a-remote-mongo-database-with-mongodb-atlas.html language=enus -->
## TOPIC 00045: Connecting to a Remote Mongo Database with MongoDB Atlas

- bundle_id: `systemlink-server`
- source_path: `connecting-to-a-remote-mongo-database-with-mongodb-atlas.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/connecting-to-a-remote-mongo-database-with-mongodb-atlas.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect to a MongoDB Atlas account for simpler database setup and administration compared to other deployments. Before you begin ensure you meet the following requirements. A server running SystemLink 2021 R1 or later A MongoDB Atlas accountDue to memory constraints on the Atlas free tier, you must

### Connecting to a Remote Mongo Database with
 MongoDB Atlas

Connect to a MongoDB Atlas account for simpler database setup and administration compared
 to other deployments.

- A server running SystemLink 2021 R1 or later
- A MongoDB Atlas account Note Due to memory constraints on the Atlas free tier,
 you must have a paid Atlas account to connect to SystemLink.
- A user with the readWriteAnyDatabase role and the createCollection
 privilege Note The readWrite role does not include the createCollection
 privilege.

1. Refer to *Get Started with Atlas* to set up an Atlas cluster.
2. Refer to *Get Connection String* to obtain a connection
 string. 
 Note In the sample connection string Atlas provides, replace the instance of
 myFirstDatabase with admin. For
 example, you would update
 mongodb+srv://<username>:<password>@<cluster>/myFirstDatabase?retryWrites=true&w=majority
 to
 mongodb+srv://<username>:<password>@<cluster>/admin?retryWrites=true&w=majority.

Parent topic:

Choosing a MongoDB Deployment

Related concepts:

- MongoDB Support Limitations
- Connection String Format

Related information:

- Get Started with Atlas
- Get Connection String
- Connection Strings

<!--NI_TOPIC bundle=systemlink-server path=connecting-to-a-remote-mongo-database-with-replica-sets.html language=enus -->
## TOPIC 00046: Connecting to a Remote Mongo Database with Replica Sets

- bundle_id: `systemlink-server`
- source_path: `connecting-to-a-remote-mongo-database-with-replica-sets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/connecting-to-a-remote-mongo-database-with-replica-sets.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect to a remote MongoDB instance with replica sets to create redundancy in your database and mitigate data loss. Before you begin ensure you meet the following requirements. A server running SystemLink 2021 R1 or later Multiple servers hosting a MongoDB replica set A user with the readWriteAnyDa

### Connecting to a Remote Mongo Database with
 Replica Sets

Connect to a remote MongoDB instance with replica sets to create redundancy in your
 database and mitigate data loss.

- A server running SystemLink 2021 R1 or later
- Multiple servers hosting a MongoDB replica set
- A user with the readWriteAnyDatabase role and the createCollection
 privilege Note The readWrite role does not include the createCollection
 privilege.

1. Log into the desktop of the SystemLink server with administrator
 privileges.
2. Launch the NI SystemLink Server Configuration and navigate to the
 NoSqlDatabase tab.
3. Enable Connect to an externally managed NoSqlDatabase
 server. 
 Note NI recommends securing communications between your SystemLink server and
 MongoDB instance with TLS.
4. Enable Use a custom connection string.
5. Enter a connection string that adheres to the MongoDB standard connection
 string format. Refer to *Connection String Format* for more
 information.
6. Click Test Connection to ensure SystemLink can connect
 to the MongoDB instance.
7. Click Apply to restart SystemLink service manager and
 connect to the MongoDB instance.

Parent topic:

Choosing a MongoDB Deployment

Related concepts:

- MongoDB Support Limitations
- Connection String Format

Related information:

- MongoDB TLS
- Connection Strings
- MongoDB Compass

<!--NI_TOPIC bundle=systemlink-server path=connecting-to-an-opc-server.html language=enus -->
## TOPIC 00047: Integrating with an OPC UA Server

- bundle_id: `systemlink-server`
- source_path: `connecting-to-an-opc-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/connecting-to-an-opc-server.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect to an OPC UA server to leverage, or mirror, OPC UA variables as tag values within the default workspace of your SystemLink system. To integrate with an OPC UA server, you must install SystemLink OPC UA Connector. In the SystemLink web application, under Connectors, click OPC UA. Click Create

### Integrating with an OPC UA Server

Connect to an OPC UA server to leverage, or mirror, OPC UA variables as tag values
 within the default workspace of your SystemLink system.

To integrate with an OPC UA server, you must install SystemLink OPC UA Connector.

1. In the SystemLink web application, under Connectors, click
 OPC UA.
2. Click 
 Create.
3. Follow the prompts to create and configure a session for connecting to the OPC UA server.
4. Click 
 Connect to accept the automatically generated security certificate and begin the session. 
 Note To manually add a security certificate, click 
 Manage Certificates.

[IMAGE alt='image' src='GUID-261CCDAD-EA42-441A-A410-BEC277311E0C-a5.png']

Your SystemLink Server stays connected to the OPC UA server until you pause or delete
 the session.

Parent topic:

Sharing Data

Related tasks:

- Monitoring and Visualizing Data with Tags
- Mapping Tags to OPC UA Variables

<!--NI_TOPIC bundle=systemlink-server path=connecting-with-data-index.html language=enus -->
## TOPIC 00048: Finding Data from DIAdem and LabVIEW Clients

- bundle_id: `systemlink-server`
- source_path: `connecting-with-data-index.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/connecting-with-data-index.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect client software, such as DIAdem or LabVIEW, to a DataFinder instance on SystemLink Server to browse and search in the data of this instance. To do so, save the connection parameters in a client configuration file ( .urf ) and enable the connection on the client computer. In Data Indexing, cl

### Finding Data from DIAdem and LabVIEW
 Clients

Connect client software, such as DIAdem or LabVIEW, to a DataFinder instance on
 SystemLink Server to browse and search in the data of this instance. To do so, save the
 connection parameters in a client configuration file ( .urf ) and enable the connection on
 the client computer.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect»Export Client Configuration.
3. Specify the name of the configuration file.
4. Use the following table to select the connection parameters. 
 Connection Parameters
 DescriptionUse computer name + add full domain name
 Saves the name of the computer on which the DataFinder instance is running and the complete domain name in the configuration file, for example Computer@Domain. This default setting is suitable for standard client-server constellations. Select this setting if the client is in a different domain than the computer on which the DataFinder instance is running.
 Use computer name
 Saves the name of the computer, on which the DataFinder instance is running, in the configuration file. This setting only works if the client is in the same domain as the computer on which the DataFinder instance is running.
 Use IP address
 Saves the IP address of the computer, on which the DataFinder instance is running, in the configuration file.
5. Specify the timeouts.
6. Use the following table to specify the DataPlugin settings. 
 DataPlugins
 DescriptionInclude DataPlugins in client configuration
 Encrypts and saves all VBS DataPlugins in the configuration file. This allows the client to load the corresponding data from the search areas of the DataFinder instance. The installation of the configuration file on the client overwrites earlier DataPlugin versions with the DataPlugins from the SystemLink server.
 Synchronize DataPlugins automatically
 When you establish the DataFinder instance connection in the client software, the client software overwrites the existing VBS DataPlugins on the client with the DataPlugins from the SystemLink server by default. You can disable this setting in the client software.
 Enforce synchronization
 When you establish the DataFinder instance connection in the client software, the client software overwrites the existing VBS DataPlugins on the client with the DataPlugins from the SystemLink server. You cannot disable this setting in the client software.
7. Click 
 Export and save the configuration file on the client computer.
8. Register the DataFinder instance by double-clicking the configuration file
 (.urf).
9. Connect to the DataFinder instance from client software such as DIAdem or
 LabVIEW. 
 You can now browse and search in the search areas of the DataFinder instance from DIAdem
 with My DataFinder or from LabVIEW using the VIs on the DataFinder palette.

Parent topic:

Connecting to LabVIEW and DIAdem

<!--NI_TOPIC bundle=systemlink-server path=connection-string-format.html language=enus -->
## TOPIC 00049: Connection String Format

- bundle_id: `systemlink-server`
- source_path: `connection-string-format.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/connection-string-format.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following guidelines when formatting your connection string to connect to a MongoDB instance. The query parameter tls= is not supported. Use ssl= to achieve the same degree of security. Use uppercase when URL escaping characters. For example, %2F. Consider using MongoDB Compass to conne

### Connection String Format

Consider the following guidelines when formatting your connection string to connect to a
 MongoDB instance.

- The query parameter tls= is not supported. Use
 ssl= to achieve the same degree of security.
- Use uppercase when URL escaping characters. For example,
 %2F .
- Consider using MongoDB Compass to connect to your replica set to help construct a
 valid connection string and verify the configuration.
- Use the mongodb+srv:// URI format to avoid having to create new
 connection strings if the servers in the replica set change.

#### Example Connection String

```text
mongodb://myusername:<password>@
ec2-123-123-12.compute-1.amazonaws.com27017,
ec2-234-234-23.compute-1.amazonaws.com:27017,
ec2-456-456-45.compute-1.amazonaws.com:27017/
?authSource=admin
&replicaSet=rs0
&readPreference=primary
&ssl=true
```

Parent topic:

Choosing a MongoDB Deployment

Related information:

- Get Connection String
- Connection Strings

<!--NI_TOPIC bundle=systemlink-server path=continuously-scanning-raw-data-areas.html language=enus -->
## TOPIC 00050: Continuously Scanning Raw Data Areas for New or Deleted Files

- bundle_id: `systemlink-server`
- source_path: `continuously-scanning-raw-data-areas.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/continuously-scanning-raw-data-areas.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Scan raw data areas in short intervals to detect whether files were added or deleted. The continuous scan is fast because it does not scan for modified files. In Data Preparation, click Data Preprocessor Instances. Select an instance and click Manage. On the Monitoring tab, click Continuous Scan. En

### Continuously Scanning Raw Data Areas for New
 or Deleted Files

Scan raw data areas in short intervals to detect whether files were added or deleted.
 The continuous scan is fast because it does not scan for modified files.

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Monitoring tab, click Continuous
 Scan.
4. Enable the continuous scan, enter the scan interval, and click 
 OK.
5. Click Apply to accept the settings.

Parent topic:

Configuring a Data Preprocessor Instance

<!--NI_TOPIC bundle=systemlink-server path=creating-a-new-jupyter-notebook.html language=enus -->
## TOPIC 00051: Creating a New Jupyter Notebook

- bundle_id: `systemlink-server`
- source_path: `creating-a-new-jupyter-notebook.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-a-new-jupyter-notebook.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a new Jupyter notebook (.ipynb) in JupyterHub to develop code for visualizing, analyzing, and processing data from your tests, measurements, assets, and more. Before you create a Jupyter notebook, complete the following tasks:Install Jupyter Notebooks for SystemLink from NI Package Manager to

### Creating a New Jupyter Notebook

Create a new Jupyter notebook (.ipynb) in JupyterHub to
 develop code for visualizing, analyzing, and processing data from your tests,
 measurements, assets, and more.

- Install Jupyter Notebooks for SystemLink from NI Package Manager to access
 predefined Jupyter notebooks that can leverage SystemLink Python APIs.
- Append /niapis/python/index.html to your SystemLink application URL to
 access the Python APIs.
- Learn about the user interface and structure of a Jupyter notebook.
- Install Python libraries you want to use to enhance your data analysis and processing. NI
 recommends using the Python Package Index (PyPI) to obtain packages.
- Learn about the built-in magic commands that the IPython kernel enables.

1. In the SystemLink web application, click Jupyter.
2. Under Notebook, click Python
 3. 
 A Jupyter notebook launches and starts a kernel to run Python in the
 notebook.
3. Rename the notebook to describe the type of report the notebook executes.
4. In a code cell, import the Python modules, libraries, and widgets for your interactive
 notebook. 
 For example, you can implement code to import Pandas and Scrapbook for the
 following goals: To build and to handle dataframes (Pandas).
 To execute a notebook (Scrapbook).
 To capture notebook results (Scrapbook).import copy
import datetime
import dateutil.parser
import pandas as pd
import scrapbook as sb
from dateutil import tz
5. Use one of the SystemLink Python APIs to access the data you want to visualize,
 analyze, or process. 
 To access data from the SystemLink Test Monitor service, use the following
 command.from systemlink.clientconfig import get_configuration
from systemlink.clients.nitestmonitor import *
6. Establish a connection to your SystemLink server. 
 To connect a Test Monitor client to the server, use the following command.
 http_client_config = get_configuration(route_name='nitestmonitor')
7. Define the parameters and metadata for the notebook.
  1. In a code cell, define the parameters. 
 You can implement code to accomplish the following goals: Filter your test results by a specific time range.
 Group your test results by the day the test system acquired the result.filter = 'startedWithin <= "30.0:0:0"'
group_by = 'Day'
  2. On the right sidebar, open the Property Inspector
 pane.
  3. In the Cell Metadata code block, add the parameters, the
 parameter default values, and the outputs. 
 To add this information, you can implement the following
 code:"papermill": {
 "parameters": {
 "group_by": "Day",
 "results_filter": "startedWithin <= \"30.0:0:0\"",
 }
 },
 "systemlink": {
 "namespaces": [
 "ni-testmanagement"
 ],
 "outputs": [
 {
 "display_name": "This will show in dashboard output selector",
 "id": "data_frame_output",
 "type": "data_frame"
 },
 {
 "display_name": "This will show in dashboard output selector",
 "id": "scalar_output",
 "type": "scalar"
 }
 ],
 "parameters": [
 {
 "display_name": "Group By",
 "id": "group_by",
 "options": [
 "Day",
 "System",
 "Test Program",
 "Operator",
 "Product"
 ],
 "type": "string"
 },
 {
 "default_display": {
 "startedWithin": {
 "unit": "DAYS",
 "value": 30
 }
 },
 "display_name": "Results Filter",
 "id": "results_filter",
 "type": "test_monitor_result_query"
 },
 ],
 "version": 2
 },
 "tags": [
 "parameters"
 ]
}
  4. For namespaces, enter one or more of the following
 namespaces depending on where you want to view your report: 
 Namespace
 Report display locationni-assetmanager
 Asset Manager
 ni-testmanagement
 Test Monitor
 Any namespace you define
 Any other client that uses namespaces to query
 notebooks
  5. For version, enter one of the following version
 numbers depending on how you want to use your notebook: 
 Goal
 VersionYou want to view your data in Test Insights under Reports.
 You are customizing a notebook that is installed with a previous
 version of SystemLink.
 1
 You want to return multiple outputs with one
 notebook.
 You want to use a scalar output type.
 You want to see your data in a dashboard.
 2
8. Query a SystemLink data service for the data you want to visualize, analyze, or
 process. 
 To query the Test Monitor service for test results in ascending order, you can use
 the following code:
 results_api = ResultsApi(api_client=ApiClient(http_client_config))
query = ResultsAdvancedQuery(filter=filter, order_by=[ResultSortDefinitionObject(field=ResultField.STARTED_AT)])
query_response = await results_api.query_results_v2(post_body=query)
results = query_response.results

results_list = [result.to_dict() for result in results]
9. Format Pandas dataframe data based on how you want to group the data returned from the
 query. 
 To group test results by their status, you can use the following
 code:group_names = []
for result in results_list:
 if grouping in result:
 group_names.append(result[grouping])

formatted_results = {
 'id': [result['id'] for result in results_list],
 'status': [result['status']['status_type'] for result in results_list],
 grouping: group_names
}

df_results = pd.DataFrame.from_dict(formatted_results)
10. Configure how you want to visualize, analyze, or process the data. 
 The following examples are some of the ways you can configure the data.
  - Filter out results you do not want to include in the report.
  - Convert timestamps.
  - Compute data within a timeframe.
  - Group data in a specific way.
11. Convert the Pandas dataframe into the output format of a SystemLink report. 
 To convert the Pandas dataframe, you can use the following
 code:result.append({
 'type': 'data_frame',
 'id': 'data_frame_output', 
 data': [{
 'format': 'XY',
 'x': ['2018-11-17T00:00:00', '2018-11-18T00:00:00', ...],
 'y': [94.0, 89.9, ...]
 }],
 'config': {
 'title': 'Title',
 'graph': {
 'axis_labels': ['x-axis-label', 'y-axis-label'],
 'tick_labels': [{'x': 0, 'label': 'tick label 0', ... }],
 'orientation': 'VERTICAL',
 'plot_style': ['SCATTER'],
 'plot_color': ['blue']
 }
 }
}) 
 Tip To ensure Test Monitor
 supports the dataframe output, verify the value of the ID (data_frame_output). The value must be correct in the cell and in the Code
 Metadata for the parameter code cell. For more information, refer to the previous step
 7.
 Note If you use the V2 report format in a
 Jupyter notebook, you can only visualize the report results on a dashboard.
12. Add a new scalar output. 
 To add a scalar output, you can use the following code:
 result.append({
 'type': 'scalar',
 'id': 'scalar_output',
 'config': {
 'title': 'Scalar Output Title'
 },
 'value': 3
}) 
 Note For more information on adding a
 scalar output, refer to the SystemLink examples repository in GitHub.
13. Record results with Scrapbook. 
 To parse the SystemLink web application for results, you can use the following
 code.sb.glue('result', result)
14. Add a new cell in the notebook.
15. On the toolbar, choose Markdown from the dropdown menu
 to add documentation about your code to the notebook.
16. On the menu bar, select Run»All Cells to verify the notebook correctly returns and processes data. 
 If the notebook returns an error, add import pdb;
 pdb.set_trace() to the code cell with the error. Adding this code activates the
 built-in Python debugger.
17. Click Save.
18. Optional: 
 To run your notebook at a scheduled time, create an Analysis Automation procedure and
 add a scheduled task.

Sharing a Jupyter Notebook

Parent topic:

Reporting Data with Jupyter Notebooks

Related tasks:

- Installing Additional Python Modules
- Adding or Editing Tasks for Analysis Automation Procedures

Related information:

- Python API Reference
- Jupyter User Interface
- Structure of a Notebook Document
- PyPI
- Built-In Magic Commands
- SystemLink Examples Repository

<!--NI_TOPIC bundle=systemlink-server path=creating-a-workspace.html language=enus -->
## TOPIC 00052: Creating a Workspace

- bundle_id: `systemlink-server`
- source_path: `creating-a-workspace.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-a-workspace.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a workspace to control which systems and data different types of users can interact with. Creating a workspace requires a SystemLink Advanced Server license. Workspaces limit user access to a particular collection of systems and the data those systems produce. When you add a system to a works

### Creating a Workspace

Create a workspace to control which systems and data different types of users can
 interact with.

Creating a workspace requires a SystemLink Advanced Server
 license.

Workspaces

automatic data encapsulation

1. In the SystemLink web application, click Access Control.
2. In the Workspaces tab, click Create
 Workspace.
3. Enter a name for the workspace and click OK.
4. Optional: 
 Repeat these steps to create as many workspaces as you need to organize your
 resources and reflect your organizational structure.

After you create a workspace,
 specify who can access it by connecting user attributes to roles. When using the
 SystemLink Web Application and SystemLink REST APIs, a user must be a member of a
 workspace to access the systems and data within the workspace.

Parent topic:

Managing Access to SystemLink

Related tasks:

- Configuring a Role and Privileges
- Assigning Users to Roles in a Workspace

Related reference:

- Role-Based Access Control Concepts

<!--NI_TOPIC bundle=systemlink-server path=creating-analysis-automation-procedures.html language=enus -->
## TOPIC 00053: Creating Analysis Automation Procedures in DIAdem

- bundle_id: `systemlink-server`
- source_path: `creating-analysis-automation-procedures.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-analysis-automation-procedures.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create analysis automation procedures in DIAdem to perform recurring analyses with similar data in Analysis Automation, and export the results as a PDF or graphics file. Analysis automation procedures contain the analysis script, the parameter definition, and the search query for the data you want t

### Creating Analysis Automation Procedures in DIAdem

Create analysis automation procedures in DIAdem to perform recurring analyses with
 similar data in Analysis Automation, and export the results as a PDF or graphics file.
 Analysis automation procedures contain the analysis script, the parameter definition, and
 the search query for the data you want to analyze.

1. Open 
 DIAdem SCRIPT.
2. Select 
 Settings»SystemLink TDM»Analysis Automation Procedure.
3. Click 
 New Analysis Automation Procedure.
4. Create the new analysis automation procedure:
  1. Enter a name, description, and author of the new procedure.
  2. Choose Python or DIAdem
 (VBS) as your programming
 Environment.
  3. Click OK.
5. Define the data for analysis on the 
 Search Query tab.
6. Check 
 Data filter enabled to define the search query. For example, make the following settings to limit the analysis to TDM files: 
 Level
 Property
 ValueFile
 DataPlugin name
 TDM
7. Use the Parameter Definition tab to define the
 parameters and initialization values. You can still change the value of the
 parameters when defining the task in Analysis Automation.
 Use the Context object in the analysis script to access the
 parameters. Refer to the DIAdem help Programming Reference»Object-Oriented Script Interface»SystemLink for more information about which objects to use from the
 SystemLink API.
8. Select the 
 Analysis Script tab to edit the analysis script and add more files to the analysis automation procedure configuration.
9. Specify the 
 Evaluation mode. 
 Note The setting 
 Parallel evaluation: Each retrieved element is processed individually is only available if you have enabled the data filter on the 
 Search Query tab.
10. Select the main.vbsa or the main.py and click
 Edit Selected File.
11. In the configuration dialog box, click [IMAGE alt='image' src='GUID-10C22F32-9C8C-4D29-BA7D-95E9B93EBFE1-a5.png'] to continue
 configuring the analysis automation procedure.
12. Optional: 
 Click Add File to Analysis Automation Procedure if you
 require additional files in the analysis script.
13. Select Save Analysis Automation Procedure As. The
 analysis automation procedure has the file extension
 .anp.

Procedures

Analysis
 Automation

Parent topic:

Analyzing Data

Related tasks:

- Adding Analysis Automation Procedures

<!--NI_TOPIC bundle=systemlink-server path=creating-anp-with-jupyter.html language=enus -->
## TOPIC 00054: Creating, Editing, Testing, and Uploading Analysis Procedures in Jupyter

- bundle_id: `systemlink-server`
- source_path: `creating-anp-with-jupyter.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-anp-with-jupyter.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create, edit, or test analysis procedures in Jupyter and upload them to the procedures library in Analysis Automation. Analysis procedures define how SystemLink executes your automated data analyses and presents the results. A procedure includes the analysis notebook, execution parameters, and the s

### Creating, Editing, Testing, and Uploading
 Analysis Procedures in Jupyter

Create, edit, or test analysis procedures in Jupyter and upload them to the procedures
 library in Analysis Automation. Analysis procedures define how SystemLink executes your
 automated data analyses and presents the results.

A procedure includes the analysis
 notebook, execution parameters, and the search query for the data you want to
 analyze.

1. Click [IMAGE alt='image' src='GUID-37C82BEA-D9B2-4525-A84A-E93F091DE43E-a5.svg']»Utilities»Jupyter to open the Jupyter environment for SystemLink. 
 If Jupyter is not installed, refer to *Creating a New Jupyter Notebook* to
 find out how to install Jupyter.
2. On the [IMAGE alt='image' src='GUID-6E170FBF-9384-4CCB-9AB0-866400BEDB07-a5.svg'] tab, click
 [IMAGE alt='image' src='GUID-240AE4D6-DBF9-477F-B7B2-CE427637128A-a5.svg'] to add a
 new procedure or [IMAGE alt='image' src='GUID-E22207D8-74A5-447D-8D3C-E919D8FBD0F0-a5.svg']
 to edit an existing procedure.
3. Create or edit the analysis notebook in the Jupyter editor and specify the analyses you
 want to run on your data. Refer to the Analysis Automation notebook for a basic
 example.
4. On the Edit Procedure tab, specify the following
 information:
  1. Enter a name and description for the procedure.
  2. Choose a Workspace to define the users that can interact
 with the procedure.
  3. In the dropdown menu, choose a Search Query you saved in
 Data Navigation. 
 The query defines the data you want to analyze with the analysis notebook.
  4. Select the Execution Mode. 
 Execution Mode
 ResultComparative
 Runs the analysis notebook on all data elements the search query
 retrieves and outputs the results in one report. This allows you to compare the
 data at a glance.Parallel
 Runs the analysis notebook on each data element the search query
 retrieves and outputs the results in a separate report for each data
 element.
  5. To export the notebook to the file service, switch the toggle to Export
 Report and choose HTML or
 PDF as the export format. If you want to export results only,
 switch the toggle to Exclude Code.
  6. Click [IMAGE alt='image' src='GUID-D5A7C916-A93F-4A08-BB71-3DF56CFC3740-a5.png'] to open a new tab
 to test the analysis procedure. 
 Choose a Data Source.
 Choose a Search Query.
 Click Start. 
 Results are displayed in the same tab with errors, if any.
5. Click [IMAGE alt='image' src='GUID-E22207D8-74A5-447D-8D3C-E919D8FBD0F0-a5.svg']. Click
 Save. 
 The procedure uploads to Analysis Automation.
6. In the dialog box that opens, you can either click Close to
 close the dialog box or click the link to Analysis Automation. The
 Procedures tab in Analysis Automation opens, where you can view
 the procedure.
7. If you get a message saying that the procedure must be approved, you do not have the
 privileges to Approve and reject procedures. To extend your
 privileges, contact your system administrator.

After uploading the procedure, create a
 task to execute your procedure in Analysis Automation.

Parent topic:

Analyzing Data

Related tasks:

- Creating a New Jupyter Notebook
- Finding Data with Advanced Search
- Adding or Editing Tasks for Analysis Automation Procedures

Related information:

- Analysis Automation notebook

<!--NI_TOPIC bundle=systemlink-server path=creating-backup.html language=enus -->
## TOPIC 00055: Creating a Backup of an Instance

- bundle_id: `systemlink-server`
- source_path: `creating-backup.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-backup.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Back up a DataFinder, Data Preprocessor, or an Analysis Automation instance in a backup file to restore the instance when necessary. In Data Preparation or Data Indexing: Click Data Preprocessor Instances or DataFinder Instances. Select an instance and click Stop if the instance is running. Click Mo

### Creating a Backup of an Instance

Back up a DataFinder, Data Preprocessor, or an Analysis Automation instance in a backup
 file to restore the instance when necessary.

1. Optional: 
 In Data Preparation or Data
 Indexing: 
 
 Mode
 DescriptionNormal
 Creates a default backup of a DataFinder instance.
 Migration
 Creates a backup of a DataFinder instance which you can use to move the DataFinder
 instance to another computer. The backup file contains all
 necessary information for connecting to the Microsoft SQL
 Server. You do not need to recreate the index of a migrated
 DataFinder instance. Creating a backup of an instance in the
 Migration mode deletes this
 instance.
  1. Click Data Preprocessor Instances or
 DataFinder Instances.
  2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Stop if the instance is running.
  3. Click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»More»Create Backup. Specify the folder where you want to save the backup
 file. Use a UNC path to specify the folder. An example UNC path is
 \\Server\MyFolder.
  4. Specify whether the backup of a DataFinder or Data Preprocessor
 instance should exclude the index. If you exclude the index, you need to
 reindex the instance after it has been restored. This may take some
 time. 
 Note You can only back up instances with their index if the index size is
 smaller than 50 GB.
  5. Make the following settings for DataFinder
 instances that use the Microsoft SQL Server as an index adaptor.
 Adaptors connect a DataFinder instance index to a different database to
 store the index.
2. Optional: 
 In Analysis Automation:
  1. Click Instance on the dashboard.
  2. Click [IMAGE alt='image' src='GUID-A2DAEE93-CE77-45A0-ABEE-9B9F2BBACA6F-a5.png']»Stop if the instance is running.
  3. Click [IMAGE alt='image' src='GUID-A2DAEE93-CE77-45A0-ABEE-9B9F2BBACA6F-a5.png']»More»Create Backup. Specify the folder where you want to save the backup
 file. Use a UNC path to specify the folder. An example UNC path is
 \\Server\MyFolder.
3. In all instances, click OK to save the backup. Backups
 have the following file extensions:
  - DataFinder instance:
 .bakdf
  - Data Preprocessor instance:
 .bakdpp
  - Analysis Automation
 instance: .bakas
4. Optional: 
 To create a schedule that backs up the instances regularly, select [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»More»Regular Backup Schedule, enable the setting Backup server
 regularly, make your settings, and click
 OK. Use a UNC path to specify the folder. An example
 UNC path is \\Server\MyFolder.

Parent topic:

Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

<!--NI_TOPIC bundle=systemlink-server path=creating-configuring-data-indexing.html language=enus -->
## TOPIC 00056: Creating a DataFinder Instance

- bundle_id: `systemlink-server`
- source_path: `creating-configuring-data-indexing.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-configuring-data-indexing.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create DataFinder instances to index your technical data in one or multiple workspaces in the SystemLink file service, or in one or multiple folders called search areas on the SystemLink server or other network computers. The instances you create can either serve as a data source in an automated ana

### Creating a DataFinder Instance

Create DataFinder instances to index your technical data in one or multiple workspaces
 in the SystemLink file service, or in one or multiple folders called search areas on the
 SystemLink server or other network computers. The instances you create can either serve as a
 data source in an automated analysis process, or you can use them to manually search data
 with Data Navigation or client software like DIAdem or LabVIEW.

Note

Global Settings

»

Display SQL Server Settings

1. In SystemLink Web Application, under Data Administration, click Data
 Indexing and then DataFinder Instances.
2. Click New»DataFinder Instance to start the configuration wizard.
3. Enter a name and click Next. 
 You need to know the name when you want to add this DataFinder instance to an
 analysis automation procedure as a data source. Data Navigation and clients need
 this name to connect to the instance.
4. Specify the type of DataFinder instance you want to create. 
 Setting
 DescriptionNetwork shares within the organization
 Indexes data on network computers. A search area specifies a folder, which
 DataFinder instances index to enable Data Navigation or a
 client software to browse and search for data. You can add
 more search areas later.
 SystemLink file service
 Indexes the data in the SystemLink file service. The file service is the central
 data storage in SystemLink.Note Data Indexing already has a
 default FileIndex instance dedicated to searching data
 in the SystemLink file service.
5. If you select Network shares within the organization,
 complete the following steps:
  1. Specify a descriptive name for the search area and choose the folder
 with the data you want to index. Use UNC paths to specify folders, for
 example, \\Server\MyFolder.
  2. Choose a workspace to determine which users can access this search area
 in Data Navigation.
6. Click 
 Finish.
7. Select the DataFinder instance in the overview and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Start to start the instance.

If you created a DataFinder instance
 that indexes network shares, add one or more search areas.

Parent topic:

Indexing Data

Related tasks:

- Configuring File Indexing for a DataFinder Instance
- Adding and Editing Search Areas

<!--NI_TOPIC bundle=systemlink-server path=creating-configuring-data-preparation.html language=enus -->
## TOPIC 00057: Creating a Data Preprocessor Instance

- bundle_id: `systemlink-server`
- source_path: `creating-configuring-data-preparation.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-configuring-data-preparation.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Data Preprocessor instance to harmonize measurement data from different sources and make it easier to compare in a report. In DIAdem you define how the data is harmonized and save the procedure in a DPP file you upload to the Data Preprocessor instance. If you want to use a Microsoft SQL Serve

### Creating a Data Preprocessor
 Instance

Use a Data Preprocessor instance to harmonize measurement data from different sources
 and make it easier to compare in a report. In DIAdem you define how the data is harmonized
 and save the procedure in a DPP file you upload to the Data Preprocessor instance.

Note

Global Settings

»

Display SQL Server Settings

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Click [IMAGE alt='image' src='GUID-240AE4D6-DBF9-477F-B7B2-CE427637128A-a5.svg']New»Data Preprocessor Instance to start the configuration wizard.
3. Enter a name and click 
 Next.
4. Configure the data areas. The Data Preprocessor instance takes the data from the raw data area, transforms the data into a consistent form, and stores the data in the processed data area. Use a UNC path to specify the folder. An example UNC path is 
 \\Server\MyFolder. 
 Parameter
 Description
 ExampleName
 Name of the data areas.
 MyRawAndProcessedData
 Raw data
 Folder containing the raw data.
 \\MyServer\Data\Raw_Data
 Processed data
 Folder where the Data Preprocessor instance saves the harmonized data.
 \\MyServer\Data\Processed_Data
5. If you are using a Microsoft SQL Server database, enable MS SQL support and
 specify the settings for the database connection.
6. Specify the configuration mode. 
 Option
 DescriptionUse default configuration
 Converts the raw data to TDM and calculates the minimum and maximum values.
 Use custom configuration
 Harmonizes the raw data according to the data preparation procedure
 (*.dpp) you upload.
7. Select the instance you created and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Start to start the instance.

After creating a Data Preprocessor instance, upload a data
 preparation procedure, add DataPlugins to convert your raw data, and configure how you want to
 process the files.

Parent topic:

Harmonizing and Enriching Data

Related tasks:

- Updating Data Preparation Procedures
- Specifying File Types to Be Scanned and Processed
- Configuring the Monitoring and Processing of Raw Data

<!--NI_TOPIC bundle=systemlink-server path=creating-data-preparation-procedures.html language=enus -->
## TOPIC 00058: Creating Data Preparation Procedures in DIAdem

- bundle_id: `systemlink-server`
- source_path: `creating-data-preparation-procedures.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-data-preparation-procedures.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Harmonize disparate measurement data from different sources with data preparation procedures. In data preparation procedures, you specify the original property identifiers and values, units, and data file format and their target equivalent. Launch DIAdem and open the SCRIPT panel. Select SettingsSys

### Creating Data Preparation Procedures in DIAdem

Harmonize disparate measurement data from different sources with data preparation
 procedures. In data preparation procedures, you specify the original property identifiers
 and values, units, and data file format and their target equivalent.

1. Launch DIAdem and open the SCRIPT panel.
2. Select Settings»SystemLink TDM»Data Preparation Procedure.
3. Click New Data Preparation Procedure.
4. Enter the name of the new data preparation procedure, a description, and the
 author. Click OK.
5. On the Replace Identifiers tab, specify how the Data
 Preprocessor instance replaces property labels. The example in the following
 table shows labels from 3 different sources. The data preparation process
 replaces the different property identifiers from the 3 data sources with the
 newly defined identifier Engine_Fuel_Type in the harmonized
 target file. 
 Source 1
 Source 2
 Source 3
 Harmonized IdentifierProperty Identifier
 Engine
 Engine_Type
 Fuel
 Engine_Fuel_Type
6. On the Replace Values tab, specify how the Data
 Preprocessor instance replaces property values. The example in the following
 table shows values from 3 different sources. The data preparation process
 replaces the different property values from the 3 data sources with the newly
 defined value Diesel in the harmonized target file. 
 Source 1
 Source 2
 Source 3
 Harmonized ValueProperty Value
 Diesel
 D
 Fuel_Diesel
 Diesel 
 The data preparation process creates data with comparable identifiers, values, and
 units. Harmonized IdentifierHarmonized ValueEngine_Fuel_TypeDiesel
7. Optional: 
 Further configure this procedure in any of the following
 ways: 
 TabConfigurationConvert Units
 Specify the engineering unit to convert data to. For example, if temperatures were
 measured in °F and °C and you want
 to evaluate them in the unit K, specify that the
 process converts and saves all temperatures in the unit
 K.Statistics
 Calculate characteristic statistical values, such as mean, quantile,
 or dispersion. The process saves the statistical results as custom
 properties in the target files.V&V
 Check whether the data is plausible and complete. For validation and verification,
 create a script that checks whether the data adheres to a limit. Refer
 to the DIAdem help under Programming Reference»Object-Oriented Script Interface»SystemLink for more information about which objects to use from the
 SystemLink API.Convert File
 Specify the file format to which the process saves the target files.
8. Click Save Data Preparation Procedure As, enter a name,
 and click Save.

*.dpp

Parent topic:

Harmonizing and Enriching Data

Related tasks:

- Updating Data Preparation Procedures

<!--NI_TOPIC bundle=systemlink-server path=creating-diagnostics-file.html language=enus -->
## TOPIC 00059: Creating a Diagnostics File for a Service Request

- bundle_id: `systemlink-server`
- source_path: `creating-diagnostics-file.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-diagnostics-file.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a diagnostics file to send to your NI support representative or submit in a service request through ni.com. Diagnostics files contain logging information from all existing DataFinder, Data Preprocessor, and Analysis Automation instances. SystemLink TDM logs server activities in the Standard m

### Creating a Diagnostics File for a Service Request

Create a diagnostics file to send to your NI support representative or submit in a
 service request through ni.com. Diagnostics files contain logging information from all
 existing DataFinder, Data Preprocessor, and Analysis Automation instances.

Standard

Note

1. Use one of the following applications to create a
 diagnostics file. In Data Indexing or Data
 Preparation:
  1. Click DataFinder Instances or
 DataPreprocessor Instances on the
 dashboard.
  2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Global Settings»Logfile and Diagnostics File. 
 Note In the Analysis Automation instance, click Global Settings»Logfile and Diagnostics File.
2. Click Create. 
 Creating a diagnostics file may take a while. The diagnostics file contains
 the information scope from the active logging mode. 
 Logging mode
 DescriptionStandard
 Writes basic information to the logfile.
 Extended
 Writes additional information to the logfile to improve
 troubleshooting.
 User-defined
 Logs custom information with an XML file you receive from NI following a support
 request. Upload this file here.
3. Click the filename to open or save the ZIP file.
4. If you need to change the logging mode, choose the
 required option and click OK. Run the logging mode for
 the length of time suggested. Then continue with steps 1-2 to create a
 diagnostics file. 
 Changing the logging mode takes effect immediately. All previous logfiles
 maintain their format and remain on the server.

Parent topic:

Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

<!--NI_TOPIC bundle=systemlink-server path=creating-email-notifications.html language=enus -->
## TOPIC 00060: Creating Email Notifications for Tests

- bundle_id: `systemlink-server`
- source_path: `creating-email-notifications.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-email-notifications.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use SystemLink TestStand steps to automatically send emails depending on test results. Before you can create email notifications, you must first integrate TestStand with your SystemLink server. In NI SystemLink Server Configuration, ensure your server host name is correct and log in if your server r

### Creating Email Notifications for Tests

Use SystemLink TestStand steps to automatically send emails depending on test results.

Before you can create email
 notifications, you must first integrate TestStand with your SystemLink server.

1. In NI SystemLink Server Configuration, ensure your server host name is correct and log in if your server requires credentials.
2. Specify an email address to send email notifications from.
3. In TestStand, in the test you want to send notifications for, right-click in the 
 Step panel and click 
 Insert Step...»SystemLink»Email Notification.
4. In theStep Settings panel, under 
 Recipient, enter one or more email addresses or a local variable containing email addresses.
5. Specify the test condition(s) under which you want the recipients to receive the notification. 
 Note If you select 
 Send Immediately, TestStand sends a notification to the recipients when the test starts.
6. Create a TestStand step to use a preconfigured email template for the notifications.
  1. Click 
 Insert Step...»SystemLink»Get Email Templates.
  2. In the 
 Variables panel, under 
 Locals, click 
 Insert»Local»Array of»Container to return an array of template metadata, including each template's name and ID.
  3. In the 
 Step Settings panel, under 
 Templates, specify the variable name you created in step b.
  4. In the details section for the Email Notification step, use a TestStand expression to specify the ID for the template you want to edit. 
 For example, 
 Locals.Templates[3].Id.

When you run your test, TestStand sends email notifications according to the conditions you specified in step 5. The notification emails contain links to the test results in 
 Test Monitor.

Parent topic:

Monitoring Tests

Related tasks:

- Integrating Test Monitor with TestStand

<!--NI_TOPIC bundle=systemlink-server path=creating-packages-labview-package-builder.html language=enus -->
## TOPIC 00061: Creating Packages with LabVIEW Package Builder

- bundle_id: `systemlink-server`
- source_path: `creating-packages-labview-package-builder.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/creating-packages-labview-package-builder.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create packages in LabVIEW to deploy to clients. Before creating packages, install a supported version of LabVIEW to your host. Create content to include in your package, such as a source distribution, package project library, or executable. You cannot include VIs from your project directly in a pac

### Creating Packages with LabVIEW Package Builder

Create packages in LabVIEW to deploy to clients.

Note

1. In the 
 Project Explorer in LabVIEW, right-click 
 Build Specifications and select 
 New»Package.
2. Under 
 Information, enter the name you want to use for your package in 
 Package name. 
 The package name must be all lowercase and contain no spaces. Package Manager and other packages will use this name to reference the package you create.
3. Under 
 Source Files, specify which files or build specification outputs you want to install.
4. Under 
 Destinations, set up any destination folders where you plan to install the package in the client.
5. Under 
 Shortcuts, you can add a shortcut to the Startup menu on a Windows system if you want your application to run as soon as the system starts up. You can also add a shortcut to the Desktop or Program Menu on Windows. 
 By default, SystemLink on Windows also creates a shortcut in the Windows Program menu for any application in your project.
6. Under 
 Package, specify the display name and synopsis for your package. 
 The display name is what users will see in the NI Package Manager or the SystemLink
 web application when they install your package. The synopsis is the first line of the
 description that users see before they click on a package to see its full description.
7. Under 
 Dependencies, specify dependencies on any currently installed packages.
  1. Configure the relationship of the dependency. You can define a dependency as 
 Required, 
 Recommended, or 
 Suggested and specify version ranges.
  2. To prompt the user to install your package when they install a related package, select 
 Enhanced.
8. Under 
 Version Information, specify the version of your package and what version you want to display to the user. 
 If you remove the display version, the user sees the full version in Package Manager.
9. Under 
 Advanced, set your package to run executables or scripts while it installs or uninstalls. 
 For example, you can specify whether installation or uninstallation waits for a certain action to complete. On Linux systems, you can also specify whether the application is a startup application.
10. Optional: 
 If you want to create a new SystemLink feed for the package, click 
 Feed.
  1. Check the box next to 
 Publish to SystemLink feed.
  2. Specify your server credentials.
  3. Specify a name and description for your SystemLink feed.
11. Click 
 Build. 
 You should see an 
 .nipkg file (Windows) or 
 .ipk file (Linux) in the destination you specified.

Next, add packages to a feed to begin distributing the package to other systems. If you
 published your package directly to a new SystemLink feed, deploy your package to clients to
 complete this workflow.

Parent topic:

Deploying Applications to Clients on a Server

Related tasks:

- Enabling Client Access to Packages
- Deploying Packages to Clients
- Hosting a WebVI in SystemLink
- Hosting a Web Application on the NI Web Server

<!--NI_TOPIC bundle=systemlink-server path=customizing-asset-reports-jupyterhub.html language=enus -->
## TOPIC 00062: Customizing Asset Reports with JupyterHub

- bundle_id: `systemlink-server`
- source_path: `customizing-asset-reports-jupyterhub.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/customizing-asset-reports-jupyterhub.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit the Python notebooks that install with Asset Module to customize your asset reports. To edit code in asset report notebooks, first install NI SystemLink Asset Module and JupyterHub Module. Refer to Jupyter Notebooks and Scrapbook documentation for details about programming with JupyterHub. In A

### Customizing Asset Reports with JupyterHub

Edit the Python notebooks that install with Asset Module to customize your asset reports.

To edit code in asset report notebooks, first install NI SystemLink Asset Module and JupyterHub Module.

Refer to Jupyter Notebooks and Scrapbook
 documentation for details about programming with JupyterHub.

1. In 
 Asset Manager, select one of the reports on the dashboard.
2. Select the report you want to customize in JupyterHub.
3. Click Download Source to save a copy of the
 .ipynb file to your local machine. 
 Note You can find all preinstalled notebooks in
 C:\ProgramData\National
 Instruments\Skyline\JupyterHub\notebooks\_shared\reports .
4. On the toolbar, click [IMAGE alt='image' src='GUID-AE4F09C7-035C-44CA-BB97-7DB45D0F8FE2-a5.png'] and click
 Jupyter.
5. Create a new folder and name it reports.
6. In the reports folder, upload the .ipynb file you saved.
7. Open the notebook and modify it using Python code. 
 To learn about setting up and using Jupyter Notebooks, refer to *Creating a New
 Jupyter Notebook*.
 To learn about importing data from different sources, such as tags, test results, or
 TDMS files, refer to the Python API examples in GitHub, the Python API document on
 your server, or *Installing Additional Python Modules*.
8. Save the notebook.

Asset Manager

Reports

Parent topic:

Reporting Data with Jupyter Notebooks

Related tasks:

- Creating a New Jupyter Notebook
- Installing Additional Python Modules

Related information:

- SystemLink Examples Repository

<!--NI_TOPIC bundle=systemlink-server path=customizing-reports.html language=enus -->
## TOPIC 00063: Customizing Test Reports with JupyterHub

- bundle_id: `systemlink-server`
- source_path: `customizing-reports.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/customizing-reports.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit the Python notebooks that install with Test Module to customize your test reports. To edit code in test report notebooks, first install NI SystemLink Test Module and JupyterHub Module. Refer to Jupyter Notebooks and Papermill documentation for details about programming with JupyterHub. In Test

### Customizing Test Reports with JupyterHub

Edit the Python notebooks that install with Test Module to customize your test reports.

To edit code in test report notebooks, first install NI SystemLink Test Module and JupyterHub Module.

Refer to Jupyter Notebooks and Papermill documentation for details about programming with JupyterHub.

1. In Test Insights, click Reports.
2. Select the report you want to customize in JupyterHub.
3. Click Download Source to save a copy of the
 .ipynb file to your local machine. 
 Note You can find all preinstalled notebooks in
 C:\ProgramData\National
 Instruments\Skyline\JupyterHub\notebooks\_shared\reports .
4. On the toolbar, click [IMAGE alt='image' src='GUID-AE4F09C7-035C-44CA-BB97-7DB45D0F8FE2-a5.png'] and click
 Jupyter.
5. Create a new folder and name it reports.
6. In the reports folder, upload the .ipynb file you saved.
7. Open the notebook and modify it using Python code. 
 To learn about setting up and using Jupyter Notebooks, refer to *Creating a New
 Jupyter Notebook*.
 To learn about importing data from different sources, such as tags, test results, or
 TDMS files, refer to the Python API examples in GitHub, the Python API document on
 your server, or *Installing Additional Python Modules*.
8. Save the notebook.
9. If you want other users on your server to access this report, save the report
 to C:\ProgramData\National
 Instruments\Skyline\JupyterHub\notebooks\_shared\reports.

Test
 Insights

Reports

Parent topic:

Reporting Data with Jupyter Notebooks

Related tasks:

- Creating a New Jupyter Notebook
- Installing Additional Python Modules

Related information:

- SystemLink Examples Repository

<!--NI_TOPIC bundle=systemlink-server path=data-cart-analysis.html language=enus -->
## TOPIC 00064: Adding TDMS Files to the Data Cart for Analysis

- bundle_id: `systemlink-server`
- source_path: `data-cart-analysis.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/data-cart-analysis.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Select and add TDMS file references from Test Insights Results to the Data Cart for use in a task in Analysis Automation. Use the Data Cart when you want to execute more than one test for different batches of TDMS files. Before you begin, ensure that you have test results that contain at least one T

### Adding TDMS Files to the Data Cart for
 Analysis

Select and add TDMS file references from Test Insights Results to the Data Cart for use
 in a task in Analysis Automation. Use the Data Cart when you want to execute more than one test
 for different batches of TDMS files.

Before you begin, ensure that you have
 test results that contain at least one TDMS file attachment.

1. In Test Insights, select a result that contains one or more TDMS file
 attachments.
2. Click Attachments and select the TDMS files you want to
 analyze.
3. Repeat steps 1-2 until you have selected all the TDMS
 files from each test result you want to analyze in one or more Data Analysis
 tasks.
4. In the SystemLink web application, click Measurement Data Analysis»Data Analysis. 
 Note Data Analysis retains file references
 in the Data Cart from Test Insights.
5. Click the Data Cart and select the file references you want to add as a data
 source for a task.
6. Open a task and click Run to execute the task using the
 file references you selected in the Data Cart.
7. Repeat steps 5-6 for each Data Analysis task you want to
 execute.

Parent topic:

Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-server path=data-navigator.html language=enus -->
## TOPIC 00065: Retrieving Data from Your Data Stores

- bundle_id: `systemlink-server`
- source_path: `data-navigator.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/data-navigator.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Data Navigation to manually find data in the folders of a company network or in the SystemLink file service. After you retrieve the data, you can inspect, upload, download your data, add custom properties or export the files for further analyses to Data Analysis. Complete the tasks that best sui

### Retrieving Data from Your Data
 Stores

Use Data Navigation to manually find data in the folders of a company network or in the
 SystemLink file service. After you retrieve the data, you can inspect, upload, download your
 data, add custom properties or export the files for further analyses to Data
 Analysis.

Complete the tasks that best suit your goals.

- [Finding Data with Quick Search](finding-data-with-quick-search.html) Use Quick Search to find search terms in the file properties of a DataFinder instance. Perform a quick search if you only have partial search information or if you are unsure whether the information is in a file, channel group, or channel.
- [Finding Data with Advanced Search](finding-data-with-advanced-search.html) Use Advanced Search to find files, channel groups, or channels containing specified property values. Combine search conditions with logical operators to define complex search queries.
- [Working with Search Results](working-with-search-results.html) After completing a search, inspect, export, or make the search results available for data analysis.
- [Exporting and Downloading Files](exporting-saving-files.html) Export the files you found to a zip file and download the file to your computer or make these files available for data analyses.
- [Moving Search Results to Data Analysis](providing-search-results-for-analysis.html) Add your search results to the data cart in Data Navigation to execute manual analysis tasks on these files in Data Analysis.
- [Uploading Files to SystemLink](adding-files-to-file-service.html) The File Service tab in Data Navigation displays all files stored in SystemLink. Upload files to the file service to enable clients to search for these files using a DataFinder instance that indexes the SystemLink file service.
- [Previewing Files in Data Navigation](preview-data-file.html) Preview measurement, image, and PDF files that you uploaded to the file service in Data Navigation.
- [Adding and Editing Metadata of SystemLink File Service Files](adding-meta-data-file-service-files.html) Add and edit metadata of SystemLink file service files to identify these files and to make it easier to find these files within a search.

Parent topic:

Generating Actionable Data Insights

<!--NI_TOPIC bundle=systemlink-server path=data-preparation.html language=enus -->
## TOPIC 00066: Harmonizing and Enriching Data

- bundle_id: `systemlink-server`
- source_path: `data-preparation.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/data-preparation.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data Preparation harmonizes disparate raw data from various sources, file formats, units, and naming conventions to provide a consistent and comparable view of your test results in one source. Harmonized data is the basis for reliable, actionable insights into your testing activities. A diagram of t

### Harmonizing and Enriching Data

Data Preparation harmonizes disparate raw data from various sources, file formats,
 units, and naming conventions to provide a consistent and comparable view of your test
 results in one source. Harmonized data is the basis for reliable, actionable insights into
 your testing activities.

[IMAGE alt='A diagram of the relationship between the Data Maintainer role, the Method Engineer, and system configuration.' src='GUID-610B741D-A133-4204-92FB-F8FBBE880CD9-a5.svg']

Complete the tasks that best suit your data preparation goals.

- [Creating Data Preparation Procedures in DIAdem](creating-data-preparation-procedures.html) Harmonize disparate measurement data from different sources with data preparation procedures. In data preparation procedures, you specify the original property identifiers and values, units, and data file format and their target equivalent.
- [Creating a Data Preprocessor Instance](creating-configuring-data-preparation.html) Use a Data Preprocessor instance to harmonize measurement data from different sources and make it easier to compare in a report. In DIAdem you define how the data is harmonized and save the procedure in a DPP file you upload to the Data Preprocessor instance.
- [Configuring a Data Preprocessor Instance](preparing-data-for-preprocessing.html) Configure scanning schedules and the reaction to file changes, manage raw data areas and DataPlugins, and initiate manual processing.
- [Monitoring the Processing Status](monitoring-status-datapreprocessor.html) Check the processing status of the files in the raw data areas of a Data Preprocessor instance. Initiate scanning or reprocessing of files or folders if necessary.

Parent topic:

Generating Actionable Data Insights

<!--NI_TOPIC bundle=systemlink-server path=data-types-tag-data.html language=dede -->
## TOPIC 00067: Datentypen zur Darstellung von Tag-Daten

- bundle_id: `systemlink-server`
- source_path: `data-types-tag-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/dede/data-types-tag-data.html
- source_language: `dede`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Die Ein- oder Ausgabeart bestimmt den Typ der Tag-Daten, die in den Eigenschaften akzeptiert werden. Verwenden Sie die folgende Tabelle, um Ihre Tags für die Eigenschaftsbindungen häufiger Ein- und Ausgabearten zu formatieren. Eingabe/Ausgabe Eigenschaft Von Eigenschaft akzeptierte Tag-Datentyp(en)

### Datentypen zur Darstellung von Tag-Daten

Die Ein- oder Ausgabeart bestimmt den Typ der Tag-Daten, die in den Eigenschaften akzeptiert werden. Verwenden Sie die folgende Tabelle, um Ihre Tags für die Eigenschaftsbindungen häufiger Ein- und Ausgabearten zu formatieren.

| Eingabe/Ausgabe | Eigenschaft | Von Eigenschaft akzeptierte Tag-Datentyp(en) | Beispiel |
| --- | --- | --- | --- |
| Zahl Behälter Rundinstrument Schieber | Alle Bereichs-Eigenschaften Wert | Doppelt | 2,5 |
| Textfeld | Wert Platzhalter | String | Hallo Welt |
| Datum/Zeit | Alle Bereichs-Eigenschaften Platzhalter | Zeitstempel String | 04-09-2018 14:35:56 |
| Schalter Auswahlfeld LED | Wert | Boolesches Element | True |
| Dropdown-Liste Listenfeld Optionsfeldgruppe | Objekte | String-Darstellung von JSON-Array mit Objekten. Jedes Objekt umfasst: Beschriftung - den im Element angezeigten Text Wert - den Objektwert | [{"Beschriftung":"Objekt 1","Wert":"Wert 1"},{"Beschriftung":"Objekt 2","Wert":"Wert 2"}] |
| Graph | Wert eines einzelnen Plots | String-Darstellung von JSON-Array mit Zahlen. | [1,0, 2,0] |
| Diagramm | Wert eines einzelnen Plots | Doppelt (einer pro Plotwert) | 1,0 |
| Baumstruktur | Objekte | String-Darstellung von JSON-Array mit Objekten. Jedes Objekt umfasst: Name - String-Beschriftung für das Objekt Wert - dem Objekt zugeordneter Wert Objekte - Array mit untergeordneten Objekten. Jedes untergeordnete Objekte ist ein Array, das Name, Wert und Objekte umfasst, wenn das untergeordnete Objekt weitere Objekte enthält. | [{"Name":"Objekt 1","Wert":"1","Objekte":[{"Name":"Objekt 1.1","Wert":"1.1"},{"Name":"Objekt 1.2","Wert":"1.2"}]},{"Name":"Objekt 2","Wert":"2","Objekte":[{"Name":"Objekt 2.1","Wert":"2.1"}]}]}] |
| Tabelle | Wert | 2D-String-Array | [["1","2","3"],["4","5","6"],["7","8","9"],["10","11","12"],["13","14","15"],["16","17","18"]] |
| Tag-Gitter | Spalten | String-Darstellung von JSON-Array mit Objekten. Jedes Objekt umfasst: Beschriftung - die Überschrift für die Spalte Wert - die Tag-Eigenschaft zum Auffüllen des Rasters Gültige Werte umfassen: Pfad Wert Zeitstempel Typ Anzahl Min Max Mittel SammelBerechnungsergebnisse Stichwörter Alle benutzerdefinierten Eigenschaften, die Sie mit Hilfe der Formateigenschaften Eigenschaften.<Eigenschaftsname> definieren. | [{"Beschriftung":"Tag Pfad","Wert":"Pfad"},{"Beschriftung":"Tag Wert","Wert":"Eigenschaften.MeineEigenschaft"}] |
| Map | Map-Mitte Map-Markierungen Zoomstufe | Map-Mitte oder Map-Markierungen: String-Darstellung von JSON-Array (Double) mit einer Größe von 2. Zoomstufe: Ganzzahl Hinweis Ordnen Sie die Werte für Mitte und Zoomstufe separat zu. | Map-Mitte oder Map-Markierung [32,787, -96,887] Zoomstufe: 10 |

Übergeordnetes Thema:

Darstellen von Tag-Daten in einem Dashboard mit freiem Layout

Zugehörige Tasks:

- Angeben von Werten für Objektelemente
- Zuordnen von Tags zu OPC-UA-Variablen

Zugehörige Verweise:

- Bindungs-Syntax

<!--NI_TOPIC bundle=systemlink-server path=decreasing-cpu-usage-for-single-node-deployments.html language=enus -->
## TOPIC 00068: Decreasing CPU Usage for Single Node Deployments

- bundle_id: `systemlink-server`
- source_path: `decreasing-cpu-usage-for-single-node-deployments.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/decreasing-cpu-usage-for-single-node-deployments.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Increase the index cache size to process more data, avoid high CPU usage, and enable the Asset Management module in a single-node deployment. NI recommends increasing the available memory for the index to 8GB. Log into the desktop of the SystemLink server with administrator privileges. Launch the NI

### Decreasing CPU Usage for Single Node
 Deployments

Increase the index cache size to process more data, avoid high CPU usage, and enable the
 Asset Management module in a single-node deployment. NI recommends increasing the
 available memory for the index to 8GB.

1. Log into the desktop of the SystemLink server with
 administrator privileges.
2. Launch the NI SystemLink Server Configuration.
3. Navigate to the NoSqlDatabase
 section.
4. Enable The NoSqlServer is launched and managed by
 SystemLink and adjust the value of
 The cache size of the database in
 Gigabytes (GB). 
 Note NI recommends increasing the index cache size to
 8GB.
5. Click Apply.

Parent topic:

Choosing a MongoDB Deployment

<!--NI_TOPIC bundle=systemlink-server path=defining-additional-raw-data-areas.html language=enus -->
## TOPIC 00069: Defining Additional Raw Data Areas

- bundle_id: `systemlink-server`
- source_path: `defining-additional-raw-data-areas.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/defining-additional-raw-data-areas.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add new folders with raw data to be scanned or processed by the Data Preprocessor instance. In Data Preparation, click Data Preprocessor Instances. Select an instance and click ManageRaw Data Areas. Click Add and specify a name and folders for the raw data and processed data. Use UNC paths to specif

### Defining Additional Raw Data Areas

Add new folders with raw data to be scanned or processed by the Data Preprocessor
 instance.

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Select an instance and click 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Raw Data Areas.
3. Click Add and specify a name and folders for the raw data and
 processed data. Use UNC paths to specify a folder. An example UNC path is
 \\Server\MyFolder.
4. Click OK to confirm your settings.
5. Optional: 
 To modify the regular file scanning schedule for the raw data folders, click Monitoring»File Scan Schedule.
6. Make your settings and click OK.
7. Click Apply to accept the settings.
8. Optional: 
 Select a raw data area and click Exclude Subfolder to
 exclude subfolders from scanning and processing.
9. Optional: 
 To change a name of a raw data area, select the name and click
 Edit.

Parent topic:

Configuring a Data Preprocessor Instance

<!--NI_TOPIC bundle=systemlink-server path=defining-data-integrity-rules.html language=enus -->
## TOPIC 00070: Checking Compliance of Data Entering File Service

- bundle_id: `systemlink-server`
- source_path: `defining-data-integrity-rules.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/defining-data-integrity-rules.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Define data integrity rules to ensure that all data entering the SystemLink file service complies with the metadata requirements for your data analyses. The checks apply to the workspaces that the DataFinder instance indexes. Define data integrity rules in a JSON file that you upload to a DataFinder

### Checking Compliance of Data Entering File
 Service

Define data integrity rules to ensure that all data entering the SystemLink file service
 complies with the metadata requirements for your data analyses. The checks apply to the
 workspaces that the DataFinder instance indexes.

Define data integrity rules in a JSON file
 that you upload to a DataFinder dedicated to indexing the file service. Once DataFinder
 indexes and checks files for compliance, Data Navigation highlights all files that do
 not comply with the data integrity rules.

1. In a text editor, create a JSON file that defines the required metadata at the
 root, group, and
 channel level for all TDM data entering the file
 service. 
 Tip Update the
 RequiredMetadataVersion property when updating a
 definition file. This enables you to search for data that complies with a
 specific version of the definition file. 
 Refer to the code example for a metadata definition file at the bottom of this
 page.
2. Upload the JSON file to the DataFinder that indexes the file service.
  1. In SystemLink Web Application, under Data Administration, click
 Data Indexing and then DataFinder
 Instances.
  2. Select the instance to which you want to upload the file and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
  3. On the Index tab, click Data
 Integrity Rules.
  4. Upload the definition file from your disk and click
 OK. 
 The DataFinder instance checks all new files entering the file
 service for compliance with the metadata definition and adds two
 properties to the index: Added PropertiesValuesNI_FS~RequiredMetadata~Compliant
 (searchable in Data Navigation)Not compliant: Value =
 0Compliant: Value > 0 
Compliant value is "RequiredMetadataVersion" from the metadata definition fileNI_FS~RequiredMetadata~ErrorText
 (not searchable in Data Navigation)Missing keys:metadata1,
 metadata2, ...
  5. To remove the file, click Remove
 definition file.
3. On the Search Areas tab, select the
 Workspaces you want to index. If you want to index
 the entire file service, switch the toggle to Index all workspaces on
 the system.
4. Optional: 
 Reset the entire index to execute a compliance check on already indexed files
 in the file service.
  1. Select the Index tab.
  2. Click the arrow next to Reset Index and choose
 Entire Index. 
 The DataFinder instance reindexes all files in the file service,
 checks them for compliance, and adds the same properties as above to the
 index. This process may take a while.

Example for a definition file:

```text
{
    "FileVersion": 1,
    "Description": "Required metadata keys for SystemLink (this line is ignored)",
    "RequiredMetadataVersion": 1.0,
    "RequiredMetadataKeys": {
        "root": ["product_identifier", "product_type", "product_design_step"],
        "group": ["package", "dut_id"],
        "channel": ["ResultStatArithMean", "ResultStatMax", "ResultStatMin"]
    }
}
```

Search for all files that do not comply
 with the data integrity rules in the advanced search in Data Navigation and add the missing
 metadata.

Parent topic:

Preparing Data for Searching

Related tasks:

- Finding Data with Advanced Search
- Adding and Editing Metadata of SystemLink File Service Files

<!--NI_TOPIC bundle=systemlink-server path=deploying-applications-to-clients.html language=enus -->
## TOPIC 00071: Deploying Applications to Clients on a Server

- bundle_id: `systemlink-server`
- source_path: `deploying-applications-to-clients.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/deploying-applications-to-clients.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a package (.nipkg) from an application and deploy it to all your managed systems.

### Deploying Applications to Clients on a Server

Create a package (.nipkg) from an application and deploy it to all
 your managed systems.

- [Creating Packages with LabVIEW Package Builder](creating-packages-labview-package-builder.html) Create packages in LabVIEW to deploy to clients.
- [Enabling Client Access to Packages](enabling-client-access-to-packages.html) Upload packages you created to your SystemLink server for clients to access.
- [Deploying Packages to Clients](deploying-packages.html) Add feeds containing packages you created to SystemLink clients.
- [Troubleshooting Package Deployment and Server Configuration](troubleshooting.html) Understand and solve potential issues when deploying packages to clients.
- [Deploying System States to Clients](deploying-system-states.html) Create a state to deploy the same system image and set of packages to multiple systems.
- [Comparing Software across Systems](comparing-system-states.html) Compare installed packages, or system states, to facilitate decisions about deployment and maintenance.
- [Controlling Software Updates on a Client](locally-controlling-software-updates-on-client-system.html) Lock a client locally to ensure that software installations do not occur while you are working on the client.
- [Updating NI Software on a SystemLink Linux RT Client](updating-ni-software-on-systemlink-linux-rt-client.html) Upgrade NI software on a SystemLink Linux RT client from the SystemLink web application.

Related information:

- TestStand Deployment Utility
- NI Package Builder
- Command-Line Interface

<!--NI_TOPIC bundle=systemlink-server path=deploying-packages.html language=enus -->
## TOPIC 00072: Deploying Packages to Clients

- bundle_id: `systemlink-server`
- source_path: `deploying-packages.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/deploying-packages.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add feeds containing packages you created to SystemLink clients. Before deploying a package, you must add it to a feed. Under Systems, click Systems to see all the systems currently connected to your SystemLink server. Select one or more systems and click Software. In the Feeds tab, click Add. Speci

### Deploying Packages to Clients

Add feeds containing packages you created to SystemLink clients.

Before deploying a package, you must add
 it to a feed.

1. Under Systems, click
 Systems to see all the systems currently connected to
 your SystemLink server.
2. Select one or more systems and click 
 Software.
3. In the 
 Feeds tab, click 
 Add.
4. Specify a feed from a package repository, a URL, or the ni.com Downloads page.
5. Click Add.
6. Click the 
 Available tab to view the packages you can deploy to your target.
7. Click 
 Install on the packages you want to deploy to your SystemLink client and then 
 Next to see a summary.
8. Review your selections and click 
 Apply.

Navigate back to Systems to monitor the
 progress of your systems.

Parent topic:

Deploying Applications to Clients on a Server

Related tasks:

- Enabling Client Access to Packages

<!--NI_TOPIC bundle=systemlink-server path=deploying-system-states.html language=enus -->
## TOPIC 00073: Deploying System States to Clients

- bundle_id: `systemlink-server`
- source_path: `deploying-system-states.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/deploying-system-states.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a state to deploy the same system image and set of packages to multiple systems. A state is any set of packages installed on a system. After you define a state, you can apply it to other systems to more quickly deploy packages to multiple systems. In SystemLink Web Application, in Systems, cl

### Deploying System States to Clients

Create a state to deploy the same system image and set of packages to multiple systems.

state

1. In SystemLink Web Application, in Systems,
 click Systems.
2. Double-click the system from which you want to create a state. 
 Note You can also manually define a state under Systems»States»»Create.
3. Click More [IMAGE alt='image' src='GUID-219456BE-BCA1-4C72-9096-3E2C8A5929FF-a5.png']»Create State.
4. Specify the workspace the state belongs to. 
 Only users in the workspace you specify can use the state. You can reassign
 the state to another workspace at any time.
5. Review feeds, packages, and the image for your system to ensure you want to
 include them in the state. 
 Note If you include a system image in the
 state, you can only apply it to NI Linux RT targets. Applying the state
 erases all currently installed software or data from the primary hard drive
 of the target.
6. Optional: 
 Customize the state to include additional packages in your state that are not currently installed on the system. Specify the feeds you need to access the additional packages you want to include.
  1. Under Feeds, click 
 Add.
  2. Specify a feed from a package repository, a URL, or the ni.com Downloads page.
  3. Check the box for each package you want to include in your state.
7. Click 
 Create to finalize the state.
8. In Systems, select the systems you want to apply the
 state to.
9. Click 
 Software.
10. In the 
 States tab, click 
 Install next to the state(s) you want to apply. 
 The States tab appears only if the feeds and packages in the state
 are compatible with the systems you select.
11. Click 
 Next and review the packages and feeds the state contains.
12. Click 
 Apply.

Available

Parent topic:

Deploying Applications to Clients on a Server

Related tasks:

- Comparing Software across Systems
- Deploying Packages to Clients

<!--NI_TOPIC bundle=systemlink-server path=detecting-errors-in-analysis-automation-processes.html language=enus -->
## TOPIC 00074: Detecting Errors in Analysis Automation Procedures

- bundle_id: `systemlink-server`
- source_path: `detecting-errors-in-analysis-automation-processes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/detecting-errors-in-analysis-automation-processes.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Check the system notifications of Analysis Automation to detect errors that occurred during analyses. In Analysis Automation, click Instance on the dashboard. Click System Notifications to view all notifications. Filter on notification types by selecting them on the No Error Level Selected dropdown

### Detecting Errors in Analysis Automation Procedures

Check the system notifications of 
 Analysis Automation to detect errors that occurred during analyses.

1. In Analysis Automation, click
 Instance on the dashboard.
2. Click System Notifications to view all notifications.
3. Optional: 
 Filter on notification types by selecting them on the No Error Level
 Selected dropdown list. For example, to display only analysis
 automation procedures with errors and with warnings, select
 Errors and Warnings.
4. Optional: 
 Click Apply Filter to enable the error level filter.

Parent topic:

Analyzing Data

<!--NI_TOPIC bundle=systemlink-server path=displaying-data-in-different-hierarchy.html language=enus -->
## TOPIC 00075: Displaying Data in a Different Hierarchy

- bundle_id: `systemlink-server`
- source_path: `displaying-data-in-different-hierarchy.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/displaying-data-in-different-hierarchy.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Load a hierarchy configuration to change the hierarchy in which the data is displayed. In Data Indexing, click DataFinder Instances. Select an instance and click ManageConnectRemote Access. Click DataFinder Hierarchy to determine in which hierarchy the client displays the data. Select User-defined t

### Displaying Data in a Different Hierarchy

Load a hierarchy configuration to change the hierarchy in which the data is displayed.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»[IMAGE alt='image' src='GUID-A2DAEE93-CE77-45A0-ABEE-9B9F2BBACA6F-a5.png']»Connect»Remote Access.
3. Click DataFinder Hierarchy to determine in which
 hierarchy the client displays the data.
4. Select User-defined to load your
 own model hierarchy with the file extension .dfh or
 .asamconfig. 
 To define and save DataFinder hierarchies, open the SCRIPT panel in DIAdem and
 click Settings»SystemLink TDM»DataFinder Hierarchy.

Parent topic:

Indexing Data

<!--NI_TOPIC bundle=systemlink-server path=displaying-metadata-of-system.html language=enus -->
## TOPIC 00076: Visualizing Metadata of a System

- bundle_id: `systemlink-server`
- source_path: `displaying-metadata-of-system.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/displaying-metadata-of-system.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Display and modify the metadata, such as the name, IP address, or model, associated with your system so you can interact with data more efficiently. Configure the Systems Management details in the SystemLink Web Application to display information important to you about your systems. In the SystemLin

### Visualizing Metadata of a System

Display and modify the metadata, such as the name, IP address, or model, associated with
 your system so you can interact with data more efficiently.

Configure the Systems Management details in
 the SystemLink Web Application to display information important to you about your
 systems.

1. In the SystemLink web application under Systems Management,
 click Systems.
2. Click a system to modify the metadata and the order in which it is
 displayed.
3. In the black ribbon, click Edit [IMAGE alt='image' src='GUID-AF0C5C1B-16A8-446A-B16D-39EF3338571B-a5.png'].
4. Add or remove properties in the order you want to display them.
5. Click Update.

Parent topic:

Managing Your Systems

Related tasks:

- Visualizing Data

<!--NI_TOPIC bundle=systemlink-server path=distributing-computing-nodes.html language=enus -->
## TOPIC 00077: Distributing Compute Nodes

- bundle_id: `systemlink-server`
- source_path: `distributing-computing-nodes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/distributing-computing-nodes.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: To control the utilization of server resources, specify the number of requests Data Preparation and Analysis Automation instances process in parallel. The total number of compute nodes you assign determines how many tasks Analysis Automation and Data Preparation can process in parallel. The limit is

### Distributing Compute Nodes

To control the utilization of server resources, specify the number of requests Data
 Preparation and Analysis Automation instances process in parallel.

Note

1. Optional: 
 In Data Preparation:
  1. Click Data Preprocessor Instances.
  2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Monitoring»Number of Parallel Requests to the Compute
 Nodes.
2. Optional: 
 In Analysis Automation:
  1. Click Instance on the dashboard.
  2. Click Settings»Number of Parallel Requests to the Compute
 Nodes.
3. Specify the maximum number of requests that this instance in Data
 Preparation or Analysis Automation can
 process in parallel.
4. Click OK.
5. Click Apply to accept the settings.

Parent topic:

Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

<!--NI_TOPIC bundle=systemlink-server path=enabling-access-to-new-file-types.html language=enus -->
## TOPIC 00078: Accessing Your Files with DataPlugins

- bundle_id: `systemlink-server`
- source_path: `enabling-access-to-new-file-types.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/enabling-access-to-new-file-types.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use DataPlugins to access your files with SystemLink for further processing, indexing, or analysis. NI provides more than 200 DataPlugins for common file formats for download. If you cannot find a DataPlugin for your file format, you can create your own. NI provides documentation and examples to cod

### Accessing Your Files with
 DataPlugins

Use DataPlugins to access your files with SystemLink for further processing, indexing,
 or analysis. NI provides more than 200 DataPlugins for common file formats for download. If
 you cannot find a DataPlugin for your file format, you can create your own. NI provides
 documentation and examples to code your plugin in VBS, Python, LabVIEW or C++.

| Goal | Task |
| --- | --- |
| Use ready DataPlugins from NI for common file formats. | Search for your file format and download the corresponding DataPlugin from the DataPlugins page on ni.com. |
| Create your own DataPlugin. | Follow the basic instructions and example code to create DataPlugins for NI software like SystemLink, DIAdem, or LabVIEW. Use the programming languages VBS for DataPlugins in DIAdem, Python, C++, or G. |
| Enable Data Preprocessor and DataFinder instances to scan and process specific file types with a dedicated DataPlugin. | Registering DataPlugins to Index and Process New File Types |
| Add a file extension to an already registered DataPlugin. | Adding File Extensions to a Registered DataPlugin |

Parent topic:

Generating Actionable Data Insights

Related tasks:

- Registering DataPlugins to Index and Process New File Types
- Adding File Extensions to a Registered DataPlugin

Related information:

- DataPlugins
- Python DataPlugins
- NI DataPlugin SDK for C++
- LabVIEW DataPlugin SDK

<!--NI_TOPIC bundle=systemlink-server path=enabling-client-access-to-packages.html language=enus -->
## TOPIC 00079: Enabling Client Access to Packages

- bundle_id: `systemlink-server`
- source_path: `enabling-client-access-to-packages.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/enabling-client-access-to-packages.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload packages you created to your SystemLink server for clients to access. In the SystemLink web application, click Package Repository. Click Create to create a new feed. You can also copy an existing feed by selecting Replicate and specifying the URL of the feed you want to copy. Enter details fo

### Enabling Client Access to Packages

Upload packages you created to your SystemLink server for clients to access.

1. In the SystemLink web application, click Package Repository.
2. Click 
 Create to create a new feed. 
 You can also copy an existing feed by selecting 
 Replicate and specifying the URL of the feed you want to copy.
3. Enter details for your feed. 
 Only users belonging to the workspace you specify will access the packages you
 upload.
4. Click Create.
5. Click [IMAGE alt='Gear icon.' src='GUID-D6237B29-557B-4209-9B43-FAF6DD22B3E8-a5.png'] next to the feed name.
6. In the Packages section, click
 Add to add packages to the server.

Next, deploy packages to clients to
 complete this workflow.

Parent topic:

Deploying Applications to Clients on a Server

Related tasks:

- Deploying Packages to Clients

<!--NI_TOPIC bundle=systemlink-server path=enabling-dataplugins-datafinder.html language=enus -->
## TOPIC 00080: Enabling DataPlugins to Index New File Types

- bundle_id: `systemlink-server`
- source_path: `enabling-dataplugins-datafinder.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/enabling-dataplugins-datafinder.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable DataPlugins to index new file types so you can use them with DataFinder instances. If you use an instance that indexes the file service, like the FileIndex instance, and there is no dedicated DataPlugin for a file type, SystemLink uses the NI_UNK_DP DataPlugin to index the file properties. Yo

### Enabling DataPlugins to Index New File Types

Enable DataPlugins to index new file types so you can use them with DataFinder
 instances. If you use an instance that indexes the file service, like the FileIndex
 instance, and there is no dedicated DataPlugin for a file type, SystemLink uses the
 NI_UNK_DP DataPlugin to index the file properties. You can only search
 on the file level of file service files which are indexed by this DataPlugin.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the DataPlugins tab, select an inactive DataPlugin
 and click Enable.
4. Click Apply to accept the settings. 
 Note If you enable several DataPlugins that
 index the same file extension, make sure that your DataPlugins recognize the
 file format they have been programmed for. All other file formats with the
 same file extension should throw an error. If a file is indexed multiple
 times by different DataPlugins, this may result in multiple search results
 for the same file.

Parent topic:

Preparing Data for Searching

<!--NI_TOPIC bundle=systemlink-server path=enabling-dataplugins-datapreprocessor.html language=enus -->
## TOPIC 00081: Specifying File Types to Be Scanned and Processed

- bundle_id: `systemlink-server`
- source_path: `enabling-dataplugins-datapreprocessor.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/enabling-dataplugins-datapreprocessor.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable DataPlugins to determine which file types a Data Preprocessor instance scans and processes. In Data Preparation, click Data Preprocessor Instances. Select an instance and click Manage. On the DataPlugins tab, select an inactive DataPlugin and click Enable. If you cannot find the DataPlugin yo

### Specifying File Types to Be Scanned and
 Processed

Enable DataPlugins to determine which file types a Data Preprocessor instance scans
 and processes.

1. In Data Preparation, click Data Preprocessor
 Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the DataPlugins tab, select an inactive DataPlugin
 and click Enable. 
 Note If you cannot find the DataPlugin you
 need, add a new DataPlugin in DataPlugins.
4. Click Apply to accept the settings. 
 Note If you enable several DataPlugins that
 process the same file extension, make sure that your DataPlugins recognize
 the file format they have been programmed for. All other file formats with
 the same file extension should then throw an error. If a file is processed
 multiple times by different DataPlugins, a warning displays in the
 processing status.

Parent topic:

Configuring a Data Preprocessor Instance

Related tasks:

- Accessing Your Files with DataPlugins

<!--NI_TOPIC bundle=systemlink-server path=enabling-sso.html language=enus -->
## TOPIC 00082: Enabling Single Sign-On in SystemLink

- bundle_id: `systemlink-server`
- source_path: `enabling-sso.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/enabling-sso.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure SystemLink to authenticate using OpenID Connect so users can access SystemLink with their existing credentials, identity, and access levels in your organization. Configure the claim to use as the SystemLink username before users begin using the server to avoid creating duplicate users and

### Enabling Single Sign-On in SystemLink

Configure SystemLink to authenticate using OpenID Connect so users
 can access SystemLink with their existing credentials, identity, and access levels in your
 organization.

Notice

Enabling OpenID Connect requires a SystemLink Advanced Server
 license. A user with the Server Administrator role must complete these steps.

1. In NI Web Server Configuration, on the Authentication tab,
 select Use OpenID Connect (advanced).
2. Click Apply and restart.
3. Navigate to the SystemLink web application and select Access Control»Roles»[IMAGE alt='Gear icon' src='GUID-F365AA0A-76E7-445B-BF21-BD366FEDA5D4-a5.png'].
4. Add an OpenID Connect Claim mapping for the Server Administrator role.
5. Log out and log back in as an OpenID Connect user with a mapping for the Server
 Administrator role and confirm they have the correct privileges.

After you enable single sign-on, you can map users to roles with
 their single sign-on credentials for your organization.

Parent topic:

Managing Access with OpenID Connect

Related tasks:

- Assigning Users to Roles in a Workspace

<!--NI_TOPIC bundle=systemlink-server path=examples.html language=enus -->
## TOPIC 00083: SystemLink Server Examples

- bundle_id: `systemlink-server`
- source_path: `examples.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/examples.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI installs example code with your software or driver that demonstrates the functionality of SystemLink Server. Use these examples to learn about the product or accelerate your own application development. Most NI products install examples that you can access directly or from within NI software. The

### SystemLink Server
 Examples

NI installs example code with your software or driver that demonstrates the
 functionality of SystemLink Server. Use these examples to learn about
 the product or accelerate your own application development.

Most NI products install examples that you can access directly or from within NI
 software. The example experience can differ slightly across products and
 versions.

SystemLink Server examples are located in the
 systemlink-server-examples GitHub repository.

| Example Folder Name | Description |
| --- | --- |
| dashboards | This example folder provides layouts and tile configurations for customized use. |
| jupyter | This example folder uses Jupyter notebook to exercise the different SystemLink Services APIs (Tag, File, TDMReader, and Test Monitor). |
| python/testmonitor | This example folder demonstrates how to access a SystemLink server through Python clients. |

Related information:

- SystemLink Server Examples on GitHub
- SystemLink Python API Reference

<!--NI_TOPIC bundle=systemlink-server path=excluding-custom-properties.html language=enus -->
## TOPIC 00084: Excluding Custom Properties

- bundle_id: `systemlink-server`
- source_path: `excluding-custom-properties.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/excluding-custom-properties.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Exclude custom properties from the index to save disk space and show only the most relevant information in the properties display in Data Navigation. You can either exclude all custom properties automatically, or manually select the custom properties you want to exclude. In Data Indexing, click Data

### Excluding Custom Properties

Exclude custom properties from the index to save disk space and show only the most
 relevant information in the properties display in Data Navigation. You can either exclude
 all custom properties automatically, or manually select the custom properties you want to
 exclude.

1. In Data Indexing, click DataFinder
 Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Custom Properties tab, determine whether you want
 to exclude custom properties on File,
 Group, or Channel level.
4. Choose one of the following options to exclude or reinclude properties in the
 index: 
 GoalInstructionsAutomatically exclude non-optimized and new properties
 Select the level (File,
 Group, or
 Channel).
 Switch the toggle to Autoexclude
 properties. Click
 OK.
 To reduce the physical index size after excluding properties,
 click Reset Index on the
 Index tab.
 Note Deoptimizing an
 optimized custom property automatically excludes it.Automatically reinclude properties
 Switch off the Autoexclude properties
 toggle.
 Optional: Click
 Reset Index to retroactively include
 excluded properties in the index.Manually exclude properties
 Select properties and click Exclude to
 remove the properties from the index.
 To reduce the physical index size after excluding properties,
 click Reset Index on the
 Index tab.Manually reinclude all properties
 Select the excluded properties and click
 Deoptimize.
 Click Reset Index on the
 Index tab to reinclude the properties
 of indexed files in the index.Note Reincluding
 custom properties in the index may significantly increase
 your index size.
5. Click Apply to accept the settings.

Parent topic:

Configuring File Indexing for a DataFinder Instance

<!--NI_TOPIC bundle=systemlink-server path=execute-data-analyzer-tasks.html language=enus -->
## TOPIC 00085: Executing Analysis Automation Tasks

- bundle_id: `systemlink-server`
- source_path: `execute-data-analyzer-tasks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/execute-data-analyzer-tasks.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Data Analysis to run analysis automation tasks. Data Analysis displays the manual tasks enabled in the Analysis Automation instance. In Data Analysis, click to open the task you want to run. If you cannot find the task you need: Switch to Analysis Automation. Click Tasks and check the status of

### Executing Analysis Automation Tasks

Use Data Analysis to run analysis automation tasks. Data
 Analysis displays the manual tasks enabled in the Analysis Automation instance.

1. In Data Analysis, click [IMAGE alt='image' src='GUID-36BC81B5-7EEC-4A10-8E6F-D6843D8601DD-a5.png'] to open the task you want to
 run. If you cannot find the task you need:
  1. Switch to Analysis Automation.
  2. Click Tasks and check the status of the task you
 want to view in Data Analysis.
  3. To enable the task, click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Enable.
2. Choose the data source on which you want to run the task. 
 OptionDescriptionPreconfigured data source
 Analyzes the data in the data source originally configured in Analysis
 Automation.Note If the data source is not available,
 complete steps 1a to 1b to check the status of the
 task.Selected elements in Data Cart
 Analyzes the data you select in Data Cart. To add data to
 Data Cart, search for data in Data
 Navigation, select the results you want to analyze, and
 click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Add to Data Cart.
3. Optional: 
 Click 
 [IMAGE alt='image' src='GUID-36BC81B5-7EEC-4A10-8E6F-D6843D8601DD-a5.png']Parameterization to change the values of parameters. For example, you can change the folder where Data Analysis stores the analysis result.
4. Click Run to execute the task.
5. Optional: 
 In Latest Results, click [IMAGE alt='image' src='GUID-6212E807-7A6D-412E-A834-6AAD529B16AF-a5.png'] to open the task history.
6. Optional: 
 If the analysis script in the Analysis Automation procedure contains the
 UploadResultFile command, you can preview the report and
 download the results in SystemLink File Viewer. Open
 Latest Results and click the link in the
 Results Preview column.

Parent topic:

Generating Actionable Data Insights

<!--NI_TOPIC bundle=systemlink-server path=exploring-data-with-DIAdem.html language=enus -->
## TOPIC 00086: Utilizing DIAdem Desktop Application with SystemLink

- bundle_id: `systemlink-server`
- source_path: `exploring-data-with-DIAdem.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/exploring-data-with-DIAdem.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the DIAdem desktop application for ad-hoc post-processing and in-depth, root-cause analysis of measurement data. View and investigate your data, transform it with analysis functions, and share results. DIAdem also helps engineers configure the SystemLink Data Preparation, Data Indexing, and Data

### Utilizing DIAdem Desktop Application with
 SystemLink

Use the DIAdem desktop application for ad-hoc post-processing and in-depth, root-cause
 analysis of measurement data. View and investigate your data, transform it with
 analysis functions, and share results.

DIAdem also helps engineers configure the SystemLink Data Preparation, Data
 Indexing, and Data Analysis applications.

| Goal | Data Management Task |
| --- | --- |
| Explore individual data sets. | Use DIAdem VIEW and DIAdem ANALYSIS panels in the DIAdem desktop application. |
| Search files on the SystemLink server from the DIAdem desktop application using SystemLink DataFinders. | Connect DIAdem with SystemLink and search for data. |
| Configure Data Indexing to specify the properties and the order in which they display in a client like Data Navigation or DIAdem. | Create a new DataFinder hierarchy in DIAdem SCRIPT and upload it to Data Indexing. |
| Configure Data Preparation to harmonize your data according to a set of rules you define. | Create a data preparation procedure in DIAdem SCRIPT and upload it to Data Preparation. |
| Configure Data Analysis to perform recurring analyses and create management reports for specific data. | Create an analysis automation procedure in DIAdem SCRIPT with VBS or Python and upload it to Analysis Automation. |
| Generate a SystemLink tag. | Generate the tag in a data preparation or an analysis automation procedure. To do so, refer to the programming reference for the SystemLink object-oriented script interface in the DIAdem help. |

Parent topic:

Generating Actionable Data Insights

Related tasks:

- Finding Data from DIAdem and LabVIEW Clients
- Displaying Data in a Different Hierarchy
- Updating Data Preparation Procedures
- Creating Analysis Automation Procedures in DIAdem

<!--NI_TOPIC bundle=systemlink-server path=exporting-saving-files.html language=enus -->
## TOPIC 00087: Exporting and Downloading Files

- bundle_id: `systemlink-server`
- source_path: `exporting-saving-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/exporting-saving-files.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Export the files you found to a zip file and download the file to your computer or make these files available for data analyses. In Data Navigation, select the DataFinder or the Federation instance and click . Create a Quick Search or an Advanced Search and run the search. In the search results list

### Exporting and Downloading Files

Export the files you found to a zip file and download the file to your computer or make these files available for data analyses.

1. In Data Navigation, select the DataFinder or the
 Federation instance and click [IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png'].
2. Create a 
 Quick Search or an 
 Advanced Search and run the search.
3. In the search results list, select the files you want to export. 
 Note Data Navigation always exports entire
 files, even if you only select groups or channels in the search results.
4. Export the files or make the files available for data analyses. 
 OptionDescription[IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png']»Export (Original Format)
 Exports the search results in the original format to a zip file. If you searched for
 data in the SystemLink file service, the exported zip file also contains
 a json file with the file service meta data of the exported
 file.[IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png']»Export As
 Exports the search results to a zip file in a format for which you have registered a writing DataPlugin.[IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png']»Show File
 Displays the search results in SystemLink File Viewer as a chart.[IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png']»Add to Data Cart
 Copies the search results to the Data Cart so that you can analyze these files with Data Analysis. 
 Note A zip file can contain a maximum of 200 files and must not be larger than 2 GB.
5. Change the filename of the zip file and click 
 OK.
6. Click 
 Downloads at the top of the window to open the Download Center. 
 Note After two weeks, Data Navigation deletes all zip files from the Download Center by default. Only an authorized user can change the specified 2 weeks by selecting 
 Global Settings»Data Navigation Environment Settings in 
 Data Indexing. Data Navigation does not delete files that have the 
 Processing status.
7. Select a zip file and click 
 [IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png']»Download to save the zip file on your computer.

Parent topic:

Retrieving Data from Your Data Stores

<!--NI_TOPIC bundle=systemlink-server path=extending-dashboards-python-javascript.html language=dede -->
## TOPIC 00088: Erweitern des Dashboard-Funktionsumfangs mit Python und JavaScript

- bundle_id: `systemlink-server`
- source_path: `extending-dashboards-python-javascript.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/dede/extending-dashboards-python-javascript.html
- source_language: `dede`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Sie können mit Hilfe von Python und JavaScript mehr Funktionsumfang zu Dashboards mit freiem Layout hinzufügen. Unabhängig davon, ob Sie auf Datenquellenaktualisierungen reagieren oder benutzerdefinierte Widgets erstellen möchten, Sie können eingeschränkten Python-Code oder einen JavaScript-Wrapper

### Erweitern des Dashboard-Funktionsumfangs mit Python und JavaScript

Sie können mit Hilfe von Python und JavaScript mehr Funktionsumfang zu Dashboards mit freiem Layout hinzufügen. Unabhängig davon, ob Sie auf Datenquellenaktualisierungen reagieren oder benutzerdefinierte Widgets erstellen möchten, Sie können eingeschränkten Python-Code oder einen JavaScript-Wrapper verwenden, um mehr mit Ihren Dashboards mit freiem Layout zu interagieren.

Hinweis

Führen Sie einen der folgenden Schritte aus, um Ihre Dashboard-Ziele zu erreichen.

- [Wiederverwenden von Skripten in einem Dashboard](adding-shared-scripts-to-dashboard.html) Sie können ein gemeinsam genutztes Python-Skript hinzufügen, das auf jedes Widget in Ihrem Dashboard angewendet werden kann.
- [Binden von virtuellen Tags an Widgets](binding-virtual-tags-to-widgets.html) Fügen Sie Ihrem Dashboard mit freiem Layout ein virtuelles Tag-Skript hinzu, um virtuelle Tags für die Bindung an ein Widget zu generieren.

Übergeordnetes Thema:

Darstellen von Tag-Daten in einem Dashboard mit freiem Layout

<!--NI_TOPIC bundle=systemlink-server path=federation.html language=enus -->
## TOPIC 00089: Searching for Data with Federated DataFinder Instances

- bundle_id: `systemlink-server`
- source_path: `federation.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/federation.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Federations to search for data across multiple DataFinder instances on your SystemLink Server or distributed servers. Clients, such as Data Navigation, DIAdem, or LabVIEW address their search queries to the Federation instance, which transfers the queries to the members of the Federation instanc

### Searching for Data with Federated DataFinder
 Instances

Use Federations to search for data across multiple DataFinder instances on your
 SystemLink Server or distributed servers.

Clients, such as Data Navigation, DIAdem, or LabVIEW address their search queries to the
 Federation instance, which transfers the queries to the members of the Federation instance.
 The members return their search results to the Federation instance, which combines the results
 and returns them to the client. Refer to *Forming a Federation from Multiple DataFinder
 Instances* to learn how to set up a Federation instance.

Note

Finding Data from DIAdem
 and LabVIEW clients

Parent topic:

Indexing Data

Related tasks:

- Creating a Federation of Multiple DataFinder Instances
- Finding Data from DIAdem and LabVIEW Clients

<!--NI_TOPIC bundle=systemlink-server path=file-formats-supported-in-file-preview.html language=enus -->
## TOPIC 00090: File Formats Supported in File Preview

- bundle_id: `systemlink-server`
- source_path: `file-formats-supported-in-file-preview.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/file-formats-supported-in-file-preview.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: SystemLink Server allows you to preview various file formats. Limitations on File PreviewThe file preview only supports files with a file size of less than 250 MB. Tests on the Monaco editor use a large file containing 400,000 lines. Each line has 100 words. Media Files If you are unable to preview

### File Formats Supported in File
 Preview

SystemLink Server allows you to preview various file
 formats.

#### Limitations on File Preview

Note

#### Media
 Files

Note

SystemLink Server

| Format | Description |
| --- | --- |
| .bmp | Bitmap |
| .gif | Graphics Interchange Format, an image format for animations |
| .jpg | Joint Photographic Experts Group |
| .png | Portable Network Graphics, an image format that supports transparency |

#### Text
 Files

| Format | Description |
| --- | --- |
| .csv | Comma-separated values file, a file format for saving tabular data as plain text |
| .html | Hypertext Markup Language file |
| .pdf | Portable Document Format |
| .tdm | NI file format for saving measurement data |
| .tdms | NI file format for saving measurement data |
| .txt | Plain text file |

Parent topic:

Storing and Managing Files

<!--NI_TOPIC bundle=systemlink-server path=filtering-between-systems-on-dashboard.html language=enus -->
## TOPIC 00091: Filtering Between Systems on a Dashboard

- bundle_id: `systemlink-server`
- source_path: `filtering-between-systems-on-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/filtering-between-systems-on-dashboard.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Change the system data a dashboard displays using a filter. Before you begin, verify you enabled system filtering on the dashboard when you configure a tile dashboard. You can use one dashboard to filter between systems. Filtering allows you to visualize data specific to the system you select. In th

### Filtering Between Systems on a
 Dashboard

Change the system data a dashboard displays using a filter.

Before you begin, verify you enabled system
 filtering on the dashboard when you configure a tile dashboard.

You can use one dashboard to filter between
 systems. Filtering allows you to visualize data specific to the system you
 select.

1. In the SystemLink web application, open the dashboard to change the system it
 displays.
2. Select the System drop-down and select the system you
 want to display on the dashboard. 
 The dashboard updates to show data from the system you
 selected.

Parent topic:

Visualizing Data on a Tile Dashboard

Related tasks:

- Visualizing Data on a Tile Dashboard

<!--NI_TOPIC bundle=systemlink-server path=filtering-test-results.html language=enus -->
## TOPIC 00092: Filtering Test Results

- bundle_id: `systemlink-server`
- source_path: `filtering-test-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/filtering-test-results.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Query test results to gain specific insights about your test data. In the SystemLink web application, click Test Insights. Click Test Results. Click Filter icon and specify the information you want to use to filter results. For Group by, choose how you want to organize this information. For Query by

### Filtering Test Results

Query test results to gain specific insights about your test data.

1. In the SystemLink web application, click Test Insights.
2. Click Test Results.
3. Click [IMAGE alt='Filter icon' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'] and specify the information you want to use to filter results. 
 
 The test results automatically filter to match the search configuration you
 specified.
  1. For Group by, choose how you
 want to organize this information.
  2. For Query by product and Query by
 result, choose the metadata, such as keyword or system, that you want
 the results to match.
4. Optional: 
 To access the query, or search configuration, on a recurring basis, click
 Save Query. 
 The query appears under Test Results on the
 sidebar.

Parent topic:

Analyzing and Interacting with Test Results

Related tasks:

- Generating Test Execution Reports

<!--NI_TOPIC bundle=systemlink-server path=filtering-your-assets.html language=enus -->
## TOPIC 00093: Filtering Your Assets

- bundle_id: `systemlink-server`
- source_path: `filtering-your-assets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/filtering-your-assets.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Query your assets or calibrated assets to gain specific insights about asset tracking and calibration compliance. In the SystemLink web application, click Systems Assets . Click Assets or Calibrated. Click and define the query you want to use to filter your assets or calibrated assets. Select the pr

### Filtering Your Assets

Query your assets or calibrated assets to gain specific insights about asset tracking and calibration compliance.

1. In the SystemLink web application, click Systems»Assets.
2. Click Assets or Calibrated.
3. Click 
 [IMAGE alt='image' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'] and define the query you want to use to filter your assets or calibrated assets.
  1. Select the property whose value you want to use to filter the results. 
 A property can be a name, model, model number, and more.
  2. Select the operation for how the property must correspond to the value. 
 Depending on the property you select, your query can only perform certain operations. 
 For example, if you want to query assets by their model or name, you can only perform the 
 matches operation.
  3. Specify the value of the property you want to use to filter the results.
4. Optional: 
 Repeat step 3 for as many times as you need to successfully filter your assets or calibrated assets.
5. To access the query, or search configuration, on a recurring basis, click
 Save Search. 
 The query appears under Assets or Calibrated
 Assets on the sidebar.

#### Example Query

| Property | Operator | Value |
| --- | --- | --- |
| Vendor | contains | NI |
| Slot Number | greater than or equal | 4 |

Parent topic:

Managing Your Assets

<!--NI_TOPIC bundle=systemlink-server path=filtering-your-systems.html language=enus -->
## TOPIC 00094: Filtering Your Systems

- bundle_id: `systemlink-server`
- source_path: `filtering-your-systems.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/filtering-your-systems.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Query your systems to create filtered views that you can reuse and share. In the SystemLink web application, click Systems Management Systems . Click systems. Click and define the query you want to use to filter your systems. Select the property whose value you want to use to filter the results. A p

### Filtering Your Systems

Query your systems to create filtered views that you can reuse and share.

1. In the SystemLink web application, click Systems Management»Systems.
2. Click systems.
3. Click [IMAGE alt='image' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'] and define the
 query you want to use to filter your systems.
  1. Select the property whose value you want to use to filter the results. 
 A property can be a name, model, model number, and more.
  2. Select the operation for how the property must correspond to the value. 
 Depending on the property you select, your query can only perform
 certain operations. 
 For example, if you want to query systems by whether they are locked, you can only
 perform the equals or does not
 equal operation.
  3. Specify the value of the property you want to use to filter the
 results.
4. Optional: 
 Repeat step 3 for as many times as you need to successfully filter your
 systems.
5. Click OK.
6. To access the view on a recurring basis, click the drop-down next to [IMAGE alt='image' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'] and select Save. Saving
 preserves your column, grouping, and sorting options as well.

#### Example Query

| Property | Operator | Value |
| --- | --- | --- |
| Vendor | contains | NI |
| Connection Status | equals | Connected |

Edit View

Create View

Parent topic:

Managing Your Systems

<!--NI_TOPIC bundle=systemlink-server path=finding-data-with-advanced-search.html language=enus -->
## TOPIC 00095: Finding Data with Advanced Search

- bundle_id: `systemlink-server`
- source_path: `finding-data-with-advanced-search.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/finding-data-with-advanced-search.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Advanced Search to find files, channel groups, or channels containing specified property values. Combine search conditions with logical operators to define complex search queries. If you want to search for custom properties, optimize them beforehand to make them searchable. In Data Navigation, s

### Finding Data with Advanced Search

Use Advanced Search to find files, channel groups, or channels containing specified
 property values. Combine search conditions with logical operators to define complex search
 queries.

If you want to search for custom properties, optimize them
 beforehand to make them searchable.

1. In Data Navigation, select the DataFinder or the
 Federation instance you want to search with and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect. 
 Note To search in the search areas of a
 DataFinder or Federation instance, the instance requires web access. An
 authorized user can enable web access in Data
 Indexing. To enable web access, select the instance, click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage. Then click [IMAGE alt='image' src='GUID-2BC6EFFE-2BE5-42FE-B822-F31ECB48B160-a5.png']»Connect»Remote Access, and on the Web Access tab enable
 Allow access to DataFinder through web
 connections.
2. Click the toggle button to enable the Advanced
 Search.
3. Click [IMAGE alt='image' src='GUID-240AE4D6-DBF9-477F-B7B2-CE427637128A-a5.svg']Add Search Condition to create a search condition.
  1. Enter a Label to name the search.
  2. Select the Level at which you want to search for
 the value of a property.
  3. Select the Property with the value you want to
 search for.
  4. Select an Operator.
  5. Enter the Value you are searching for. Click
 ... to open the list of available values for
 the property you want to search. Double-click a value to insert. 
 Refer to the following table for more advanced search methods: 
 Goal
 Search methodFind parts of search terms with
 wildcards
 Enter wildcards
 (* and
 ?), for example,
 exa*, when searching for
 text.
 Combine several search conditions
 Combine the search conditions with
 AND or
 OR. If you repeatedly click
 ... and add further
 values, Data Navigation combines the values with
 OR.
 Find a search term containing the
 text OR or
 AND
 In the search term, replace the
 text OR or
 AND with
 /OR or
 /AND.
 Note Advanced Search is
 case-insensitive.
  6. Click OK to add the search condition.
4. Add additional search conditions. 
 Note Data Navigation enters the
 logical operators according to the search conditions in the search input
 area. The names C1, C2,
 C3, ... refer to the
 individual search conditions. You can combine several search conditions with
 AND or OR. Use parentheses
 to specify the order of the evaluation.
5. Click Search. 
 The latest search results will replace those from the previous
 search.
6. Optional: 
 Save your search query to reuse it.
  1. Click Save or Save
 As.
  2. On the slide-out, enter a Name and a
 Description (optional), and choose a
 Workspace. 
 Note You cannot replace a query with a query
 that has the same name. To edit a query, click
 Load and select
 Edit from the [IMAGE alt='image' src='GUID-2BC6EFFE-2BE5-42FE-B822-F31ECB48B160-a5.png']More Options menu.
  3. Click OK. 
 This makes the search query available to all users in the
 specified workspace.

Working with Search Results

Parent topic:

Retrieving Data from Your Data Stores

Related concepts:

- Combining Search Conditions in an Advanced Search

Related tasks:

- Exporting and Downloading Files
- Finding Data with Quick Search
- Working with Search Results
- Making Custom Properties Searchable

<!--NI_TOPIC bundle=systemlink-server path=finding-data-with-quick-search.html language=enus -->
## TOPIC 00096: Finding Data with Quick Search

- bundle_id: `systemlink-server`
- source_path: `finding-data-with-quick-search.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/finding-data-with-quick-search.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Quick Search to find search terms in the file properties of a DataFinder instance. Perform a quick search if you only have partial search information or if you are unsure whether the information is in a file, channel group, or channel. In Data Navigation, select the DataFinder or the Federation

### Finding Data with Quick Search

Use Quick Search to find search terms in the file properties of a DataFinder instance.
 Perform a quick search if you only have partial search information or if you are unsure
 whether the information is in a file, channel group, or channel.

1. In Data Navigation, select the DataFinder or the
 Federation instance you want to search with and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect. 
 Note To search in the search areas of a
 DataFinder or Federation instance, the instance requires web access. An
 authorized user can enable web access in Data
 Indexing. To enable web access, select the instance, click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage. Then click [IMAGE alt='image' src='GUID-2BC6EFFE-2BE5-42FE-B822-F31ECB48B160-a5.png']ConnectRemote
 Access, and on the Web Access tab
 enable Allow access to DataFinder through web
 connections.
2. If the toggle is set to Advanced Search (right), click
 the toggle to disable Advanced Search (left).
3. Enter a search term in the search input box. 
 Goal
 SolutionFind multiple search terms
 Separate multiple search terms with spaces.
 Use wildcards to find parts of search terms
 Find parts of search terms with wildcards
 (* and ?).
 You can only use wildcards at the end of a search term, for
 example, exa*.
 Find numeric values
 Use Advanced Search. Quick Search always interprets
 search terms as text. For example, if you enter the search
 term 100, Data Navigation searches
 for the text 100 and not for the
 numeric value 100.
 Find search terms containing special characters
 Use Advanced Search. Quick Search replaces the special
 characters in a search term with spaces.
 Note Quick Search is case-insensitive.
4. Click 
 Search. 
 The latest search results will replace those from the previous
 search.

Properties Display

Data Cart

Working with Search Results

Parent topic:

Retrieving Data from Your Data Stores

Related tasks:

- Finding Data with Advanced Search
- Exporting and Downloading Files
- Working with Search Results

<!--NI_TOPIC bundle=systemlink-server path=forming-federation.html language=enus -->
## TOPIC 00097: Creating a Federation of Multiple DataFinder Instances

- bundle_id: `systemlink-server`
- source_path: `forming-federation.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/forming-federation.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Federations to access data from multiple DataFinder instances with a single search query. A Federation groups multiple DataFinder instances from the SystemLink or distributed servers and combines their search results. You can only access a Federation from Data Navigation if the federated DataFin

### Creating a Federation of Multiple DataFinder
 Instances

Use Federations to access data from multiple DataFinder instances with a single search
 query. A Federation groups multiple DataFinder instances from the SystemLink or distributed
 servers and combines their search results.

Note

1. In Data Indexing, click Federation
 Instances.
2. Click [IMAGE alt='image' src='GUID-240AE4D6-DBF9-477F-B7B2-CE427637128A-a5.svg']New»Federation Instance.
3. Enter a name for the Federation instance. Clients use the name to connect to
 the Federation instance.
4. Enable Export member connection automatically and click
 Finish.
5. Save the connection file of the Federation instance.
6. Switch to the Dashboard and click DataFinder
 Instances.
7. Select the DataFinder instance you want to add to the Federation instance and
 select [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Federation Membership.
8. Enable Join a Federation and click
 Add.
9. Select the Federation member connection file, click Open»OK.
10. Click Apply to accept the settings. 
 The Federation instance you added is now in the List of all joined
 Federation instances under
 Federation-Membership.
11. Optional: 
 Repeat steps 5 through 10 to add more DataFinder instances to the Federation. 
 Note To add a DataFinder
 instance to an existing Federation, select the Federation instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect»Export Federation Member Connection and save the connection file with the file extension
 *.fed to a place where you can access it from the
 DataFinder instance.

For a list of Federation instance members, switch to the Dashboard, click
 Federation Instances, select the instance, and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Members. For a list of all Federation instances which a DataFinder instance
 has joined, switch to the Dashboard, click DataFinder Instances, select the instance
 and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Federation Membership.

Note

Refresh

Parent topic:

Searching for Data with Federated DataFinder Instances

<!--NI_TOPIC bundle=systemlink-server path=generating-asset-reports.html language=enus -->
## TOPIC 00098: Generating Asset Reports

- bundle_id: `systemlink-server`
- source_path: `generating-asset-reports.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/generating-asset-reports.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create detailed reports about your assets using predefined Jupyter notebooks that install with NI SystemLink Asset Module. The Jupyter notebooks (.ipynb) contain documentation and Python code. When you execute a notebook in Asset Manager, the notebook returns the data as a report. In the SystemLink

### Generating Asset Reports

Create detailed reports about your assets using predefined Jupyter notebooks that
 install with NI SystemLink Asset Module.

.ipynb

1. In the SystemLink web application, click Systems»Reports.
2. Specify the information you want your report to contain.
  1. For Report, choose the
 type of information you want in your report.
  2. For Group
 by, choose how you want to organize this
 information.
  3. For Filter, choose the metadata and properties
 that you want the results to match.
3. Click Generate Report at the top of the page. 
 The graph updates with the data you queried.
4. To return to your full assets list, click Assets.

Parent topic:

Managing Your Assets

<!--NI_TOPIC bundle=systemlink-server path=generating-test-execution-reports.html language=enus -->
## TOPIC 00099: Generating Test Execution Reports

- bundle_id: `systemlink-server`
- source_path: `generating-test-execution-reports.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/generating-test-execution-reports.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create detailed test reports for analysis using predefined Jupyter notebooks that install with NI SystemLink Test Module. The installed Jupyter notebooks contain documentation and Python code. When you execute a notebook in Test Monitor, the notebook computes the prepared processes and returns the d

### Generating Test Execution Reports

Create detailed test reports for analysis using predefined Jupyter notebooks that install with NI SystemLink Test Module.

The installed Jupyter notebooks contain documentation and Python code. When you execute a
 notebook in Test Monitor, the notebook computes the prepared processes and returns the data
 as a report in Test Insights.

If you want to modify or create a Jupyter notebook to generate reports
 specific to the needs of your team, refer to *Customizing Test Reports with
 JupyterHub* or *Creating a New Jupyter Notebook* in this manual
 for more information.

1. In the SystemLink web application, click Test Insights.
2. Click 
 Reports.
3. Specify the information you want your report to contain.
  1. For Report, choose the
 type of information you want in your report.
  2. For Group
 by, choose how you want to organize this
 information.
  3. For Query by product and Query by
 result, choose the metadata, such as keyword or system,
 that you want the results to match.
4. Click 
 Generate Report.
5. To access your report later, click Save
 Report. 
 The report appears under Reports on the sidebar.
6. To return to your full results list, click 
 View Results.

Parent topic:

Analyzing and Interacting with Test Results

Related tasks:

- Filtering Test Results

<!--NI_TOPIC bundle=systemlink-server path=hosting-a-web-vi.html language=enus -->
## TOPIC 00100: Hosting a WebVI in SystemLink

- bundle_id: `systemlink-server`
- source_path: `hosting-a-web-vi.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/hosting-a-web-vi.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Host a WebVI in SystemLink to securely share it with users on the server. Before hosting a WebVI in SystemLink, create a package (.nipkg) in G Web Development Software that contains the WebVI. In SystemLink web application, click Custom Applications Web Applications . Click IMPORT. Select the packag

### Hosting a WebVI in SystemLink

Host a WebVI in SystemLink to securely share it with users on the
 server.

.nipkg

1. In SystemLink web application, click Custom Applications»Web Applications.
2. Click IMPORT.
3. Select the package you want to upload from your local machine. 
 The WebVI you import must be 100 MB or smaller.
4. Select the workspace you want to host the WebVI in.
5. Click UPLOAD.
6. Click the WebVI to run it.
7. To update an existing WebVI, select the WebVI and click [IMAGE alt='image' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png'] and select
 Update.

Users in the workspace you selected who have WebVI permissions can interact with the
 WebVI you uploaded.

Parent topic:

Sharing Data

Related tasks:

- Creating a Package of Your Web Application in G Web Development Software or LabVIEW NXG Web Module
- Creating Packages with LabVIEW Package Builder
- Hosting a Web Application on the NI Web Server

<!--NI_TOPIC bundle=systemlink-server path=hosting-ni-web-server.html language=enus -->
## TOPIC 00101: Hosting a Web Application on the NI Web Server

- bundle_id: `systemlink-server`
- source_path: `hosting-ni-web-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/hosting-ni-web-server.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: To make your application available to other users, host your build output on a web server that is accessible to other users. This topic demonstrates hosting WebVIs as simple static files with limited access control options. Instead it is recommended to leverage the Web Applications service for permi

### Hosting a Web Application on the NI Web
 Server

To make your application available to other users, host your build output on a web
 server that is accessible to other users.

Note

- Remove the URL, username, and password from the
 panel and the diagram to maximize the security of your web application. Refer to the
 Hosting Authentication Credentials Securely section of Security in NI Web
 Technology for more information.

NI SystemLink and G Web Development Software both use NI Web Server. Complete the
 following steps to host your web application on NI Web Server.

1. Open your web application project (.gwebproject).
2. Locate the NI Web Server root directory. 
 Open File»Preferences on the Web Server tab of the NI Web Server option
 note the root directory path. 
 Here is an example of a root directory path: C:\Program Files\National
 Instruments\Shared\Web Server\htdocs\.
3. Copy your entire web application output directory into the root directory. 
 To navigate to your web application output on your machine, open your web application
 component and on the Document tab click the path shown under Build Information»Output directory.
4. Open a web browser and navigate to
 http://localhost/WebApp_Web%20Server/Main.html,
 localhost is the IP address of the server and
 Main.html is the file name of the top-level
 WebVI in your web application.

Parent topic:

Sharing Data

Related information:

- Enabling SystemDesigner Visibility
- Considerations for Packaging a Web Application
- Security in NI Web Technology

<!--NI_TOPIC bundle=systemlink-server path=indexing-files-for-searching.html language=enus -->
## TOPIC 00102: Maintaining DataFinder Instance Index Manually

- bundle_id: `systemlink-server`
- source_path: `indexing-files-for-searching.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/indexing-files-for-searching.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: In some cases you may need to trigger the indexing process of a DataFinder instance index manually. In Data Indexing, click DataFinder Instances. Select an instance and click ManageIndex. Select Index Now to synchronize all files. This option is not available for instances dedicated to the SystemLin

### Maintaining DataFinder Instance Index
 Manually

In some cases you may need to trigger the indexing process of a DataFinder instance index manually.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Index.
3. Select Index Now to synchronize all files. This option
 is not available for instances dedicated to the SystemLink file service.
4. Optional: 
 Click Reset Index and choose one
 of the actions from the following table to delete and recreate the index. This
 process may take a while depending on the amount of data. 
 Parameter
 DescriptionEntire Index
 Deletes the entire index and re-indexes all files.
 Files with Indexing Status
 Files Timed Out During
 Indexing - Resets the index of the
 files whose indexing has exceeded the maximum
 specified time and re-indexes the files.
 Files with Indexing Errors
 - Resets the index of all files with indexing errors
 and re-indexes the files.
 Files with Unsuitable
 DataPlugin - Resets the index of all
 files indexed with an unsuitable DataPlugin and
 re-indexes the files.
5. Optional: 
 Select one of the actions from the following table to
 optimize the index for custom properties or recreate the Quick Search index. 
 Parameter
 DescriptionOptimize Index
 Optimizes the index to speed up the search performance.
 Recreate Quick Search Index
 Recreates only the index of the Quick Search. Clients use
 the Quick Search if they only have parts of the information
 they are searching for, or if they do not know whether the
 information they are searching for is in a file, a channel
 group, or a channel. Click Reset Index»Recreate Quick Search Index.

Parent topic:

Configuring File Indexing for a DataFinder Instance

<!--NI_TOPIC bundle=systemlink-server path=installation-guide.html language=enus -->
## TOPIC 00103: SystemLink Quick Installation Guide

- bundle_id: `systemlink-server`
- source_path: `installation-guide.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/installation-guide.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Install and configure a SystemLink instance with a single-seat license. You can use this instance to begin managing systems and working with data. SystemLink installs on a single-purpose Windows server. The system specifications required to operate SystemLink varies based on workload. Before install

### SystemLink Quick Installation Guide

Install and configure a SystemLink instance with a single-seat license. You can use this
 instance to begin managing systems and working with data.

SystemLink installs on a single-purpose Windows server.

Note

Uploading Files to Amazon Simple Storage
 Service

Based on the your SystemLink license size, ensure you have dedicated hardware that
 matches the following specifications:

| Specification | Small | Medium |
| --- | --- | --- |
| Processor | 4+ cores | 8+ cores |
| RAM | 16+ GB | 32+ GB |
| Disk Space | 128+ GiB | 256 + GiB |
| Recommended Amazon EC2 Instance Type | t3.xlarge | t3.2xlarge |

1. Download and open SystemLink.
2. Select the application software version, add-ons, and any additional
 items. 
 Note Select the following options for a SystemLink
 license. A SystemLink Server license allows for the selection of additional
 options.NI SystemLink Core Services
 NI SystemLink Server - Software Configuration
 Module
 NI SystemLink Server - JupyterHub Module
 NI SystemLink Server - Test Module
 NI SystemLink Server - Asset Module
3. Install SystemLink by reviewing and accepting the SystemLink Server license
 agreements.
4. Verify the software license and the activation status through NI
 License Manager. 
 You can use online or offline activation to license your server.
5. Configure SystemLink for secure connectivity.
  1. Open NI Web Server Configuration.
  2. In the Authentication tab, specify your login
 options. 
 These options control how users log into SystemLink. Allow
 administrator access to SystemLink by setting an administrator
 password. Granting administrator access does not consume a user
 license. Note To enable a simple login setup,
 specify the following: Allow a login through a Windows account
 Allow a login by local and active directory usersYou can also allow users to connect through an LDAP
 server or through OpenID Connect. For more information on
 these configurations, refer to the *SystemLink
 Operations Handbook*.
  3. In the HTTPS tab, specify the security
 certificate. 
 You can obtain a certificate through a certificate authority, such as
 *Let's Encrypt*, or from your IT department.
 Note When generating a certificate, you can use
 the NI Web Server Configuration workflow,
 *Create a certificate signing request*. This workflow
 streamlines the certificate request process and eliminates common
 errors.
  4. Install the certificate through NI Web Server
 Configuration.
  5. Click Apply.
  6. Restart SystemLink.
6. Ensure the security certificate defines the preferred host name.
  1. In NI Web Server Configuration, navigate to the
 HTTPS tab and click View
 certificate.
  2. In the View Certificate dialog box, click
 Details.
  3. In the Details tab, ensure the host name and DNS
 name are correct in the Subject Alternative Name
 field.
7. Enable email notifications by configuring the SMTP settings.
  1. Open NI SystemLink Server Configuration.
  2. Under NI SystemLink Service Manager, select the
 SMPT service.
  3. Set the Host to your preferred SMTP service
 address. For example, you can set the host to
 outlook.office365.com.
  4. Configure the remaining fields as required by your chosen SMTP
 service.
  5. Send a test email to ensure that you have properly configured the
 settings.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Uploading Files to Amazon Simple Storage Service (S3)

Related information:

- Download SystemLink
- Download Let's Encrypt
- SystemLink Operations Handbook

<!--NI_TOPIC bundle=systemlink-server path=installing-python-modules.html language=enus -->
## TOPIC 00104: Installing Additional Python Modules

- bundle_id: `systemlink-server`
- source_path: `installing-python-modules.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/installing-python-modules.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use third-party Python modules to further customize your test reports. In a Jupyter notebook cell on your host machine, type !pip install <package-name>, where <package-name> is the name of the package in PyPI you want to install. Execute the step. The package installs on the server. If you upgrade

### Installing Additional Python Modules

Use third-party Python modules to further customize your test reports.

1. In a Jupyter notebook cell on your host machine, type !pip install
 <package-name>, where
 <package-name> is the name of the package in PyPI you want to
 install.
2. Execute the step. 
 The package installs on the server. Note If you upgrade to a newer version of
 SystemLink, you must reinstall any Python modules.

For information on how to use a specific Python module,
 refer to the documentation for the module you install.

Parent topic:

Reporting Data with Jupyter Notebooks

<!--NI_TOPIC bundle=systemlink-server path=installing-python.html language=enus -->
## TOPIC 00105: Installing Additional Python Packages

- bundle_id: `systemlink-server`
- source_path: `installing-python.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/installing-python.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: If you need additional Python packages to run your analysis automation tasks, you can extend the SystemLink Python environment. Before you begin, go to the Python Package Index repository (PyPI) to determine the name of the package you want to install. Log in to SystemLink as administrator. Open Win

### Installing Additional Python Packages

If you need additional Python packages to run your analysis automation tasks, you can
 extend the SystemLink Python environment.

Before you begin, go to the Python Package Index repository
 (PyPI) to determine the name of the package you want to install.

1. Log in to SystemLink as administrator.
2. Open Windows command prompt.
3. Change the work directory to C:\Program Files\National
 Instruments\Shared\Skyline\Python\<latest version>.
4. Execute the command python -m pip install
 <package>, where <package> is the name of the
 package in PyPI you wish to install.

Parent topic:

Creating Analysis Automation Procedures in DIAdem

Related information:

- PyPI

<!--NI_TOPIC bundle=systemlink-server path=integrating-with-teststand.html language=enus -->
## TOPIC 00106: Integrating Test Monitor with TestStand

- bundle_id: `systemlink-server`
- source_path: `integrating-with-teststand.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/integrating-with-teststand.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Send test metadata from TestStand to your SystemLink server. To integrate SystemLink with TestStand, install a supported version of TestStand and SystemLink Client on your system. Installing SystemLink Client on the test system automatically installs the Test Monitor Client plug-in for TestStand. In

### Integrating Test Monitor with TestStand

Send test metadata from TestStand to your SystemLink server.

To integrate SystemLink with TestStand,
 install a supported version of TestStand and SystemLink Client on your system.

Installing SystemLink Client on the test
 system automatically installs the Test Monitor Client plug-in for TestStand.

1. In the TestStand Sequence Editor, open a test sequence.
2. Click Configure»Result Processing and enable the NI SystemLink Test Monitor Client plug-in. 
 Note If the plug-in does not appear under
 Result Processing, select Show More Options»Insert New [IMAGE alt='Insert New icon (blue plus).' src='GUID-2634C82C-B433-4184-A772-6587825E68EE-a5.png'].
 [IMAGE alt='TestStand Result Processing dialog showing NI SystemLink Test Monitor Client selected.' src='GUID-5ED6C877-9BBB-49FA-BB33-00529ED3E2D5-a5.png']
 Tip Click Options
 [IMAGE alt='Options button icon (wrench and screwdriver).' src='GUID-A0F49F02-CE84-4AA9-8532-C76914258CA8-a5.png'] to configure the NI SystemLink Test Monitor Client plug-in. This
 configuration enables a variety of reporting options, such as tracking utilization
 information, storing test data on the client, and more.
3. Open SystemLink and click Test Insights. 
 The Test Insights Dashboard shows high-level insights for
 tests associated with your managed systems. Test results update this dashboard in real
 time.
4. Send test reports from TestStand to download in the SystemLink web application.
  1. In TestStand, click Configure»Result Processing.
  2. In Report, click Options [IMAGE alt='Options button icon (wrench and screwdriver).' src='GUID-A0F49F02-CE84-4AA9-8532-C76914258CA8-a5.png'].
  3. In the Report Format drop-down, select HTML
 Document and click OK.
  4. Run the test sequence you want to send a report for. 
 Note You can run tests
 sequentially or in parallel. TestStand automatically creates all necessary tags to
 monitor values for each instance of the test sequence. You can view these tags in
 the SystemLink web application under Tags.
  5. In SystemLink Test Insights, click Results.
  6. Select the test and then click Download Attachments.

You can view any files from TestStand in Files. If the file is a
 TDMS file, you can select the file and click Preview to view
 additional information.

Tip

Parent topic:

Monitoring Tests

Related tasks:

- Publishing Test Results with the Test Monitor API
- Storing and Forwarding Test Data
- Managing Your Assets

<!--NI_TOPIC bundle=systemlink-server path=licensing-and-activating-systemlink-products.html language=enus -->
## TOPIC 00107: Licensing and Activating SystemLink Products

- bundle_id: `systemlink-server`
- source_path: `licensing-and-activating-systemlink-products.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/licensing-and-activating-systemlink-products.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: License and activate your SystemLink products. Ensure that you have set up a SystemLink server. Complete the steps for the tool you want to use. Option Description Single Seat License Activate a SystemLink small or medium license through NI License Manager. Volume License Manager Complete steps 1-4

### Licensing and Activating SystemLink
 Products

License and activate your SystemLink products.

Ensure that you have set up a SystemLink server.

1. Complete the steps for the tool you want to use. 
 Option
 DescriptionSingle Seat License
 Activate a SystemLink small or medium license through NI License
 Manager.
 Volume License Manager
 Complete steps 1-4 of *Getting Started With NI Volume License Manager
 (NI VLM)*.
 Open NI VLM and click Licenses.
 If any of your licenses list Named-User as the license model, contact
 services@ni.com to request that they update the license model to one of the
 following settings.License
 ModelSystemLink TDM
 Computer-Based (not concurrent)
 Other
 Unmanaged Concurrent
 If any of your SystemLink licenses list Computer-Based as the license
 model, complete the process for *Getting Started with NI VLM: Adding
 Client Permissions* to assign permissions to your SystemLink
 server.
 FlexNet Tools
 Complete the process for *Getting Started with FlexNet Publisher
 Configuration*.
 If any of your SystemLink licenses list Computer-Based as the license
 model, complete the process for *Construct Options File for FlexNet
 Publisher* to assign permissions to your SystemLink server.
2. Open NI License Manager and navigate to the Network Licenses
 tab.
3. If you don't see license and licensing server information, use the troubleshooting
 articles. If you still cannot see the license information, contact NI Technical
 Support.
4. Open NI SystemLink Server Configuration and select NI SystemLink Service Manager»Restart to restart all your SystemLink services.

Related tasks

Related information

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Setting Up a SystemLink Server
- Connecting a Windows Target to Your SystemLink Server
- Connecting an NI Linux Real-Time Target to Your SystemLink Server

Related information:

- Getting Started With NI Volume License Manager (VLM)
- Getting Started with NI VLM: Adding Client Permissions
- Getting Started with FlexNet Publisher Configuration
- Construct Options File for FlexNet Publisher
- Troubleshooting: Unable to Communicate With License Server Error in NI
 VLM
- Troubleshooting: NI License Manager Hangs When Querying a Volume License
 Server

<!--NI_TOPIC bundle=systemlink-server path=licensing-systemlink.html language=enus -->
## TOPIC 00108: Purchasing SystemLink Licenses

- bundle_id: `systemlink-server`
- source_path: `licensing-systemlink.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/licensing-systemlink.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Choose a SystemLink licensing option based on your goals and assign those licenses to your systems. With SystemLink 2025 Q3 and later, the following license options are available. License Users Nodes SystemLink Base - Small 5 10 SystemLink Base - Medium 10 25 SystemLink Server - Volume License Manag

### Purchasing SystemLink Licenses

Choose a SystemLink licensing option based on your goals and assign those licenses to
 your systems.

With SystemLink 2025 Q3 and later, the following license options are available.

| License | Users | Nodes |
| --- | --- | --- |
| SystemLink Base - Small | 5 | 10 |
| SystemLink Base - Medium | 10 | 25 |
| SystemLink Server - Volume License Manager | Variable | Variable |

The number of user licenses and node licenses are fixed in a SystemLink Base license
 agreement. To complete a license activation, use ni.com or NI License
 Manager. The number of users licenses or nodes licenses are customizable to fit
 your requirements in a volume license agreement for SystemLink Server. To complete a license
 activation, use NI Volume License Manager.

After activating a single-seat license, a SystemLink Base license allows a specified number
 of users and nodes. These licenses also allow a few additional user accounts and node
 accounts for temporary variability. SystemLink relinquishes user licenses after a 30-day
 period of login inactivity. Node licenses are immediately available after removing the
 associated system through the Systems application.

For simple installation and simple activation, NI recommends a SystemLink Base Small or
 Medium license. If you need additional users or nodes, consider the following tables to
 determine the installation option that fits your needs.

1. Install NI Volume License Manager. 
 The computer that you install with Volume License Manager becomes a
 *license server*.
2. Determine the installation option fits your needs. 
 Number of SystemLink Servers
 Installation Option
 Description1
 Install VLM on the same computer as SystemLink
 Server.
 Reduces network complexity
 Ensures SystemLink Server and VLM can always communicate
 1
 Install VLM on a remote computer, separate from SystemLink
 Server
 Allows you to use an existing license server
 Requires connectivity between both machines
 Multiple
 Install VLM with each SystemLink Server installation
 Reduces network complexity
 Specifies node seat quantity for each server
 Requires multiple license agreements
 Multiple
 Install VLM on one license server for multiple SystemLink Server
 installations
 Connects multiple SystemLink Servers and nodes to a single license
 server
 Enables transferring licenses among servers
3. Determine whether you need a standard or advanced server license for SystemLink. 
 Use Case
 Server License TypeOne server with one workspace for all your data and systems
 All machines are in the same location
 Standard
 Users in your organization need varying levels of access to different data
 sets all on one server
 Users in your organization can access SystemLink with their existing
 OpenID Connect credentials
 Your machines are in various locations
 Advanced
4. Purchase the server, user, and node licenses you need. 
 SystemLink requires three license types.
 License type
 DescriptionServer (Standard or Advanced)
 Use a server license for each SystemLink server.
 Module node
 Use a module node license for each SystemLink module.
 Examples of modules include the Software Configuration Module, Asset Module, and
 Test Module.
 Module user
 Use a module user license for each user who accesses a
 module.

| Scenario | Licensing requirements |
| --- | --- |
| 5 Validation benches running Windows 5 PXI test systems 1 central server with SystemLink | SystemLink Base - Small |
| 10 Windows PCs 15 CompactRIO devices 1 central server with SystemLink | SystemLink Base - Medium |
| 1 server for production 1 server for development 50 PC-based test systems for production 10 targets for development The production system and development system use different license servers | License server 1 Volume License Manager: 1 seat SystemLink Server: 1 seat SystemLink Module Node: 50 seats SystemLink Module User: 5 seats License server 2 Volume License Manager: 1 seat SystemLink Server: 1 seat SystemLink Module Node: 10 seats SystemLink Module User: 1 seat |
| 3 servers to support 3 sites Each site has 100 PXI test systems All systems will use 1 central machine as a license server | Volume License Manager: 1 seat on remote machine SystemLink Server: 3 seats SystemLink Module Node: 300 seats SystemLink Module User: 10 seats |

After licensing SystemLink, continue the setup process for
 your server and clients.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Installing and Configuring SystemLink Server and Clients
- Setting Up a SystemLink Server

Related information:

- Volume License Manager

<!--NI_TOPIC bundle=systemlink-server path=loading-data-preparation-procedures.html language=enus -->
## TOPIC 00109: Updating Data Preparation Procedures

- bundle_id: `systemlink-server`
- source_path: `loading-data-preparation-procedures.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/loading-data-preparation-procedures.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload a new data preparation procedure to replace the existing one. Data preparation procedures define how the Data Preprocessor instance harmonizes your raw data from various data formats and sources. In Data Preparation, click Data Preprocessor Instances. Select an instance and click Manage. On t

### Updating Data Preparation Procedures

Upload a new data preparation procedure to replace the existing one. Data preparation
 procedures define how the Data Preprocessor instance harmonizes your raw data from various
 data formats and sources.

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Procedure tab, click Update
 Procedure, select a data preparation procedure, and click
 Open.
4. Enable 
 Reprocess all files in the raw data areas after upload to harmonize the raw data with the new procedure.
5. Click 
 OK.

Parent topic:

Configuring a Data Preprocessor Instance

Related tasks:

- Creating Data Preparation Procedures in DIAdem

<!--NI_TOPIC bundle=systemlink-server path=locally-controlling-software-updates-on-client-system.html language=enus -->
## TOPIC 00110: Controlling Software Updates on a Client

- bundle_id: `systemlink-server`
- source_path: `locally-controlling-software-updates-on-client-system.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/locally-controlling-software-updates-on-client-system.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Lock a client locally to ensure that software installations do not occur while you are working on the client. Before you begin, install SystemLink Client on the client and connect it to your SystemLink Server. Log into the client system. Launch the NI SystemLink Client Tray. On the Windows toolbar,

### Controlling Software Updates on a
 Client

Lock a client locally to ensure that software installations do not occur while you are
 working on the client.

Before you begin, install SystemLink Client on the client and
 connect it to your SystemLink Server.

1. Log into the client system.
2. Launch the NI SystemLink Client Tray.
3. On the Windows toolbar, right-click NI SystemLink
 Notifications [IMAGE alt='image' src='GUID-F1E1C19B-640D-4AC4-B206-D71F5EF05FF2-a5.png'] in the system tray.
4. Click Lock.
5. When you complete your work, right-click [IMAGE alt='image' src='GUID-F1E1C19B-640D-4AC4-B206-D71F5EF05FF2-a5.png'] and select
 Unlock.

After you unlock the client system,
 any software update the server has deployed will install.

Note

.lock

| OS | Location |
| --- | --- |
| Windows | C:\\ProgramData\\National Instruments\\salt\\conf\\lock |
| RT | /var/lib/salt/minion/blackout |

Parent topic:

Deploying Applications to Clients on a Server

Related tasks:

- Connecting a Windows Target to Your SystemLink Server

<!--NI_TOPIC bundle=systemlink-server path=managing-access-with-openid-connect.html language=enus -->
## TOPIC 00111: Managing Access with OpenID Connect

- bundle_id: `systemlink-server`
- source_path: `managing-access-with-openid-connect.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/managing-access-with-openid-connect.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure SystemLink to use OpenID Connect to authorize users and use a common identity for users across multiple applications. This allows SystemLink to leverage corporate single sign-on and all its security benefits, such as streamlined login and limiting user credential proliferation. You

### Managing Access with OpenID Connect

You can configure SystemLink to use OpenID Connect to authorize users and
 use a common identity for users across multiple applications. This allows
 SystemLink to leverage corporate single sign-on and all its security benefits, such as
 streamlined login and limiting user credential proliferation. You can use OpenID Connect
 alongside or as a replacement for LDAP, Active Directory, and local Windows accounts for
 authentication.

1. Configuring SystemLink to Connect to Your OpenID Connect Provider Create the configuration files SystemLink uses to connect to your OpenID Connect provider.
2. Configuring Your OpenID Connect Provider to Connect to SystemLink Specify the redirect URL that the client configuration for your provider will use at login.
3. Enabling Single Sign-On in SystemLink Configure SystemLink to authenticate using OpenID Connect so users can access SystemLink with their existing credentials, identity, and access levels in your organization.
4. Viewing Claims for OpenID Connect Users You can use claims to assign OpenID Connect users to roles and to update their SystemLink username.
5. Configuring the SystemLink Username for OpenID Connect Users Assign a more readable username to OpenID Connect users.
6. Assigning User Claims to Roles in a Workspace Create custom experiences for each type of user on the server by specifying which role a user has and which workspaces they can access.
7. Supported Signing and Encryption Algorithms SystemLink supports the following algorithms for ID token signing, ID token key management encryption, and ID token content encryption.
8. Troubleshooting Failed OpenID Connect Authentication Use OpenID Connect provider logs and NI Web Server logs to resolve common authentication issues.

Parent topic:

Managing Access to SystemLink

<!--NI_TOPIC bundle=systemlink-server path=managing-access.html language=enus -->
## TOPIC 00112: Managing Access to SystemLink

- bundle_id: `systemlink-server`
- source_path: `managing-access.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/managing-access.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: As a system administrator, specify which parts of Systemlink different users can access through workspaces, roles, and privileges.

### Managing Access to SystemLink

As a system administrator, specify which parts of Systemlink different users can access
 through workspaces, roles, and privileges.

- [Managing Access with OpenID Connect](managing-access-with-openid-connect.html) You can configure SystemLink to use OpenID Connect to authorize users and use a common identity for users across multiple applications.
- [Creating a Workspace](creating-a-workspace.html) Create a workspace to control which systems and data different types of users can interact with.
- [Configuring a Role and Privileges](configuring-roles-privileges.html) Create a role and assign privileges to the role to customize how users can interact with each SystemLink application and service.
- [Assigning Users to Roles in a Workspace](mapping-roles.html) Create custom experiences for each type of user on the server by specifying which role a user has and which workspaces they can access.
- [Adding Users to a Workspace Without Using an Identity Provider](adding-users-without-idp.html) As a workspace owner, add users to workspaces and manually specify roles without creating a mapping to an identity provider (IdP). This increases flexibility when managing workspace membership and roles.
- [Archiving Your Workspaces](archiving-workspaces.html) Store your workspaces when your organization is no longer using them.
- [Role-Based Access Control Concepts](access-control-glossary.html) Understand workspaces, roles, and privileges in SystemLink to organize your data and tailor SystemLink Web Application to different types of users.
- [Predefined Roles in SystemLink](predefined-roles.html) Control access to your server more easily using roles related to common use cases.

Related tasks:

- Creating a Workspace
- Configuring a Role and Privileges

Related reference:

- Role-Based Access Control Concepts

<!--NI_TOPIC bundle=systemlink-server path=managing-asset-utilization-tracking-on-a-client.html language=enus -->
## TOPIC 00113: Tracking Asset Utilization on a Client

- bundle_id: `systemlink-server`
- source_path: `managing-asset-utilization-tracking-on-a-client.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/managing-asset-utilization-tracking-on-a-client.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Automatically track asset utilization when you log into a client system. This level of tracking allows you to minimize changes to VIs or scripts. The utilization of an asset shows the percentage of time your team used the asset to perform tests and automated measurements. Your client system must hav

### Tracking Asset Utilization on a Client

Automatically track asset utilization when you log into a client system. This level of
 tracking allows you to minimize changes to VIs or scripts.

The *utilization* of an asset shows the percentage of time your team used
 the asset to perform tests and automated measurements.

Note

1. Log into the client system.
2. On the Windows toolbar, right-click NI SystemLink
 Notifications [IMAGE alt='image' src='GUID-F1E1C19B-640D-4AC4-B206-D71F5EF05FF2-a5.png'] in the system tray.
3. Refer to the following table to enable, disable, or modify asset utilization
 tracking on the client. 
 Goal
 InstructionsEnable automatic asset utilization tracking
 Click Automatically Start Asset
 Utilization»Enable Automatic Tracking.
 Select either All assets or
 System Controller.
 The client system tracks the asset(s) you selected until
 you lock, log out, close the remote session, or shut
 down the system.
 Disable automatic asset utilization tracking
 Click Automatically Start Asset
 Utilization»Disable Automatic Tracking.
 Click Yes.
 The client system stops tracking the asset(s) you
 selected.
 Modify the asset(s) you track
 Click Automatically Start Asset
 Utilization»Disable Automatic Tracking.
 Click Yes.
 Click Automatically Start Asset
 Utilization»Enable Automatic Tracking.
 Select either All assets or
 System Controller.
 The client system tracks the asset(s) you selected until
 you lock, log out, close the remote session, or shut
 down the system.

The next time you log into the client system, the type of
 asset utilization tracking you configured persists. You can view the asset utilization
 chart on a dashboard or in a report in Asset Manager.

Parent topic:

Managing Your Assets

Related reference:

- SystemLink Client 2025 Q3 Changes

<!--NI_TOPIC bundle=systemlink-server path=managing-instances.html language=enus -->
## TOPIC 00114: Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

- bundle_id: `systemlink-server`
- source_path: `managing-instances.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/managing-instances.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create backups, restore and upgrade instances, and move DataFinder or Data Preprocessor instances to other computers to ensure their availability and performance. Complete the tasks that best suit your goals.

### Maintaining DataFinder, Data Preprocessor,
 and Analysis Automation Instances

Create backups, restore and upgrade instances, and move DataFinder or Data Preprocessor
 instances to other computers to ensure their availability and performance.

Complete the tasks that best suit your goals.

- [Renaming an Instance](renaming-instance.html) Rename a DataFinder, Data Preprocessor, Analysis Automation, or Federation instance if you want to assign a different name to the instance.
- [Creating a Backup of an Instance](creating-backup.html) Back up a DataFinder, Data Preprocessor, or an Analysis Automation instance in a backup file to restore the instance when necessary.
- [Moving an Instance with MS SQL Connection](moving-instance-with-mssql-connection.html) When you create a DataFinder or Data Preprocessor instance, you can store the index on a Microsoft SQL server instead of in the standard database. To move such an instance to another computer, you must save the instance in migration mode and restore it to the target computer.
- [Restoring an Instance](restoring-instances.html) Restore a DataFinder, Data Preprocessor, or an Analysis Automation instance from a backup file to reuse this instance.
- [Upgrading an Instance with a New SystemLink TDM Version](updating-instances-after-tdm-upgrade.html) If you have installed a new version of SystemLink TDM software on your existing server, upgrade your Data Preparation, Data Indexing, and Analysis Automation instances.
- [Distributing Compute Nodes](distributing-computing-nodes.html) To control the utilization of server resources, specify the number of requests Data Preparation and Analysis Automation instances process in parallel.
- [Creating a Diagnostics File for a Service Request](creating-diagnostics-file.html) Create a diagnostics file to send to your NI support representative or submit in a service request through ni.com. Diagnostics files contain logging information from all existing DataFinder, Data Preprocessor, and Analysis Automation instances.

Parent topic:

Generating Actionable Data Insights

<!--NI_TOPIC bundle=systemlink-server path=managing-systems.html language=enus -->
## TOPIC 00115: Managing Your Systems

- bundle_id: `systemlink-server`
- source_path: `managing-systems.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/managing-systems.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure systems, view system settings, and set up alarms and notifications to monitor system health.

### Managing Your Systems

Configure systems, view system settings, and set up alarms and notifications to
 monitor system health.

- [Modifying the Settings of a System](modying-setting-of-connected-system.html) Configure the settings of a system to manage how it operates.
- [Queuing Jobs for Offline Systems](queuing-jobs.html) Specify actions for managed systems to perform after they connect to your server.
- [Visualizing Metadata of a System](displaying-metadata-of-system.html) Display and modify the metadata, such as the name, IP address, or model, associated with your system so you can interact with data more efficiently.
- [Monitoring System Health with Alarms](monitoring-system-health.html) Set rules that trigger alarm instances when a tag value meets certain conditions.
- [Specifying Notification Settings for Alarms](specifying-notification-settings.html) Create email groups and custom messages to notify users when alarms are triggered.
- [Filtering Your Systems](filtering-your-systems.html) Query your systems to create filtered views that you can reuse and share.
- [Troubleshooting System Connection Issues](troubleshooting-system-connection-issues.html) Troubleshoot systems with connection issues.

<!--NI_TOPIC bundle=systemlink-server path=managing-your-assets.html language=enus -->
## TOPIC 00116: Managing Your Assets

- bundle_id: `systemlink-server`
- source_path: `managing-your-assets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/managing-your-assets.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: View and manage calibration data, track your physical assets, and visualize information about your assets on a dashboard. An asset is any hardware device for which NI has a driver, including third-party drivers. SystemLink automatically detects most NI assets and shows them in SystemLink Web Applica

### Managing Your Assets

View and manage calibration data, track your physical assets, and visualize information about your assets on a dashboard.

asset

- [Viewing Calibration Data for Hardware](viewing-calibration.html) View hardware calibration data to make maintenance decisions about your assets.
- [Manually Adding Assets](manually-adding-assets.html) Add assets from SystemLink Web Application to manage both NI assets and third-party assets.
- [Manually Adding Calibration Data](manual-calibration-data.html) Add calibration data for NI-owned and third-party assets for more complete system insights and maintenance planning.
- [Monitoring Asset Calibration Compliance with Alarms](monitoring-asset-calibration-compliance-alarms.html) Monitor the calibration compliance of your assets through notifications every time an asset's calibration status triggers an alarm.
- [Tracking Asset Connection History](tracking-asset-availability.html) Determine when, where, and how long an asset was connected to the system or how long the system was online.
- [Comparing Asset Connection History](comparing-asset-availability.html) Visualize the connection history for different assets to make maintenance decisions and analyze performance.
- [Filtering Your Assets](filtering-your-assets.html) Query your assets or calibrated assets to gain specific insights about asset tracking and calibration compliance.
- [Applying Custom Metadata to Assets](applying-custom-metadata-to-assets.html) Assign properties or keywords to your assets to facilitate searching and filtering in your workspace.
- [Generating Asset Reports](generating-asset-reports.html) Create detailed reports about your assets using predefined Jupyter notebooks that install with NI SystemLink Asset Module.
- [Tracking Asset Utilization on a Client](managing-asset-utilization-tracking-on-a-client.html) Automatically track asset utilization when you log into a client system. This level of tracking allows you to minimize changes to VIs or scripts.

Related tasks:

- Monitoring Asset Calibration Compliance with Alarms

Related information:

- NI Drivers download page

<!--NI_TOPIC bundle=systemlink-server path=manual-calibration-data.html language=enus -->
## TOPIC 00117: Manually Adding Calibration Data

- bundle_id: `systemlink-server`
- source_path: `manual-calibration-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/manual-calibration-data.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add calibration data for NI-owned and third-party assets for more complete system insights and maintenance planning. In the SystemLink web application, click Systems Management Assets . Double-click the asset for which you want to add calibration data. On the Calibration tab, click Add Calibration.

### Manually Adding Calibration Data

Add calibration data for NI-owned and third-party assets for more complete system
 insights and maintenance planning.

1. In the SystemLink web application, click Systems Management»Assets.
2. Double-click the asset for which you want to add calibration data.
3. On the Calibration tab, click Add
 Calibration. 
 Note To update existing
 calibration data, click [IMAGE alt='image' src='GUID-5149C9B2-1BE6-4CEF-8FFB-19682559663A-a5.png'].
4. Enter the calibration information and click Add.
5. Navigate to Asset Manager»Calibrated to view calibration data, including calibration history and
 status.

Parent topic:

Managing Your Assets

Related tasks:

- Viewing Calibration Data for Hardware
- Filtering Your Assets

<!--NI_TOPIC bundle=systemlink-server path=manually-adding-assets.html language=enus -->
## TOPIC 00118: Manually Adding Assets

- bundle_id: `systemlink-server`
- source_path: `manually-adding-assets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/manually-adding-assets.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add assets from SystemLink Web Application to manage both NI assets and third-party assets. In Systems Manager, double-click the system you want to add an asset to. On the Assets tab, click Add Asset. Enter a name for the asset. Specify any other information relevant to the asset. For Location, you

### Manually Adding Assets

Add assets from SystemLink Web Application to manage both NI assets
 and third-party assets.

1. In Systems Manager, double-click the system you want to add an asset to.
2. On the Assets tab, click Add
 Asset.
3. Enter a name for the asset.
4. Specify any other information relevant to the asset. For
 Location, you can specify a physical location or the
 name of a system the asset belongs to.
5. Use the Supports external calibration toggle to specify
 whether you want to configure and manage calibration for this asset. 
 If you specify that an asset supports external calibration, you can view
 and add calibration data in the asset details.
6. Specify properties or keywords if you want your asset to appear in specific
 queries.
7. Click OK.

After you add an asset manually, it appears
 in Asset Manager, and you can manage it just like any other asset.

Parent topic:

Managing Your Assets

Related tasks:

- Manually Adding Calibration Data
- Managing Your Assets

<!--NI_TOPIC bundle=systemlink-server path=mapping-roles.html language=enus -->
## TOPIC 00119: Assigning Users to Roles in a Workspace

- bundle_id: `systemlink-server`
- source_path: `mapping-roles.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/mapping-roles.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create custom experiences for each type of user on the server by specifying which role a user has and which workspaces they can access. This workflow requires administrator privileges and uses identity provider (IdP) mappings to define a user's role. If you don't have administrator privileges or wan

### Assigning Users to Roles in a
 Workspace

Create custom experiences for each type of user on the server by specifying which role
 a user has and which workspaces they can access.

This workflow requires administrator privileges and uses
 identity provider (IdP) mappings to define a user's role. If you don't have administrator
 privileges or want to add a user to a workspace without using an identity provider, add them
 as a member of the workspace instead.

1. In Access Control, click
 Workspaces.
2. Find the workspace you want to add users to and click [IMAGE alt='Workspace actions menu icon (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png']»Edit workspace. 
 A user must be a member of a workspace to access the systems and data within the
 workspace. This is true for both the SystemLink Web Application and SystemLink REST
 APIs.
3. Click Role mappings.
4. Click +Mapping and select the attribute associated with
 the user(s) who will have this role. 
 If you enabled single sign-on for your server, select the attribute that matches the
 authentication protocol your organization uses. Refer to the NI Web Server help to learn
 more about authentication options.
5. Enter the user name, group name, or other attribute for the user(s) you are
 mapping to the role.
6. In the Role column, select the role you want to assign
 to the user. 
 You can select a role you have defined or one of the predefined roles that
 install with SystemLink.Note If you assign a user backed by your identity
 provider to the Server Administrator role, NI
 recommends disabling the admin user in NI Web Server
 Configuration afterward.
7. Optional: 
 If a user or group of users needs to have more than one role, create a separate
 mapping for each role.
8. Click Update. 
 After a user logs in to SystemLink for the first time, their account
 appears under Access Control»Users.
9. If a user or group of users needs access to more than one
 workspace, repeat these steps for each workspace. 
 If you add a user to multiple workspaces, the user will see resources in
 those workspaces simultaneously within grids and other views in the web
 application.

Account

»

Workspaces

Parent topic:

Managing Access to SystemLink

Related tasks:

- Adding Users to a Workspace Without Using an Identity Provider
- Enabling Single Sign-On in SystemLink
- Configuring a Role and Privileges

Related reference:

- Role-Based Access Control Concepts
- Predefined Roles in SystemLink

Related information:

- NI Web Server help

<!--NI_TOPIC bundle=systemlink-server path=mapping-tags-to-opc.html language=enus -->
## TOPIC 00120: Mapping Tags to OPC UA Variables

- bundle_id: `systemlink-server`
- source_path: `mapping-tags-to-opc.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/mapping-tags-to-opc.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Interpret variables from an OPC server as SystemLink tags to track, update, or visualize external data within your system. Variables are the OPC equivalent of SystemLink tags. Before you can read or write OPC UA variables as SystemLink tags, you must install NI SystemLink Server OPC Module, connect

### Mapping Tags to OPC UA Variables

Interpret variables from an OPC server as SystemLink tags to track, update, or visualize external data within your system.

Variables are the OPC equivalent of
 SystemLink tags. Before you can read or write OPC UA variables as SystemLink tags, you must
 install NI SystemLink Server OPC Module, connect to an OPC server, and ensure SystemLink
 supports the data type of the variable.

1. In the root directory on your OPC session, navigate to the location of the variable on the OPC server.
2. Click 
 Create monitor to connect the variable to a tag. 
 Refer to the following table to determine which SystemLink data type corresponds to the data type of your OPC UA variable. 
 OPC UA variable data typeSystemLink tag data typeboolbooleanBooleanfloatdoubleDoubleintint32byteshortint16uint16uintnumberIntuint32uint64UInt64bytestringstringStringdatetimeutctimeDateTime 
 A monitor watches the OPC UA variable and writes its values to a corresponding
 SystemLink tag. Data from the OPC UA variable will now show as tag data in
 Tags, and you can visualize this tag data with
 Dashboards.
3. Optional: 
 To temporarily stop the monitor from writing to a tag, click Pause
 Monitor. To remove the connection between SystemLink and the OPC
 UA variable, click Delete Monitor.

After you map a variable to a tag, you can read values of the tag as it updates. The OPC UA variable will also update with any changes you make to the corresponding SystemLink tag.

Parent topic:

Integrating with an OPC UA Server

Related tasks:

- Monitoring and Visualizing Data with Tags
- Integrating with an OPC UA Server

Related information:

- Data Types for Visualizing Tag Data

<!--NI_TOPIC bundle=systemlink-server path=modying-setting-of-connected-system.html language=enus -->
## TOPIC 00121: Modifying the Settings of a System

- bundle_id: `systemlink-server`
- source_path: `modying-setting-of-connected-system.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/modying-setting-of-connected-system.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure the settings of a system to manage how it operates. Before you begin, you must connect the system to the server as a managed system. In the SystemLink web application under Systems Management, click Systems. Double-click the system you want to modify the settings for. On the System Setting

### Modifying the Settings of a System

Configure the settings of a system to manage how it operates.

Before you begin, you must connect the
 system to the server as a managed system.

1. In the SystemLink web application under Systems Management,
 click Systems.
2. Double-click the system you want to modify the settings for.
3. On the System Settings tab, enter an alias to make the system easy
 to identify. 
 When a client system connects to a SystemLink Server, the server uses the system's
 hostname to identify it. A hostname is often not human readable because IT administrators
 require each hostname in a network be unique. Changing the system alias helps you quickly
 identify the system.Tip Use
 the comments field to further identify the system.
4. Assign properties or keywords to your systems to facilitate searching and filtering. 
 The following table describes different use cases for keywords and properties. Use case
 Metadata typeYou want to associate the system with a string.
 Keyword
 You want to create key-value pairs for a group of systems.
 Property
5. Choose the workspace you want to contain the system.
6. Select the startup configurations you want to apply.
7. On the Time Settings tab, set the date and time for your
 system.
8. On the Network Settings tab, set the network settings for your
 system.

You can filter or search for the system
 by alias, keywords, or properties.

Parent topic:

Managing Your Systems

Related tasks:

- Connecting a Windows Target to Your SystemLink Server
- Connecting an NI Linux Real-Time Target to Your SystemLink Server

<!--NI_TOPIC bundle=systemlink-server path=mongodb-support-limitations.html language=enus -->
## TOPIC 00122: MongoDB Support Limitations

- bundle_id: `systemlink-server`
- source_path: `mongodb-support-limitations.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/mongodb-support-limitations.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the limitations that might prevent SystemLink from connecting to your MongoDB instance. NI does not support configurations where multiple SystemLink servers use the same MongoDB instance. NI Does not support configurations where another application uses the same MongoDB instance as Syste

### MongoDB Support Limitations

Learn about the limitations that might prevent SystemLink from connecting to your MongoDB
 instance.

- NI does not support configurations where multiple SystemLink servers use the same
 MongoDB instance.
- NI Does not support configurations where another application uses the same MongoDB
 instance as SystemLink.
- SystemLink can connect to and use a sharded MongoDB cluster,
 mongos . However, SystemLink does not take advantage of the
 horizontal scaling capabilities that a sharded cluster enables.
- SystemLink 2023 Q3 and earlier cannot connect to MongoDB instances if the MongoDB
 username contains a dash or underscore.

Parent topic:

Choosing a MongoDB Deployment

<!--NI_TOPIC bundle=systemlink-server path=monitoring-asset-calibration-compliance-alarms.html language=enus -->
## TOPIC 00123: Monitoring Asset Calibration Compliance with Alarms

- bundle_id: `systemlink-server`
- source_path: `monitoring-asset-calibration-compliance-alarms.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/monitoring-asset-calibration-compliance-alarms.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Monitor the calibration compliance of your assets through notifications every time an asset's calibration status triggers an alarm. SystemLink comes with a preconfigured notification strategy to notify you and other users about assets approaching or past their recommended calibration dates. Add your

### Monitoring Asset Calibration Compliance with Alarms

Monitor the calibration compliance of your assets through notifications every time an
 asset's calibration status triggers an alarm.

SystemLink comes with a preconfigured notification strategy to notify you and other users
 about assets approaching or past their recommended calibration dates. Add your team
 to the strategy to receive email alerts for all your assets.

1. In the SystemLink web application, click Utilities»Alarms.
2. Under Notifications, select 
 Email Groups.
3. For Selected Group, select 
 Approaching calibration email group to add recipients.
4. List the email addresses you want to notify.
5. Click 
 Save.
6. Repeat steps 3-5 for the 
 Past calibration email group.

When an asset approaches or passes its calibration date, you and your team will receive an email notification.

Parent topic:

Managing Your Assets

Related tasks:

- Modifying the Settings of a System
- Manually Adding Calibration Data

<!--NI_TOPIC bundle=systemlink-server path=monitoring-data-with-tags.html language=enus -->
## TOPIC 00124: Monitoring and Visualizing Data with Tags

- bundle_id: `systemlink-server`
- source_path: `monitoring-data-with-tags.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/monitoring-data-with-tags.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create and configure a tag to track the value of scalar data. In Tags, click Create. Specify a path, or display name, for the tag. You can also use the wildcard character (*) to specify multiple paths. Refer to the following table to see how you can use the wildcard to specify multiple paths, or dis

### Monitoring and Visualizing Data with
 Tags

Create and configure a tag to track the value of scalar data.

1. In Tags, click Create.
2. Specify a path, or display name, for the tag. 
 You can also use the wildcard character (*) to specify multiple paths.
 Refer to the following table to see how you can use the wildcard to specify
 multiple paths, or display names.GoalExample Tag Search PathResultI want to specify one tag path.Station1.TemperatureSearches for one tag, 
 Station1.Temperature.I want to specify multiple tags using a common path.Station*Searches for all tags starting with 
 Station.Note Use dot separators
 instead of slashes in tag paths. The tag path is how you programmatically
 reference the tag.
3. Specify the data type of the values the tag will hold.
4. Specify the workspace in which your tag will monitor data. 
 Users need access to this workspace to use this tag for dashboards, alarms, and notebooks.
 You cannot move a tag to another workspace after you create it.
5. Specify the retention type, which determines how long to store previous tag
 values. 
 After you configure your tag, you can see a chart of current and past
 values under History.
6. Specify whether the tag will aggregate values. 
 If a tag collects aggregates, you can see the minimum, maximum, and average values of
 the tag, as well as its total number of updates, in the Tags list.
7. Click 
 Create.
8. Click the gear next to the tag to view details and set keywords or properties
 for the tag. 
 You can use keywords and properties to search for tags in Tags
 or programmatically with Query Tags.
9. Click Tags to return to your list of tags.
10. Search for a tag in one of the following ways: 
 
 You can use the wildcard character (*) when you search by path.
  - Type a tag path or part of a tag path in
 the search bar.
  - Click the filter button next to the search bar to search for exact matches. You can include multiple queries, but only tags matching all the queries return as results.

After you create and configure a tag, you can write values to tags, read tags, query tags, and create alarms or data visualizations using tag values.

Parent topic:

Communicating Data with Tags

Related tasks:

- Mapping Tags to OPC UA Variables
- Visualizing Data

<!--NI_TOPIC bundle=systemlink-server path=monitoring-status-datapreprocessor.html language=enus -->
## TOPIC 00125: Monitoring the Processing Status

- bundle_id: `systemlink-server`
- source_path: `monitoring-status-datapreprocessor.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/monitoring-status-datapreprocessor.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Check the processing status of the files in the raw data areas of a Data Preprocessor instance. Initiate scanning or reprocessing of files or folders if necessary. In Data Preparation, click Data Preprocessor Instances. Select an instance and click ManageProcessing Status. Check the processing statu

### Monitoring the Processing Status

Check the processing status of the files in the raw data areas of a Data Preprocessor
 instance. Initiate scanning or reprocessing of files or folders if necessary.

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Processing Status.
3. Check the processing status of the files in the raw data area.
4. To reprocess files or folders or initiate a scan manually, use
 the options on the Process menu.
5. Optional: 
 Click 
 Filter View to filter processes by status. For example, you can only display files which have not yet been processed or with an unsuitable DataPlugin.
6. Optional: 
 For basic processing information, click 
 [IMAGE alt='image' src='GUID-178B9EF2-D542-430D-AFE0-2D681C2BACAA-a5.png']»Quick Info. For more detailed information, click 
 [IMAGE alt='image' src='GUID-178B9EF2-D542-430D-AFE0-2D681C2BACAA-a5.png']»Advanced Statistics. 
 Note 
 Advanced Statistics
 can show more processed files than existing files because there may be
 several DataPlugins processing the same file type.

Parent topic:

Harmonizing and Enriching Data

Related tasks:

- Scanning and Processing Files Manually

<!--NI_TOPIC bundle=systemlink-server path=monitoring-status-indexing.html language=enus -->
## TOPIC 00126: Monitoring the Indexing Status

- bundle_id: `systemlink-server`
- source_path: `monitoring-status-indexing.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/monitoring-status-indexing.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Monitor the system status of DataFinder instances to restart them if necessary. If the DataFinder instance is not started, the system status displays the most recent data from before the instance stopped. If you restart the instance after deleting large search areas, it may take some time until the

### Monitoring the Indexing Status

Monitor the system status of DataFinder instances to restart them if necessary.

Note

1. In Data Indexing, click DataFinder
 Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Indexing Status.
3. Check the indexing status at file level. If you use an instance that indexes
 the file service, like the FileIndex instance, SystemLink sorts the files in
 ascending order by the date of the last file changes.
4. Optional: 
 Perform any of the following tasks. 
 Goal
 What to doFilter files by indexing status.
 Click Filter View. For example,
 you can only display files whose indexing has failed or
 which have not yet been indexed.
 Index folders that have not yet been
 indexed (not available for instances that index the file
 service, like the FileIndex instance).
 Select a folder and choose Index Folder»Index.
 Index one file that was not successfully indexed.
 Select a file and click Reindex
 File.
 Index multiple files that were not successfully indexed
 (not available for instances that index the file service,
 like the FileIndex instance).
 Select a folder and choose Index Folder»Reindex.
5. Optional: 
 For basic indexing information, click [IMAGE alt='image' src='GUID-178B9EF2-D542-430D-AFE0-2D681C2BACAA-a5.png']»Quick Info. For more detailed information, click [IMAGE alt='image' src='GUID-178B9EF2-D542-430D-AFE0-2D681C2BACAA-a5.png']»Advanced Statistics. 
 Note 
 Advanced
 Statistics might show more indexed files than existing files
 because several DataPlugins can be used for one file type.

Parent topic:

Indexing Data

<!--NI_TOPIC bundle=systemlink-server path=monitoring-system-health.html language=enus -->
## TOPIC 00127: Monitoring System Health with Alarms

- bundle_id: `systemlink-server`
- source_path: `monitoring-system-health.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/monitoring-system-health.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Set rules that trigger alarm instances when a tag value meets certain conditions. Before setting up an alarm, ensure you have created a tag for the value you want to monitor. Under UtilitiesTags, double-click the tag for which you want to create an alarm rule. Under Alarm Rules, click Create. Specif

### Monitoring System Health with Alarms

Set rules that trigger alarm instances when a tag value meets certain conditions.

Before setting up an alarm, ensure you have created a tag for the value you want to monitor.

1. Under Utilities»Tags, double-click the tag for which you want to create an alarm rule.
2. Under 
 Alarm Rules, click 
 Create.
3. Specify a name for the rule.
4. Specify one or more tag paths to search for. 
 
 The table below illustrates examples of each type of tag search path. Example Tag Search Path
 Resultsystem1.Health.Disk.Total
 Searches for one tag,
 system1.Health.Disk.Total.
 *.Health.Disk.Total
 Searches for all tags ending with
 .Health.Disk.Total.
  - To apply the alarm rule to
 one tag, specify the absolute path of the tag.
  - To apply the alarm rule to
 multiple tags of the same data type, use the wildcard character
 ( * ) to represent any number of characters in the
 path.
5. Choose the workspace you want the rule to belong to. 
 The workspace you choose determines which data the rule processes. For more
 information about workspaces, refer to the access control help.
6. Choose whether the alarm rule evaluates tags based on their assigned value or
 their last updated time.
7. Specify the data type of the tags for which you are creating an alarm rule. The
 data type you specify must match the data type specified in the tag.
8. Specify a name and description to appear each time the alarm instance becomes active.
9. Configure conditions to specify when this rule creates an alarm.
  1. Under 
 Conditions, click 
 Create.
  2. Choose the 
 Severity Level you want to define conditions for.
  3. Choose the 
 Comparator you want the alarm rule to use to process values.
  4. Specify a Set Point or Compare
 To value for the tag this alarm rule monitors. If you're
 monitoring timestamp values, you can choose to compare values to a
 specific date and time or to the current time.
  5. Specify a Deadband for the alarm. The deadband
 determines how far the tag value must be from the set point to clear an
 active alarm. 
 Use the following table to determine how deadband values operate in
 each comparison scenario. 
 Comparator
 Value needed to clear the alarmLess Than
 Any value greater than or equal to [Set
 Point]+[Deadband]
 Less Than or Equal
 Any value greater than [Set Point]+[Deadband]
 Greater Than
 Any value less than or equal to [Set Point]-[Deadband]
 Greater Than or Equal
 Any value less than [Set Point]-[Deadband]
 In Range
 Any value less than [Set Point (Low)]-[Deadband] or
 greater than [Set Point (High)]+[Deadband]
 Equal
 Any value equal to [Set Point]+[Deadband]
 Not Equal
 Any value not equal to [Set Point]+[Deadband]
  6. If this alarm rule compares timestamp values to
 the current time, specify an Offset. The offset
 determines how close to the current time a timestamp must be to trigger
 an alarm. If a timestamp leaves the offset range, the alarm
 clears.
  7. Choose a notification strategy to alert users about alarm activity. 
 Users specified in the strategy receive notifications whenever the alarm reaches a new
 maximum severity. For example, users receive a notification if a change
 in tag values causes a moderate-severity alarm instance to become high
 severity.
  8. Click Create.
10. Click Create at the top of the page.
11. When an alarm rule triggers an alarm, you can clear the alarm, acknowledge it,
 or do neither. 
 The following table illustrates the alarm states that result from different
 actions you perform on an active alarm. 
 Cleared?
 Acknowledged?
 Resulting alarm stateYes. Alarm condition is no longer met.
 Yes
 Alarm becomes inactive.
 Yes. Alarm condition is no longer met.
 No
 Alarm stays active.
 Yes. User force cleared the alarm.
 Yes (force clearing acknowledges the alarm)
 Alarm becomes inactive.
 No
 Yes
 Alarm becomes acknowledged but stays active.
 No
 No
 Alarm stays active.

Parent topic:

Managing Your Systems

Related tasks:

- Managing Access to SystemLink
- Managing Your Systems
- Specifying Notification Settings for Alarms

<!--NI_TOPIC bundle=systemlink-server path=monitoring-tests.html language=enus -->
## TOPIC 00128: Monitoring Tests

- bundle_id: `systemlink-server`
- source_path: `monitoring-tests.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/monitoring-tests.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Track test progress and view test reports in Test Monitor through either the Test Monitor API or TestStand integration. Test Insights in the SystemLink web application allows the same functionality for both test monitoring methods.

### Monitoring Tests

Track test progress and view test reports in Test Monitor through either the Test
 Monitor API or TestStand integration.

Test Insights in the SystemLink web
 application allows the same functionality for both test monitoring methods.

- [Integrating Test Monitor with TestStand](integrating-with-teststand.html) Send test metadata from TestStand to your SystemLink server.
- [Storing and Forwarding Test Data](storing-and-forwarding-offline-data-from-client.html) Store offline test data on a client to back up data or insure against network disruptions. The NI SystemLink Test Monitor Client plugin for TestStand stores test data locally and forwards this data to the server whenever a network connection is available.
- [Associating Test Results with a Product](associating-test-results-with-a-product.html) Specify a part number in test result metadata to associate the result with a product.
- [Publishing Test Results with the Test Monitor API](test-monitoring-http-api.html) Publish test results, log parametric data, and attach additional files to results for review or analysis using the SystemLink Test Monitor API.
- [Analyzing and Interacting with Test Results](analyzing-test-data-jupyter.html) Filter, generate, and visualize test results to analyze your test and measurement data.
- [Moving a Test Result to Another Workspace](moving-a-test-result.html) Move a test result to a different workspace so users in that workspace can access it.
- [Uploading Custom Files to Test Monitor](uploading-custom-files.html) Attach any type of file, including TDMS files, as a TestStand result to upload data to Test Monitor.
- [Creating Email Notifications for Tests](creating-email-notifications.html) Use SystemLink TestStand steps to automatically send emails depending on test results.
- [Predefined Properties](predefined-properties.html) Reference NI-created properties to organize your tests, assets, tags, or files, and avoid using the same names when adding custom properties.

Related tasks:

- Visualizing Data

<!--NI_TOPIC bundle=systemlink-server path=moving-a-test-result.html language=enus -->
## TOPIC 00129: Moving a Test Result to Another Workspace

- bundle_id: `systemlink-server`
- source_path: `moving-a-test-result.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/moving-a-test-result.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Move a test result to a different workspace so users in that workspace can access it. Before updating the workspace for a test result, ensure you have delete privileges in the current workspace and create privileges in the destination workspace. A test result can only belong to one workspace. In Tes

### Moving a Test Result to Another
 Workspace

Move a test result to a different workspace so users in that workspace can access
 it.

Before updating the workspace for a test
 result, ensure you have delete privileges in the current workspace and
 create privileges in the destination workspace. A test result can only
 belong to one workspace.

1. In Test Insights, click Test Results.
2. Select one or more test results you want to move.
3. Click Edit»Workspace.
4. Select the workspace you want to move the result to.
5. Click OK.

After you move a test result to a new workspace, only users in that
 workspace can access the test result.

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-server path=moving-files-on-the-server.html language=enus -->
## TOPIC 00130: Moving Incoming Files to Other Locations

- bundle_id: `systemlink-server`
- source_path: `moving-files-on-the-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/moving-files-on-the-server.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure rules to move files entering your SystemLink server. This allows you to use folders or file storages as an alternative or in addition to the central SystemLink file service. SystemLink only applies file moving rules to incoming files when they reach the file service, not to files in the fi

### Moving Incoming Files to Other
 Locations

Configure rules to move files entering your SystemLink server. This allows you to use
 folders or file storages as an alternative or in addition to the central SystemLink file
 service.

Note

Note

- Programmatically transfer files with the File Transfer
 API in LabVIEW, the HTTP API, or the Python API.
- Manually upload files with the Files application or
 on the File Service tab in Data
 Navigation .

Complete the following steps to configure a rule for moving incoming
 files:

1. Click [IMAGE alt='App Browser Icon' src='GUID-D7488A56-ED3B-4438-8C8F-B94DB2A64658-a5.svg']»Utilities»Files.
2. In the ribbon, click [IMAGE alt='Gear icon' src='GUID-0BBB5DF7-2F3D-4E09-AF49-E49EF12C2574-a5.png']»File Moving Rules.
3. Click New.
4. Enter a name for the rule and select the default destination to move the files
 to. 
 Note To change the default destination, launch
 NI SystemLink Server Configuration on the server through the Windows Start
 menu and click FileMoving. Click
 Browse to locate and set the default destination.
 To create a new destination, you must add a configuration JSON file to
 C:\ProgramData\National
 Instruments\Skyline\Data\FileMoving on your server.
5. Specify a relative path below the root path you specified in step 3. You can
 use the properties of the file to determine the folder structure. 
 An example relative path is
 <Year>\<Month>\<Day>, representing
 the creation date of the file. This relative path will create folders within the
 root path that correspond to the specific year, month, and day values of the
 files. The following is a list of properties you can use as placeholders in
 relative paths. 
 
 Note Property placeholders are
 case-sensitive. 
 In addition to these properties, you can specify a relative path containing any custom
 property you define using the File API.
  - Day
  - Month
  - Year
  - Name
  - Extension
6. Select the operation you want to apply to incoming files. 
 OperationDescriptionMove
 Moves files to the specified folder.Copy
 Moves files to the file service and copies them to the specified
 folder. 
 Note If more than one rule
 applies to a file, the file service applies all rules. If at least one rule
 is a *move* operation, you cannot view the file in the
 Files application.
7. Indicate whether you want the rule to replace invalid characters in file path
 names with underscores using the checkbox.
8. Select how you want the rule to work if there is a conflict; for example, if a
 file of the same name already exists in the new location. 
 Conflict ResolutionDescriptionOverwrite
 Overwrites the existing file.Rename Existing
 Renames the existing file in the target folder and adds the new file
 with its name.Rename New
 Renames the new file and adds it to the target folder.Do Nothing
 Does not resolve the conflict, but adds the new file to the file service.
9. Specify Rule Matching Metadata for the file moving rule.
 Rule Matching Metadata refers to any values in
 incoming files that determine which files to move. If a file's metadata matches
 a value you specify, the file service moves that file.
10. Click Create.

Parent topic:

Storing and Managing Files

Related tasks:

- Sharing Data
- Monitoring and Visualizing Data with Tags
- Transferring Files from Disk to the Server
- Transferring Files from Memory to the Server

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=moving-instance-with-mssql-connection.html language=enus -->
## TOPIC 00131: Moving an Instance with MS SQL Connection

- bundle_id: `systemlink-server`
- source_path: `moving-instance-with-mssql-connection.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/moving-instance-with-mssql-connection.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: When you create a DataFinder or Data Preprocessor instance, you can store the index on a Microsoft SQL server instead of in the standard database. To move such an instance to another computer, you must save the instance in migration mode and restore it to the target computer. In Data Indexing or Dat

### Moving an Instance with MS SQL
 Connection

When you create a DataFinder or Data Preprocessor instance, you can store the index on
 a Microsoft SQL server instead of in the standard database. To move such an instance to
 another computer, you must save the instance in migration mode and restore it to the target
 computer.

1. In 
 Data Indexing or 
 Data Preparation, open the instance overview.
2. Select the instance which you want to move to a different computer and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Stop if the server is running.
3. Select 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»More»Create Backup. You can only back up instances with their index if the index size is smaller than 50 GB.
4. Select the Migration mode.
5. Select the folder to which you want to save the backup file and click
 OK. Use a UNC path to specify the folder. 
 An example for a UNC path is \\Server\MyFolder. 
 The instance no longer displays in the instance overview.
6. Copy the backup file to the computer to which you want to move the DataFinder
 or Data Preprocessor instance.
7. In Data Indexing or Data
 Preparation on the new machine, click New»New from Backup and select the backup file. Backup files have the following
 extensions:
  - DataFinder:
 .bakdf
  - Data Preprocessor:
 .bakdpp
8. Specify a name for the new DataFinder or Data Preprocessor instance and click 
 OK. 
 Note After you restore an instance on the target
 computer, the backup file becomes invalid.

Parent topic:

Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

<!--NI_TOPIC bundle=systemlink-server path=new-features-and-changes.html language=enus -->
## TOPIC 00132: SystemLink Server New Features and Changes

- bundle_id: `systemlink-server`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/new-features-and-changes.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of SystemLink Server. Discover what is new in the latest releases of SystemLink Server.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your ve

### SystemLink Server
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of SystemLink Server.

SystemLink Server

Note

Release Notes

Related information:

- Software and Driver Downloads

#### SystemLink Server 2026 Q2 Changes

Learn about new features, behavior changes, and other updates in SystemLink Server 2026
 Q2.

- Security updates.

#### SystemLink Client 2026 Q2 Changes

Learn about new features, behavior changes, and other updates in SystemLink Client 2026
 Q2.

- Added support for ATE Core Configurations Generation 2 health metrics.

#### SystemLink Server 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in SystemLink Server 2026
 Q1.

- Security updates.

#### SystemLink Server 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in SystemLink Server 2025
 Q4.

- Security updates.

#### SystemLink Client 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in SystemLink Client 2025
 Q4.

- Security updates.

#### SystemLink Server 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in SystemLink Server 2025
 Q3.

- Security updates
- Track user licenses and system licenses using the Licenses 
 application. To access this application, click Access Control»Licenses .

#### SystemLink Client 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in SystemLink Client 2025
 Q3.

- SystemLink now excludes the LAN eXtension Instrumentation (LXI) asset type
 when you configure automatic utilization reporting in the SystemLink Client Tray App or in
 TestStand. You can report LXI asset utilization data through the following means:
  - LabVIEW
  - Python
  - REST APIs
  - By enabling automatic reporting for the NI-VISA driver (2025 Q1 and later)
- Updates to the SystemLink Client Tray App : For more information on these settings, refer to *Tracking Asset Utilization
 on a Client*.
  - Configuration settings now save at the system level. You can access these settings
 in the following location: %ProgramData%\National Instruments\Systems
 Management\NIMinionConfig\trayapp_settings.json 
 Note With this release, every user on the system now uses the
 same configuration. This update removes all previous user-level
 customization.
  - The default value of the Enable Automatic Tracking setting
 has changed from All Assets to System
 Controller .

Related tasks:

- Tracking Asset Utilization on a Client

#### SystemLink 2025 Q1 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2025
 Q1.

- Updated the following components to improve security.
  - Apache httpd for NI Web Server
  - curl
  - OpenSSL
- SystemLink 2025 Q1 includes version 7.0 of MongoDB. If your SystemLink uses the
 default database, running this installer makes your local database files compatible with
 MonogDB 7.0. You cannot load the converted database files to older versions of
 SystemLink. Note Server Configuration Utility refers to
 MongoDB as a NoSQL database. This installer does not modify data in an
 externally managed database. The data becomes accessible after upgrading. NI recommends
 creating backups of all data stored by SystemLink before you upgrade. For more
 information about creating a MongoDB backup, refer to *Upgrading and Migrating
 SystemLink Server*.

Related information:

- Upgrading and Migrating SystemLink Server

#### SystemLink 2024 Q1 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2024
 Q1.

- Added support for SystemLink Client 2024 Q1.

#### SystemLink 2023 Q3 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2023
 Q3.

- Updated the following components to improve security.
  - Apache httpd for NI Web Server
  - OpenSSL Note Supports TLS 1.3
  - Erlang
  - RabbitMQ
  - Dashboard dependencies
- Web applications use the X-Content-Type-Options header.

#### SystemLink 2023 Q1 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2023
 Q1.

- Added support for SLSC devices.

<!--NI_TOPIC bundle=systemlink-server path=predefined-properties.html language=enus -->
## TOPIC 00133: Predefined Properties

- bundle_id: `systemlink-server`
- source_path: `predefined-properties.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/predefined-properties.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reference NI-created properties to organize your tests, assets, tags, or files, and avoid using the same names when adding custom properties. SystemLink automatically assigns predefined properties to tests, tags, and files that you create. You can reference them in your code, but avoid creating cust

### Predefined Properties

Reference NI-created properties to organize your tests, assets, tags, or files, and
 avoid using the same names when adding custom properties.

| Property | Description |
| --- | --- |
| nitmSource | Test framework that published the result |
| nitmTestSocketIndex | TestStand socket on which the test was executed |
| nitmProcessModel | TestStand process model used to execute the test |
| nitmBatchId | Unique identifier for other test results which executed in the same batch |
| nitmTestSocketCount | Number of TestStand test sockets on the system when the test was executed |
| nitmTestStandStartTime | Start time of the test as reported by TestStand |

| Property | Description |
| --- | --- |
| nitagRetention | Retention type of the tag |
| nitagMaxHistoryCount | Retention count if nitagRetention is set to COUNT |
| nitagHistoryTTLDays | Time history is kept for the tag if nitagRetention is set to DURATION |

| Property | Description |
| --- | --- |
| Name | Name of the file |

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-server path=predefined-roles.html language=enus -->
## TOPIC 00134: Predefined Roles in SystemLink

- bundle_id: `systemlink-server`
- source_path: `predefined-roles.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/predefined-roles.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Control access to your server more easily using roles related to common use cases. Use the following table to decide which predefined roles to assign a user or group of users in your organization. For detailed lists of privileges for each role, refer to Access Control in SystemLink Web Application.

### Predefined Roles in SystemLink

Control access to your server more easily using roles related to common use
 cases.

Use the following table to decide which predefined roles to assign a user or group of
 users in your organization.

Note

Access Control

| Role | Privileges |
| --- | --- |
| Server Administrator | Full privileges for all SystemLink workspaces, applications, and rolesNote This is the most permissive role in SystemLink. Only users who administer access control should have this role. |
| Data Maintainer | Create, read, update, and delete privileges for tests, files, and data-related tasks Read privileges for systems. assets, and alarms |
| Systems Maintainer | Create, read, update, and delete privileges for systems, assets, and alarms Read privileges for test results, dashboards, tags, and data stores |
| Collaborator | Limited alarm, message, and DataPlugins privileges Read privileges for all SystemLink applications |
| Automated Agent Note You can assign this role to systems and analysis routines only. | Create, read, update, and delete privileges for tests, assets, files, and tags Limited read privileges across other SystemLink applications |
| Workspace Owner | Assign role mapping and add users to workspaces they own Note This role allows server administrators to delegate setting up access to SystemLink data and applications while limiting overall access to other workspaces. |

Parent topic:

Managing Access to SystemLink

Related tasks:

- Managing Access to SystemLink
- Configuring a Role and Privileges
- Assigning Users to Roles in a Workspace

<!--NI_TOPIC bundle=systemlink-server path=preparing-data-for-indexing.html language=enus -->
## TOPIC 00135: Preparing Data for Searching

- bundle_id: `systemlink-server`
- source_path: `preparing-data-for-indexing.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/preparing-data-for-indexing.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: DataFinder instances index data in search areas or in the SystemLink file service to enable you to search for files and specific properties in files with Data Navigation and clients like DIAdem and LabVIEW. Complete the tasks that best suit your goals.

### Preparing Data for Searching

DataFinder instances index data in search areas or in the SystemLink file service to
 enable you to search for files and specific properties in files with Data Navigation and
 clients like DIAdem and LabVIEW.

Complete the tasks that best suit your goals.

- [Checking Compliance of Data Entering File Service](defining-data-integrity-rules.html) Define data integrity rules to ensure that all data entering the SystemLink file service complies with the metadata requirements for your data analyses. The checks apply to the workspaces that the DataFinder instance indexes.
- [Configuring File Indexing for a DataFinder Instance](configuring-file-indexing-for-searching.html) Index the data in the search areas or in the SystemLink file service to allow you to manually or automatically search for data with Data Navigation, DIAdem, or LabVIEW.
- [Enabling DataPlugins to Index New File Types](enabling-dataplugins-datafinder.html) Enable DataPlugins to index new file types so you can use them with DataFinder instances. If you use an instance that indexes the file service, like the FileIndex instance, and there is no dedicated DataPlugin for a file type, SystemLink uses the NI_UNK_DP DataPlugin to index the file properties. You can only search on the file level of file service files which are indexed by this DataPlugin.

Parent topic:

Indexing Data

<!--NI_TOPIC bundle=systemlink-server path=preparing-data-for-preprocessing.html language=enus -->
## TOPIC 00136: Configuring a Data Preprocessor Instance

- bundle_id: `systemlink-server`
- source_path: `preparing-data-for-preprocessing.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/preparing-data-for-preprocessing.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure scanning schedules and the reaction to file changes, manage raw data areas and DataPlugins, and initiate manual processing. Complete the tasks that best suit your needs.

### Configuring a Data Preprocessor Instance

Configure scanning schedules and the reaction to file changes, manage raw data areas and DataPlugins, and initiate manual processing.

Complete the tasks that best suit your needs.

- [Updating Data Preparation Procedures](loading-data-preparation-procedures.html) Upload a new data preparation procedure to replace the existing one. Data preparation procedures define how the Data Preprocessor instance harmonizes your raw data from various data formats and sources.
- [Defining Additional Raw Data Areas](defining-additional-raw-data-areas.html) Add new folders with raw data to be scanned or processed by the Data Preprocessor instance.
- [Specifying File Types to Be Scanned and Processed](enabling-dataplugins-datapreprocessor.html) Enable DataPlugins to determine which file types a Data Preprocessor instance scans and processes.
- [Configuring the Monitoring and Processing of Raw Data](configuring-monitoring-processing-raw-data.html) A Data Preprocessor instance scans the raw data areas to detect new files, file changes, or deleted files, and processes the data according to processing rules.
- [Specifying the Reaction to File Changes](specifying-data-preparation-reaction-to-file-changes.html) Specify how a Data Preprocessor instance reacts to data changes in the raw data area. These rules apply every time the system scans and processes files.
- [Continuously Scanning Raw Data Areas for New or Deleted Files](continuously-scanning-raw-data-areas.html) Scan raw data areas in short intervals to detect whether files were added or deleted. The continuous scan is fast because it does not scan for modified files.
- [Scanning and Processing Files Manually](scanning-processing-files-manually.html) Scan or process the files in the raw data areas of a Data Preprocessor instance manually if the automated process is deactivated, if the file system scan didn't work properly, or if you need to process a new or changed file immediately.
- [Batch Processing Folders or Files](batch-processing-datapreprocessor.html) Use job files to prioritize the harmonization of new files in a batch process. Enable the processing of job files and specify their location.

Parent topic:

Harmonizing and Enriching Data

<!--NI_TOPIC bundle=systemlink-server path=preview-data-file.html language=enus -->
## TOPIC 00137: Previewing Files in Data Navigation

- bundle_id: `systemlink-server`
- source_path: `preview-data-file.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/preview-data-file.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Preview measurement, image, and PDF files that you uploaded to the file service in Data Navigation. Before you begin, install the Data Indexing application, create a DataFinder instance, and upload files. Previewing files in Data Navigation is only available for DataFinder instances that index the f

### Previewing Files in Data Navigation

Preview measurement, image, and PDF files that you uploaded to the file service in Data
 Navigation.

Before you begin, install the Data
 Indexing application, create a DataFinder instance, and upload files.

Previewing files in Data Navigation is only available for
 DataFinder instances that index the file service.

1. In Data Navigation, select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Connect.
2. On the Search tab, select a file and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Show File to preview a file in Data Navigation. 
 A preview of the file opens in a new tab on your browser.

Parent topic:

Retrieving Data from Your Data Stores

Related tasks:

- Creating a DataFinder Instance

<!--NI_TOPIC bundle=systemlink-server path=previous-features-and-changes.html language=enus -->
## TOPIC 00138: Updates and Changes for SystemLink Server 2022 and Earlier

- bundle_id: `systemlink-server`
- source_path: `previous-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/previous-features-and-changes.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in SystemLink Server 2022 and earlier versions. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible c

### Updates and Changes for SystemLink Server 2022 and Earlier

Browse updates and changes made in SystemLink Server 2022 and
 earlier versions.

Note

Release Notes

#### SystemLink 2022 Q1 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2022
 Q1.

- Connect to a PostgeSQL database—Configure SystemLink Test Monitor to access a
 PostgreSQL database to enhance scalability and fault tolerance.
- Execute an Analysis Task from Test Insights Results—Execute an Analysis Task or add
 TDMS files from Test Insights Results to the Data Cart for use in the Data Analysis
 module. Analysis Tasks are developed as Jupyter Notebooks or DIAdem scripts and allow
 analysis routines to execute unsupervised.
- Retrigger the execution of analysis tasks—Re-execute a failed task under the original conditions, using the same data after resolving the cause of the failure.
- LabVIEW API returns an error for multiple alarm acknowledgments—When you acknowledge an
 alarm more than once, you now get an error (-251041).

#### SystemLink 2021 R3 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2021
 R3.

- Adding users—Add a user directly to a workspace by username or email.
- Restricted analysis privileges—Grant read privileges of all workspaces while limiting
 uploading and updating content to one workspace.
- Workspace owner role—Add users to a workspace without being a server administrator.
- Asset attachments—Add attachments to assets, such as a calibration certificate or
 manual.
- Tag data—Configure the asset grid to show tag data as a column.
- Filter systems—In the query builder on the systems grid, you can filter by systems with
 or without a specific software package installed on the system.
- System files—Use the Files tab in the system details view to see
 documents uploaded by the system.
- Calibration updates—Quickly view assets past due or approaching calibration dates using
 pre-configured filters from the assets grid.
- Asset actions—Run self-test, self-calibration, and reset on supported assets.
- Systems grid configurations—Save and share your custom system view.
- Jupyter Notebooks and Analysis Automation procedures—Use Jupyter to create procedures,
 test analysis procedures, and see results.
- Preview files—Preview measurement, image, and PDF files that you uploaded to the file
 service in Data Navigation.
- Workspace support (LabVIEW and G Web Development)—With the Use Workspace VI in LabVIEW
 or G Web Development, specify a workspace for APIs to use. The following APIs now support
 workspaces:
  - Alarms
  - Test Monitor
- Non-compliant files—After DataFinder indexes and checks files for compliance, Data
 Navigation highlights all files that do not comply with the data integrity rules.

#### SystemLink 2021 R2 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2021
 R2.

- Asset attachments—Add attachments to assets, such as a calibration certificate or
 manual.
- Support for health-tracking sensors—Collect data about the health of assets and publish
 it to SystemLink tags.
- System filtering—Filter systems by various attributes, such as serial number, model,
 custom properties, keywords, and workspaces.
- System reports—See data such as testing throughput, pass rate, and utilization for each
 system in the grid. To do this, add system grid columns and specify a notebook to
 run.
- Excluding custom properties—Exclude custom properties from the index to save disk space
 and show only the most relevant information in the properties display.
- Jupyter Notebooks and Analysis Automation procedures—Use Jupyter to edit notebooks
 contained in an analysis procedure and see your changes in Analysis Automation.
- Complex channels—Use complex channels in Analysis Automation. Note This is a preview feature.
- Build Asset Tag Path VI (LabVIEW)—Create a tag path to publish tags relating to your
 assets.
- List All Assets VI (LabVIEW)—Get a list of all assets available in your workspace.
- Workspace support (LabVIEW and G Web Development)—With the Use Workspace VI in LabVIEW
 or G Web Development, specify a workspace for APIs to use. The following APIs now support
 workspaces:
  - Tag
  - Message
  - File
- AMQP support—SystemLink no longer supports AMQP configurations. AMQP versions of
 existing nodes are deprecated. NI recommends using HTTP configurations instead.
- G Web Development Support—G Web Development now supports any SystemLink APIs that
 LabVIEW NXG Web Module previously supported.
- G API workspace support—Some parts of the G API are now workspace aware. Specifying a
 workspace in the Use Workspace VI affects all VIs that reference that configuration. Refer
 to the new features list for details.
- Forced deletion in the Delete File VI—The Delete File VI in LabVIEW now supports
 deleting corrupted files.
- Pagination in the Query Files VI—The Query Files VI in LabVIEW now supports pagination
 with optional skip and take parameters.
- LabVIEW support—SystemLink APIs no longer support LabVIEW 2017.

#### SystemLink 2021 R1 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2021
 R1.

- Timestamp support for alarms—Trigger alarms based on timestamp tag data.
- Properties and tag values for systems—Configure the systems grid to show tag values and
 properties for each system.
- Custom properties for systems and assets—Configure the systems and assets grid to show
 custom properties.
- System and asset grouping—Group systems and assets by any attribute, such as operating
 system, the workspace the system belongs to, or custom properties you define.
- Support for advanced Mongo configuration—Connect to a remote MongoDB server instance
 whose configuration requires parameters. SystemLink now supports MongoDB Atlas. Refer to
 the SystemLink Operations Handbook for more information on advanced Mongo
 configuration.
- Asset health monitoring—View health tags and active alarms for any asset.
- Improved time filtering for test results—More easily filter test results by week, month,
 or year to date.
- Additional TestStand data logging—Capture additional UUT data, including an "Include in
 Report" flag for variables and support for clusters and arrays.
- Workspace-specific data indexing and integrity rules—Apply different indexing and
 integrity rules depending on the kind of data you upload to SystemLink.
- Amazon S3 storage—File Service now uses S3 as its storage backend.
- Analysis automation and execution privileges—Define which users can approve and reject
 analysis automation procedures. Assign the "Approve and reject procedures" privilege in
 Access Control.
- User account settings—View information for your SystemLink account, including your
 assigned workspaces and roles.
- Improved navigation—SystemLink Web Application now uses universal left navigation.
- System groups under system settings—View and edit groups a system belongs to under the
 Settings tab in the system details view.
- Analysis Automation instance—Analysis Automation is now single instance.
- Default workspace rules—If you're upgrading from SystemLink 2020 R1 or earlier,
 SystemLink recreates any deleted preconfigured rules in the default workspace.
- Extended analysis automation and execution privileges—"Create and update procedures" is
 now a separate privilege you can assign in Access Control. This privilege is not
 automatically assigned to any user.

#### SystemLink 2020 R4 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2020
 R4.

- Single sign-on support—Configure SystemLink to authenticate using OpenID Connect so
 users can access SystemLink with their existing credentials, identity, and access levels
 in your organization.
- SystemLink Operations Handbook—Further customize your SystemLink setup with more
 advanced open-source scripting solutions for situations like migrating or restoring
 data.
- Installation progress—Systems Manager lists software installation progress for NI Linux
 RT systems.
- Manual asset addition—Add assets from the SystemLink web application to manage both NI
 and third-party assets.
- Custom calibration intervals—Define calibration intervals to match varying calibration
 schedules across your assets.
- Query condition storage—Store DataFinder queries directly on the server.
- Data integrity rules—Define data integrity rules to ensure that all data entering the
 SystemLink file service meets metadata requirements for your data analysis purposes.
- WebVI hosting—Host a WebVI in SystemLink to securely share it with users on the
 server.
- Installation simulation—Systems Manager simulates software installation jobs to show
 what will be changed before proceeding
- Microsoft Edge support—SystemLink Web Application no longer supports Edge Legacy
 (versions 44 and earlier). To use Edge with SystemLink, use a Chromium-based version of
 Edge.
- States detail view—Systems Manager shows the package display name and display version
 instead of the raw package name and version.
- Utilization reports timeframe—Asset utilization reports can span 24 hours in addition to
 8 hours.

#### SystemLink 2020 R3 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2020
 R3.

- Custom and predefined service roles—Use roles to specify the security context an
 analysis automation procedure uses to execute a task.
- System images within states—Include OS information in a system state to install the same
 system image across multiple NI Linux RT targets.
- Calibration information—Manually add calibration information to any asset.
- Utilization information—View utilization for an asset directly from the asset detail
 view.
- Asset detail view customization—Specify which properties appear in the asset detail
 view.
- Support for v2 notebooks—Use v2 notebook examples and view v2 notebook reports in Test
 Monitor.
- Python API—Access a first-class Tag API for Python.
- Preview Feature: Amazon S3 support for File Ingestion Service—Move incoming files
 directly to an S3 storage instead of a network share.
- General consistency and usability improvements
- User and workspace awareness in SystemLink TDM—Specify user and workspace contexts for
 analysis automation tasks.

#### SystemLink 2020 R2 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2020
 R2.

- Security web interface—Manage workspaces and define roles and privileges within
 SystemLink Web Application.
- Workspaces—Organize data, systems, and applications so users only see what's relevant to
 them.
- Roles and privileges—Customize how different users interact with each part of SystemLink
 by assigning granular privileges for different roles.
- Feed disable option—Enable or disable feeds for your systems.
- CSV previewer—Seamlessly preview CSV file attachments in the web application.
- Store and forward—Stability and usability improvements when storing and forwarding
 data.
- System alias support—Assign aliases to your assets.
- Improved Python support for DataPlugins
- General consistency and usability improvements
- Workspace support—Resources in your system belong to the workspace you specify.
- Roles and privileges—Server administrators can use the Security application to specify
 different user types and which actions they can perform in each SystemLink application.
  - Users previously mapped to the admins role in NI Web Server will map to
 the Server Administrator role upon upgrade. This role has access to all
 resources in all workspaces.
  - Users previously mapped to the users role in NI Web Server will not
 have access to any SystemLink applications immediately after upgrade. A Server
 Administrator must create a role mapping for these users in one or more workspaces.
- Data—Data is automatically uploaded to the workspace of the system that produces
 it.
- Assets—When systems move to new workspaces, assets associated with them automatically
 follow.
- DataFinder Federations—SystemLink does not support Federations with DataFinder instances
 on different machines. All DataFinder instances in a Federation must use the same
 SystemLink server.
- Free-form dashboards are deprecated—You can still edit and create free-form dashboards,
 but NI recommends using tile dashboards for new visualizations you create.
- Archiving workspaces—When the evaluation or subscription period of your Enterprise
 License expires, SystemLink automatically disables all workspaces that you have not
 archived, except for the default workspace.
- DataFinder privileges—When updating from an earlier version of SystemLink, existing
 privileges do not migrate. Use the Security application to assign DataFinder
 privileges.

#### SystemLink 2020 R1 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink 2020
 R1.

- Improved installation progress information for Windows systems
- Support for cDAQ Linux RT targets
- HTTP API updates—Create and update assets from beacons over HTTP.
- Tile navigation improvements—Navigate tiles by plot or by slice instead of the whole
 tile.
- Progress tile—Visualize progress as a percentage with a circle or a line. Use the
 progress tile to track installations, test sequences, or other processes you want to
 track.
- Use SystemLink APIs in LabVIEW NXG to share data between your client systems and
 SystemLink Server. The following functions are new to the LabVIEW NXG G API in SystemLink
 2020 R1.
  - Build Alarm ID
  - Build Path
  - Get Minion ID
  - Get System Name
  - Get TDM File Metadata
- RT support—SystemLink now supports all RT packages.
- RT installation—For Linux RT clients, users now install Linux RT System Image instead of
 SystemLink Client.
- Test Monitor reports—This version improves the workflow for navigating back to test
 results.
- HTTP node configuration—For tag, message, and file functions in LabVIEW and LabVIEW NXG,
 the HTTP configuration input is now recommended instead of required.
- OS support—SystemLink supports Windows Server 2019.
- TDM DataFinder Module licensing—Users only need one user license for all federation
 members.

#### SystemLink 19.6 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink
 19.6.

- Customized reports—Group the results for asset management reports by asset attribute or
 property.
- Asset utilization management on clients—Automatically start, disable, or end logging
 asset utilization information on a client system.
- Improved third-party support—Log asset utilization for third-party assets.
- Asset Management .NET API—Manage and communicate asset information relating to your
 systems and tests.
- New dashboard tiles—Select table or markdown tiles to visualize data on dashboards.
- Updated graph tile—Query tags to bind to graph tiles.
- System filtering—Enable the system filter to quickly switch between systems you want to
 visualize.
- Asset and systems support—Bind asset, system, and job queries as data sources to
 tiles.
- Updated notebook support—Expanded binding support for notebooks and the ability to
 return multiple values for a single notebook.
- Use SystemLink APIs in LabVIEW or LabVIEW NXG to share data between your client systems
 and SystemLink Server. The following data services are new to the G API for SystemLink
 19.6. Product
 APILabVIEW NXG
 File Transfer
 Tag Historian
 Open Configuration (Auto)
- Automatic asset utilization logging—Log
 utilization information about test system assets on the client when TestStand runs
 tests.
- Metrics table in the parametric data view—Add metrics, such as mean, min, and max, to
 the graph as plots.
- Expanded parametric data view—Customize the x-axis and data grouping of parametric
 data.
- Sweeps—Improved support for viewing parametric data sweeps.
- Overall Equipment Efficiency (OEE) report—Generate reports and add them to dashboards to
 visualize the productivity of your test and measurement systems.
- Systems Management dashboard—See high-level system insights at a glance.
- Updated system details view—Manage system information and settings to keep your systems
 healthy and running.
- Update RT distributions—Update RT targets to newer versions of LabVIEW without
 formatting them in NI Measurement & Automation Explorer.
- Progress updates on clients—Visualize progress information on a client when software
 installations and state applications occur.
- Pending jobs notifications on clients—Receive notifications on clients to when a job is
 running so you know when to lock or unlock the system.
- New sidebar—Navigate better through apps.
- New dashboards—Get key statistics about instances.
- New DataFinder instance "FileIndex"—Search data in the SystemLink file ingestion
 service.
- Custom properties—Display and highlight
 non-optimized custom properties in the Properties Display.
- Results list—Show default content in search results.
- Metadata—Add and edit metadata of SystemLink file service files.
- File Service—Upload files to SystemLink File Service.
- Analysis automation procedures—Create analysis automation procedures using the new HTTP
 API.
- Tag Historian API—SystemLink Server contains a different Tag Historian. Refer to the
 following list to learn more about the changes.
  - The 19.5 version of the LabVIEW SystemLink Toolkit cannot interact with the 19.6 Tag
 Historian API.
  - New versions of Read History and Multi-Read
 History replaced the deprecated versions of these functions on the
 palette.
  - The skip input of Configure Window
 (Undecimated) is no longer supported.
  - The take input of Configure Window
 (Undecimated) moved to a new position on the connector pane.
  - Configure Window defaults to read decimated tag values.
  - Decimated reads now return a different amount of data, which reach up to 4x the
 decimation factor.
- Writing tag value limit—Writing tag values is rate-limited to 1,000 writes per second by
 default.
- Open Configuration node—The desktop version of Open
 Configuration in LabVIEW NXG defaults to the Auto function configuration when
 you add it to the diagram.

#### SystemLink 19.5 Extended Support
 Changes

Learn about new features, behavior changes, and other updates in SystemLink
 19.5.

- Asset calibration and utilization
 analysis—Execute and generate Jupyter Notebooks ( .ipynb ) to visualize
 asset data.
- Asset Manager sidebar—Navigate to different areas in Asset Manager using the
 sidebar.
- Updated tile dashboard interface—Create a dashboard with an easy to use interface.
- New dashboard tiles—Display asset, test, and system status data on dashboards.
- Graph tile—Display tag and historical tag data on a graph tile.
- Automatically display properties on tiles—Add metadata to a data source, such as a tag
 or notebook. The properties automatically populate on a tile when you bind the data
 source.
- Use SystemLink APIs in LabVIEW or LabVIEW NXG to share data between your client systems
 and SystemLink Server. The following data services are new to the G API for SystemLink
 19.5. Product
 APILabVIEW
 Alarms
 Asset Utilization
 LabVIEW NXG
 Alarms
 Asset Utilization
- Leverage SystemLink services using .NET APIs. Access .NET API documentation in the
 public SystemLink GitHub repository or on NuGet.org.
- Products view—Analyze product information about
 your tests to determine the quality metrics of the devices under test (DUT).
- Parametric data view—Query a subset of test results to visualize parametric data
 trends.
- Export test data—Export test results and test steps as CSV files.
- Export generated test reports—Export test reports from the Reports view. The reports can
 render as HTML files or PDF files.
- System scalability—Increase the number of managed systems connected to your SystemLink
 Server.
- System alias—Assign names to your managed systems to make those systems easier to
 identify.
- Install SystemLink TDM to interact with web applications that prepare and manage your
 data for analysis. These applications include Data Preparation ,
 Data Indexing , Analysis Automation , and
 Data Navigation .
- Analysis Automation tasks—Interactively run tasks to analyze data with Analysis
 Automation procedures.
- Share data items between Data Navigation and Data
 Analysis . You can choose the input data for your task from the Data Cart or
 from the data sources of a DataFinder instance.
- Specify the file types a DataFinder or Data
 Preprocessor instance can index or process with
 DataPlugins .
- Find data by querying channel groups and channels.
- Export files—Convert files for download with DataPlugins .
- Data visualization—Display and inspect data in a browser window.
- Save queries—Store search results in Data Cart for further processing.
- Configure schedules for analysis—Perform Scheduled Tasks on data in the data cart.
- Task execution status information—Visualize more contextual information about a task
 execution provided by the context object.
- New tag creation method—Use the CreateOrUpdateTag method to create a
 tag in Tags .
- Output format standardization—Create a standardized output format with
 DataPlugins .
- Complex test result queries—Test Monitor supports advanced querying to analyze a subset
 of test results further.
- Dashboard Builder—Create dashboards with the new data binding interface and query
 building interface for tiles.
- Open Configuration node— Open Configuration 
 defaults to an HTTP configuration when you add it to the diagram in LabVIEW and LabVIEW
 NXG.
- SystemLink API packaging—Install the SystemLink LabVIEW Toolkit with NI
 Package Manager to interact with SystemLink APIs in LabVIEW and LabVIEW NXG.
- Jupyter Notebook server—The Jupyter Notebook server limits the number of concurrent
 servers running to five by default. To increase the number of servers running at one time,
 ask an administrator.
- Jupyter Notebook kernels—Kernels automatically shut down after running on idle for an
 hour.
- Test step details—To view trend data for test steps, use the Parametric
 Data viewer. The Trends view is no longer nested under
 test step details.

<!--NI_TOPIC bundle=systemlink-server path=properties-structure-job-files.html language=enus -->
## TOPIC 00139: Properties and Structure of Job Files

- bundle_id: `systemlink-server`
- source_path: `properties-structure-job-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/properties-structure-job-files.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use job files for DataFinder and Data Preprocessor instances to process specific files and specific folders. You can use job files in a batch process while data indexing or during data preparation. Job files for DataFinder and Data Preprocessor instances have an almost identical structure. With a Da

### Properties and Structure of Job Files

Use job files for DataFinder and Data
 Preprocessor instances to process specific files and specific folders. You can use
 job files in a batch process while data indexing or during data preparation.

Job files for DataFinder and Data Preprocessor
 instances have an almost identical structure. With a DataFinder
 instance, you can automate systems to create job files. This creation occurs after
 generating a file batch and prompting the indexing process. For example, you can generate a
 job file in a specified location with the Create Index Job File VI in
 LabVIEW.

The following table displays the properties of job files.

| Property | Description |
| --- | --- |
| File type | Text |
| File extensions | A DataFinder instance: .dfij A Data Preprocessor instance: .dfpj |
| Maximum number of lines | 100 lines |
| Maximum file size | 100 KB |
| File encoding | UTF-16LE UTF-8 with BOM ANSI |

The following table describes the structure of job files:

| Row | Syntax | Description |
| --- | --- | --- |
| 1 | DFSEBatchIndexer/PreProcessorJobFile | This syntax identifies the file as a job file for DataFinder and Data Preprocessor instances. |
| 2 | Version 1.0 | This syntax represents the version number. The version number must be 1.0. |
| 3-n | <Command>;"<Path>";<Parameter=Value> | This syntax defines the files and folders to be indexed or processed. |

Note

Data Preprocessor

DataFinder

| Command | Description | Parameter | Parameter Values |
| --- | --- | --- | --- |
| IndexFile | Indexes a file. | Reindex | True (default) - DataFinder instances and DataPreprocessor instances always redo the indexing or processing of the file. False - DataFinder instances and DataPreprocessor instances index or process the file only under the following circumstances: If the file changes. If the file has been added since the last indexing or processing. |
| IndexFolder | Indexes a folder. | Reindex | True - DataFinder instances and DataPreprocessor instances always redo the indexing or processing of the folder. False (default) - DataFinder and DataPreprocessor instances index or process the folder only under the following circumstances: If the files in the folder changed. If the files in the folder were added since the last indexing or processing. |
| IndexFolder | Indexes a folder. | IncludeSubFolder | True (default) - DataFinder and DataPreprocessor instances also index or process subfolders. False - DataFinder and DataPreprocessor instances do not index or process subfolders. |

Separate several parameters with commas, for example,
 <param1>=<value1>,<param2>=<value2>. The
 order of the parameters is arbitrary. If you do not specify a parameter, the
 DataFinder and Data Preprocessor instances use
 the default value of this parameter.

The following is an example of a job file:

```text
DFSEBatchIndexer
Version 1.0
IndexFile;"\\Server\TestData1\MyFile1.tdm";
IndexFile;"\\Server\TestData1\MyFile2.tdm";Reindex=True
IndexFolder;"\\Server\TestData2";Reindex=False,IncludeSubfolder=True
```

Parent topic:

Configuring File Indexing for a DataFinder Instance

<!--NI_TOPIC bundle=systemlink-server path=providing-search-results-for-analysis.html language=enus -->
## TOPIC 00140: Moving Search Results to Data Analysis

- bundle_id: `systemlink-server`
- source_path: `providing-search-results-for-analysis.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/providing-search-results-for-analysis.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add your search results to the data cart in Data Navigation to execute manual analysis tasks on these files in Data Analysis. In Data Navigation, select the DataFinder or the Federation instance on the Instance Overview tab and click Connect. Run a quick search or an advanced search. In the search r

### Moving Search Results to Data
 Analysis

Add your search results to the data cart in Data Navigation to execute manual analysis
 tasks on these files in Data Analysis.

1. In Data Navigation, select the DataFinder or the
 Federation instance on the Instance Overview tab and
 click [IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png']»Connect.
2. Run a quick search or an advanced search.
3. In the search results list, select the files you want to add to the data cart. 
 Note Data Navigation adds files
 to the data cart, even when you select groups or channels in the search
 results list.
4. Click [IMAGE alt='image' src='GUID-01D83C17-7E88-4934-824C-B12205C1FA49-a5.png']»Add to Data Cart.
5. Click [IMAGE alt='image' src='GUID-5CE659AF-067E-45D3-9662-C3DD854FF179-a5.png'] to view the
 files in the data cart.
6. Open Data Analysis to run manual analysis automation tasks on the files in the data
 cart.

Parent topic:

Retrieving Data from Your Data Stores

Related tasks:

- Executing Analysis Automation Tasks

<!--NI_TOPIC bundle=systemlink-server path=querying-tags-for-tile.html language=enus -->
## TOPIC 00141: Adding Tag Queries to a Graph Tile

- bundle_id: `systemlink-server`
- source_path: `querying-tags-for-tile.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/querying-tags-for-tile.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Build a query to add tags to a graph tile. Before you begin, open a tile dashboard and click Edit. Click New Tile and Graph. Click Tag query . Select a query to bind to the tile. Under Parameters, configure how you want the graph to display data. Select the number of plots. For Sort by, select the v

### Adding Tag Queries to a Graph Tile

Build a query to add tags to a graph tile.

Edit

1. Click New Tile and Graph.
2. Click [IMAGE alt='image' src='GUID-A620AA96-45C5-4191-A7FE-99176ACCC8F8-a5.png']»Tag query [IMAGE alt='image' src='GUID-A620AA96-45C5-4191-A7FE-99176ACCC8F8-a5.png'].
3. Select a query to bind to the tile.
4. Under Parameters, configure how you want the graph to
 display data.
  1. Select the number of plots.
  2. For Sort by, select the values you want to
 visualize.
5. Click Properties and configure how you want the graph to
 look.
6. Click Done.

Edit

Parent topic:

Visualizing Data on a Tile Dashboard

<!--NI_TOPIC bundle=systemlink-server path=queuing-jobs.html language=enus -->
## TOPIC 00142: Queuing Jobs for Offline Systems

- bundle_id: `systemlink-server`
- source_path: `queuing-jobs.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/queuing-jobs.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Specify actions for managed systems to perform after they connect to your server. In the SystemLink web application under Systems Management, click Systems. Click the system for which you want to queue jobs. Use the options to configure any changes to the system the same way you would for an online

### Queuing Jobs for Offline Systems

Specify actions for managed systems to perform after they connect to your server.

1. In the SystemLink web application under Systems Management,
 click Systems.
2. Click the system for which you want to queue jobs.
3. Use the options to configure any changes to the system the same way you would for an
 online system. 
 These changes can include any of the following:
  - Installing software
  - Changing network settings
  - Changing the password
  - Restarting the system
  - Configuring startup settings
4. To view your queued jobs, click [IMAGE alt='image' src='GUID-D7488A56-ED3B-4438-8C8F-B94DB2A64658-a5.svg']»Jobs. 
 Any jobs you specify for disconnected systems appear as
 In-Queue until the system connects to the server.

Parent topic:

Managing Your Systems

Related tasks:

- Managing Your Systems
- Modifying the Settings of a System

<!--NI_TOPIC bundle=systemlink-server path=re-execute-tasks.html language=enus -->
## TOPIC 00143: Re-executing Completed Analysis Automation Tasks

- bundle_id: `systemlink-server`
- source_path: `re-execute-tasks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/re-execute-tasks.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Re-initiate a completed task in the Analysis Automation instance to implement updates or to troubleshoot failed analysis tasks. Before you begin, ensure you have an Analysis Automation instance and scheduled or triggered tasks that reference an existing procedure. Analysis Automation stores the foll

### Re-executing Completed Analysis Automation
 Tasks

Re-initiate a completed task in the Analysis Automation instance to implement updates or
 to troubleshoot failed analysis tasks.

Before you begin, ensure you have an Analysis
 Automation instance and scheduled or triggered tasks that reference an existing
 procedure.

- All references to the processed data – or, input data – including file paths,
 ASAM information, and custom strings.
- Task parameters passed during execution.
- The ID and name of the analysis procedure that the task references.
- Comparative or parallel execution.

Note

1. From the Dashboard, click Instance to access your Analysis Automation
 Instance. 
 Note The default name for the instance created upon installation is
 AnalysisService.
2. Click History and select one or more of the analysis
 tasks. 
 Note Selecting multiple tasks disables the Show Details, Go to Task Definition,
 and Go to Analysis Automation Procedures Library options.
3. Click the gear for one of the tasks you chose and select Re-execute
 Task. 
 Note If you update a procedure
 prior to re-execution, the task uses the updated procedure - including
 changed parameters. If you delete a task but re-execute an existing task
 execution entry, SystemLink uses the stored parameter values. If a procedure
 is deleted, the system returns an error.
4. Confirm that the status of each task you re-executed is successful. If the task
 fails, check that the procedure has not been deleted and that the data links are
 current and available then execute the task again.

Parent topic:

Analyzing Data

<!--NI_TOPIC bundle=systemlink-server path=reading-tdm-data.html language=enus -->
## TOPIC 00144: Reading Measurement Data from TDMS Files

- bundle_id: `systemlink-server`
- source_path: `reading-tdm-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/reading-tdm-data.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Query TDMS files to read measurement data. What to Use You can find the SystemLink TDM Reader and Configuration APIs on the Data Communications palette in LabVIEW NXG and G Web Development Software. What to Do On the client, create the following diagram in a VI to query TDMS file.Customize the gray

### Reading Measurement Data from TDMS
 Files

Query TDMS files to read measurement data.

#### What to Use

You can find the SystemLink TDM Reader and Configuration APIs on the Data
 Communications palette in LabVIEW NXG and G Web Development
 Software.

#### What
 to Do

1. On the client, create the following diagram in a VI to query TDMS
 file. Customize the gray sections for your unique programming
 goals. [IMAGE alt='image' src='GUID-7722D04D-D27D-41EC-81C1-CD505537F2AE-a5.png'] 1Open Configuration initializes a
 connection with a SystemLink Server
 based on the credentials you supply.2Create Filter creates or adds a
 query to an existing filter based on the criteria you
 specify. For example, in the VI above, Create
 Filter (Name) queries the TDMS files with
 "demo" in the name.3Query TDMS Files searches a SystemLink server for files
 matching the criteria configured by Create
 Filter.4Cluster Properties reads the TDMS
 files reference returned and provides the file IDs, which
 the Listbox Properties
 displays.5Index Array indexes the
 file ids with the file
 currently selected in the Matching File
 IDs listbox.6In the Case Structure, Open File opens
 references to matching TDMS files on your SystemLink
 server.Note The VI
 stores the clusters returned by Query TDMS
 Files instead of calling Open
 File again when the listbox selection
 changes.7Read Data returns the specified
 measurement data from the TDMS files, which you can
 visualize on a graph.

#### Troubleshooting

- If you receive timeout errors, connection refused errors, or 404 errors,
 verify the following things:
  - The VI is connected to the correct server machine.
  - The NI Web Server is configured, running on the server machine, and
 accepts remote connections.
  - The web service you want to use is installed on the server
 machine.
- If Open Configuration (Auto) returns an error, verify
 the application is on the server machine or a system managed by the
 server.
- If you receive a 401 unauthorized errors, verify the credentials you specify
 are correct and have sufficient permission specified in the NI Web
 Server. Note Verify the permissions for each SystemLink API.
- If your application is a WebVI and you receive network errors, verify you
 enabled CORS for web servers running on the same machine as clients in NI
 Web Server.
- If you application is a WebVI and you want to deploy it, use Open
 Configuration (Auto) and log into the web server before
 accessing the WebVI.

Parent topic:

Connecting to LabVIEW and DIAdem

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=register-dataplugin-with-new-file-types.html language=enus -->
## TOPIC 00145: Registering DataPlugins to Index and Process New File Types

- bundle_id: `systemlink-server`
- source_path: `register-dataplugin-with-new-file-types.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/register-dataplugin-with-new-file-types.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Register a DataPlugin so that DataFinder instances can index files with the related extensions and Data Preprocessor instances can scan and process files with the related extensions. In DataPlugins, click Add. Enable Overwrite existing DataPlugins to overwrite an existing DataPlugin with the same na

### Registering DataPlugins to Index and Process
 New File Types

Register a DataPlugin so that DataFinder instances can index files with the related
 extensions and Data Preprocessor instances can scan and process files with the related
 extensions.

1. In 
 DataPlugins, click 
 Add.
2. Enable Overwrite existing
 DataPlugins to overwrite an existing DataPlugin with the same
 name.
3. Click 
 Browse and select the DataPlugin. DataPlugins have the file extension 
 .uri.
4. Click 
 Open and then 
 OK to add the selected DataPlugin.

Parent topic:

Accessing Your Files with DataPlugins

<!--NI_TOPIC bundle=systemlink-server path=regularly-updating-index-datafinder.html language=enus -->
## TOPIC 00146: Regularly Updating the Index of a DataFinder Instance

- bundle_id: `systemlink-server`
- source_path: `regularly-updating-index-datafinder.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/regularly-updating-index-datafinder.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Ensure your DataFinder instance always provides the latest data by enabling regular search area monitoring. You cannot regularly update the index of instances that index the SystemLink file service, like the FileIndex instance. In Data Indexing, click DataFinder Instances. Select an instance and cli

### Regularly Updating the Index of a DataFinder Instance

Ensure your DataFinder instance always provides the latest data by enabling regular
 search area monitoring. You cannot regularly update the index of instances that index the
 SystemLink file service, like the FileIndex instance.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»Index»Continuous Scan.
3. Enable the continuous scan, enter the scan interval, and click 
 OK.
4. Click Apply to accept the settings.

Parent topic:

Configuring File Indexing for a DataFinder Instance

<!--NI_TOPIC bundle=systemlink-server path=remote-file-share.html language=enus -->
## TOPIC 00147: Configuring FileIngestion Storage Options

- bundle_id: `systemlink-server`
- source_path: `remote-file-share.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/remote-file-share.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure SystemLink to store files on a remote network drive. Launch NI SystemLink Server Configuration. Under NI SystemLink Service Manager, click FileIngestion. Under Configuration, choose a storage location for new files. To use an local or networked file system, choose File System and specify t

### Configuring FileIngestion Storage
 Options

Configure SystemLink to store files on a remote network drive.

1. Launch NI SystemLink Server Configuration.
2. Under NI SystemLink Service Manager, click
 FileIngestion.
3. Under Configuration, choose a storage location for new
 files.
  - To use an local or networked file system, choose File
 System and specify the Output Path .
  - To use Amazon S3, choose Amazon Simple Storage Service
 (S3) . For more information on this service, refer to Uploading Files
 to Amazon Simple Storage Service (S3) .
4. Choose whether to run the service as a network service or as a custom user. 
 
 Note Contact your IT administrator to determine which option
 fits your use case.
  - If you use the credentials of a server to authenticate with the remote drive,
 choose Network Service .
  - If a specific user has access, choose Other
 account .
5. Click Apply.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Connecting to a Standalone Remote Mongo Database
- Setting Up a SystemLink Server
- Creating a Workspace
- Connecting to a Remote PostgreSQL Database

<!--NI_TOPIC bundle=systemlink-server path=remote-mongo-database.html language=enus -->
## TOPIC 00148: Connecting to a Standalone Remote Mongo Database

- bundle_id: `systemlink-server`
- source_path: `remote-mongo-database.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/remote-mongo-database.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure SystemLink to access a remote Mongo database to enhance scalability and fault tolerance. Before you begin, contact your database administrator to determine the port and login credentials you need to use to connect to a remote Mongo database. Refer to MongoDB documentation for more informat

### Connecting to a Standalone Remote Mongo
 Database

Configure SystemLink to access a remote Mongo database to enhance scalability and fault
 tolerance.

Before you begin, contact your database administrator to
 determine the port and login credentials you need to use to connect to a remote Mongo
 database. Refer to MongoDB documentation for more information on installing and setting up a
 Mongo database.

1. Launch NI SystemLink Server Configuration.
2. Under NI SystemLink Service Manager, click
 NoSqlDatabase.
3. Under Configuration, choose whether you want to connect
 using parameters or a custom connection string.
4. If you want to connect using parameters, click
 Connect to an externally managed server using
 parameters and specify the following information: 
 Host—The name of the Mongo server.
 Port—The port this connection will use. The most
 common port is 27017.
 The username and password you use to connect to the Mongo database.
5. If you want to connect using a custom connection string,
 click Connect to an externally managed server using a connection
 string and enter it in the Custom connection
 string textbox. 
 Refer to the MongoDB documentation for more information about connecting to
 remote MongoDB instances using replica sets.
6. Click Apply.

Parent topic:

Choosing a MongoDB Deployment

Related concepts:

- Connection String Format

Related tasks:

- Configuring FileIngestion Storage Options
- Setting Up a SystemLink Server
- Creating a Workspace

Related information:

- MongoDB documentation

<!--NI_TOPIC bundle=systemlink-server path=remote-postgres-databse.html language=enus -->
## TOPIC 00149: Connecting to a Remote PostgreSQL Database

- bundle_id: `systemlink-server`
- source_path: `remote-postgres-databse.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/remote-postgres-databse.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure SystemLink to access a remote PostgreSQL database to enhance scalability and fault tolerance in Test Monitor. Before you begin, contact your database administrator to determine the port and login credentials you need to connect to a PostgreSQL database. Refer to PostgreSQL documentation fo

### Connecting to a Remote PostgreSQL
 Database

Configure SystemLink to access a remote PostgreSQL database to enhance scalability and
 fault tolerance in Test Monitor.

Before you begin, contact your database
 administrator to determine the port and login credentials you need to connect to a PostgreSQL
 database. Refer to PostgreSQL documentation for more information on installing and setting up
 a PostgreSQL database.

1. Launch NI SystemLink Server Configuration.
2. Under NI SystemLink Service Manager, click
 PostgreSQLDatabase.
3. Under Configuration, choose whether you want to connect
 using parameters or a connection string.
4. If you want to connect using parameters, click
 Connect to an externally managed server using
 parameters and specify the following information: 
 Host—The name of the PostgreSQL server.
 Port—The port this connection will use. The most
 common port is 5433.
 Database—The name of the PostgreSQL
 database.
 The username and password you use to connect to the PostgreSQL
 database.
5. If you want to connect using a connection string, click
 Connect to an externally managed server using a connection
 string and enter it in the Npgsql connection
 string textbox. 
 Refer to the Npgsql documentation for more information about connection string
 parameters.
6. Click Apply.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Configuring FileIngestion Storage Options
- Setting Up a SystemLink Server
- Creating a Workspace

Related information:

- PostgreSQL documentation
- Npgsql documentation

<!--NI_TOPIC bundle=systemlink-server path=renaming-instance.html language=enus -->
## TOPIC 00150: Renaming an Instance

- bundle_id: `systemlink-server`
- source_path: `renaming-instance.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/renaming-instance.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Rename a DataFinder, Data Preprocessor, Analysis Automation, or Federation instance if you want to assign a different name to the instance. In Data Preparation or Data Indexing: Click Data Preprocessor Instances or DataFinder Instances on the dashboard. Select an instance and click Stop if the insta

### Renaming an Instance

Rename a DataFinder, Data Preprocessor, Analysis Automation, or Federation instance if
 you want to assign a different name to the instance.

1. In Data Preparation or Data
 Indexing:
  1. Click Data Preprocessor Instances or DataFinder
 Instances on the dashboard.
  2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Stop if the instance is running.
  3. Click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»More»Rename.
2. Optional: 
 In Analysis Automation:
  1. Click Instance on the dashboard.
  2. Click [IMAGE alt='image' src='GUID-A2DAEE93-CE77-45A0-ABEE-9B9F2BBACA6F-a5.png']»Stop if the instance is running.
  3. Click [IMAGE alt='image' src='GUID-A2DAEE93-CE77-45A0-ABEE-9B9F2BBACA6F-a5.png']»More»Rename.
3. Enter a new name and click OK.

For DataFinder or Federation instances, complete the following additional
 tasks:

1. Export the client configuration (DataFinder) or the membership connection (Federation)
 to ensure that a client like DIAdem or LabVIEW can access the renamed instance.
2. If an Analysis Automation instance receives data from the renamed DataFinder instance,
 edit the data source in the associated task in Analysis Automation.

Parent topic:

Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

Related tasks:

- Finding Data from DIAdem and LabVIEW Clients
- Creating a Federation of Multiple DataFinder Instances
- Adding or Editing Tasks for Analysis Automation Procedures

<!--NI_TOPIC bundle=systemlink-server path=reporting-data-with-jupyter-notebooks.html language=enus -->
## TOPIC 00151: Reporting Data with Jupyter Notebooks

- bundle_id: `systemlink-server`
- source_path: `reporting-data-with-jupyter-notebooks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/reporting-data-with-jupyter-notebooks.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Develop interactive reports with Jupyter notebooks. Use the reports to visualize and analyze your test and measurement data and asset management. When you install Jupyter Notebook for SystemLink, predefined Jupyter notebooks (.ipynb) install on your server. The Jupyter notebooks contain Python code

### Reporting Data with Jupyter Notebooks

Develop interactive reports with Jupyter notebooks. Use the reports to visualize and
 analyze your test and measurement data and asset management.

When you install Jupyter Notebook for SystemLink, predefined Jupyter notebooks
 (.ipynb) install on your server. The Jupyter notebooks contain Python
 code and instructions for leveraging the SystemLink Python APIs to obtain, analyze, and
 process data. When you execute notebooks in JupyterHub, Test Monitor, or Asset Manager, the
 notebooks communicate the results as graphical reports in the environment you executed them.

Before you start implementing your reporting goals, make sure
 you have the necessary privileges for all resources involved, such as the data you want to
 report.

Depending on your reporting goals,
 complete any of the following tasks.

- [Creating a New Jupyter Notebook](creating-a-new-jupyter-notebook.html) Create a new Jupyter notebook ( .ipynb ) in JupyterHub to develop code for visualizing, analyzing, and processing data from your tests, measurements, assets, and more.
- [Customizing Test Reports with JupyterHub](customizing-reports.html) Edit the Python notebooks that install with Test Module to customize your test reports.
- [Customizing Asset Reports with JupyterHub](customizing-asset-reports-jupyterhub.html) Edit the Python notebooks that install with Asset Module to customize your asset reports.
- [Sharing a Jupyter Notebook](sharing-a-jupyter-notebook.html) Share Jupyter notebooks ( .ipynb ) with other SystemLink users for further analysis or to render notebook data correctly in a shared dashboard.
- [Installing Additional Python Modules](installing-python-modules.html) Use third-party Python modules to further customize your test reports.

Related tasks:

- Creating a New Jupyter Notebook

<!--NI_TOPIC bundle=systemlink-server path=restoring-instances.html language=enus -->
## TOPIC 00152: Restoring an Instance

- bundle_id: `systemlink-server`
- source_path: `restoring-instances.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/restoring-instances.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Restore a DataFinder, Data Preprocessor, or an Analysis Automation instance from a backup file to reuse this instance. In Data Indexing, Data Preparation, or Analysis Automation, open the instance overview. Select an instance and click NewNew from Backup or MoreRestore. Option Description New New fr

### Restoring an Instance

Restore a DataFinder, Data Preprocessor, or an Analysis Automation instance from a backup file to reuse this instance.

1. In Data Indexing, Data
 Preparation, or Analysis Automation, open
 the instance overview.
2. Select an instance and click New»New from Backup or [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»More»Restore. 
 Option
 DescriptionNew»New from Backup
 Creates a copy of an instance on another
 computer.
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»More»Restore
 Replaces an instance with its backup.
3. Select the backup file. Backup files have the following file extensions: 
 Backup files have the following file extensions: 
 Option
 DescriptionDataFinder instance
 .bakdf
 Data Preprocessor instance
 .bakdpp
 Analysis Automation instance
 .bakas
4. If you create a copy, give the new instance a name and click
 OK.

Parent topic:

Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

<!--NI_TOPIC bundle=systemlink-server path=scanning-processing-files-manually.html language=enus -->
## TOPIC 00153: Scanning and Processing Files Manually

- bundle_id: `systemlink-server`
- source_path: `scanning-processing-files-manually.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/scanning-processing-files-manually.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Scan or process the files in the raw data areas of a Data Preprocessor instance manually if the automated process is deactivated, if the file system scan didn't work properly, or if you need to process a new or changed file immediately. In Data Preparation, click Data Preprocessor Instances. Select

### Scanning and Processing Files Manually

Scan or process the files in the raw data areas of a Data Preprocessor instance manually if the automated process is deactivated, if the file system scan didn't work properly, or if you need to process a new or changed file immediately.

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Processing Status tab, click
 Process and choose one of the actions from the
 following table. 
 Goal
 What to doProcess one file in a raw data area that
 was not successfully processed.
 Select a file and choose Reprocess File.
 Scan folders for new or changed files.
 Select a folder and choose Selected Folder»Scan.
 Scan all raw data areas for new or
 changed files.
 Choose All Raw Data Areas»Scan now.
 Process raw data folders that have not
 yet been processed.
 Select a folder and choose Selected Folder»Reprocess.
 Reprocess all raw data areas.
 Choose All Raw Data Areas»Reprocess.
 Process files with a certain status.
 Choose All Raw Data Areas»Reprocess Files with Status and a status.

Parent topic:

Configuring a Data Preprocessor Instance

<!--NI_TOPIC bundle=systemlink-server path=searching-for-data-with-data-indexing.html language=enus -->
## TOPIC 00154: Indexing Data

- bundle_id: `systemlink-server`
- source_path: `searching-for-data-with-data-indexing.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/searching-for-data-with-data-indexing.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use DataFinder instances to index technical data in the SystemLink file service and in search areas on SystemLink Server. Indexing data significantly improves search performance. Complete the tasks that best suit your data indexing goals.

### Indexing Data

Use DataFinder instances to index technical data in the SystemLink file service and in
 search areas on SystemLink Server. Indexing data significantly improves search
 performance.

[IMAGE alt='image' src='GUID-2FB61A18-A790-4D96-94ED-994AED3C14B9-a5.svg']

Complete the tasks that best suit your data indexing goals.

- [Creating a DataFinder Instance](creating-configuring-data-indexing.html) Create DataFinder instances to index your technical data in one or multiple workspaces in the SystemLink file service, or in one or multiple folders called search areas on the SystemLink server or other network computers. The instances you create can either serve as a data source in an automated analysis process, or you can use them to manually search data with Data Navigation or client software like DIAdem or LabVIEW.
- [Preparing Data for Searching](preparing-data-for-indexing.html) DataFinder instances index data in search areas or in the SystemLink file service to enable you to search for files and specific properties in files with Data Navigation and clients like DIAdem and LabVIEW.
- [Configuring the File Export for Data Navigation](configuring-file-export.html) Configure the download area of Data Navigation to keep it uncluttered and to distribute resources.
- [Monitoring the Indexing Status](monitoring-status-indexing.html) Monitor the system status of DataFinder instances to restart them if necessary.
- [Searching for Data with Federated DataFinder Instances](federation.html) Use Federations to search for data across multiple DataFinder instances on your SystemLink Server or distributed servers.
- [Displaying Data in a Different Hierarchy](displaying-data-in-different-hierarchy.html) Load a hierarchy configuration to change the hierarchy in which the data is displayed.
- [Using a DataFinder Instance as ASAM ODS Server](using-data-indexing-as-asamods-server.html) Use a DataFinder instance as an ASAM ODS server to display data in the search areas according to the ASAM data model, and make it available to clients through the Corba interface.

Parent topic:

Generating Actionable Data Insights

<!--NI_TOPIC bundle=systemlink-server path=selecting-a-tile-type.html language=enus -->
## TOPIC 00155: Selecting a Tile Type

- bundle_id: `systemlink-server`
- source_path: `selecting-a-tile-type.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/selecting-a-tile-type.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Choose which tile you need to use based on the data source you want to visualize. Refer to the following table to determine the type of tile you want to add. Goal Data you want to display Tile type Visualize numeric information about your systems, assets, tests, or measurements Tags Tests Assets Not

### Selecting a Tile Type

Choose which tile you need to use based on the data source you want to
 visualize.

Refer to the following table to determine the type of tile you want to
 add.

| Goal | Data you want to display | Tile type |
| --- | --- | --- |
| Visualize numeric information about your systems, assets, tests, or measurements | Tags Tests Assets Notebooks Systems Jobs | Number |
| Visualize data proportionally from multiple sources to display performance, test results, and asset utilization, and tests | Tags Tests Assets Systems Jobs | Donut |
| Visualize data on a graph to review historical trends and results from Jupyter notebooks | Tags Notebooks | Graph |
| Visualize contextual information about your systems, assets, tests, and measurements | Tags Static text | Text |
| Visualize the time an event took place, timestamps associated with your data, or the current time in any time zone | Tags Current time | Timestamp |
| Visualize the conditions or health of your systems, assets, or tests | Tags | Status |
| Visualize data comparatively from multiple sources to display performance, test results, asset utilization, and tests | Tests Systems | Table |
| Visualize custom content | Text | Markdown |
| Visualize data as a percentage of a fixed total | Tags Notebooks | Progress |

Parent topic:

Visualizing Data on a Tile Dashboard

Related tasks:

- Visualizing Data on a Tile Dashboard
- Selecting a Data Source for a Tile

<!--NI_TOPIC bundle=systemlink-server path=selecting-data-source-for-tile.html language=enus -->
## TOPIC 00156: Selecting a Data Source for a Tile

- bundle_id: `systemlink-server`
- source_path: `selecting-data-source-for-tile.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/selecting-data-source-for-tile.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a data source, such as a tag, asset, test, or notebook, to display on a tile. Before you begin, you must open a dashboard and select a tile type to add. Refer to the following table to determine the steps you need to complete to select the data source. Type of data you selected Task(s) Tags Ente

### Selecting a Data Source for a Tile

Add a data source, such as a tag, asset, test, or notebook, to display on a
 tile.

Before you begin, you must open a
 dashboard and select a tile type to add.

Refer to the following table to determine the steps you need to complete to
 select the data source.

| Type of data you selected | Task(s) |
| --- | --- |
| Tags | Enter a full or partial tag path(s) to select the tag.Note The search is case sensitive. If your tile is a graph, click … to build a tag query. |
| Assets Tests Systems Jobs | Select an existing query. Modify the existing query or create a new one.Note You cannot create new queries for assets. |
| Notebooks | Select a notebook. (Optional) Configure the parameters if you do not want to use the default values. Select a time interval for how often you want the notebook to execute and provide updated results. |

Note

Health.Memory.Total

NI-cRIO-9042-01E10AB8.Health.Memory.Total

Parent topic:

Visualizing Data on a Tile Dashboard

Related tasks:

- Selecting a Tile Type
- Visualizing Data on a Tile Dashboard
- Adding Tag Queries to a Graph Tile

<!--NI_TOPIC bundle=systemlink-server path=setting-up-systemlink-client-linux.html language=enus -->
## TOPIC 00157: Connecting an NI Linux Real-Time Target to Your SystemLink Server

- bundle_id: `systemlink-server`
- source_path: `setting-up-systemlink-client-linux.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/setting-up-systemlink-client-linux.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Establish a connection between your SystemLink server and an NI Linux Real-Time target. The host or the server is the computer where you have installed SystemLink Server. The target refers to the computer you want to connect to the server. The client refers to the computer where you have installed S

### Connecting an NI Linux Real-Time Target to
 Your SystemLink Server

Establish a connection between your SystemLink server and an NI Linux Real-Time
 target.

host

server

The *target* refers to the
 computer you want to connect to the server.

The *client* refers to the
 computer where you have installed SystemLink Client and connected to the
 server.

*Your computer* refers to a computer running Windows on which you
 can install application software and connect with the target.

- On the host, you have installed SystemLink Server.
- On the host, you have configured SystemLink Server.
- On your computer, you have installed the drivers that are required to communicate with
 your NI Linux Real-Time target. Note NI MAX is installed along with these drivers.
  - To set up a CompactRIO Linux RT target, install NI CompactRIO and Drivers.
  - To set up a PXI RT System, install PXI Platform Services.
- The host has enough node licenses available in Volume License Manager.
- You have configured any remote database connections. Changing your database
 configuration after connecting a client can cause a loss of data.

1. On your computer, launch NI MAX.
2. Ensure the following. 
 The Firmware on the target is 7.0 or later.
 The date and time are correct.
3. In the SystemLink Settings section of System
 Settings, ensure that the DNS alias and Server are correct. 
 Note If you want to create a DNS alias for
 your host, refer to steps 4-5 in *Setting Up a SystemLink Server*.
4. Launch and log in to the SystemLink web application.
5. Click 
 Systems Manager and click 
 Pending systems.
6. Click 
 Approve next to the name of the target. 
 The target is now a client connected to your SystemLink server. To manage the
 client in the SystemLink web application, click Systems Manager and
 then click Managed systems. The following image shows an example
 list of clients that are connected to a server.[IMAGE alt='image' src='GUID-0A6B87EA-D1C7-4D0E-AF4A-2140B9042ECA-a5.png']
7. If any of your clients show as Not Activated, select the client and click More»Activate.
8. Select the workspace you want to contain the client. 
 The assigned workspace determines the resources that the client can interact with. To
 learn more about workspaces, refer to *Managing Access to SystemLink*. 
 SystemLink automatically stores all data the client produces in the workspace.
 SystemLink also adds all the client assets to the workspace.
9. Optional: 
 If you want to prevent actions, from executing on your client, select the client in
 Managed Systems and click More»Lock. For example, actions include installing software or restarting.
 SystemLink queues the actions but executes only when you unlock the client. You can view
 all jobs, including jobs that are currently queued, under History.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Setting Up a SystemLink Server
- Connecting to a Standalone Remote Mongo Database
- Connecting to a Remote PostgreSQL Database
- Managing Access to SystemLink
- Troubleshooting System Connection Issues

Related reference:

- SystemLink Server Requirements

Related information:

- Download NI CompactRIO and Drivers
- Download PXI Platform Services

<!--NI_TOPIC bundle=systemlink-server path=setting-up-systemlink-client-windows.html language=enus -->
## TOPIC 00158: Connecting a Windows Target to Your SystemLink Server

- bundle_id: `systemlink-server`
- source_path: `setting-up-systemlink-client-windows.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/setting-up-systemlink-client-windows.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Establish a connection between your SystemLink server and a remote Windows target. The server is the computer where you have installed SystemLink Server. The target refers to the computer you want to connect to the server. The client refers to the computer where you have installed SystemLink Client

### Connecting a Windows Target to Your
 SystemLink Server

Establish a connection between your SystemLink server and a remote Windows target.

The *server* is the computer where you have installed SystemLink
 Server. The *target* refers to the computer you want to connect to
 the server. The *client* refers to the computer where you have installed
 SystemLink Client and connected to the server.

- On the server, you have installed SystemLink Server .
- On the server, you have configured SystemLink Server .
- The server has enough node licenses available in NI Volume License
 Manager .
- You have configured any remote database connections. Changing your database
 configuration after connecting a target can cause a loss of data.

1. On the Windows target, open NI Package Manager.
2. Search for and install SystemLink Client.
3. Launch SystemLink Client.
4. Select Connect to a SystemLink server and specify the name, IP
 address, or DNS alias of the server that you want to connect. 
 Note If you want to create a DNS alias for
 your server, refer to *Setting up a SystemLink Server*.
5. Using a web browser, launch and log in to your SystemLink server.
6. Click Systems Manager and click the Pending
 systems tile.
7. Click Approve for the targets you want to connect to
 SystemLink. 
 The target is now a client connected to your SystemLink server. To manage the client in
 the SystemLink web application, click Systems Manager and then
 click Managed systems.
 The following image shows an example list of clients that are connected to a
 server.
 [IMAGE alt='image' src='GUID-0A6B87EA-D1C7-4D0E-AF4A-2140B9042ECA-a5.png']
8. If any of your clients show as Not Activated, click the client
 and select More»Activate. 
 Note If you cannot activate a client, review your SystemLink
 licenses to verify that a license is available for your client.
9. Select the workspace you want to contain the client. 
 The assigned workspace determines the resources that the client can interact with. To
 learn more about workspaces, refer to *Managing Access to SystemLink*. 
 SystemLink automatically stores all data the client produces in the workspace.
 SystemLink also adds all the client assets to the workspace.
10. Optional: 
 To prevent actions from executing on your client, select the client in
 Managed Systems and click More»Lock. 
 Actions include installing software or restarting. SystemLink
 Server queues the actions but executes only when you unlock the client. You
 can view all jobs, including queued jobs, under History.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Setting Up a SystemLink Server
- Connecting to a Standalone Remote Mongo Database
- Connecting to a Remote PostgreSQL Database
- Managing Access to SystemLink
- Troubleshooting System Connection Issues

<!--NI_TOPIC bundle=systemlink-server path=setting-up-systemlink-network-security.html language=enus -->
## TOPIC 00159: Setting Up SystemLink Network Security

- bundle_id: `systemlink-server`
- source_path: `setting-up-systemlink-network-security.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/setting-up-systemlink-network-security.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to ensure your interactions with SystemLink are secure. Use firewalls to restrict open ports to only those ports your environment requires. The following table shows the ports and hostname that SystemLink Server uses. The hostname is the same for all hosts in SystemLink

### Setting Up SystemLink Network Security

Complete the following steps to ensure your interactions with SystemLink are
 secure.

1. Use firewalls to restrict open ports to only those ports your environment requires. The
 following table shows the ports and hostname that SystemLink Server uses. 
 Note The hostname is the same for all
 hosts in SystemLink Server. For SystemLink TDM, refer to *Setting Up a SystemLink
 Server*.
 Host
 Ports
 Description
 ExampleHostname
 443, 4505, 4506
 The web application hostname that end users log into to interact with
 SystemLink. This hostname is used when configuring redirect URLs with your
 OpenID Connect provider.
 The API hostname that endpoint testers use to send and to retrieve SystemLink
 data.
 The hostname listening on the Salt ports used to established connections and
 send Salt commands to testers. Due to the capabilities of Salt, ensure that
 you configure firewalls and appropriate CIDR blocks to prevent exposing Salt
 ports to the public internet.
 app.sle.corp.com
 Note If your hosts have invalid hostnames,
 SystemLink cannot receive data from managed targets. Likewise, users cannot access the
 web application.
2. In the production environments, update the security features.
  1. Disable Cross Origin Resource Sharing (CORS).
  2. Allow only requests from the app hostname, and other trusted web clients, to access
 the API hostname.
3. Optional: 
 Use HTTPS for communication between your SystemLink server and OpenID Connect
 provider. 
 Tip A SystemLink server does not require OpenID
 Connect authentication. For more information about using OpenID Connect for SystemLink,
 refer to *Single Sign-on with OpenID Connect* in the SystemLink Operations
 Handbook.
4. Assign a strong password for the admin user on managed NI Linux Real-Time
 targets. 
 These credentials are necessary under the following circumstances:
 When creating an SSH connection to a target.
 When a SystemLink server adds a Linux Real-Time target to the collection of managed
 systems.
5. If applicable, configure your remotely connected MongoDB instance to use TLS
 communication. Refer to the MongoDB documentation for information on how to enable
 TLS.
6. Set up the SSL certificate for SystemLink Server. For more information, refer to
 *Network Security* in the SystemLink Operations Handbook.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Setting Up a SystemLink Server

Related information:

- Single Sign-on with OpenID Connect
- Network Security

<!--NI_TOPIC bundle=systemlink-server path=setting-up-systemlink-server.html language=enus -->
## TOPIC 00160: Setting Up a SystemLink Server

- bundle_id: `systemlink-server`
- source_path: `setting-up-systemlink-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/setting-up-systemlink-server.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Install and configure SystemLink Server on your host to begin managing systems and working with data. SystemLink Server includes the SystemLink web application and SystemLink APIs. Before you begin, determine the size of the server to optimize performance. You must also install the following applica

### Setting Up a SystemLink Server

Install and configure SystemLink Server on your host to begin managing systems and
 working with data. SystemLink Server includes the SystemLink web application and SystemLink
 APIs.

- NI Package Manager (NIPM)
- Volume License Manager 
 Note Install this application if you plan to use SystemLink on
 non-host machines. For example, if you are connecting a machine to a server through
 SystemLink Client.

Note

1. In NI Package Manager, on the Browse
 Products tab, search for and install SystemLink Server and related
 installers. 
 You do not need to install SystemLink Client on your server machine.
2. Restart your machine to complete the installation.
3. Launch NI Web Server Configuration and follow the prompts in NI Web Server
 Configuration to set up your server. You can use these credentials to log into
 SystemLink with server administrator privileges. 
 For more information on server settings, refer to the NI Web Server Configuration
 help.
4. Create a DNS alias.
  1. In NI Web Server Configuration, click
 Remote.
  2. Select Allow remote connection from any
 client.
  3. Enter the DNS alias to use for your server. 
 The third-party DNS server you use determines the alias.
  4. Click Apply and Restart.
5. Prepare your server to connect to SystemLink Client.
  1. Ensure the following default ports are open on your server. 
 Note SystemLink automatically manages the local Windows
 firewall. If you are on a corporate network, you might need to work with your IT
 department to configure your corporate network firewall. 
 Port
 Purpose80 (default HTTP) or 443 (default HTTPS,
 recommended)
 SystemLink uses these ports to allow targets to perform the following
 actions.
 Install packages from the server.
 Publish data.
 Receive data.
 4505-4506
 SaltStack uses these ports to execute remote procedures
 on targets.
 5672
 RabbitMQ uses this port. Legacy client communications
 require this port. SystemLink disables the port by default.
 59100-59110
 LogosXT uses these ports for OPCUA connectivity.
 2343, 2809, and 59110-59210
 Clients, such as DIAdem, use these ports to access the
 SystemLink DataFinder index and TDM. SystemLink Base, Full, and Pro do not
 require these ports.
  2. If you are setting up SystemLink on a network that uses a
 proxy server, configure proxy settings for SystemLink.

- Connect to a remote database or file share to enhance scalability.
- Manage access to SystemLink using workspaces, roles, and privileges.
- Set up at least one SystemLink client for a Windows target or NI Linux Real-Time target
 to begin managing systems.

Parent topic:

Installing and Configuring SystemLink Server and Clients

Related tasks:

- Configuring Proxy Settings for SystemLink
- Configuring FileIngestion Storage Options
- Connecting to a Standalone Remote Mongo Database
- Connecting to a Remote PostgreSQL Database
- Managing Access to SystemLink
- Connecting an NI Linux Real-Time Target to Your SystemLink Server
- Connecting a Windows Target to Your SystemLink Server
- Assigning Users to Roles in a Workspace

Related information:

- Download NI Package Manager (NIPM)
- Download Volume License Manager
- NI Web Server Configuration help

<!--NI_TOPIC bundle=systemlink-server path=sharing-a-jupyter-notebook.html language=enus -->
## TOPIC 00161: Sharing a Jupyter Notebook

- bundle_id: `systemlink-server`
- source_path: `sharing-a-jupyter-notebook.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/sharing-a-jupyter-notebook.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Share Jupyter notebooks (.ipynb) with other SystemLink users for further analysis or to render notebook data correctly in a shared dashboard. Before you can share a Jupyter notebook (.ipynb), you must save it on your machine. Custom Jupyter notebooks are initially saved to your security identifier (

### Sharing a Jupyter Notebook

Share Jupyter notebooks (.ipynb) with other SystemLink users for
 further analysis or to render notebook data correctly in a shared dashboard.

.ipynb

Custom Jupyter notebooks are initially saved to your
 security identifier (SID) folder of the Jupyter notebooks directory. To share a Jupyter
 notebook with others, move it to a shared folder. You can share Jupyter notebooks in
 SystemLink regardless of your organization's role-based access control
 settings.

1. On your machine, navigate to your SID folder: C:\ProgramData\National
 Instruments\Skyline\JupyterHub\notebooks\<SID>. 
 Tip If you do not know your SID, open the Command Prompt and enter
 one of the following commands based on your situation.ScenarioCommand to enterYou do not know your username.wmic useraccount get
 name,sidYou do know your username.wmic useraccount where name="<username>"
 get sid
2. Locate the Jupyter notebook you want to share and copy it.
3. Navigate to the Jupyter notebooks _shared directory and
 paste your report in the folder. 
 The file path to the _shared directory is
 C:\ProgramData\National
 Instruments\Skyline\JupyterHub\notebooks\_shared\reports.Note When
 you add a Jupyter notebook to the _shared directory,
 you make it accessible to every SystemLink user.

Parent topic:

Reporting Data with Jupyter Notebooks

<!--NI_TOPIC bundle=systemlink-server path=sharing-data-across-systems.html language=enus -->
## TOPIC 00162: Sharing Data

- bundle_id: `systemlink-server`
- source_path: `sharing-data-across-systems.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/sharing-data-across-systems.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Transfer data to where it is needed using the SystemLink data services or by connecting external systems and software using APIs, software tools like LabVIEW VIs, or connectors for DIAdem and OPC UA Servers. Refer to the following topics to determine how to share your data with, or move data on, the

### Sharing Data

Transfer data to where it is needed using the SystemLink data services or by connecting
 external systems and software using APIs, software tools like LabVIEW VIs, or connectors
 for DIAdem and OPC UA Servers.

Refer to the following topics to determine how to share your data with, or move data
 on, the SystemLink platform depending on your needs.

- [Storing and Managing Files](storing-and-managing-files.html) View and manage all files in the central SystemLink file service with the dedicated Files application.
- [Communicating Data with Tags](communicating-data-with-tags.html) Communicate and manage data from your test and measurement systems with tags. Tags in SystemLink transmit and store slow-moving measurement data like system status or health. Use tags to track measurements, monitor system health, create alarms, and visualize data on dashboards.
- [Connecting to LabVIEW and DIAdem](connecting-labview-and-diadem.html) Exchange data between clients like LabVIEW or DIAdem and SystemLink Server using SystemLink data services. Access these data services through the Data Communication palette in LabVIEW and LabVIEW NXG, or the DataFinder connection in DIAdem NAVIGATOR.
- [Integrating with an OPC UA Server](connecting-to-an-opc-server.html) Connect to an OPC UA server to leverage, or mirror, OPC UA variables as tag values within the default workspace of your SystemLink system.
- [Hosting a Web Application on the NI Web Server](hosting-ni-web-server.html) To make your application available to other users, host your build output on a web server that is accessible to other users.
- [Hosting a WebVI in SystemLink](hosting-a-web-vi.html) Host a WebVI in SystemLink to securely share it with users on the server.

<!--NI_TOPIC bundle=systemlink-server path=specifying-data-preparation-reaction-to-file-changes.html language=enus -->
## TOPIC 00163: Specifying the Reaction to File Changes

- bundle_id: `systemlink-server`
- source_path: `specifying-data-preparation-reaction-to-file-changes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/specifying-data-preparation-reaction-to-file-changes.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Specify how a Data Preprocessor instance reacts to data changes in the raw data area. These rules apply every time the system scans and processes files. In Data Preparation, click Data Preprocessor Instances. Select an instance and click Manage. On the Monitoring tab, click Processing Rules and spec

### Specifying the Reaction to File Changes

Specify how a Data Preprocessor instance reacts to data changes in the raw data area.
 These rules apply every time the system scans and processes files.

1. In 
 Data Preparation, click 
 Data Preprocessor Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Monitoring tab, click Processing
 Rules and specify whether the Data Preprocessor instance
 processes changed files and/or reacts to deleted files. The Data Preprocessor
 instance always processes new files in the raw data area automatically.
4. Specify how the Data Preprocessor instance handles the files that are already in the processed data area when the associated raw data changes. 
 Processed Data
 DescriptionReplace existing files
 Overwrites the existing files in the processed data area with the new processed files.
 Deleted files in the raw data area are also deleted in the
 processed data area.
 Rename existing files
 Adds an underscore and a sequential number to the names of the old files
 in the processed data area, and saves the new processed
 files under the original name in the processed data area.
 The file with the lowest sequential number is therefore
 always the latest version of a processed file. You cannot
 combine this setting with the React to deleted
 files setting.
 Save under a new, unambiguous filename
 Saves the new processed files in the processed data area under the original name with an underscore and a sequential number. The file with the highest sequential number is therefore always the latest version of a processed file. You cannot combine this setting with the 
 React to deleted files setting.
 Flag processing as error
 Saves the new processed files in the processed data area under the original name, and assigns the name 
 Error, extended by an underscore and a sequential number, to the original files in the process data area. You cannot combine this setting with the 
 Process changed files setting.

Parent topic:

Configuring a Data Preprocessor Instance

Related tasks:

- Continuously Scanning Raw Data Areas for New or Deleted Files
- Scanning and Processing Files Manually

<!--NI_TOPIC bundle=systemlink-server path=specifying-notification-settings.html language=enus -->
## TOPIC 00164: Specifying Notification Settings for Alarms

- bundle_id: `systemlink-server`
- source_path: `specifying-notification-settings.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/specifying-notification-settings.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create email groups and custom messages to notify users when alarms are triggered. Before you set up notifications, use NI SystemLink Server Configuration to configure the Simple Mail Transfer Protocol (SMTP) service on your server through STARTTLS. Under Utilities, click Alarms. Under Notifications

### Specifying Notification Settings for Alarms

Create email groups and custom messages to notify users when alarms are triggered.

Before you set up notifications, use NI SystemLink Server Configuration to configure the Simple Mail Transfer Protocol (SMTP) service on your server through STARTTLS.

1. Under Utilities, click Alarms.
2. Under 
 Notifications, clickStrategies. 
 A notification strategy ensures the right users receive the right information whenever an
 alarm is triggered. You can use notification strategies across multiple
 workspaces.
  1. Under 
 Selected Strategy, choose a preset notification strategy to customize or click 
 New to create a strategy from scratch.
  2. Under 
 Email Group, select a list of users to receive notifications. If you have not created an email group yet, leave 
 Placeholder address group selected.
  3. Under 
 Email Template, choose a preset message template to use or customize.
  4. Click 
 Save.
3. On the 
 Email Groups tab, specify the email addresses you want to receive notifications.
  1. Under 
 Selected Group, select an existing group or click 
 New to create a new email group.
  2. List which email addresses you want to notify.
  3. Click 
 Save.
4. Optional: 
 In the 
 Email Templates tab, customize the message template you selected.
  1. Under 
 Selected Template, select the message template you specified for the strategy.
  2. Specify a subject for the email you will want to send to users to notify them of an alarm.
  3. Decide which information you want to include in the message body. To include specific information about a system, you can use any tag property, as well as special supported parameters, as a variable in the email body. 
 The following table describes special supported parameters for email templates that you can use in addition to any defined tag properties. 
 Special ParameterDescription<value>Current value of the tag when the alarm was
 triggered.<minionId>minionId property, if the tag
 has one. If not, this parameter becomes the first
 segment of the tag's path.<system>Alias of the system associated with the tag whose value triggered the alarm.<alarm_link>Link to the alarm triggered.<alarm_name>Display name of the alarm triggered.<server_url>Link to the SystemLink Server instance.<alarm_occurred_at>Time at which the alarm was triggered.<alarm_severity>The severity level of the alarm.
  4. Write the message template. 
 The following table shows example body text for email message templates and how tags populate the variables in a template with real values from your tag properties. 
 Email Message Template StringMessage Using Tag Property ValuesCPU usage on '<system>' is high. CPU usage
 is <value>%.CPU usage on 'test1' is high. CPU usage is 90%.PXI chassis in rack number '<rack_number>'
 is overheating.PXI chassis in rack number '154' is overheating.
  5. Click 
 Save.
5. If you created a new email group or template from scratch, assign them to the strategy you want to use.
  1. Click 
 Strategies.
  2. Select the strategy you want to assign the new email group or template to.
  3. Select the 
 Email Group and 
 Email Template you created.
  4. Click 
 Save.
6. Assign the strategy to an alarm rule.
  1. In Alarms, under Alarm
 Rules, click Tags or
 Calibration.
  2. Click [IMAGE alt='Gear icon.' src='GUID-D6237B29-557B-4209-9B43-FAF6DD22B3E8-a5.png'] next to the alarm rule you want to assign the notification
 strategy to.
  3. Under Conditions, click Create to configure a new condition,
 or click [IMAGE alt='Gear icon.' src='GUID-D6237B29-557B-4209-9B43-FAF6DD22B3E8-a5.png'] next to the severity level that you want to trigger an alarm
 notification, to modify a condition.
  4. Under 
 Notification Strategy, select the strategy you created or modified.
  5. Click 
 Save.

SystemLink immediately notifies the email recipients when an is alarm is created and when it increases to a higher severity level.

Parent topic:

Managing Your Systems

Related tasks:

- Monitoring System Health with Alarms
- Managing Your Systems

<!--NI_TOPIC bundle=systemlink-server path=specifying-timout-of-analysis-processes.html language=enus -->
## TOPIC 00165: Specifying the Timeout of Analysis Automation Procedures

- bundle_id: `systemlink-server`
- source_path: `specifying-timout-of-analysis-processes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/specifying-timout-of-analysis-processes.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Specify a value for the time after which analysis automation aborts analysis processes. Analysis automation uses the global timeout value only if the analysis automation procedure contains the value 0 for the timeout. In Analysis Automation, click Instance. Click SettingsGlobal Timeout [Min]. Enter

### Specifying the Timeout of Analysis
 Automation Procedures

Specify a value for the time after which analysis automation aborts analysis processes.
 Analysis automation uses the global timeout value only if the analysis automation procedure
 contains the value 0 for the timeout.

1. In Analysis Automation, click
 Instance.
2. Click Settings»Global Timeout [Min].
3. Enter a value for the time in minutes and click OK. 
 The time it takes to search for data is not included. You can enter a maximum
 value of 1440. This value corresponds to one day.
4. Click Apply to accept the settings.

Parent topic:

Adding Analysis Automation Procedures

<!--NI_TOPIC bundle=systemlink-server path=specifying-values-items-controls.html language=dede -->
## TOPIC 00166: Angeben von Werten für Objektelemente

- bundle_id: `systemlink-server`
- source_path: `specifying-values-items-controls.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/dede/specifying-values-items-controls.html
- source_language: `dede`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Welche Objekte in einem Objektelement enthalten sind und welche Werte jedem Objekt zugewiesen werden, wird von Ihnen definiert. Ein Objektelement ist ein Bedienelement mit mehreren Objekten, wie z. B. eine Dropdown-Liste, ein Listenfeld, eine Optionsfeldgruppe oder eine Baumstruktur. Legen Sie fest,

### Angeben von Werten für Objektelemente

Welche Objekte in einem Objektelement enthalten sind und welche Werte jedem Objekt zugewiesen werden, wird von Ihnen definiert.

Dropdown-Liste

Listenfeld

Optionsfeldgruppe

Baumstruktur

1. Legen Sie fest, welche Objekte in das Objektelement aufgenommen werden sollen. Verwenden Sie eine der folgenden Methoden, um im Konfigurationsbereich Objekte für ein Objektelement anzugeben.
  - Fügen Sie einzelne Objekte in der Liste Objekte hinzu. Klicken Sie doppelt auf jedes Objekt in der Liste, um die Beschriftung und den Wert festzulegen.
  - Binden Sie die Liste Objekte an ein String-Tag, das ein JSON-Array mit Objekten darstellt.
  - Geben Sie eine Tag-Abfrage an, bei der die Objekte mit allen Tags gefüllt werden, die der Abfrage entsprechen.
2. Klicken Sie doppelt auf jedes Objekt in der Liste Objekte, um den jeweiligen Wert zu definieren. Verwenden Sie eine der folgenden Methoden, um den Objektwert für jedes Objekt zu definieren.
  - Definieren Sie einen Wert, indem Sie das Objekt an ein Tag binden. Aktivieren Sie die Option Als Tags binden , um die Objektbeschriftung in der Liste Objekt als Tags anstelle von Strings zu interpretieren. Der Objektwert wird dann an den Wert des Tags gebunden.
  - Definieren Sie einen Wert, indem Sie den Objektwert direkt angeben. Lassen Sie Als Tags binden deaktiviert und geben Sie unter Objektwert einen Wert an.

Übergeordnetes Thema:

Darstellen von Tag-Daten in einem Dashboard mit freiem Layout

Zugehörige Tasks:

- Überwachen von Daten mit Hilfe von Tags

Zugehörige Verweise:

- Bindungs-Syntax
- Datentypen zur Darstellung von Tag-Daten

<!--NI_TOPIC bundle=systemlink-server path=speeding-up-search.html language=enus -->
## TOPIC 00167: Making Custom Properties Searchable

- bundle_id: `systemlink-server`
- source_path: `speeding-up-search.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/speeding-up-search.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Optimize custom properties to make them searchable with clients like Data Navigation. Optimizing custom properties also speeds up your search. In Data Indexing, click DataFinder Instances. Select an instance and click Manage. On the Custom Properties tab, choose whether to optimize custom properties

### Making Custom Properties Searchable

Optimize custom properties to make them searchable with clients like Data Navigation.
 Optimizing custom properties also speeds up your search.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage.
3. On the Custom Properties tab, choose whether to optimize
 custom properties on the File,
 Group, or Channel level.
4. Optional: 
 Click Calculate Occurrences and then click the
 Occurrences column header. 
 This sorts the custom properties with the most occurrences, which means they
 might benefit from optimization.
5. Select the property, or several properties, you want to optimize and click
 Optimize. 
 Tip Make
 sure you select all custom properties you want to optimize before you
 run the optimization process. Data Indexing will block the instance
 during the process, which may take some time.
6. Click Apply to accept the settings. 
 Note A custom property may be of a different
 data type in different files. In this case, DataFinder uses the data
 type with the highest occurrence to optimize the property across all
 files.

Data Navigation

Note

Parent topic:

Configuring File Indexing for a DataFinder Instance

Related tasks:

- Excluding Custom Properties
- Finding Data with Advanced Search

<!--NI_TOPIC bundle=systemlink-server path=storing-and-forwarding-offline-data-from-client.html language=enus -->
## TOPIC 00168: Storing and Forwarding Test Data

- bundle_id: `systemlink-server`
- source_path: `storing-and-forwarding-offline-data-from-client.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/storing-and-forwarding-offline-data-from-client.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Store offline test data on a client to back up data or insure against network disruptions. The NI SystemLink Test Monitor Client plugin for TestStand stores test data locally and forwards this data to the server whenever a network connection is available. Refer to the following table to determine th

### Storing and Forwarding Test Data

Store offline test data on a client to back up data or insure against network
 disruptions. The NI SystemLink Test Monitor Client plugin for TestStand stores test data locally
 and forwards this data to the server whenever a network connection is available.

Refer to the following table to determine the conditions under which you want
 your client to store data and forward it to Test Monitor.

| Goal | What to do |
| --- | --- |
| Store all test data on the client regardless of connection status, memory consumption, and storage space. Automatically forward this data in batches whenever the client is connected to the server. | Open TestStand on the managed system you want to store offline data during network disruptions. Select Configure » Result Processing. For NI SystemLink Test Monitor Client, click Options . Check Enable Storing and Forwarding of Test Data and select Always. Click OK. |
| Store test data on the client only when the client is disconnected from the server; for example, during a network interruption. Automatically forward this data to the server when the client reconnects to it. | Open TestStand on the managed system you want to store offline data during network disruptions. Select Configure » Result Processing. For NI SystemLink Test Monitor Client, click Options . Check Enable Storing and Forwarding of Test Data and select Only When Disconnected From Server. Click OK. |
| Maintain optimal memory usage and storage availability regardless of losing offline data. | Use the default configuration of the plugin. |

Parent topic:

Monitoring Tests

Related tasks:

- Integrating Test Monitor with TestStand

<!--NI_TOPIC bundle=systemlink-server path=storing-and-managing-files.html language=enus -->
## TOPIC 00169: Storing and Managing Files

- bundle_id: `systemlink-server`
- source_path: `storing-and-managing-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/storing-and-managing-files.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: View and manage all files in the central SystemLink file service with the dedicated Files application. SystemLink server applications cannot access files in the file service that have dependency files, such as TDM and TDX files. You need to save files with dependency files in a separate folder using

### Storing and Managing Files

View and manage all files in the central SystemLink file service with the dedicated Files
 application.

Note

- [File Formats Supported in File Preview](file-formats-supported-in-file-preview.html) SystemLink Server allows you to preview various file formats.
- [Moving Incoming Files to Other Locations](moving-files-on-the-server.html) Configure rules to move files entering your SystemLink server. This allows you to use folders or file storages as an alternative or in addition to the central SystemLink file service.
- [SystemLink Predefined Properties](systemlink-properties.html) Predefined properties are user-facing key-value pairs that install with SystemLink and SystemLink APIs.

Parent topic:

Sharing Data

Related tasks:

- Uploading Files to SystemLink

<!--NI_TOPIC bundle=systemlink-server path=storing-historical-tag-values.html language=enus -->
## TOPIC 00170: Storing Historical Tag Values

- bundle_id: `systemlink-server`
- source_path: `storing-historical-tag-values.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/storing-historical-tag-values.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure how long or how many historical tag values you store on your SystemLink server account. What to Use You can find the SystemLink APIs on the Data Communication palette in LabVIEW, LabVIEW NXG, and G Web Development Software. What to Do On the client, create the following diagram in a VI to

### Storing Historical Tag Values

Configure how long or how many historical tag values you store on your SystemLink server
 account.

#### What to Use

You can find the SystemLink APIs on the Data Communication palette in LabVIEW, LabVIEW NXG,
 and G Web Development Software.

#### What to Do

1. On the client, create the following diagram in a VI to configure how you want to store
 tag values on your SystemLink server account. Customize the gray
 sections for your unique programming goals. [IMAGE alt='image' src='GUID-7379B008-078F-401D-93F5-39D1EA43FE2D-a5.png']

| 1 | Initiate a connection with your SystemLink server account using Open Configuration.Note This example uses a subVI to allow the user to select the connection settings on the front panel. |
| --- | --- |
| 2 | Build Path identifies the system and top-level application that generates the tag as a tag path. |
| 3 | Open Tag opens a reference to the tag on your SystemLink server account. If a reference does not exist, this function creates one. |
| 4 | Configure Retention sets how long or how many historical tag values you want to store on your SystemLink server account. |
| 5 | Write Tag specifies tag values to the tag reference Open Tag opens or creates. You can see these values on SystemLink server account in real time. |
| 6 | Wait enforces a minimum time for the VI to wait before sending the tag value to your SystemLink server account. |
| 7 | Delete Tag removes tag values from your SystemLink server account. |
| 8 | Close Configuration invalidates any open reference to objects this VI creates and closes connections associated with the configuration. |

#### Troubleshooting

- If you receive timeout errors, connection refused errors, or 404 errors,
 verify the following things:
  - The VI is connected to the correct server machine.
  - The NI Web Server is configured, running on the server machine, and
 accepts remote connections.
  - The web service you want to use is installed on the server
 machine.
- If Open Configuration (Auto) returns an error, verify
 the application is on the server machine or a system managed by the
 server.
- If you receive a 401 unauthorized errors, verify the credentials you specify
 are correct and have sufficient permission specified in the NI Web
 Server. Note Verify the permissions for each SystemLink API.
- If your application is a WebVI and you receive network errors, verify you
 enabled CORS for web servers running on the same machine as clients in NI
 Web Server.
- If you application is a WebVI and you want to deploy it, use Open
 Configuration (Auto) and log into the web server before
 accessing the WebVI.

Parent topic:

Connecting to LabVIEW and DIAdem

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=structuring-your-test-data.html language=enus -->
## TOPIC 00171: Structuring Your Test Data

- bundle_id: `systemlink-server`
- source_path: `structuring-your-test-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/structuring-your-test-data.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a cluster to structure the properties of your test step data so the data displays correctly in Test Monitor. Test Monitor only supports displaying the TestStand data model. Therefore, how you configure the key-value pairs for each property in the cluster determines whether your data displays

### Structuring Your Test Data

Create a cluster to structure the properties of your test step data so the data
 displays correctly in Test Monitor.

Test Monitor only supports displaying the TestStand data model. Therefore, how you
 configure the key-value pairs for each property in the cluster determines whether your
 data displays correctly in Test Monitor.

Before you structure your test data, you need create a VI for
 acquiring test results.

#### What to Use

- Build Array
- Bundle By Name
- In Place Element Structure
- Number To Decimal String
- Property Node
- Unbundle/Bundle Elements Border Node
- Unbundle By Name

#### What to Do

On the client, create the following diagram in a VI to structure your test step data.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-CB8D25A5-6F11-43E1-9E61-E869260C115A-a5.png']

| 1 | The test step in control provides the test steps of your test program. The Property Node reads the Data property from the test steps. |
| --- | --- |
| 2 | The step parameters control provides the parameters of your test steps. Unbundle by Name returns the names of the step parameters. |
| 3 | The SystemLink Properties type definition contains the key-value pair structure you need to use for your step parameter properties. |
| 4 | Bundle By Name specifies the keys and values of each step parameter. These key-value pairs appear in Test Monitor. |
| 5 | Build Array creates an array containing all the key-value properties of the step parameters. |
| 6 | In Place Element Structure uses Unbundle/Bundle Elements Border Nodes and Build Array to assemble the data obtained from test step in and the key-value properties from step parameters into a cluster structure. |
| 7 | The Property Node uses the cluster to display the data correctly in Test Monitor. |

Create Test Step

Parent topic:

Acquiring Test Results

Related tasks:

- Acquiring Test Results

Related information:

- LabVIEW Programming VIs and Functions

<!--NI_TOPIC bundle=systemlink-server path=supported-signing-and-encryption-algorithms.html language=enus -->
## TOPIC 00172: Supported Signing and Encryption Algorithms

- bundle_id: `systemlink-server`
- source_path: `supported-signing-and-encryption-algorithms.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/supported-signing-and-encryption-algorithms.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: SystemLink supports the following algorithms for ID token signing, ID token key management encryption, and ID token content encryption. ID Token Signing Algorithm None ECDSA Using P256 Curve and SHA-256 ECDSA Using P384 Curve and SHA-384 ECDSA Using P521 Curve and SHA-512 HMAC using SHA-256 HMAC usi

### Supported Signing and Encryption
 Algorithms

SystemLink supports the following algorithms for ID token signing, ID token key
 management encryption, and ID token content encryption.

#### ID Token Signing
 Algorithm

- None
- ECDSA Using P256 Curve and SHA-256
- ECDSA Using P384 Curve and SHA-384
- ECDSA Using P521 Curve and SHA-512
- HMAC using SHA-256
- HMAC using SHA-384
- HMAC using SHA-512
- RSA using SHA-256
- RSA using SHA-384
- RSA using SHA-512
- RSASSA-PSS using SHA-256
- RSASSA-PSS using SHA-384
- RSASSA-PSS using SHA-512

#### ID Token Key Management Encryption
 Algorithm

Algorithms that do not require a private key.

- No encryption
- Direct Encryption with symmetric key
- AES-128 Key Wrap
- AES-192 Key Wrap
- AES-256 Key Wrap

Algorithms that require a private key.

- RSAES OAEP
- ECDH-ES

#### ID Token Content Encryption Algorithm

- Composite AES-CBC-128 HMAC-SHA-256
- Composite AES-CBC-192 HMAC-SHA-384
- Composite AES-CBC-256 HMAC-SHA-512

Parent topic:

Managing Access with OpenID Connect

<!--NI_TOPIC bundle=systemlink-server path=systemlink-client-requirements.html language=enus -->
## TOPIC 00173: SystemLink Client Requirements

- bundle_id: `systemlink-server`
- source_path: `systemlink-client-requirements.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/systemlink-client-requirements.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: To use SystemLink Client to communicate with targets, your targets must meet the following requirements. Hardware Requirements 4 Hardware Requirements for Targets Using SystemLink Client Component Windows NI Linux Real-Time Processor Pentium 4 G1 (equivalent or better) Intel or ARM model RAM 2 GiB m

### SystemLink Client Requirements

To use SystemLink Client to communicate with targets, your targets must meet the
 following requirements.

#### Hardware Requirements

| Component | Windows | NI Linux Real-Time |
| --- | --- | --- |
| Processor | Pentium 4 G1 (equivalent or better) | Intel or ARM model |
| RAM | 2 GiB minimum 4 GiB recommended | 512 MiB minimum 1+ GiB recommended |
| Disk | 1 GB minimum 2+ GB recommended | 512 MB |

#### Software
 Requirements

For SystemLink Client software requirements, refer to
 *SystemLink Client and External Dependencies
 Compatibility*.

#### Node
 Requirements

| Component | Windows | NI Linux Real-Time |
| --- | --- | --- |
| OS (64-bit only) | Windows 10 (64-bit) Windows 11 (64-bit) | NI Linux Real-Time 2019, 2020, 2021 (Supports LabVIEW RT 2019, 2020, 2021 and NXG 5.0 and later) |
| Processor | 64-bit | All Intel and ARM models supported |
| RAM | 2 GiB minimum 4 GiB recommended | 512 MiB minimum 1+ GiB recommended |
| Disk | 1 GB minimum 2+ GB recommended | 512 MB recommended |

Note

Parent topic:

SystemLink Server Requirements

Related information:

- SystemLink Client and External Dependencies
 Compatibility

<!--NI_TOPIC bundle=systemlink-server path=systemlink-properties.html language=enus -->
## TOPIC 00174: SystemLink Predefined Properties

- bundle_id: `systemlink-server`
- source_path: `systemlink-properties.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/systemlink-properties.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Predefined properties are user-facing key-value pairs that install with SystemLink and SystemLink APIs. You can call these properties in code and display their current values in the details area for assets, systems, tags, and tests in the SystemLink web application.You cannot delete predefined prope

### SystemLink Predefined Properties

Predefined properties are user-facing key-value pairs that install with SystemLink and
 SystemLink APIs.

Note

#### Predefined Properties

Refer to the following table to learn more about the predefined properties you can view and
 interact with in the SystemLink web application.

| Property | Full name or key | Description | API(s) | Example value |
| --- | --- | --- | --- | --- |
| Path | path | Path to the tag referenceNote A tag path uses dot separators to separate each component of the path. For example, a tag path looks like <system>.<namespace>.<tag>. | Tag | 39a98f00-7200-461b-8a7r-e8c84dc3094d.Throughput_Test.status |
| Current Value | value | Most recent value of the tag | Tag | June 04, 2019 2:34:04 AM CDT |
| Minimum Aggregate Value | min | Smallest value of a tag | Tag | 0 |
| Maximum Aggregate Value | max | Largest value of a tag | Tag | 69,905,949,604 |
| Mean Value | avg | Average value of a tag | Tag | 34,952,974,802 |
| Count | count | Number of times a tag produced a value | Tag | 11819 |
| Batch Serial Number | nitmBatchSerialNumber | Serial number assigned to a batch of DUTs or UUTs in TestStand | Test Monitor | 0123456789 |
| Serial Number | nitmSerialNumber | Serial number assigned to the DUT or UUT in TestStand. | Test Monitor | 1E28B2D |
| Test Socket Index | nitmTestSocketIndex | Indexed number associated with a test socket | Test Monitor | 4 |
| Test Socket Count | nitmTestSocketCount | Total number of test sockets included in the TestStand test sequence | Test Monitor | 5 |
| Source | nitmSource | What software application acquired the test results | Test Monitor | niteststand |
| Started At | nitmTestStandStartTime | Time when the test started running in TestStand | Test Monitor | 2019-04-29T14:37:26.467 |
| Test Program | nitmTestProgram | Name of the test program that executes the test steps | Test Monitor | Manufacturing Test.seq |
| Process Model | nitmProcessModel | Set of operations that establishes how TestStand performs a test on a DUT or UUT | Test Monitor | Sequential |
| Operator | nitmOperator | Person who executes the test | Test Monitor | Administrator |
| Batch ID | nitmBatchId | Identifier assigned to a batch of DUTs or UUTs in TestStand. | Test Monitor | 1 |
| System Name | nitmSystemName | Name of the test system performing the test | Test Monitor | VirtualBox--MAC-08-00-27-C1-70-57 |
| Hostname | nitmHostname | Name assigned to the device | Test Monitor | localhost |
| Part Number | nitmPartNumber | Unique number assigned to a test device or asset | Test Monitor | 154119E-01L |
| Product | nitmProduct | Type of device under test | Test Monitor | cRIO-9030 |
| Value | value | Value associated with the process your team started monitoring when the alarm transition generates | Alarm | 15 |
| Minion ID | minionId | Unique identifier associated with a client systemNote When you query the Alarm service, it translates the minion ID into the hostname in the SystemLink web application. | Alarm Tag | cRIO-9068--SN-190D5D5--MAC-00-80-2F-15-AF-CC |

Parent topic:

Storing and Managing Files

Related tasks:

- Visualizing Data
- Visualizing Data on a Tile Dashboard

<!--NI_TOPIC bundle=systemlink-server path=systemlink-requirements.html language=enus -->
## TOPIC 00175: SystemLink Server Requirements

- bundle_id: `systemlink-server`
- source_path: `systemlink-requirements.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/systemlink-requirements.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: To use SystemLink Server, you must have a server and nodes that meet the following requirements. Latest version of a supported browser: Chrome Firefox Edge (Chromium) Safari 16+ GB of disk space Server RequirementsNI recommends setting up one server if your facility has the following characteristics

### SystemLink Server
 Requirements

To use SystemLink Server, you must have a server and nodes that
 meet the following requirements.

- Latest version of a supported browser:
  - Chrome
  - Firefox
  - Edge (Chromium)
  - Safari
- 16+ GB of disk space

#### Server Requirements

- One lab or one production line
- Up to 100 nodes

| Server number | Components | Processor | RAM |
| --- | --- | --- | --- |
| 1 | ApplicationsDatabases | 16-core | 128 GiB |

- A large lab or a low-quantity production
- A system dependent on one SystemLink module
- Up to 200 nodes

| Server number | Components | Processor | RAM |
| --- | --- | --- | --- |
| 1 | ApplicationsSecondary database | 16-core | 128 GiB |
| 2 | Primary database | 16-core | 64 GiB |

- A large lab or a low-quantity production
- A system heavily dependent on multiple SystemLink modules
- Up to 200 nodes

| Server number | Components | Processor | RAM |
| --- | --- | --- | --- |
| 1 | Applications | 16-core | 128 GiB |
| 2 | MongoDB 4.0 | 16-core | 64 GiB |
| 3 | PostgreSQL 12 or 13 | 16-core | 64 GiB |

<!--NI_TOPIC bundle=systemlink-server path=systemlink-server-overview.html language=enus -->
## TOPIC 00176: SystemLink Server Overview

- bundle_id: `systemlink-server`
- source_path: `systemlink-server-overview.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/systemlink-server-overview.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemLink Server is web-based software for managing connected systems, software configurations, test results, and measurement data. SystemLink Server is for product engineers, production engineers, and lab managers. Use SystemLink Server to manage automated test systems, collect data, and create re

### SystemLink Server
 Overview

SystemLink Server is web-based software for managing connected
 systems, software configurations, test results, and measurement data. SystemLink Server is for product engineers, production engineers, and
 lab managers.

Use SystemLink Server to manage automated test systems, collect
 data, and create reports from a centralized location. With SystemLink Server, use product-centric analytics to derive
 actionable insights.

#### SystemLink Server Key
 Features

SystemLink Server includes the following key features.

- Systems management to perform operations such as managing system health, comparing systems, and deploying software to multiple systems at once.
- Asset management to track utilization, calibration information, and find assets.
- Test Insights application to ingest test data and monitor performance and status.
- Dashboards to monitor live systems and display key performance indicators.
- Jupyter Notebook to automate analysis, HTML, and PDF report generation.
- Leverage SystemLink TDM Analysis Automation to trigger custom tasks on an event or
 schedule.
- Role-based access control to simplify user management and data access.

<!--NI_TOPIC bundle=systemlink-server path=systemlink-server-system-components.html language=enus -->
## TOPIC 00177: Components of a SystemLink Server System

- bundle_id: `systemlink-server`
- source_path: `systemlink-server-system-components.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/systemlink-server-system-components.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemLink Server is designed for use in a system that might require hardware, drivers, and software to optimize SystemLink Server for your application. Use the minimum required SystemLink Server system components as a starting point for building your system. A diagram of the relationship between Sy

### Components of a SystemLink Server System

SystemLink Server is designed for use in a system that might require
 hardware, drivers, and software to optimize SystemLink Server for your
 application. Use the minimum required SystemLink Server system
 components as a starting point for building your system.

[IMAGE alt='A diagram of the relationship between SystemLink Server and the management of systems, assets, and data.' src='GUID-6FA9D442-3622-4918-B14C-8C10709C0129-a5.svg']

Depending on what your team needs to accomplish, you need to purchase and install specific
 SystemLink software. Refer to the following table to determine what SystemLink software your
 team needs.

| Goal | Minimum Required Software to Install |
| --- | --- |
| Role-Based Access Control | SystemLink |
| Systems Management | SystemLink SystemLink Software Configuration Module |
| Asset Management | SystemLink SystemLink Asset Module |
| Test Management | SystemLink SystemLink Test Module |
| Data Management | SystemLink SystemLink TDM |

Related tasks:

- Installing and Configuring SystemLink Server and Clients

<!--NI_TOPIC bundle=systemlink-server path=systemlink-server-theory-of-operation.html language=enus -->
## TOPIC 00178: SystemLink Server Theory of Operation

- bundle_id: `systemlink-server`
- source_path: `systemlink-server-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/systemlink-server-theory-of-operation.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemLink implements a server-client architecture to transmit data over a connected network between your systems and server. The architecture of SystemLink enables central coordination and management of your test and measurement systems, assets, software, and data. Refer to the following image and

### SystemLink Server Theory of Operation

SystemLink implements a server-client architecture to transmit data over
 a connected network between your systems and server.

The architecture of SystemLink enables central coordination and management of
 your test and measurement systems, assets, software, and data. Refer to the
 following image and table to learn about the SystemLink architecture.

[IMAGE alt='image' src='GUID-350AE701-0734-4BDE-8EDA-9EDC87E43C36-a5.svg']

| Component | Description |
| --- | --- |
| Identity provider | Stores and verifies user identity so users log into the SystemLink web application. SystemLink requires you to supply an identity provider that supports the OpenID Connect protocol. |
| Users | Access SystemLink through an OpenID Connect identity provider. |
| Test systems | Execute test applications. SystemLink can manage test systems, install software at scale, track connected assets, and automatically ingest the data they produce. SystemLink manages the authentication and authorization of test systems with role-base access control. |
| Web server | Enforces log-in configuration and redirection, inactivity timeout, and session management. |
| Role-based access control | Provides strong isolation between different workspaces as well as privileges for systems, data, and analysis routines in SystemLink. You can manage roles and workspace access through OpenID Connect user claims or direct assignment. |
| Systems management | Allows you to connect a test system to SystemLink securely, manage system configuration and settings, and remotely install software. |
| Asset management | Allows you to track assets connected to test systems and calculate the utilization of those assets. SystemLink retains asset data when you move an asset between systems. You can track asset utilization outside of the connected system or test application. |
| Test Insights | Ingests test steps and test results using a TestStand plug-in or API. You can organize test results by product. You can search test result by querying test meta data. You can also create higher level test metrics and data visualizations using integrations with SystemLink TDM Analysis Automation and SystemLink dashboards. |
| File ingestion | Allows you to store files on-premise or in the cloud and query the files without complex database syntax. You can access files through an API. Integration with SystemLink TDM Analysis Automation and Jupyter Notebooks enables you to perform custom analysis of files immediately upon upload. |
| Analysis and report generation | Enables interactive and automated analysis of test data through Jupyter Notebooks. The analyses can produce KPIs and computer analytics in dashboards. The analyses can also produce HTML reports and PDF reports. |

<!--NI_TOPIC bundle=systemlink-server path=systemlink-tdm-overview.html language=enus -->
## TOPIC 00179: Generating Actionable Data Insights

- bundle_id: `systemlink-server`
- source_path: `systemlink-tdm-overview.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/systemlink-tdm-overview.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create reports to make informed decisions about your setups for automated testing and monitoring. You can customize TDM components in SystemLink to extract information from your test data. After data extraction, use computational transformation and analysis tools to visualize the information in a st

### Generating Actionable Data Insights

Create reports to make informed decisions about your setups for automated testing and
 monitoring.

You can customize TDM components in SystemLink to extract information from your test data.
 After data extraction, use computational transformation and analysis tools to visualize the
 information in a structured report.

- Data harmonization
- Data indexing
- Analysis
- Report generation

- Configuring workspaces
- Determining data storage locations
- Making the appropriate application settings
- Writing data preparation
- Writing analysis scripts

[IMAGE alt='A diagram of the relationship between the Data Maintainer role, collaborators, and system configuration.' src='GUID-4AA85711-3359-4960-AA8F-64F9EC2D8DFE-a5.svg']

- File Service is the central SystemLink file repository that receives
 all data files from your test devices, measurement devices, and software.
- DataPlugins map your file types to the TDM model for further
 processing.
- Data Preparation harmonizes raw data from varying file formats,
 naming conventions, and units to make the data comparable.
- Data Indexing indexes files in the File Service, another folder on a
 network share, or on servers in different geographical locations. Indexing these files
 increases the speed of retrieving data.
- Analysis Automation applies automated data analyses from DIAdem,
 Python, or Jupyter to the indexed data. The automation then creates managerial reports and
 result data.
- Data Navigation enables Collaborators to run search queries,
 download, convert, or evaluate indexed data. The application then adds the data to Data Cart
 for further analysis in Data Analysis.
- Data Analysis enables Collaborators to run data analyses on data
 sources or the Data Cart. The application then creates managerial reports or result data.
 In addition to SystemLink, use DIAdem to create configuration scripts in VBS or Python.
 Use these scripts for Data Preparation, Data Indexing, and Analysis Automation. DIAdem
 also allows you to inspect, explore, and make calculations with individual data sets to
 gain in-depth insights from your data.

<!--NI_TOPIC bundle=systemlink-server path=test-monitoring-http-api.html language=enus -->
## TOPIC 00180: Publishing Test Results with the Test Monitor API

- bundle_id: `systemlink-server`
- source_path: `test-monitoring-http-api.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/test-monitoring-http-api.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Publish test results, log parametric data, and attach additional files to results for review or analysis using the SystemLink Test Monitor API. The Test Monitor API, which is available in G, .NET, Python, HTTP, and C#, communicates with the Test Monitor service over an HTTP connection. If you use Te

### Publishing Test Results with the Test
 Monitor API

Publish test results, log parametric data, and attach additional files to results for
 review or analysis using the SystemLink Test Monitor API.

The Test Monitor API, which is available in G, .NET, Python, HTTP, and C#, communicates with
 the Test Monitor service over an HTTP connection.

If you use TestStand, Integrate Test Monitor with TestStand.

1. In your programming environment, use the Test Monitor API to publish test results and
 associated steps to the server.
2. In the SystemLink web application, click Test Insights. 
 Results from the test you created will instantly appear here and update in real
 time.
3. To upload an attachment to the test result, use the File Ingestion API or File Transfer
 API.
4. To download the report attachment in the SystemLink web application, complete the
 following steps.
  1. In Test Insights, select Results.
  2. Double-click the test whose attachment you want to download.
  3. Expand Attachments to select the attachment and click
 Download.

Parent topic:

Monitoring Tests

Related tasks:

- Integrating Test Monitor with TestStand
- Analyzing and Interacting with Test Results

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=tracking-asset-availability.html language=enus -->
## TOPIC 00181: Tracking Asset Connection History

- bundle_id: `systemlink-server`
- source_path: `tracking-asset-availability.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/tracking-asset-availability.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Determine when, where, and how long an asset was connected to the system or how long the system was online. In the SystemLink web application, click Systems Management Assets . Click Assets or Calibrated. Double-click the asset for which you want to review asset usage information. Complete one of th

### Tracking Asset Connection History

Determine when, where, and how long an asset was connected to the system or how long
 the system was online.

1. In the SystemLink web application, click Systems Management»Assets.
2. Click Assets or Calibrated.
3. Double-click the asset for which you want to review asset usage
 information.
4. Complete one of the following tasks based on your goals. 
 Goal
 What to doSee on which system(s) your team installed the asset.
 Click [IMAGE alt='Actions menu (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png']»Download»Location history.
 See the frequency and duration your team connected the asset to one
 of your systems.
 In the asset details, view the connection history and utilization
 history for the asset.

Parent topic:

Managing Your Assets

Related tasks:

- Comparing Asset Connection History
- Managing Your Assets

<!--NI_TOPIC bundle=systemlink-server path=tracking-asset-utilization.html language=enus -->
## TOPIC 00182: Tracking Asset Utilization with LabVIEW

- bundle_id: `systemlink-server`
- source_path: `tracking-asset-utilization.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/tracking-asset-utilization.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Record utilization information about the assets performing test and measurement tasks. When you track an asset, you also track the assets your team connected to it. For example, if you mark a FAM accessory as in use, the service also marks the PXI board your team attached to the FAM accessory, as we

### Tracking Asset Utilization with
 LabVIEW

Record utilization information about the assets performing test and measurement
 tasks.

When you track an asset, you also track the assets your team connected to it. For
 example, if you mark a FAM accessory as in use, the service also marks the PXI board
 your team attached to the FAM accessory, as well as the PXI chassis that contains the
 board and the PXI controller installed in the PXI chassis.

#### What to Use

Note

#### What to Do

1. Create the following diagram in a VI to record utilization information about the
 asset(s) performing test and measurement tasks. Customize the gray sections
 for your unique programming goals. [IMAGE alt='image' src='GUID-2EA09BF9-89C9-4730-976A-836DEEA2FE46-a5.png'] 1Start Utilization collects
 utilization data about the asset(s) performing a test or
 measurement task.2End Utilization stops collecting
 utilization data when the test or measurement task
 finishes.

#### Troubleshooting

- If you do not see asset utilization data show up on the server, you may need
 to wait a few minutes for the client to send the data to the server.

Parent topic:

Connecting to LabVIEW and DIAdem

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=transfer-messages.html language=enus -->
## TOPIC 00183: Sending Messages Between Systems

- bundle_id: `systemlink-server`
- source_path: `transfer-messages.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/transfer-messages.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use messages to send commands, status updates, or data, such as JSON, between systems and applications. Messages operate as a network queue, which uses the publish/subscribe model. What to Use You can find the SystemLink Message and Configuration APIs on the Data Communication palette in LabVIEW, La

### Sending Messages Between Systems

Use messages to send commands, status updates, or data, such as JSON, between
 systems and applications. Messages operate as a network queue, which uses
 the publish/subscribe model.

#### What to Use

Note

#### What to Do

1. Create the following diagram in a VI to subscribe to and read messages. 
 Customize the gray sections for your unique programming goals. 1Open Configuration initiates a connection with a SystemLink
 server.2Open creates a message session with the server, which allows you to subscribe to a message queue.3Subscribe registers an endpoint, such as a web application, to a specific topic. 
 Note Subscribers of a topic receive every message published to that topic beginning from the point they subscribe. They do not receive or have access to messages sent before that point.4Read returns a message from the queue.
 If there are no queued messages, the call
 synchronously blocks up to the timeout specified or to
 the maximum timeout defined by the web server, whichever
 is smaller. If you leave the timeout milliseconds input
 unwired, the Read node has a
 default timeout of 100 milliseconds. In this example,
 the timeout is set to 2000 milliseconds. Note NI Web Server has a
 maximum timeout of 10 seconds. You can edit the
 timeout for the NI Web Server.To adjust the timeout for NI Web Server, edit the configuration file of the server. Refer to
 Configuring NI Web Server more information.Use Unflatten from JSON when using
 Read to make messages easier to
 parse from a web browser.Use a While Loop to continue reading
 messages until a condition is met. In this example, the
 node reads messages until there is an error.
2. Create the following diagram in a VI to publish messages. 
 Customize the gray sections for your unique programming goals. 1Open Configuration initiates a connection with a SystemLink
 server.2Open creates a message session with the server, allowing you to publish messages to a message queue.3Publish writes a message to a topic. If multiple messages are published, the subscriber reads the messages in the order they are received. 
 Use Flatten to JSON when using Publish to convert LabVIEW data types to string, which is the only data type messages support, and to easily interact with the data when reading messages in LabVIEW and other JSON-supported languages.Use a Case Structure to set up conditions for when to publish. In this example, Publish write messages until you move the Publish switch to the off position on the panel.Use a While Loop to continue publishing tags until a condition is met. In this example, Publish writes messages until there is an error.4Close terminates the message session with the server.5Close Configuration cleans up connections associated with the configuration by invalidating any open references to created objects.

#### Troubleshooting

- Call Subscribe before calling Read . You must subscribe to a topic before your program will read a message.
- Verify that you are subscribed to the right topic before running the code. 
 Note Topics are case sensitive.

Parent topic:

Connecting to LabVIEW and DIAdem

Related tasks:

- Transferring Data Using Tags

Related information:

- SystemLink API Reference
- Configuring NI Web Server

<!--NI_TOPIC bundle=systemlink-server path=transfer-tags.html language=enus -->
## TOPIC 00184: Transferring Data Using Tags

- bundle_id: `systemlink-server`
- source_path: `transfer-tags.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/transfer-tags.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use tags to send and receive data from one system to other systems. What to Use You can find the SystemLink Tag and Configuration APIs on the Data Communication palette in LabVIEW, LabVIEW NXG Web Module, and G Web Development Software. This example uses G Web Development Software Tag and Configurat

### Transferring Data Using Tags

Use tags to send and receive data from one system to other systems.

#### What to Use

Note

#### What to Do

1. Create the following diagram in a VI to read tag data. 
 Customize the gray sections for your unique programming goals. 1Open Configuration initiates a connection with a SystemLink
 server.2Open Tag opens a reference to a tag on
 the server defined by the configuration. Note Use
 Query Tags instead of
 Open Tag if you do not know the
 data type of the tag.If the reference does not exist on the server,
 Open Tag will create one.
 Open Tag will return an error
 if a tag with the same path but of a different data type
 already exists.Use a For Loop to open a tag for
 each element in an array of tag names. In this example,
 the VI opens an array of station temperature tags.3Read Tag checks the current value of
 the tag. Follow an open/read/close model when using this VI.
 Note 
 Use Multi Read instead of
 Read Tag if you need to read
 multiple tag values as a part of a single operation.Use a While Loop to continue reading
 tags until a condition is met. In this example, Read Tag
 returns tag values unless the Boolean
 constant changes to True.4Close Tag closes a tag reference. 
 Use a For Loop to close tags from an array of tag names, or call Open Tag (Multiple) instead.5Close Configuration invalidates any open reference to created objects and closes connections associated with the configuration.
2. Create the following diagram in a VI to write a tag value. 
 Customize the gray sections for your unique programming goals. 1Open Configuration initiates a connection with a SystemLink
 server.2Open Tag opens a reference to a tag on the server defined by the configuration. 
 Note Use Query Tags instead of Open Tag if you do not know the data type of the tag.If the reference does not exist on the server, Open Tag will create one. Open Tag will return an error if a tag with the same path but of a different data type already exists.Use a For Loop to open a tag for each element in an array of tag names. In this example, Open Tag opens an array of station temperature tags.3Write Tag writes a value to a tag.
 Follow an open/write/close model when using this VI. Note Use
 Multi Write instead of
 Write Tag if you need to write
 multiple tag values as a part of a single operation.If you want the server to manage the time stamp of when
 the tag was written, leave the time stamp cluster
 unwired.Use a While Loop to continue reading
 tags until a condition is met. In this example,
 Write Tag writes tags until you
 click the stop button on the panel.Use a For Loop to write a tag for
 each element in an array of tag names.4Close Tag closes a tag reference.
 Use a For Loop to close tags
 from an array of tag names, or call Open Tag
 (Multiple) instead.5Close Configuration invalidates any open reference to created objects and closes connections associated with the configuration.

#### Troubleshooting

- Verify that the data type of the tag matches the
 Function configuration or selected polymorphism
 of the VI. For instance, if the data type of the tag called from the server
 is a double-precision, floating-point number, select
 Double as your Function
 configuration .

Parent topic:

Communicating Data with Tags

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=transferring-files-from-disk-to-server.html language=enus -->
## TOPIC 00185: Transferring Files from Disk to the Server

- bundle_id: `systemlink-server`
- source_path: `transferring-files-from-disk-to-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/transferring-files-from-disk-to-server.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Send files stored on disk from a client to the server to save, process, or enable access for others. What to Use You can find the SystemLink File Transfer and Configuration APIs on the Data Communication palette in LabVIEW 2016 or later. What to Do On the client, create the following diagram in a VI

### Transferring Files from Disk to the Server

Send files stored on disk from a client to the server to save, process, or enable access for others.

#### What to Use

You can find the SystemLink File Transfer and Configuration APIs on the Data
 Communication palette in LabVIEW 2016 or later.

#### What to Do

On the client, create the following diagram in a VI to send files from disk to the server.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-3BDD600B-2BF6-4974-97C1-2C7D50811B01-a5.png']

| 1 | Open Configuration initiates a connection to the file service on the SystemLink Server. Note SystemLink Server supports both HTTP and AMQP configurations. |
| --- | --- |
| 2 | Send uses the path you specify to locate the local file you want to upload. It then reads and transmits the data of the file in packets to the file service. The file service then creates the file on the server and writes the packets to the file. |

#### Troubleshooting

- If your client disconnects during a file transfer, you need to abort the file transfer and wait for the server to automatically delete the partial file transfer. After the server deletes the partial file transfer, initiate a new file transfer. 
 Note If a partial file transfer does not progress within an hour, the server automatically treats it as an abandoned transfer and deletes it.
- If your file transfer times out because your file is large or from memory, use Send Packet to send different packet sizes during the file transfer and to manage when to transfer a packet.
- If no data is available to send within the one-hour timeout period for file transfers, use Send Packet to send a zero-byte packet to keep the file transfer active.

#### Examples

- Sync File IO

Parent topic:

Connecting to LabVIEW and DIAdem

Related tasks:

- Transferring Files from Memory to the Server

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=transferring-files-from-memory-to-server.html language=enus -->
## TOPIC 00186: Transferring Files from Memory to the Server

- bundle_id: `systemlink-server`
- source_path: `transferring-files-from-memory-to-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/transferring-files-from-memory-to-server.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Send files stored in memory from a client to the server to save, process, or enable access for others. What to Use You can find the SystemLink File Transfer and Configuration APIs on the Data Communication palette in LabVIEW 2016 or later. What to Do On the client, create the following diagram in a

### Transferring Files from Memory to the Server

Send files stored in memory from a client to the server to save, process, or enable access for others.

#### What to Use

You can find the SystemLink File Transfer and Configuration APIs on the Data
 Communication palette in LabVIEW 2016 or later.

#### What to Do

On the client, create the following diagram in a VI to send files from memory to the server.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-C3ABE401-3919-46DF-ACF4-48CFB71BA6B3-a5.png']

| 1 | Open Configuration initiates a connection with the file service on the SystemLink server. Note SystemLink Server supports both HTTP and AMQP configurations.. |
| --- | --- |
| 2 | Create generates a writable file on the file service using the name and properties you specify. |
| 3 | Within the For Loop, Send Packet transmits the file's data in packets to the file service. LabVIEW automatically numbers the packets zero-indexed sequential integers. The file service will use the packet numbering to sequentially write the packets to disk on the server after it receives the final packet. |
| 4 | Send Last Packet transmits the last packet of data to the file service. After receiving the final packet, the file service sequentially writes the packets to disk on the server. After Send Last Packet transmits the last packet of data, the file is no longer writable. Therefore, you cannot send additional packets of the file to the file service. |
| 5 | Close invalidates and closes all open references. |

#### Troubleshooting

- If your client disconnects during a file transfer, you need to abort the file transfer and wait for the server to automatically delete the partial file transfer. After the server deletes the partial file transfer, initiate a new file transfer. 
 Note If a partial file transfer does not progress within an hour, the server automatically treats it as an abandoned transfer and deletes it.

- If your system has unreliable network
 connections or slow transfer rates, you may need to adjust the packet size for
 the file transfer. Decrease the packet size input of
 Send Packet to a smaller number to prevent timeouts.
 Note A smaller packet size
 means more packets are sent, which increases the total time required to
 transfer the file because more roundtrips must occur between the server and
 client.

#### Examples

- Sync File IO

Parent topic:

Connecting to LabVIEW and DIAdem

Related tasks:

- Transferring Files from Disk to the Server

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=troubleshooting-failed-openid-connect-authentication.html language=enus -->
## TOPIC 00187: Troubleshooting Failed OpenID Connect Authentication

- bundle_id: `systemlink-server`
- source_path: `troubleshooting-failed-openid-connect-authentication.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/troubleshooting-failed-openid-connect-authentication.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use OpenID Connect provider logs and NI Web Server logs to resolve common authentication issues. You can find these logs in the following locations: To locate the most recent error log file for NI Web, navigate to C:\ProgramData\National Instruments\Web Server\logs\error.current.log. To locate the l

### Troubleshooting Failed OpenID Connect
 Authentication

Use OpenID Connect provider logs and NI Web Server logs to resolve common
 authentication issues.

- To locate the most recent error log file for NI Web, navigate to
 C:\ProgramData\National Instruments\Web
 Server\logs\error.current.log .
- To locate the log files for your application, consult the documentation for
 your OpenID Connect provider.

| Error | Details | Steps to Resolve | Example Error Log |
| --- | --- | --- | --- |
| SystemLink returns Internal Server Error when attempting to log in. | This error typically occurs for the following reasons. SystemLink returns a large number of claims. SystemLink returns claims with values that exceed the capacity of the OpenID Connect shared memory cache. | As an administrator, open C:\\Program Files\\National Instruments\\Shared\\Web Server\\conf\\defines.d\\, and open 50_mod_auth_openidc-defines.conf. Configure Define AUTH_OIDC_CACHE_ENTRY_SIZE to a number larger than the required size of the cache entry specified in the error log. | oidc_cache_shm_set: could not store value since value size is too large oidc_cache_set: could NOT store X bytes in shm cache backend for key Y |
| The user redirects to the SystemLink login page after authentication. | This error typically occurs for the following reasons. The provider is using an asymmetric encryption algorithm for ID token management. Also, the private keys are missing or incorrect. The provider is using an unsupported encryption algorithm for ID token management. | Confirm that the provider uses supported encryption and signing algorithms. For more information, refer to Supported Signing and Encryption Algorithms and the documentation for your provider. If the provider is using asymmetric ID token management encryption, confirm the configuration of the following: The private key in the provider-issuer-uri.conf file. The public key that corresponds to the private key in the provider. For information on configuring the private key, refer to Configuring SystemLink to Connect to Your OpenID Connect Provider. For information on configuring the public key, refer to the documentation for your provider. For information on configuring the encryption algorithm for ID token management refer to the documentation for your provider. | oidc_proto_parse_idtoken: oidc_jwt_parse failed |

Parent topic:

Managing Access with OpenID Connect

Related tasks:

- Configuring SystemLink to Connect to Your OpenID Connect Provider

Related reference:

- Supported Signing and Encryption Algorithms

<!--NI_TOPIC bundle=systemlink-server path=troubleshooting-system-connection-issues.html language=enus -->
## TOPIC 00188: Troubleshooting System Connection Issues

- bundle_id: `systemlink-server`
- source_path: `troubleshooting-system-connection-issues.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/troubleshooting-system-connection-issues.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Troubleshoot systems with connection issues. In the SystemLink web application, click System ManagementSystems. Hover over the connection status icon for your system to see the status message. Use the following table to understand and troubleshoot the connection status of your system. Icon Status Me

### Troubleshooting System Connection
 Issues

Troubleshoot systems with connection issues.

1. In the SystemLink web application, click System Management»Systems.
2. Hover over the connection status icon for your system to see the status
 message.
3. Use the following table to understand and troubleshoot the connection status of
 your system. 
 Icon
 Status Message
 Description[IMAGE alt='image' src='GUID-4C76937A-1A87-4BA9-918A-83EE51012762-a5.png']
 The system is connected.
 The system is fully connected via SaltTCP (4505, 4506)
 and has successfully authenticated with the SystemLink
 server via the /niauth/v1/auth HTTP route.
 [IMAGE alt='image' src='GUID-6ED0E27F-C5CE-49F4-A454-5AF8131703DA-a5.png']
 The system is disconnected.
 The system is is not connected via SaltTCP (4505, 4506).
 See the SaltStack communication model documentation for more
 information.
 [IMAGE alt='image' src='GUID-D13A2FC2-5B5C-4881-AC09-969CBEE2B518-a5.png']
 The system is approved but it did not try to connect
 yet.
 The system has been approved by an authorized user, but
 it is not trying to connect to the SystemLink
 server.
 [IMAGE alt='image' src='GUID-D13A2FC2-5B5C-4881-AC09-969CBEE2B518-a5.png']
 The system is connected and the refresh job is
 running.
 The system is fully connected via SaltTCP (4505, 4506)
 and is currently running the initial refresh job to complete
 the connection.
 [IMAGE alt='image' src='GUID-6ED0E27F-C5CE-49F4-A454-5AF8131703DA-a5.png']
 The system is connected but the refresh job
 failed.
 The system has attempted to execute 5 refresh jobs and
 each one has failed. Ensure that the SystemLink client and
 its dependencies are properly installed and running.
 [IMAGE alt='image' src='GUID-D13A2FC2-5B5C-4881-AC09-969CBEE2B518-a5.png']
 The system is activated but the connection is not
 established yet.
 The system has been activated but needs to be approved by
 an authorized user.
 [IMAGE alt='image' src='GUID-0B6ED918-5D7F-4E2A-9C62-A6CE98C66F2E-a5.png']
 The system is connected but it cannot publish
 data.
 The system can communicate with the server over SaltTCP
 (4505, 4506), but cannot reach or authenticate the
 server over HTTP. Complete the following steps to
 troubleshoot.Check that you are specifying the fully
 qualified domain name of the SystemLink server in
 the SystemLink client tray app on Windows or NI
 MAX on NI Linux RT.
 Ensure that your security certificate has not
 expired and that the system can reach the
 appropriate certificate authority.
 Regenerate the system API key by changing the
 workspace of the system or deleting it from the
 server and reconfiguring the client to connect
 again.Note Deleting the system removes all tracked data about
 the system from the server.

Parent topic:

Managing Your Systems

Related tasks:

- Installing and Configuring SystemLink Server and Clients
- Connecting a Windows Target to Your SystemLink Server
- Connecting an NI Linux Real-Time Target to Your SystemLink Server

Related information:

- Understanding SaltStack Communication and Security

<!--NI_TOPIC bundle=systemlink-server path=troubleshooting-tag-data.html language=enus -->
## TOPIC 00189: Verifying Your Tag Data in Tags

- bundle_id: `systemlink-server`
- source_path: `troubleshooting-tag-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/troubleshooting-tag-data.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Troubleshoot your test and measurement data in Tags to verify your system returns tag data as expected. Before you start troubleshooting your tag data in Tags, you must: Verify the system for which you want to obtain and communicate tag data is a managed system in Systems Manager. Verify the applica

### Verifying Your Tag Data in Tags

Troubleshoot your test and measurement data in Tags to verify
 your system returns tag data as expected.

Tags

- Verify the system for which you want to obtain
 and communicate tag data is a managed system in Systems Manager .
- Verify the application sending tag data to your
 SystemLink Server is running.

1. In the SystemLink web application, click Tags.
2. Search for a tag in one of the following ways: 
 
 You can use the wildcard character (*) when you search by path.
  - Type a tag path or part of a tag path in
 the search bar.
  - Click the filter button next to the search bar to search for exact matches. You can include multiple queries, but only tags matching all the queries return as results.
3. Double-click the tag to open it.
4. Under 
 Tag Details, verify the details for the tag appear accurate.
  1. Verify the tag value updates at the time interval you set in the application.
  2. Verify the data type of your tag is correct.
  3. Verify the workspace your tag belongs to is correct.
5. Optional: 
 Under 
 History, review the graph to visualize your data. 
 Note To view historical data, you must have 
 Retention set to either 
 Count, 
 Duration, or 
 Permanent. If you set 
 Retention to 
 None, SystemLink will not retain the historical data of your tag.
  1. If you see an event where your data did not perform as expected, select the magnifying glass to examine the value closer.
  2. Click the camera ([IMAGE alt='image' src='GUID-44C1EDD2-4C00-4759-91BB-2F8E4D216DE1-a5.png']) to capture the data for
 analysis.
  3. To return to the default view of the historical tag values,
 double-click the graph.
6. If your data is not performing as expected, debug your application in the programming environment. 
 The following table highlights common troubleshooting tips. 
 InstructionsExampleVerify the endpoint of your application is your SystemLink Server URL. 
 Note The protocol must be HTTP.http://localhost:80Verify you defined the tag path with dot separators.Station1.Temperature.BuildingAVerify your Salt minion's ID is correct. There are two ways you can locate your system's minion ID: 
 On disk 
 (Windows) 
 C:\ProgramData\National Instruments\salt\conf\minion_id(Linux RT) 
 \etc\salt\minion_idIn LabVIEW 2016 or laterAdd
 Build Path to the block
 diagram.Specify the tag name, or path, and wire it to
 Build Path. Note Use
 dot separators instead of slashes or hyphens; for
 example, Station1.Temperature.Leave the namespace (top-level
 VI) input empty.Wire
 an indicator to Build Path.Execute the application to obtain the minion ID.<hostname>_<MAC address>-<serial number>Note Refer to 
 *Transferring Data Using Tags* in this manual for more information.
7. After you finish debugging your application, reopen Tags and
 confirm the tag values return as expected.

Parent topic:

Communicating Data with Tags

Related tasks:

- Transferring Data Using Tags

<!--NI_TOPIC bundle=systemlink-server path=troubleshooting.html language=enus -->
## TOPIC 00190: Troubleshooting Package Deployment and Server Configuration

- bundle_id: `systemlink-server`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/troubleshooting.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Understand and solve potential issues when deploying packages to clients. Use the following table to troubleshoot different aspects of SystemLink installation and package deployment based on the problem you encounter. Problem Possible Cause Steps to Take Available tab doesn’t display packages stored

### Troubleshooting Package Deployment and Server
 Configuration

Understand and solve potential issues when deploying packages to clients.

Use the following table to troubleshoot different aspects of SystemLink
 installation and package deployment based on the problem you encounter.

| Problem | Possible Cause | Steps to Take |
| --- | --- | --- |
| Available tab doesn’t display packages stored in the server's package repository. Available tab displays errors or warnings. Installing packages on clients fails because SystemLink cannot locate packages. | Your proxy server might not be correctly configured, preventing your server from accessing the feeds you need. | Ensure you have configured your proxy server to use with SystemLink, including specifications for bypassing local addresses. |
| Installation time on clients is unexpectedly high or differs widely between similar clients. | SystemLink might be repeatedly timing out while trying to update feeds the server cannot reach. This might happen when a client tries to access ni.com feeds but can only access the feeds stored on the server. | Complete one of the following actions to ensure clients can access the feeds they need: Configure clients with your proxy server information.In the Software tab of the system details, remove the feeds that the clients cannot access. |

Parent topic:

Deploying Applications to Clients on a Server

Related tasks:

- Configuring Proxy Settings for SystemLink
- Deploying Applications to Clients on a Server
- Enabling Client Access to Packages

<!--NI_TOPIC bundle=systemlink-server path=unblocking-data-sources-analysis-automation-tasks.html language=enus -->
## TOPIC 00191: Unblocking Data Sources for Analysis Automation Tasks

- bundle_id: `systemlink-server`
- source_path: `unblocking-data-sources-analysis-automation-tasks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/unblocking-data-sources-analysis-automation-tasks.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Unblock data sources to make them available for an Analysis Automation instance. Analysis automation instance tasks can use all available DataFinder instances as data sources. When you create a task, you select the data source for the analysis. SystemLink does not support the file service as a data

### Unblocking Data Sources for Analysis Automation Tasks

Unblock data sources to make them available for an Analysis Automation instance.
 Analysis automation instance tasks can use all available DataFinder instances as data
 sources. When you create a task, you select the data source for the analysis.

Note

1. In Analysis Automation, click
 Instance on the dashboard.
2. Click Data Sources and select the type of data
 source.
3. Select a data source with the status 
 Data source blocked and select 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Unblock to unblock the data source for tasks.
4. Optional: 
 Select a data source with the status Unblocked and
 select [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Block to block the data source for tasks. 
 The Analysis automation instance cannot analyze data from blocked data
 sources.
5. Select [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Reassign Connected Tasks to reassign the tasks of a data source to a renamed data source.

Parent topic:

Analyzing Data

<!--NI_TOPIC bundle=systemlink-server path=updating-analysis-automation-procedures.html language=enus -->
## TOPIC 00192: Updating Analysis Automation Procedures

- bundle_id: `systemlink-server`
- source_path: `updating-analysis-automation-procedures.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/updating-analysis-automation-procedures.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use analysis automation procedures to automate data analyses with Analysis Automation. You create and edit analysis automation procedures in DIAdem, Python, or Jupyter notebooks. To edit an analysis automation procedure, download it to your client machine, make your modifications in your programming

### Updating Analysis Automation Procedures

Use analysis automation procedures to automate data analyses with Analysis Automation.
 You create and edit analysis automation procedures in DIAdem, Python, or Jupyter notebooks.
 To edit an analysis automation procedure, download it to your client machine, make your
 modifications in your programming environment, and upload the modified procedure to Analysis
 Automation.

1. In Analysis Automation, click
 Instance on the dashboard.
2. Click Procedures.
3. Select the analysis automation procedure you want to update and click 
 [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Download.
4. Click Save File»OK to save the file on your client computer.
5. Edit and save the analysis automation procedure with DIAdem, Jupyter, or Python.
6. Return to Analysis Automation, select the analysis
 automation procedure you are updating and click »[IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Update.
7. Navigate to the revised analysis automation procedure on your client machine
 and click Open.
8. Optional: 
 Modify the Workspace if you want a different set of
 users to work with this procedure.
9. Click Apply to accept the settings. 
 The analysis automation procedure displays under Procedures.
 Note If you don't have
 sufficient privileges, the Approved column displays
 this icon [IMAGE alt='image' src='GUID-7B4AFC35-EAFC-4233-A917-3BD21B4425BE-a5.svg'] indicating the procedure is pending
 approval. A user with permissions to approve or reject procedures needs to
 click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Approve to approve the procedure.

Parent topic:

Adding Analysis Automation Procedures

Related tasks:

- Creating Analysis Automation Procedures in DIAdem

<!--NI_TOPIC bundle=systemlink-server path=updating-instances-after-tdm-upgrade.html language=enus -->
## TOPIC 00193: Upgrading an Instance with a New SystemLink TDM Version

- bundle_id: `systemlink-server`
- source_path: `updating-instances-after-tdm-upgrade.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/updating-instances-after-tdm-upgrade.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: If you have installed a new version of SystemLink TDM software on your existing server, upgrade your Data Preparation, Data Indexing, and Analysis Automation instances. NI recommends you always install a software upgrade on a new server. Refer to the topics in this manual on how to backup and restor

### Upgrading an Instance with a New SystemLink
 TDM Version

If you have installed a new version of SystemLink TDM software on your existing server,
 upgrade your Data Preparation, Data Indexing, and Analysis Automation instances.

Note

1. In 
 Data Preparation, 
 Data Indexing, or 
 Analysis Automation, open the instance overview.
2. Select the instance you want to upgrade. 
 Note SystemLink flags instances from earlier
 versions with a red exclamation mark.
3. Click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Upgrade. The Upgrade button only displays if a new
 version exists.

Repeat this procedure until all Data Preprocessor, DataFinder,
 and Analysis Automation instances are using the newest software version.

Parent topic:

Maintaining DataFinder, Data Preprocessor, and Analysis Automation Instances

Related tasks:

- Creating a Backup of an Instance
- Restoring an Instance

<!--NI_TOPIC bundle=systemlink-server path=updating-ni-software-on-systemlink-linux-rt-client.html language=enus -->
## TOPIC 00194: Updating NI Software on a SystemLink Linux RT Client

- bundle_id: `systemlink-server`
- source_path: `updating-ni-software-on-systemlink-linux-rt-client.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/updating-ni-software-on-systemlink-linux-rt-client.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Upgrade NI software on a SystemLink Linux RT client from the SystemLink web application. During the update, SystemLink formats the client and installs a new version of Linux RT System Image. Only systems with NI SystemLink Client 19.0 or later can upgrade to the latest Linux RT System Image from the

### Updating NI Software on a SystemLink Linux RT Client

Upgrade NI software on a SystemLink Linux RT client from the SystemLink web
 application. During the update, SystemLink formats the client and installs a new
 version of Linux RT System Image.

Note

Before you begin, save all data or software stored on the client. The upgrade erases all installed software and data.

1. In the SystemLink web application, click Systems Management»Systems.
2. Select the Linux RT client system(s) you want to update and then click 
 Software. 
 Note If SystemLink does not discover any system
 images for your client, add the images feed.
3. Click 
 System Images and select which version of the system image you want to install on the client.
4. Click 
 Next.
5. Review the summary and click 
 Apply. 
 SystemLink deploys and installs the system image on the target.

After the upgrade finishes, the client automatically reconnects with the server and reports the job succeeded in the job history.

Parent topic:

Deploying Applications to Clients on a Server

<!--NI_TOPIC bundle=systemlink-server path=uploading-custom-files.html language=enus -->
## TOPIC 00195: Uploading Custom Files to Test Monitor

- bundle_id: `systemlink-server`
- source_path: `uploading-custom-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/uploading-custom-files.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Attach any type of file, including TDMS files, as a TestStand result to upload data to Test Monitor. Integrating Test Monitor with TestStand allows you to see test metadata in the SystemLink web application. To create a more complete picture of the tests you run in TestStand, you can configure TestS

### Uploading Custom Files to Test Monitor

Attach any type of file, including TDMS files, as a TestStand result to upload data to Test Monitor.

Integrating Test Monitor with TestStand allows you to see test metadata in the SystemLink
 web application. To create a more complete picture of the tests you run in TestStand, you
 can configure TestStand or LabVIEW 2015 or later to upload any test result file to Test
 Monitor.

- [Uploading Custom Files with a VI](uploading-files-with-a-vi.html) Upload custom files to Test Monitor individually or in batches using TestStand and LabVIEW 2015 or later.
- [Uploading Files with a TestStand Step](uploading-files-with-teststand.html) Upload custom files to Test Monitor from within TestStand.

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-server path=uploading-files-to-amazon-s3.html language=enus -->
## TOPIC 00196: Uploading Files to Amazon Simple Storage Service (S3)

- bundle_id: `systemlink-server`
- source_path: `uploading-files-to-amazon-s3.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/uploading-files-to-amazon-s3.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure SystemLink file service to store incoming data in Amazon Web Services (AWS). Using Amazon S3 as your file storage disables all file moving rules.Before you begin, complete the following tasks. Create an AWS account. Create a bucket with a policy that allows the following actions. s3:PutObj

### Uploading Files to Amazon Simple Storage
 Service (S3)

Configure SystemLink file service to store incoming data in Amazon Web Services
 (AWS).

Note

Before you begin, complete the following tasks.

- Create an AWS account.
- Create a bucket with a policy that allows the following actions. Note For more information, refer to *Bucket policy
 examples*.
  - s3:PutObject
  - s3:PutObjectTagging
  - s3:GetObject
  - s3:GetObjectAttributes
  - s3:DeleteObject
- Ensure that you know your access keys, secret keys, bucket name, and region.

Note

1. In the NI SystemLink Server Configuration tool, under NI SystemLink
 Service Manager, select
 FileIngestion.
2. Select Amazon Simple Storage service (S3).
3. Specify the following settings. 
 SettingDescriptionAccess Key
 The access key string for the user provided access to the S3 bucket.Secret Key
 The secret key string for the user provided access to the S3 bucket.Region
 Sets the AWS region where the bucket is located. For example,
 us-east-1.Bucket
 The name of the bucket in the specified AWS region stores the files. To use the
 name of the SystemLink workspace in the bucket name, enter
 <workspace>. Ensure that the workspace name follows the
 bucket naming rules.Folder
 (optional) Specifies the folder to which you want to save your files. You can
 enter <workspace> to use the name of the SystemLink
 workspace in the folder name.
4. Click Apply to commit your entries. 
 Note To avoid duplicate file collisions,
 SystemLink ensures all files names in S3 use a unique ID. The filenames from SystemLink
 are not shown in Amazon S3. To view the SystemLink filename, refer to the
 FileName tag on the Properties tab of the file in AWS.

File System

Note

Files

Parent topic:

Configuring FileIngestion Storage Options

Related tasks:

- Moving Incoming Files to Other Locations

Related information:

- Sign up for AWS
- Creating a bucket
- Bucket naming rules
- Bucket policy examples

<!--NI_TOPIC bundle=systemlink-server path=uploading-files-to-amazon-s3_2.html language=zhcn -->
## TOPIC 00197: 将文件上传至Amazon Simple Storage Service (S3)

- bundle_id: `systemlink-server`
- source_path: `uploading-files-to-amazon-s3_2.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/zhcn/uploading-files-to-amazon-s3_2.html
- source_language: `zhcn`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: 配置SystemLink文件服务将传入的数据存储在Amazon Web Service (AWS)中。 使用Amazon S3作为文件存储会禁用所有文件移动规则。 开始之前，请完成以下任务。 创建AWS账户。 创建一个bucket，bucket的policy允许下列操作。s3:PutObjects3:PutObjectTaggings3:GetObjects3:GetObjectAttributess3:DeleteObject详细信息，请参考Bucket policy examples。 确保知晓访问秘钥、私有秘钥、bucket名称和区域。 与Amazon S3进行交互会在Amazon方产生

### 将文件上传至Amazon Simple Storage Service (S3)

配置SystemLink文件服务将传入的数据存储在Amazon Web Service (AWS)中。

备注

开始之前，请完成以下任务。

- 创建AWS账户。
- 创建一个bucket，bucket的policy允许下列操作。 备注 详细信息，请参考*Bucket policy examples*。
  - s3:PutObject
  - s3:PutObjectTagging
  - s3:GetObject
  - s3:GetObjectAttributes
  - s3:DeleteObject
- 确保知晓访问秘钥、私有秘钥、bucket名称和区域。

备注

1. 在NI SystemLink Server Configuration工具中，在NI SystemLink Service Manager下选择FileIngestion。
2. 选择Amazon Simple Storage Service (S3)。
3. 指定以下设置。 
 设置说明信息Access Key
 为用户访问S3 bucket提供的访问密钥字符串。Secret Key
 为用户访问S3 bucket提供的密钥字符串。区域
 设置bucket所在的AWS区域。例如，us-east-1。Bucket
 指定AWS区域中bucket的名称，用于存储文件。要在bucket名称中使用SystemLink工作区的名称，请输入<workspace>。确保工作区名称符合bucket命名规则。文件夹
 （可选）指定保存文件的文件夹。可在文件夹名称中输入<workspace>，使用SystemLink工作区的名称。
4. 单击应用，提交输入的信息。 
 备注 为避免文件重复冲突，SystemLink确保S3中的所有文件名使用唯一ID。SystemLink的文件名不会显示在Amazon S3中。要查看SystemLink文件名，请参考AWS中属性选项卡的文件名称标签。

File System

备注

文件

上级主题：

存储和管理文件

<!--NI_TOPIC bundle=systemlink-server path=uploading-files-with-a-vi.html language=enus -->
## TOPIC 00198: Uploading Custom Files with a VI

- bundle_id: `systemlink-server`
- source_path: `uploading-files-with-a-vi.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/uploading-files-with-a-vi.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload custom files to Test Monitor individually or in batches using TestStand and LabVIEW 2015 or later. On the diagram, use Send File to specify a file or multiple files to upload to SystemLink. Create one output for each file ID you want to return. To upload many files, create an array output for

### Uploading Custom Files with a VI

Upload custom files to Test Monitor individually or in batches using TestStand and LabVIEW 2015 or later.

1. On the diagram, use Send File to specify a file or multiple files to upload to SystemLink.
2. Create one output for each file ID you want to return. To upload many files, create an array output for the file IDs you want to return.
3. Click 
 Run to return a unique file ID for each file.
4. In TestStand, store the file IDs using a local variable.
  1. In the 
 Variables pane, right-click 
 Locals.
  2. Click 
 Insert Local and select 
 String.
  3. Enter the file ID or array of file IDs.
  4. Repeat for each file ID or array of file IDs you want to store.
5. Attach the file(s) to a test result.
  1. Click the test step that uploaded the file.
  2. Under 
 Properties, click 
 Additional Results.
  3. Click 
 + to create a custom result.
  4. Under Name, type "NI. SYSTEMLINK. TESTMONITOR.
 FILE" (including quotes). 
 Use this name for all additional results you add.
  5. Under 
 Value to Log, specify the local variable you created.

Test Monitor automatically attaches the file you specified to the current test result.

Parent topic:

Uploading Custom Files to Test Monitor

Related tasks:

- Uploading Files with a TestStand Step

<!--NI_TOPIC bundle=systemlink-server path=uploading-files-with-teststand.html language=enus -->
## TOPIC 00199: Uploading Files with a TestStand Step

- bundle_id: `systemlink-server`
- source_path: `uploading-files-with-teststand.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/uploading-files-with-teststand.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload custom files to Test Monitor from within TestStand. Create a step to upload the file or group of files. Right-click in the Steps pane of your sequence file. Click Insert StepSystemLinkUpload File. Specify a file path or ID for one or more files to upload. Store the file IDs using local variab

### Uploading Files with a TestStand Step

Upload custom files to Test Monitor from within TestStand.

1. Create a step to upload the file or group of files.
  1. Right-click in the 
 Steps pane of your sequence file.
  2. Click 
 Insert Step»SystemLink»Upload File.
2. Specify a file path or ID for one or more files to upload.
3. Store the file IDs using local variables.
  1. In the 
 Variables pane, right-click 
 Locals.
  2. Click 
 Insert Local and select 
 String.
  3. Enter the file ID or array of file IDs.
  4. Repeat for each file ID or array of file IDs you want to store.

Test Monitor

File Viewer

Parent topic:

Uploading Custom Files to Test Monitor

Related tasks:

- Uploading Custom Files with a VI

<!--NI_TOPIC bundle=systemlink-server path=user-manual-welcome.html language=enus -->
## TOPIC 00200: SystemLink Server User Manual

- bundle_id: `systemlink-server`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/user-manual-welcome.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SystemLink Server User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### SystemLink Server
 User Manual

The SystemLink Server User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- License Setup and Activation
- Discussion Forums
- NI Learning Center
- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=using-data-indexing-as-asamods-server.html language=enus -->
## TOPIC 00201: Using a DataFinder Instance as ASAM ODS Server

- bundle_id: `systemlink-server`
- source_path: `using-data-indexing-as-asamods-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/using-data-indexing-as-asamods-server.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a DataFinder instance as an ASAM ODS server to display data in the search areas according to the ASAM data model, and make it available to clients through the Corba interface. In Data Indexing, click DataFinder Instances. Select an instance and click ManageConnectRemote Access. Select ASAM ODS,

### Using a DataFinder Instance as ASAM ODS Server

Use a DataFinder instance as an ASAM ODS server to display data in the search areas according to the ASAM data model, and make it available to clients through the Corba interface.

1. In 
 Data Indexing, click 
 DataFinder Instances.
2. Select an instance and click [IMAGE alt='image' src='GUID-3BDA0C0E-A50A-4089-9A5D-C8E0FA54D331-a5.png']»Manage»[IMAGE alt='image' src='GUID-A2DAEE93-CE77-45A0-ABEE-9B9F2BBACA6F-a5.png']»Connect»Remote Access.
3. Select ASAM ODS, enable Enable NI ASAM ODS
 Server, and click OK. 
 Use the displayed connection information to connect a client with this
 DataFinder instance. You use a DataFinder instance as an ASAM ODS server to
 display, browse, and filter data with an ASAM-conform data model. The
 applications supporting the ASAM ODS Corba interface can access the ASAM ODS
 server in order to find and load this data.
4. Stop the server to complete the process.
5. Optional: 
 To make custom properties available for searching and filtering through the
 Corba interface of ASAM ODS:
  1. Select Custom Properties and click, for example,
 Channel.
  2. Select the custom properties to optimize and click
 Optimize
6. Click Apply to accept the settings.

Parent topic:

Indexing Data

<!--NI_TOPIC bundle=systemlink-server path=viewing-calibration.html language=enus -->
## TOPIC 00202: Viewing Calibration Data for Hardware

- bundle_id: `systemlink-server`
- source_path: `viewing-calibration.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/viewing-calibration.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: View hardware calibration data to make maintenance decisions about your assets. In the SystemLink web application, click Systems Management Assets . Click Calibrated. You can see a list of your calibrated assets and the data associated with them, including calibration status. Complete the following

### Viewing Calibration Data for Hardware

View hardware calibration data to make maintenance decisions about your assets.

1. In the SystemLink web application, click Systems Management»Assets.
2. Click Calibrated. 
 
 You can see a list of your calibrated assets and the data associated
 with them, including calibration status.
3. Complete the following tasks based on your asset goals. 
 Goal
 What to doAccess the calibration certificate for a specific
 hardware device
 Double-click the device name and click[IMAGE alt='More options icon (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png']Calibration certificate .
 Export the latest calibration entry for your hardware to a comma-separated values
 (CSV) file
 Select the hardware whose information you want to export and click Download»Calibrated assets report.
 Export the entire calibration history for a specific
 hardware device to a CSV file
 Double-click the asset and click [IMAGE alt='More options icon (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png']»Download»Calibration history. Note If
 self-calibration runs multiple times as a server or client restarts,
 SystemLink only records the latest self-calibration from that
 timeframe.
 Ensure readings from your hardware remain accurate over
 time
 Select the hardware to calibrate and click
 Self-Calibrate.

Parent topic:

Managing Your Assets

Related tasks:

- Manually Adding Calibration Data
- Filtering Your Assets

<!--NI_TOPIC bundle=systemlink-server path=viewing-claims-for-openid-connect-users.html language=enus -->
## TOPIC 00203: Viewing Claims for OpenID Connect Users

- bundle_id: `systemlink-server`
- source_path: `viewing-claims-for-openid-connect-users.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/viewing-claims-for-openid-connect-users.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use claims to assign OpenID Connect users to roles and to update their SystemLink username. Log into the server running SystemLink, navigate to C:\Program Files\National Instruments\Shared\Web Server\conf\defines.d\, and open 50_mod_auth_openidc-defines.conf in a text editor. Change the conf

### Viewing Claims for OpenID Connect
 Users

You can use claims to assign OpenID Connect users to roles and to update their SystemLink
 username.

1. Log into the server running SystemLink, navigate to C:\Program
 Files\National Instruments\Shared\Web Server\conf\defines.d\, and
 open 50_mod_auth_openidc-defines.conf in a text
 editor.
2. Change the configuration UnDefine
 AUTH_OIDC_ENABLE_CLAIM_INFO to Define
 AUTH_OIDC_ENABLE_CLAIM_INFO. Your file should look similar to
 the following example. 
 #
# Defined OpenID-Connect configuration for the Windows Apache installation.
#

# The name of the JSON map containing metadata about each identity provider.
Define AUTH_OIDC_ATTRIBUTES_KEY ni-attributes

# CA bundle to use when making requests to an identity provider.
Define AUTH_OIDC_BUNDLE ../nicurl/ca-bundle.crt

# Path to OIDC provider configuration.
Define AUTH_OIDC_PROVIDER_DIR ${HTCONF_PATH}/openidc

# The location to redirect when performing an OpenID-Connect login.
Define AUTH_OIDC_REDIRECT_URI /login/openidc-redirect

#
# User-editable variables.
#

# Whether OIDC is enabled.
Define AUTH_OIDC_ENABLED

# When enabled, /login/openidc-redirect?info=json and
# /login/openidc-redirect?info=html will return the claims for the currently
# logged in user.
Define AUTH_OIDC_ENABLE_CLAIM_INFO
3. If the provider is https and has a certificate signed by a CA that is not
 included in the NI-CURL CA bundle at C:\Program Files\National
 Instruments\Shared\nicurl\ca-bundle.crt, update
 AUTH_OIDC_BUNDLE to point to a CA bundle that contains
 the provider CA. The path can be absolute or relative to C:\Program
 Files\National Instruments\Shared\Web Server.
4. Save the file and restart NI Web Server.
5. Navigate to the following addresses to view user claims. 
 protocol://systemlink-dns/login/openidc-redirect?info=typeWhereprotocol is
 https:// or http://.
 systemlink-dns is the port of the
 SystemLink server. You can omit the port if you are using port 80 or
 443.Note NI
 recommends the DNS name in the redirect URI match the preferred
 hostname set in NI Web Server Configuration on the SystemLink
 server.
 type is either
 html or json.

Parent topic:

Managing Access with OpenID Connect

Related tasks:

- Assigning Users to Roles in a Workspace

<!--NI_TOPIC bundle=systemlink-server path=visualizing-metadata-of-your-test-results.html language=enus -->
## TOPIC 00204: Visualizing Your Test Result Metadata

- bundle_id: `systemlink-server`
- source_path: `visualizing-metadata-of-your-test-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/visualizing-metadata-of-your-test-results.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: View and modify the metadata, such as keywords or properties, associated with your test results so you can interact with data more efficiently. Configure the Test Results Details in the SystemLink web application to display information important to you about your test data. In Test Insights, click T

### Visualizing Your Test Result Metadata

View and modify the metadata, such as keywords or properties, associated with
 your test results so you can interact with data more efficiently.

Test Results
 Details

1. In Test Insights, click Test Results.
2. Double-click a test result to modify the metadata associated with it.
3. In Test Results Details, click [IMAGE alt='image' src='GUID-0BBB5DF7-2F3D-4E09-AF49-E49EF12C2574-a5.png'].
4. In Edit Properties, configure how you want to display
 properties on Test Results Details. 
 Drag a property to a new position.
 Modify an existing property.
 Add or remove a property.Note You cannot remove certain properties,
 such as Product, Serial Number, and Test Program, from Test Result
 Details.
5. Enter new values to user-defined properties.

Parent topic:

Visualizing Data

Related tasks:

- Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-server path=visualizing-parametric-data-of-your-tests.html language=enus -->
## TOPIC 00205: Visualizing the Parametric Data Trends of Your Test Results

- bundle_id: `systemlink-server`
- source_path: `visualizing-parametric-data-of-your-tests.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/visualizing-parametric-data-of-your-tests.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create advanced queries to view test data for your DUTs or test procedures. You can select which product, program, test steps, and properties you want to visualize in a graph to analyze data trends. In the SystemLink web application, click Test Insights. Click Test Results and double-click a test re

### Visualizing the Parametric Data Trends of Your
 Test Results

Create advanced queries to view test data for your DUTs or test procedures.

You can select which product, program, test steps, and
 properties you want to visualize in a graph to analyze data trends.

1. In the SystemLink web application, click Test Insights.
2. Click Test Results and double-click a test result to
 view the test steps associated with it.
3. Under Steps, locate the test step you want to visualize and
 click [IMAGE alt='Trend chart icon (Upward linear trend on a graph).' src='GUID-F06BB647-67EB-4416-A82D-616D368CAD2D-a5.png']. 
 The parametric data viewer launches.
4. Optional: 
 If the data you want to visualize is not preselected,
 click + in Measurements to query the
 data.
  1. Select the product and test program that acquired the test data. Then
 click Next.
  2. Specify the properties and values you want to use to filter test
 results. Then click Next.
  3. Specify the properties and values you want to use to filter test steps.
 Then click Next.
  4. Select the test steps and substeps of which you want to view parametric
 data. Then click Done.
5. Click Toggle elapsed time [IMAGE alt='Clock icon.' src='GUID-43A8A850-C547-4C02-8165-8258FAD5CC5E-a5.png'] to display elapsed time data on the graph.
6. In Inputs, select the inputs to filter the
 measurements.
7. Optional: 
 If you want to change the available inputs, click
 + and enter the input(s) in the filter. When you
 finish adding inputs to the filter, click Done.
8. Click Configure graph [IMAGE alt='Gear icon.' src='GUID-D6237B29-557B-4209-9B43-FAF6DD22B3E8-a5.png'] and configure how you want the graph to display data.
  1. In Grouping, select the step information and inputs you want
 to use to group the data by color.
  2. In Plot Type, select how you want to plot the data
 points.
  3. In X-Axis, choose whether you want to view results based on
 the time they executed or their index values.
  4. Enable Limits to see the range of values that determine the
 pass/fail status of the measurement on the graph.
  5. In Limit Display, select which limit you want to display on
 the graph.
9. In the table, click [IMAGE alt='Gear icon' src='GUID-D6237B29-557B-4209-9B43-FAF6DD22B3E8-a5.png'] to select the metrics to display.
10. Optional: 
 To visualize the metric as a plot on the graph, click the statistic.

Parent topic:

Visualizing Data

Related tasks:

- Analyzing and Interacting with Test Results
- Filtering Test Results

<!--NI_TOPIC bundle=systemlink-server path=visualizing-tag-data-free-form-dashboard.html language=dede -->
## TOPIC 00206: Darstellen von Tag-Daten in einem Dashboard mit freiem Layout

- bundle_id: `systemlink-server`
- source_path: `visualizing-tag-data-free-form-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/dede/visualizing-tag-data-free-form-dashboard.html
- source_language: `dede`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Sie können ein Dashboard mit freiem Layout mit Bedien- und Anzeigeelementen zum Darstellen von Tag- und Systemdaten erstellen, die von Ihren verteilten Systemen erfasst wurden. Dieser Dashboard-Typ ist veraltet. Es wird empfohlen, Kachel-Dashboards anstelle von Dashboards mit freiem Layout zu verwen

### Darstellen von Tag-Daten in einem Dashboard mit freiem Layout

Sie können ein Dashboard mit freiem Layout mit Bedien- und Anzeigeelementen zum Darstellen von Tag- und Systemdaten erstellen, die von Ihren verteilten Systemen erfasst wurden.

Hinweis

1. Klicken Sie in der SystemLink-Webanwendung auf Benutzerdefinierte Anwendungen»Dashboards.
2. Klicken Sie in der Dropdown-Liste auf Neues Freiform-Dashboard. Sie können auch auf Importieren klicken, um nach einem bereits vorhandenen Dashboard zu suchen.
3. Geben Sie einen Namen für das Dashboard ein.
4. Optional: Fügen Sie eine Beschreibung hinzu oder ändern Sie den Arbeitsbereich des Dashboards.
5. Klicken Sie auf OK. Daraufhin öffnet sich der Dashboard-Editor.
6. Wählen Sie oben im Editor die Bildschirmgröße aus, für die Sie Ihr Dashboard optimieren möchten.
7. Ziehen Sie das Bedien- oder Anzeigeelement, das Sie zur Darstellung von Tag-Daten verwenden möchten, auf das Panel. Informationen dazu, welche Datentypen die Bedien- und Anzeigeelemente annehmen können, finden Sie in der Hilfe zur Tag-Formatierung.
8. Binden Sie die Eigenschaften von Eingängen an Tag-Werte. Sie finden alle Tags, die derzeit auf Ihrem Server gespeichert sind, in der Tag-Anzeige (Tags). Verschieben Sie das Tag in das Wertefeld im Konfigurationsbereich oder klicken Sie auf die Box neben dem Werte-Feld und geben Sie den Tag-Namen ein. Der Feldtext wird blau, um anzuzeigen, dass Sie ein Tag auswählen. In der folgenden Abbildung ist ein boolesches Tag dargestellt, das an den Wert eines Auswahlfeld-Elements gebunden ist. [IMAGE alt='image' src='GUID-D5C0F2C5-F008-4AF2-BBF8-854CC07B24B2-a5.png'] Wenn Sie eine Bindung für ein Objektelement wie eine Dropdown-Liste oder Optionsfeldgruppe herstellen, klicken Sie auf Als Tags binden, um den im Element angezeigten String als Tag zu interpretieren, Weitere Informationen zum Festlegen von Werten für diese Art von Bedienelementen finden Sie in der Hilfe zu Objektelementen. Informationen zum Erstellen komplexerer Zuordnungen, wie beispielsweise zwischen den Eigenschaftswerten von Bedien- oder Anzeigeelementen, finden Sie in der Hilfe zur Bindungssyntax.
9. Optional: Um einen hartkodierten Wert festzulegen, löschen Sie den Tag-Wert und klicken Sie auf die Box neben dem Feld, um den Wert einzugeben.
10. Geben Sie im Konfigurationsbereich andere benutzerdefinierte Werte für die Eingaben oder Ausgaben in Ihrem Dashboard ein, wie z. B. Format- und Anzeigeoptionen.
11. Wiederholen Sie die Schritte 7 bis 10 für alle anderen Eingaben oder Ausgaben, die auf Ihrem Dashboard enthalten sein sollen.
12. Klicken Sie auf Speichern und Wiedergabe, um Ihr Dashboard anzuzeigen.
13. Um weitere Änderungen vorzunehmen, klicken Sie auf [IMAGE alt='image' src='GUID-0BBB5DF7-2F3D-4E09-AF49-E49EF12C2574-a5.png']»Bearbeiten.

Übergeordnetes Thema:

Darstellen von Daten

Zugehörige Tasks:

- Überwachen von Daten mit Hilfe von Tags
- Angeben von Werten für Objektelemente

Zugehörige Verweise:

- Bindungs-Syntax
- Datentypen zur Darstellung von Tag-Daten

<!--NI_TOPIC bundle=systemlink-server path=visualizing-tag-data-tile-dashboard.html language=enus -->
## TOPIC 00207: Visualizing Data on a Tile Dashboard

- bundle_id: `systemlink-server`
- source_path: `visualizing-tag-data-tile-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/visualizing-tag-data-tile-dashboard.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a dashboard comprised of tiles to visualize tag, test, system, or asset data your distributed systems generate. Make sure you have sufficient privileges to view, create, or modify dashboards and use tags in the workspace(s) where you want to visualize data on a dashboard. You also need suffic

### Visualizing Data on a Tile Dashboard

Create a dashboard comprised of tiles to visualize tag, test, system, or asset data
 your distributed systems generate.

Make sure you have sufficient privileges to view, create, or
 modify dashboards and use tags in the workspace(s) where you want to visualize data on a
 dashboard. You also need sufficient privileges for the data you want to
 display.

1. In the SystemLink web application, click Custom Applications»Dashboards.
2. Click New Tile Dashboard. 
 To browse for an existing dashboard, click the dropdown arrow and select
 Import.
3. Enter a name and a description for the dashboard.
4. Select the workspace to which you want to add the dashboard. 
 Note You can change your selection later
 by clicking [IMAGE alt='Gear icon' src='GUID-F365AA0A-76E7-445B-BF21-BD366FEDA5D4-a5.png']Settings.
5. Click New Tile and select the tile type
 you want to use to visualize data.
6. On the Data tab, select the type of data source you want
 to display on the tile. 
 For example, if you want to display data from a Jupyter notebook on a graph tile,
 click [IMAGE alt='image' src='GUID-A620AA96-45C5-4191-A7FE-99176ACCC8F8-a5.png']Tag path»[IMAGE alt='Notebooks icon.' src='GUID-11447B4A-1BE3-4F56-8A1A-894358751151-a5.png'] Notebooks.
7. Specify the data source you want to display on the tile.
8. If you want to display additional data on the tile, click
 + and repeat steps 6-7 as many times as you
 need. 
 Note Donut and graph tiles are
 the only tile types to which you can add multiple data sources. The
 additional data sources must be the same type of data source. Therefore, if
 you add a tag to a graph tile, you can only add other tags to the
 tile.
9. On the Properties tab, configure how you want the tile
 to look. 
 For example, you can disable the Units toggle if you do not want
 to display the unit property on the tile. 
 Refer to *Adding Properties to a Data
 Source to Display on a Dashboard Tile* in this manual to learn
 more about the properties you can automatically display on a
 tile.
10. Repeat steps 5-9 to add more tiles to the dashboard.
11. At the top of the editor, click [IMAGE alt='Laptop icon.' src='GUID-0FFD90CF-A6CA-4902-9D68-C9F064356CAB-a5.png'] Panel Size and select the type of device on which you want to
 monitor the dashboard.
12. Disable the Edit toggle to view your dashboard. 
 Note The dashboard editor
 automatically saves your dashboard whenever you make a change.
13. To make more changes, enable the Edit toggle.
14. Click the [IMAGE alt='More options icon (three vertical dots).' src='GUID-219456BE-BCA1-4C72-9096-3E2C8A5929FF-a5.png'] More button to export, duplicate, or delete your dashboard.

Parent topic:

Visualizing Data

Related tasks:

- Selecting a Tile Type
- Selecting a Data Source for a Tile

Related reference:

- SystemLink Predefined Properties

<!--NI_TOPIC bundle=systemlink-server path=visualizing-tag-data.html language=enus -->
## TOPIC 00208: Visualizing Data

- bundle_id: `systemlink-server`
- source_path: `visualizing-tag-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/visualizing-tag-data.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Display important data about your distributed systems.

### Visualizing Data

Display important data about your distributed systems.

- [Visualizing Data on a Tile Dashboard](visualizing-tag-data-tile-dashboard.html) Create a dashboard comprised of tiles to visualize tag, test, system, or asset data your distributed systems generate.
- [Visualizing Test Data on a Dashboard](visualizing-test-results-on-dashboard.html) Create a dashboard to visualize test results from the Test Monitor API or TestStand.
- [Visualizing TDMS Data](visualizing-tdms-data.html) Display measurement data in a TDMS file ( .tdms ) on a chart to visualize results and trends.
- [Visualizing Your Test Result Metadata](visualizing-metadata-of-your-test-results.html) View and modify the metadata, such as keywords or properties, associated with your test results so you can interact with data more efficiently.
- [Visualizing Product Information Associated with Test Results](visualizing-test-results-by-product.html) Analyze product information about your tests to determine the quality metrics of the devices under test (DUT).
- [Visualizing the Parametric Data Trends of Your Test Results](visualizing-parametric-data-of-your-tests.html) Create advanced queries to view test data for your DUTs or test procedures.

Related tasks:

- Hosting a WebVI in SystemLink
- Visualizing Metadata of a System
- Monitoring and Visualizing Data with Tags

Related reference:

- SystemLink Predefined Properties

<!--NI_TOPIC bundle=systemlink-server path=visualizing-tdms-data.html language=enus -->
## TOPIC 00209: Visualizing TDMS Data

- bundle_id: `systemlink-server`
- source_path: `visualizing-tdms-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/visualizing-tdms-data.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Display measurement data in a TDMS file (.tdms) on a chart to visualize results and trends. Before you visualize your measurement data, upload TDMS files to the server with the File API or in the File Viewer. In the SystemLink web application, click File Viewer. Select the TDMS file with the measure

### Visualizing TDMS Data

Display measurement data in a TDMS file (.tdms) on a chart to
 visualize results and trends.

Before you visualize your measurement
 data, upload TDMS files to the server with the File API or in the File Viewer.

1. In the SystemLink web application, click File Viewer.
2. Select the TDMS file with the measurement data you want to visualize and click
 Preview.
3. In Explore, select the file. 
 The graph displays the measurement data from the file.
4. Use the tasks in the following table to visualize your data in different ways. 
 Goal
 TaskVisualize specific channel data on the graph
 In Explore, select the TDMS file and expand the tree
 to the channels.[IMAGE alt='image' src='GUID-0E9A78DD-E83D-4291-9BE8-EDD2C8BA5842-a5.png']
 Enable or disable the channel(s).Note You can highlight a channel without
 disabling other channels.
 Visualize specific channel data in a table
 In Explore, select the TDMS file and expand the tree
 to the channels.[IMAGE alt='image' src='GUID-0E9A78DD-E83D-4291-9BE8-EDD2C8BA5842-a5.png']
 Click the channel(s) you want to visualize.
 Expand Channel Data to view the data in the
 table.
 
[IMAGE alt='image' src='GUID-CAC5E3B7-01BE-42FE-A123-B00090529222-a5.png']
 Visualize the properties of the TDMS file, group, or channel(s)
 In Explore, click either the TDMS file, group, or
 channel name.
 In Properties, expand or collapse sections to
 visualize property information.
 Visualize specific channel measurements on a graph
 On the toolbar, click Filter [IMAGE alt='image' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'].
 In the drop-down, select a channel and click
 +.
 Create a filter to display the measurements on the graph. Use one of the
 following methods to filter the measurements:Define specific measurement criteria for the filter to display on the
 graph. For example, if you want to display results greater than or equal
 to 24.914 degrees Celsius, enter X >= 24.914.Select the measurements you want to display on the graph.
 Repeat step c to add more channel data to the filter.
5. Save the measurement data on your local machine.
  1. Click File Details.
  2. Click Download.

Parent topic:

Visualizing Data

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-server path=visualizing-test-results-by-product.html language=enus -->
## TOPIC 00210: Visualizing Product Information Associated with Test Results

- bundle_id: `systemlink-server`
- source_path: `visualizing-test-results-by-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/visualizing-test-results-by-product.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Analyze product information about your tests to determine the quality metrics of the devices under test (DUT). In the SystemLink web application, click Test Insights. Click Products to view the pass rates and results associated with each product or product family. Filter the products to review test

### Visualizing Product Information Associated
 with Test Results

Analyze product information about your tests to determine the quality metrics of the
 devices under test (DUT).

1. In the SystemLink web application, click Test Insights.
2. Click Products to view the pass rates and results
 associated with each product or product family.
3. Optional: 
 Filter the products to review test data about a specific product or product
 family.
  1. For Group
 by, choose how you want to organize this
 information.
  2. For Query by, choose the metadata, such as
 keyword or family, that you want the results to match.
4. To access the query on a recurring basis, click
 Save Query. 
 The query appears under Products on the sidebar.
5. Double-click a product to view test metadata associated with it. 
 Note Refer to *Visualizing Your Test Result Metadata* to learn more
 about displaying test metadata associated with your products.
6. Analyze and visualize test data associated with a product in any of the
 following ways:
  - Click Reports to create and view graphical
 reports associated with a product.
  - Click Test Results to review test results
 associated with a product.
  - Click Attachments to view files associated with a
 product, such as images of the DUT, schematics, instructions, and
 more.

Parent topic:

Visualizing Data

Related tasks:

- Analyzing and Interacting with Test Results
- Filtering Test Results
- Visualizing Your Test Result Metadata

<!--NI_TOPIC bundle=systemlink-server path=visualizing-test-results-on-dashboard.html language=enus -->
## TOPIC 00211: Visualizing Test Data on a Dashboard

- bundle_id: `systemlink-server`
- source_path: `visualizing-test-results-on-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/visualizing-test-results-on-dashboard.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a dashboard to visualize test results from the Test Monitor API or TestStand. Test Monitor installs a default dashboard to help you visualize test data immediately. Edit the default dashboard or create a new one to visualize test data that is important to you. In the SystemLink web applicatio

### Visualizing Test Data on a Dashboard

Create a dashboard to visualize test results from the Test Monitor API or
 TestStand. Test Monitor installs a default dashboard to help you visualize
 test data immediately. Edit the default dashboard or create a new one to visualize test data
 that is important to you.

1. In the SystemLink web application, click Test Insights.
2. On the sidebar, hover over Dashboard and click
 +. 
 Note If you want to use an
 existing dashboard as a template for a new dashboard, click Options [IMAGE alt='image' src='GUID-219535F2-9376-4130-AF9C-F2765FE760BB-a5.png']»Duplicate. Complete the prompts and proceed to step 5.
3. For Source, select how you want
 to generate the dashboard. Refer to the following table to choose the dashboard
 you want to generate. 
 Source option
 DescriptionCreate new dashboard
 Build a dashboard from scratch.
 Add existing dashboard
 Access a dashboard in Test Insights under Dashboards.
 Import dashboard file
 Upload a dashboard from another server as an
 .fpg file.
4. Depending on what you selected for the Source,
 complete one of the following tasks: 
 
 The dashboard editor opens. The dashboard also appears under
 Dashboard on the sidebar.
  - Enter a name for the dashboard and click OK.
  - Select the dashboard you want to access in
 Test Insights and click OK .
5. At the top of the editor, click [IMAGE alt='image' src='GUID-0FFD90CF-A6CA-4902-9D68-C9F064356CAB-a5.png'] Panel Size and select
 the type of device on which you want to monitor the dashboard.
6. Considering your goals and the type of dashboard you generated, customize the
 dashboard in any of the following ways. 
 Note Refer to *Visualizing Data on a
 Tile Dashboard* and *SystemLink Predefined Properties* in this manual
 for more information about creating a dashboard.
  - Click New Tile and select the tile type you want to use to
 visualize data.
  - Select a tile on the dashboard and
 modify its data sources or properties.
  - Move a tile to another
 position on the panel.
  - Select an existing tile and
 delete it.
7. Disable the Edit toggle to view your dashboard. 
 Note The dashboard editor
 automatically saves your dashboard whenever you make a change.
8. To make more changes, enable the Edit toggle.
9. Optional: 
 To make this dashboard the default dashboard in Test
 Insights, hover over it in the sidebar and click [IMAGE alt='image' src='GUID-131F32C8-0632-4E1A-B2ED-3DAF35A42B15-a5.png']»Set as default.

#### Test Insights Dashboards

Find more dashboards you can use in Test Insights on GitHub.

Parent topic:

Visualizing Data

Related tasks:

- Analyzing and Interacting with Test Results
- Visualizing Data on a Tile Dashboard
- Selecting a Tile Type
- Selecting a Data Source for a Tile

Related reference:

- SystemLink Predefined Properties

Related information:

- SystemLink Server Examples

<!--NI_TOPIC bundle=systemlink-server path=working-with-search-results.html language=enus -->
## TOPIC 00212: Working with Search Results

- bundle_id: `systemlink-server`
- source_path: `working-with-search-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-server/raw/resource/enus/working-with-search-results.html
- source_language: `enus`
- document_id: `systemlink-server`
- page_type: `leaf`
- content_type: `task`
- source_description: After completing a search, inspect, export, or make the search results available for data analysis. The following table highlights tasks you perform with your search results.GoalTaskDisplay properties.Select a file, group, or channel found in the search and click Properties Display on the right side

### Working with Search Results

After completing a search, inspect, export, or make the search results available for data
 analysis.

| Goal | Task |
| --- | --- |
| Display properties. | Select a file, group, or channel found in the search and click Properties Display on the right side of the window. The Properties Display window lists all standard and custom properties. Non-optimized custom properties are highlighted in gray. |
| Display channel data in a chart. | Open the Channel Preview. Move the cursor to view individual channel values. |
| Export files to zip files. | Click » Export File (Original Format) or » Export File As . You can export the files in every format for which you have registered a writing DataPlugin. |
| Copy your search results to Data Analysis. | Click » Add to Data Cart to copy the selected files to the clipboard. Access the files in Data Analysis. |

Parent topic:

Retrieving Data from Your Data Stores
