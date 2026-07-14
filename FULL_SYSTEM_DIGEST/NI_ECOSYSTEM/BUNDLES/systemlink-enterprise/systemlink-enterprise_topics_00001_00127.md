# NI DOCUMENT BUNDLE: systemlink-enterprise

<!--NI_BUNDLE_CHUNK bundle=systemlink-enterprise start=1 end=127 -->
<!--NI_TOPIC bundle=systemlink-enterprise path=access-control-glossary.html language=enus -->
## TOPIC 00001: Role-Based Access Control Concepts

- bundle_id: `systemlink-enterprise`
- source_path: `access-control-glossary.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/access-control-glossary.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Understand workspaces, roles, and privileges in SystemLink Enterprise. Automatic data encapsulation The process of data being stored in the same workspace as the system that produces it. Along with defining roles and privileges, this process helps keep data organized and ensures users only see the d

### Role-Based Access Control Concepts

Understand workspaces, roles, and privileges in SystemLink Enterprise.

Automatic data encapsulation

Workspace

SystemLink Enterprise

Default workspace

Role

User

SystemLink Enterprise

Privilege

SystemLink Enterprise

Mapping

Parent topic:

Assigning Users to Roles in a Workspace

<!--NI_TOPIC bundle=systemlink-enterprise path=acquiring-test-results.html language=enus -->
## TOPIC 00002: Acquiring Test Results

- bundle_id: `systemlink-enterprise`
- source_path: `acquiring-test-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/acquiring-test-results.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create test steps to record your test and measurement data. What to Use You can find the SystemLink Test Monitor and Configuration APIs on the Data Communication palette in LabVIEW 2018 or later.The SystemLink Configuration API is available in LabVIEW 2016 or later. What to Do On the client, create

### Acquiring Test Results

Create test steps to record your test and measurement data.

#### What to Use

Data
 Communication

Note

#### What to Do

- Create test results and steps.
- Run a test sequence.
- Structure your data to render it correctly in the Test Monitor UI.
- Acquire results.

Add the code in the following images to the diagram. Customize the gray sections for your
 unique programming goals.

Figure 1.

[IMAGE alt='LabVIEW diagram that opens SystemLink configuration and creates a test result and test step.' src='GUID-217D45F1-3701-4D4D-8E05-A03D5794C38C-a5.png']

Figure 2.

[IMAGE alt='LabVIEW diagram that generates named values and creates a SystemLink test step.' src='GUID-0C75DBDF-8138-4D5E-843F-B532145ECF08-a5.png']

Figure 3.

[IMAGE alt='LabVIEW block diagram updating a SystemLink test step and test result with collected named values.' src='GUID-2B7813F3-030B-436E-A0A5-1A40F95BFF6F-a5.png']

1. Open Configuration initiates a connection to SystemLink.
2. Initialize Test Result configures a local reference of the new test
 result on the client test system. Note The local reference does not exist in SystemLink until you wire this VI to
 Create Test Result.
3. The Property Node sets properties to the test result. You can see
 these properties in the Test Monitor UI.
4. Create Test Result adds the local test result reference with the
 properties you set to SystemLink.
5. Initialize Test Step From Result configures and associates a local
 reference of a test step to the test result you created. Note You must add the test result to
 SystemLink before you can associate any test steps with it. Therefore, call this VI
 after you call Create Test Result. The VI creates only a local
 reference to the test step. You must call Create Test Step after
 this VI to add it to SystemLink.
6. Generate Named Value converts the data you want to add to the test
 step as a named value object. Wire Build Array 
 to the named value this VI generates to format the test data.
7. The Property Node sets the inputs for the test step using the
 named values the Build Array returns.
8. Create Test Step adds the local test step reference with the
 properties you set to SystemLink. You can run a test VI after Create Test
 Step . Note In a more
 advanced test sequence, you might determine a standard VI prototype and load test VIs
 from a directory on disk.
9. Build a cluster structure for the TestStand data model so data displays correctly in
 the Test Monitor UI. Refer to Structuring Your Test Data to create the subVI you need to
 display your data correctly in Test Monitor.
10. Generate Named Value converts the test data into outputs. Wire
 Build Array to the named value this VI
 generates to format the test data.
11. The Property Node reads the outputs and data for the test step.
 Note You must set the Data Model as
 TestStand for your data to display correctly in the Test
 Monitor UI.
12. Update Test Step modifies the test step with the properties and
 data set by the Property Node .
13. Update Test Result sets the result status based on the result of
 the test step. You can see the results in the Test Monitor UI.

#### Troubleshooting

| Scenario | Resolution |
| --- | --- |
| Your test data does not display correctly in the Test Monitor UI. | Verify if your cluster structure for the TestStand Data Model object is correct. Refer to Structuring Your Test Data for more information. |

Parent topic:

Connecting to Clients

Related tasks:

- Structuring Your Test Data

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=add-dynamic-qr.html language=enus -->
## TOPIC 00003: Adding Dynamic QR Codes to a Dashboard

- bundle_id: `systemlink-enterprise`
- source_path: `add-dynamic-qr.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/add-dynamic-qr.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create dashboards that generate quick-response (QR) codes for various systems or assets. These dashboards allow users to select a system or asset to display a QR code. This action also displays other available information about the chosen system or asset. The following QR code generation methods are

### Adding Dynamic QR Codes to a Dashboard

Create dashboards that generate quick-response (QR) codes for various systems or
 assets.

These dashboards allow users to select a system or asset to display a QR
 code. This action also displays other available information about
 the chosen system or asset.

The following QR code generation methods are available.

- Display QR codes that users can select from a drop-down
 menu.
- Create interactive tables for users to select a scan code that
 update the QR code visualization.
- Generate QR codes for multiple systems or assets
 simultaneously.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Click New to create a new
 dashboard.
3. On the Dashboard page,
 click Dashboard
 Settings ([IMAGE alt='Gear icon.' src='GUID-D6237B29-557B-4209-9B43-FAF6DD22B3E8-a5.png']).
4. Create a QR query variable for your systems or assets.
  1. Navigate to the Variables tab and click Add variable.
  2. Set the Select
 variable type to Query.
  3. Name the variable.
  4. In the Data
 source drop-down, select SystemLink Systems or
 SystemLink
 Assets.
  5. Set the Return
 type to Scan
 code.
  6. Enable Multi-value to allow multiple
 selections.
  7. Click Apply to save the variable.
5. Click Save
 dashboard.
6. Add the QR query variable to the dashboard.
  1. On the Dashboard page, click Add»Visualization.
  2. Click Change
 visualization and select QR code visualization
 from the drop-down.
  3. In the right panel, select Repeat options.
  4. Select your QR query variable.
  5. In the Value field, enter
 $ and the name of your QR
 query variable. 
 Note For example, if
 you named your variable
 systemsScanCode, enter the
 Value as
 $systemsScanCode.
  6. Click Apply.
7. Optional: 
 Create a table visualization for your systems or assets. 
 Note If you only want drop-down
 selector for your QR code, you can skip this
 step.
  1. On the Dashboard page, click Add»Visualization.
  2. Click Change
 visualization and select Table visualization
 from the drop-down.
  3. In the Data
 source drop-down, select SystemLink Systems or
 SystemLink
 Assets for your query variable.
  4. Based on your data source, select the
 appropriate property. 
 Data Source
 PropertySystemLink Systems
 In the Query editor, set the Query Type to
 Properties.SystemLink Assets
 Click the Properties drop-down and select the
 Scan Code
 property.
  5. In the Data
 links section, click Add link.
  6. Enter a link Title to represent the name of the
 URL.
  7. Enter a link URL that uses the following
 format. 
 d/<YOUR_DASHBOARD_UID>/<YOUR_DASHBOARD_NAME>?orgId=1&var-<selectedScanCode>=${__data.fields["scan
 code"]}The
 <YOUR_DASHBOARD_UID>
 variable represents the dashboard UID. To locate
 the dashboard UID, refer to the dashboard URL. For
 example, if the dashboard URL is
 https://system-server/dashboards/d/bf43k48qlijgga/dashboard,
 then the dashboard UID is
 bf43k48qlijgga.
 The
 <YOUR_DASHBOARD_NAME>
 variable represents the dashboard name. NI
 recommends that the dashboard name is URL
 friendly.
 The <selectedScanCode>
 variable represents the query variable name.
  8. Disable Open in new
 tab to ensure that the dashboard
 updates in place.
  9. Click Save.
  10. Click Apply.
8. Click Save
 dashboard.

Once dynamic QR code generation is set up, you can test the QR code
 generator on your dashboard.

| QR Code Generation Method | How to Test |
| --- | --- |
| QR codes with a drop-down selector for a single system or asset. | On the Dashboard page, in the Variable drop-down, choose a system or asset. Observe that a unique QR code generates for the chosen system or asset. |
| QR codes with a drop-down selector for multiple systems or assets. | On the Dashboard page, in the Variable drop-down, choose multiple systems or assets. Observe that a unique QR code generates for each chosen system or asset. |
| QR codes with a table selector. | In the table, click a scan code value. Observe that a unique QR code generates for the chosen scan code value. |

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-enterprise path=add-locations.html language=enus -->
## TOPIC 00004: Adding and Editing Locations

- bundle_id: `systemlink-enterprise`
- source_path: `add-locations.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/add-locations.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create locations to track assets and systems from SystemLink. Refer to the following table for the steps that best suit your use case. Add a new location Navigate to Systems Management Locations . Click Add Location. Add a location under an existing location Navigate to Systems Management Locations

### Adding and Editing Locations

Create locations to track assets and systems from SystemLink.

1. Refer to the following table for the steps that best suit your use case. 
 OptionDescriptionAdd a new location
 Navigate to Systems Management»Locations.
 Click Add Location.Add a location under an existing location
 Navigate to Systems Management»Locations.
 Select an existing location and click Add
 location.Note This method assigns your selected
 location as the parent of the new location.Edit an existing location
 Navigate to Systems Management»Assets or Systems Management»Systems.
 Select a system or asset.
 Click Edit.
2. In the slide-out, click Info to modify the following
 information about the location. 
 Name—Assigns a real-world name to the location.
 Location State—Enables or disables the acceptance of assets or systems
 for assignment.
 Type—Creates or assigns string values to the location.
 Parent—Sets the hierarchal relationship of the location in relation to
 other locations.
 Workspace—Determines which users can view the location.
3. Click Properties to modify the properties of the
 location.
4. Click QR Code to assign a QR code value to a
 location. 
 Use QR codes to assign assets and systems to a location through the
 Move function.
5. Click Save.

Parent topic:

Managing Your Locations

<!--NI_TOPIC bundle=systemlink-enterprise path=adding-assets.html language=enus -->
## TOPIC 00005: Adding Assets

- bundle_id: `systemlink-enterprise`
- source_path: `adding-assets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/adding-assets.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Add NI assets and third-party assets to SystemLink so you can manage them from the web application. Refer to the following table to find the steps that best suit your use case. Automatically add NI assets. Connect the asset to a connected SystemLink Client system. Install the appropriate drivers for

### Adding Assets

Add NI assets and third-party assets to SystemLink so you can manage them from the web
 application.

Refer to the following table to find the steps that best suit your use case.

| Option | Description |
| --- | --- |
| Automatically add NI assets. | Connect the asset to a connected SystemLink Client system. Install the appropriate drivers for the asset. SystemLink automatically adds the asset and tracks the location of the asset when you move it to another managed system. |
| Automatically add third-party assets. | Connect the asset to a managed system. Install the appropriate drivers for the asset. Install NI VISA. SystemLink automatically adds the asset and tracks the location of the asset when you move it to another managed system.Note SystemLink can only automatically track third-party assets that are SCPI compliant and respond to a *IDN? command in the format manufacturer,model,serial number,firmware. manufacturer, model, and serial number are required and cannot be empty. For devices that are not Plug and Play, you must click Scan for Instruments in NI MAX before SystemLink can detect your device. This ensures that the resulting *IDN? request does not interrupt any test operations without direct user intervention. |
| Manually add assets. | In the SystemLink web application, click System Management » Systems and double-click the system you want to add an asset to. On the Assets tab, click Add asset. Enter a unique name and other identifying information for the asset.Note Ensure that you enter the correct vendor, model, and serial number when adding the asset. This information makes the asset easier to identify when the asset is connected to a system. Having distinguishing information is also useful if you are adding an unused NI device to an unmanaged location for the first time. For Location, select a system from the drop-down or enter the name of a physical location. Enable Supports external calibration to configure and to manage calibration for this asset manually. Specify the appropriate properties and keywords for any queries you want the asset to appear in. Click OK. |

Parent topic:

Managing Your Assets

<!--NI_TOPIC bundle=systemlink-enterprise path=adding-custom-fields-to-the-ui.html language=enus -->
## TOPIC 00006: Adding Custom Input Fields to the User Interface

- bundle_id: `systemlink-enterprise`
- source_path: `adding-custom-fields-to-the-ui.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/adding-custom-fields-to-the-ui.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use dynamic form fields to add custom input fields to the configuration slide-out for a resource. Introduced in January 2025 Form fields are custom input fields that you can add to the SystemLink Enterprise UI. Dynamic form fields (DFFs) allow you to create custom input fields that can adapt accordi

### Adding Custom Input Fields to the User
 Interface

Use dynamic form fields to add custom input fields to the configuration slide-out
 for a resource.

Introduced in January 2025

Form fields

SystemLink Enterprise

Dynamic form
 fields

DFFs let you collect additional
 information about a resource by providing additional input fields the user.

- Assets
- Products
- Systems
- Work Items
- Work Orders

*Display rules* allow you to control when a field is visible
 to the user. For example, you can specify that a field is visible only when the
 vendor for the asset is NI.

Complete the following steps to define and to
 implement your DFFs in a configuration.

1. Configuring Dynamic Form Fields Use the example Dynamic Form Fields Configuration and the Dynamic Form Fields (DFFs) API to as a starting point for your custom configuration.
2. Customizing a Dynamic Form Field Configuration Modify the example Dynamic Form Fields Configuration to create a custom dynamic form fields (DFFs) configuration.

Related concepts:

- SystemLink Enterprise Examples

<!--NI_TOPIC bundle=systemlink-enterprise path=adding-specifications-to-product.html language=enus -->
## TOPIC 00007: Adding Product Specifications through Jupyter Notebook and the SCM API

- bundle_id: `systemlink-enterprise`
- source_path: `adding-specifications-to-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/adding-specifications-to-product.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add specifications for a product with Jupyter Notebook or by using the Specification Compliance Module (SCM) API. Adding Specifications with Jupyter Notebook Upload a file that contains specification information for a product Use Jupyter Notebook to extract the information into the SCM. Cont

### Adding Product Specifications through Jupyter
 Notebook and the SCM API

You can add specifications for a product with Jupyter Notebook or by using the
 Specification Compliance Module (SCM) API.

#### Adding Specifications with Jupyter Notebook

1. Upload a file that contains specification information for a
 product
2. Use Jupyter Notebook to extract the information into the
 SCM.

Note

#### Adding Specifications with the SCM API

1. Configure web access to SystemLink Enterprise .
2. Use the following URL to access the SCM API reference: https://<apihostname>/niapis/?urls.primaryName=Specification%20Management

Note

<apihostname>

global.apiHosts

systemlink-values

Parent topic:

Specification Compliance

<!--NI_TOPIC bundle=systemlink-enterprise path=adding-users.html language=enus -->
## TOPIC 00008: Adding Users to a Workspace

- bundle_id: `systemlink-enterprise`
- source_path: `adding-users.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/adding-users.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: As a workspace owner, add users to workspaces and specify roles without knowing the identity provider (IdP) configuration. This increases flexibility when managing workspace membership and roles. To add users to a workspace, ensure each user has successfully logged in to the SystemLink web applicati

### Adding Users to a Workspace

As a workspace owner, add users to workspaces and specify roles without knowing the
 identity provider (IdP) configuration. This increases flexibility when managing workspace
 membership and roles.

To add users to a workspace, ensure each
 user has successfully logged in to the SystemLink web application at least once.

1. In the SystemLink web application, click Access Control»Workspaces.
2. Click the workspace you want to add a user to.
3. Click Members. 
 This tab shows members who have logged in to SystemLink and are not part of an IdP
 role mapping.
4. Click +MEMBERS to add a new member to this workspace.
5. Enter the name or email of the user you want to add to the workspace.
6. Select the user that matches your query from the list and click
 Add.
7. Use the role drop-down menus to select the appropriate roles for the user.
8. Click Update.

The user you added will receive an email inviting them to
 the workspace.

Parent topic:

Managing Access to SystemLink Enterprise

Related tasks:

- Creating a Workspace

<!--NI_TOPIC bundle=systemlink-enterprise path=alarms-data-source.html language=enus -->
## TOPIC 00009: Adding the Alarms Data Source to a Dashboard

- bundle_id: `systemlink-enterprise`
- source_path: `alarms-data-source.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/alarms-data-source.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create dashboards using the Alarms data source. In SystemLink Enterprise, navigate to Overview Dashboards . Click New dashboard icon New dashboard . Click Add a new panel. In the Query tab, set the Data source to SystemLink Alarms. Set the Query Type to List Alarms. Select an Output Type to view the

### Adding the Alarms Data Source to a
 Dashboard

Create dashboards using the Alarms data source.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Click [IMAGE alt='New dashboard icon' src='GUID-69B726A6-D4C1-451C-882A-5ED0B10972FD-a5.png']»New dashboard.
3. Click Add a new
 panel.
4. In the Query tab, set the
 Data source to
 SystemLink
 Alarms.
5. Set the Query Type to
 List
 Alarms.
6. Select an Output Type to
 view the appropriate results. 
 Output Type
 DescriptionProperties
 View the properties of the
 alarms.Total
 Count
 View a numeric count of the
 alarms.
7. Set the Output to
 Properties.
8. In the Properties
 drop-down, select the properties to display.
9. Optional: 
 In the Query Builder, add
 filters to narrow the query results.
10. Enter a Take value to
 specify the maximum number of results that the query should
 return.
11. Click Save.
12. Update the Query Type to
 change the query results. 
 Query Type
 DescriptionAlarms
 Trend
 View a timeline of alarms. You can also
 group the alarms by severity.List
 Alarms
 View the properties or a numeric count of
 the alarms.

The following are examples of queries you can create using the alarm data
 source:

- List all products under a family. This list also includes the
 properties of those products.
- List all products by various query conditions. You can then use
 data transformation to display a count of filtered
 products.

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-enterprise path=alarms-overview-dashboard.html language=enus -->
## TOPIC 00010: Using the Alarms Overview Dashboard

- bundle_id: `systemlink-enterprise`
- source_path: `alarms-overview-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/alarms-overview-dashboard.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: The Alarms Overview Dashboard provides an out-of-the-box view of active alarms across your workspaces in SystemLink Enterprise. Use this dashboard to complete the following actions. Monitor the overall alarm state of your workspace at a glance. Prioritize issues by severity. Track alarm trends to id

### Using the Alarms Overview Dashboard

The Alarms Overview Dashboard provides an out-of-the-box view of active alarms
 across your workspaces in SystemLink Enterprise.

Use this dashboard to complete the following actions.

- Monitor the overall alarm state of your workspace at a
 glance.
- Prioritize issues by severity.
- Track alarm trends to identify systemic problems.
- Identify the systems that need immediate attention.
- Drill down into individual alarms or systems for further
 investigation.

1. In SystemLink Enterprise, open the
 Alarms Overview Dashboard by
 clicking Alarms Overview on the
 Alarms page toolbar.
2. Use filters to scope the dashboard to your area of
 responsibility. 
 Filters
 DescriptionWorkspace
 Filters alarms by workspace.
 Select a workspace to focus on the systems and
 alarms in that workspace.
 Select All to view
 alarms across all accessible workspaces.
3. Use the Health dashboards menu in the
 top-right corner to navigate to other health-related
 dashboards. 
 For instance, you can navigate to the System Health
 dashboard.
4. Review the alarm summary to assess the severity distribution
 across your workspace. 
 Dashboard Panel
 DescriptionActive alarms |
 Summary
 Displays the count of active alarms grouped by
 severity level.
 Click a severity tile to filter the
 Active alarms table to
 display only alarms of that severity.
5. Investigate individual alarms in the active alarms table. 
 Dashboard Panel
 DescriptionActive alarms |
 All
 Displays a table of active workspace
 alarms.
 The table includes the following columns.
 Alarm—The alarm name.
 Click this column to open the alarm details and
 take action.
 System—The system
 origin of the alarm. Click to navigate to the
 system details page.
 First occurrence—When
 the alarm was first triggered.
 Acknowledged by—The
 user who acknowledged the alarm.
 Acknowledged on—The
 date and time that the system marked the alarm as
 acknowledged.
 Workspace—The workspace
 for the alarm.
 Severity—The current
 severity level of the alarm.
 Click a summary tile to filter this table by
 the corresponding severity. Use the column filters
 to search for specific systems or certain
 alarms.
6. Review alarm trends and identify systems that need your
 attention. 
 Dashboard Panel
 DescriptionAlarm Timeline
 Displays a time-series graph illustrating the
 trend of active alarms over the selected time
 range.
 Use this chart to complete the following
 actions.
 Spot spikes in alarm activity.
 Identify recurring patterns.
 Confirm that corrective actions have reduced
 alarm volume.
 Systems under alarm
 Displays a table of systems with active alarms
 in the selected workspace. Use this table to
 quickly identify the systems with the most issues.
 The table includes the following columns:
 Name—The system name.
 Click the name to view the system details.
 Most recent alarm—The
 latest alarm on that system. Click this column to
 view the alarm details.
 Total active alarms—The
 number of active alarms on the system. Systems
 with a high count may need priority
 investigation.
 Workspace—The workspace
 for the system.
7. Hover over charts to obtain details on individual data
 points.
8. Use the time range picker to adjust the time range for all
 panels. The default time range is Last 7
 days.
9. Apply column filters in tables to refine the displayed
 results.
10. Export the table data.
  1. On a dashboard panel, click the ellipsis
 ([IMAGE alt='Ellipsis (more options) menu icon on a dashboard panel.' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png']).
  2. Click Inspect»Data.
  3. Click Download
 CSV.

Parent topic:

Monitoring Tests

Related tasks:

- Using the System Health Dashboard
- Viewing Out of the Box (OOTB) Dashboards in SystemLink Enterprise

<!--NI_TOPIC bundle=systemlink-enterprise path=analyzing-files-with-jupyter-notebooks.html language=enus -->
## TOPIC 00011: Analyzing Files with Jupyter Notebook

- bundle_id: `systemlink-enterprise`
- source_path: `analyzing-files-with-jupyter-notebooks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/analyzing-files-with-jupyter-notebooks.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Process data in files using Jupyter Notebook to generate high-level insights about your data. Refer to the SystemLink Enterprise examples on GitHub for an example notebook. Navigate to Product Insights Files . Select one or more files, expand the Analyze drop-down, and select Analyze. You can analyz

### Analyzing Files with Jupyter Notebook

Process data in files using Jupyter Notebook to generate high-level insights about your
 data.

SystemLink Enterprise

1. Navigate to Product Insights»Files.
2. Select one or more files, expand the Analyze drop-down,
 and select Analyze. 
 Note You can analyze up to 50 files at a time.
3. In the Analyze files slide-out, select the notebook you
 want to run on your files. 
 Note If you do not see the
 notebook you are looking for, ensure that you published the notebook to a
 workspace you can access.
4. Click Analyze. 
 The Executions grid opens and shows the notebook
 execution you initiated. Note SystemLink Enterprise preserves up to 16 MB of
 notebook execution data for 7 days. To retain more data for longer, ensure
 that your notebook saves and uploads your data to SystemLink.

Parent topic:

Reporting Data with Jupyter Notebooks

Related tasks:

- Visualizing Notebook Data on a Dashboard
- Using Notebook Outputs as Dashboard Variables

Related information:

- SystemLink Examples on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=analyzing-param-data-in-a-data-space.html language=enus -->
## TOPIC 00012: Analyzing Parametric Data in a Data Space

- bundle_id: `systemlink-enterprise`
- source_path: `analyzing-param-data-in-a-data-space.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/analyzing-param-data-in-a-data-space.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Derive insights about your parametric data in a data space. Introduced in December 2024 This section uses the default Jupyter Notebook, Data Space Analysis. To create a custom script for analyzing parametric data, refer to the Related tasks. Before you begin, complete the following tasks. Download t

### Analyzing Parametric Data in a Data
 Space

Derive insights about your parametric data in a data space.

Introduced in December 2024

Data
 Space Analysis

Related tasks

- Download the default Jupyter Notebook, Data Space Analysis 
 ( Data_Space_Default_Analysis.ipynb ) from GitHub.
 Publish the notebook under the DataSpace Analysis 
 interface of a workspace you can access.
- Plot the data you want to analyze in a data space.

To analyze your parametric data, complete the following
 steps.

1. Navigate to Product Insights»Data Spaces.
2. Open the data space with the data you want to analyze.
3. To expand the Analysis window at the bottom of the page,
 click Show analysis table ([IMAGE alt='Show analysis table button (up arrow) at the bottom of the page.' src='GUID-EB23BB3A-6A16-486E-A969-C4CC4D054D11-a5.png']).
4. Click Analyze. 
 After the analysis completes, SystemLink Enterprise displays the
 statistical results.
5. Optional: 
 In the Analysis window, click
 Configure
 [IMAGE alt='Configure icon (three vertical sliders).' src='GUID-116D9367-1613-4644-B25F-ECBEAB894A5D-a5.png'] to open the Configure grid slide-out. Complete the
 steps that align with your goal and click OK. 
 OptionDescriptionChange a column.
 Click a column in the list.
 Select a new analysis from the drop-down menu.
 Update the alias for the column.Add a column.
 Click Add column.
 Select the analysis you want to add.
 Designate an alias for the column.Remove a column.
 Click Remove
 [IMAGE alt='Remove icon (X).' src='GUID-D33CA224-5327-4C1E-A6B8-026795B53DFE-a5.png'] next to the column you want to remove.Rearrange the columns.
 Click Drag to reorder
 [IMAGE alt='Drag-to-reorder handle icon (six dots).' src='GUID-1410F8D5-D872-4E87-8BE1-7AC4D5E9E3C0-a5.png'] next to the column you want to move.
 Drag and drop the column in the new location. 
 Note If you are using a custom script and do not see the
 results from your custom script, ensure the following. You have published your custom script to a workspace you can
 access.
 Your custom script conforms to the DataSpace
 Analysis interface.
6. Optional: 
 To show or hide the result from a cell in the plot, click
 Actions
 [IMAGE alt='Actions menu icon (three dots).' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png'] next to the cell.

Saving the dataspace also saves the analysis results,
 including any columns and plots.

Parent topic:

Interacting with Data in a Data Space

Related tasks:

- Publishing a Jupyter Notebook
- Creating a Custom Script for Analyzing Parametric Data

Related information:

- Data Space Analysis Notebook (GitHub)

<!--NI_TOPIC bundle=systemlink-enterprise path=analyzing-specification-compliance-with-jupyter-notebooks.html language=enus -->
## TOPIC 00013: Analyzing Specification Compliance with Jupyter Notebook

- bundle_id: `systemlink-enterprise`
- source_path: `analyzing-specification-compliance-with-jupyter-notebooks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/analyzing-specification-compliance-with-jupyter-notebooks.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Verify whether your products comply with specification requirements by analyzing product test results against the specification. Refer to the SystemLink Enterprise examples on GitHub for an example notebook. Navigate to Product Insights Products . Click the product containing the specification you w

### Analyzing Specification Compliance with
 Jupyter Notebook

Verify whether your products comply with specification requirements by analyzing product
 test results against the specification.

SystemLink Enterprise

1. Navigate to Product Insights»Products.
2. Click the product containing the specification you want to analyze.
3. Click the Specs tab.
4. Select one or more specifications you want to analyze.
5. Click Analyze.
6. In the Analyze Specs slide-out, select the notebook you
 want to use for your analysis. 
 Note If you do not see the
 notebook you are looking for, ensure that you published the notebook to a
 workspace you can access. Additionally, ensure that the notebook corresponds
 to the Specification Analysis interface.
7. Optional: 
 Set the timeout for the execution.
8. Click Analyze. 
 SystemLink opens the Executions details window and
 shows details about the execution you initiated. Note SystemLink Enterprise preserves up to 16 MB of notebook
 execution data for 7 days. To retain more data for longer, ensure that your
 notebook saves and uploads your data to SystemLink.
9. After SystemLink completes the analysis, click Configure
 [IMAGE alt='Configure button (sliders icon) in the Executions details window.' src='GUID-116D9367-1613-4644-B25F-ECBEAB894A5D-a5.png'] to open the Configure grid slide-out.
10. Optional: 
 Add one or more new columns that the analysis generated.

SystemLink adds the results from the analysis to the
 corresponding specification.

Attributes

Properties

Parent topic:

Specification Compliance

Related tasks:

- Viewing Product Specifications

Related information:

- SystemLink Examples on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=analyzing-test-data-jupyter.html language=enus -->
## TOPIC 00014: Analyzing and Interacting with Test Results

- bundle_id: `systemlink-enterprise`
- source_path: `analyzing-test-data-jupyter.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/analyzing-test-data-jupyter.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Generate, filter, and visualize test results to analyze your test and measurement data. Use the following topics to complete the tasks that best suit your goals.

### Analyzing and Interacting with Test
 Results

Generate, filter, and visualize test results to analyze your test and measurement
 data.

Use the following topics to complete the tasks that best suit your goals.

- [Creating a Product](creating-a-product.html) Create a product to group test results and files from related DUTs in one view.
- [Visualizing Your Test Result Metadata](visualizing-metadata-of-your-test-results.html) View and modify the metadata, such as keywords or properties, associated with your test results so you can interact with data more efficiently.
- [Viewing Test Results by Product](visualizing-test-results-by-product.html) Analyze information about the product associated with your tests to determine the quality metrics of the devices under test (DUT).
- [Collaborating on Test Results](collaborating-on-test-results.html) Collaborate on test results by adding comments.
- [Viewing Test Steps by Result](viewing-test-steps-by-result.html) Analyze information about the results associated with your tests to determine the quality metrics of the devices under test (DUT).
- [Moving a Test Result to Another Workspace](moving-a-test-result.html) Move a test result to a different workspace so users in that workspace can access it.
- [Analyzing Test Results with Jupyter Notebook](analyzing-test-results-with-jupyter-notebooks.html) Analyze your test results using Jupyter Notebook to get insights about your data.
- [Visualizing Notebook Data on a Dashboard](visualizing-notebook-data-on-dashboard.html) Create a dashboard to visualize data from Jupyter notebooks.
- [Visualizing Data Tables in a Dashboard](visualizing-data-tables-in-a-dashboard.html) Select data tables associated with a test result to visualize in a dashboard.
- [Using Data Tables as Dashboard Variables](using-data-tables-as-dashboard-variables.html) Create variables that use data tables to dynamically view dashboard data.
- [Interacting with Data in a Data Space](interacting-with-data-in-a-data-space.html) Data Spaces allow you to analyze your data using scripts and create data visualizations.
- [Predefined Properties](predefined-properties.html) Reference NI-created properties to organize your tests, assets, tags, or files.

Parent topic:

Monitoring Tests

Related tasks:

- Viewing Test Results by Product
- Visualizing Your Test Result Metadata

<!--NI_TOPIC bundle=systemlink-enterprise path=analyzing-test-results-with-jupyter-notebooks.html language=enus -->
## TOPIC 00015: Analyzing Test Results with Jupyter Notebook

- bundle_id: `systemlink-enterprise`
- source_path: `analyzing-test-results-with-jupyter-notebooks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/analyzing-test-results-with-jupyter-notebooks.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Analyze your test results using Jupyter Notebook to get insights about your data. Refer to the SystemLink Enterprise examples on GitHub for an example notebook. Complete the steps that best align with your goal. Analyze one or more test results Navigate to Product Insights Test Results . Analyze one

### Analyzing Test Results with Jupyter
 Notebook

Analyze your test results using Jupyter Notebook to get insights about your
 data.

SystemLink Enterprise

1. Complete the steps that best align with your goal. 
 OptionDescriptionAnalyze one or more test results
 Navigate to Product Insights»Test Results.Analyze one or more test results for a specific product
 Navigate to Product Insights»Products.
 Click the Results tab.
2. Select one or more test results and click Analyze.
3. In the Analyze results slide-out, select the notebook you
 want to run on your test results. 
 Note If you do not see the
 notebook you are looking for, ensure that you published the notebook to a
 workspace you can access. Additionally, ensure that the notebook corresponds
 to the Test Data Analysis interface.
4. Set the timeout for the execution.
5. Set additional parameters.
6. Click Analyze. 
 SystemLink opens the Executions details window and
 shows details about the execution you initiated. Note SystemLink Enterprise preserves up to 16 MB of notebook
 execution data for 7 days. To retain more data for longer, ensure that your
 notebook saves and uploads your data to SystemLink.

Parent topic:

Analyzing and Interacting with Test Results

Related information:

- SystemLink Examples on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=applying-custom-metadata-to-assets.html language=enus -->
## TOPIC 00016: Applying Custom Metadata to Assets

- bundle_id: `systemlink-enterprise`
- source_path: `applying-custom-metadata-to-assets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/applying-custom-metadata-to-assets.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Assign properties or keywords to your assets so you can search and filter them in your workspace. Navigate to Systems Management Assets . Click the asset you want to assign properties and keywords to. Click Edit icon (pencil). to edit the asset. Click Add keyword to enter a string value to associate

### Applying Custom Metadata to Assets

Assign properties or keywords to your assets so you can search and filter them in your
 workspace.

1. Navigate to Systems Management»Assets.
2. Click the asset you want to assign properties and keywords to.
3. Click [IMAGE alt='Edit icon (pencil).' src='GUID-F5E3D327-1023-4E95-BDF9-74CBA26BD57F-a5.png'] to edit the asset.
4. Click Add keyword to enter a string value to associate with the
 asset.
5. Click Add property to enter a key-value pair to associate with
 the asset.
6. Click Update. 
 You can now filter the list on the Assets page to show only
 assets that match the keywords or properties you assigned.

Parent topic:

Managing Your Assets

<!--NI_TOPIC bundle=systemlink-enterprise path=archiving-workspaces.html language=enus -->
## TOPIC 00017: Archiving Your Workspaces

- bundle_id: `systemlink-enterprise`
- source_path: `archiving-workspaces.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/archiving-workspaces.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Store your workspaces when your organization is no longer using them. Before you begin, delete or disable any active routines associated with the workspaces you want to archive. If you archive a workspace, only users with the Server Administrator role can access it. No user, including an administrat

### Archiving Your Workspaces

Store your workspaces when your organization is no longer using them.

Before you begin, delete or disable any active routines
 associated with the workspaces you want to archive.

If you archive a workspace, only users with the Server Administrator role can access it. No
 user, including an administrator, can edit its resources.

1. In the SystemLink web application, click Access Control»Workspaces.
2. Find the workspace you want to archive and click [IMAGE alt='Actions menu (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png']»Archive workspace .
3. Click ARCHIVE. 
 Your workspace is now archived.

Parent topic:

Managing Access to SystemLink Enterprise

Related tasks:

- Creating a Workspace

Related reference:

- Role-Based Access Control Concepts

<!--NI_TOPIC bundle=systemlink-enterprise path=assigning-a-server-administrator-to-a-server.html language=enus -->
## TOPIC 00018: Assigning a Server Administrator to a Server

- bundle_id: `systemlink-enterprise`
- source_path: `assigning-a-server-administrator-to-a-server.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/assigning-a-server-administrator-to-a-server.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Assign additional server administrators to help setup workspaces and define the roles available on the server. Server administrators can delegate workspace access management to workspace owners. In the SystemLink web application, click Access Control Roles . Click Gear icon and create a server admin

### Assigning a Server Administrator to a
 Server

Assign additional server administrators to help setup workspaces and define the roles
 available on the server.

Server administrators can delegate workspace access
 management to workspace owners.

1. In the SystemLink web application, click Access Control»Roles.
2. Click [IMAGE alt='Gear icon' src='GUID-F365AA0A-76E7-445B-BF21-BD366FEDA5D4-a5.png'] and create a server administrator mapping.

Parent topic:

Managing Access to SystemLink Enterprise

<!--NI_TOPIC bundle=systemlink-enterprise path=associating-test-results-with-a-product.html language=enus -->
## TOPIC 00019: Associating Test Results with a Product

- bundle_id: `systemlink-enterprise`
- source_path: `associating-test-results-with-a-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/associating-test-results-with-a-product.html
- document_id: `systemlink-enterprise`
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

<!--NI_TOPIC bundle=systemlink-enterprise path=automate-test-plans-with-jupyter-notebook.html language=enus -->
## TOPIC 00020: Automating Work Items with Jupyter Notebook

- bundle_id: `systemlink-enterprise`
- source_path: `automate-test-plans-with-jupyter-notebook.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/automate-test-plans-with-jupyter-notebook.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Jupyter Notebooks to automate and to schedule your work items with custom algorithms. For an example Jupyter notebook, refer to the SystemLink Enterprise Examples on GitHub. In SystemLink Enterprise, navigate to Operations Work Items . Select one or more work items from the work items table. In

### Automating Work Items with Jupyter
 Notebook

Use Jupyter Notebooks to automate and to schedule your work items with custom
 algorithms.

Note

SystemLink Enterprise

1. In SystemLink Enterprise, navigate to Operations»Work Items.
2. Select one or more work items from the work items table.
3. In the toolbar, choose one of the following options.
  - To automate one or more work items, click
 Automate .
  - To auto schedule one or more work items, click
 Auto schedule .
4. In the slide-out, select the notebook that you want to perform
 an action upon. 
 Note If you do not see your notebook,
 ensure that you published the notebook to an
 accessible workspace.
 Note Depending on your previous
 choice, ensure that the created notebook corresponds
 to the Work Item Automations
 interface or the Work Item
 Scheduler interface.
5. Set the timeout for the execution.
6. Based on your previous choice, click
 Automate or Auto
 schedule.

SystemLink Enterprise opens the Executions
 details window to display information on the
 execution.

SystemLink Enterprise preserves up to 16 MB of notebook
 execution data for seven days. To retain more data for longer,
 ensure that your notebook saves and uploads your data to SystemLink Enterprise.

Parent topic:

Managing Work Orders and Work Items

Related tasks:

- Scheduling a Work Item
- Publishing a Jupyter Notebook

Related information:

- SystemLink Examples on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=automating-actions-with-routines.html language=enus -->
## TOPIC 00021: Automating Actions with Routines

- bundle_id: `systemlink-enterprise`
- source_path: `automating-actions-with-routines.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/automating-actions-with-routines.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create routines to automate an action when an event occurs. In SystemLink Enterprise, click Analysis Routines . Click Create routine. In the Create routine slide-out, navigate to the General section to enter a routine name and a description. Specify the workspace you want to associate with the routi

### Automating Actions with Routines

Create routines to automate an action when an event occurs.

1. In SystemLink Enterprise, click Analysis»Routines.
2. Click Create routine.
3. In the Create routine slide-out, navigate to the
 General section to enter a routine name and a
 description.
4. Specify the workspace you want to associate with the routine. 
 Automations run on Jupyter notebooks with the permissions of the user who
 created the routine. For Work Item Changed events and Test Result Changed
 events, you must specify a service account. This account runs the Jupyter
 notebook with permissions that your system administrator
 defines.These permissions remain true regardless of who interacts
 with the routine. Users that can access the workspace of the routine can
 also enable that routine. Therefore, if a user with administrator
 permissions creates a routine, other users with fewer permissions can still
 enable that routine.Note Tag value events only
 trigger for tags contained within the selected workspace.
5. Optional: 
 Set the Routine state toggle. 
 SystemLink enables this toggle by default. As a part of this routine,
 SystemLink listens for triggering events immediately after routine creation.
 Disable the Routine state toggle to prevent the routine
 from responding to events.
6. In the Automation configuration section, specify the event
 that you want SystemLink Enterprise to monitor. 
 Option
 DescriptionAt a specific date and
 time
 The event triggers on a specific cadence.
 File uploaded
 The event after a new file upload.
 File metadata changed
 The event after an update to an existing file.
 Tag value updated
 The event after a tag value update.
 Test result changed
 The event triggers when a test result property changes.
 You can further filter which resources trigger the
 routine.
 Work item changed
 The event triggers when a specified work item property
 changes. You can further filter which resources trigger the
 routine.
7. Configure the event details.
8. Specify the automation you want SystemLink Enterprise to run
 for the routine automation configuration. 
 Option
 DescriptionExecute a notebook
 Executes a Jupyter notebook when the event triggers.
 For date/time-based and file-based events, the notebook
 uses a standard configuration. If the notebook does not
 appear, ensure the following:You published the Jupyter notebook to a
 workspace you can access.
 You assigned one of the following interfaces to
 the Jupyter notebook.Periodic Execution—Use
 this interface for time-based events.
 File Analysis or
 Test Data Extraction—Use
 these interfaces for file-based events.
 For Work Item Changed and Test Result Changed events, the
 notebook uses enhanced execution configuration options.
 These options include a service account, the notebook
 resource profile, and notebook priority.
 The Jupyter notebook must contain the Resource Changed
 Routine interface. If the notebook does not appear,
 ensure the following.
 You published the Jupyter notebook to an accessible
 workspace.
 You assigned the Resource Changed Routine interface
 to the Jupyter notebook.
 Generate alarm
 Generates an alarm that is based on the routine
 conditions.
9. Configure the automation details. 
 If you select a Execute a notebook for a Work Item
 Changed event or a Test Result Changed
 event, configure the following Jupyter notebook execution settings.Note These settings are not available for other event
 types. 
 Setting
 Configuring the SettingRun routine as
 Select a service account to run the Jupyter notebook with
 permissions defined by your system administrator.
 Service accounts are required for the Work Item Changed
 events and the Test Result Changed events.
 The service account has the following privileges.Scripts — Lists published notebooks in
 SystemLink and downloads published notebooks into
 the Jupyter development environment.
 Executions — Executes the notebook.
 (Optional) Executions — Allows authors to choose
 the resource profile.
 To create a service account, use the following steps.
 Navigate to Access Control»Roles and find or create a role with the
 previous privileges.
 Create a service account user through the SystemLink
 CLI using the following command.slcli
 user create --type service --first-name
 your-service-account-name --workspace-policies
 workspace-name-or-id:role-name-or-id
10. Expand the Advanced section to configure the following
 settings. 
 Setting
 Configuring the SettingNotebook resource profile
 Select one of the following memory allocation settings
 for the Jupyter notebook pod.
 Default — The default system allocation.
 Low — The minimal memory allocation for lightweight
 operations.
 Medium — The standard memory allocation.
 High — The maximum memory allocation for
 compute-intensive tasks.
 Notebook priority
 Select one of the following execution priority settings
 for the Jupyter notebook.
 High — The prioritized execution. This resource
 contention might favor high-priority jobs.
 Medium — The standard priority.
 Low — The lowest scheduling priority for background
 execution.
11. Click Create.

- If you selected Execute a notebook for any event
 type, navigate to Analysis»Executions to see executions for your routine. Note SystemLink Enterprise preserves up to 16 MB of Jupyter
 notebook execution data for seven days. To retain large amounts of
 execution data, ensure your Jupyter notebook uploads your data to SystemLink Enterprise.
- If you selected Generate alarm , navigate to Overview»Alarms and manage any alarm instances generated by your
 routine.

Related tasks:

- Monitoring System Health with Alarms

Related information:

- SystemLink CLI on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=change-locations.html language=enus -->
## TOPIC 00022: Changing Locations

- bundle_id: `systemlink-enterprise`
- source_path: `change-locations.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/change-locations.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Move an asset or system to a new location. Navigate to Systems Management Systems or Assets . Select a system or asset. Depending on what you are moving, use the following steps. System In the Edit system slide-out, click Location. Select a new location. Click Save. Asset Click Move. In the Move Ass

### Changing Locations

Move an asset or system to a new location.

1. Navigate to Systems Management»Systems or Assets.
2. Select a system or asset.
3. Depending on what you are moving, use the following steps. 
 OptionDescriptionSystem
 In the Edit system slide-out, click
 Location.
 Select a new location.
 Click Save.Asset
 Click Move.
 In the Move Assets window, set a
 Destination.
 Click Move.

Parent topic:

Managing Your Locations

<!--NI_TOPIC bundle=systemlink-enterprise path=changing-name-of-system.html language=enus -->
## TOPIC 00023: Changing a System Name

- bundle_id: `systemlink-enterprise`
- source_path: `changing-name-of-system.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/changing-name-of-system.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Assign your system a name that makes it easy to identify. Before you begin, you must connect the system to SystemLink Enterprise as a managed system. When a client system connects to SystemLink Enterprise, SystemLink Enterprise uses the system hostname to identify it. A hostname is often not human r

### Changing a System Name

Assign your system a name that makes it easy to identify.

SystemLink Enterprise

SystemLink Enterprise

SystemLink Enterprise

1. In the SystemLink web application under Systems
 Management, click Systems.
2. Click the system you want to rename.
3. Click Settings in the toolbar.
4. For Name, enter the alias you want to give the system. 
 Tip To enter additional
 identifying information, use the Description field.

You can now filter or search for the system by the name you assigned it.

Parent topic:

Modifying the Settings of a System

Related tasks:

- Connecting to Clients

<!--NI_TOPIC bundle=systemlink-enterprise path=collaborating-on-test-results.html language=enus -->
## TOPIC 00024: Collaborating on Test Results

- bundle_id: `systemlink-enterprise`
- source_path: `collaborating-on-test-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/collaborating-on-test-results.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Collaborate on test results by adding comments. In the SystemLink web application, navigate to Product Insights Test Results and select a test result. On the Comments tab, enter your message in the Add comment here field. You can format your comment with bold, italics, and bulleted or numbered lists

### Collaborating on Test Results

Collaborate on test results by adding comments.

1. In the SystemLink web application, navigate to Product Insights»Test Results and select a test result.
2. On the Comments tab, enter your message in the
 Add comment here field. 
 Note You can format your comment
 with bold, italics, and bulleted or numbered lists. Hitting
 Enter starts a new paragraph. Press
 Shift + Enter to start a new line.
3. @ mention other users you want to see or respond to your comment.
4. Click OK to save your comment. 
 Note You can edit and delete comments after saving. 
 SystemLink sends an email notification to any users you @
 mentioned.

Parent topic:

Analyzing and Interacting with Test Results

Related tasks:

- Viewing Test Results by Product

<!--NI_TOPIC bundle=systemlink-enterprise path=communicating-data-with-tags.html language=enus -->
## TOPIC 00025: Communicating Data with Tags

- bundle_id: `systemlink-enterprise`
- source_path: `communicating-data-with-tags.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/communicating-data-with-tags.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Communicate and manage data from your test and measurement systems with tags. Tags in SystemLink transmit and store slow-moving measurement data like system status or health. Use tags to track measurements, monitor system health, create alarms, and visualize data on dashboards.

### Communicating Data with Tags

Communicate and manage data from your test and measurement systems with tags. Tags in
 SystemLink transmit and store slow-moving measurement data like system status or health.
 Use tags to track measurements, monitor system health, create alarms, and visualize data
 on dashboards.

- [Transferring Data Using Tags](transferring-data-using-tags.html) Use tags to send and receive data from one system to other systems.
- [Monitoring Data with Tags](monitoring-data-with-tags.html) Observe the current value of one or more tags published to your system.

Parent topic:

Sharing Data across Systems

<!--NI_TOPIC bundle=systemlink-enterprise path=configuring-alarm-limits.html language=enus -->
## TOPIC 00026: Configuring Alarm Limits

- bundle_id: `systemlink-enterprise`
- source_path: `configuring-alarm-limits.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/configuring-alarm-limits.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Adjust how many alarms you can create in the SystemLink Enterprise Alarm Service. Introduced in September 2024 If you reach an alarm limit, the Alarm Service returns an error. This error occurs when Alarm Service processes a new alarm creation request. You can monitor the number of active and inacti

### Configuring Alarm Limits

Adjust how many alarms you can create in the SystemLink Enterprise Alarm Service.

Introduced in September 2024

Performance Metrics for the Alarm Service

SystemLink Enterprise

- Active alarms: The Alarm Service allows you to create up to 10,000 active
 alarms. If you reach this limit, you must complete one of the following
 actions.
  - Delete some active alarms.
  - Deactivate some active alarms. You can force alarms inactive by
 using the acknowledge API. Set the forceClear 
 flag on the request to true .
- Total alarms: The Alarm Service allows you to create up to 100,000 alarms
 total. This limit includes both active alarms and inactive alarms. If you
 reach this limit, you must delete some alarms before you can create new
 alarms.

Note

1. Open the systemlink-values.yaml file.
2. Make the changes that align with your goal. 
 OptionDescriptionConfigure the limit for active alarms.
 Modify the value of
 alarmservice.activeAlarmLimit.Configure the limit for total alarms.
 Modify the value of
 alarmservice.alarmLimit.

Parent topic:

Generating Custom Alarms

Related tasks:

- Configuring Alarm Retention
- Monitoring Alarms

<!--NI_TOPIC bundle=systemlink-enterprise path=configuring-alarm-retention.html language=enus -->
## TOPIC 00027: Configuring Alarm Retention

- bundle_id: `systemlink-enterprise`
- source_path: `configuring-alarm-retention.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/configuring-alarm-retention.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Adjust how long the SystemLink Enterprise Alarm Service keeps your alarms. Introduced in September 2024 The Alarm Service has the following default settings for retaining active and inactive alarms. Active alarms: The Alarm Service deletes active alarms that you have not updated in 90 days. Inactive

### Configuring Alarm Retention

Adjust how long the SystemLink Enterprise Alarm Service keeps your
 alarms.

Introduced in September 2024

The Alarm Service has the following default settings for retaining active and
 inactive alarms.

- Active alarms: The Alarm Service deletes active alarms that you have not updated
 in 90 days.
- Inactive alarms: The Alarm Service deletes inactive alarms after 30 days.

To change the alarm retention settings, complete the following steps.

Note

1. Open the systemlink-values.yaml file.
2. Complete the following steps based on your goal. 
 OptionDescriptionConfigure retention for active alarms.
 Modify the value of
 alarmservice.database.activeAlarmCleanup.interval.
 To delete only active alarms with
 CLEAR as the most recent transition, set
 alarmservice.database.activeAlarmCleanup.onlyCleanUpClearActiveAlarms
 to true.Configure retention for inactive alarms.
 Modify the value of
 alarmservice.database.inactiveAlarmCleanupInterval.
3. Optional: 
 To retain alarms permanently, you must specify the
 nialarminstancePermanent keyword in the keywords list
 when creating the alarm. 
 Note 
 Use this setting sparingly. The Alarm Service limits the number of alarms
 you can create. If you retain too many alarms indefinitely, you might
 reach the Alarm Service alarm limit.

Parent topic:

Generating Custom Alarms

Related tasks:

- Configuring Alarm Limits
- Monitoring Alarms

<!--NI_TOPIC bundle=systemlink-enterprise path=configuring-roles-privileges.html language=enus -->
## TOPIC 00028: Configuring a Role and Privileges

- bundle_id: `systemlink-enterprise`
- source_path: `configuring-roles-privileges.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/configuring-roles-privileges.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create and assign privileges to a role to customize how users can interact with each SystemLink application and service. A role is any set of permissions you want to assign to a group of users or services. There is no limit to the number of roles in a workspace, for a user, or for a service. You can

### Configuring a Role and Privileges

Create and assign privileges to a role to customize how users can interact with each
 SystemLink application and service.

A *role* is any set of permissions you want to assign to a group of users or
 services. There is no limit to the number of roles in a workspace, for a user, or for a
 service. You can use the same role in multiple workspaces.

1. In the SystemLink web application, click Access Control»Roles.
2. Click Create Role.
3. Enter a name for the role.
4. On the Privileges tab, under Applications and
 services, select the application or service you want to assign
 privileges for. 
 Assign the minimum number of privileges that users need to perform their work.
 Assigning the minimum number of privileges helps you maintain security.
5. Check the box for each privilege type you want the role to have. 
 Note Checking Allow all
 privileges grants this role any new privileges included in future versions
 of SystemLink Enterprise.
6. Click Create.
7. Repeat steps 3–5 for each application or service this role interacts
 with. 
 It can take up to 5 minutes for privilege changes to take effect.

After you configure a role, assign users or
 analysis routines in any workspace to the role. You can modify roles at any
 time.

Parent topic:

Managing Access to SystemLink Enterprise

Related tasks:

- Assigning Users to Roles in a Workspace

Related reference:

- Predefined Roles in SystemLink Enterprise
- Role-Based Access Control Concepts

<!--NI_TOPIC bundle=systemlink-enterprise path=configuring-user-account-settings.html language=enus -->
## TOPIC 00029: Viewing and Editing User Account Settings

- bundle_id: `systemlink-enterprise`
- source_path: `configuring-user-account-settings.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/configuring-user-account-settings.html
- document_id: `systemlink-enterprise`
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

Parent topic:

Navigating SystemLink Enterprise

<!--NI_TOPIC bundle=systemlink-enterprise path=connecting-clients.html language=enus -->
## TOPIC 00030: Connecting to Clients

- bundle_id: `systemlink-enterprise`
- source_path: `connecting-clients.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/connecting-clients.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Exchange data between clients like LabVIEW and SystemLink using SystemLink data services. Access these data services through the Data Communication palette in LabVIEW and LabVIEW NXG. Refer to the following table to determine which data service to use depending on your needs. Goal What to use Publis

### Connecting to Clients

Exchange data between clients like LabVIEW and SystemLink using SystemLink data
 services. Access these data services through the Data Communication palette in LabVIEW and
 LabVIEW NXG.

Refer to the following table to determine which data service to use depending
 on your needs.

| Goal | What to use |
| --- | --- |
| Publish an entire file from a client to SystemLink for storage, additional processing, or access by other clients. | File Transfer |
| Manage and communicate test data between your test systems and SystemLink. | Test Monitor |
| Publish DataFrames from a client to SystemLink for storage, additional processing, or access by other clients. | DataFrames |

Parent topic:

Sharing Data across Systems

Related tasks:

- Transferring Files from Disk to SystemLink Enterprise
- Acquiring Test Results

<!--NI_TOPIC bundle=systemlink-enterprise path=connecting-test-data-to-specifications.html language=enus -->
## TOPIC 00031: Connecting Test Data to Specifications

- bundle_id: `systemlink-enterprise`
- source_path: `connecting-test-data-to-specifications.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/connecting-test-data-to-specifications.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Link your test data to specifications so you can compare measurement results to specification limits. The Spec ID is the primary key you use to connect a specification to a measurement. You must store your parametric data as test results under the product that contains the specifications. Each measu

### Connecting Test Data to Specifications

Link your test data to specifications so you can compare measurement results to
 specification limits.

The Spec ID is the primary key you use to connect a specification to a measurement.

You must store your parametric data as test results under the product that contains the
 specifications. Each measurement under a test step must include a field called
 specId for each parameter that you link to a specification.

Spec Id =
 OutputVoltage1

```text
{
  "name": "Voltage Step",
  "data": {
    "parameters": [
      {
        "name": "Voltage",
        "measurement": 15.234049,
        "units": "mV",
        "specId": "OutputVoltage1"
      }
    ]
  }
}
```

If you collected the test data using the Bench Data Connector (BDC) Logging Libraries,
 use the BDC file ingestion service to ingest the data. The BDC file ingestion service
 automatically captures the Spec ID on each measurement.

Parent topic:

Specification Compliance

<!--NI_TOPIC bundle=systemlink-enterprise path=create-and-delete-states.html language=enus -->
## TOPIC 00032: Creating and Deleting System States

- bundle_id: `systemlink-enterprise`
- source_path: `create-and-delete-states.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/create-and-delete-states.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: System states provide configuration management for SystemLink systems by defining feeds and packages with specific software versions. System states are a powerful mechanism that provides configuration management for your test systems. For more information about what is possible with a system state,

### Creating and Deleting System States

System states provide configuration management for SystemLink systems by defining
 feeds and packages with specific software versions.

- For more information about what is possible with a system state,
 refer to How do I use Salt States? in the Salt
 Project documentation.
- For SystemLink examples of how to implement system states, refer
 to Advanced SystemLink State Examples in the NI
 GitHub repository.

Use the following workflows to simplify the creation of a state.

| Workflows | Steps |
| --- | --- |
| Create a state from a managed system | You can create a state that contains references to all feeds and packages on a managed system. Use this method to ensure all packages, with specific software versions, install to a target system. Note Using a state from this method does not remove unreferenced packages from the target system. Use the SystemLink navigation menu to open the Systems application. In the Systems table, select a managed system.Note Use the search function in the menu bar to find a system using the name or other metadata. From the menu bar, click More to see additional options, and select Create State. For the new state, specify a name, workspace, and any additional metadata. Click Create to confirm the changes. In the Systems application, use the notification banner to navigate to the newly created state. View the state and make any necessary edits. |
| Create a state from a set of feeds and packages | You can create a state to install a specific set of packages. Use this method to apply a software set from disparate feeds to a managed system. Use the SystemLink navigation menu to open the Systems application. In the main menu bar, click Create State. For the new state, specify a name, workspace, and any additional metadata. Click Create to confirm the changes. On the State Details page, specify the feeds and packages that the state configures and installs upon use. Navigate to the Packages tab and In the main menu bar, click Add packages. Follow the guided steps and select the software for the state to install to a system. Return to the State Details page and add more software packages. Navigate to the Feeds tab and verify that all feeds match your expectations. |

Parent topic:

Managing Your Software

Related information:

- How do I use Salt States?
- Advanced SystemLink State Examples

<!--NI_TOPIC bundle=systemlink-enterprise path=create-and-edit-spec-for-product.html language=enus -->
## TOPIC 00033: Creating and Editing Product Specifications through SystemLink

- bundle_id: `systemlink-enterprise`
- source_path: `create-and-edit-spec-for-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/create-and-edit-spec-for-product.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: You can create or edit a product specification directly from the SystemLink user interface. Navigate to Product Insights Products . Select the product within which you want to add a specification. Click the Specs tab. Click Create Spec and configure the specification values. Specify a Name and Spec

### Creating and Editing Product Specifications
 through SystemLink

You can create or edit a product specification directly from the SystemLink user
 interface.

1. Navigate to Product Insights»Products.
2. Select the product within which you want to add a specification.
3. Click the Specs tab.
4. Click Create Spec and configure the specification
 values.
  1. Specify a Name and Spec
 ID.
  2. Specify the specification type as Parametric or
 Functional. 
 Note If the specification type is parametric,
 specify the limits.
  3. Optional: 
 Specify the Symbol, Unit,
 Category, and
 Block.
  4. Click Create. 
 SystemLink opens the new specification.
5. To edit the specification, select the spec and click
 Edit
 [IMAGE alt='Edit button icon (pencil).' src='GUID-0835BF4B-9CBF-4DFB-A552-85C222FB9A9C-a5.png'].

Parent topic:

Specification Compliance

Related tasks:

- Viewing Product Specifications
- Creating, Viewing, and Managing Specification Conditions
- Deleting Specifications

Related information:

- Enabling the Specification Compliance Module

<!--NI_TOPIC bundle=systemlink-enterprise path=create-view-manage-conditions.html language=enus -->
## TOPIC 00034: Creating, Viewing, and Managing Specification Conditions

- bundle_id: `systemlink-enterprise`
- source_path: `create-view-manage-conditions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/create-view-manage-conditions.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: After creating a specification, you can add and edit specification conditions from the SystemLink user interface. Navigate to Product Insights Products . Select a product that contains a specification. Click the Specs tab. Click a spec ID. SystemLink opens the Specification details page. Click the C

### Creating, Viewing, and Managing Specification
 Conditions

After creating a specification, you can add and edit specification conditions from
 the SystemLink user interface.

1. Navigate to Product Insights»Products.
2. Select a product that contains a specification.
3. Click the Specs tab.
4. Click a spec ID. 
 SystemLink opens the Specification details page.
5. Click the Conditions tab.
6. Click Add condition. 
 SystemLink adds a new condition and displays the condition details in the pane
 on the right.
7. In the Condition details section, provide the following
 information.
  1. Set the condition type as Numeric or
 String.
  2. Specify the condition name.
  3. Optional: 
 If the condition is numeric, specify the unit.
8. In Condition values section, specify the condition
 values.
  1. For numeric conditions, provide a range of values or a discrete set of
 values. 
 Value Type
 DescriptionRange
 Provide a range of values.
 Click the Range tab.
 Click Add range.
 Specify the minimum, maximum, and step.Discrete
 Provide a discrete set of values.
 Click the Discrete tab.
 Click Add discrete.
 Specify the value.
  2. For string conditions, provide a discrete set of values.
9. Edit a condition.
  1. In the table, select a condition.
  2. In the pane on the right, update the appropriate fields.
10. Remove one or more conditions.
  1. In the table, select the conditions.
  2. Click Remove.
11. Click Save.

Parent topic:

Specification Compliance

Related tasks:

- Creating and Editing Product Specifications through SystemLink
- Viewing Product Specifications
- Deleting Specifications

Related reference:

- Structure of a Specification

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-a-new-jupyter-notebook.html language=enus -->
## TOPIC 00035: Creating a Notebook in Jupyter Notebooks

- bundle_id: `systemlink-enterprise`
- source_path: `creating-a-new-jupyter-notebook.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-a-new-jupyter-notebook.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a notebook (.ipynb) in JupyterHub to visualize, analyze, and process data. Before you create a Jupyter notebook, complete the following tasks:Learn about the user interface and structure of a Jupyter notebook.Install Python libraries you want to use to enhance your data analysis and processin

### Creating a Notebook in Jupyter
 Notebooks

Create a notebook (.ipynb) in JupyterHub to visualize, analyze,
 and process data.

- Learn about the user interface and structure of a Jupyter notebook.
- Install Python libraries you want to use to enhance your data analysis and processing. NI
 recommends using PyPI to obtain packages.
- Learn about the built-in magic commands the IPython kernel enables.

Complete the following steps to create a Jupyter
 notebook.

1. In the SystemLink web application, navigate to Analysis»Scripts.
2. Click Python 3 (ipykernel).
3. Use the linked example as a guide to create a notebook that meets your programming
 needs.

Sharing a Jupyter Notebook

Parent topic:

Reporting Data with Jupyter Notebooks

Related tasks:

- Installing Additional Python Modules

Related information:

- Example Notebook
- nisystemlink-clients Package
- nisystemlink.clients Documentation
- Python API Reference
- Jupyter User Interface
- Structure of a Notebook Document
- PyPI
- Built-In Magic Commands

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-a-product.html language=enus -->
## TOPIC 00036: Creating a Product

- bundle_id: `systemlink-enterprise`
- source_path: `creating-a-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-a-product.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a product to group test results and files from related DUTs in one view. Products can contain the following. Results Files Work Items Specifications Navigate to Product Insights Products . Click Create product. Specify a name, part number, and family for your product to make it easy to identi

### Creating a Product

Create a product to group test results and files from related DUTs in one
 view.

- Results
- Files
- Work Items
- Specifications

1. Navigate to Product Insights»Products.
2. Click Create product.
3. Specify a name, part number, and family for your product to make it easy to
 identify later.
4. Assign properties or keywords to your product to facilitate searching and
 filtering.
5. Click Create. 
 You can now select your product to open a detailed view that includes
 all the results and files associated with your product.Note When a test generates a new
 result, SystemLink automatically creates a product if it cannot find a
 product with a corresponding part number. In that case, you do not need to
 manually create a product.

Parent topic:

Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-a-test-plan.html language=enus -->
## TOPIC 00037: Creating a Work Item

- bundle_id: `systemlink-enterprise`
- source_path: `creating-a-test-plan.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-a-test-plan.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create one or more work items to track lab activities. You can create a work item in the following situations: As a part of a product As a part of a DUT As a part of a work order Independently of other constraints Complete the steps that align with your goal. Create a work item. Navigate to Operatio

### Creating a Work Item

Create one or more work items to track lab activities.

- As a part of a product
- As a part of a DUT
- As a part of a work order
- Independently of other constraints

1. Complete the steps that align with your goal. 
 OptionDescriptionCreate a work item.
 Navigate to Operations»Work Items.
 Click Create test plan.Create a work item for a specific product.
 Navigate to Product Insights»Products.
 Click the product for which you want to create a work item.
 Click the Work Items tab.
 Click Create test plan.Create a work item as part of a work order.
 Navigate to Operations»Work Orders.
 Click the work order for which you want to create a work
 item.
 Click the Work Items tab.
 Click Create test plan.Create a work item as part of a DUT.
 Navigate to Systems Management»Assets.
 Click the DUT for which you want to create a work item.
 Click the Work Items tab.
 Click Create test plan. 
 Note To create a different work item type, use the
 drop-down menu. Certain assets have work item restrictions. For a product,
 you can only create a test plan or a job. For a DUT, you can only create a
 test plan, job, or reservation.
2. Click Next and view a list of templates you can use to
 create a work item. 
 Note If the work item type does not have an associated
 template, the template selection screen does not appear. To create a new
 work item template, use the SystemLink API.
3. Select a template.
4. Click Next. 
 SystemLink Enterprise copies the template into a new work
 item.
5. Optional: 
 Click the Info tab to modify the work item
 details.
6. Optional: 
 Click the Reservation tab to accomplish the following
 goals.
  1. Reserve resources for the work item, such as systems, assets, and
 DUTs.
  2. Set the start date.
  3. Set the end date.
7. Optional: 
 For a transport order, specify the target location and the target parent for
 each resource.
8. Click Create. 
 SystemLink Enterprise opens the new work item.
9. To add files to the work item, click Files»Upload files.

After creating a work item, you can perform operations
 such as scheduling the work item through the scheduling assistant.

Parent topic:

Managing Work Orders and Work Items

Related tasks:

- Filtering Grids
- Scheduling a Work Item

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-a-workspace.html language=enus -->
## TOPIC 00038: Creating a Workspace

- bundle_id: `systemlink-enterprise`
- source_path: `creating-a-workspace.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-a-workspace.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a workspace to control which systems and data different types of users can interact with. Workspaces limit user access to a particular collection of systems and the data those systems produce. When you add a system to a workspace, SystemLink Enterprise stores data from the system in the same

### Creating a Workspace

Create a workspace to control which systems and data different types of users can
 interact with.

Workspaces

SystemLink Enterprise

automatic data encapsulation

1. In the SystemLink web application, click Access Control»Workspaces.
2. Click Create Workspace.
3. Enter a name for the workspace and click OK.
4. Optional: 
 Repeat these steps to create as many workspaces as you need to organize your
 resources and reflect your organizational structure.

After you create a workspace,
 specify who can access it by connecting user attributes to roles. When using the
 SystemLink web application and SystemLink REST APIs, a user must be a member of a
 workspace to access the systems and data within the workspace.

Parent topic:

Managing Access to SystemLink Enterprise

Related tasks:

- Assigning Users to Roles in a Workspace
- Setting up a SystemLink Client

Related reference:

- Role-Based Access Control Concepts

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-an-api-key.html language=enus -->
## TOPIC 00039: Creating an API Key

- bundle_id: `systemlink-enterprise`
- source_path: `creating-an-api-key.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-an-api-key.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create an API key to automate access to the SystemLink API from an external application. An API key has the same privileges and workspace access as the user who creates it. Ensure that you have the necessary privileges to perform the action you want the key to access.Key privileges and access do not

### Creating an API Key

Create an API key to automate access to the SystemLink API from an external
 application.

Note

You must have API Key Management privileges to complete the
 following steps.

1. Click [IMAGE alt='User profile icon.' src='GUID-6887DBEC-A1FD-4B61-8AD0-69B8BC5F40D6-a5.png']»Account.
2. In the API keys tab of the Edit account
 slide-out, click Create API Key.
3. Optional: 
 Enter a name for the key.
4. Click [IMAGE alt='Copy icon' src='GUID-4D8D8B9E-44A8-483E-99FE-A75B3CE1BC99-a5.png'] to copy the key to your clipboard.
5. Click OK.

X-NI-API-Key

Parent topic:

Managing Access to SystemLink Enterprise

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-and-managing-work-orders.html language=enus -->
## TOPIC 00040: Creating and Managing Work Orders

- bundle_id: `systemlink-enterprise`
- source_path: `creating-and-managing-work-orders.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-and-managing-work-orders.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create work orders for assignment and tracking to lab personnel. Navigate to Operations Work Orders . You can filter the list of existing work orders by clicking the summary tiles at the top of the page. Click Create work order. Specify the name, earliest start date, due date, and description. Click

### Creating and Managing Work Orders

Create work orders for assignment and tracking to lab personnel.

1. Navigate to Operations»Work Orders.
2. Optional: 
 You can filter the list of existing work orders by clicking the summary tiles
 at the top of the page.
3. Click Create work order.
4. Specify the name, earliest start date, due date, and description.
5. Click Create. 
 SystemLink Enterprise opens the work order you
 created.
6. Optional: 
 Update the state of the work order.
7. Optional: 
 Assign the work order to lab personnel.
8. Optional: 
 To add files to your work order, click Files»Upload files.

After creating a work order, you can add
 work items. Use these work items to track events such as test planning, maintenance, and
 calibration.

Parent topic:

Managing Work Orders and Work Items

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-custom-script-analyzing-param-data.html language=enus -->
## TOPIC 00041: Creating a Custom Script for Analyzing Parametric Data

- bundle_id: `systemlink-enterprise`
- source_path: `creating-custom-script-analyzing-param-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-custom-script-analyzing-param-data.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify the default Jupyter Notebook, Data Space Analysis, to meet your parametric data analysis needs. Introduced in December 2024 For more information on performing a data space analysis using different APIs, refer to the ni_data_space_analyzer Python library in the How_to_use_ni_data_space_analyze

### Creating a Custom Script for Analyzing
 Parametric Data

Modify the default Jupyter Notebook, *Data Space Analysis*, to meet
 your parametric data analysis needs.

Introduced in December 2024

Note

ni_data_space_analyzer

How_to_use_ni_data_space_analyzer’

Data Space
 Analysis

Data_Space_Default_Analysis.ipynb

1. Navigate to Analysis»Scripts.
2. Right-click the notebook and rename it.
3. To include the custom analyses, update the metadata of the notebook parameters
 . For example, add custom_analysis_scalar and
 custom_analysis_vector. 
 {
 "papermill": {
 "parameters": {
 "trace_data": "",
 "workspace_id": "",
 "analysis_options": []
 }
 },
 "systemlink": {
 "outputs": [
 {
 "display_name": "Custom Analysis Scalar",
 "id": "custom_analysis_scalar",
 "type": "scalar"
 },
 {
 "display_name": "Custom Analysis Vector",
 "id": "custom_analysis_vector",
 "type": "vector"
 }
 ],
 "parameters": [
 {
 "display_name": "Trace Data",
 "id": "trace_data",
 "type": "string"
 },
 {
 "display_name": "Analysis Options",
 "id": "analysis_options",
 "type": "string[]"
 }
 ]
 },
 "tags": ["parameters"]
}
4. Update the list of analyses supported by the notebook and specify their
 output. 
 supported_analysis = [
 {"id": "custom_analysis_scalar", "type": "scalar"},
 {"id": "custom_analysis_vector", "type": "vector"}
]
supported_analysis_options = list(map(lambda x: x["id"], supported_analysis))
5. Add functions that compute the custom analysis and add the results to the
 original data frame. 
 def compute_custom_analysis_scalar(dataframe):
 analysis_result = perform_custom_analysis_scalar(dataframe)
 dataframe["custom_analysis_scalar"] = float(analysis_result)

def def compute_custom_analysis_vector(dataframe):
 analysis_result = perform_custom_analysis_vector(dataframe)
 dataframe["custom_analysis_vector"] = list(analysis_result)
6. Perform an analysis for individual traces. 
 def perform_analysis(data_frame: pd.DataFrame) -> pd.DataFrame:
 data_space_analyzer = DataSpaceAnalyzer(dataframe=data_frame)
 for option in analysis_options:
 elif option == "custom_analysis_scalar":
 compute_custom_analysis_scalar(data_frame)
 elif option == "custom_analysis_vector":
 compute_custom_analysis_vector(data_frame)
 return data_space_analyzer.generate_analysis_output(analysis_options=analysis_options,supported_analysis=supported_analysis
7. Consolidate the results and save those results as an artifact. 
 data_space_analyzer = DataSpaceAnalyzer(pd.DataFrame()) 
 final_result = []
 traces = data_space_analyzer.load_dataset(trace_data) 
 for trace in traces: 
 trace_name = trace["name"] 
 trace_values = trace["data"] 
 analysis_results = perform_analysis(trace_values) 
 final_result.append({"plot_label": trace_name, "data": analysis_results}) 
 output_artifact_id = data_space_analyzer.save_analysis(workspace_id, final_result)
8. Using the scrapbook library, glue the output artifact to the
 execution result. 
 sb.glue("result", output_artifact_id)
9. Save the notebook.
10. Publish the notebook to SystemLink Enterprise under the
 Data Space Analysis interface.

After creating your custom script, use it to
 analyze parametric data in a data space.

Parent topic:

Reporting Data with Jupyter Notebooks

Related tasks:

- Analyzing Parametric Data in a Data Space
- Publishing a Jupyter Notebook

Related information:

- Data Space Analysis Notebook (GitHub)

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-marginal-plots.html language=enus -->
## TOPIC 00042: Creating Marginal Plots

- bundle_id: `systemlink-enterprise`
- source_path: `creating-marginal-plots.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-marginal-plots.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Transform your plots into marginal plots to gain additional insights into your data. In the SystemLink web application, navigate to Product Insights Data Spaces . Click the data space where you want to add a marginal plot. Click Settings. Under Marginal plot settings, enable one or more of the follo

### Creating Marginal Plots

Transform your plots into marginal plots to gain additional insights into your
 data.

1. In the SystemLink web application, navigate to Product Insights»Data Spaces.
2. Click the data space where you want to add a marginal plot.
3. Click Settings.
4. Under Marginal plot settings, enable one or more of the
 following distribution plots. 
 OptionDescriptionEnable horizontal distribution
 Add a marginal plot of the data on the x-axis.Enable vertical distribution
 Add a marginal plot of the data on the y-axis.
5. To select the type of plot you want to add for each marginal plot, use
 Plot type.
6. Optional: 
 To change the level of detail shown in a histogram, modify Bin
 granularity.
7. Optional: 
 To change the format of a histogram, modify Bar
 mode.
8. Click Save
 [IMAGE alt='Save icon' src='GUID-54AAC5CA-0EF8-41F8-AFFE-4E684F12AC94-a5.png'].
9. Optional: 
 To share your data space, copy the page URL.

Parent topic:

Interacting with Data in a Data Space

<!--NI_TOPIC bundle=systemlink-enterprise path=creating-metadata.html language=enus -->
## TOPIC 00043: Applying Custom Metadata to Systems

- bundle_id: `systemlink-enterprise`
- source_path: `creating-metadata.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/creating-metadata.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Assign properties or keywords to your systems to facilitate searching and filtering. In the SystemLink web application under Systems Management, click Systems. Select the system you want to assign a property or keyword to and click Settings. In the toolbar, click + Keyword or + Property to specify a

### Applying Custom Metadata to Systems

Assign properties or keywords to your systems to facilitate searching and filtering.

1. In the SystemLink web application under Systems
 Management, click Systems.
2. Select the system you want to assign a property or keyword to and click
 Settings.
3. In the toolbar, click + Keyword or +
 Property to specify a keyword or property for the system. 
 The following table describes different use cases for keywords and properties. Use case
 Metadata typeYou want to associate the system with a string.
 Keyword
 You want to create key-value pairs for a group of systems.
 Property
4. Click Save.

Parent topic:

Modifying the Settings of a System

<!--NI_TOPIC bundle=systemlink-enterprise path=customizing-dynamic-form-fields-configuration.html language=enus -->
## TOPIC 00044: Customizing a Dynamic Form Field Configuration

- bundle_id: `systemlink-enterprise`
- source_path: `customizing-dynamic-form-fields-configuration.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/customizing-dynamic-form-fields-configuration.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify the example Dynamic Form Fields Configuration to create a custom dynamic form fields (DFFs) configuration. Introduced in January 2025 Define the views, groups, and fields you want to create. Views appear as additional tabs in the configuration slide-out. You can aggregate fields into groups t

### Customizing a Dynamic Form Field
 Configuration

Modify the example *Dynamic Form Fields Configuration* to create a
 custom dynamic form fields (DFFs) configuration.

Introduced in January 2025

Views

groups

Before you begin, initiate your DFFs
 configuration.

1. Open your DFFs configuration file. 
 ...
 "views": [
 {
 "key": "View_Example",
 "order": "10",
 "displayText": "View Example",
 "helpText": "",
...
2. To specify the name of your custom tab, modify the displayText
 key.
3. Specify the order in which the tab appears. NI recommends the following order
 values. 
 Assign your first custom tab to order "10".
 Increment subsequent tabs by 10. For example, "20" and
 "30".Incrementing by 10 allows you to re-order tabs or insert new tabs between
 existing tabs easily.
4. Optional: 
 Modify the i18n key so you can provide a localized version of
 the tab you are adding. 
 ...
 "i18n": [
 {
 "localeId": "de",
 "displayText": "View Beispiel",
 "helpText": ""
 }
... 
 
 By default, SystemLink Enterprise shows the value for
 displayText you defined in the views key.
 SystemLink Enterprise shows the localized value for
 displayText when the following conditions are met.You define displayText in the i18n
 key.
 You set your browser language to one of the supported localized
 languages.
  1. Specify the localeId. Use one of the following
 supported values. 
 "fr" for French
 "de" for German
 "en" for English
 "ja" for Japanese
 "zh" for simplified Chinese
  2. Update displayText with the localized text.
5. Optional: 
 List the key values for the groups you plan to use to organize
 your fields on the user interface. You define these groups further down in the
 configuration file. 
 ...
 "groups": [
 "Group_1_Example",
 "Group_2_Example"
 ]
...
  1. Specify the fields that the group contains.
6. Define the groups you plan to use to organize your fields on the user
 interface. 
 ...
"groups": [
 {
 "workspace": "f58beba8-66de-4ba5-89f4-3388fd814f2e",
 "key": "Group_1_Example",
 "displayText": "Group 1 Example",
 "helpText": "",
...
  1. List the key values for the fields that the group
 contains. You define these fields further down in the configuration
 file. 
 ...
 "editable": false,
 "fields": [
 "Text_Field_Example",
 "Checkbox_Field_Example",
 "Number_Field_Example",
 "Enum_Field_Example"
 ]
...
7. Define the fields you want to add. The example configuration
 file includes one field of each type. 
 "TEXT"
 "BOOLEAN"
 "NUMBER"
 "ENUM"
 ...
 "fields": [
 {
 "workspace": "f58beba8-66de-4ba5-89f4-3388fd814f2e",
 "key": "Text_Field_Example",
 "type": "TEXT",
 "displayText": "Text Field Example",
 "helpText": "Help Text",
...
  1. Optional: 
 Delete the fields you do not want to add.
  2. Optional: 
 Duplicate the fields you want to add more of. Create a unique
 key value for any field you duplicate.
  3. Update the display text.
  4. Optional: 
 Add a i18n key so you can provide a localized version
 of each field you are adding.
8. Add requirements and validation parameters for the field. 
 ...
 }
 ],
 "editable": true,
 "mandatory": false,
 "defaultValue": null,
 "validation": {
 "minValue": 0,
 "maxValue": 10
 }
...
9. Save your updated configuration file.
10. Copy the contents of the configuration file and use the DFF API to update your
 initial configuration. 
 post_nidynamicformfields_v1_update-configurations
11. Open SystemLink Enterprise.
12. Navigate to the resource you specified in the configuration file to see your
 dynamic form fields.

Parent topic:

Adding Custom Input Fields to the User Interface

Related concepts:

- SystemLink Enterprise Examples

Related tasks:

- Publishing a Jupyter Notebook
- Configuring Dynamic Form Fields

<!--NI_TOPIC bundle=systemlink-enterprise path=data-extraction-performance-for-standard-files.html language=enus -->
## TOPIC 00045: Data Extraction Performance for Standard Files

- bundle_id: `systemlink-enterprise`
- source_path: `data-extraction-performance-for-standard-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/data-extraction-performance-for-standard-files.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn how SystemLink Enterprise performs when extracting test data from standard files. Standard files include Bench Data Connector (BDC) files and Standard Test Data Format (STDF) files. For each file type, NI tested data extraction for three test data scenarios using Notebook executions and measur

### Data Extraction Performance for Standard
 Files

Learn how SystemLink Enterprise performs when extracting test data
 from standard files.

Standard files include Bench Data Connector (BDC) files and Standard Test Data Format
 (STDF) files. For each file type, NI tested data extraction for three test data
 scenarios using Notebook executions and measured performance.

#### Testing
 Conditions for Data Extraction

NI evaluated performance under the
 following infrastructure and the following measurement conditions.

- Multiple file extractions inside single execution
- Parallel extractions
- Existing data sets

| Condition | Description | Specifications |
| --- | --- | --- |
| Execution pod | Execution pod deployed and managed by Kubernetes (AWS EKS) | Memory: 2 GB CPU: 100 m |
| Test Monitor service | Test Monitor service deployed and managed by Kubernetes (AWS EKS) | Replication: Auto scale (default: 2, maximum: 10) Node specification: Type: r6a.4x large​ vCPU: 16 RAM: 128 GiB Pod specification: CPU: 250 m Memory: 320 Mi (up to 512 Mi) |
| Test Monitor database | Test Monitor database sourced as a single instance of RDS PostgreSQL | PostgreSQL version: 14.7 Instance class: db.t4g.xlarge vCPU: 4 RAM: 16 GiB |

#### Data Extraction Performance for BDC
 Files

Bench Data Connector (BDC)

| Row type | Description |
| --- | --- |
| Column headers | The name of the column Each column header must be unique. |
| Column types | The type of data that the column contains Column type must be META, STD, COND, or INF. |
| Measurement data | The values associated with each measurement |

Bench Data Connector Logging Libraries

| Characteristic | Scenario 1: High Mix–High Volume | Scenario 2: Medium Mix–Medium Volume | Scenario 3: Low Mix–Low Volume |
| --- | --- | --- | --- |
| Scenario description | Many results with many steps | Medium results with medium steps | Few results with few steps |
| STD columns | 4 | 4 | 4 |
| COND columns | 20 | 15 | 10 |
| INF columns | 20 | 15 | 10 |
| META Columns | 16 | 16 | 16 |
| Number of results (META column combinations) | 89 | 61 | 36 |
| Number of steps (COND column combinations) | 10-890 | 10-610 | 10-360 |
| Number of measurements per step | 25 | 25 | 25 |
| Approximate total number of measurements | 1 million | 500,000 | 200,000 |

| Characteristic | Scenario 1: High Mix–High Volume | Scenario 2: Medium Mix–Medium Volume | Scenario 3: Low Mix–Low Volume |
| --- | --- | --- | --- |
| Scenario description | Many results with many steps | Medium results with medium steps | Few results with few steps |
| Average extraction time | 12 minutes 6 seconds | 4 minutes 53 seconds | 1 minute 52 seconds |
| Approximate rate of extraction per hour | 5 files | 10 files | 28 files |

#### Data
 Extraction Performance for STDF Files

*Standard Test Data Format
 (STDF)* files are binary files that store test and measurement data from
 semiconductor manufacturing and testing. Refer to the *Standard Test Data
 Format (STDF) Specification* to learn more about STDF files.

| Characteristic | Scenario 1: High Mix–Low Volume | Scenario 2: Low Mix–Very High Volume | Scenario 3: Low Mix–High Volume |
| --- | --- | --- | --- |
| Scenario description | Many results with few steps | Few results with very high steps | Few results with many steps |
| Number of results | 5,000 | 20 | 20 |
| Number of steps | 1,000 | 54,000 | 25,000 |
| Number of measurements per step | 1 | 1 | 1 |
| Approximate total number of measurements | 5 million | 1 million | 500,000 |

| Characteristic | Scenario 1: High Mix–Low Volume | Scenario 2: Low Mix–Very High Volume | Scenario 3: Low Mix–High Volume |
| --- | --- | --- | --- |
| Scenario description | Many results with few steps | Few results with very high steps | Few results with many steps |
| Average extraction time | 2 hours 22 minutes 18 seconds | 38 minutes 10 seconds | 18 minutes 10 seconds |
| Approximate rate of extraction per 10 hours | 4 files | 15 files | 33 files |

Parent topic:

Service Performance Specifications

Related information:

- Bench Data Connector Logging Libraries

<!--NI_TOPIC bundle=systemlink-enterprise path=data-frames-data-source.html language=enus -->
## TOPIC 00046: Using the Data Frames Data Source in a Dashboard

- bundle_id: `systemlink-enterprise`
- source_path: `data-frames-data-source.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/data-frames-data-source.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create dashboards using the Data Frames data source. In SystemLink Enterprise, navigate to Overview Dashboards . Click Apps icon New dashboard . Click Add visualization. In the Query tab, set the Data source to SystemLink Data Frames. Select a Query Type to view the appropriate type of data. Query T

### Using the Data Frames Data Source in a
 Dashboard

Create dashboards using the Data Frames data source.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Click [IMAGE alt='Apps icon' src='GUID-69B726A6-D4C1-451C-882A-5ED0B10972FD-a5.png']»New dashboard.
3. Click Add
 visualization.
4. In the Query tab, set the
 Data source to
 SystemLink Data
 Frames.
5. Select a Query Type to
 view the appropriate type of data. 
 Query Type
 DescriptionData
 Returns time-series data and tabular data that
 is suitable for the following visualization
 types:Time series
 Bar chart
 Table
 Histogram
 Plotly chart
 XY chartProperties
 Returns data table properties and column
 properties.
6. In the Query Configurations
 section, add filters to the following sub sections to filter
 the data to a specific data table. 
 Query by result
 properties
 Query by data table
 properties
 Query by column
 propertiesNote If the filters match more
 than 1,000 data tables, the data source only
 processes the first 1,000 data tables.
7. Based on your Query Type,
 update the configuration of the data source. 
 Query Type
 Data Table PropertiesData
 In the Columns
 drop-down, select the columns you want to
 visualize.Note You can
 select up to 20 columns.
 In the Decimation
 Settings section, select a
 Decimation method.Note To return undecimated data,
 select None. Set the
 Take value to determine the
 number of rows to return.Note The default
 Take value is
 10,000. The upper limit is
 1,000,000.
 (Optional) Specify the column of values for
 use as the x-axis when decimating the data in the
 X-column.Note The default
 value of the X-column field is the index column of
 the data table.
 (Optional) To load higher resolution data when
 zooming or panning across a chart, enable the
 Filter for x-axis range on zoom or
 pan option.Note The column you select as the X-column must match
 the x-axis of the plot.Note When you zoom or pan in one
 panel, SystemLink reflects that action in all
 other panels with the same configuration. These
 panels share the same X-column selection. The
 dashboard configuration does not save the zoomed
 or panned range.Properties
 In the Data Table
 Properties drop-down, select the data
 table properties to display.
 In the Column
 Properties drop-down, select the
 column properties to display.
 Set the Take value.Note The default
 Take value
 is 1,000. This value is also the
 maximum limit.
8. Click Save.

Note

Improving Data
 Table Metadata Query Performance

Parent topic:

Monitoring Tests

Related tasks:

- Visualizing Data Tables in a Data Space
- Visualizing Data Tables in a Dashboard

Related information:

- Grafana Dashboards
- Grafana Variables

<!--NI_TOPIC bundle=systemlink-enterprise path=deleting-specifications.html language=enus -->
## TOPIC 00047: Deleting Specifications

- bundle_id: `systemlink-enterprise`
- source_path: `deleting-specifications.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/deleting-specifications.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Remove one or more specifications from a product. Navigate to Product Insights Products . Click the product containing the specification you want to delete. Click the Specs tab. Select one or more specifications you want to delete and click Delete.

### Deleting Specifications

Remove one or more specifications from a product.

1. Navigate to Product Insights»Products.
2. Click the product containing the specification you want to delete.
3. Click the Specs tab.
4. Select one or more specifications you want to delete and click
 Delete.

Parent topic:

Specification Compliance

Related tasks:

- Creating and Editing Product Specifications through SystemLink
- Viewing Product Specifications
- Creating, Viewing, and Managing Specification Conditions

<!--NI_TOPIC bundle=systemlink-enterprise path=displaying-metadata-of-system.html language=enus -->
## TOPIC 00048: Visualizing Metadata of a System

- bundle_id: `systemlink-enterprise`
- source_path: `displaying-metadata-of-system.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/displaying-metadata-of-system.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Display and modify the metadata, such as the name, IP address, or model, associated with your system so you can interact with data more efficiently. Configure the Systems Management details in the SystemLink web application to display systems information you care about. In the SystemLink web applica

### Visualizing Metadata of a System

Display and modify the metadata, such as the name, IP address, or model, associated with
 your system so you can interact with data more efficiently.

Configure the Systems Management details
 in the SystemLink web application to display systems information you care about.

1. In the SystemLink web application under Systems
 Management, click Systems.
2. Select a system and click View.
3. In the details ribbon, click Edit [IMAGE alt='Edit icon (pencil).' src='GUID-AF0C5C1B-16A8-446A-B16D-39EF3338571B-a5.png'].
4. Click ADD to view additional properties you can add.
5. Click and drag properties to reorder them.
6. Click OK.

Parent topic:

Managing Your Systems

<!--NI_TOPIC bundle=systemlink-enterprise path=editing-test-result-keywords-from-a-data-space.html language=enus -->
## TOPIC 00049: Annotating Test Results or Steps with Keywords from a Data Space

- bundle_id: `systemlink-enterprise`
- source_path: `editing-test-result-keywords-from-a-data-space.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/editing-test-result-keywords-from-a-data-space.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Add, remove, and modify result keywords or step keywords from a data space. You can also exclude results or steps from a data space using a keyword. Before you begin, create a visualization of your parametric data. In the SystemLink web application, navigate to Product Insights Data Spaces . Open th

### Annotating Test Results or Steps with Keywords
 from a Data Space

Add, remove, and modify result keywords or step keywords from a data space. You can also
 exclude results or steps from a data space using a keyword.

Before you begin, create a visualization of
 your parametric data.

1. In the SystemLink web application, navigate to Product Insights»Data Spaces.
2. Open the data space that contains the results or steps you want to edit.
3. In the Plot type drop-down menu, select
 Scatter.
4. Select one or more points on the plot. 
 To select one point, click the point.
 To select multiple points, click Lasso Select and
 draw a shape around the points.
5. To add keywords to results, click Edit»Edit results in the toolbar.
  1. Use the Edit result slide-out to add, remove, or
 edit keywords for the results you selected. 
 To add a keyword, click Add keyword.
 To remove a keyword, click [IMAGE alt='Remove icon.' src='GUID-D33CA224-5327-4C1E-A6B8-026795B53DFE-a5.png'] next to the keyword.
 To edit a keyword, click the keyword.
  2. To exclude the results with a certain keyword,
 enable Exclude the selected results from the data
 space. 
 SystemLink updates the query for the data space.
6. To add keywords to steps, click Edit»Edit steps in the toolbar.
  1. Use the Edit steps slide-out to add, remove, or
 edit keywords for the steps you selected. 
 To add a keyword, click Add keyword.
 To remove a keyword, click [IMAGE alt='Remove icon.' src='GUID-D33CA224-5327-4C1E-A6B8-026795B53DFE-a5.png'] next to the keyword.
 To edit a keyword, click the keyword.
  2. To exclude the steps with a certain keyword,
 enable Exclude the selected steps from the data
 space. 
 SystemLink updates the query for the data space.
7. Click Save.

Parent topic:

Interacting with Data in a Data Space

Related tasks:

- Plotting Parametric Data in a Data Space

<!--NI_TOPIC bundle=systemlink-enterprise path=extracting-data-from-files-with-jupyter-notebooks.html language=enus -->
## TOPIC 00050: Extracting Data from Files with Jupyter Notebooks

- bundle_id: `systemlink-enterprise`
- source_path: `extracting-data-from-files-with-jupyter-notebooks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/extracting-data-from-files-with-jupyter-notebooks.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Extract data from files in SystemLink using Jupyter notebooks. Refer to the SystemLink Enterprise examples on GitHub for an example notebook. Navigate to Product Insights Products . To open the details page, click a product. Click the Files tab. Select one or more files, expand the Analyze drop-down

### Extracting Data from Files with Jupyter
 Notebooks

Extract data from files in SystemLink using Jupyter notebooks.

SystemLink Enterprise

1. Navigate to Product Insights»Products.
2. To open the details page, click a product.
3. Click the Files tab.
4. Select one or more files, expand the Analyze drop-down,
 and select Extract. 
 Note You can extract up to 50
 files at a time. You can also extract files during an upload.
5. Select the notebook you want to run on the files. 
 Note If you do not see the
 notebook you are looking for, ensure that you published the notebook to a
 workspace you can access. Additionally, ensure that you set the interface
 for the notebook to Test data extraction.
6. Set a limit for how long the notebook can execute before timing out.
7. Click Extract.
8. To see the latest execution time and status, navigate to the
 Files tab. 
 Note SystemLink Enterprise preserves up to 16 MB of notebook
 execution data for 7 days. If you must retain more data for longer, ensure
 your notebook saves and uploads your data to SystemLink.
9. To view more execution details, select a file, click
 Analyze, and select View latest execution
 details.
10. To see the extracted results, navigate to the Results
 tab.

Parent topic:

Reporting Data with Jupyter Notebooks

Related information:

- SystemLink Examples on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=file-formats-supported-in-file-preview.html language=enus -->
## TOPIC 00051: File Formats Supported in File Preview

- bundle_id: `systemlink-enterprise`
- source_path: `file-formats-supported-in-file-preview.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/file-formats-supported-in-file-preview.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: SystemLink Enterprise allows you to preview various file formats. Limitations on File PreviewThe file preview only supports files with a file size of less than 250 MB. Tests on the Monaco editor (an editor for previewing text files) use a large file containing 400,000 lines. Each line has 100 words.

### File Formats Supported in File
 Preview

SystemLink Enterprise allows you to preview various file
 formats.

#### Limitations on File Preview

Note

- The table format displays the first 10,000 rows and first 200 columns.
- The text format displays all content.

Webpage files, such as .html and
 .shtml, render as a webpage in the preview and not as
 text.

#### Media
 Files

Note

SystemLink Enterprise

| Format | Description |
| --- | --- |
| .bmp | Bitmap |
| .gif | Graphics Interchange Format, an image format for animations |
| .ico | Icon, an image format for computer icons |
| .jpeg | Joint Photographic Experts Group |
| .jpg | Joint Photographic Experts Group |
| .png | Portable Network Graphics, an image format that supports transparency |
| .svg | Scalable Vector Graphics, for vector-based images |
| .tiff | Tagged Image File Format, for high-quality images |
| .webp | WebP, an image format developed by Google with lossy and lossless compression. |

| Format | Description |
| --- | --- |
| .aac | Advanced Audio Coding, a lossy audio compression format |
| .aiff | Audio Interchange File Format, a lossless audio format |
| .flac | Free Lossless Audio Codec, a lossless audio compression format |
| .mp3 | MP3, a lossy audio format |
| .ogg | Ogg Vorbis, an open source audio format |
| .wav | Waveform Audio File Format, uncompressed audio format |

| Format | Description |
| --- | --- |
| .avi | Audio Video Interleave |
| .mkv | Matroska Video, a flexible open-source format |
| .mov | QuickTime Movie |
| .mp4 | MPEG-4 Part 14 |
| .ogg | Ogg, an open-source container format for video and audio |
| .ogv | Ogg Video, a video format with open-source codecs |
| .webm | WebM, a web-optimized video format |
| .wmv | Windows Media Video, a Microsoft video format |

#### Text Files

| Format | Description |
| --- | --- |
| .asp | Active Server Pages file for dynamic web content |
| .aspx | Active Server Pages Extended file |
| .babelrc | Babel configuration file |
| .bash | Bash script file for Linux and macOS |
| .bat | Windows Batch script file |
| .bowerrc | Bower configuration file |
| .c | C programming language source code |
| .cjs | CommonJS module file |
| .cmd | Windows command script file |
| .config | Configuration file for application settings |
| .cpp | C++ source code file |
| .cshtml | C# HTML file for Razor views |
| .csproj | C# project file |
| .css | Cascading Style Sheets |
| .dockerfile | Dockerfile for building Docker images |
| .es6 | JavaScript file with ES6 syntax |
| .eslintrc | ESLint configuration file |
| .gitconfig | Git configuration file |
| .go | Go programming language source code |
| .gql | GraphQL query file |
| .graphql | GraphQL schema or query file |
| .h | C header file |
| .ini | Configuration file for software settings |
| .jav | Older Java source code file |
| .java | Java source code file |
| .jl | Julia source code file |
| .js | JavaScript file |
| .jscsrc | JSCS configuration file |
| .jshintrc | JSHint configuration file |
| .jshtm | JavaScript HTML file |
| .json | JavaScript Object Notation file |
| .jsp | JavaServer Pages file for dynamic web pages |
| .jsx | JavaScript file with JSX syntax |
| .kt | Kotlin source code file |
| .kts | Kotlin script file |
| .less | Less CSS preprocessor file |
| .markdown | Markdown file |
| .md | Markdown file |
| .mdoc | Unix system main page documentation |
| .mdx | Markdown Extended file with JSX |
| .mjs | JavaScript module file |
| .pdf | Portable Document Format |
| .php | PHP script file |
| .php4 | Older PHP script file, version 4 |
| .php5 | Older PHP script file, version 5 |
| .phtml | PHP file with embedded HTML |
| .properties | Configuration file for Java applications |
| .props | MSBuild property file for build settings |
| .py | Python source code file |
| .r | R programming language source code |
| .rb | Ruby source code file |
| .rbx | Roblox script file |
| .redis | Redis configuration file |
| .rhistory | R command history file |
| .rjs | Ruby JavaScript file for Rails |
| .rmd | R Markdown file |
| .rprofile | R profile file for environment settings |
| .rst | ReStructuredText file for documentation |
| .rt | R template file for report generation |
| .sb | Smalltalk source code file |
| .sc | Smalltalk class file |
| .scala | Scala source code file |
| .scss | Sassy CSS file for advanced styling |
| .sh | Shell script file for Unix-like shells |
| .sv | SystemVerilog file for hardware design |
| .svg | Scalable Vector Graphics file |
| .svgz | Compressed Scalable Vector Graphics file |
| .svh | SystemVerilog header file |
| .swift | Swift source code file for iOS and macOS |
| .txt | Plain text file |
| .xaml | Extensible Application Markup Language file |
| .xhtml | Extensible Hypertext Markup Language file |
| .xml | Extensible Markup Language file |
| .yaml | YAML file for data serialization |
| .yml | YAML file for data serialization |

Parent topic:

Storing and Managing Files

<!--NI_TOPIC bundle=systemlink-enterprise path=filtering-and-sorting-test-results.html language=enus -->
## TOPIC 00052: Filtering and Sorting Test Results by Custom Properties

- bundle_id: `systemlink-enterprise`
- source_path: `filtering-and-sorting-test-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/filtering-and-sorting-test-results.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Query test results to gain specific insights about your test data. The Results grid has the same capabilities as other grids as described in Filtering Grids. The following steps are specific to the Results grid. Navigate to Product Insights Test Results . Click Filter . On the Query tab, expand the

### Filtering and Sorting Test Results by Custom
 Properties

Query test results to gain specific insights about your test data.

Results

Filtering Grids

Results

1. Navigate to Product Insights»Test Results.
2. Click [IMAGE alt='Filter' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'].
3. On the Query tab, expand the Property
 drop-down and select Properties. 
 Note The following table describes how
 operators behave for custom properties.Operator
 Behaviormatches
 Matches results where the value of the property key equals the specified
 value.
 does not match
 Matches results where the value of the property key does not equal the
 specified value.
 contains
 Matches all results where the property key equals the specified key if you
 specify only a key.
 Matches results where the value of the property key contains the specified
 value if you specify both a key and a value.
 does not contain
 Matches all results where the property key does not equal the specified key
 if you specify only a key.
 Matches results where the value of the property key does not contain the
 specified value if you specify both a key and a value.
 numeric
 Matches results where the value of the property key expressed as a
 numeric value evaluates to true when compared to the value specified. For
 example, > (numeric) converts the value of the
 property key to a numeric value matches results where that value is greater
 than the value specified.Note If the value cannot be converted to a numeric value, it will not match the
 filter.
4. Select the Sort tab.
5. To sort by a custom property, enter the name of the property key in Sort
 by. 
 Note By default, the sorting uses the
 default comparison for the field data type. For example, string-type fields sort
 alphabetically. However, you can also sort the following string-type fields
 numerically.Part number
 Serial number
 Started
 Updated
 Elapsed time
 Custom propertiesTo sort these fields numerically, use Ascending (Numeric)
 or Descending (Numeric) as the sort direction.Values
 that cannot be converted to numeric values are converted to null and
 sorted as the smallest values.
6. Click OK.
7. To better display and sort custom properties that represent numeric data in the grid,
 complete the following steps.
  1. Click [IMAGE alt='Numeric Format button.' src='GUID-116D9367-1613-4644-B25F-ECBEAB894A5D-a5.png'].
  2. Add a column for the custom property.
  3. Expand the drop-down next to the property name.
  4. Select Numeric.

Parent topic:

Monitoring Tests

Related tasks:

- Filtering Grids

<!--NI_TOPIC bundle=systemlink-enterprise path=generating-custom-alarms.html language=enus -->
## TOPIC 00053: Generating Custom Alarms

- bundle_id: `systemlink-enterprise`
- source_path: `generating-custom-alarms.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/generating-custom-alarms.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create alarms from a LabVIEW VI to notify you of system issues. Introduced in June 2024 Alarms help you implement rules and manage conditions that affect your systems, tests, or assets.To generate alarms based on tag value conditions, refer to Monitoring System Health with Alarms. What to Use You ca

### Generating Custom Alarms

Create alarms from a LabVIEW VI to notify you of system issues.

Introduced in June 2024

Note

Monitoring System Health with Alarms

#### What to Use

You can find the SystemLink Alarm and Utilities APIs on the Data Communication palette in
 LabVIEW.

#### What to Do

1. On the client, create the following diagram in a VI. [IMAGE alt='LabVIEW block diagram that computes deadband and creates a SystemLink alarm when DC value is above normal.' src='GUID-88D0E435-68B6-40A9-9CED-9A435EF77CF3-a5.png']
2. Customize the gray sections for your unique programming goals.

| 1 | Get System Name obtains the name of the system you want to monitor. |
| --- | --- |
| 2 | Build Alarm Set Transition creates a set transition parameter. The set transition parameter describes the state and the severity level of the alarm instance that triggers a notification. |
| 3 | Set Alarm triggers an alarm instance on the server. If Set Alarm has a notification strategy wired to it, the VI sends a notification to subscribers if one of the following conditions is true. The alarm instance is new. The alarm instance reaches a new severity level. The subscriber then verifies and fixes the issue before acknowledging the alarm. When the state of the alarm is below the defined alarm threshold, the application clears the alarm with Clear Alarm. |

#### Troubleshooting

- If Set Alarm only returns True the first time you
 set an alarm and then always returns False , check whether you or
 another operator acknowledged the alarm. If you or another operator did not acknowledge
 the alarm, the alarm remains active.
- If you specify a notification strategy but do not receive a notification, verify the
 following things.
  - The alarm is new or has reached a new severity. A notification is only sent when
 one of the following conditions is true.
    - The alarm instance is new.
    - The alarm instance reaches a new severity level. In the following example, the
 asterisk (*) indicates a transition of the alarm instance where you receive a
 notification.
      - Severity 1 (*)
      - Severity 2 (*)
      - Severity 3 (*)
      - Severity 2
      - Severity 4 (*)
      - Severity 3
      - Severity 4
      - Severity 5 (*)
  - You have configured email notifications in SystemLink Enterprise .

#### Examples

- Alarms

Parent topic:

Sharing Data across Systems

Related tasks:

- Monitoring System Health with Alarms

<!--NI_TOPIC bundle=systemlink-enterprise path=generating-system-configuration-reports.html language=enus -->
## TOPIC 00054: Generating System Configuration Reports

- bundle_id: `systemlink-enterprise`
- source_path: `generating-system-configuration-reports.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/generating-system-configuration-reports.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Generate reports on managed software and connected assets on a system. In the SystemLink web application, click System Management Systems . Select one or more systems and click Download. Select the report that best meets your goals. Software report Generates a report on what managed software is inst

### Generating System Configuration
 Reports

Generate reports on managed software and connected assets on a system.

1. In the SystemLink web application, click System Management»Systems.
2. Select one or more systems and click Download.
3. Select the report that best meets your goals. 
 OptionDescriptionSoftware report
 Generates a report on what managed software is installed.System report
 Generates a report on currently connected assets.

Parent topic:

Managing Your Systems

<!--NI_TOPIC bundle=systemlink-enterprise path=host-feed-and-package.html language=enus -->
## TOPIC 00055: Hosting Feeds and Packages in SystemLink

- bundle_id: `systemlink-enterprise`
- source_path: `host-feed-and-package.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/host-feed-and-package.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemLink Feeds organize, host, and manage software packages for Windows and NI LinuxRT deployments. Use the SystemLink Feeds application to organize and host your software packages. Open the navigation menu. Expand the Systems Management section. Select Feeds. Creating SystemLink Packages Create p

### Hosting Feeds and Packages in
 SystemLink

SystemLink Feeds organize, host, and manage software packages for Windows and NI
 LinuxRT deployments.

Use the SystemLink Feeds application to organize and host your software packages.

1. Open the navigation menu.
2. Expand the Systems Management section.
3. Select Feeds .

Parent topic:

Managing Your Software

#### Creating SystemLink Packages

Create packages for LabVIEW projects, TestStand sequences, and other NI
 software.

Depending on your goal, create a package through NI Package
 Manager, NI Package Builder, or
 LabVIEW Application Builder.

| Goal | Software | Details |
| --- | --- | --- |
| Create a package from a specific directory on your computer. | NI Package Manager | For more information, refer to Package Creation in the NI Package Manager user manual. |
| Create a package from a LabVIEW project. | LabVIEW Application Builder | For more information, refer to Creating Packages for Distribution in the LabVIEW user manual. |
| Create and publish complex package-based deployments. | NI Package Builder | For more information, refer to Creating a New Package in the NI Package Builder user manual. |
| Create a package from a TestStand sequence. | NI Package Builder | For more information, refer to Including TestStand Sequence Files and Workspaces in the NI Package Builder user manual. |

Related information:

- Package Creation
- Creating Packages for Distribution
- Creating a New Package
- Including TestStand Sequence Files and Workspaces

#### Creating SystemLink Feeds

Create or replicate SystemLink software feeds within a workspace for supported
 platform packages.

- A workspace to manage user access.
- A unique feed name within that workspace.
- A supported platform for the packages to install upon. Note SystemLink supports the
 Windows platform and the NI LinuxRT
 platform.

Each feed contains a unique copy of a package. Uploading a package to multiple
 feeds results in SystemLink hosting independent copies of that package in
 storage.

Use the following workflows to create a new feed or copy an existing feed.

| Workflow | Steps |
| --- | --- |
| Create a new feed | Create a new feed and upload your packages to that feed. Open the Feeds application. Click Create Feed to open the Create feed slide out. Enter a name for the new feed. The name must contain only alpha-numeric characters and be unique in the selected workspace. Enter a description for your new feed. Specify a workspace that uses the Create Feed privilege. By default, users with the Systems Maintainer role have this privilege. Select the platform for the feed. Click Create. On the Feed details page that opens, add packages in the feed. |
| Replicate a remote feed | Create a copy of a feed hosted on a remote URL. Use this method when a system does not have access to an external network, but SystemLink does. Open the Feeds application. Open the split menu of the Create feed button and select Replicate feed. Use the Replicate feed wizard to copy and alter a feed based on a URL. Click Replicate. On the Feed details page that opens, add packages in the feed. Note Network conditions and package sizes can slow the replication process. The Packages table populates as SystemLink processes each package. |
| Replicate a feed from ni.com | Create a copy of a feed hosted on ni.com/downloads. Use this method when a system does not have access to an external network, but SystemLink does. Open the Feeds application. Open the split menu of the Create feed button and select Replicate feed. In the Replicate feed wizard, select NI downloads. Use the Replicate feed wizard to locate, copy, and alter a feed from ni.com.Note You can replicate individual feeds in a software suite. For example, in a LabVIEW bundle, you can choose to only replicate the LabVIEW feed. On the Feed details page that opens, add packages in the feed. Note Network conditions and package sizes can slow the replication process. The Packages table populates as SystemLink processes each package. |
| Duplicate an existing feed | Create a copy of an existing feed hosted by SystemLink. Use this method to create a feed to host packages for users in other workspaces. Note Changes to the metadata or packages of a duplicate feed do not affect the original feed. Open the Feeds application. Select a feed to duplicate. Note Use the search function in the menu bar to find a feed using the name or other metadata. In the menu bar, click Duplicate to open the Duplicate feed slide out. Enter a new name for the duplicate feed. Enter a description or change the accessible workspace. Click Duplicate. On the Feed details page that opens, add or remove packages from the feed. |

#### Adding and Removing Packages in a SystemLink
 Feed

Manage packages in a SystemLink by adding packages, deleting packages from
 storage, updating package versions, and cleaning older feeds.

After creating a feed, you can add or remove packages from that feed.

1. On the main Feeds page, select a feed in the
 table. Note Use the search function in
 the menu bar to find a feed using the name or other
 metadata.
2. Click View to access the feed details page.
3. Modify the packages in the feed using the following workflows.

| Workflow | Steps |
| --- | --- |
| Add a package | From the feed details page, click Add packages. In the dialog box, click Upload to add one or more packages from your computer. Note Uploading the same package to multiple feeds creates duplicate copies of the package. |
| Remove a package | From the feed details page, select a package to remove. Click Delete to remove the package from the feed and from SystemLink storage. |
| Update packages | From the feed details page, open the Additional Actions menu and select Update.Note For replicated feeds, this action checks the package source for available versions. SystemLink adds any new package versions to the feed. |
| Remove old versions of packages | Reduce the storage footprint and remove unwanted older versions of packages from a feed.Note This operation only keeps the newest version of each package with a unique name in the feed. Navigate to the Details page of the feed. Open the Additional Actions menu. Select Clean. SystemLink does not check the dependency list of each package. Do not select this option if you are unsure if newer packages link to older dependencies.After running the Clean operation, use the Update workflow or Add Package workflow to remedy any issues. |

<!--NI_TOPIC bundle=systemlink-enterprise path=hosting-a-web-application.html language=enus -->
## TOPIC 00056: Hosting a Web Application

- bundle_id: `systemlink-enterprise`
- source_path: `hosting-a-web-application.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/hosting-a-web-application.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Host a web application in SystemLink Enterprise and share it with other users. Introduced in January 2025 SystemLink Enterprise supports NI package (.nipkg) files for web applications. To upload a web application, you must have web application permissions. Before you begin, create and package your w

### Hosting a Web Application

Host a web application in SystemLink Enterprise and share
 it with other users.

Introduced in January 2025

SystemLink Enterprise

.nipkg

- Create and package your application using G Web Development Software.
- Create your application using your preferred software. Package your application with NI
 Package Builder. When using NI Package Builder, configure the package to install your web
 application files on your local computer.

1. Navigate to Overview»Web Apps.
2. Click Upload web app.
3. Specify the name of your web application. The name is a component of the web
 application URL. 
 SystemLink Enterprise updates the Published
 URL field with the name of your application.
4. Select the workspace where you want to make your web application available. The
 workspace is a component of the web application URL. 
 SystemLink Enterprise updates the Published
 URL field with the workspace you selected.
5. Browse to your .nipkg file.
6. Click Upload.
7. On the Web Apps page, select the application you uploaded and
 click View. To see the application you uploaded, complete the
 following steps. 
 SystemLink Enterprise opens your web application.
8. Navigate back to Overview»Web Apps and complete the steps that align with your goal. 
 OptionDescriptionEdit a web application.
 Select a web application.
 Click Edit and make your changes.Delete one or more web applications.
 Select one or more web applications.
 Click Delete.Share a link to a web application.
 Select a web application.
 Click Copy link.SystemLink Enterprise copies the URL for your web application
 to your clipboard.

Users who have WebVI permissions can
 interact with the WebVI you uploaded.

Parent topic:

Sharing Data across Systems

Related information:

- Developing a Web Application with G Web Development
 Software
- Packaging an Application with G Web Development
 Software
- Creating a New Package in NI Package Builder

<!--NI_TOPIC bundle=systemlink-enterprise path=improving-data-table-metadata-query-performance.html language=enus -->
## TOPIC 00057: Improving Data Table Metadata Query Performance

- bundle_id: `systemlink-enterprise`
- source_path: `improving-data-table-metadata-query-performance.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/improving-data-table-metadata-query-performance.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Construct performant queries and configure MongoDB to process queries as efficiently as possible. Data table metadata queries in the DataFrame Service make heavy use of MongoDB. These queries can run slowly or time out for a variety of reasons. Poorly constructed queries degrade the performance of t

### Improving Data Table Metadata Query
 Performance

Construct performant queries and configure MongoDB to process queries as efficiently as
 possible.

Data table metadata queries in the DataFrame Service make heavy use of MongoDB. These queries can
 run slowly or time out for a variety of reasons.

Poorly constructed queries degrade the performance of the DataFrame Service. This
 degradation can also affect the services that are connected to the same
 MongoDB instance as the DataFrame Service.

Parent topic:

Monitoring Tests

#### Creating Efficient DataFrame Service
 Queries

Follow certain guidelines when constructing a performant query for the DataFrame
 Service.

| Guideline | Description |
| --- | --- |
| Include a clause that adds an equality filter on a high cardinality indexed field inside all query clauses.Note A high cardinality indexed field contains mostly unique values. | These clauses enable the database to efficiently reduce the query search space to a small number of database entries.Example clauses include the TestResultId field or any high-cardinality field with a configured index. Note By default, SystemLink indexes the TestResultId field and Id field.The clause should also include one of the following filters: A simple equality filter on the high cardinality indexed field. A filter that checks if the field is equal to one of several values. |
| Order all results by the RowsModifiedAt field. | The indexes created by the DataFrame Service support efficient ordering by RowsModifiedAt. Ordering by other fields requires an expensive in-memory sort in the database. |

<!--NI_TOPIC bundle=systemlink-enterprise path=initiating-dynamic-form-field-configuration.html language=enus -->
## TOPIC 00058: Configuring Dynamic Form Fields

- bundle_id: `systemlink-enterprise`
- source_path: `initiating-dynamic-form-field-configuration.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/initiating-dynamic-form-field-configuration.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the example Dynamic Form Fields Configuration and the Dynamic Form Fields (DFFs) API to as a starting point for your custom configuration. Introduced in January 2025 Download the example Dynamic Form Fields Configuration (DynamicFormFieldConfigurationExample.json) from GitHub. Open the file. { "

### Configuring Dynamic Form Fields

Use the example *Dynamic Form Fields Configuration* and the Dynamic Form
 Fields (DFFs) API to as a starting point for your custom configuration.

Introduced in January 2025

1. Download the example *Dynamic Form Fields Configuration*
 (DynamicFormFieldConfigurationExample.json) from
 GitHub.
2. Open the file. 
 {
 "configurations": [
 {
 "workspace": "f58beba8-66de-4ba5-89f4-3388fd814f2e",
 "resourceType": "workitem:workitem",
 "name": "Configuration Example",
 "displayRule": "properties['name']=='Test'",
...
3. For the workspace, specify the workspace ID where you want the
 form fields to be available. 
 Note You must update each instance of the
 workspace value in the configuration file.
4. For the resourceType, specify the resource where you want the
 form fields to be available. 
 Choose from the following configurations. 
 ResourceConfigurationAssets
 "resourceType": "asset:asset"Files
 "resourceType": "file:file"Locations
 "resourceType": "location:location"Products
 "resourceType": "testmonitor:product"Results
 "resourceType": "testmonitor:result"Systems
 "resourceType": "system:system"Work Items
 "resourceType": "workitem:workitem"Note To specify the type of work item, use
 type == "<work item type>" in the display
 rule. SystemLink Enterprise supports the following
 work item types: "testplan",
 "maintenance", "calibration",
 "reservation", and
 "job".Work Orders
 "resourceType": "workorder:workorder"
5. Optional: 
 Change the name of the configuration.
6. To control the conditions under which the fields are visible, modify the
 displayRule value. 
 "displayRule": "name.includes('NI') && (properties['Location'] == 'Austin' || 'Austin' in keywords)"
7. Save the configuration file.
8. Copy the contents of the configuration file and use the DFFs API to post your
 updated configuration. 
 POST <server_api_url>/nidynamicformfields/v1/update-configurations 
 The API responds with a copy of your configuration that includes a
 configuration ID.
9. Copy the contents of the API response.
10. Replace the contents of your configuration file with the API response.
11. Save the configuration file.
12. Open SystemLink Enterprise.
13. Navigate to the resource you specified in the configuration file to see your
 custom fields.

Customize the fields in your DFFs
 configuration.

Parent topic:

Adding Custom Input Fields to the User Interface

Related concepts:

- SystemLink Enterprise Examples

Related tasks:

- Customizing a Dynamic Form Field Configuration
- Publishing a Jupyter Notebook

<!--NI_TOPIC bundle=systemlink-enterprise path=installing-python-modules.html language=enus -->
## TOPIC 00059: Installing Additional Python Modules

- bundle_id: `systemlink-enterprise`
- source_path: `installing-python-modules.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/installing-python-modules.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use third-party Python modules to customize your test reports. Include the following code in a cell at the top of your Jupyter notebook. !pip install <package-name> Where package-name is the name of the package in PyPI you want to install. Every time the notebook runs, the package installs on the co

### Installing Additional Python Modules

Use third-party Python modules to customize your test reports.

Include the following code in a cell at the top of your Jupyter notebook.

```text
!pip install <package-name>
```

Where package-name is the name of the package in PyPI you want to
 install.

Every time the notebook runs, the package installs on the container that
 includes the notebook.

For information on how to use a specific Python module,
 refer to the documentation for the module you install.

Parent topic:

Reporting Data with Jupyter Notebooks

<!--NI_TOPIC bundle=systemlink-enterprise path=integrating-with-teststand.html language=enus -->
## TOPIC 00060: Connecting SystemLink with TestStand

- bundle_id: `systemlink-enterprise`
- source_path: `integrating-with-teststand.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/integrating-with-teststand.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Send test metadata from TestStand to SystemLink Enterprise. Before you begin, install the following software on the system you want to send test reports from. TestStand 2014 or later SystemLink Client Installing SystemLink Client automatically installs the Test Monitor Client plug-in for TestStand.

### Connecting SystemLink with TestStand

Send test metadata from TestStand to SystemLink Enterprise.

- TestStand 2014 or later
- SystemLink Client

Installing SystemLink Client
 automatically installs the Test Monitor Client plug-in for TestStand.

1. In TestStand, navigate to Configure»Result Processing.
2. Enable the Test Monitor Client plug-in for SystemLink. 
 Note If you do not see the plug-in under
 Result Processing, complete the following steps.Select Show More Options.
 Click Insert New[IMAGE alt='Insert New icon (blue plus).' src='GUID-2634C82C-B433-4184-A772-6587825E68EE-a5.png'].
 Select the plug-in.
 [IMAGE alt='TestStand Result Processing dialog showing NI SystemLink Test Monitor Client selected.' src='GUID-5ED6C877-9BBB-49FA-BB33-00529ED3E2D5-a5.png']
 Tip Click Options
 [IMAGE alt='Options button icon (wrench and screwdriver).' src='GUID-A0F49F02-CE84-4AA9-8532-C76914258CA8-a5.png'] to configure the NI SystemLink Test Monitor Client plug-in. You
 can enable a variety of reporting options, such as storing test data on the
 client.
3. Open the SystemLink Enterprise web application and navigate to Product Insights»Test Results. 
 The Test Results grid displays the most recent test
 results and their status in real time.
4. Send test reports from TestStand to SystemLink and download the reports from the
 SystemLink web application.
  1. In TestStand, click Configure»Result Processing.
  2. In Report, click Options [IMAGE alt='Options button icon (wrench and screwdriver).' src='GUID-A0F49F02-CE84-4AA9-8532-C76914258CA8-a5.png'].
  3. In the Report Format drop-down, select HTML
 Document and click OK.
  4. Run the test sequence. 
 Note You can run tests
 sequentially or in parallel. TestStand automatically creates all necessary tags to
 monitor values for each instance of the test sequence. You can view these tags in
 the SystemLink web application under Tags.
  5. In the SystemLink web application, navigate to Product Insights»Test Results.
  6. Select the test and then click Download Attachments.

You can view any files uploaded from TestStand in Files. If the file
 is a TDMS file, you can select the file and click Preview to view
 additional information.

Tip

Test Monitor does not consider steps that have children. This method avoids duplicate
 reporting of sub-sequences when aggregating the following.

- The status summary.
- The pass rate for a test result.

Ensure that TestStand sequences only report a success when all child steps succeed.
 Otherwise the sequence might report a failure with a 100% pass rate.

Parent topic:

Monitoring Tests

Related tasks:

- Storing and Forwarding Test Data

<!--NI_TOPIC bundle=systemlink-enterprise path=interacting-with-data-in-a-data-space.html language=enus -->
## TOPIC 00061: Interacting with Data in a Data Space

- bundle_id: `systemlink-enterprise`
- source_path: `interacting-with-data-in-a-data-space.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/interacting-with-data-in-a-data-space.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data Spaces allow you to analyze your data using scripts and create data visualizations. Use the following documentation to complete the tasks that best suit your goals.

### Interacting with Data in a Data Space

Data Spaces allow you to analyze your data using scripts and create data
 visualizations.

Use the following documentation to complete the tasks that best suit your goals.

- [Visualizing Data Tables in a Data Space](visualizing-data-tables-in-a-data-space.html) Derive insights about data from data tables by visualizing the data in different types of plots.
- [Plotting Parametric Data in a Data Space](plotting-parametric-data.html) Derive insights about parametric test data by visualizing it in different types of charts.
- [Analyzing Parametric Data in a Data Space](analyzing-param-data-in-a-data-space.html) Derive insights about your parametric data in a data space.
- [Creating Marginal Plots](creating-marginal-plots.html) Transform your plots into marginal plots to gain additional insights into your data.
- [Annotating Test Results or Steps with Keywords from a Data Space](editing-test-result-keywords-from-a-data-space.html) Add, remove, and modify result keywords or step keywords from a data space. You can also exclude results or steps from a data space using a keyword.

Parent topic:

Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-enterprise path=interacting-with-grids.html language=enus -->
## TOPIC 00062: Filtering Grids

- bundle_id: `systemlink-enterprise`
- source_path: `interacting-with-grids.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/interacting-with-grids.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Query your grids to create filtered views that you can reuse and share. In the SystemLink Enterprise web application, expand the navigation menu and click the application that best matches your goal. Systems Management Systems Operations Work Items Operations Work Orders Product Insights Products Pr

### Filtering Grids

Query your grids to create filtered views that you can reuse and share.

1. In the SystemLink Enterprise web application, expand the navigation
 menu and click the application that best matches your goal. 
 Systems Management»Systems
 Operations»Work Items
 Operations»Work Orders
 Product Insights»Products
 Product Insights»Test Results
 Product Insights»Files
 Analysis»Routines
 Analysis»Executions
2. Click [IMAGE alt='Filter icon.' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'] and define the query you want to use to filter items in your grid. 
 
 For example, you want to see only systems that are connected and have NI as the
 vendor. To create the view, use the following query settings. Property
 Operator
 ValueVendor
 contains
 NI
 Connection Status
 equals
 Connected
  1. Select the property you want to use to filter the results. 
 A property can be a name, model, model number, and more.
  2. Select the operation for how the property must correspond to the value. 
 Depending on the property you select, your query can only perform certain
 operations. 
 For example, if you want to query for locked systems, you can perform only the
 equals operation or the does not equal
 operation.
  3. Specify the value of the property you want to use to filter the results.
3. Optional: 
 To filter your grid successfully, repeat the filtering step, as needed.
4. Click OK.
5. Click [IMAGE alt='Column chooser icon.' src='GUID-520B177E-8277-4540-9620-9994144B0F10-a5.png'].
6. In the Configure grid slide-out, use the Column
 tab to add or remove columns from your view. To organize your grid items by
 shared traits, use the Grouping tab . You can click and drag the
 items in these tabs to change the order of the items in your view.
7. To access the view on a recurring basis, click the drop-down next to [IMAGE alt='View menu drop-down icon' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png'] and select Save. Saving preserves your column, grouping,
 and sorting options as well.

Configure View

Create View

Parent topic:

Navigating SystemLink Enterprise

Related tasks:

- Filtering and Sorting Test Results by Custom Properties
- Viewing Product Specifications

<!--NI_TOPIC bundle=systemlink-enterprise path=manage-locations.html language=enus -->
## TOPIC 00063: Managing Your Locations

- bundle_id: `systemlink-enterprise`
- source_path: `manage-locations.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/manage-locations.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Assign locations in SystemLink to track systems and assets Locations represent a specific point, area, or setting in the real world. Use locations to organize a hierarchy of physical places in parent-child relationships. Locations can reach a maximum hierarchy depth of 11.

### Managing Your Locations

Assign locations in SystemLink to track systems and assets

*Locations* represent a specific point, area, or setting in the real world. Use
 locations to organize a hierarchy of physical places in parent-child
 relationships.

Note

- [Adding and Editing Locations](add-locations.html) Create locations to track assets and systems from SystemLink.
- [Searching SystemLink by Location](search-by-location.html) Display all assets or systems at a location.
- [Changing Locations](change-locations.html) Move an asset or system to a new location.

<!--NI_TOPIC bundle=systemlink-enterprise path=manage-your-software.html language=enus -->
## TOPIC 00064: Managing Your Software

- bundle_id: `systemlink-enterprise`
- source_path: `manage-your-software.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/manage-your-software.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemLink centralizes software package hosting for test systems through feeds and system states that manage dependencies and versions. A package is a single, compressed file that contains software to install on a target machine. Each package contains a collection of files and metadata to install an

### Managing Your Software

SystemLink centralizes software package hosting for test systems through feeds
 and system states that manage dependencies and versions.

A *package* is a single, compressed file that contains software to
 install on a target machine. Each package contains a collection of files and
 metadata to install and uninstall the files.

feed

Note

A *system state* specifies a collection of feeds and the specific
 version of a package to install. System states help organize collections of
 software packages for deployment to one or more of your managed systems.

- NI TestStand
- NI DAQmx drivers
- Custom LabVIEW test applications
- Any configuration files

You can deploy a system state to accommodate these requirements. The
 system state ensures that the correct software versions install to
 the managed system.

- [Hosting Feeds and Packages in SystemLink](host-feed-and-package.html#GUID-DBF83468-4407-4987-B56A-76B6342E7200) SystemLink Feeds organize, host, and manage software packages for Windows and NI LinuxRT deployments.
- [Creating and Deleting System States](create-and-delete-states.html) System states provide configuration management for SystemLink systems by defining feeds and packages with specific software versions.

Parent topic:

Managing Your Systems

<!--NI_TOPIC bundle=systemlink-enterprise path=managing-access.html language=enus -->
## TOPIC 00065: Managing Access to SystemLink Enterprise

- bundle_id: `systemlink-enterprise`
- source_path: `managing-access.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/managing-access.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: As a system administrator, specify which parts of SystemLink Enterprise different users can access. You can control access through workspaces, roles, and privileges. The SystemLink web application uses role-based access control (RBAC) to specify privileges in SystemLink Enterprise. These privileges

### Managing Access to SystemLink Enterprise

As a system administrator, specify which parts of SystemLink Enterprise different users can access. You can control access
 through workspaces, roles, and privileges.

SystemLink Enterprise

- Which users or systems can access resources.
- What the users or systems can do with the resources.
- What applications the users or systems can access.

SystemLink Enterprise

- [Assigning a Server Administrator to a Server](assigning-a-server-administrator-to-a-server.html) Assign additional server administrators to help setup workspaces and define the roles available on the server.
- [Creating a Workspace](creating-a-workspace.html) Create a workspace to control which systems and data different types of users can interact with.
- [Configuring a Role and Privileges](configuring-roles-privileges.html) Create and assign privileges to a role to customize how users can interact with each SystemLink application and service.
- [Assigning Users to Roles in a Workspace](mapping-roles.html) Create custom experiences for each type of user by specifying the user's role has and the workspaces the user can access.
- [Adding Users to a Workspace](adding-users.html) As a workspace owner, add users to workspaces and specify roles without knowing the identity provider (IdP) configuration. This increases flexibility when managing workspace membership and roles.
- [Archiving Your Workspaces](archiving-workspaces.html) Store your workspaces when your organization is no longer using them.
- [Creating an API Key](creating-an-api-key.html) Create an API key to automate access to the SystemLink API from an external application.

<!--NI_TOPIC bundle=systemlink-enterprise path=managing-systems.html language=enus -->
## TOPIC 00066: Managing Your Systems

- bundle_id: `systemlink-enterprise`
- source_path: `managing-systems.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/managing-systems.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: View, configure, and generate reports about the settings and details of your systems. Complete the following tasks to meet your systems management goals.

### Managing Your Systems

View, configure, and generate reports about the settings and details of your
 systems.

Complete the following tasks to meet your systems management goals.

- [Setting up a SystemLink Client](setting-up-systemlink-client.html) Install SystemLink Client to establish a connection between your SystemLink server and a remote target.
- [Managing Your Software](manage-your-software.html) SystemLink centralizes software package hosting for test systems through feeds and system states that manage dependencies and versions.
- [Modifying the Settings of a System](modifying-setting-of-connected-system.html) Configure the settings of a system to manage how it operates.
- [Queuing Jobs for Offline Systems](queuing-jobs.html) Specify actions for managed systems to perform after they connect to SystemLink.
- [Visualizing Metadata of a System](displaying-metadata-of-system.html) Display and modify the metadata, such as the name, IP address, or model, associated with your system so you can interact with data more efficiently.
- [Generating System Configuration Reports](generating-system-configuration-reports.html) Generate reports on managed software and connected assets on a system.
- [Monitoring System Health with Alarms](monitoring-system-health.html) Use a routine to create alarm instances when a tag value meets certain conditions.

<!--NI_TOPIC bundle=systemlink-enterprise path=managing-work-orders-and-test-plans.html language=enus -->
## TOPIC 00067: Managing Work Orders and Work Items

- bundle_id: `systemlink-enterprise`
- source_path: `managing-work-orders-and-test-plans.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/managing-work-orders-and-test-plans.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Operations section to create, view, and track work while you evaluate products. A work order is the top-level lab request. Work orders represent a contract between a requester and the lab. Work orders are a special type of work item that represents a collection of all other work item types.

### Managing Work Orders and Work Items

Use the Operations section to create, view, and track work while you
 evaluate products.

A *work order* is the top-level lab request. Work orders represent a contract
 between a requester and the lab. Work orders are a special type of work item that represents a
 collection of all other work item types.

A *work item* is a request to track specific operations involving lab resources. Work
 items help you organize, schedule, and track lab work.

SystemLink supports the following work item types.

| Work Item Type | Description | Example Use |
| --- | --- | --- |
| Calibration | A Calibration work item schedules and reserves systems and assets for periodic calibration. Your lab or company might require that a third party perform calibrations on your assets. | Send a set of measurement instruments to a calibration lab before their calibration certificates expire. |
| Job | A Job schedules and reserves systems, assets, and DUTs for custom lab activities. Jobs are a generic and flexible work item type. Use jobs for work that does not produce a test result or additional measurement data. | Before testing begins, mount a DUT onto a test fixture and verify the physical connections. |
| Maintenance | A Maintenance work item schedules and reserves systems and assets for periodic maintenance. | Perform scheduled preventive maintenance on a test system, including replacing worn connectors and updating firmware. |
| Reservation | A Reservation work item manually reserves a system, asset, or DUT for a lab activity. Reservations are the simplest type of work item. | Check a specific instrument out of an equipment library. |
| Test Plan | A Test Plan schedules, reserves, and executes tests on one or more DUTs with a specific system. A test plan must link to a product and produce test results. | Run a characteristic test on a DUT using a dedicated test system and record the results for compliance. |
| Transport Order | A Transport Order schedules and reserves assets and DUTs for movement between locations. Transport orders do not require a system or fixtures. For each asset or DUT, you can specify a target location and a target parent. | Move a set of DUTs from a warehouse to a test station and mount each DUT to a specific slot. |

Refer to the following topics to create and manage work orders and work
 items.

- [Creating and Managing Work Orders](creating-and-managing-work-orders.html) Create work orders for assignment and tracking to lab personnel.
- [Creating a Work Item](creating-a-test-plan.html) Create one or more work items to track lab activities.
- [Scheduling a Work Item](scheduling-a-test-plan.html) Use the scheduling assistant to schedule a work item based on which resources are available.
- [Viewing Scheduled Work Items](viewing-scheduled-test-plans.html) Use the Schedule view to review all work items scheduled for a system.
- [Automating Work Items with Jupyter Notebook](automate-test-plans-with-jupyter-notebook.html) Use Jupyter Notebooks to automate and to schedule your work items with custom algorithms.
- [Reserving Fixtures for a Work Item](scheduling-a-test-plan-to-fixtures.html#GUID-D4386790-22EE-49E3-A331-C220DA2F9BF5) Use SystemLink Enterprise to reserve one or more fixtures under a system for a work item.

<!--NI_TOPIC bundle=systemlink-enterprise path=managing-your-assets.html language=enus -->
## TOPIC 00068: Managing Your Assets

- bundle_id: `systemlink-enterprise`
- source_path: `managing-your-assets.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/managing-your-assets.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: View calibration data, track your physical assets, and visualize information about your assets. An asset is any hardware device, including third-party devices. SystemLink Enterprise automatically detects most NI assets and many standards compliant third-party devices and shows them in the SystemLink

### Managing Your Assets

View calibration data, track your physical assets, and visualize information
 about your assets.

asset

SystemLink Enterprise

SystemLink Enterprise

Adding
 Assets

SystemLink Enterprise

NI Driver Downloads

- [Viewing Hardware Calibration Data](viewing-hardware-calibration-data.html) View hardware calibration data to make maintenance decisions about your assets.
- [Adding Assets](adding-assets.html) Add NI assets and third-party assets to SystemLink so you can manage them from the web application.
- [Tracking the Location of Assets over Time](tracking-the-location-of-assets-over-time.html) Determine when, where, and how long an asset was connected to a system. You can also see how long the system was online.
- [Applying Custom Metadata to Assets](applying-custom-metadata-to-assets.html) Assign properties or keywords to your assets so you can search and filter them in your workspace.

Related tasks:

- Adding Assets

Related information:

- NI Driver Downloads

<!--NI_TOPIC bundle=systemlink-enterprise path=mapping-roles.html language=enus -->
## TOPIC 00069: Assigning Users to Roles in a Workspace

- bundle_id: `systemlink-enterprise`
- source_path: `mapping-roles.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/mapping-roles.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create custom experiences for each type of user by specifying the user's role has and the workspaces the user can access. This workflow requires administrator privileges and uses identity provider (IdP) mappings to define a user's role. You might want to add a user as a member of a workspace instead

### Assigning Users to Roles in a
 Workspace

Create custom experiences for each type of user by specifying the user's role has and
 the workspaces the user can access.

- You do not have administrator privileges.
- You do not know the identity provider configuration.

1. Navigate to Access Control»Workspaces.
2. Find the workspace you want to add users to and click [IMAGE alt='Workspace actions menu icon (three vertical dots).' src='GUID-665A9E3E-D9C9-43D2-AFE7-DA8F00B39505-a5.png']»Edit workspace. 
 A user must be a member of a workspace to access the systems and data within the
 workspace. This is true for both the SystemLink Enterprise web
 application and the SystemLink REST APIs.
3. Click Role mappings.
4. Click +Mapping and select the attribute that matches the
 authentication protocol your organization configured at installation.
5. Enter the attribute and value for the users you are mapping to the role. 
 Attributes can include the following: The common OpenID Connect claims such as email
 Non-standard claims such as groups for Microsoft Entra
 IDNote 
 All string values are case sensitive.
 If the claim value is a scalar, it must exactly match the value you specify in the
 role mapping .
 If the claim value is an array, one of the array elements must exactly match the
 value you specify in the role mappings.
 If the claim value contains quotes, you must escape the quotation marks with a
 backslash. Refer to the following example and the following figure.
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
}[IMAGE alt='The edit workspace page demonstrating the use of the role mappings section' src='GUID-29F7870E-36AC-4EA0-BA45-8577F2C58B59-a5.png']
6. In the Role column, select the role you want to assign
 to the user.
7. Optional: 
 If a user or group of users needs more than one role, create a separate mapping for
 each role.
8. Click Update. 
 After a user logs into SystemLink Enterprise for the first
 time, their account appears under Access Control»Users.
9. If a user or group of users needs access to more than one
 workspace, repeat these steps for each workspace. 
 If you add a user to multiple workspaces, the user sees resources in the
 workspaces simultaneously.

SystemLink Enterprise

Account

»

Workspaces

Parent topic:

Managing Access to SystemLink Enterprise

Related tasks:

- Configuring a Role and Privileges
- Adding Users to a Workspace
- Assigning a Server Administrator to a Server

Related reference:

- Predefined Roles in SystemLink Enterprise

<!--NI_TOPIC bundle=systemlink-enterprise path=modifying-setting-of-connected-system.html language=enus -->
## TOPIC 00070: Modifying the Settings of a System

- bundle_id: `systemlink-enterprise`
- source_path: `modifying-setting-of-connected-system.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/modifying-setting-of-connected-system.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure the settings of a system to manage how it operates. In the SystemLink web application under Systems Management, click Systems. Select one or more systems and click Settings. Use the following table to complete the task that aligns with your goal. Goal Tasks Assign properties to a system Se

### Modifying the Settings of a System

Configure the settings of a system to manage how it operates.

1. In the SystemLink web application under Systems
 Management, click Systems.
2. Select one or more systems and click Settings.
3. Use the following table to complete the task that aligns with your goal. 
 Goal
 TasksAssign properties to a system
 Select one or more systems in the same workspace.
 In the menu bar, click Edit.
 Navigate to the Properties tab.
 Click Add property to update the system
 properties.
 Assign keywords to a system
 Select a system.
 In the menu bar, click Edit.
 Navigate to the Properties tab.
 Click Add keyword to update the system
 keywords.
 Change the workspace of the system
 Select one or more systems that are in the same workspace.
 In the menu bar, click Edit.
 In the Info tab, select a new workspace.
 Change the startup configuration of one or more RT
 systems
 Select one or more RT systems that are in the same workspace.
 In the menu bar, click Edit.
 Navigate to the Target tab.
 Enable or disable startup configuration options.An unchecked option means that no systems have that
 configuration.
 A dash (-) by the option means that some
 systems have that configuration and others do not.
 A checked option means that all systems have that configuration.
 View the network settings of an RT system
 Select a system.
 In the menu bar, click Edit.
 Navigate to the Target tab.
 View the last known configuration for the network adapters.
 Assign a new system name
 Select a system.
 In the menu bar, click Edit.
 In the Info tab, update the name of the system.
 Specify a location for one or more systems
 Select one or more systems in the same workspace.
 Click Edit in the menu.
 In the Info tab, select a
 Location for the systems.
4. Click Save.

Parent topic:

Managing Your Systems

Related tasks:

- Applying Custom Metadata to Systems

<!--NI_TOPIC bundle=systemlink-enterprise path=monitoring-alarms.html language=enus -->
## TOPIC 00071: Monitoring Alarms

- bundle_id: `systemlink-enterprise`
- source_path: `monitoring-alarms.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/monitoring-alarms.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Monitor, acknowledge, and clear alarms in your system. In SystemLink Enterprise, navigate to Overview Alarms . Filter or search for your alarm in the grid. Click on the alarm to see details on that alarm in the slide-out panel. You can perform the following alarm actions: Acknowledge Force Clear Del

### Monitoring Alarms

Monitor, acknowledge, and clear alarms in your system.

1. In SystemLink Enterprise, navigate to Overview»Alarms.
2. Filter or search for your alarm in the grid.
3. Click on the alarm to see details on that alarm in the slide-out panel.
4. You can perform the following alarm actions: 
 Acknowledge
 Force Clear
 Delete
 Note To understand the alarm state resulting from each
 action, refer to *Generating Custom Alarms*.
 Note To generate alarms based on tag value conditions,
 refer to *Monitoring System Health with Alarms*.

Parent topic:

Sharing Data across Systems

Related tasks:

- Generating Custom Alarms
- Monitoring System Health with Alarms

<!--NI_TOPIC bundle=systemlink-enterprise path=monitoring-data-with-tags.html language=enus -->
## TOPIC 00072: Monitoring Data with Tags

- bundle_id: `systemlink-enterprise`
- source_path: `monitoring-data-with-tags.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/monitoring-data-with-tags.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Observe the current value of one or more tags published to your system. In the SystemLink web application under Systems Management, click Systems. Select the system your tag is published to and click the Tags tab. You will see all tags published to the system and their current value. Tags published

### Monitoring Data with Tags

Observe the current value of one or more tags published to your system.

1. In the SystemLink web application under Systems Management,
 click Systems.
2. Select the system your tag is published to and click the Tags
 tab. 
 You will see all tags published to the system and their current value. Tags
 published to the system have a path that begins with SystemID. For
 example, {$SystemID}.Maintenance.InspectionDueDate.
3. Hover over a tag and click [IMAGE alt='Options menu icon (three dots)' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png']»Copy relative path.
4. Navigate back to Systems and click [IMAGE alt='Configure grid icon' src='GUID-116D9367-1613-4644-B25F-ECBEAB894A5D-a5.png'] to open the Configure grid slide-out.
5. Click Add column and select Tag as the
 column type.
6. In the Configure tag column slide-out, paste the relative path you
 copied earlier.
7. Specify which tag data you want to display in the Systems
 grid.
8. Specify the Column name that you want to show in the column
 header.
9. Click Done to confirm your changes.
10. Close the Configure tag column slide-out.
11. Drag the new tag column to the position you want in the column list.
12. Click OK to close the Configure grid
 slide-out.

Parent topic:

Communicating Data with Tags

<!--NI_TOPIC bundle=systemlink-enterprise path=monitoring-system-health.html language=enus -->
## TOPIC 00073: Monitoring System Health with Alarms

- bundle_id: `systemlink-enterprise`
- source_path: `monitoring-system-health.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/monitoring-system-health.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a routine to create alarm instances when a tag value meets certain conditions. Introduced in May 2025 You can create routines to monitor system health tags and trigger alarms based on these tag values. These routines help ensure that critical resources, such as the disk space or the CPU usage of

### Monitoring System Health with Alarms

Use a routine to create alarm instances when a tag value meets certain
 conditions.

Introduced in May 2025

You can create routines to monitor system health tags and trigger alarms based on these tag
 values. These routines help ensure that critical resources, such as the disk space or the
 CPU usage of the system, remain within acceptable limits. This proactive approach to test
 station management can help maintain system reliability.

1. Navigate to Analysis»Routines and click Create routine.
2. Specify a name and description for the routine.
3. Select a workspace for the routine. 
 Note The workspace you choose determines
 the input data for the routine process. For more information about workspaces, refer to
 *Managing Access to SystemLink Enterprise*.
4. Select the Tag value updated event option.
5. Select the Generate alarm automation option.
6. Specify the tag(s) to monitor in the Tag path field. 
 To apply the routine to one tag, specify the absolute path of the tag.
 To apply the routine to multiple tags of the same data type, use the wildcard
 character (*). This character can represent any number of
 characters in the path. 
 The following table displays examples of each type of tag expression.
 Example Tag Expression
 Resultsystem1.Health.Disk.Total
 Monitors only the system1.Health.Disk.Total tag.
 *.Health.Disk.Total
 Monitors all tags ending with .Health.Disk.Total.
7. Specify the tag data type for the routine. 
 Note The routine only monitors tags that
 match the specified data type.
8. Specify a name and description for the alarms.
  1. To make the name and description of your alarm more informative, embed any custom
 property values from the triggering tag. To embed the value, include the property name
 within angle brackets. 
 The following table displays examples of custom property values.
 Property
 Example<displayName>
 Test Machine CPU USED
 <nitagHistoryTTLDays>
 30
 <nitagMaxHistoryCount>
 10000
 <nitagRetention>
 DURATION
 <units>
 %
  2. When the system meets an alarm condition, the routine processor adds the properties
 displayed in the following table. 
 Property
 Example
 Description<system>
 System A
 A user-friendly identifier for the system associated with the tag that
 triggered the alarm. This property is the system alias (if set), the
 hostname (if set), or the first segment of the tag path.
 <alarm_occurred_at_date>
 April 14, 2025
 An American English formatted date stamp of when the alarm
 triggers.
 <alarm_occurred_at_time>
 5:43:26 PM
 An American English formatted time stamp of when the alarm
 triggers.
 <trigger_value>
 17.2
 The value of the tag when the alarm triggers.
 <routine_id>
 67f6bfd155359a8fa775a2a6
 The unique identifier for the routine that triggered the alarm.
 <alarm_condition>
 Greater than: 15
 A formatted string of the tag conditions when the alarm
 triggers.
 <alarm_link>
 https://example.com/alarms/6814dfc3fa3
 A link to the triggered alarm.
 <source_link>
 https://example.com/systems/Test-Machine-00-6A-67-C8-7B
 A link to the system associated with the tag that triggered the
 alarm.
 <minionId>
 Test-Machine-00-6A-67-C8-7B
 An identifier for the system associated with the tag that triggered the
 alarm. By convention, this property is the first segment of the tag
 path.
 The following table illustrates how an alarm name with embedded properties looks
 before and after value substitution.
 Before Substitution
 After SubstitutionCPU usage on <system> is high. CPU usage is
 <value>%.
 CPU usage on test1 is high. CPU usage is 90%.
 PXI chassis in rack number <rack_number> is
 overheating.
 PXI chassis in rack number 154 is overheating.
9. Configure the conditions to specify when to create an alarm.
  1. Under Alarm Conditions, click Add
 Condition and choose the Severity Level for which
 you want to define conditions.
  2. Choose the Comparison Mode you want the alarm rule to use to
 process values.
  3. Specify a Deadband for the alarm. The deadband determines
 how far the tag value must be from the set point to clear an active alarm. 
 Use the following table to determine how deadband values operate in each comparison
 mode.
 Comparison Mode
 Alarm Clearing ValueLess Than
 A value greater than or equal to [Set
 Point]+[Deadband] clears the alarm.
 Less Than or Equal
 A value greater than [Set Point]+[Deadband] clears the
 alarm.
 Greater Than
 A value less than or equal to [Set Point]-[Deadband]
 clears the alarm.
 Greater Than or Equal
 A value less than [Set Point]-[Deadband] clears the
 alarm.
 In Range
 A value less than [Set Point (Low)]-[Deadband] or
 greater than [Set Point (High)]+[Deadband] clears the
 alarm.
10. Choose whether to alert users about alarm activity through email notifications. 
 Note Users receive a new email whenever
 the alarm reaches a new maximum severity due to a tag value change. For example, users
 receive an email if a moderate severity alarm becomes a high severity alarm.
11. Click Create.

When a rule triggers an alarm, you have three options. You can clear the alarm, acknowledge
 the alarm, or ignore the alarm.

The following table illustrates the alarm states that result from different actions you
 perform on an active alarm.

| Cleared? | Acknowledged? | Resulting Alarm State |
| --- | --- | --- |
| No | No | Active |
| No | Yes | Active and acknowledged |
| YesThe alarm condition is no longer met. | No | Active |
| YesThe alarm condition is no longer met. | Yes | Inactive |
| YesThe user force clears the alarm. | Yes By force clearing the alarm, the user also acknowledges the alarm. | Inactive |

Parent topic:

Managing Your Systems

Related tasks:

- Managing Access to SystemLink Enterprise
- Automating Actions with Routines

<!--NI_TOPIC bundle=systemlink-enterprise path=monitoring-tests.html language=enus -->
## TOPIC 00074: Monitoring Tests

- bundle_id: `systemlink-enterprise`
- source_path: `monitoring-tests.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/monitoring-tests.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Track test progress and view test reports in Product Insights Test Results . You can use the /nitestmonitor API or TestStand integration. Product Insights in the SystemLink web application allows the same functionality for both test monitoring methods. Use the following topics to choose a method and

### Monitoring Tests

Track test progress and view test reports in Product Insights»Test Results. You can use the /nitestmonitor API or TestStand integration.

Product Insights

Use the following topics to choose a method and start monitoring tests.

- [Connecting SystemLink with TestStand](integrating-with-teststand.html) Send test metadata from TestStand to SystemLink Enterprise .
- [Associating Test Results with a Product](associating-test-results-with-a-product.html) Specify a part number in test result metadata to associate the result with a product.
- [Publishing Test Results with the Test Monitor API](test-monitoring-http-api.html) Publish test results, log parametric data, and attach additional files to results using the SystemLink Test Monitor API.
- [Analyzing and Interacting with Test Results](analyzing-test-data-jupyter.html) Generate, filter, and visualize test results to analyze your test and measurement data.
- [Storing and Forwarding Test Data](storing-and-forwarding-offline-data-from-client.html) Use the SystemLink Test Monitor Client to avoid data loss during network disruptions.
- [Uploading Custom Files to Test Monitor](uploading-custom-files.html) Upload any type of file to a test result to maintain data traceability.
- [Filtering and Sorting Test Results by Custom Properties](filtering-and-sorting-test-results.html) Query test results to gain specific insights about your test data.
- [Improving Data Table Metadata Query Performance](improving-data-table-metadata-query-performance.html#GUID-A138C555-5F45-4264-8D60-C55B2B983A47) Construct performant queries and configure MongoDB to process queries as efficiently as possible.
- [Viewing Out of the Box (OOTB) Dashboards in SystemLink Enterprise](viewing-out-of-the-box-dashboards.html) SystemLink Enterprise provides preconfigured dashboards for easy access to common information such as asset calibration, lab overview, and product test summary.
- [Adding Dynamic QR Codes to a Dashboard](add-dynamic-qr.html) Create dashboards that generate quick-response (QR) codes for various systems or assets.
- [Adding the Alarms Data Source to a Dashboard](alarms-data-source.html) Create dashboards using the Alarms data source.
- [Using the Data Frames Data Source in a Dashboard](data-frames-data-source.html) Create dashboards using the Data Frames data source.
- [Using Parametric Trend Dashboards](parametric-trend-dashboard.html) The Parametric Trend Dashboard provides an out-of-the-box view of parametric test data in SystemLink Enterprise .
- [Using the Alarms Overview Dashboard](alarms-overview-dashboard.html) The Alarms Overview Dashboard provides an out-of-the-box view of active alarms across your workspaces in SystemLink Enterprise .
- [Using the System Health Dashboard](system-health-dashboard.html) The System Health Dashboard provides an out-of-the-box view of a system's status, active alarms, and connected instruments in SystemLink Enterprise .

Related tasks:

- Setting up a SystemLink Client

<!--NI_TOPIC bundle=systemlink-enterprise path=moving-a-test-result.html language=enus -->
## TOPIC 00075: Moving a Test Result to Another Workspace

- bundle_id: `systemlink-enterprise`
- source_path: `moving-a-test-result.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/moving-a-test-result.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Move a test result to a different workspace so users in that workspace can access it. A test result can belong to only one workspace. Before updating the workspace for a test result, ensure the following. You have delete privileges in the current workspace. You have create privileges in the destinat

### Moving a Test Result to Another
 Workspace

Move a test result to a different workspace so users in that workspace can access
 it.

- You have delete privileges in the current workspace.
- You have create privileges in the destination workspace.

1. Navigate to Product Insights»Test Results.
2. Select the test result you want to move.
3. Click Edit in the toolbar.
4. Select the workspace you want to move the result to.
5. To move attachments to the new workspace, enable Update
 attachments.
6. Click OK.

You have moved the test result to the new
 workspace. Now, only users in the new workspace can access the test result.

Parent topic:

Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-enterprise path=new-features-and-changes.html language=enus -->
## TOPIC 00076: SystemLink Enterprise New Features and Changes

- bundle_id: `systemlink-enterprise`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/new-features-and-changes.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of SystemLink Enterprise. Discover what is new in the latest releases of SystemLink Enterprise.If you cannot find new features and changes for your version, it might not include user-facing updates. However,

### SystemLink Enterprise
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of SystemLink Enterprise.

SystemLink Enterprise

Note

Release Notes

Related concepts:

- Updates and Changes for SystemLink Enterprise 2024 and Earlier

Related information:

- Release Notes

#### June 2026

Explore the June 2026 SystemLink Enterprise release, including
 support for PostgreSQL 18, support for Grafana 12, and new features for managing
 specification conditions.

- Support for PostgreSQL 18.
- Support for Grafana 12.
- Filter for files with specific custom property keys.
- Manage specification conditions from the SystemLink user interface. For more information,
 refer to Creating, Viewing, and Managing Specification Conditions .

#### May 2026

Explore the May 2026 SystemLink Enterprise release, including a new
 work item type and an upgrade for Dremio 26.

- Create a Transport Order to schedule and reserve assets and DUTs for movement between
 locations. For more information, refer to Managing Work
 Orders and Work Items .
- Open files in DIAdem from SystemLink. In the Files 
 application, select a file and click Open in DIAdem . To
 use this feature, you must install both Diadem and DIAdem SystemLink Toolkit .
- Upgraded SystemLink to Dremio 26. For more information, refer to the Release Notes and the SystemLink Enterprise IT Administrators
 Manual .

#### April 2026

Explore the April 2026 SystemLink Enterprise release, including work
 item API support, test plan management, and high resolution zoom for data
 frames.

- Added the SystemLink Enterprise IT Administrators Manual . Use this manual to
 deploy, configure, and troubleshoot SystemLink Enterprise.
- Added support for Reservation, Maintenance, Job, and Calibration work items. From more
 information, refer to Managing Work Orders and Work Items .
- Added support for reserving multiple DUTs and other assets as part of test plans.
- Added support for providing granular privileges with each work item type.
- Added support for high resolution zoom in the Data Frames Data Source. For more information,
 refer to Using the Data Frames Data Source in a Dashboard .
- Added support for location search through the Systems application and the Assets
 application. For more information, refer to Managing Your
 Locations .
- Updated client Python APIs for alarms, assets, and file ingestion. For more information,
 refer to the nisystemlink.clients Python API
 documentation for nisystemlink 0.1.4.

#### March 2026

Explore the March 2026 SystemLink Enterprise updates, including
 the ability to query undecimated data and improvements to the Routines
 application.

- Added support for querying undecimated data to the Data Frames data source. For more
 information, refer to Using the Data Frames Data Source in a Dashboard .
- Added support for filtering dashboards for systems.
- Updated the Routines application. The updates include improvements to search, the summary
 pane, and the table view configuration.
- Added a new Helm value: smtpServer.fromDomain . This value allows you to set
 the domain name for the Routines application during the SMTP HELO/EHLO
 handshake. Setting the domain name helps meet corporate SMTP server requirements
 such as allowing listed domains, subdomain validation, or DNS/rDNS
 consistency.

#### February 2026

Explore the February 2026 SystemLink Enterprise updates, including
 new dashboards, chart types, and enhanced asset search capabilities.

- Added new out-of-the-box dashboard for Alarms Overview. For more information, refer to Using the
 Alarms Overview Dashboard .
- Added new out-of-the-box dashboard for System Health. For more information, refer to Using the
 System Health Dashboard .
- Added the box chart type to the Plotly panel in dashboards.
- Added the violin chart type to the Plotly panel in dashboards.
- Removed support for deploying MongoDB with the SystemLink Helm chart. SystemLink still
 requires MongoDB, but now you can decide where to run and set up MongoDB.
- Added support for Test Result Changed events and Work Item Changed
 Routine events. For more information, refer to Automating
 Actions with Routines .
- In the Assets application, search queries return results
 from all assets rather than only shown assets.
- In the Assets application, you can specify a filter for
 assets under a specific location hierarchy.

#### January 2026

Explore the January 2026 SystemLink Enterprise updates, including
 new methods for storing, indexing, and filtering data.

- Use Dremio to store and index tabular data. For more information, refer to the SystemLink Enterprise IT Administrators Manual .
- Use the Data Frames data source in dashboards to filter data tables using result properties
 and data table properties. For more information, refer to Using the
 Data Frames Data Source in a Dashboard .
- Create variables that use data table columns to dynamically view dashboard data. For more
 information, refer to Using Data Tables as Dashboard Variables .
- Use the Resource Changed Routine interface with notebooks to create a routine that executes
 on a SystemLink resource. For more information, refer to Publishing a
 Jupyter Notebook .

<!--NI_TOPIC bundle=systemlink-enterprise path=normalize-data-for-efficient-storage-and-access.html language=enus -->
## TOPIC 00077: Normalizing Data for Efficient Storage and Access

- bundle_id: `systemlink-enterprise`
- source_path: `normalize-data-for-efficient-storage-and-access.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/normalize-data-for-efficient-storage-and-access.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data tables are a read-optimized, columnar data storage format designed to store tables with many rows of data. You can use the API of the Data Frame Service to normalize data from multiple file formats into one common format. Using one format for all data allows you to create reusable analysis rout

### Normalizing Data for Efficient Storage and
 Access

Data tables are a read-optimized, columnar data storage format designed to store
 tables with many rows of data.

You can use the API of the Data Frame Service to normalize data from multiple file
 formats into one common format. Using one format for all data allows you to create
 reusable analysis routines and visualizations.

You can use data tables to store waveform data or time-series data. Data tables that
 contain time-series data do not require a constant time interval.

You can perform the following actions with data tables.

- Use multiple extract, transform, and load (ETL) pipelines to convert different file
 types with different data structures into a data table.
- Use common analysis routines and visualization techniques to interact with the
 single, normalized format.
- Append multiple new rows to a data table in a single API call. A data table can have
 an unlimited number of rows. The rows can be in any order. Any column can reorder
 the rows during the reading of the table. Note Row data might not be available
 for reading for up to five minutes after writing.
- Use the API of the Data Frame Service for the following purposes.
  - Read data within a data table.
  - Specify the columns for a data table.
  - Specify the number of rows for a data table.
- Query table metadata to return one or more data tables that match the parameters of
 the query. This method is useful for identifying tables that are associated with a
 test result or other test metadata.
- Query within the table for specific data. This method is useful when you are
 searching for a particular characteristic in your data that is missing from the
 table metadata. For example, you can query within a data table to find the first
 instance of a value over a particular threshold.
- Export queried table data as a comma-separate values (CSV) file to view the
 normalized data in a spreadsheet editor.

When querying within a table, you can decimate the data before returning it to the
 caller. Use one of the following methods to decimate the data. Decimation is useful when
 visualizing large data sets. Decimation is also useful in analysis when the shape of the
 data is more critical than each individual point. For example, you might use a
 MAX_MIN decimation method to find outliers without returning all
 data in the data table.

| Method | Description | Example |
| --- | --- | --- |
| LOSSY | Returns a set maximum number of points from a uniform sample of the result set. If there are fewer data points than the maximum specified, the decimation returns all points. This method allows you to see the general shape of the data quicker but is less accurate. Spikes might not show up while plotting the result set. |  |
| MAX_MIN | Returns the points where the selected Y-channel reaches its maximum and minimum values in each interval of data. This decimation allows you to plot the data using continuous lines. Using continuous lines maintains the shape of the data, including spikes. |  |
| ENTRY_EXIT | Returns a similar set of points as MAX_MIN except that it adds the entry and exit points for each of the intervals. Entry is the left-most point in a graph where the x-value is minimum in an interval. Exit, is the right-most point where the x-value is maximum in an interval. |  |

If there are too few data points per interval, null values and NaN
 values can disrupt the shape of the data.

- NaN values can appear as the minimum or maximum value for the
 column containing these values.
- Null values can appear as the maximum value, similar to Infinity.

NaN

Note

NaN

Parent topic:

Storing and Managing Files

Related tasks:

- Normalizing Incoming Data Automatically

<!--NI_TOPIC bundle=systemlink-enterprise path=normalizing-incoming-data-automatically.html language=enus -->
## TOPIC 00078: Normalizing Incoming Data Automatically

- bundle_id: `systemlink-enterprise`
- source_path: `normalizing-incoming-data-automatically.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/normalizing-incoming-data-automatically.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a routine to automatically convert incoming data files into a data table. In the SystemLink web application, navigate to Analysis Scripts . Click Python 3 (ipykernel). Use the linked example as a template to create ETL pipelines. The example includes steps to complete the following actions. E

### Normalizing Incoming Data
 Automatically

Create a routine to automatically convert incoming data files into a data
 table.

1. In the SystemLink web application, navigate to Analysis»Scripts.
2. Click Python 3 (ipykernel).
3. Use the linked example as a template to create ETL pipelines. 
 The example includes steps to complete the following actions.Extract the file contents.
 Transform the data into a data table format.
 Load the data into storage with the DataFrame Service API. 
 Note When you create a data
 table, you must do the following.Define the column type.
 Define the data type for each column.
 Define the total number of columns. The total number of columns
 cannot exceed 2500.You cannot change these settings after creating the table. However, you
 can define and update additional metadata for existing tables or
 columns.
 Column Type
 DescriptionNORMAL
 The column has no special properties. This behavior is
 the default behavior.
 INDEX
 The column provides a unique value per row. Each table
 must provide one INDEX column with one of
 the following data types. INT32
 INT64
 TIMESTAMP
 NULLABLE
 The column allows rows to contain null
 values. You can exclude NULLABLE columns
 when appending rows. Appended rows will use
 null values for that column.
 Note After you finish appending
 data to a table, free up resources associated with the table. Use the route
 POST
 /nidataframe/v1/tables/{id}/data where
 {id} is the table ID. Set
 endOfData to true in the
 JSON body of the request.
4. Create a routine to execute your notebook and specify File
 uploaded for the event. Refer to *Automating Actions with
 Routines* to learn how to create a routine. 
 When files are created, your notebook will execute to convert the file
 data into a data table.

| From a dashboard | Click the top of the data table panel in your dashboard and select Inspect. Click Download CSV.Note Data tables downloaded from a dashboard are decimated based on the query settings for the dashboard. |
| --- | --- |
| From a test result | Select a data table in the Data Tables tab and click Download CSV.Note Data tables downloaded from a test result are undecimated. |

Parent topic:

Storing and Managing Files

Related concepts:

- Normalizing Data for Efficient Storage and Access

Related tasks:

- Automating Actions with Routines

Related information:

- ETL Example

<!--NI_TOPIC bundle=systemlink-enterprise path=parametric-trend-dashboard.html language=enus -->
## TOPIC 00079: Using Parametric Trend Dashboards

- bundle_id: `systemlink-enterprise`
- source_path: `parametric-trend-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/parametric-trend-dashboard.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: The Parametric Trend Dashboard provides an out-of-the-box view of parametric test data in SystemLink Enterprise. Use this dashboard to identify trends and anomalies across measurements, products, and test programs. The dashboard contains interactive charts and tables that visualize up to the most re

### Using Parametric Trend Dashboards

The Parametric Trend Dashboard provides an out-of-the-box view of parametric test data in
 SystemLink Enterprise.

Use this dashboard to identify trends and
 anomalies across measurements, products, and test programs. The dashboard contains
 interactive charts and tables that visualize up to the most recent 1000 results and
 steps.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Open the Default Dashboards folder and
 select Parametric Trend Dashboard.
3. Use the filters to view the parametric data for specific tests. 
 Filters
 DescriptionWorkspace
 Represents the top-level grouping.
 Product
 Represents the parts that you are testing.
 Test
 Program
 Represents the test sequences and any associated
 settings.
 Step
 Represents the individual measurements and sequences that
 are part of the test program.
4. View your dashboard data using the following panels. 
 Dashboard Panel
 DescriptionSummary of Test
 Steps
 Count of Test Steps across different states. SystemLink Enterprise groups this counting
 by the statusType property.
 Average Duration of Test
 Steps
 Displays the calculated average of test steps for a given
 population.
 Time-series
 Graph
 Displays all the measurements, and any corresponding
 limits, from the chosen steps over time. This graph uses the
 Step.StartedAt property as an
 x-axis.
 Test Steps per Day Bar
 Graph
 Counts the number of test steps per day. The count is
 grouped by the statusType property. This
 graph uses the Step.StartedAt property as
 an x-axis.
 Test Results
 Table
 Displays the following result properties in a table. Test program name
 Part number
 Serial number
 Status (color coded)
 Host name
 Start time
 Total time
 Workspace
 Operator
 Test Results Pie
 Chart
 Displays the overall test results states. SystemLink Enterprise groups this chart by
 the statusType property.
5. Hover over charts to obtain details on the data.
6. Apply more group filters to refine the data.
7. Export the table data.
  1. On a dashboard panel, click the ellipsis ([IMAGE alt='Ellipsis (more options) menu icon on a dashboard panel.' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png']).
  2. Click Inspect»Data.
  3. Click Download CSV.

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-enterprise path=plotting-parametric-data.html language=enus -->
## TOPIC 00080: Plotting Parametric Data in a Data Space

- bundle_id: `systemlink-enterprise`
- source_path: `plotting-parametric-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/plotting-parametric-data.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Derive insights about parametric test data by visualizing it in different types of charts. Navigate to Product Insights Data Spaces . Click Create data space. SystemLink opens the Create data space slide-out. Under Data source, select Parametric test data. Specify the product, result, and step prope

### Plotting Parametric Data in a Data
 Space

Derive insights about parametric test data by visualizing it in different types of
 charts.

1. Navigate to Product Insights»Data Spaces.
2. Click Create data space. 
 SystemLink opens the Create data space
 slide-out.
3. Under Data source, select Parametric test
 data.
4. Specify the product, result, and step properties for the data you want to get
 parametric data for. To narrow down measurement data, you can filter by a
 condition. 
 Note You must specify at least
 one product-level filter.
5. Click Run query .
6. On the Data tab, select the plot type you want to
 create. 
 Note You can configure
 additional settings on the Settings tab. The settings
 change based on the plot type you choose.
7. Click Add X-Axis and specify the data you want to use
 for the x-axis. 
 OptionDescriptionIndex
 Shows points in the order Test Insights received the pointsTime
 Shows points in chronological order relative to step start
 timeConditions
 Shows points organized by the condition you selectMeasurements
 Shows points organized by the measurement you select
8. Click Close.
9. Click Add Y-Axis and specify the data you want to use
 for the y-axis. 
 OptionDescriptionConditions
 Shows points organized by the condition you selectMeasurements
 Shows points organized by the measurement you select
10. Click Close.
11. Click Save
 [IMAGE alt='Save button.' src='GUID-54AAC5CA-0EF8-41F8-AFFE-4E684F12AC94-a5.png'].
12. Specify a name, assign a workspace, and click
 Save. 
 SystemLink adds this data space to Product Insights»Data Spaces.
13. Optional: 
 To share your data space, copy the page URL.

You can create marginal plots from your parametric data
 plots.

Parent topic:

Interacting with Data in a Data Space

Related tasks:

- Viewing Test Steps by Result
- Viewing Test Results by Product
- Creating Marginal Plots

<!--NI_TOPIC bundle=systemlink-enterprise path=predefined-properties.html language=enus -->
## TOPIC 00081: Predefined Properties

- bundle_id: `systemlink-enterprise`
- source_path: `predefined-properties.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/predefined-properties.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reference NI-created properties to organize your tests, assets, tags, or files. SystemLink automatically assigns predefined properties to tests, tags, and files that you create. You can reference the predefined properties in your code. Avoid creating custom properties with names identical to the pre

### Predefined Properties

Reference NI-created properties to organize your tests, assets, tags, or
 files.

Note

| Property | Description |
| --- | --- |
| nitmSource | Test framework that published the result |
| nitmTestSocketIndex | TestStand socket on which the test was executed |
| nitmProcessModel | TestStand process model used to execute the test |
| nitmBatchId | Unique identifier for other test results that executed in the same batch |
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

Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-enterprise path=predefined-roles.html language=enus -->
## TOPIC 00082: Predefined Roles in SystemLink Enterprise

- bundle_id: `systemlink-enterprise`
- source_path: `predefined-roles.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/predefined-roles.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Control access to SystemLink Enterprise applications and stored data more easily using roles related to common use cases. To decide which predefined roles to assign a user or group of users, use the following table.For detailed lists of privileges for each role, refer to Access Control in the System

### Predefined Roles in SystemLink Enterprise

Control access to SystemLink Enterprise applications and stored
 data more easily using roles related to common use cases.

To decide which predefined roles to assign a user or group of users, use the following
 table.

Note

Access Control

| Role | Privileges |
| --- | --- |
| Server Administrator | Full privileges for all SystemLink Enterprise workspaces, applications, and rolesNote Server Administrator is the most permissive role in SystemLink Enterprise. Assign this role only to users who administer access control. |
| Data Maintainer | Create, read, update, and delete privileges for tests, files, dashboards, and data-related tasks Read privileges for systems and assets Create and manage API keys |
| Systems Maintainer | Create, read, update, and delete privileges for systems, assets, alarms, and dashboards Read privileges for test results and data stores Create and manage API keys |
| Collaborator | Read privileges for all SystemLink Enterprise applications |
| Automated Agent | Create, read, update, and delete privileges for tests, assets, files, and tags Limited read privileges across other SystemLink Enterprise applications Note You can assign this role to systems only. |
| Workspace Owner | Assign role mapping and add users to the workspaces owned by the usersNote As a Server Administrator, use the Workplace Owner role to delegate tasks while limiting access to other workspaces. For example, you can delegate setting up access to data and applications. |
| Routine Maintainer | All routine privileges Read and cancel notebook executions |

Parent topic:

Configuring a Role and Privileges

<!--NI_TOPIC bundle=systemlink-enterprise path=previous-features-and-changes.html language=enus -->
## TOPIC 00083: Updates and Changes for SystemLink Enterprise 2024 and Earlier

- bundle_id: `systemlink-enterprise`
- source_path: `previous-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/previous-features-and-changes.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in SystemLink Enterprise 2024 and earlier versions. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visib

### Updates and Changes for SystemLink Enterprise 2024 and Earlier

Browse updates and changes made in SystemLink Enterprise 2024 and
 earlier versions.

Note

Release Notes

#### 2025

Explore the 2025 SystemLink Enterprise updates.

##### December 2025

Explore the December 2025 SystemLink Enterprise updates, including
 asset management with QR codes, changes to the specification workflow, and the ability to
 specify locations for systems.

- Use QR codes to manage assets, systems, and locations from mobile devices. For more
 information, refer to Adding Dynamic QR Codes to a Dashboard .
- Create and edit specifications from SystemLink. For more information, refer to Creating and
 Editing Product Specifications through SystemLink .
- Specify a Location for your Systems.

##### November 2025

Explore the November 2025 SystemLink Enterprise update on how to use
 test plans within work items.

- Use test plans within work items to track lab operations and resources. For more
 information, refer to Managing Work Orders and Work Items .

##### October 2025

Explore the October 2025 SystemLink Enterprise updates, including
 system location management, uploading files with chunked transfer encoding, and support for
 binary ingestion in DataFrame.

- Create and manage the locations of your systems and assets in the
 Locations page.
- Upload files through chunked transfer encoding using the SystemLink API.
- Support for binary ingestion in the DataFrame service.

##### September 2025

Explore the September 2025 SystemLink Enterprise updates, including
 features for managing test plans, customizing workflows, and resolving system
 issues.

- View all test plans scheduled for a specific system in the System Details page. For more
 information, refer to Viewing Scheduled Work Items .
- Use the Schedule page to search and filter for fixtures.
- Customize test plan workflows to match the processes of your organization. For more
 information, refer to the Test Plan Operations Example page in
 GitHub.
- Manage system keys to resolve connection and security issues.
- Use the Assets data source in dashboards to display the total count of returned assets in a
 query.
- Compatibility with Grafana 11.

##### August 2025

Explore the August 2025 SystemLink Enterprise update of new support
 for Server-Side Encryption through the AWS Key Management Service.

- Support for Server-Side Encryption through the Key Management Service (AWS SSE-KMS).

##### July 2025

Explore the July 2025 SystemLink Enterprise updates, including
 support for Azure hosting, support for full text search, and enhanced dashboard
 capabilities.

- Support for hosting SystemLink Enterprise on Microsoft Azure. For more
 information, refer to Configuring File Storage in the SystemLink Enterprise IT Administrators Manual .
- Support for full text search on all file types. For more information, refer to
 Configuring an Elasticsearch Instance in the SystemLink Enterprise IT Administrators Manual .
- Use out of the box dashboards to access information such as asset calibration, lab overview,
 and product test summary. For more information, refer to Viewing Out
 of the Box (OOTB) Dashboards .
- Support for the following data sources in dashboards: For more information, refer to [Visualizing Notebook Data on a Dashboard](visualizing-notebook-data-on-dashboard.html).
  - Test Plans
  - Work Orders
  - Test Results
- Filter systems and test plans in schedule view. You can then save these filters and schedule
 view configurations as named views. For more information, refer to Viewing
 Scheduled Work Items .

##### June 2025

Explore the June 2025 SystemLink Enterprise updates, including
 automation for test plans through Jupyter Notebook.

- Use Jupyter Notebook to automatically schedule test plans. For more information, refer to
 Automating Work Items with Jupyter Notebook .
- Use Jupyter Notebook to automate operations on test plans.
- View fixture details from the Scheduling Assistant 
 page.
- When either installing software or applying a system state, you can enable the
 Automatically Restart option. SystemLink now
 remembers this selection when the action is next taken again.

##### May 2025

Explore the May 2025 SystemLink Enterprise updates, including new
 features for creating tag threshold alarms, sending email notifications, and using grids to
 monitor system health.

- Use routines to create tag threshold alarms and to send email notifications. For more
 information, refer to Monitoring System Health with Alarms .
- Use the Systems grid and the Assets 
 grid to determine if an associated tag has an active alarm.
- View the details of a fixture while scheduling a test plan. For more information, refer to
 Viewing
 Scheduled Work Items .

##### April 2025

Explore the April 2025 SystemLink Enterprise updates, including new
 features for test plans, file formats, statistical insights, alarms, and virtual
 systems.

- Schedule a test plan to a fixture under a system. A lab might refer to a fixture as a slot,
 a socket, or a channel. For more information, refer to Reserving
 Fixtures for a Work Item .
- Preview common plain text file formats. For more information, refer to File Formats
 Supported in File Preview .
- Save statistical insights from the analysis of parametric data in a data space.
- Manage alarm instances by navigating to Overview»Alarms .
- Added support for results and steps in the Test Monitor
 Python library. For more information, refer to the Releases ni/systemlink-clients-python 
 page on GitHub.
- Added support for virtual systems. Use a virtual system to manually or programmatically
 manage any data and assets associated with that virtual system.
- Retry and run new notebook executions from the Executions 
 page.
- Filter files by file ID .
- Configure file properties to display in the File Details 
 page.

##### March 2025

Explore the March 2025 SystemLink Enterprise updates, including new
 features for displaying product information, previewing CSV files, and previewing HTML
 files.

- Display product data and properties from the Test Monitor backend service in
 dashboards.
- Preview your CSV files.
- Preview your HTML files.

##### February 2025

Explore the February 2025 SystemLink Enterprise updates, including
 new features for previewing PDF files, filtering work orders, and integrating Google Cloud
 Storage.

- Preview your PDF files.
- Filter the list of work orders you see based on their status or their metadata and save
 custom views. Navigate to Operations»Work Orders and click the summary tiles at the top of the page. For more
 information, refer to Creating and Managing Work Orders .
- Enhanced the performance of queries against continuously written data tables.
- Use Google Cloud Storage (GCS) to store your files.

##### January 2025

Explore the January 2025 SystemLink Enterprise updates, including
 dynamic form fields, hosting web applications, previewing media files, filtering test plans,
 and adjusting Jupyter Notebook rate limits.

- Use dynamic form fields to add custom input fields to the user interface. You can add fields
 to the configuration slide-out of the following resources. For more information, refer to [Adding
 Custom Input Fields to the User Interface](adding-custom-fields-to-the-ui.html).
  - Assets
  - Products
  - Systems
  - Test Plans
  - Work Orders
- Host web applications. For more information, refer to Hosting a Web
 Application .
- Preview your image, audio, and video files. For more information, refer to File Formats
 Supported in File Preview .
- Filter the list of test plans you see based on their status or their metadata. Navigate to Operations»Work Items and click the summary tiles at the top of the page.
- Adjust the default rate limits for Jupyter Notebook operations. For more information, refer
 to the SystemLink Enterprise IT Administrators Manual .

#### 2024

Explore the 2024 SystemLink Enterprise updates.

##### December 2024

Explore the
 December 2024 SystemLink Enterprise updates, including the
 ability to analyze parametric data and manage test plans.

- Analyze your parametric data in a Data Space to get
 statistical insights. For more information, refer to Analyzing
 Parametric Data in a Data Space .
- Create a custom script to analyze your parametric data in a Data
 Space . For more information, refer to Creating a
 Custom Script for Analyzing Parametric Data .
- Use the keyboard to interact with grids. For example, you can use the arrow keys
 to navigate to different rows and different columns.
- Add a hyperlink to an external URL as the value of a custom property. Use the
 following syntax similar to Markdown: `[link
 text](URL)` .
- View additional details about a test plan from the Schedule 
 page. To see more details, navigate to Operations»Schedule and click a test plan card.
- Switch between day, week, month, and year views on the
 Schedule page.
- Download multiple files at once.
- Apply a state to multiple systems at once. Navigate to Systems Management»Systems . Select the systems and click More»Apply state .

##### November 2024

Explore the
 November 2024 SystemLink Enterprise updates, including enhanced
 data management, calibration forecasting, and support for Kubernetes 1.29.

- Search, filter, and save custom views in Data Spaces .
- View, add, and manage calibration data for assets.
- Download a CSV reports for assets. Navigate to Systems Management»Assets and click Download report .
- Forecast upcoming asset calibrations using the built-in calibration forecast
 dashboard. Navigate to Systems Management»Assets . To launch the calibration forecast dashboard, click
 Calibration forecast .
- Improved query performance for data tables.
- Added support for Kubernetes 1.29.
- Added support for PostgreSQL 15.

##### October 2024

Explore the
 October 2024 SystemLink Enterprise updates, including the
 scheduling assistant and new data table viewing options.

- Use the scheduling assistant to see what systems and DUTs are available and
 schedule test plans without conflicts. For more information, refer to Scheduling a
 Work Item .
- Add comments with @ mention and rich text on work orders
 and test plans.
- Configure resource profiles to maximize resource utilization for the Notebook
 Execution Service. In systemlink-values.yaml , you can
 modify the low, medium, or high resource profiles.
- When viewing your data tables in a data space, you can now view your data in a
 table as well as a chart. For more information, refer to Visualizing
 Data Tables in a Data Space .

##### September 2024

Explore the
 September 2024 SystemLink Enterprise updates, including the
 ability to visualize data tables and support for private certificate
 authorities.

- Navigate to Operations»Schedule to view the test plans scheduled across all systems in timeline
 view. For more information, refer to Viewing
 Scheduled Work Items .
- Use the following new features when visualizing data tables in data spaces.
  - Search for columns to plot from the axis selection grid.
  - Color traces by data table and by column metadata.
- Adjust how long the SystemLink Enterprise Alarm Service keeps
 your alarms. For more information, refer to Configuring
 Alarm Retention .
- Adjust how many alarms you can create in the SystemLink Enterprise Alarm Service. For more information,
 refer to Configuring Alarm Limits .
- Learn about the performance metrics for the Dashboard Host Alarm Service.
- Support for private certificate authorities. For more information, refer to the [SystemLink Enterprise IT Administrators Manual](http://www.ni.com/r/sle-it-admin).
  - Connect to MongoDB and S3 compatible interfaces that use certificates
 signed by a private authority.
  - Call SystemLink APIs from Jupyter Notebook . You must configure the
 SystemLink API endpoint to use a certificate signed by a private
 authority.

##### August 2024

Explore the
 August 2024 SystemLink Enterprise updates, including data table
 interactions, new data limits, and performance metrics for the Alarm Service.

- Enable, delete, or disable multiple routines at once. Navigate to Analysis»Routines and select the routines you want to modify. For more information,
 refer to Automating Actions with Routines .
- View and manage data tables across all test results. Navigate to Product Insights»Data Tables and select the data tables you want to interact with.
- Learn about data limits for proxy servers and for ingress controllers. For more information,
 refer to SystemLink Enterprise IT Administrators Manual .
- Learn about the performance metrics for the SystemLink Enterprise Alarm Service.

##### July 2024

Explore the July
 2024 SystemLink Enterprise updates, including new data table
 alignments, data decimation modes, and workspace assignments for products.

- Align the x-axis of your data table plots to zero.
- Decimate the data in your Data Spaces plots using Lossy, Max/Min, or Entry/Exit
 modes.
- Filter and save a custom view of a test plans grid.
- SystemLink Enterprise adds the workspace property to products.
 For products already in your system, SystemLink Enterprise 
 assigns a workspace using the following logic. The product has test results.
 SystemLink Enterprise assigns the workspace
 associated with the first test results listed for the
 product.The product does not have test results.
 SystemLink Enterprise assigns the default
 workspace. For new products, assign a workspace so you can control
 access. For more information, refer to [Creating
 a Workspace](creating-a-workspace.html).

##### June 2024

Explore the June
 2024 SystemLink Enterprise updates, including new options for
 managing alarms and test results.

- Create alarms to notify you when an issue occurs in your system. For more
 information, refer to Generating Custom Alarms .
- Delete one or more product specifications you no longer need. For more
 information, refer to Deleting Specifications .
- Select one or more Test Results and send those results to a Jupyter Notebook for
 analysis. For more information, refer to Analyzing
 Test Results with Jupyter Notebook .
- Select one or more product specifications and send those specs to a Jupyter
 Notebook for analysis. For more information, refer to Analyzing
 Specification Compliance with Jupyter Notebook .
- Automatically copy files linked to a test plan template when you create a test
 plan.
- Filter the test plans grid by using test plan metadata.

##### May 2024

Explore the May
 2024 SystemLink Enterprise updates, including navigation
 enhancements and new data visualizations.

- Navigate SystemLink Enterprise faster with the intuitively
 organized Home page and the navigation pane.
- Visualize data tables in a data space to gain insights into your time-series
 data.
- Analyze test results with Jupyter Notebook.
- Annotate steps with keywords from a data space. For more information, refer to
 Annotating Test Results or Steps with Keywords from a Data
 Space .
- Save custom column configurations for the product specifications grid.
- Create and manage test plans under a product. For more information, refer to
 Managing Work Orders and Work Items .
- Define and apply custom states to a system.

##### April 2024

Explore the
 April 2024 SystemLink Enterprise updates, including new features
 for test plans and managing data spaces.

- Create test plans faster by using a test plan template. For more information,
 refer to Creating a Work Item .
- Edit result keywords from a data space. You can also exclude results from a data
 space using a keyword that the results have in common.
- Learn about the performance metrics for the SystemLink DataFrame service.
- Create feeds and upload custom packages.
- Replicate feeds from a remote URL.
- Upload, download, and configure metadata for system state files.
- Easily move third-party assets between test systems or unmanaged locations.

##### March 2024

Explore the
 March 2024 SystemLink Enterprise updates, including enhancements
 to specification management and test data extraction.

- Use the Specification Management UI to maintain a central repository of
 specifications that you can use to analyze your test results and measurements.
 For more information, refer to Specification
 Compliance .
- Extract Standard Test Data Format (STDF) files into SystemLink results, steps,
 and measurements.
- Learn how SystemLink performs when extracting test data from Bench Data
 Connector (BDC) files and STDF files.
- Duplicate existing routines so you can create similar routines faster. In the
 SystemLink web application, navigate to Analysis»Routines . Select a routine and click
 Duplicate .

##### February 2024

Explore the
 February 2024 SystemLink Enterprise updates, including new APIs,
 new automation routines, and support for Kubernetes 1.28.

- Use the SystemLink Enterprise Test Plans module to create,
 view, and manage work orders and test plans.
- Use APIs for specification management to maintain a central repository of
 specifications. These specifications store test limits and test conditions.
- Create routines to automate an action when an event occurs.
- Distribute Helm charts through the Docker registry to simplify your
 deployment.
- Added support for Kubernetes 1.28.

##### January 2024

Explore the
 January 2024 SystemLink Enterprise updates, including support
 for SystemLink Client, offline activation, and dark mode.

- Added support for SystemLink Client 2024 Q1.
- Activate SystemLink Enterprise offline.
- You can @ mention other users in comments on test results
 and data spaces.
- Trigger test data extraction routines from the Product details page. For more information,
 refer to Data Extraction Performance for Standard Files .
- You can trend step data from the Results details page directly into a data
 space.
- Monitor disk utilization for your user data in JupyterHub. You can see the utilization in
 the main status bar at the bottom of the window.
- Enable dark mode which tracks the settings for your device.

#### 2023

Explore the 2023 SystemLink Enterprise updates.

##### December 2023

Explore the
 December 2023 SystemLink Enterprise updates, including asset
 location tracking, file management, software installation feeds, and parametric data
 visualization in histograms.

- You can track the location history of your assets. For more information, refer
 to Managing
 Your Assets .
- You can manage files associated with your assets.
- You can enable software installation from ni.com or a remote URL by adding those
 locations as feeds on your system.
- You can visualize parametric data in histograms in data spaces.

##### October 2023

Explore the
 October 2023 SystemLink Enterprise updates, including data
 tables enhancements, asset tracking, and MongoDB connectivity.

- You can add comments to test results. For more information, refer to Collaborating
 on Test Results .
- You can view the current and historical values of a tag in dashboards.
- Data tables have improved reliability and scalability and can support thousands
 of concurrent writers.
- You can connect to external MongoDB instances.
- You can view all tracked assets on the Assets page. For more
 information, refer to Managing Your Assets .
- You can change the version of a package installed on a managed system.

##### September 2023

Explore the
 September 2023 SystemLink Enterprise updates, including the
 ability to change system software versions and the ability to add part numbers as
 metadata.

- You can change the version of software installed on a system from the
 System Details page.
- You can specify a part number as additional tracked metadata when adding new assets to
 SystemLink. For more information, refer to Managing Your
 Assets .

##### August 2023

Explore the
 August 2023 SystemLink Enterprise updates, including the ability
 to install software from feeds and the ability to view detailed job
 information.

- Install software on a system from feeds that are already configured on the
 device. In the SystemLink web application, select Systems Management»Systems . Double-click a system, open the Software 
 tab, and click Install software .
- View detailed information about jobs that have executed on a system. In the
 SystemLink web application, select Systems Management»Systems . Double-click a system, open the Jobs tab,
 select a job, and click View .

##### July 2023

Explore the July
 2023 SystemLink Enterprise updates, including test step data
 visualization, enhanced grid features, and new tag management options.

- View detailed test step data under a test result.
- Results and Products grids display a count of
 items that match a query. For more information, refer to Filtering
 Grids .
- Visualize parametric data with a single click from a test result or from the test results
 grid. For more information, refer to Viewing Test
 Results by Product .
- View box, violin, and histogram charts in the margins of a scatter chart in a
 data space.
- Color traces in scatter charts by product, result, step, condition, and
 measurement data.
- The Systems grid tag column supports autocomplete for tag
 paths.
- Added the Tag Historian Service.
- Copy a tag path using the context menu in the Tags grid on the
 System Details page. For more information, refer to
 Monitoring Data with Tags .
- Delete tags in the Tags grid on the System
 Details page.
- Notebook dropdowns group notebooks by workspace.

##### June 2023

Explore the June
 2023 SystemLink Enterprise updates, including asset tracking,
 manual asset addition, data space management, and improved PostgreSQL
 resilience.

- Track the location and status of assets on the Assets tab for your
 system. For more information, refer to Managing Your
 Assets .
- Manually add assets to your system to track third-party devices and devices
 without drivers.
- Edit and delete data spaces from the data spaces table and from an individual
 data space.
- The PostgreSQL backend for the Test Insights Service is more resilient.

##### May 2023

Explore the May
 2023 SystemLink Enterprise updates to the System
 Details page.

- Added tags. Publish and view the current value of tags from your test systems. Monitor the
 status of your test fleet with automatically published system health data on the
 System Details page. For more information, refer to
 Monitoring Data with Tags .

##### April 2023

Explore the
 April 2023 SystemLink Enterprise updates, including data space
 creation, DataFrame Service enhancements, and changes to the Dremio S3 and
 argo-workflows.

- Create data spaces to view parametric test data on a scatter chart. For more information,
 refer to Plotting Parametric Data in a Data Space .
- The DataFrame Service uses streaming data deserialization. This allows you to
 use larger batch sizes with more rows per write.
- The Dremio S3 automatically promotes missing data sets on query. You get improved
 reliability in scenarios where a dataset is deleted at the same time it is
 queried. To uptake this change, delete all Dremio PVCs and restart all Dremio
 and DataFrame Service pods. For more information, refer to Normalizing
 Incoming Data Automatically .
- You can show custom properties in the Files grid and create
 saved views.
- You can filter the steps grid by step and measurement name.
- The default pull policy for images in argo-workflows has
 changed. Instead of always , the new default is
 IfNotPresent .
- The executions grid groups by status by default.
- Schedule routines are enabled by default.
- The feature flag
 routineservice.featureToggle.publishScheduleEvent has been
 removed from the SystemLink Helm chart.
- The DataFrame Service has new limits intended to ensure availability of the
 service.

##### March 2023

Explore the
 March 2023 SystemLink Enterprise updates, including CSV exports,
 Kubernetes 1.23 support, PostgreSQL enhancements, and telemetry metrics for various
 services.

- Export data tables to CSV.
- Query product, results, and steps tables with the table query builder.
- Added support for Kubernetes 1.23.
- Added support for PostgreSQL 13 and 14.
- Added telemetry metrics for the Test Monitor Service, Data Frame Service, and
 Kafka service.
- Replaced oidc/user-info with /oidc/userinfo as
 the endpoint to view claims for the current logged in user.
- Enabled Kafka UI for debugging and monitoring.
- Increased the default memory provided to Kafka topic operator from 256 MB to 512
 MB to increase the total number of tables the Data Frame Service can write
 to.
- Kafka S3 sink connectors are automatically deleted if a data table is marked
 endOfData .
- Deleted Kafka S3 sink connectors are automatically reestablished if connectors
 are manually deleted.

##### February 2023

Explore the
 February 2023 SystemLink Enterprise updates, including support
 for PostgreSQL 14.x and enhanced test result grid customization.

- Added support for PostgreSQL 14.x.
- Add, remove, and reorder columns in the Steps grid when
 viewing the details of a test result.

##### January 2023

Explore the
 January 2023 SystemLink Enterprise updates, including the
 ability to schedule Jupyter notebooks, viewing detailed test step information, and
 accessing SystemLink Enterprise settings

- Schedule a Jupyter notebook to run at a specific time or on a repeating
 schedule.
- View detailed information about individual test steps for a test result. For more
 information, refer to Viewing Test Steps by Result .
- Access SystemLink navigation and user account settings when using the Jupyter
 environment.

#### 2022

Explore the 2022 SystemLink Enterprise updates.

##### December 2022

Explore the
 December 2022 SystemLink Enterprise updates, including Helm
 chart enhancements, dashboard variable support, and features for grid
 customization.

- The top-level Helm chart includes the License Service. For more information on the
 configuration requirements for this service, refer to the release notes.
- You can specify data table IDs as variables in dashboards. For more information, refer to
 Using
 Data Tables as Dashboard Variables .
- You can customize, filter, save, and load views in the
 Products grid.
- You can upload and view files associated with a product.
- You can filter the Executions grid by date ranges and
 workspaces.

##### November 2022

Explore the
 November 2022 SystemLink Enterprise update for uploading
 files.

- You can upload files up to 10 GB through the web interface.

<!--NI_TOPIC bundle=systemlink-enterprise path=publishing-a-jupyter-notebook.html language=enus -->
## TOPIC 00084: Publishing a Jupyter Notebook

- bundle_id: `systemlink-enterprise`
- source_path: `publishing-a-jupyter-notebook.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/publishing-a-jupyter-notebook.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Publish a Jupyter Notebook (.ipynb) to SystemLink Enterprise so you can use the notebook for a data analysis and for visualizations. Navigate to Analysis Scripts . Right-click the notebook you want to share and select Publish to SystemLink. Select the workspace you want to share the notebook to. Spe

### Publishing a Jupyter Notebook

Publish a Jupyter Notebook (.ipynb) to SystemLink Enterprise so you can use the notebook for a data analysis and for
 visualizations.

1. Navigate to Analysis»Scripts.
2. Right-click the notebook you want to share and select Publish to
 SystemLink.
3. Select the workspace you want to share the notebook to.
4. Specify the interface where you intend to use the notebook.
5. Click Publish to SystemLink.

- In SystemLink Enterprise , select the file and click
 Analyze .
- In Jupyter Notebook, click Analysis Development and select the
 workspace.

You can interact with notebooks using the following interfaces.

Note

SystemLink Enterprise

| Interface | Description | Inputs | Outputs |
| --- | --- | --- | --- |
| Assets Grid | This interface is not in use. | — | — |
| Data Space Analysis | You can use this interface on notebooks to analyze the parametric data in a data space and calculate statistics. | trace_data: Dict[string, string]This input is data from the plotted dataspace traces for the analysis. The data stores as a notebook execution artifact. Data takes the following format: {'artifact_id': 'artifact_id'}.The following is an example: {'artifact_id': '09875b26-3081-496a-9f62-07d3f8daf47e'} analysis_options: string[] workspace_id: string | This output is a list of analysis options the corresponding notebook provides. The list takes the following format: [{display_name: `Analysis 1`, id: `analysis_1`, type: scalar/vector} ...] . The following is an example: [{display_name: `Min`, id: `min`, type: scalar}] |
| File Analysis | You can use this interface on notebooks to analyze a file or create a routine with a file change trigger. | file_ids: string[] | No output required. |
| Periodic Execution | You can use this interface on notebooks to create a routine that executes on a repeatable cadence. This cadence starts at a specific date and a specific time. | No input required. | No output required. |
| Resource Changed Routine | You can use this interface on notebooks to create a routine that executes on a SystemLink resource changing. | context: dictThis input is a context dictionary. The dictionary contains the following information about a routine after a triggering event: routine_id: string—The ID of the routine that triggers the notebook. correlation_id: string—The correlation ID associated with the request to execute the notebook. Use this information to internally trace a request. triggered_at: string—The time value that represents when the system triggered the routine. This value is an ISO 8601 string in UTC. resource_type: string—The type of resource that triggered the routine. before: dict—A snapshot of the resource before a change. This input does not have a value if the routine triggers from a resource under creation. after: dict—A snapshot of the resource after a change. This input does not have a value if the routine triggers from a resource under deletion. | No output required. |
| Specification Analysis | You can use this interface on notebooks to analyze your chosen specifications. | spec_ids: string[] product_id: string | No output required. |
| Systems Grid | You can use this interface on notebooks to display custom information as a column in the Systems application. | No input required. | The output must have: A data_frame type. A one-element list that contains the result inside the data field. The data field is a dictionary that contains a list in the values field. This list contains the minion IDs and any minion ID associated values. The following is an example: [{type:"data_frame", data:{values:[["minion-id-1", 3], ["minion-id-2", 0]]}}] |
| Test Data Analysis | You can use this interface on notebooks to analyze your chosen test results. | result_ids: string[] | No output required. |
| Test Data Extraction | You can use this interface on notebooks to extract parametric data from files with specific formats (BDC, STDF). The interface transforms the data into test results, steps, and measurements. | file_id: string part_number: string notebook_id: string | No output required. |
| Work Item Operations | You can use this interface on notebooks that the system invokes through the action of a work item execution. | workItemId: string systemId: string The action of a work item execution might also pass user-defined parameters to the notebook | No output required. |
| Work Item Automations | You can use this interface on notebooks to perform automated actions on one or more work items for customer specific use cases. | work_item_ids: string[] | No output required. |
| Work Item Scheduler | You can use this interface on notebooks to schedule work items using an algorithm. You can customize your algorithms to meet the scheduling methodology of the lab. | work_item_ids: string[] | No output required. |

Parent topic:

Reporting Data with Jupyter Notebooks

Related tasks:

- Automating Work Items with Jupyter Notebook

<!--NI_TOPIC bundle=systemlink-enterprise path=queuing-jobs.html language=enus -->
## TOPIC 00085: Queuing Jobs for Offline Systems

- bundle_id: `systemlink-enterprise`
- source_path: `queuing-jobs.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/queuing-jobs.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Specify actions for managed systems to perform after they connect to SystemLink. Navigate to Systems Management Systems . Select the system you want to queue jobs for. Use the Systems toolbar options to configure any changes to the system the same way you would for an online system. You can queue th

### Queuing Jobs for Offline Systems

Specify actions for managed systems to perform after they connect to SystemLink.

1. Navigate to Systems Management»Systems.
2. Select the system you want to queue jobs for.
3. Use the Systems toolbar options to configure any changes to the system the same way you
 would for an online system. 
 You can queue the following changes offline:
  - Refresh the system
  - Change the password
  - Restart the system
  - Configure startup settings
  - Lock or unlock the system
  - Configure the hostname
  - Change the system description
4. To view your queued or past jobs, select a system, click View,
 and open the Jobs tab. 
 Any jobs you specify for disconnected systems appear as
 In-Queue until the system connects to SystemLink.

Parent topic:

Managing Your Systems

Related tasks:

- Managing Your Systems
- Modifying the Settings of a System

<!--NI_TOPIC bundle=systemlink-enterprise path=reporting-data-with-jupyter-notebooks.html language=enus -->
## TOPIC 00086: Reporting Data with Jupyter Notebooks

- bundle_id: `systemlink-enterprise`
- source_path: `reporting-data-with-jupyter-notebooks.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/reporting-data-with-jupyter-notebooks.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Develop interactive reports with Jupyter Notebooks. Use reports to visualize and analyze test and measurement data. You can also use reports to visualize asset utilization. You can execute notebooks in JupyterHub, dashboards, or Asset Manager. The notebooks communicate the results as graphical repor

### Reporting Data with Jupyter Notebooks

Develop interactive reports with Jupyter Notebooks. Use reports to visualize and
 analyze test and measurement data. You can also use reports to visualize asset
 utilization.

You can execute notebooks in JupyterHub, dashboards, or Asset Manager. The notebooks
 communicate the results as graphical reports in the environment where you executed the
 notebooks.

Before you start implementing your reporting goals, make sure
 you have the necessary privileges for all resources involved, such as the data you want to
 report.

Use the following topics to complete the
 tasks that best suit your goals.

- [Creating a Notebook in Jupyter Notebooks](creating-a-new-jupyter-notebook.html) Create a notebook ( .ipynb ) in JupyterHub to visualize, analyze, and process data.
- [Creating a Custom Script for Analyzing Parametric Data](creating-custom-script-analyzing-param-data.html) Modify the default Jupyter Notebook, Data Space Analysis , to meet your parametric data analysis needs.
- [Publishing a Jupyter Notebook](publishing-a-jupyter-notebook.html) Publish a Jupyter Notebook ( .ipynb ) to SystemLink Enterprise so you can use the notebook for a data analysis and for visualizations.
- [Installing Additional Python Modules](installing-python-modules.html) Use third-party Python modules to customize your test reports.
- [Analyzing Files with Jupyter Notebook](analyzing-files-with-jupyter-notebooks.html) Process data in files using Jupyter Notebook to generate high-level insights about your data.
- [Extracting Data from Files with Jupyter Notebooks](extracting-data-from-files-with-jupyter-notebooks.html) Extract data from files in SystemLink using Jupyter notebooks.

Related information:

- Jupyter

<!--NI_TOPIC bundle=systemlink-enterprise path=scheduling-a-test-plan-to-fixtures.html language=enus -->
## TOPIC 00087: Reserving Fixtures for a Work Item

- bundle_id: `systemlink-enterprise`
- source_path: `scheduling-a-test-plan-to-fixtures.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/scheduling-a-test-plan-to-fixtures.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use SystemLink Enterprise to reserve one or more fixtures under a system for a work item. Introduced in April 2025 A single test system in a lab can test multiple DUTs in parallel. DUTs connect to a test system through fixtures. A fixture is a dedicated space or a connection for the DUT on the test

### Reserving Fixtures for a Work Item

Use SystemLink Enterprise to reserve one or more fixtures under a
 system for a work item.

Introduced in April 2025

A single test system in a lab can test multiple DUTs in parallel. DUTs connect to a test
 system through fixtures. A *fixture* is a dedicated space or a connection for
 the DUT on the test setup.

Depending on the nature of the DUT or the test system setup, you might use different
 terminologies. Your lab might call a fixture a *slot*, a *socket*,
 or a *channel*.

Apart from scheduling a work item to a system, you can reserve slots, sockets, and
 channels for the work item. For example, a 12-slot battery test system can have multiple
 configurations based on the size and dimensions of the DUTs. A battery cell might need
 one slot while a large battery pack or a large battery module might need multiple
 slots.

You can give your fixtures meaningful names that include words such as
 slot, socket, or
 channel. The following are recommendations for fixture
 names:

- Use standard naming conventions for fixtures across all systems in your lab.
- Use names that explain the purpose of a fixture. For example, you can name your
 fixtures Slot_01 , Socket_01 , or
 Channel_01 .
- Maintain the numerical order of your fixture names by using 2 or 3 digits. For
 example, instead of naming a fixture Slot_1 and
 Slot_2 , use Slot_01 and
 Slot_02 . Using this numbering system allows the
 scheduling assistant to order the fixture names alphabetically.

Parent topic:

Managing Work Orders and Work Items

#### Adding Fixtures to a System

Add fixtures as assets under the test system.

1. Open SystemLink Enterprise.
2. Navigate to Systems Management»Systems.
3. Select the system you want to model a fixture under.
4. Click the Assets tab.
5. Click Add Asset and model the slots, sockets, or
 channels as assets.
6. Set the asset type to Fixture.

Add
 Asset

Edit Asset

#### Scheduling a Work Item to a Fixture

Use the Scheduling Assistant to schedule a work item to a
 fixture.

1. Navigate to Operations»Work Items.
2. Select a work item and click Schedule to open the
 Scheduling Assistant.
3. In the Scheduling Assistant, use the following sections to
 select resources for your work item. 
 Table 14.Available Resources by SectionSection
 ResourceSystems
 Select and expand a system to select one or more
 fixtures.
 DUTs
 Select one or more DUTs.Note You cannot assign a Maintenance
 work item or a Calibration work item to a
 DUT.
 Assets
 Select one or more assets.
4. To reserve a fixture without reserving a system, select the fixture from the
 Assets tab.
5. To learn more about a fixture, hover over the fixture and click the info
 icon.
6. On the Schedule your work item here row, click and drag the work item to the
 desired time slot. 
 Note Time slots are based on the availability of the
 selected system, fixtures, DUTs, and assets.
7. Click Save.

From the Schedule page, you can drag work items from a fixture
 of one system to another system. If you reschedule a work item this way, slot
 assignments occur automatically.

Slot names determine assignments. For example, moving a work item in the
 Schedule page from Slot_01 in
 System A to System B reschedules that work
 item. For this automatic rescheduling to occur, System B must have
 a matching fixture name.

<!--NI_TOPIC bundle=systemlink-enterprise path=scheduling-a-test-plan.html language=enus -->
## TOPIC 00088: Scheduling a Work Item

- bundle_id: `systemlink-enterprise`
- source_path: `scheduling-a-test-plan.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/scheduling-a-test-plan.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the scheduling assistant to schedule a work item based on which resources are available. Before you schedule a work item, create the work item. Find the work item you want to schedule. See all work items. Navigate to Operations Work Items . You can filter the list of existing work items by click

### Scheduling a Work Item

Use the scheduling assistant to schedule a work item based on which resources are
 available.

Before you schedule a work item, create the work
 item.

1. Find the work item you want to schedule. 
 OptionDescriptionSee all work items.
 Navigate to Operations»Work Items.
 You can filter the list of existing work
 items by clicking the summary tiles at the top of the page.See work items for a specific work order.
 Navigate to Operations»Work Orders.
 Click the work order for which you want to schedule a work
 item.
 Click Work Items.See work items for a specific product.
 Navigate to Product Insights»Products.
 Click on the product for which you want to schedule a work
 item.
 Click Work Items.See all work items created for that specific DUT.
 Navigate to Systems Management»Assets.
 Click the DUT for which you want to schedule a work item.
 Click Work Items.
2. Select a work item.
3. Click Schedule.
4. In the Scheduling Assistant, use the following sections to
 select resources for your work item. 
 Table 13.Available Resources by
 SectionSection
 ResourceSystems
 Select and expand a system to select one or more
 fixtures.
 DUTs
 Select one or more DUTs.Note You cannot assign a Maintenance
 work item or a Calibration work item to a
 DUT.
 Assets
 Select one or more assets.Note SystemLink adds shading to the top row to
 indicate if another work item overlaps in terms of scheduling for the
 selected resource.
5. In the top row, click and drag the work item to the correct time slot.
6. Click Save.

Operations

»

Schedule

Parent topic:

Managing Work Orders and Work Items

Related tasks:

- Automating Work Items with Jupyter Notebook
- Viewing Scheduled Work Items

Related information:

- SystemLink Examples on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=search-by-location.html language=enus -->
## TOPIC 00089: Searching SystemLink by Location

- bundle_id: `systemlink-enterprise`
- source_path: `search-by-location.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/search-by-location.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Display all assets or systems at a location. Navigate to Systems Management Systems or Assets . Refer to the following table for the steps that best suit your use case. Search by location In the Search bar, your search extends beyond locations and into other areas such as properties and serial numbe

### Searching SystemLink by Location

Display all assets or systems at a location.

1. Navigate to Systems Management»Systems or Assets.
2. Refer to the following table for the steps that best suit your use case. 
 OptionDescriptionSearch by location
 In the Search bar, your search extends beyond locations and into
 other areas such as properties and serial numbers.
 Click the Search bar.
 Enter a location name.Query by location
 In the Query builder, you can specify that the query looks for
 systems or assets within a location.
 Click [IMAGE alt='Filter icon.' src='GUID-731A5124-8F1A-4C37-AB46-A92BD043BE9B-a5.png'].
 In the Configure query slide-out, set the
 filter variable to Location.
 Set the variable to a location name.
 Click OK.
3. Review the list of assets or systems.

Parent topic:

Managing Your Locations

<!--NI_TOPIC bundle=systemlink-enterprise path=service-performance-specifications.html language=enus -->
## TOPIC 00090: Service Performance Specifications

- bundle_id: `systemlink-enterprise`
- source_path: `service-performance-specifications.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/service-performance-specifications.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about the performance of SystemLink services.

### Service Performance Specifications

Learn about the performance of SystemLink services.

- [Performance of the Test Monitor API on PostgreSQL](test-monitor-api-performance-on-postgresql.html) Learn about the query and ingestion performance of Test Monitor APIs on PostgreSQL for four common test data scenarios.
- [Data Extraction Performance for Standard Files](data-extraction-performance-for-standard-files.html) Learn how SystemLink Enterprise performs when extracting test data from standard files.

<!--NI_TOPIC bundle=systemlink-enterprise path=setting-up-systemlink-client.html language=enus -->
## TOPIC 00091: Setting up a SystemLink Client

- bundle_id: `systemlink-enterprise`
- source_path: `setting-up-systemlink-client.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/setting-up-systemlink-client.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Install SystemLink Client to establish a connection between your SystemLink server and a remote target. Before setting up a client, ensure the following: You have installed SystemLink Enterprise on your cluster. You have configured any remote database connections. Changing your database configuratio

### Setting up a SystemLink Client

Install SystemLink Client to establish a connection between your SystemLink server and
 a remote target.

- You have installed SystemLink Enterprise on your cluster.
- You have configured any remote database connections. Changing your database
 configuration after connecting a client can cause data loss.
- (Linux Real-Time only) On the host machine, you have installed drivers you need to
 communicate with your NI LinuxRT device:
  - To set up a CompactRIO Linux RT target, install NI CompactRIO and Drivers.
  - To set up a PXI RT System, install PXI Platform Services.

1. Use the following table to complete the steps that suit your target type. 
 OptionDescriptionWindows
 On a Windows target, launch NI Package Manager.
 Search for and install NI SystemLink Client.
 Launch NI SystemLink Client.
 Select Connect to a SystemLink server.
 Specify the host name, IP address, or DNS alias of the SystemLink server to
 which you want to connect.Linux Real-Time
 On the host machine, launch NI MAX.
 Ensure the firmware on the target is 7.0 or higher.
 Ensure that the date and time are correct.
 In NI MAX, right-click the target and select
 Format Disk.
 Click Add/Remove Software and install the
 Linux RT System Image.
 Under SystemLink Settings, ensure the DNS
 alias and Server are correct.
 Note Assign a strong password for the admin user on NI Linux
 Real-Time targets managed by SystemLink Enterprise. These
 credentials are required in the following scenarios.You SSH into the target.
 A SystemLink server adds a Linux Real-Time target to its collection of managed
 systems.
2. Log in to SystemLink.
3. Click Systems Management»Systems and click the pending tile.
4. Select the Minion IDs for the systems you want to add and click
 Next.
5. Select the workspace you want to add your systems to. 
 This action determines which resources the system can interact with. To learn more
 about workspaces, refer to the access control help. 
 When you add a system to a workspace, all data the system produces stores in the
 workspace. SystemLink also adds all assets of that system to the workspace.
6. Click Add. 
 The systems are now clients of the SystemLink server. To manage
 the client, click Systems Management»Systems. The following image displays an example list of clients that are
 connected to a server.[IMAGE alt='Systems Management page listing connected and disconnected clients and their system details.' src='GUID-205ADD10-38FE-43DC-8450-D46AE237EC2F-a5.png']
7. Optional: 
 Lock your client to prevent the execution of unwanted actions. 
 Unwanted actions include any operation performed through SystemLink that might disrupt
 a running test. 
 
 The jobs join a queue but do not execute until you unlock the system. You can
 view all jobs, including queued jobs, under History.
  1. Select the client in Systems.
  2. Click More»Lock.

Parent topic:

Managing Your Systems

Related tasks:

- Managing Access to SystemLink Enterprise

Related information:

- NI CompactRIO
- PXI Platform Services

<!--NI_TOPIC bundle=systemlink-enterprise path=sharing-data-across-systems.html language=enus -->
## TOPIC 00092: Sharing Data across Systems

- bundle_id: `systemlink-enterprise`
- source_path: `sharing-data-across-systems.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/sharing-data-across-systems.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Share or move data on the SystemLink platform. You can transfer data using one of the following approaches. Use the SystemLink data services. Connect to external systems and software using APIs. Refer to the following topics to determine how to share or move data on the SystemLink platform.

### Sharing Data across Systems

Share or move data on the SystemLink platform.

- Use the SystemLink data services.
- Connect to external systems and software using APIs.

- [Storing and Managing Files](storing-and-managing-files.html) View and manage all files in the central SystemLink File Ingestion Service with the dedicated Files application.
- [Communicating Data with Tags](communicating-data-with-tags.html) Communicate and manage data from your test and measurement systems with tags. Tags in SystemLink transmit and store slow-moving measurement data like system status or health. Use tags to track measurements, monitor system health, create alarms, and visualize data on dashboards.
- [Connecting to Clients](connecting-clients.html) Exchange data between clients like LabVIEW and SystemLink using SystemLink data services. Access these data services through the Data Communication palette in LabVIEW and LabVIEW NXG.
- [Generating Custom Alarms](generating-custom-alarms.html) Create alarms from a LabVIEW VI to notify you of system issues.
- [Monitoring Alarms](monitoring-alarms.html) Monitor, acknowledge, and clear alarms in your system.
- [Hosting a Web Application](hosting-a-web-application.html) Host a web application in SystemLink Enterprise and share it with other users.

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=specification-compliance.html language=enus -->
## TOPIC 00093: Specification Compliance

- bundle_id: `systemlink-enterprise`
- source_path: `specification-compliance.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/specification-compliance.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Specification Compliance Module (SCM) to ensure your products meet design requirements throughout their life cycle. A specification in SystemLink, is complimentary to, and often connected with, a product requirement that you are managing with a traditional requirements management tool. The S

### Specification Compliance

Use the Specification Compliance Module (SCM) to ensure your products meet design
 requirements throughout their life cycle.

A specification in SystemLink, is complimentary to, and often connected with, a
 product requirement that you are managing with a traditional requirements
 management tool. The SCM enables you to connect product requirements with
 test data in a way that allows for repeatable analysis.

- Specification storage and management: Maintain a central
 repository of specifications. A specification might already
 be part of a product requirement that you manage in a
 traditional requirements management tool.
- Specification compliance: Connect specifications with product
 test data to produce a compliance matrix for your
 products.

For information about the structure of specifications in SystemLink and how to
 use the specifications, browse the following topics.

- [Structure of a Specification](structure-of-a-specification.html) Learn the detailed data structure of specifications in the Specification Compliance Module (SCM).
- [Creating and Editing Product Specifications through SystemLink](create-and-edit-spec-for-product.html) You can create or edit a product specification directly from the SystemLink user interface.
- [Adding Product Specifications through Jupyter Notebook and the SCM API](adding-specifications-to-product.html) You can add specifications for a product with Jupyter Notebook or by using the Specification Compliance Module (SCM) API.
- [Viewing Product Specifications](viewing-spec-details-for-product.html) View the specifications associated with a product and the detailed information within a specification document.
- [Creating, Viewing, and Managing Specification Conditions](create-view-manage-conditions.html) After creating a specification, you can add and edit specification conditions from the SystemLink user interface.
- [Connecting Test Data to Specifications](connecting-test-data-to-specifications.html) Link your test data to specifications so you can compare measurement results to specification limits.
- [Deleting Specifications](deleting-specifications.html) Remove one or more specifications from a product.
- [Analyzing Specification Compliance with Jupyter Notebook](analyzing-specification-compliance-with-jupyter-notebooks.html) Verify whether your products comply with specification requirements by analyzing product test results against the specification.

<!--NI_TOPIC bundle=systemlink-enterprise path=storing-and-forwarding-offline-data-from-client.html language=enus -->
## TOPIC 00094: Storing and Forwarding Test Data

- bundle_id: `systemlink-enterprise`
- source_path: `storing-and-forwarding-offline-data-from-client.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/storing-and-forwarding-offline-data-from-client.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the SystemLink Test Monitor Client to avoid data loss during network disruptions. A test system using the SystemLink Test Monitor Client requires a stable network connection to SystemLink. If you have an unstable connection, you can configure the Client avoid data loss.To maintain optimal memory

### Storing and Forwarding Test Data

Use the SystemLink Test Monitor Client to avoid data loss during network
 disruptions.

To maintain optimal memory usage and storage
 availability regardless of losing offline data, use the default configuration of the
 plug-in.

1. Open TestStand on the managed system you want to store offline data during network
 disruptions.
2. Select Configure»Result Processing.
3. For NI SystemLink Test Monitor Client, click Options [IMAGE alt='Options button icon (wrench and screwdriver).' src='GUID-A0F49F02-CE84-4AA9-8532-C76914258CA8-a5.png'].
4. Choose the option that best meets your needs. 
 OptionDescriptionStore all test data on the client regardless of connection status, memory
 consumption, and storage space. Automatically forward this data in batches whenever
 the client is connected to SystemLink.
 Check Enable Storing and Forwarding of Test Data and
 select Always.Store test data on the client only when the client is disconnected from
 SystemLink; for example, during a network interruption. Automatically forward this
 data to SystemLink when the client reconnects to it.
 Check Enable Storing and Forwarding of Test Data and
 select Only When Disconnected From Server.
5. Click OK.

Parent topic:

Monitoring Tests

<!--NI_TOPIC bundle=systemlink-enterprise path=storing-and-managing-files.html language=enus -->
## TOPIC 00095: Storing and Managing Files

- bundle_id: `systemlink-enterprise`
- source_path: `storing-and-managing-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/storing-and-managing-files.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: View and manage all files in the central SystemLink File Ingestion Service with the dedicated Files application. Navigate to Product Insights Files . Use the following table to determine how to organize and interact with files. Goal Task Transfer files from other clients, devices, or software to Sys

### Storing and Managing Files

View and manage all files in the central SystemLink File Ingestion Service with the
 dedicated Files application.

1. Navigate to Product Insights»Files.
2. Use the following table to determine how to organize and interact with files. 
 Goal
 TaskTransfer files from other clients, devices, or software to
 SystemLink using APIs.
 To move files between clients and SystemLink, choose a way
 to access the File Ingestion Service.
 Upload a file manually.
 Click Upload files.
 Choose a file.
 Click OK.
 Analyze a file at upload.
 Click Upload files.
 Choose one or more files.
 Expand the Analysis type drop-down, and select
 File analysis.
 Click Next.
 Expand the Notebooks drop-down and select the
 notebook you want to use.
 Click Analyze.
 Analyze a file.
 Select a file.
 Expand the Analyze drop-down and select
 Analyze. Note You can analyze up to 50
 files at a time.
 Expand the Notebooks drop-down and select the
 notebook you want to use.
 Click Analyze.
 View latest execution details of a file.
 Select a file.
 Expand the Analyze drop-down and select
 View latest execution details.
 Add properties to a file.
 Select a file.
 Click Settings.
 Click + Property.
 Enter a key and a value.Alternatively, you can automate this process using one of the APIs. Note Properties make it easier for
 you to find files in many SystemLink applications.
 Download one or more files manually.
 Select one or more files and click
 Download.
 View the properties or a preview of a file.
 Select a file and click View, if
 available. For a list of file formats supported for preview in SystemLink Enterprise, refer to *Related
 reference*.
 Copy a dashboard compatible link to an image file.
 Select an image file.
 If available, click View.Note For a list of file formats supported for preview in
 SystemLink Enterprise, refer to *Related
 reference*
 In the toolbar, click Copy image link.
 Use the link to load the image in a dashboard.
 Delete a file.
 Select one or more files, click
 Delete, and confirm your choice.Note Links to deleted files persist
 in the Test Results, Products, and
 Assets applications.
 Note SystemLink applications cannot access
 files in the File Ingestion Service that have dependency files, such as TDM files and
 TDX files. You must save files with dependency files in a separate folder using file
 rules.

Parent topic:

Sharing Data across Systems

Related reference:

- File Formats Supported in File Preview

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=structure-of-a-specification.html language=enus -->
## TOPIC 00096: Structure of a Specification

- bundle_id: `systemlink-enterprise`
- source_path: `structure-of-a-specification.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/structure-of-a-specification.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn the detailed data structure of specifications in the Specification Compliance Module (SCM). A specification is linked to a specific product and contains three primary categories of information. Properties Limits Conditions The following figure depicts the relationships between the three catego

### Structure of a Specification

Learn the detailed data structure of specifications in the Specification Compliance
 Module (SCM).

1. Properties
2. Limits
3. Conditions

[IMAGE alt='Diagram depicting the relationship between products, specifications, properties, conditions and limits.' src='GUID-6020AB32-3013-49C2-90C3-F28DD6E7474A-a5.svg']

#### Specification Properties

A specification has both standard properties and
 custom properties. Use the specification properties to identify individual
 specifications or group specifications into useful categories.

Standard
 properties are a component of every specification. The following tables lists the
 standard properties and their descriptions.

| Property | Description | Example |
| --- | --- | --- |
| Spec ID | An alphanumeric string that uniquely identifies the specification in the context of a particular product and workspace The Spec ID is the primary key that enables you to connect a specification to test results. | Spec001 |
| Name | The name of the specification | Output Voltage |
| Category | The group to which a specification belongsWhen you view specifications in the Specs tab for a product, SystemLink groups the specifications by Category. | Electrical Specifications |
| Type | The type of specification Specifications can be either PARAMETRIC or FUNCTIONAL. Parametric specifications define a set of numerical limits for product test data. Functional specifications define pass/fail criteria. | PARAMETRIC |
| Symbol | The engineering symbol that appears in a data sheet for the specification Use a shortened version or technical representation of the specification name. | Vout |
| Block | The functional or architectural block of the product to which the specification appliesFor example, in a system-on-chip, the block might be the micro-processor, the USB interface, or the memory subsystem. | Amplifier |
| Unit | The SI unit of the measured values in a parametric specificationThe unit can include the prefix if desired. For example, mV and V are both allowed. | V |
| Workspace | The workspace to which the specification belongsUsers can see specifications in workspaces that the users are members of. | My Lab Workspace |

You can add custom properties and keywords after creating a specification.
 Custom properties and keywords help you find and group specifications. The SCM
 tracks the date and time of specification updates and the user who made the
 updates.

#### Specification Limits

- When the limits change, you can compare previously measured values to the
 new limits without re-measuring.
- Instead of hard coding limits into your test code, you can pull limits into
 the test code directly from the specification. The SCM enables you to reuse
 your test code.

| Limit Type | Description |
| --- | --- |
| Minimum | A measured value less than the minimum limit is out of compliance. Use minimum limits when a specification must be guaranteed. |
| Maximum | A measured value that is greater than the maximum limit is out of compliance. Use maximum limits when a specification must be guaranteed. |
| Typical | Measured values are expected to have a statistical mean that is close to the typical limit. Use typical limits to denote a typical specification. You can use typical limits with or without the minimum and maximum limits. |

#### Specification Conditions

Conditions are the set of parameters that are
 controlled by the test environment and impact the measurements. The SCM represents
 conditions as a list of parameters and their values. Specification conditions
 dictate the circumstances under which you must run a test and collect a measurement.
 A *condition space* is the set of all Cartesian combinations of parameter
 values. You must run a test under each of these combinations.

| Parameters | Description |
| --- | --- |
| Name | The name of the conditionThis value must match the name for the condition in your test code. |
| Unit | The SI unit for the condition The unit can include the prefix. For example, the unit can be GHz or Hz. |
| Range | A list of numeric ranges for the conditionSystemLink supports a list of ranges so you can specify disjoint numeric ranges. For example, you can sweep a frequency with different step sizes in different ranges. |
| Discrete values | A list of individual values for the conditionUse discrete lists in addition to ranges or independently. When you use discrete lists along with ranges, the total set of values is the combination of the ranges and the discrete values. |

The following example shows a frequency condition in GHz that a
 mixture of disjoint ranges and discrete
 values.

```text
{
  "name": "Frequency",
  "value": {
    "unit": "GHz",
    "type": "NUMERIC",
    "range": [
      { "min": 1.0, "step": 1, "max": 5.0 },
      { "min": 5.0, "step": 0.1, "max": 7.0 },
      { "min": 7.0, "step": 1, "max": 10.0 }
    ],
    "discrete": [0.5, 10.1]
  }
}
```

| Attribute | Description |
| --- | --- |
| Name | The name of the conditionThis value must match the name for the condition in your test code. |
| Discrete values | A list of individual values for the conditionString condition values must be discrete values. |

```text
{
  "name": "Operating Mode",
  "value": {
    "discrete": ["High Gain", "Low Gain", "Passthrough"]
  }
}
```

Parent topic:

Specification Compliance

Related tasks:

- Creating, Viewing, and Managing Specification Conditions

<!--NI_TOPIC bundle=systemlink-enterprise path=structuring-your-test-data.html language=enus -->
## TOPIC 00097: Structuring Your Test Data

- bundle_id: `systemlink-enterprise`
- source_path: `structuring-your-test-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/structuring-your-test-data.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a cluster to structure the properties of your test step data. Structuring you test data ensures that the data displays correctly in Test Insights. Before you structure your test data, you need create a VI for acquiring test results. Test Monitor only supports displaying the TestStand data mod

### Structuring Your Test Data

Create a cluster to structure the properties of your test step data. Structuring you
 test data ensures that the data displays correctly in Test Insights.

Before you structure your test data, you need create a VI for
 acquiring test results.

Test Monitor only supports displaying the TestStand data model. Therefore, how you
 configure the key-value pairs for each property in the cluster determines whether your data
 displays correctly in Test Results.

On the client, create the following diagram in a VI to structure your test step data.

Customize the gray sections for your unique programming goals.

[IMAGE alt='LabVIEW diagram building a parameters array with key-value pairs for a SystemLink test step.' src='GUID-CB8D25A5-6F11-43E1-9E61-E869260C115A-a5.png']

1. The test step in control provides the test steps of your test
 program. The Property Node reads the Data property
 from the test steps.
2. The step parameters control provides the parameters of your test
 steps. Unbundle by Name returns the names of the step parameters.
3. The SystemLink Properties type definition contains the key-value
 pair structure you need to use for your step parameter properties.
4. Bundle By Name specifies the keys and values of each step parameter.
 These key-value pairs appear in Test Insights.
5. Build Array creates an array containing all the key-value properties
 of the step parameters.
6. In Place Element Structure uses Unbundle/Bundle Elements
 Border Nodes and Build Array to assemble the following
 components into a cluster structure: 
 Data from test step in
 Key-value properties from step parameters
7. The Property Node uses the cluster to display the data correctly in
 Test Monitor.

Acquiring Test Results

Create Test
 Step

Parent topic:

Acquiring Test Results

<!--NI_TOPIC bundle=systemlink-enterprise path=system-health-dashboard.html language=enus -->
## TOPIC 00098: Using the System Health Dashboard

- bundle_id: `systemlink-enterprise`
- source_path: `system-health-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/system-health-dashboard.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: The System Health Dashboard provides an out-of-the-box view of a system's status, active alarms, and connected instruments in SystemLink Enterprise. Use this dashboard to complete the following actions. Check that the system is online and operating normally. Identify any active alarms that require a

### Using the System Health Dashboard

The System Health Dashboard provides an out-of-the-box view of a system's status,
 active alarms, and connected instruments in SystemLink Enterprise.

Use this dashboard to complete the following actions.

- Check that the system is online and operating
 normally.
- Identify any active alarms that require attention.
- Review historical health trends to recognize recurring
 issues.
- Verify that connected instruments have undergone
 calibration and is ready for use.

1. In SystemLink Enterprise, open the
 System Health Dashboard by
 clicking View System Health on the
 Systems page toolbar.
2. Use filters to scope the dashboard to your area of
 responsibility. 
 Filters
 DescriptionWorkspace
 Sorts the list of available systems by
 workspace. Select the workspace that contains your
 test system.
 System
 Selects the specific system to display. The
 list only includes the systems under a
 workspace.
3. Review the system status panels at the top of the
 dashboard. 
 Dashboard Panel
 DescriptionSystem Name
 Displays the name of your selected system.
 Connection
 Status
 Displays the current connection state of the
 system.
 Locked Status
 Displays the current lock state of the
 system.
 System Health
 Displays the CPU, disk, and memory usage of the
 system.
4. Check for active alarms and review the health trend. 
 Dashboard Panel
 DescriptionActive Alarms
 Displays a table of alarms currently active on
 the selected system.
 The table includes the following columns.
 Alarm—The alarm name.
 Click this column to open the alarm details and
 take action.
 First occurrence—When
 the alarm was first triggered.
 Acknowledged by—The
 user who acknowledged the alarm.
 Severity—The current
 severity level of the alarm.
 Health History
 Displays a time-series chart that displays how
 the CPU, Disk, and Memory usage of a system has
 changed over a time range.
5. Verify the instruments connected to the system. 
 Dashboard Panel
 DescriptionInstruments
 Displays a table of instruments associated with
 the selected system.
 The table includes the following columns.
 Name
 Serial Number
 Model Name
 Vendor
 Firmware
 Type
 Location
 Calibration Due
 Date
 Calibration Status
6. Hover over charts to obtain details on individual data
 points.
7. Use the time range picker to adjust the time range for all
 panels. The default time range is Last 7
 days.
8. Apply column filters in tables to refine the displayed
 results.
9. Export the table data.
  1. On a dashboard panel, click the ellipsis
 ([IMAGE alt='Ellipsis (more options) menu icon on a dashboard panel.' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png']).
  2. Click Inspect»Data.
  3. Click Download
 CSV.

Parent topic:

Monitoring Tests

Related tasks:

- Using the Alarms Overview Dashboard
- Viewing Out of the Box (OOTB) Dashboards in SystemLink Enterprise

<!--NI_TOPIC bundle=systemlink-enterprise path=systemlink-client-requirements.html language=enus -->
## TOPIC 00099: SystemLink Client Requirements

- bundle_id: `systemlink-enterprise`
- source_path: `systemlink-client-requirements.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/systemlink-client-requirements.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: To use SystemLink Client to communicate with targets, your targets must meet the following requirements. Hardware Requirements 1 Hardware Requirements for Targets Using SystemLink Client Component Windows NI Linux Real-Time Processor Pentium 4 G1 (equivalent or better) Intel or ARM model RAM 2 GiB m

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

SystemLink Enterprise Requirements

<!--NI_TOPIC bundle=systemlink-enterprise path=systemlink-enterprise-examples.html language=enus -->
## TOPIC 00100: SystemLink Enterprise Examples

- bundle_id: `systemlink-enterprise`
- source_path: `systemlink-enterprise-examples.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/systemlink-enterprise-examples.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can find .NET, Python, and Jupyter Notebook examples in the SystemLink Enterprise GitHub repository. Use these examples to learn about the product or accelerate your own application development. Do not change the text in the <shortdesc> or the <p>. The "Examples" map should at minimum provide an

### SystemLink Enterprise
 Examples

You can find .NET, Python, and Jupyter Notebook examples in the SystemLink Enterprise GitHub repository. Use these examples to learn about
 the product or accelerate your own application development.

SystemLink Enterprise examples are located in the
 https://github.com/ni/systemlink-enterprise-examples
 GitHub repository.

| Example Name | Description |
| --- | --- |
| Test Monitor Results: Create Results and Steps | This example demonstrates how to use the API of the SystemLink Test Monitor. Use this example to create test results and steps. |
| Test Monitor Results: Delete Results | This example demonstrates how to use the API of the SystemLink Test Monitor. Use this example to delete test results. |

| Example Name | Description |
| --- | --- |
| Test Monitor Results: Create Results and Steps | This example demonstrates how to use the API of the SystemLink Test Monitor. Use this example to create test results and steps. |
| Test Monitor Results: Delete Results | This example demonstrates how to use the API of the SystemLink Test Monitor. Use this example to delete test results. |

| Example Name | Description |
| --- | --- |
| Data Space Analysis | This example demonstrates how to analyze parametric data in a data space and calculate statistics. |
| Specification Analysis | This example demonstrates how to use the Spec Service to query, analyze, and update specifications with the latest properties. |
| Test Results Analysis | This example demonstrates how to create a Number of Failures Pareto chart for test results. |
| Simple ETL | This example demonstrates how to use the SystemLink APIs to perform data extraction and normalization on a file. |

| Example Name | Description |
| --- | --- |
| Work Item Operations | This example demonstrates how to use the Work Item Operations interface to execute a work item. You can use this interface to run a test or process user-defined parameters. |
| Work Item Scheduler | This example demonstrates how to use the Work Item Scheduler interface with a custom algorithm. You can customize the scheduling algorithm to meet the scheduling methodology of your lab. |
| Work Item Automations | This example demonstrates how to use the Work Item Automations interface. You can use this interface to perform automated actions on one or more work items. |
| Dynamic Form Fields Configuration | This example demonstrates how to define a Dynamic Form Fields configuration. |

Related information:

- SystemLink Examples on GitHub
- SystemLink Python API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=systemlink-enterprise-interface.html language=enus -->
## TOPIC 00101: Navigating SystemLink Enterprise

- bundle_id: `systemlink-enterprise`
- source_path: `systemlink-enterprise-interface.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/systemlink-enterprise-interface.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find useful links on the SystemLink Enterprise home page. Use the navigation menu Navigation menu icon. to access all applications within SystemLink Enterprise. Use the account menu User profile icon. to change your language settings. Home page with navigation menu, user profile icon, and tiles for

### Navigating SystemLink Enterprise

Find useful links on the SystemLink Enterprise home page.

Use the navigation menu [IMAGE alt='Navigation menu icon.' src='GUID-76DDF849-A311-4441-B77C-3AC530C07A77-a5.png'] to access all applications within SystemLink Enterprise.
 Use the account menu [IMAGE alt='User profile icon.' src='GUID-6887DBEC-A1FD-4B61-8AD0-69B8BC5F40D6-a5.png'] to change your language settings.

[IMAGE alt='Home page with navigation menu, user profile icon, and tiles for Systems, Products, Test Plans, and Dashboards.' src='GUID-98522835-61B2-4FCE-9959-6010F73EE655-a5.png']

Home

- SystemLink Docs : Open the SystemLink Enterprise 
 User Manual on ni.com .
- SystemLink Client Download : Go to the download page
 for SystemLink Client on ni.com .
- API Documentation : Open the SystemLink REST API documentation
 specific to your instance of SystemLink Enterprise .

<!--NI_TOPIC bundle=systemlink-enterprise path=systemlink-enterprise-requirements.html language=enus -->
## TOPIC 00102: SystemLink Enterprise Requirements

- bundle_id: `systemlink-enterprise`
- source_path: `systemlink-enterprise-requirements.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/systemlink-enterprise-requirements.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: To use SystemLink Enterprise, your computer must meet certain requirements. Latest version of a supported browser: Chrome Firefox Edge (Chromium) Safari

### SystemLink Enterprise
 Requirements

To use SystemLink Enterprise, your computer must meet certain
 requirements.

- Latest version of a supported browser:
  - Chrome
  - Firefox
  - Edge (Chromium)
  - Safari

<!--NI_TOPIC bundle=systemlink-enterprise path=systemlink-enterprise-theory-of-operation.html language=enus -->
## TOPIC 00103: SystemLink Enterprise Theory of Operation

- bundle_id: `systemlink-enterprise`
- source_path: `systemlink-enterprise-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/systemlink-enterprise-theory-of-operation.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemLink Enterprise implements a server-client architecture to transmit data over a connected network between your systems and server. This is a Theory of Operation (TOP) template topic. CHECK IN AS to author a unique version for your product. Your TOP topic should provide a mental model for the u

### SystemLink Enterprise Theory of Operation

SystemLink Enterprise implements a server-client architecture to
 transmit data over a connected network between your systems and server.

The architecture of SystemLink Enterprise enables central
 coordination and management of the following:

- Test and measurement systems
- Assets
- Software
- Data

SystemLink Enterprise

[IMAGE alt='Diagram showing the connections between users, servers, the SystemLink architecture, and test systems.' src='GUID-63584D06-DDE6-47CD-9350-D08B611DC81B-a5.svg']

| Component | Description |
| --- | --- |
| Identity provider | Stores and verifies user identity so users log into the SystemLink Enterprise web application. SystemLink requires you to supply an identity provider that supports the OpenID Connect protocol. |
| Users | Access SystemLink Enterprise through an OpenID Connect identity provider. |
| Test systems | Execute test applications. SystemLink Enterprise can help you manage your test systems in the following ways. Install software at scale. Track connected assets. Automatically ingest the data produce by the test systems. SystemLink Enterprise manages the authentication and authorization of test systems with role-base access control. |
| Web server | Enforces log-in configuration and redirection, inactivity timeout, and session management. |
| API load balancer | Allows for high performance network communication directly into the Kubernetes cluster hosting SystemLink Enterprise. |
| Role-based access control | Provides strong isolation between different workspaces as well as privileges for systems, data, and analysis routines in SystemLink Enterprise. You can manage roles and workspace access through OpenID Connect user claims or direct assignment. |
| Systems management | Allows you to connect a test system to SystemLink Enterprise securely, manage system configuration and settings, and remotely install software. |
| Asset management | Allows you to track assets connected to test systems and calculate the utilization of those assets. SystemLink Enterprise retains asset data when you move an asset between systems. You can track asset utilization outside of the connected system or test application. |
| Test Insights | Ingests test steps and test results using a TestStand plug-in or API. You can organize test results by product. You can search test result by querying test meta data. You can also create higher level test metrics and data visualizations using integrations with analysis routines and SystemLink dashboards. |
| File ingestion | Allows you to store files on-premise or in the cloud and query the files without complex database syntax. You can access files through an API. Integration with Routines and Jupyter Notebooks enables you to perform custom analysis of files immediately upon upload. |
| DataFrame tables | Enables the normalization of disparate data and file formats into a columnar data structure. You can associate DataFrame tables with test results. Then, you can use DataFrame tables to visualize and to search data. |
| Analysis and report generation | Enables interactive and automated analysis routines of test data through Jupyter Notebooks. The routines can produce KPIs and computer analytics in dashboards. The routines can also produce HTML reports and PDF reports. |
| Kubernetes | Provides container orchestration, auto-scaling, and life cycle management for the various services, web applications, and the infrastructure that makes up SystemLink Enterprise. |

<!--NI_TOPIC bundle=systemlink-enterprise path=systemlink-enterprise.html language=enus -->
## TOPIC 00104: SystemLink Enterprise Overview

- bundle_id: `systemlink-enterprise`
- source_path: `systemlink-enterprise.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/systemlink-enterprise.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemLink Enterprise is scalable, self-hosted software for product engineers, production engineers, and lab managers working on a large corporate scale. Use SystemLink Enterprise to manage your automated test systems, data collection, and reporting from a central location. SystemLink Enterprise Key

### SystemLink Enterprise
 Overview

SystemLink Enterprise is scalable, self-hosted software for product
 engineers, production engineers, and lab managers working on a large corporate
 scale. Use SystemLink Enterprise to manage your automated test
 systems, data collection, and reporting from a central location.

#### SystemLink Enterprise Key
 Features

SystemLink Enterprise has the following features and
 capabilities.

- Systems management to perform operations such as the following:
  - Managing system health
  - Deploying software to multiple systems at once
- Asset management to track utilization, calibration information, and find assets.
- A Test Insights application to ingest test data and monitor performance and status.
- Data tables to normalize data from multiple formats so you can run analyses on all data in a
 common format.
- Dashboards to monitor systems and key performance indicators.
- Jupyter notebooks to automate analysis and the creation of HTML and PDF reports.
- Routines to trigger Jupyter notebook execution on configurable events or on a schedule.
- Role-based access control to simplify user management and access to data in a large
 organization.
- Kubernetes to manage container life cycle, reliability, and horizontal scaling.
- Helm charts to simplify installation.

<!--NI_TOPIC bundle=systemlink-enterprise path=systemlink-properties.html language=enus -->
## TOPIC 00105: SystemLink Predefined Properties

- bundle_id: `systemlink-enterprise`
- source_path: `systemlink-properties.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/systemlink-properties.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Predefined properties are user-facing key-value pairs that install with SystemLink and SystemLink APIs. You can call these properties in code and display their current values in the details area of the SystemLink web application for the following: Assets Systems Tags Tests You cannot delete predefin

### SystemLink Predefined Properties

Predefined properties are user-facing key-value pairs that install with SystemLink and
 SystemLink APIs.

- Assets
- Systems
- Tags
- Tests

Note

#### Predefined Properties

Refer to the
 following table to learn more about the predefined properties you can view and
 interact with in the SystemLink web application.

| Property | Full name or key | Description | API | Example value |
| --- | --- | --- | --- | --- |
| Path | path | Path to the tag referenceNote A tag path uses dot separators to separate each component of the path. For example, <system>.<namespace>.<tag>. | Tag | 39a98f00-7200-461b-8a7r-e8c84dc3094d.Throughput_Test.status |
| Current Value | value | Most recent value of the tag | Tag | June 04, 2019 2:34:04 AM CDT |
| Minimum Aggregate Value | min | Smallest value of a tag | Tag | 0 |
| Maximum Aggregate Value | max | Largest value of a tag | Tag | 69,905,949,604 |
| Mean Value | avg | Average value of a tag | Tag | 34,952,974,802 |
| Count | count | Number of times a tag produced a value | Tag | 11819 |
| Batch Serial Number | nitmBatchSerialNumber | Serial number assigned to a batch of DUTs or UUTs in TestStand | Test Monitor | 0123456789 |
| Serial Number | nitmSerialNumber | Serial number assigned to the DUT or UUT in TestStand | Test Monitor | 1E28B2D |
| Test Socket Index | nitmTestSocketIndex | Indexed number associated with a test socket | Test Monitor | 4 |
| Test Socket Count | nitmTestSocketCount | Total number of test sockets included in the TestStand test sequence | Test Monitor | 5 |
| Source | nitmSource | Software application that acquired the test results | Test Monitor | niteststand |
| Started At | nitmTestStandStartTime | Time when the test started running in TestStand | Test Monitor | 2019-04-29T14:37:26.467 |
| Test Program | nitmTestProgram | Name of the test program that executes the test steps | Test Monitor | Manufacturing Test.seq |
| Process Model | nitmProcessModel | Set of operations that establishes how TestStand performs a test on a DUT or UUT | Test Monitor | Sequential |
| Operator | nitmOperator | Person who executes the test | Test Monitor | Administrator |
| Batch ID | nitmBatchId | Identifier assigned to a batch of DUTs or UUTs in TestStand | Test Monitor | 1 |
| System Name | nitmSystemName | Name of the test system performing the test | Test Monitor | VirtualBox--MAC-08-00-27-C1-70-57 |
| Hostname | nitmHostname | Name assigned to the device | Test Monitor | localhost |
| Part Number | nitmPartNumber | Unique number assigned to a test device or asset | Test Monitor | 154119E-01L |
| Product | nitmProduct | Type of device under test | Test Monitor | cRIO-9030 |
| Value | value | Value associated with the process you start monitoring when the alarm condition is met | Alarm | 15 |
| Minion ID | minionId | Unique identifier associated with a client systemNote When you query the Alarm Service, it translates the minion ID into the hostname in the SystemLink web application. | Alarm Tag | cRIO-9068--SN-190D5D5--MAC-00-80-2F-15-AF-CC |

Parent topic:

Storing and Managing Files

Related tasks:

- Visualizing Notebook Data on a Dashboard

<!--NI_TOPIC bundle=systemlink-enterprise path=test-monitor-api-performance-on-postgresql.html language=enus -->
## TOPIC 00106: Performance of the Test Monitor API on PostgreSQL

- bundle_id: `systemlink-enterprise`
- source_path: `test-monitor-api-performance-on-postgresql.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/test-monitor-api-performance-on-postgresql.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about the query and ingestion performance of Test Monitor APIs on PostgreSQL for four common test data scenarios. Scenario Description Performance Summary High Mix-Low Volume Many products with low steps volume Average number of steps ingested when ingesting 100 steps per request is 636 steps

### Performance of the Test Monitor API on
 PostgreSQL

Learn about the query and ingestion performance of Test Monitor APIs on PostgreSQL
 for four common test data scenarios.

| Scenario | Description | Performance Summary |
| --- | --- | --- |
| High Mix-Low Volume | Many products with low steps volume | Average number of steps ingested when ingesting 100 steps per request is 636 steps per second Average response time for queries on the Product, Results, and Steps grids is less than 1 second Average response time for queries on simple data spaces with filters on Part number and Program name is less than 1 second Data spaces queries with filters on Part number contains take more than 30 seconds exceeding the timeout threshold PostgreSQL storage used for 25 million step records is 65.1 GB with an average step size of 2.71 KB |
| Low Mix-High Volume | Few products with high steps volume | Average number of steps ingested when ingesting 500 steps per request is 1082 steps per second Average response time for queries on the Product, Results, and Steps grids is less than 1 second Average response time for queries on the Steps grid is 2 seconds Average response time for queries on simple data spaces with filters on Part number and Program name is less than 1 second Data spaces queries with filters on Contains, Metadata, Input condition, and Path take more than 30 seconds exceeding the timeout threshold PostgreSQL storage used for 25 million step records is 46.1 GB with an average step size of 1.93KB |
| Low Mix-Medium Volume | Few products with high results volume | Average number of steps ingested when ingesting 100 steps per request is 594 steps per second Average response time for queries on the Product and Steps grids is less than 1 second Average response time for queries on the Results grid is 2 seconds Average response time for queries on simple data spaces with filters on Program name and Metadata equals is 7 seconds Data spaces queries with filters on Part number contains, Input condition, Product name, and Metadata contains take more than 30 seconds exceeding timeout threshold PostgreSQL storage used for 25 million step records is 50.2 GB with an average step size of 2.1 KB |
| Low Mix-Very High Volume | Single product with very high result and step volume | Average number of steps ingested when ingesting 500 steps per request is 1058 steps per second Average response time for queries on the Product, Results, and simple Steps grids is 1 second Average response time for queries on the Steps grid with filters on properties like Step name contains/equals/not null is 5 seconds Average response time for queries on simple data spaces with filters on Part number and Program name is less than 1 second Data spaces queries with filters on Contains, Input condition, and Metadata take more than 30 seconds exceeding the timeout threshold PostgreSQL storage used for 25 million step records is 46 GB with an average step size of 1.93 KB |

#### Control
 Conditions

NI evaluated the performance of the Test Monitor API for each
 scenario under the following infrastructure and measurement conditions.

- A Test Monitor service deployed and managed by Kubernetes (AWS EKS) with the
 following specifications. Specification
 DescriptionNode specification
 Type: r6a.4x large​
 vCPU: 16
 RAM: 128 GiB
 Pod specification
 CPU: 250 m
 Memory: 320 Mi (up to 512 Mi)
 Pod Replication
 Auto scale default: 2
 Auto scale maximum: 10
- A Test Monitor database with the following specifications. Database Specification
 DescriptionSource
 Single Instance of RDS PostgreSQL
 Specifications
 PostgreSQL version: 14.5
 Instance class: db.t4g.xlarge
 vCPU: 4
 RAM: 16 GB
- Data uploaded from an EC2 instance into a PostgreSQL database in the same AWS
 cluster to remove any network latency. Data was uploaded as products, results
 and steps.
- Queries for the following workflows from the Test Insights UI.
  - Product grid queries to view and filter products based on part number,
 product details, and metadata.
  - Results grid queries to view and filter results based on part number,
 result details, and metadata.
  - Steps grid queries to view and filter steps based on step name and
 measurement name.
  - Data spaces queries to filter and retrieve step details for
 visualization. Filters can include advanced LINQ filters, result
 metadata, step metadata, and condition filters.

#### Variable
 Conditions

NI evaluated the performance of the Test Monitor API under the
 following different dataset conditions.

| Dataset size | 5M | 10M | 15M | 20M | 25M |
| --- | --- | --- | --- | --- | --- |
| Number of Steps | 5 Million | 10 Million | 15 Million | 20 Million | 25 Million |
| Number of Products | 250 | 500 | 750 | 1000 | 1250 |
| Number of Results per Product | 200 | 200 | 200 | 200 | 200 |
| Number of Steps per Result | 100 | 100 | 100 | 100 | 100 |

| Dataset size | 5M | 10M | 15M | 20M | 25M |
| --- | --- | --- | --- | --- | --- |
| Number of Steps | 5 Million | 10 Million | 15 Million | 20 Million | 25 Million |
| Number of Products | 1 | 2 | 3 | 4 | 5 |
| Number of Results per Product | 313 | 313 | 313 | 313 | 313 |
| Number of Steps per Result | 16000 | 16000 | 16000 | 16000 | 16000 |

| Dataset size | 5M | 10M | 15M | 20M | 25M |
| --- | --- | --- | --- | --- | --- |
| Number of Steps | 5 Million | 10 Million | 15 Million | 20 Million | 25 Million |
| Number of Products | 50 | 50 | 50 | 50 | 50 |
| Number of Results per Product | 1000 | 2000 | 3000 | 4000 | 5000 |
| Number of Steps per Result | 100 | 100 | 100 | 100 | 100 |

| Dataset size | 5M | 10M | 15M | 20M | 25M |
| --- | --- | --- | --- | --- | --- |
| Number of Steps | 5 Million | 10 Million | 15 Million | 20 Million | 25 Million |
| Number of Products | 1 | 1 | 1 | 1 | 1 |
| Number of Results per Product | 1000 | 1000 | 1000 | 1000 | 1000 |
| Number of Steps per Result | 5000 | 10000 | 15000 | 20000 | 25000 |

#### High
 Mix-Low Volume Scenario: Performance Details

In this scenario, the number
 of steps per result and number of results per product remains constant. Data scale
 is increased by adding more products.

| Ingestion Step | Average number of Steps ingested per second | Average number of requests per second |
| --- | --- | --- |
| 0 to 5 Million | 744 | 7.4 |
| 5 Million to 10 Million | 673 | 6.73 |
| 10 Million to 15 Million | 607 | 6.07 |
| 15 Million to 20 Million | 584 | 5.84 |
| 20 Million to 25 Million | 574 | 5.74 |

Figure 4.

[IMAGE alt='Histogram of request time per ingestion batch (0–5M to 20–25M steps).' src='GUID-C343948D-E3E9-4497-8C86-B1D1C734DBAC-a5.png']

Figure 5.

[IMAGE alt='CDF chart of ingestion request times for 0–5M to 20–25M steps, with a 2-sigma trend line.' src='GUID-0EFCC8FC-C4C2-4E1C-8B18-345330B0DD2A-a5.png']

| Filter applied | Take1 | Return count2 | 5M (seconds) | 10M (seconds) | 15M (seconds) | 20M (seconds) | 25M (seconds) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Products Grid Queries |  |  |  |  |  |  |  |
| Part number | 1000 | False | 0.064 | 0.056 | 0.108 | 0.093 | 0.062 |
| Family and Name | 1000 | False | 0.071 | 0.059 | 0.058 | 0.061 | 0.06 |
| Updated time | 1000 | False | 0.069 | 0.062 | 0.103 | 0.076 | 0.069 |
| Metadata | 1000 | False | 0.081 | 0.086 | 0.08 | 0.078 | 0.065 |
| No filter | 1000 | False | 0.075 | 0.063 | 0.064 | 0.062 | 0.066 |
| Results Grid Queries |  |  |  |  |  |  |  |
| Test program | 1000 | False | 0.164 | 0.286 | 0.328 | 0.502 | 0.363 |
| Part number | 1000 | False | 0.152 | 0.073 | 0.095 | 0.091 | 0.075 |
| Status | 1000 | False | 0.169 | 0.129 | 0.136 | 0.145 | 0.135 |
| Property | 1000 | False | 0.147 | 0.195 | 0.754 | 0.864 | 0.813 |
| Keyword | 1000 | False | 0.239 | 0.379 | 0.38 | 0.252 | 0.296 |
| Workspace | 1000 | False | 0.112 | 0.149 | 0.145 | 0.131 | 0.326 |
| Id | 1000 | False | 0.234 | 0.115 | 0.222 | 0.153 | 0.125 |
| No filter | 1000 | False | 0.185 | 0.276 | 0.591 | 0.444 | 0.268 |
| Count queries | 0 | True | 0.102 | 0.113 | 0.263 | 0.335 | 0.435 |
| Steps Grid Queries |  |  |  |  |  |  |  |
| Step name | 1000 | True | 0.068 | 0.076 | 0.075 | 0.084 | 0.104 |
| Measurement Name | 1000 | True | 0.069 | 0.089 | 0.093 | 0.088 | 0.093 |
| Measurement name and Step name | 1000 | True | 0.086 | 0.079 | 0.078 | 0.083 | 0.093 |
| Applying projections | 1000 | True | 0.08 | 0.086 | 0.069 | 0.095 | 0.074 |
| Step id | 1000 | True | 0.068 | 0.084 | 0.065 | 0.069 | 0.077 |
| Data Spaces Queries |  |  |  |  |  |  |  |
| Part number | 1000 or 10000 | False | 3.584 | 1.171 | 1.343 | 1.967 | 2.383 |
| Product name | 10000 | False | 1.662 | 2.022 | 2.043 | 2.97 | 3.101 |
| Part number and Test program | 10000 | False | 0.974 | 1.099 | 1.462 | 1.591 | 1.42 |
| Product name and Result status | 10000 | False | 1.949 | 1.685 | 1.945 | 2.258 | 2.532 |
| Part number and Result metadata | 1000 | False | 1.659 | 0.518 | 0.723 | 0.841 | 0.995 |
| Part number and Step status | 10000 | False | 1.587 | 2.322 | 2.238 | 2.147 | 1.855 |
| Part number, Test program and Step name | 1000 or 10000 | False | 0.111 | 0.143 | 0.171 | 0.413 | 0.218 |
| Part number and Paths | 1000 | False | 0.712 | 0.48 | 0.719 | 1.131 | 1.011 |
| Input conditions | 1000 | False | 0.539 | 0.764 | 1.238 | 1.957 | 1.721 |
| Part number (Path API) | 1000 | False | 2.604 | 7.255 | 11.738 | Timed out | Timed out |
| Part number and Program name (Path API) | 1000 | False | 0.105 | 0.147 | 0.219 | 0.141 | 0.13 |
| Part number contains | 10000 | False | 17.772 | Timed out | Timed out | Timed out | Timed out |
| 1Represents the take parameter in the query request body, which limits the number of records fetched. 2Represents the returnCount parameter in the query request body, which fetches the total count of records matching the applied filter if true. Note 6.7% of Data Spaces queries with the Part number contains filter returned 503 errors with an increase in data size. These errors indicate the resource limitations for Test Monitor service. |  |  |  |  |  |  |  |

[IMAGE alt='Line chart showing most Data Spaces queries complete in under 1 second across data sizes.' src='GUID-A0E4994B-28BA-4E62-BB4A-8BBE2FB9CD49-a5.png']

#### Low
 Mix-High Volume Scenario: Performance Details

In this scenario, the number
 of steps per result and number of results per product remain constant. Data scale is
 increased by adding more products.

| Ingestion Step | Average number of steps ingested per second | Average number of requests per second |
| --- | --- | --- |
| 0 to 5 Million | 1182 | 2.36 |
| 5 Million to 10 Million | 1138 | 2.28 |
| 10 Million to 15 Million | 1085 | 2.17 |
| 15 Million to 20 Million | 1017 | 2.03 |
| 20 Million to 25 Million | 990 | 1.98 |

[IMAGE alt='Histogram of request latency for 0–25M ingested steps, showing longer times as ingestion increases.' src='GUID-E34B5CF3-E6EF-4D96-8169-63E32D451BDD-a5.png']

[IMAGE alt='CDF of request latency by ingestion range (0–5M to 20–25M steps); higher ranges show longer latency.' src='GUID-DA87D4A9-F151-4B5A-B12D-C3536CE91735-a5.png']

| Filter applied | Take1 | Return count2 | 5M (seconds) | 10M (seconds) | 15M (seconds) | 20M (seconds) | 25M (seconds) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Products Grid Queries |  |  |  |  |  |  |  |
| Part number | 1000 | False | 0.088 | 0.084 | 0.066 | 0.088 | 0.056 |
| Family and Name | 1000 | False | 0.096 | 0.088 | 0.063 | 0.073 | 0.059 |
| Updated time | 1000 | False | 0.079 | 0.083 | 0.084 | 0.063 | 0.058 |
| Metadata | 1000 | False | 0.072 | 0.058 | 0.087 | 0.064 | 0.088 |
| No filter | 1000 | False | 0.082 | 0.059 | 0.063 | 0.099 | 0.064 |
| Results Grid Queries |  |  |  |  |  |  |  |
| Test program | 1000 | False | 0.086 | 0.08 | 0.094 | 0.093 | 0.092 |
| Part number | 1000 | False | 0.122 | 0.09 | 0.172 | 0.102 | 0.1 |
| Status | 1000 | False | 0.143 | 0.092 | 0.123 | 0.105 | 0.105 |
| Property | 1000 | False | 0.089 | 0.109 | 0.074 | 0.073 | 0.066 |
| Keyword | 1000 | False | 0.083 | 0.109 | 0.077 | 0.069 | 0.075 |
| Workspace | 1000 | False | 0.085 | 0.081 | 0.101 | 0.103 | 0.089 |
| Id | 1000 | False | 0.15 | 0.1 | 0.12 | 0.11 | 0.129 |
| No filter | 1000 | False | 0.08 | 0.113 | 0.15 | 0.126 | 0.127 |
| Count query | 0 | True | 0.082 | 0.082 | 0.077 | 0.075 | 0.065 |
| Steps Grid Queries |  |  |  |  |  |  |  |
| Step name | 1000 | True | 0.205 | 0.89 | 3.922 | 4.107 | 4.772 |
| Measurement Name | 1000 | True | 0.292 | 1.647 | 3.474 | 4.792 | 5.934 |
| Measurement name and Step name | 1000 | True | 0.17 | 0.749 | 3.42 | 2.742 | 4.565 |
| Applying projections | 1000 | True | 0.106 | 0.099 | 0.09 | 0.085 | 0.105 |
| Step id | 1000 | True | 0.107 | 0.079 | 0.104 | 0.092 | 0.096 |
| Data Spaces Queries |  |  |  |  |  |  |  |
| Part number | 1000 or 10000 | False | 1.15 | 1.381 | 1.073 | 1.172 | 1.086 |
| Product name | 10000 | False | 1.475 | 2.299 | 1.442 | 1.473 | 1.447 |
| Part number and Test program | 10000 | False | 1.698 | 2.059 | 1.48 | 1.448 | 1.749 |
| Product name and Result status | 10000 | False | 1.648 | 1.558 | 1.557 | 1.566 | 2.386 |
| Part number and Result metadata | 1000 | False | 0.594 | 0.843 | 2.065 | 1.008 | 2.492 |
| Part number and Step status | 10000 | False | 1.612 | 1.536 | 1.486 | 2.243 | 1.583 |
| Part number, Test program and Step name | 1000 or 10000 | False | 1.344 | 6.632 | 6.863 | 15.797 | 14.59 |
| Part number and Paths | 1000 | False | 0.273 | 2.648 | 1.217 | 0.32 | 1.095 |
| Input conditions | 1000 | False | 0.259 | 0.28 | 0.252 | 0.306 | 0.285 |
| Part number (Path API) | 1000 | False | 0.255 | 0.755 | 0.984 | 1.336 | 2.825 |
| Part number and Program name (Path API) | 1000 | False | 0.117 | 0.2 | 0.196 | 0.24 | 0.157 |
| Input condition value - equals | 1000 | False | 17.45 | Timed out | Timed out | Timed out | Timed out |
| Program name - Contains | 1000 or 10000 | False | 2.281 | Timed out | Timed out | Timed out | Timed out |
| Result metadata - Contains | 1000 | False | 2.355 | Timed out | Timed out | Timed out | Timed out |
| 1Represents the take parameter in the query request body, which limits the number of records fetched. 2Represents the returnCount parameter in the query request body, which fetches the total count of records matching the applied filter if true. Note 8.7% of Data Spaces queries with filters like Program name contains, Result metadata contains, and Input condition value equals returned 503 errors, which indicates the resource limitations for Test Monitor service. |  |  |  |  |  |  |  |

[IMAGE alt='Histogram of query elapsed time, showing peaks near 0 seconds and at 30 seconds for 5M–25M.' src='GUID-706634F9-8426-415E-9D39-5A7902B5D76B-a5.png']

#### Low
 Mix-Medium Volume Scenario: Performance Details

In this scenario, the
 number of steps per result and number of products remain constant. Data scale is
 increased by adding new results under existing products.

| Ingestion Step | Average number of steps ingested per second | Average number of requests per second |
| --- | --- | --- |
| 0 to 5 Million | 727 | 7.27 |
| 5 Million to 10 Million | 590 | 5.9 |
| 10 Million to 15 Million | 572 | 5.72 |
| 15 Million to 20 Million | 541 | 5.41 |
| 20 Million to 25 Million | 539 | 5.39 |

[IMAGE alt='Histogram of request times for each 5M ingestion batch; peaks shift right as batches increase.' src='GUID-25C252A0-C3A2-4272-AC16-2029A87985E0-a5.png']

[IMAGE alt='CDF of request times by ingestion batch; curves shift right as ingestion volume increases.' src='GUID-8C51497E-30C8-41CE-901D-83EB40819CBC-a5.png']

| Filter applied | Take1 | Return count2 | 5M (seconds) | 10M (seconds) | 15M (seconds) | 20M (seconds) | 25M (seconds) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Products Grid Queries |  |  |  |  |  |  |  |
| Part number | 1000 | False | 0.081 | 0.064 | 0.077 | 0.072 | 0.104 |
| Family and Name | 1000 | False | 0.061 | 0.067 | 0.092 | 0.073 | 0.08 |
| Updated time | 1000 | False | 0.061 | 0.079 | 0.085 | 0.066 | 0.081 |
| Metadata | 1000 | False | 0.061 | 0.078 | 0.122 | 0.091 | 0.094 |
| No filter | 1000 | False | 0.065 | 0.067 | 0.058 | 0.095 | 0.055 |
| Results Grid Queries |  |  |  |  |  |  |  |
| Test program | 1000 | False | 0.2 | 0.541 | 1.811 | 1.482 | 1.878 |
| Part number | 1000 | False | 0.149 | 0.214 | 0.496 | 0.197 | 0.33 |
| Status | 1000 | False | 0.146 | 0.273 | 0.206 | 0.268 | 0.483 |
| Property | 1000 | False | 0.201 | 0.807 | 2.048 | 0.942 | 1.83 |
| Keyword | 1000 | False | 0.317 | 1.827 | 2.717 | 3.473 | 3.473 |
| Workspace | 1000 | False | 0.148 | 0.39 | 1.706 | 0.633 | 0.917 |
| Id | 1000 | False | 0.135 | 0.152 | 0.371 | 0.227 | 0.166 |
| No filter | 1000 | False | 0.259 | 0.662 | 1.741 | 1.323 | 1.269 |
| Count query | 0 | True | 0.131 | 0.315 | 2.001 | 0.869 | 2.574 |
| Steps Grid Queries |  |  |  |  |  |  |  |
| Step name | 1000 | True | 0.071 | 0.135 | 0.171 | 0.103 | 0.183 |
| Measurement Name | 1000 | True | 0.071 | 0.111 | 0.194 | 0.106 | 0.171 |
| Measurement name and Step name | 1000 | True | 0.069 | 0.113 | 0.289 | 0.122 | 0.217 |
| Applying projections | 1000 | True | 0.077 | 0.103 | 0.129 | 0.102 | 0.102 |
| Step id | 1000 | True | 0.081 | 0.085 | 0.149 | 0.102 | 0.133 |
| Data Spaces queries |  |  |  |  |  |  |  |
| Part number and Test program | 10000 | False | 0.427 | 1.124 | 2.571 | 1.035 | 3.897 |
| Part number and Result metadata | 1000 | False | 0.209 | 0.407 | 1.952 | 0.784 | 1.896 |
| Part number, Test program and Step name | 1000 or 10000 | False | 0.186 | 0.401 | 2.945 | 1.14 | 2.093 |
| Part number and Paths | 1000 | False | 0.784 | 4.956 | 7.993 | 5.836 | 8.107 |
| Part number (Path API) | 1000 | False | 10.452 | 20.032 | Timed out | 19.767 | 16.725 |
| Part number and Program name (Path API) | 1000 | False | 0.196 | 0.377 | 0.848 | 0.284 | 0.275 |
| Part number (equals and contains) | 1000 or 10000 | False | 9.1 | Timed out | Timed out | Timed out | Timed out |
| Input conditions | 1000 | False | Timed out | Timed out | Timed out | Timed out | Timed out |
| Product name | 10000 | False | 4.594 | Timed out | Timed out | Timed out | Timed out |
| Result metadata | 1000 | False | 6.167 | Timed out | Timed out | Timed out | Timed out |
| 1Represents the take parameter in the query request body, which limits the number of records fetched. 2Represents the returnCount parameter in the query request body, which fetches the total count of records matching the applied filter if true. Note 39% of Data Spaces queries with filters like Contains, Product name equals, Result metadata, and Input condition returned 503 errors. These errors indicate the resource limitations for Test Monitor service. |  |  |  |  |  |  |  |

[IMAGE alt='Histogram of Data Spaces query duration, showing most queries under 5 seconds and a spike at 30 seconds.' src='GUID-921B810D-D44D-4EA2-9B07-00F3EAF07F2A-a5.png']

#### Low
 Mix-Very High Volume Scenario: Performance Details

In this scenario, the
 number of products and number of results per product remain constant. Data scale is
 increased by adding new steps under existing results.

| Ingestion Step | Average number of steps ingested per second | Average number of requests per second |
| --- | --- | --- |
| 0 to 5 Million | 1184 | 2.37 |
| 5 Million to 10 Million | 1101 | 2.2 |
| 10 Million to 15 Million | 1052 | 2.1 |
| 15 Million to 20 Million | 999 | 2 |
| 20 Million to 25 Million | 953 | 1.91 |

[IMAGE alt='Histogram of request times for five 5M ingestion batches; curves shift right as total ingested increases.' src='GUID-E0C9547A-C488-4C35-B5A5-3B14BE191EAF-a5.png']

[IMAGE alt='CDF of ingestion request times for five 5M batches; curves shift right as total ingested increases.' src='GUID-45E2C1E2-B33A-4CFA-9312-FCA1E1A56484-a5.png']

| Filter applied | Take1 | Return count2 | 5M (seconds) | 10M (seconds) | 15M (seconds) | 20M (seconds) | 25M (seconds) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Products Grid Queries |  |  |  |  |  |  |  |
| Part number | 1000 | False | 0.076 | 0.079 | 0.063 | 0.087 | 0.052 |
| Family and Name | 1000 | False | 0.065 | 0.053 | 0.06 | 0.057 | 0.058 |
| Updated time | 1000 | False | 0.083 | 0.06 | 0.064 | 0.059 | 0.058 |
| Metadata | 1000 | False | 0.072 | 0.057 | 0.072 | 0.055 | 0.079 |
| No filter | 1000 | False | 0.071 | 0.052 | 0.058 | 0.059 | 0.056 |
| Results Grid Queries |  |  |  |  |  |  |  |
| Test program | 1000 | False | 0.133 | 0.082 | 0.085 | 0.091 | 0.097 |
| Part number | 1000 | False | 0.129 | 0.127 | 0.131 | 0.129 | 0.126 |
| Status | 1000 | False | 0.113 | 0.098 | 0.116 | 0.094 | 0.092 |
| Property | 1000 | False | 0.07 | 0.107 | 0.073 | 0.075 | 0.063 |
| Keyword | 1000 | False | 0.073 | 0.079 | 0.075 | 0.063 | 0.069 |
| Workspace | 1000 | False | 0.098 | 0.133 | 0.103 | 0.085 | 0.09 |
| Id | 1000 | False | 0.099 | 0.107 | 0.139 | 0.203 | 0.099 |
| No filter | 1000 | False | 0.131 | 0.137 | 0.107 | 0.126 | 0.144 |
| Count query | 0 | True | 0.075 | 0.070 | 0.071 | 0.057 | 0.056 |
| Steps Grid Queries |  |  |  |  |  |  |  |
| Step name | 1000 | True | 0.082 | 1.287 | 2.778 | 5.129 | 5.891 |
| Measurement Name | 1000 | True | 0.132 | 2.053 | 1.989 | 5.382 | 3.71 |
| Measurement name and Step name | 1000 | True | 0.142 | 1.277 | 3.927 | 4.681 | 7.07 |
| Applying projections | 1000 | True | 0.08 | 0.119 | 0.079 | 0.092 | 0.082 |
| Step id | 1000 | True | 0.08 | 0.092 | 0.093 | 0.09 | 0.108 |
| Data Spaces Queries |  |  |  |  |  |  |  |
| Part number | 1000 or 10000 | False | 1.039 | 1.038 | 1.01 | 1.084 | 1.132 |
| Product name | 10000 | False | 1.452 | 1.422 | 1.403 | 1.472 | 1.816 |
| Part number and Test program | 10000 | False | 1.465 | 1.478 | 1.48 | 1.528 | 1.44 |
| Product name and Result status | 10000 | False | 1.566 | 1.474 | 1.437 | 1.503 | 1.488 |
| Part number and Result metadata | 1000 | False | 0.623 | 0.606 | 1.074 | 1.609 | 0.343 |
| Part number and Step status | 10000 | False | 1.503 | 1.442 | 1.498 | 1.527 | 1.9 |
| Part number, Test program, and Step name | 1000 or 10000 | False | 1.412 | 9.546 | 2.031 | 3.761 | 5.345 |
| Part number and Paths | 1000 | False | 0.245 | 0.344 | 0.569 | 0.336 | 0.467 |
| Input conditions | 1000 | False | 0.241 | 0.226 | 0.234 | 0.232 | 0.223 |
| Part number (Path API) | 1000 | False | 0.235 | 0.422 | 0.482 | 0.748 | 0.431 |
| Part number and Program name (Path API) | 1000 | False | 0.099 | 0.227 | 0.167 | 0.145 | 0.217 |
| Input condition value - equals | 1000 | False | 14.024 | Timed out | Timed out | Timed out | Timed out |
| Program name - Contains | 10000 | False | 2.498 | Timed out | Timed out | Timed out | Timed out |
| Result metadata - Contains | 1000 | False | 1.575 | Timed out | Timed out | Timed out | Timed out |
| 1Represents the take parameter in the query request body, which limits the number of records fetched. 2Represents the returnCount parameter in the query request body, which fetches the total count of records matching the applied filter if true. Note 5.7% of Data Spaces queries with filters like Program name contains and Result metadata returned 503 errors. These errors indicate the resource limitations for Test Monitor service. |  |  |  |  |  |  |  |

[IMAGE alt='Histogram of Data Spaces query elapsed time, showing most queries under 5 seconds and a spike near 30 seconds.' src='GUID-DAF199EE-E595-4711-8AD8-E2C1E8B39966-a5.png']

Parent topic:

Service Performance Specifications

Related tasks:

- Publishing Test Results with the Test Monitor API
- Monitoring Tests

Related information:

- SystemLink API Reference
- Dynamic Linq Query Language

<!--NI_TOPIC bundle=systemlink-enterprise path=test-monitoring-http-api.html language=enus -->
## TOPIC 00107: Publishing Test Results with the Test Monitor API

- bundle_id: `systemlink-enterprise`
- source_path: `test-monitoring-http-api.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/test-monitoring-http-api.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Publish test results, log parametric data, and attach additional files to results using the SystemLink Test Monitor API. The Test Monitor Service has an HTTP API. The Test Monitor Service also has useful wrappers available in G, C#, and Python. If you use TestStand, integrate Test Monitor with TestS

### Publishing Test Results with the Test
 Monitor API

Publish test results, log parametric data, and attach additional files to results
 using the SystemLink Test Monitor API.

The Test Monitor Service has an HTTP API. The Test Monitor Service also has useful wrappers
 available in G, C#, and Python.

If you use TestStand, integrate Test Monitor with TestStand instead of using the API.

1. In your programming environment, use the Test Monitor API to publish test results and
 associated steps to SystemLink.
2. In the SystemLink web application, click Product Insights. 
 Results from the test you created will instantly appear here and update in real
 time.
3. To upload an attachment to the test result, use the File Ingestion API or File Transfer
 API.
4. To download the report attachment in the SystemLink web application, complete
 the following steps.
  1. Navigate to Product Insights»Test Results.
  2. Double-click the test whose attachment you want to download.
  3. Expand Attachments to select the attachment and
 click Download.

Parent topic:

Monitoring Tests

Related tasks:

- Analyzing and Interacting with Test Results

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=tracking-the-location-of-assets-over-time.html language=enus -->
## TOPIC 00108: Tracking the Location of Assets over Time

- bundle_id: `systemlink-enterprise`
- source_path: `tracking-the-location-of-assets-over-time.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/tracking-the-location-of-assets-over-time.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Determine when, where, and how long an asset was connected to a system. You can also see how long the system was online. Navigate to Systems Management Assets . Select the asset you want to view location information for and click View. Click the Locations tab. The Locations tab shows a list of inter

### Tracking the Location of Assets over
 Time

Determine when, where, and how long an asset was connected to a system. You can also see
 how long the system was online.

1. Navigate to Systems Management»Assets.
2. Select the asset you want to view location information for and click
 View.
3. Click the Locations tab. 
 The Locations tab shows a list of intervals when the
 asset was connected to a system over the past 3 months. An interval ends when
 one of the following occurs:The system disconnects.
 The asset is physically moved.
4. Click [IMAGE alt='Filter icon for refining search results.' src='GUID-731A5124-8F1A-4C37-AB46-A92BD043BE9B-a5.png'] to filter assets by a given timestamp or
 location.

Parent topic:

Managing Your Assets

<!--NI_TOPIC bundle=systemlink-enterprise path=transferring-data-using-tags.html language=enus -->
## TOPIC 00109: Transferring Data Using Tags

- bundle_id: `systemlink-enterprise`
- source_path: `transferring-data-using-tags.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/transferring-data-using-tags.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use tags to send and receive data from one system to other systems. What to Use You can find the SystemLink Tag and Configuration APIs on the Data Communication palette in LabVIEW, LabVIEW NXG Web Module, and G Web Development Software. This example uses G Web Development Software Tag and Configurat

### Transferring Data Using Tags

Use tags to send and receive data from one system to other systems.

#### What to Use

Note

#### What to Do

1. Create the following diagram in a VI to read
 tag data. Customize the gray sections for your unique programming goals. 1
 Open Configuration
 initiates a connection with SystemLink.
 2
 Open Tag opens a
 reference to a tag on the server defined by the
 configuration. Note Use
 Query Tags instead of
 Open Tag if you do not know the
 data type of the tag.If the reference does
 not exist on the server, Open Tag
 will create one. Open Tag will return
 an error if a tag with the same path but of a different
 data type already exists.Use a For
 Loop to open a tag for each element in an
 array of tag names. In this example, the VI opens an
 array of station temperature tags.
 3
 Read Tag checks the
 current value of the tag. Follow an open/read/close model
 when using this VI. Note Use
 Multi Read instead of
 Read Tag if you need to read
 multiple tag values as a part of a single operation.Use a While Loop to
 continue reading tags until a condition is met. In this
 example, Read Tag returns tag values unless the
 Boolean constant changes to True.
 4
 Close Tag closes a tag
 reference. Use a For Loop to close
 tags from an array of tag names, or call Open
 Tag (Multiple) instead.
 5
 Close Configuration
 invalidates any open reference to created objects and closes
 connections associated with the configuration.
2. Create the following diagram in a VI to write a
 tag value. Customize the gray sections for your unique programming goals. 1
 Open Configuration
 initiates a connection with SystemLink.
 2
 Open Tag opens a
 reference to a tag on the server defined by the
 configuration. Note Use
 Query Tags instead of
 Open Tag if you do not know the
 data type of the tag.If the reference does
 not exist on the server, Open Tag
 will create one. Open Tag will return
 an error if a tag with the same path but of a different
 data type already exists.Use a For
 Loop to open a tag for each element in an
 array of tag names. In this example, Open
 Tag opens an array of station temperature
 tags.
 3
 Write Tag writes a
 value to a tag. Follow an open/write/close model when using
 this VI. Note Use
 Multi Write instead of
 Write Tag if you need to write
 multiple tag values as a part of a single operation.If you want the server to manage the time
 stamp of when the tag was written, leave the time stamp
 cluster unwired.Use a While
 Loop to continue reading tags until a
 condition is met. In this example, Write
 Tag writes tags until you click the stop
 button on the panel.Use a For
 Loop to write a tag for each element in an
 array of tag names.
 4
 Close Tag closes a tag
 reference. Use a For Loop to close
 tags from an array of tag names, or call Open
 Tag (Multiple) instead.
 5
 Close Configuration
 invalidates any open reference to created objects and closes
 connections associated with the configuration.

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

<!--NI_TOPIC bundle=systemlink-enterprise path=transferring-files-from-disk-to-systemlink.html language=enus -->
## TOPIC 00110: Transferring Files from Disk to SystemLink Enterprise

- bundle_id: `systemlink-enterprise`
- source_path: `transferring-files-from-disk-to-systemlink.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/transferring-files-from-disk-to-systemlink.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Send files stored on disk from a client to SystemLink Enterprise to save, process, or enable access for others. What to Use You can find the SystemLink File Transfer and Configuration APIs on the Data Communication palette in LabVIEW 2016 or later. What to Do On the client, create the following diag

### Transferring Files from Disk to SystemLink Enterprise

Send files stored on disk from a client to SystemLink Enterprise to
 save, process, or enable access for others.

#### What to Use

You can find the SystemLink File Transfer and Configuration APIs on the Data
 Communication palette in LabVIEW 2016 or later.

#### What to Do

On the client, create the following diagram in a VI to send files from disk to SystemLink.

Customize the highlighted sections for your unique programming goals.

[IMAGE alt='LabVIEW diagram sending a file to SystemLink using Open Configuration HTTP Selector and Send HTTP.' src='GUID-3BDD600B-2BF6-4974-97C1-2C7D50811B01-a5.png']

1. Open Configuration initiates a connection to the File Ingestion
 Service.
2. Send uses the path you specify to do the following. The File Ingestion Service creates the file in SystemLink Enterprise and writes the packets to the file.
  1. Locate the local file you want to upload.
  2. Read and transmit the data of the file in packets to the File Ingestion
 Service.

#### Troubleshooting

| Scenario | Strategy |
| --- | --- |
| Your client disconnects during a file transfer. | Complete the following steps. Abort the file transfer. Wait for SystemLink Enterprise to automatically delete the partial file transfer. After SystemLink deletes the partial file transfer, initiate a new file transfer. Note If a partial file transfer does not progress within an hour, SystemLink automatically treats it as an abandoned transfer and deletes it. |
| Your file transfer times out because your file is large or from memory. | Use Send Packet to do the following: Send different packet sizes during the file transfer. Manage when to transfer a packet. |
| No data is available to send within the one-hour timeout period for file transfers. | Use Send Packet to send a zero-byte packet to keep the file transfer active. |

#### Examples

- Sync File IO

Parent topic:

Connecting to Clients

Related tasks:

- Transferring Files from Memory to SystemLink

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=transferring-files-from-memory-to-systemlink.html language=enus -->
## TOPIC 00111: Transferring Files from Memory to SystemLink

- bundle_id: `systemlink-enterprise`
- source_path: `transferring-files-from-memory-to-systemlink.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/transferring-files-from-memory-to-systemlink.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Send files stored in memory from a client to SystemLink to save, process, or enable access for others. What to Use You can find the SystemLink File Transfer and Configuration APIs on the Data Communication palette in LabVIEW 2016 or later. What to Do On the client, create the following diagram in a

### Transferring Files from Memory to
 SystemLink

Send files stored in memory from a client to SystemLink to save, process, or enable
 access for others.

#### What to Use

You can find the SystemLink File Transfer and Configuration APIs on the Data
 Communication palette in LabVIEW 2016 or later.

#### What to Do

On the client, create the following diagram in a VI to send files from memory to
 SystemLink.

Customize the highlighted sections for your unique programming goals.

[IMAGE alt='LabVIEW diagram sending in-memory file data and properties to SystemLink using HTTP VIs.' src='GUID-C3ABE401-3919-46DF-ACF4-48CFB71BA6B3-a5.png']

1. Open Configuration initiates a connection to the File Service.
2. Send uses the file name and data buffer to transmit the data to the
 File Service. The File Service creates a file with the file name and data buffer
 contents in SystemLink.

#### Troubleshooting

- If your client disconnects during a file transfer, complete the following steps. Note If a partial file transfer does
 not progress within an hour, SystemLink automatically treats it as an abandoned transfer
 and deletes it.
  1. Abort the file transfer.
  2. Wait for SystemLink to automatically delete the partial file transfer.
  3. After SystemLink deletes the partial file transfer, initiate a new file transfer.

#### Examples

- Sync File IO

Parent topic:

Connecting to Clients

Related information:

- SystemLink API Reference

<!--NI_TOPIC bundle=systemlink-enterprise path=uploading-custom-files.html language=enus -->
## TOPIC 00112: Uploading Custom Files to Test Monitor

- bundle_id: `systemlink-enterprise`
- source_path: `uploading-custom-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/uploading-custom-files.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload any type of file to a test result to maintain data traceability. Integrating Test Monitor with TestStand allows you to see test metadata in the SystemLink web application. To capture the tests you run in TestStand, you can configure the following products to upload files to Test Monitor. Test

### Uploading Custom Files to Test Monitor

Upload any type of file to a test result to maintain data traceability.

- TestStand 2014 or later
- LabVIEW 2015 or later

Use one of the following methods to upload a custom file or group of files.

- [Uploading Custom Files with a VI](uploading-files-with-a-vi.html) Upload one or more files using TestStand and LabVIEW 2015 or later.
- [Uploading Files with a TestStand Step](uploading-files-with-teststand.html) Upload custom files to Test Monitor from using only TestStand.

Parent topic:

Monitoring Tests

Related tasks:

- Uploading Files with a TestStand Step
- Uploading Custom Files with a VI

<!--NI_TOPIC bundle=systemlink-enterprise path=uploading-files-with-a-vi.html language=enus -->
## TOPIC 00113: Uploading Custom Files with a VI

- bundle_id: `systemlink-enterprise`
- source_path: `uploading-files-with-a-vi.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/uploading-files-with-a-vi.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload one or more files using TestStand and LabVIEW 2015 or later. On the diagram in LabVIEW, use Send File to specify one or more files to upload to SystemLink. Create one output for each file ID you want to return. To upload many files, create an array output for the file IDs you want to return.

### Uploading Custom Files with a VI

Upload one or more files using TestStand and LabVIEW 2015 or later.

1. On the diagram in LabVIEW, use Send File to specify one or more
 files to upload to SystemLink.
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
5. Attach the files to a test result.
  1. Click the test step that uploaded the file.
  2. Under Properties, click Additional
 Results.
  3. Click + to create a custom result.
  4. Under Name, type
 "NI.SYSTEMLINK.TESTMONITORFILE" including quotes. 
 Use this name for all additional results you add.
  5. Under Value to Log, specify the local variable you created.

Test Monitor automatically attaches the file you specified to the current test result.

Parent topic:

Uploading Custom Files to Test Monitor

<!--NI_TOPIC bundle=systemlink-enterprise path=uploading-files-with-teststand.html language=enus -->
## TOPIC 00114: Uploading Files with a TestStand Step

- bundle_id: `systemlink-enterprise`
- source_path: `uploading-files-with-teststand.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/uploading-files-with-teststand.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Upload custom files to Test Monitor from using only TestStand. Create a step to upload the file or group of files. Right-click in the Steps pane of your sequence file. Click Insert StepSystemLinkUpload File. Specify a file path or ID for one or more files to upload. Store the file IDs using local va

### Uploading Files with a TestStand Step

Upload custom files to Test Monitor from using only TestStand.

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

When you run your test, TestStand uploads
 the file to the default workspace. TestStand then attaches the file to the test
 result.

Parent topic:

Uploading Custom Files to Test Monitor

<!--NI_TOPIC bundle=systemlink-enterprise path=user-manual-welcome.html language=enus -->
## TOPIC 00115: SystemLink Enterprise User Manual

- bundle_id: `systemlink-enterprise`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/user-manual-welcome.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SystemLink Enterprise User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### SystemLink Enterprise
 User Manual

The SystemLink Enterprise User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Release Notes
- Installation Guide on GitHub
- YouTube Channel
- SystemLink Enterprise IT Administrators Manual

<!--NI_TOPIC bundle=systemlink-enterprise path=using-data-tables-as-dashboard-variables.html language=enus -->
## TOPIC 00116: Using Data Tables as Dashboard Variables

- bundle_id: `systemlink-enterprise`
- source_path: `using-data-tables-as-dashboard-variables.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/using-data-tables-as-dashboard-variables.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create variables that use data tables to dynamically view dashboard data. In SystemLink Enterprise, navigate to Overview Dashboards . Click Apps icon and select the dashboard that contains the variable you want to edit. Click Dashboard settings. In the Variables tab, click New variable and enter a v

### Using Data Tables as Dashboard
 Variables

Create variables that use data tables to dynamically view dashboard data.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Click [IMAGE alt='Apps icon' src='GUID-69B726A6-D4C1-451C-882A-5ED0B10972FD-a5.png'] and select the dashboard that contains the variable you want to
 edit.
3. Click Dashboard settings.
4. In the Variables tab, click New
 variable and enter a variable name.
5. Expand the Type drop-down and select
 Query.
6. In the Query options section, update the relevant
 properties.
  1. Set the Data Source as SystemLink
 Data Frames.
  2. Select a Query Type. 
 Query Type
 DescriptionList data tables
 Returns a list of data table names that match the
 filters.
 List data table columns
 Returns a list of columns from each data table
 that match the filters.
  3. Add filters to the following sections to filter the data to a specific
 data table. 
 Query by result properties
 Query by data table properties
 Query by column properties
7. Click Apply.
8. Return to the dashboard. 
 You can now reference the variable in panels that use the SystemLink
 Data Frames Data source by typing $ followed by the
 variable name.

Parent topic:

Analyzing and Interacting with Test Results

Related information:

- Grafana Add and Manage Variables

<!--NI_TOPIC bundle=systemlink-enterprise path=using-notebook-outputs-as-dashboard-variables.html language=enus -->
## TOPIC 00117: Using Notebook Outputs as Dashboard Variables

- bundle_id: `systemlink-enterprise`
- source_path: `using-notebook-outputs-as-dashboard-variables.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/using-notebook-outputs-as-dashboard-variables.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create variables that use notebook outputs to dynamically view dashboard data. In SystemLink Enterprise, navigate to Overview Dashboards . Click Apps icon and select the dashboard you want to edit variable for. Click Dashboard settings and open the Variables tab. Click Add variable and give your var

### Using Notebook Outputs as Dashboard
 Variables

Create variables that use notebook outputs to dynamically view dashboard
 data.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Click [IMAGE alt='Apps icon' src='GUID-69B726A6-D4C1-451C-882A-5ED0B10972FD-a5.png'] and select the dashboard you want to edit variable for.
3. Click Dashboard settings and open the
 Variables tab.
4. Click Add variable and give your variable a name.
5. Expand the Type drop-down and select
 Query.
6. Expand the Data source drop-down and select
 SystemLink Notebooks.
7. Expand the Notebooks drop-down and select the notebook you want
 to use.
8. Click Update.

Parent topic:

Visualizing Notebook Data on a Dashboard

Related tasks:

- Viewing Out of the Box (OOTB) Dashboards in SystemLink Enterprise

<!--NI_TOPIC bundle=systemlink-enterprise path=viewing-hardware-calibration-data.html language=enus -->
## TOPIC 00118: Viewing Hardware Calibration Data

- bundle_id: `systemlink-enterprise`
- source_path: `viewing-hardware-calibration-data.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/viewing-hardware-calibration-data.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: View hardware calibration data to make maintenance decisions about your assets. Navigate to Systems Management Assets . Click Filter icon. . Refer to the following table to find the query that best suits your use case. Use Case Property Operator Value View assets that are currently out of calibratio

### Viewing Hardware Calibration Data

View hardware calibration data to make maintenance decisions about your
 assets.

1. Navigate to Systems Management»Assets.
2. Click [IMAGE alt='Filter icon.' src='GUID-731A5124-8F1A-4C37-AB46-A92BD043BE9B-a5.png'].
3. Refer to the following table to find the query that best suits your use case. 
 Use Case
 Property
 Operator
 ValueView assets that are currently out of calibration
 Calibration due date
 is before
 The current dateNote This
 value is automatically populated. Configure the resulting table to show the
 Calibration due date column to see the expected
 calibration date for each asset.
 View assets that are due for calibration next monthNote Specify both queries with an
 AND
 Calibration due date
 is on or after
 The first day of the next month formatted
 DD-Month-YYYY.
 Calibration due date
 is on or before
 The last day of the next month formatted
 DD-Month-YYYY.
 View assets that have not run self-calibration in the past week
 Last self calibration date
 is before
 The date one week ago formatted
 DD-Month-YYYY.

Parent topic:

Managing Your Assets

<!--NI_TOPIC bundle=systemlink-enterprise path=viewing-out-of-the-box-dashboards.html language=enus -->
## TOPIC 00119: Viewing Out of the Box (OOTB) Dashboards in SystemLink Enterprise

- bundle_id: `systemlink-enterprise`
- source_path: `viewing-out-of-the-box-dashboards.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/viewing-out-of-the-box-dashboards.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: SystemLink Enterprise provides preconfigured dashboards for easy access to common information such as asset calibration, lab overview, and product test summary. In SystemLink Enterprise, navigate to Overview Dashboards . Open the Default Dashboards folder. To view a dashboard, click on a dashboard.

### Viewing Out of the Box (OOTB) Dashboards in
 SystemLink Enterprise

SystemLink Enterprise provides preconfigured dashboards for easy access
 to common information such as asset calibration, lab overview, and product test
 summary.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Open the Default Dashboards folder.
3. To view a dashboard, click on a dashboard.

Note

Grafana Dashboards

Grafana Variables

Note

Using Notebook
 Outputs as Dashboard Variables

Parent topic:

Monitoring Tests

Related tasks:

- Using Notebook Outputs as Dashboard Variables
- Using the Alarms Overview Dashboard
- Using the System Health Dashboard

Related information:

- Grafana Dashboards
- Grafana Variables

<!--NI_TOPIC bundle=systemlink-enterprise path=viewing-scheduled-test-plans.html language=enus -->
## TOPIC 00120: Viewing Scheduled Work Items

- bundle_id: `systemlink-enterprise`
- source_path: `viewing-scheduled-test-plans.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/viewing-scheduled-test-plans.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Schedule view to review all work items scheduled for a system. To view scheduled work items, complete the following steps that align with your goal. Goal Steps View work items scheduled for all systems Navigate to Operations Schedule . View work items scheduled for a specific system Navigate

### Viewing Scheduled Work Items

Use the Schedule view to review all work items scheduled for a
 system.

1. To view scheduled work items, complete the following steps that align with your
 goal. 
 GoalStepsView work items scheduled for all systems
 Navigate to Operations»Schedule.View work items scheduled for a specific system
 Navigate to Systems Management»Systems.
 Click a system to view the associated work item schedules.
 Click the Schedule tab. 
 SystemLink loads the calendar for the current month.
2. To change the calendar view, complete the steps that align with your
 goal. 
 OptionDescriptionView a different month
 Click Next month
 [IMAGE alt='Next month arrow icon.' src='GUID-3BA432AC-37C1-4FD4-A278-5D298811AC74-a5.png'] or Previous month
 [IMAGE alt='Previous month arrow icon.' src='GUID-F73317A9-1472-4D83-B8AD-AB9D67116AD6-a5.png']Switch between different calendar views
 Click the Select the calendar view drop-down
 menu and choose from the following options: Day
 Week
 Month
 YearNavigate to a specific date
 Click the calendar drop-down menu and select the dateNavigate to the current date
 Click Today
3. To view additional details for a scheduled work item, click the work item in
 the calendar.
4. To re-schedule a work item, drag and drop the work item to a different
 time. 
 Note You can also drag and drop the work item to a
 different system.
5. To refresh the view of a work item, click Refresh
 ([IMAGE alt='Refresh icon (circular arrow).' src='GUID-B86831AB-03F4-47F9-8BC4-B0863A0D3C5E-a5.png']).
6. To filter your schedule view, click Configure query
 ([IMAGE alt='Configure query icon (funnel).' src='GUID-EB0685D0-E223-4671-A11C-EF215D6A11F5-a5.png']) and define a query.
7. To save a custom view, click the view selector drop-down menu ([IMAGE alt='View selector drop-down menu showing Default.' src='GUID-F0FC3C4C-BF2F-4728-94AE-FE77CB7C41F2-a5.png']) and select Create view. You can use custom
 views to switch between different calendar views with different query filters.
 You can also reuse and share these views.
8. To highlight work items on the schedule page, configure the URL in the output
 of the auto scheduling notebook. The URL must include
 work-items query parameters with IDs for the work
 item.
9. To view conflicting work item schedules, click Settings
 ([IMAGE alt='Settings gear icon.' src='GUID-7F29A48D-030C-4383-B9DC-CE32E9DD7EA6-a5.png']) and enable Show conflicting work items.

SystemLink Enterprise

Parent topic:

Managing Work Orders and Work Items

Related information:

- SystemLink Examples on GitHub

<!--NI_TOPIC bundle=systemlink-enterprise path=viewing-spec-details-for-product.html language=enus -->
## TOPIC 00121: Viewing Product Specifications

- bundle_id: `systemlink-enterprise`
- source_path: `viewing-spec-details-for-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/viewing-spec-details-for-product.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: View the specifications associated with a product and the detailed information within a specification document. Before you begin, add specifications for your product. Navigate to Product Insights Products . Select the product specification you want to view. Click the Specs tab. SystemLink lists all

### Viewing Product Specifications

View the specifications associated with a product and the detailed information within a
 specification document.

Before you begin, add specifications
 for your product.

1. Navigate to Product Insights»Products.
2. Select the product specification you want to view.
3. Click the Specs tab. 
 SystemLink lists all the specifications for the product.
4. To limit the list of specifications you see, complete the
 following steps.
  1. Click Filter
 [IMAGE alt='Filter icon (funnel)' src='GUID-731A5124-8F1A-4C37-AB46-A92BD043BE9B-a5.png'].
  2. Define the query you want to use to filter items in your grid.
5. Click the Spec ID for the specification you want to
 view. 
 SystemLink opens the specification details window.
6. View the following parameters in the top pane. 
 Name (Symbol)
 Spec ID
 Updated at
 Updated by
 Category
 Type
 Spec limits
 Block
 Create at
 Created by
 ID
 Version
 Workspace
7. Configure the pane to display the keywords and custom
 properties of the specification.
8. In the Details page, use the following tabs to view
 specification information: 
 Tab
 DescriptionAttributes
 View the keywords and custom properties.
 Conditions
 View and manage specification conditions.

Products

Parent topic:

Specification Compliance

Related tasks:

- Creating and Editing Product Specifications through SystemLink
- Deleting Specifications
- Creating, Viewing, and Managing Specification Conditions
- Filtering Grids

Related information:

- Enabling the Specification Compliance Module

<!--NI_TOPIC bundle=systemlink-enterprise path=viewing-test-steps-by-result.html language=enus -->
## TOPIC 00122: Viewing Test Steps by Result

- bundle_id: `systemlink-enterprise`
- source_path: `viewing-test-steps-by-result.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/viewing-test-steps-by-result.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Analyze information about the results associated with your tests to determine the quality metrics of the devices under test (DUT). Navigate to Product Insights Test Results . Click the result you want to analyze. On the Steps tab, expand a step to see the following details. Step children, hierarchy,

### Viewing Test Steps by Result

Analyze information about the results associated with your tests to determine the quality
 metrics of the devices under test (DUT).

1. Navigate to Product Insights»Test Results.
2. Click the result you want to analyze.
3. On the Steps tab, expand a step to see the following
 details. 
 Step children, hierarchy, name, status, and time elapsed.
 Measurement name, value, unit, low limit, and high limit if
 available.
4. Click [IMAGE alt='Filter icon.' src='GUID-731A5124-8F1A-4C37-AB46-A92BD043BE9B-a5.png'] to filter steps by the step or measurement name. 
 Note You can save a custom view
 of the Steps grid. You can reuse custom
 Steps grid views for results with the same test
 program under a product.
5. Click a step to open the Step Details slide-out. You can
 view step measurements, inputs, outputs, and properties in the
 Info tab. You can view the raw JSON string in the
 Data tab.
6. Click Close.
7. To visualize the parametric data of a step, click [IMAGE alt='More options icon' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png'] next to the step name and select Visualize
 Steps.
8. Click Add X-Axis and select
 Index. 
 This will trend the parametric data with the part number, test program,
 step path, and input conditions filters of the selected step.
9. To visualize a measurement filtered by one of the following: 
 Part number
 Test program
 Step path
 Input conditions filter
  1. Click [IMAGE alt='More options icon' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png'] next to the measurement name.
  2. select Visualize measurement.
10. To visualize a measurement filtered by part number and test program across all
 steps, complete the following steps.
  1. Click [IMAGE alt='More options icon' src='GUID-F497298E-7DB8-41EA-80BF-A05E39E2D1C1-a5.png'] next to the measurement name.
  2. select Visualize measurement for all
 steps.

Parent topic:

Analyzing and Interacting with Test Results

Related tasks:

- Creating a Product
- Connecting SystemLink with TestStand
- Publishing Test Results with the Test Monitor API
- Viewing Test Results by Product
- Filtering Grids

Related information:

- ETL Example
- Steps

<!--NI_TOPIC bundle=systemlink-enterprise path=visualizing-data-tables-in-a-dashboard.html language=enus -->
## TOPIC 00123: Visualizing Data Tables in a Dashboard

- bundle_id: `systemlink-enterprise`
- source_path: `visualizing-data-tables-in-a-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/visualizing-data-tables-in-a-dashboard.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Select data tables associated with a test result to visualize in a dashboard. In SystemLink Enterprise, select Product Insights Test Results . Click the test result you want to visualize. Under Data tables, select the data tables you want to see in a graph and click Visualize Dashboard . Navigate to

### Visualizing Data Tables in a Dashboard

Select data tables associated with a test result to visualize in a dashboard.

1. In SystemLink Enterprise, select Product Insights»Test Results.
2. Click the test result you want to visualize.
3. Under Data tables, select the data tables you want to see
 in a graph and click Visualize»Dashboard.
4. Navigate to the Query tab of the dashboard, set the
 Data source to SystemLink Data
 Frames.
5. Set the Query Type to Data. 
 Note For more information on the Data Frames data
 source configuration, refer to *Adding the Data Frames Data Source to a
 Dashboard*.
6. In the Columns drop-down, select the columns you want to
 visualize. 
 Note You can select up to 20 columns.
7. Optional: 
 In the Decimation Settings section, specify the column for
 using as the x-axis when decimating the data in X-column field. 
 Note The default value of the X-Column field is the
 index column of the data table.
8. Configure the time range option and click Run
 query. 
 If your data has time stamps, a time series graph appears along with a
 table.
9. Optional: 
 Copy the page URL to share your query.
10. Click Add to dashboard to create a new dashboard with
 this visualization or to add the visualization to an existing dashboard.

Parent topic:

Analyzing and Interacting with Test Results

Related concepts:

- Normalizing Data for Efficient Storage and Access
- Improving Data Table Metadata Query Performance

Related tasks:

- Using the Data Frames Data Source in a Dashboard
- Using Data Tables as Dashboard Variables

Related information:

- Grafana Explore

<!--NI_TOPIC bundle=systemlink-enterprise path=visualizing-data-tables-in-a-data-space.html language=enus -->
## TOPIC 00124: Visualizing Data Tables in a Data Space

- bundle_id: `systemlink-enterprise`
- source_path: `visualizing-data-tables-in-a-data-space.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/visualizing-data-tables-in-a-data-space.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Derive insights about data from data tables by visualizing the data in different types of plots. Complete the following steps based on your goal. Select data tables to visualize in a data space Navigate to Product Insights Data Tables . Select the data tables you want to visualize. Click Visualize D

### Visualizing Data Tables in a Data
 Space

Derive insights about data from data tables by visualizing the data in different types of
 plots.

1. Complete the following steps based on your goal. 
 OptionDescriptionSelect data tables to visualize in a data space
 Navigate to Product Insights»Data Tables.
 Select the data tables you want to visualize.
 Click Visualize»Data space.Select data tables associated with a test result to visualize in a
 data space
 Navigate to Product Insights»Test Results.
 Click the test result you want to visualize.
 Under Data tables, select the data tables
 you want to graph.
 Click Visualize»Data space.Create data space to query data tables
 Navigate to Product Insights»Data Spaces.
 Click Create data space.
 Under Data source, select Data
 tables.
 Specify the tables and rows you want to get data for. You must
 specify at least one table-level filter.
 Click Run query .
2. On the Data tab, select the type of plot you want to
 create. 
 
 Note You can configure additional settings on the Settings
 tab. The settings change based on the plot type you choose.
  - Scatter
  - Line
3. Click Add X-Axis.
4. Specify up to one column per table to use as the x-axis and click
 OK.
5. Click Add Y-Axis.
6. Specify one or more columns to plot on the y-axis and click
 OK. 
 SystemLink Enterprise plots the data from the axes you
 selected. You can also view the data as a table on the
 Table tab.
7. Optional: 
 To lower the sampling rate of the data on the plot, complete the following
 steps. 
 
 
 To learn about the different decimation modes, refer to *Normalize Data
 for Efficient Storage and Access*.
  1. Enable Decimate data.
  2. Select the mode from the following options.
  - Lossy
  - Max/Min
  - Entry/Exit
8. Optional: 
 To align the starting point of all traces to zero, enable Align
 x-axis to zero from the Settings tab.
9. Click Save
 [IMAGE alt='Save button.' src='GUID-54AAC5CA-0EF8-41F8-AFFE-4E684F12AC94-a5.png'].
10. Specify a name, assign a workspace, and click
 Save. 
 SystemLink adds this data space to Product Insights»Data Spaces.
11. Optional: 
 To share your data space, copy the page URL.

You can create marginal plots from your scatter plots and
 line plots.

Parent topic:

Interacting with Data in a Data Space

Related concepts:

- Normalizing Data for Efficient Storage and Access
- Improving Data Table Metadata Query Performance

Related tasks:

- Using the Data Frames Data Source in a Dashboard
- Creating Marginal Plots
- Visualizing Data Tables in a Dashboard

<!--NI_TOPIC bundle=systemlink-enterprise path=visualizing-metadata-of-your-test-results.html language=enus -->
## TOPIC 00125: Visualizing Your Test Result Metadata

- bundle_id: `systemlink-enterprise`
- source_path: `visualizing-metadata-of-your-test-results.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/visualizing-metadata-of-your-test-results.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: View and modify the metadata, such as keywords or properties, associated with your test results so you can interact with data more efficiently. Configure the Test Results Details in the SystemLink web application to display information important to you about your test data. Navigate to Product Insig

### Visualizing Your Test Result Metadata

View and modify the metadata, such as keywords or properties, associated with your test
 results so you can interact with data more efficiently.

Test Results
 Details

1. Navigate to Product Insights»Test Results.
2. To open a detailed view, select a test result and click
 View.
3. Click Edit result
 [IMAGE alt='Edit icon' src='GUID-0835BF4B-9CBF-4DFB-A552-85C222FB9A9C-a5.png'] and use the slide-out to add, remove, or edit custom properties. 
 Note You can use absolute or relative
 hyperlinks as the value of a custom property using the following syntax similar to
 Markdown: `[link
 text](URL)`. SystemLink does not support
 Markdown syntax for custom tooltips. Absolute links must start with
 https:// or http://. Relative links must
 start with a forward slash.
4. Click Save.
5. Click [IMAGE alt='Close icon' src='GUID-982E63A6-40E8-4B78-B9FE-A397CE3B6974-a5.png'].
6. Use the Configure result display slide-out to configure how you
 want to display properties in the detailed view. 
 Drag a property to a new position.
 Add or remove a property.
7. Click OK.

Parent topic:

Analyzing and Interacting with Test Results

<!--NI_TOPIC bundle=systemlink-enterprise path=visualizing-notebook-data-on-dashboard.html language=enus -->
## TOPIC 00126: Visualizing Notebook Data on a Dashboard

- bundle_id: `systemlink-enterprise`
- source_path: `visualizing-notebook-data-on-dashboard.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/visualizing-notebook-data-on-dashboard.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a dashboard to visualize data from Jupyter notebooks. In SystemLink Enterprise, navigate to Overview Dashboards . Click Apps icon + New dashboard . Click Add a new panel. In the Query tab, expand the Data source drop-down and select SystemLink Notebooks. Expand the Notebooks drop-down and sel

### Visualizing Notebook Data on a
 Dashboard

Create a dashboard to visualize data from Jupyter notebooks.

1. In SystemLink Enterprise, navigate to Overview»Dashboards.
2. Click [IMAGE alt='Apps icon' src='GUID-69B726A6-D4C1-451C-882A-5ED0B10972FD-a5.png']»+ New dashboard.
3. Click Add a new panel.
4. In the Query tab, expand the Data source
 drop-down and select SystemLink Notebooks.
5. Expand the Notebooks drop-down and select the notebook you want
 to use.
6. Click Save.

Parent topic:

Analyzing and Interacting with Test Results

Related tasks:

- Using Notebook Outputs as Dashboard Variables
- Analyzing and Interacting with Test Results

Related information:

- Grafana Variables
- Grafana Dashboards

<!--NI_TOPIC bundle=systemlink-enterprise path=visualizing-test-results-by-product.html language=enus -->
## TOPIC 00127: Viewing Test Results by Product

- bundle_id: `systemlink-enterprise`
- source_path: `visualizing-test-results-by-product.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-enterprise/raw/resource/enus/visualizing-test-results-by-product.html
- document_id: `systemlink-enterprise`
- page_type: `leaf`
- content_type: `task`
- source_description: Analyze information about the product associated with your tests to determine the quality metrics of the devices under test (DUT). Navigate to Product Insights Products to view a list of product part numbers, names, families, and latest update times. Click on column headers to sort values in ascendi

### Viewing Test Results by Product

Analyze information about the product associated with your tests to determine the
 quality metrics of the devices under test (DUT).

1. Navigate to Product Insights»Products to view a list of product part numbers, names, families, and latest update
 times.
2. Click on column headers to sort values in ascending or descending
 order.
3. Select a product and click Edit to add, remove, or edit
 user-defined properties.
4. Double-click a product in the list to open a detailed view.
5. Click Results to review test results associated with a
 product.
6. To visualize the parametric data of test results in different charts, select the
 results and click Visualize.
7. Click Files to view files associated with a product, such as
 images of the DUT, schematics, instructions, and more.

Parent topic:

Analyzing and Interacting with Test Results

Related tasks:

- Visualizing Your Test Result Metadata
- Creating a Product
- Viewing Test Steps by Result
- Plotting Parametric Data in a Data Space
