# NI DOCUMENT BUNDLE: labview-report-generation-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-report-generation-toolkit start=1 end=13 -->
<!--NI_TOPIC bundle=labview-report-generation-toolkit path=common-graph-types-for-reports.html language=enus -->
## TOPIC 00001: Common Graph Types for Reports

- bundle_id: `labview-report-generation-toolkit`
- source_path: `common-graph-types-for-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/common-graph-types-for-reports.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Word Graphs and Pictures VIs and Excel Graphs and Pictures VIs support all the graph types that Microsoft Office uses. The following table defines some of the most commonly used graph types. Refer to the specific version of Microsoft Word or Microsoft Excel that you are using for a complete list

### Common Graph Types for Reports

The Word Graphs and Pictures VIs and Excel Graphs and
 Pictures VIs support all the graph types that Microsoft Office
 uses.

The following table defines some of the most commonly used graph types. Refer to the
 specific version of Microsoft Word or Microsoft Excel that you are using for a
 complete list of available graph types.

| Graph Type | Description |
| --- | --- |
| XY or Scatter | Displays the relationship or degree of a relationship between the numbers in several graph data series or plots two groups of numbers as one series of XY coordinates. XY graphs show uneven intervals of data. Arrange data with x values in one row or column, followed by one or more corresponding y values in adjacent rows or columns. Note Only XY graphs have the ability to scale both the x- and y-axes. |
| Area | Displays the relative importance of values over a period of time. Although area graphs appear similar to line graphs, area graphs emphasize the amount of change or magnitude of values. |
| Line | Displays trends or changes in data over a period of time at even intervals. Although line graphs appear similar to area graphs, line graphs emphasize time flow and the rate of change. |
| Column | Displays variation over a period of time or illustrates comparisons between items. Stacked and 100-percent stacked column graphs show relationships to a whole. Although column graphs are similar to bar graphs, column graphs organize categories horizontally and values vertically. |
| Bar | Displays individual figures at a specific time or illustrates comparisons between items. Stacked and 100-percent stacked bar graphs show relationships to a whole. Although bar graphs are similar to column graphs, bar graphs organize categories vertically and values horizontally. This type of organization places more emphasis on comparisons and less emphasis on time. |
| Three-dimensional surface | Displays a view that resembles a sheet stretched over a three-dimensional column graph. You can use surface graphs to find the best combinations between two sets of data. Surface graphs can show relationships between large amounts of data that might otherwise be difficult to see. Colors or patterns indicate areas that have the same value. The colors do not mark the data series. The wire frame format displays the data in black and white. Contour graph formats provide a two-dimensional view of the data from above, similar to a two-dimensional topographic map. |
| Pie | Displays the relationship or proportions of the parts to the whole. You can use pie graphs to emphasize a significant element. Pie graphs always contain one data series. If you select more than one data series when you create a pie graph, only one data series displays. Use a doughnut graph, a variation of a pie graph, if you want to display more than one data series in a round graph format. |

Parent topic:

Graphs Available in Reports

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=creating-reports-from-templates.html language=enus -->
## TOPIC 00002: Create Reports from Templates

- bundle_id: `labview-report-generation-toolkit`
- source_path: `creating-reports-from-templates.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/creating-reports-from-templates.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the MS Office Report Express VI to create a report from a Microsoft Word or Microsoft Excel template. Word and Excel templates contain placeholders for data and components that are common to all reports. The MS Office Report Express VI inserts data into the placeholders so you can displa

### Create Reports from Templates

You can use the MS Office Report Express VI to create a report
 from a Microsoft Word or Microsoft Excel template. Word and Excel templates contain
 placeholders for data and components that are common to all reports. The MS
 Office Report Express VI inserts data into the placeholders so you can
 display, print, or save the resulting report. These templates are located in the
 labview\templates\Report directory.

Complete the following steps to create a report from a basic Word template using the MS
 Office Report Express VI:

1. Place the MS Office Report Express VI on the block
 diagram.
2. In the configuration dialog box that appears, select Basic Report
 for Word from the Template pull-down
 list. 
 Note Do not change the Report
 Generation Toolkit basic templates for Word and Excel. If you want to edit
 the basic templates, save them with different filenames and select
 Custom Report for Word or Custom
 Report for Excel in the configuration dialog box of the
 MS Office Report Express VI.
3. Click the Author_Name item in the Bookmarks
 in the Selected Template list. Each item in this list represents
 a placeholder in the template.
4. Select Fixed Value from the Value
 Source pull-down list.
5. In the Fixed Value text box that appears, enter your
 name.
6. Repeat steps 3 through 5 for the Company_Name and
 Report_Title_Main items in the Bookmarks
 in the Selected Template list.Enter My First
 Report for the Report_Title_Main
 item.
7. Click the Graph1_Data_Input item in the
 Bookmarks in the Selected Template list. Verify that
 the Value Source for this item is
 Input and that the Input Appearance in
 Report is Graph.
8. In the Report Destination pull-down list, select
 Open in Microsoft Office.
9. Click the OK button to close the configuration dialog
 box. 
 The Express VI icon on the block diagram displays inputs for all the
 bookmarks configured with a Value Source of
 Input.
10. Place the Simulate Signal Express VI on the block
 diagram.
11. Click the OK button in the configuration dialog box that
 appears.
12. Wire the Sine output of the Simulate Signal
 Express VI to the Graph1_Data_Input input
 of the MS Office Report Express VI.
13. Run the VI. 
 Notice that the generated report opens in Microsoft Word and contains the text
 you entered for each placeholder in the template as well as the sine wave you
 created with the Simulate Signal Express VI.

You can create custom report templates in Word and Excel to ensure a consistent appearance in
 multiple reports. Use templates to define page size, text formatting, and other
 aspects of report appearance. You also can specify placeholders for text, tables,
 graphs, and images. Both Word and Excel provide ways to insert placeholders into
 documents and worksheets. Use bookmarks in Word and named ranges in Excel to define
 placeholders.

Refer to the Microsoft Word Help or Microsoft Excel Help for more information about creating templates.

Parent topic:

Create Reports

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=creating-reports.html language=enus -->
## TOPIC 00003: Create Reports

- bundle_id: `labview-report-generation-toolkit`
- source_path: `creating-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/creating-reports.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Report Generation VIs to create reports from existing or custom templates, including Microsoft Word or Microsoft Excel reports, in LabVIEW. You can insert text, numbers, tables and pictures into reports.

### Create Reports

You can use the Report Generation VIs to create reports from existing
 or custom templates, including Microsoft Word or Microsoft Excel reports, in LabVIEW.
 You can insert text, numbers, tables and pictures into reports.

- [Select a Report Type](selecting-report-types.html)
- [Create Reports from Templates](creating-reports-from-templates.html)
- [Bookmarks and Named Ranges in Reports](using-bookmarks-and-named-ranges-in-reports.html)

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=formatting-graphs-in-reports.html language=enus -->
## TOPIC 00004: Graph Formatting in Reports

- bundle_id: `labview-report-generation-toolkit`
- source_path: `formatting-graphs-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/formatting-graphs-in-reports.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the LabVIEW Report Generation Toolkit for Microsoft Office, the Excel Graphs and Pictures VIs and the Word Graphs and Pictures VIs provide an interface for Microsoft Office's graphing capabilities.When you insert graphs into reports, you must send data to the graph as a 2D array of numbers. You c

### Graph Formatting in Reports

In the LabVIEW Report Generation Toolkit for Microsoft Office, the Excel Graphs
 and Pictures VIs and the Word Graphs and Pictures VIs
 provide an interface for Microsoft Office's graphing capabilities.

When you insert graphs into reports, you must send data to the graph as a 2D array of numbers.
 You can send row and column headers, or values and categories, as 1D arrays of strings.
 Graphs can hold up to 4,000 rows and 4,000 columns including row and column headers, and
 they can display up to 256 data series.

Graphs and images form a collection for each Microsoft Word document or Microsoft Excel
 worksheet. Each object in a collection has an index value based on the order of the
 objects in the document or worksheet. Index values begin at 0. The indexes for graphs
 and images are separate. For example, if an Excel report contains an image, a second
 image, and a graph, the index value for the graph is 0 because the graph is the first
 graph in the report.

Enter index values in the graph index or picture
 index inputs of the Graphs and Pictures VIs to
 specify which graph or image you want the VI to format. By default, Graphs and
 Pictures VIs apply to the last object in a collection of a document or
 worksheet. You can avoid confusion with collection index values by formatting graphs and
 images immediately after you insert them into a report.

The Graphs and Pictures VIs support all graph types that Microsoft Office
 uses. If you want to format a graph in a way that the Graphs and
 Pictures VIs do not support, insert the graph in a Word or Excel template,
 format the graph, and use the Word Update Graph VI or the
 Excel Update Graph VI to fill the graph with data.

Refer to the MSGraph Reports.llb in the
 labview\examples\office directory for examples of inserting and
 formatting graphs in Word and Excel reports.

Parent topic:

Graphs Available in Reports

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=importing-macros-into-visual-basic-projects.html language=enus -->
## TOPIC 00005: Import Macros into Visual Basic Projects

- bundle_id: `labview-report-generation-toolkit`
- source_path: `importing-macros-into-visual-basic-projects.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/importing-macros-into-visual-basic-projects.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: If you are using a Microsoft Word or Microsoft Excel template that contains a macro, you can manually import the module containing the macro into the Visual Basic for Applications (VBA) project associated with the template.Complete the following steps to import the module manually: Open the template

### Import Macros into Visual Basic
 Projects

If you are using a Microsoft Word or Microsoft Excel template that contains a macro,
 you can manually import the module containing the macro into the Visual Basic for
 Applications (VBA) project associated with the template.

Complete the following steps to import the module manually:

1. Open the template in Word or Excel.
2. Select Tools»Macro»Visual Basic Editor. 
 Note If using
 Microsoft Word or Excel 2007, access the Visual Basic Editor by opening the
 Developer tab, select Visual
 Basic.
3. In the project window of the Visual Basic editor, right-click the template and
 select Import File from the shortcut menu.
4. Select the file in which the macro is defined and click the
 Open button.

The Word Import Module VI and the Excel Import Module VI
 can import modules dynamically from a VBA function file (.bas) or
 from a LabVIEW string that contains the module source code.

Parent topic:

Macros in Reports

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=including-report-generation-vis-in-stand-alon.html language=enus -->
## TOPIC 00006: Include Report Generation VIs in Stand-Alone Applications

- bundle_id: `labview-report-generation-toolkit`
- source_path: `including-report-generation-vis-in-stand-alon.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/including-report-generation-vis-in-stand-alon.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can include Report Generation VIs when you build stand-alone applications and create shared libraries in LabVIEW. You must use the Application Builder to build stand-alone applications.The LabVIEW Professional Development System includes the Application Builder. If you use the LabVIEW Base Devel

### Include Report Generation VIs in Stand-Alone
 Applications

You can include Report Generation VIs when you build stand-alone
 applications and create shared libraries in LabVIEW. You must use the Application
 Builder to build stand-alone applications.

Note

When building applications with Report Generation VIs, you must complete the
 following additional steps:

- Verify all files and VIs you use to build an application are in the LabVIEW project.
- Add the following files to the LabVIEW project: 
 labview\vi.lib\Utility\NIReport.llb\Word\NI_Word.lvclass
 if the application uses Microsoft Word.
 labview\vi.lib\Utility\NIReport.llb\Excel\NI_Excel.lvclass
 if the application uses Microsoft Excel.
 From the Source Files page of the Application
 Properties or Shared Library
 Properties dialog box, navigate to and select the class
 files you added to the project. Click the right arrow button next to the
 Always Included list to add the class files
 to the application.
- If the application you are building contains the MS Office Report
 Express VI, you must add any Microsoft Word or Microsoft Excel
 templates that you use to the LabVIEW project and to the application. From the
 Source Files page, select the template you use and
 click the right arrow button next to the Always Included
 list to add the template file to the application. 
 For example, if you are using the basic Excel template with the MS
 Office Report Express VI, add
 MSOffice_RGT_Template.xlt to the LabVIEW project and the
 application. The basic template files are located in the
 labview\templates\Report directory.Note The default custom
 destination for templates is a data subdirectory of the
 destination directory. Do not change the custom destination for the
 templates you add.
- If the application you are building contains the Word Add New
 Document VI, ensure that the version of Microsoft Office installed
 on the target computer is compatible with the application. 
 Applications containing the Word Add New Document VI that
 you build on a computer with Office XP can run only on target computers that
 also have Office XP. Applications containing the Word Add New
 Document VI that you build on a computer with Office 2003 or 2007
 can run only on target computers with either Office 2003 or Office 2007.

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=overview.html language=enus -->
## TOPIC 00007: LabVIEW Report Generation Toolkit Overview

- bundle_id: `labview-report-generation-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/overview.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Report Generation Toolkit for Microsoft Office provides VIs you can use to create and edit reports in Microsoft Word and Microsoft Excel formats. You can use the Report Generation VIs to perform the following tasks: Create and edit Word documents and Excel worksheets Use Word and Excel t

### LabVIEW Report Generation Toolkit
 Overview

The LabVIEW Report Generation Toolkit for Microsoft Office provides VIs you can use to
 create and edit reports in Microsoft Word and Microsoft Excel formats.

You can use the Report Generation VIs to perform the following
 tasks:

- Create and edit Word documents and Excel worksheets
- Use Word and Excel templates to create reports with a consistent style
- Insert, format, and edit text, tables, images, and graphs within Word documents and
 Excel worksheets
- Run Microsoft Visual Basic for Applications macros from Word documents and Excel
 worksheets

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=running-visual-basic-macros-in-word-and-excel.html language=enus -->
## TOPIC 00008: Run Visual Basic Macros in Word and Excel

- bundle_id: `labview-report-generation-toolkit`
- source_path: `running-visual-basic-macros-in-word-and-excel.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/running-visual-basic-macros-in-word-and-excel.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Word Run Macro VI and the Excel Run Macro VI to run Visual Basic for Applications (VBA) macros in Microsoft Word and Microsoft Excel. These VIs allow you to can run existing VBA macros and macros that you program to implement functionality that the LabVIEW Report Generation Toolkit f

### Run Visual Basic Macros in Word and
 Excel

You can use the Word Run Macro VI and the Excel Run
 Macro VI to run Visual Basic for Applications (VBA) macros in Microsoft
 Word and Microsoft Excel. These VIs allow you to can run existing VBA macros and macros
 that you program to implement functionality that the LabVIEW Report Generation Toolkit
 for Microsoft Office does not include.

Before running a macro, make sure you include the module that defines the macro in the VBA
 project associated with the report or in the template on which you based the report. The
 Word Import Module VI and the Excel Import
 Module VI can import modules dynamically from a VBA function file
 (.bas) or from a LabVIEW string that contains the module source
 code.

#### Macros
 with Input Arguments

If the macro you want to run requires input
 arguments, enter them into the parameters input of the VI.
 The data type for this input is an array of variants. You must convert all the input
 parameters sent to the macro to variants and bundle the parameters into an array.
 Use the To Variant function to convert the parameters to variants.
 Use the Build Array function to build the parameters into an
 array.

#### Retrieve an
 Output Value

If you want to retrieve an output value from a macro that
 LabVIEW runs, you can find this value in the return value
 parameter of the Word Run Macro VI or the Excel Run
 Macro VI. These VIs return the output value as a variant. Use the
 Variant To Data function to convert the value to
 LabVIEW-compatible data.

#### Manipulate
 an Object from Another Application

To run a macro that manipulates objects
 from another application, set a reference to the application type library. Creating
 a reference allows easy access to objects that use either the Word Add
 Reference to VBproj VI or the Excel Add Reference to
 VBproj VI. Refer to the Microsoft Visual Basic Help
 for more information about type libraries.

#### Example

Report
 Generation

Create Report

Append Table to Report VI

Word Import Module

Word Run Macro

ProcessTable

Word Remove
 Module

Save Report to
 File

Dispose
 Report

Figure 1.

[IMAGE alt='image' src='GUID-463FF6CE-749B-45E1-8361-577D79FB2E6A-a5.gif']

Run Macro on Word Table
 example

labview\examples\office\Word
 Reports.llb

Parent topic:

Macros in Reports

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=selecting-report-types.html language=enus -->
## TOPIC 00009: Select a Report Type

- bundle_id: `labview-report-generation-toolkit`
- source_path: `selecting-report-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/selecting-report-types.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a report in LabVIEW, you must decide which type of report you want. Consider whether you need to print, save, or email the report, and whether you want to use a template to create the report. Also consider the applications that are available on other computers from which users access

### Select a Report Type

When you create a report in LabVIEW, you must decide which type of report you want. Consider
 whether you need to print, save, or email the report, and whether you want to use a
 template to create the report. Also consider the applications that are available on
 other computers from which users access the report.

You can use LabVIEW to create HTML reports. LabVIEW supports a limited
 number of formatting options, and you cannot use templates. HTML
 reports require no additional software on the computer you use to create the reports.
 However, users need a web browser to read an HTML report. You can
 save an HTML report, but the report might not print with consistent
 formatting. LabVIEW supports a limited number of formatting options for
 HTML reports, and you cannot use templates.

With the Report Generation Toolkit, you also can create Microsoft Word and Microsoft Excel reports. You must have Word or Excel installed to create Word or Excel reports, respectively. Word and Excel reports also require that users who want to read or print the reports have the appropriate application on their computers. You can insert text, tables, images, and graphs into Word and Excel reports. You can save, print, and email the reports. You can set a variety of formatting options with text and tables, and you can use templates to create a consistent report style.

You can set the type of report you want to create in the Create Report VI and
 in the Report and MS Office Report Express
 VIs.

Parent topic:

Create Reports

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00010: LabVIEW Report Generation Toolkit User Manual

- bundle_id: `labview-report-generation-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Report Generation Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Inf

### LabVIEW Report Generation Toolkit
 User Manual

The LabVIEW Report Generation Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=using-bookmarks-and-named-ranges-in-reports.html language=enus -->
## TOPIC 00011: Bookmarks and Named Ranges in Reports

- bundle_id: `labview-report-generation-toolkit`
- source_path: `using-bookmarks-and-named-ranges-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/using-bookmarks-and-named-ranges-in-reports.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use bookmarks in Microsoft Word or named ranges in Microsoft Excel to insert text, numbers, tables, or pictures into a template.The filename extensions of Microsoft Word and Microsoft Excel files are as follows:Word template filenames include the .dot extension.Excel template filenames inclu

### Bookmarks and Named Ranges in Reports

You can use bookmarks in Microsoft Word or named ranges in Microsoft Excel to insert
 text, numbers, tables, or pictures into a template.

- Word template filenames include the .dot extension.
- Excel template filenames include the .xlt extension.
- (Office 2007) Word template filenames include the .dotx 
 extension.
- Excel template filenames include the .xltx extension.

You can use the MS Office Report Express VI to generate reports using
 templates. For each bookmark or named range, you can specify whether you want the
 Express VI to format data as text or, if the data is an array, as
 a table or graph.

You also can use the Report Generation VIs to insert text, tables, and graphs
 into bookmark or named range locations. In the MS Office
 parameters input, specify the bookmark or named range where the VI
 inserts data. If you do not specify a bookmark, the VI inserts data at the end of the
 document. If you do not specify a named range, the VI inserts data into the cell that
 the position input defines.

Refer to the Microsoft Word Help or the Microsoft Excel
 Help for information about creating and viewing bookmarks and named
 ranges, respectively.

Parent topic:

Create Reports

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=using-graphs-in-reports.html language=enus -->
## TOPIC 00012: Graphs Available in Reports

- bundle_id: `labview-report-generation-toolkit`
- source_path: `using-graphs-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/using-graphs-in-reports.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Report Generation VIs to insert and format graphs within Microsoft Word documents and Microsoft Excel worksheets.The Graphs and Pictures VIs support all graph types that Microsoft Office uses.

### Graphs Available in Reports

You can use the Report Generation VIs to
 insert and format graphs within Microsoft Word
 documents and Microsoft Excel worksheets.

The Graphs and Pictures VIs support all graph types that Microsoft Office
 uses.

- [Graph Formatting in Reports](formatting-graphs-in-reports.html)
- [Common Graph Types for Reports](common-graph-types-for-reports.html)

<!--NI_TOPIC bundle=labview-report-generation-toolkit path=using-macros.html language=enus -->
## TOPIC 00013: Macros in Reports

- bundle_id: `labview-report-generation-toolkit`
- source_path: `using-macros.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit/raw/resource/enus/using-macros.html
- document_id: `labview-report-generation-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Report Generation VIs to run Visual Basic for Applications (VBA) macros in Microsoft Word and Microsoft Excel.Before you can run a macro in a report, you must include the module that defines the macro in the VBA project associated with the report or in the template on which you based

### Macros in Reports

You can use the Report Generation VIs to run Visual
 Basic for Applications (VBA) macros in Microsoft Word and
 Microsoft Excel.

Before you can run a macro in a report, you must include the module that defines the macro in the
 VBA project associated with the report or in the template on
 which you based the report.

- [Run Visual Basic Macros in Word and Excel](running-visual-basic-macros-in-word-and-excel.html)
- [Import Macros into Visual Basic Projects](importing-macros-into-visual-basic-projects.html)
