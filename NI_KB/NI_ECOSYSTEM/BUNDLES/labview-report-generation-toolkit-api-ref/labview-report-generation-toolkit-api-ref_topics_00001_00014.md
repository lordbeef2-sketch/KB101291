# NI DOCUMENT BUNDLE: labview-report-generation-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-report-generation-toolkit-api-ref start=1 end=14 -->
<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/building_report_applications.html language=enus -->
## TOPIC 00001: Building Report Applications (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/building_report_applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/building_report_applications.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Building Report Applications (Report Generation Toolkit)

You can build stand-alone applications that [include Report Generation VIs](rgt_stand_alone_apps.html) and then distribute those applications to other computers.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/creating_bm_word.html language=enus -->
## TOPIC 00002: Using Bookmarks and Named Ranges in Reports (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/creating_bm_word.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/creating_bm_word.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Bookmarks and Named Ranges in Reports (Report Generation Toolkit)

You can use bookmarks in Microsoft Word or named ranges in Microsoft Excel to insert text, numbers, tables, or pictures into a template. Refer to the *Microsoft Word Help* or the *Microsoft Excel Help* for information about creating and viewing bookmarks and named ranges, respectively. Word template filenames include the .dot extension. Excel template filenames include the .xlt extension. (Office 2007) Word template filenames include the .dotx extension. Excel template filenames include the .xltx extension.

You can use the [MS Office Report](/csh?topicname=lvoffice/ms_office_report.html) Express VI to generate reports using templates. For each bookmark or named range, you can specify whether you want the Express VI to format data as text or, if the data is an array, as a table or graph.

You also can use the [Report Generation](/csh?topicname=lvoffice/report_generation_vis.html) VIs to insert text, tables, and graphs into bookmark or named range locations. In the **MS Office parameters** input, specify the bookmark or named range where the VI inserts data. If you do not specify a bookmark, the VI inserts data at the end of the document. If you do not specify a named range, the VI inserts data into the cell that the **position** input defines.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/creating_reports.html language=enus -->
## TOPIC 00003: Creating Reports (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/creating_reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/creating_reports.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Reports (Report Generation Toolkit)

You can use the [Report Generation](/csh?topicname=lvoffice/report_generation_vis.html) VIs to create reports in LabVIEW. You can generate different [types of reports](select_report_types.html), including Microsoft Word or Microsoft Excel reports. Create Word and Excel reports from existing or custom [templates](using_report_expvis.html) by inserting text, numbers, tables, or pictures into [placeholders](creating_bm_word.html).

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/graph_types.html language=enus -->
## TOPIC 00004: Common Graph Types for Reports (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/graph_types.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/graph_types.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Common Graph Types for Reports (Report Generation Toolkit)

The [Word Graphs and Pictures](/csh?topicname=lvoffice/word_graph_pic_vis.html) VIs and [Excel Graphs and Pictures](/csh?topicname=lvoffice/excel_graph_pic_vis.html) VIs support all the graph types that Microsoft Office uses. The following table defines some of the most commonly used graph types. Refer to the specific version of Microsoft Word or Microsoft Excel that you are using for a complete list of available graph types.

| Graph Type | Description |
| --- | --- |
| XY or Scatter | Displays the relationship or degree of a relationship between the numbers in several graph data series or plots two groups of numbers as one series of XY coordinates. XY graphs show uneven intervals of data. Arrange data with x values in one row or column, followed by one or more corresponding y values in adjacent rows or columns. Note Only XY graphs have the ability to scale both the x- and y-axes. |
|  | Note Only XY graphs have the ability to scale both the x- and y-axes. |
| Area | Displays the relative importance of values over a period of time. Although area graphs appear similar to line graphs, area graphs emphasize the amount of change or magnitude of values. |
| Line | Displays trends or changes in data over a period of time at even intervals. Although line graphs appear similar to area graphs, line graphs emphasize time flow and the rate of change. |
| Column | Displays variation over a period of time or illustrates comparisons between items. Stacked and 100-percent stacked column graphs show relationships to a whole. Although column graphs are similar to bar graphs, column graphs organize categories horizontally and values vertically. |
| Bar | Displays individual figures at a specific time or illustrates comparisons between items. Stacked and 100-percent stacked bar graphs show relationships to a whole. Although bar graphs are similar to column graphs, bar graphs organize categories vertically and values horizontally. This type of organization places more emphasis on comparisons and less emphasis on time. |
| Three-dimensional surface | Displays a view that resembles a sheet stretched over a three-dimensional column graph. You can use surface graphs to find the best combinations between two sets of data. Surface graphs can show relationships between large amounts of data that might otherwise be difficult to see. Colors or patterns indicate areas that have the same value. The colors do not mark the data series. The wire frame format displays the data in black and white. Contour graph formats provide a two-dimensional view of the data from above, similar to a two-dimensional topographic map. |
| Pie | Displays the relationship or proportions of the parts to the whole. You can use pie graphs to emphasize a significant element. Pie graphs always contain one data series. If you select more than one data series when you create a pie graph, only one data series displays. Use a doughnut graph, a variation of a pie graph, if you want to display more than one data series in a round graph format. |

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/import_macros.html language=enus -->
## TOPIC 00005: Importing Macros into Visual Basic Projects (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/import_macros.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/import_macros.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Importing Macros into Visual Basic Projects (Report Generation Toolkit)

If you are using a Microsoft Word or Microsoft Excel template that contains a macro, you can manually import the module containing the macro into the Visual Basic for Applications (VBA) project associated with the template. Complete the following steps to import the module manually.

1. Open the template in Word or Excel.
2. Select Tools»Macro»Visual Basic Editor .

|  | Note (Microsoft Word or Excel 2007) On the Developer tab, select Visual Basic. |
| --- | --- |

1. In the project window of the Visual Basic editor, right-click the template and select Import File from the shortcut menu.
2. Select the file in which the macro is defined and click the Open button.

The [Word Import Module](/csh?topicname=lvoffice/word_import_module.html) VI and the [Excel Import Module](/csh?topicname=lvoffice/excel_import_module.html) VI can import modules dynamically from a VBA function file (.bas) or from a LabVIEW string that contains the module source code.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/lvrgthelp_boilerplt.html language=enus -->
## TOPIC 00006: Report Generation Toolkit for Microsoft Office

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/lvrgthelp_boilerplt.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/lvrgthelp_boilerplt.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Report Generation Toolkit for Microsoft Office

May 2018, 372120H-01

The LabVIEW Report Generation Toolkit for Microsoft Office provides VIs you can use to create and edit [reports](../lvrgthelp/creating_reports.html) in Microsoft Word and Microsoft Excel formats. You can use the [Report Generation](/csh?topicname=lvoffice/report_generation_vis.html) VIs to perform the following tasks:

- Create and edit Word documents and Excel worksheets.
- Use Word and Excel templates to create reports with a consistent style.
- Insert, format, and edit text, tables, images, and graphs within Word documents and Excel worksheets.
- Run Microsoft Visual Basic for Applications macros from Word documents and Excel worksheets.

© 2018 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/report_related_doc.html language=enus -->
## TOPIC 00007: Related Documentation (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/report_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/report_related_doc.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Report Generation Toolkit)

The following documents contain information that you may find helpful as you use the LabVIEW Report Generation Toolkit for Microsoft Office.

- LabVIEW Report Generation Toolkit for Microsoft Office Readme—Use this file to learn important last-minute information, including installation and upgrade issues, compatibility issues, changes from the previous version, and known issues with the Report Generation Toolkit. Open this readme by selecting Start»All Programs»National Instruments»LabVIEW»Readme and opening readme_RepGen.html or by navigating to the labview\readme directory and opening readme_RepGen.html .
- LabVIEW Report Generation Toolkit for Microsoft Office Example VIs—Refer to the labview\examples\office directory for example VIs that demonstrate common tasks using the Report Generation Toolkit. You also can access these VIs by selecting Help»Find Examples and selecting Toolkits and Modules»Report Generation for Microsoft Office in the NI Example Finder window.
- Additional LabVIEW documentation .
- Microsoft Word Help and Microsoft Excel Help —Refer to these files for more information about using Microsoft Word and Microsoft Excel, respectively. These files are available with any version of Microsoft Office.
- Microsoft Visual Basic Help —Refer to this file for more information about using Microsoft Visual Basic for Applications. This file is available with any version of Microsoft Office.

Refer to the National Instruments Product Manuals Library for updated documentation resources.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/rgt_stand_alone_apps.html language=enus -->
## TOPIC 00008: Including Report Generation VIs in Stand-Alone Applications (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/rgt_stand_alone_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/rgt_stand_alone_apps.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Including Report Generation VIs in Stand-Alone Applications (Report Generation Toolkit)

You can include [Report Generation](/csh?topicname=lvoffice/report_generation_vis.html) VIs when you build stand-alone applications and create shared libraries in LabVIEW. You must use the Application Builder to build stand-alone applications.

|  | Note The LabVIEW Professional Development System includes the Application Builder. If you use the LabVIEW Base Development System or Full Development System, you can purchase the Application Builder separately by visiting the National Instruments Web site. |
| --- | --- |

When building applications with Report Generation VIs, you must complete the following additional steps:

- Verify all files and VIs you use to build an application are in the LabVIEW project .
- Add the following files to the LabVIEW project:
  - labview\vi.lib\Utility\NIReport.llb\Word\NI_Word.lvclass if the application uses Microsoft Word.
  - labview\vi.lib\Utility\NIReport.llb\Excel\NI_Excel.lvclass if the application uses Microsoft Excel.
  - From the Source Files page of the Application Properties or Shared Library Properties dialog box, navigate to and select the class files you added to the project. Click the right arrow button next to the Always Included list to add the class files to the application.
- If the application you are building contains the MS Office Report Express VI, you must add any Microsoft Word or Microsoft Excel templates that you use to the LabVIEW project and to the application. From the Source Files page, select the template you use and click the right arrow button next to the Always Included list to add the template file to the application. For example, if you are using the basic Excel template with the MS Office Report Express VI, add MSOffice_RGT_Template.xlt to the LabVIEW project and the application. The basic template files are located in the labview\templates\Report directory.
 [IMAGE alt='image' src='note.gif']
**Note** The default custom destination for templates is a data subdirectory of the destination directory. Do not change the custom destination for the templates you add.
- If the application you are building contains the Word Add New Document VI, ensure that the version of Microsoft Office installed on the target computer is compatible with the application. Applications containing the Word Add New Document VI that you build on a computer with Office XP can run only on target computers that also have Office XP. Applications containing the Word Add New Document VI that you build on a computer with Office 2003 or 2007 can run only on target computers with either Office 2003 or Office 2007.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/running_we_macros.html language=enus -->
## TOPIC 00009: Running Visual Basic Macros in Word and Excel (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/running_we_macros.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/running_we_macros.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Running Visual Basic Macros in Word and Excel (Report Generation Toolkit)

You can use the [Word Run Macro](/csh?topicname=lvoffice/word_run_macro.html) VI and the [Excel Run Macro](/csh?topicname=lvoffice/excel_run_macro.html) VI to run Visual Basic for Applications (VBA) macros in Microsoft Word and Microsoft Excel. These VIs can run existing VBA macros and macros that you program to implement functionality that the LabVIEW Report Generation Toolkit for Microsoft Office does not include.

If the macro you want to run requires input arguments, enter them into the **parameters** input of the VI. The data type for this input is an array of variants. You must convert all the input parameters sent to the macro to variants and bundle the parameters into an array. Use the [To Variant](/csh?topicname=glang/to_variant.html) function to convert the parameters to variants. Use the [Build Array](/csh?topicname=glang/build_array.html) function to build the parameters into an array.

If you want to retrieve an output value from a macro that LabVIEW runs, you can find this value in the **return
 value** parameter of the Word Run Macro VI or the Excel Run Macro VI. These VIs return the output value as a variant. Use the [Variant To Data](/csh?topicname=glang/variant_to_data.html) function to convert the value to LabVIEW-compatible data.

Before running a macro, make sure you include the module that defines the macro [in the VBA project associated with the report](import_macros.html) or in the template on which you based the report. The [Word Import Module](/csh?topicname=lvoffice/word_import_module.html) VI and the [Excel Import Module](/csh?topicname=lvoffice/excel_import_module.html) VI can import modules dynamically from a VBA function file (.bas) or from a LabVIEW string that contains the module source code.

To run a macro that manipulates objects from another application, set a reference to the application type library. Creating a reference allows easy access to objects that use either the [Word Add Reference to VBproj](/csh?topicname=lvoffice/word_add_ref_to_vbproj.html) VI or the [Excel Add Reference to VBproj](/csh?topicname=lvoffice/excel_add_ref_to_vbproj.html) VI. Refer to the *Microsoft Visual Basic Help* for more information about type libraries.

The following example uses [Report Generation](/csh?topicname=lvoffice/report_generation_vis.html) VIs to run a Word macro. The [Create Report](/csh?topicname=lvreport/new_report.html) VI creates a new Word document. The [Append Table to Report](/csh?topicname=lvreport/append_table_to_report.html) VI inserts a table into the report. The Word Import Module VI adds a VBA module to the report. The Word Run Macro VI runs the ProcessTable macro that the module defines. The [Word Remove Module](/csh?topicname=lvoffice/word_remove_module.html) VI deletes the module from the report. The [Save Report to File](/csh?topicname=lvreport/save_report_to_file.html) VI saves the report as a Word document. The [Dispose Report](/csh?topicname=lvreport/dispose_report.html) VI closes the Word document.

[IMAGE alt='image' src='noloc_bd_wmacro.gif']

The VI in the previous figure is similar to the Run Macro on Word Table example VI, located in the labview\examples\office\Word Reports.llb. 
 

 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/select_report_types.html language=enus -->
## TOPIC 00010: Selecting Report Types (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/select_report_types.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/select_report_types.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Selecting Report Types (Report Generation Toolkit)

When you create a report in LabVIEW, you must decide which type of report you want. Consider whether you need to print, save, or email the report, and whether you want to use a template to create the report. Also consider the applications that are available on other computers from which users access the report.

You can use LabVIEW to create HTML reports. LabVIEW supports a limited number of formatting options, and you cannot use templates. HTML reports require no additional software on the computer you use to create the reports. However, users need a Web browser to read an HTML report. You can save an HTML report, but the report might not print with consistent formatting. LabVIEW supports a limited number of formatting options for HTML reports, and you cannot use templates.

With the Report Generation Toolkit, you also can create Microsoft Word and Microsoft Excel reports. You must have Word or Excel installed to create Word or Excel reports, respectively. Word and Excel reports also require that users who want to read or print the reports have the appropriate application on their computers. You can insert text, tables, images, and graphs into Word and Excel reports. You can save, print, and email the reports. You can set a variety of formatting options with text and tables, and you can use templates to create a consistent report style.

You can set the type of report you want to create in the [Create Report](/csh?topicname=lvreport/new_report.html) VI and in the [Report](/csh?topicname=lvreport/report.html) and [MS Office Report](/csh?topicname=lvoffice/ms_office_report.html) Express VIs.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/use_graph_in_report.html language=enus -->
## TOPIC 00011: Formatting Graphs in Reports (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/use_graph_in_report.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/use_graph_in_report.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Formatting Graphs in Reports (Report Generation Toolkit)

The [Excel Graphs and Pictures](/csh?topicname=lvoffice/excel_graph_pic_vis.html) VIs and the [Word Graphs and Pictures](/csh?topicname=lvoffice/word_graph_pic_vis.html) VIs in the LabVIEW Report Generation Toolkit for Microsoft Office provide an interface to the graphing capabilities of Microsoft Office.

When you insert graphs into reports, you must send data to the graph as a 2D array of numbers. You can send row and column headers, or values and categories, as 1D arrays of strings. Graphs can hold up to 4,000 rows and 4,000 columns including row and column headers, and they can display up to 256 data series.

Graphs and images form a collection for each Microsoft Word document or Microsoft Excel worksheet. Each object in a collection has an index value based on the order of the objects in the document or worksheet. Index values begin at 0. The indexes for graphs and images are separate. For example, if an Excel report contains an image, a second image, and a graph, the index value for the graph is 0 because the graph is the first graph in the report.

Enter index values in the **graph index** or **picture index** inputs of the Graphs and Pictures VIs to specify which graph or image you want the VI to format. By default, Graphs and Pictures VIs apply to the last object in a collection of a document or worksheet. You can avoid confusion with collection index values by formatting graphs and images immediately after you insert them into a report.

The Graphs and Pictures VIs support all graph types that Microsoft Office uses. If you want to format a graph in a way that the Graphs and Pictures VIs do not support, insert the graph in a Word or Excel template, format the graph, and use the [Word Update Graph](/csh?topicname=lvoffice/word_update_graph.html) VI or the [Excel Update Graph](/csh?topicname=lvoffice/excel_update_graph.html) VI to fill the graph with data.

Refer to the MSGraph Reports.llb in the labview\examples\office directory for examples of inserting and formatting graphs in Word and Excel reports. 
 

 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/using_graphs.html language=enus -->
## TOPIC 00012: Using Graphs in Reports (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/using_graphs.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/using_graphs.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Graphs in Reports (Report Generation Toolkit)

You can use the [Report Generation](/csh?topicname=lvoffice/report_generation_vis.html) VIs to insert and [format](use_graph_in_report.html) graphs within Microsoft Word documents and Microsoft Excel worksheets. The Graphs and Pictures VIs support all [graph types](graph_types.html) that Microsoft Office uses.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/using_macros.html language=enus -->
## TOPIC 00013: Using Macros (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/using_macros.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/using_macros.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Macros (Report Generation Toolkit)

You can use the [Report Generation](/csh?topicname=lvoffice/report_generation_vis.html) VIs to [run Visual Basic for Applications (VBA) macros](running_we_macros.html) in Microsoft Word and Microsoft Excel. Before you can run a macro in a report, you must include the module that defines the macro [in the VBA project associated with the report](import_macros.html) or in the template on which you based the report.

<!--NI_TOPIC bundle=labview-report-generation-toolkit-api-ref path=lvrgthelp/using_report_expvis.html language=enus -->
## TOPIC 00014: Creating Reports from Templates (Report Generation Toolkit)

- bundle_id: `labview-report-generation-toolkit-api-ref`
- source_path: `lvrgthelp/using_report_expvis.html`
- source_url: https://docs-be.ni.com/bundle/labview-report-generation-toolkit-api-ref/raw/resource/enus/lvrgthelp/using_report_expvis.html
- document_id: `labview-report-generation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Reports from Templates (Report Generation Toolkit)

You can use the [MS Office Report](/csh?topicname=lvoffice/ms_office_report.html) Express VI to create a report from a Microsoft Word or Microsoft Excel template. Word and Excel templates contain placeholders for data and components that are common to all reports. The MS Office Report Express VI inserts data into the placeholders so you can display, print, or save the resulting report.

The LabVIEW Report Generation Toolkit for Microsoft Office includes basic templates for Word documents and Excel worksheets. These templates are located in the labview\templates\Report directory.

Complete the following steps to use the MS Office Report Express VI to create a report from a basic Word template.

1. Place the MS Office Report Express VI on the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
2. In the configuration dialog box that appears, select Basic Report for Word from the Template pull-down list.

|  | Note Do not change the Report Generation Toolkit basic templates for Word and Excel. If you want to edit the basic templates, save them with different filenames and select Custom Report for Word or Custom Report for Excel in the configuration dialog box of the MS Office Report Express VI. |
| --- | --- |

1. Click the Author_Name item in the Bookmarks in the Selected Template list. Each item in this list represents a placeholder in the template.
2. Select Fixed Value from the Value Source pull-down list.
3. In the Fixed Value text box that appears, enter your name.
4. Repeat steps 3 through 5 for the Company_Name and Report_Title_Main items in the Bookmarks in the Selected Template list. Enter My First Report for the Report_Title_Main item.
5. Click the Graph1_Data_Input item in the Bookmarks in the Selected Template list. Verify that the Value Source for this item is Input and that the Input Appearance in Report is Graph .
6. In the Report Destination pull-down list, select Open in Microsoft Office .
7. Click the OK button to close the configuration dialog box. The Express VI icon on the block diagram displays inputs for all the bookmarks configured with a Value Source of Input .
8. Place the Simulate Signal Express VI on the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
9. Click the OK button in the configuration dialog box that appears.
10. Wire the Sine output of the Simulate Signal Express VI to the Graph1_Data_Input input of the MS Office Report Express VI.
11. Run the VI. Notice that the generated report opens in Microsoft Word and contains the text you entered for each placeholder in the template as well as the sine wave you created with the Simulate Signal Express VI.

Refer to the following VIs for other examples of using the MS Office Report Express VI to generate reports from templates.

- labview\examples\office\Excel Reports.llb\Generate Report From Template (Excel).vi Open example
- labview\examples\office\Word Reports.llb\Generate Report From Template (Word).vi Open example

You can create custom report templates in Word and Excel to ensure a consistent appearance in multiple reports. Use templates to define page size, text formatting, and other aspects of report appearance. You also can specify placeholders for text, tables, graphs, and images. Both Word and Excel provide ways to insert placeholders into documents and worksheets. Use [bookmarks in Word](../lvrgthelp/creating_bm_word.html) and [named ranges in Excel](../lvrgthelp/creating_bm_word.html) to define placeholders.

Refer to the *Microsoft Word Help* or *Microsoft Excel Help* for more information about creating templates.
