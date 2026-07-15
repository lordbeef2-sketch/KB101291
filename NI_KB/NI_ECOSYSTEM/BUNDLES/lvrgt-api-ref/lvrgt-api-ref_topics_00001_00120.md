# NI DOCUMENT BUNDLE: lvrgt-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvrgt-api-ref start=1 end=120 -->
<!--NI_TOPIC bundle=lvrgt-api-ref path=dialog-boxes/configure-date-time-format-dialog-box.html language=enus -->
## TOPIC 00001: Configure Date & Time Format Dialog Box

- bundle_id: `lvrgt-api-ref`
- source_path: `dialog-boxes/configure-date-time-format-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/dialog-boxes/configure-date-time-format-dialog-box.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the configuration dialog box of the MS Office Report Express VI, select a Value Source of System Defined Value and click the Configure Date & Time Format button to display this dialog box. Use this dialog box to set date and time formatting for system-defined values. This dialog box includes the

### Configure Date & Time Format Dialog Box

In the configuration dialog box of the [MS Office Report](/csh?context=lvmnt_rgt_lvoffice_ms_office_report) Express VI, select a **Value Source** of **System Defined Value** and click the **Configure Date & Time Format** button to display this dialog box.

Use this dialog box to set date and time formatting for system-defined values.

This dialog box includes the following components:

- Date Format —Specifies whether the VI uses the system date format or a custom date format. The default is the LabVIEW system date format. This page appears only if you specify a System Defined Value of Date in the configuration dialog box of the MS Office Report Express VI. If you choose to use a custom date format, you can specify the order in which to display the month, day, and year. You also can specify whether the year displays in two-digit or four-digit format, or does not display at all.
- Date preview —Displays a preview of the date in the format you specify.
- Time Format —Specifies whether you want to use the system-defined time format or a custom time format. The default is the LabVIEW system-defined format. This page appears only if you specify a System Defined Value of Time in the configuration dialog box of the MS Office Report Express VI. If you choose to use a custom time format, you can specify whether to use a 12-hour or 24-hour clock. You also can specify the order in which to display the hours, minutes, and seconds.
- Time preview —Displays a preview of the time in the format you specify.

Parent topic:

Report Generation Toolkit Dialog Box Reference

<!--NI_TOPIC bundle=lvrgt-api-ref path=dialog-boxes/configure-save-to-file-options-dialog-box.html language=enus -->
## TOPIC 00002: Configure Save to File Options Dialog Box

- bundle_id: `lvrgt-api-ref`
- source_path: `dialog-boxes/configure-save-to-file-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/dialog-boxes/configure-save-to-file-options-dialog-box.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the configuration dialog box of the MS Office Report Express VI, specify a Report Destination of Save to File and click the Configure Save to File Options button to display this dialog box. Use this dialog box to set options for saving reports to files. This dialog box includes the following comp

### Configure Save to File Options Dialog Box

In the configuration dialog box of the [MS Office Report](/csh?context=lvmnt_rgt_lvoffice_ms_office_report) Express VI, specify a **Report Destination** of **Save to File** and click the **Configure Save to File Options** button to display this dialog box.

Use this dialog box to set options for saving reports to files.

This dialog box includes the following components:

- Base File Name —Specifies the filename and location that the VI uses to save the report.
- Action —Specifies whether you want to save the report as a single file or as a series of files.
  - Save to one file —Saves the report to a single file.
    - Ask user to choose file —Causes a file dialog box to appear so users can navigate to the filename and directory where they want to save the report. If you do not place a checkmark in the checkbox, the VI uses the filename and directory that Base File Name specifies.
  - Save to a series of files —Saves the report or reports into multiple files. You can specify whether you want the series of filenames to include the date and time, sequential numbering, or both.
    - Date and Time —Appends the current date and time to the filename to distinguish among multiple files.
    - Sequential numbers —Appends numbers in sequential order to the filename to distinguish among multiple files.
      - Pad with zeros —Adds a zero to the sequential numbers from one to nine in the filename.
      - Width —Specifies the number of zeros to use if you pad the filename numbers with zeros. The default is 2.
    - Both —Appends each filename in the series with the date and time, followed by a number in sequential order.
    - Filename preview —Contains an example of the filenaming convention the VI uses if you select Save to a series of files .
- If a file already exists —Specifies the action the VI takes if the filename exists. The default is to rename the existing file. You also can set the VI to select another name for the new report filename or to overwrite the existing file with the new report.

Parent topic:

Report Generation Toolkit Dialog Box Reference

<!--NI_TOPIC bundle=lvrgt-api-ref path=dialog-boxes/rgt-dialog-box-help.html language=enus -->
## TOPIC 00003: Report Generation Toolkit Dialog Box Reference

- bundle_id: `lvrgt-api-ref`
- source_path: `dialog-boxes/rgt-dialog-box-help.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/dialog-boxes/rgt-dialog-box-help.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find detailed information about dialog boxes, including the purpose of the dialog box, how to access the dialog box, and detailed information about the controls and indicators in the dialog box. These pages are accessed by clicking the Help buttons in the dialog boxes.

### Report Generation Toolkit Dialog Box Reference

Find detailed information about dialog boxes, including the purpose of the dialog box, how to access the dialog box, and detailed information about the controls and indicators in the dialog box.

These pages are accessed by clicking the **Help** buttons in the dialog boxes.

<!--NI_TOPIC bundle=lvrgt-api-ref path=errors/error-codes.html language=enus -->
## TOPIC 00004: Error Codes

- bundle_id: `lvrgt-api-ref`
- source_path: `errors/error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/errors/error-codes.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Report Generation Toolkit VIs can return the following error codes. Code Name Description‑41117 LVRGT_GetXLDataFailed One or more cells contain invalid data or data that is incompatible with the specified data type. Remove all invalid data, or specify a different data type.‑41116 LVRGT_SetXLHead

### Error Codes

The [Report Generation Toolkit](../functions/report-generation-vis.html) VIs can return the following error codes.

| Code | Name | Description |
| --- | --- | --- |
| ‑41117 | LVRGT_GetXLDataFailed | One or more cells contain invalid data or data that is incompatible with the specified data type. Remove all invalid data, or specify a different data type. |
| ‑41116 | LVRGT_SetXLHeaderFailed | The header text you specified does not fit within the Excel header field. Consider reducing the font size of the header or reducing the number of characters in the header. |
| ‑41115 | LVRGT_SetXLFooterFailed | The footer text you specified does not fit within the Excel footer field. Consider reducing the font size of the footer or reducing the number of characters in the footer. |
| ‑41114 | LVRGT_MSGraphMaxPts | Graphs you create or edit in Microsoft Office cannot contain more than 4,000 rows or columns, including row and column headers. |
| ‑41113 | LVRGT_VBATrustedSource | You have not selected Visual Basic Project as a Trusted Source in Microsoft Word or Excel. Check the Macro Security settings in Word or Excel. |
| ‑41112 | LVRGT_UncommittedChanges | Uncommitted changes appear in an active cell of an Excel worksheet. Select the cell and press the Enter key to commit all changes. |
| ‑41111 | LVRGT_RptFromTemplate | You must configure the MS Office Report Express VI to generate reports from a template. |
| ‑41110 | LVRGT_InvalidBkmkName | You specified invalid Word bookmarks or Excel named ranges. |
| ‑41109 | LVRGT_HeaderFooterPrint | You have not installed a printer. You cannot set headers or footers in Excel unless a printer is installed. |
| ‑41108 | LVRGT_NoPrinter | You have not installed a printer. |
| ‑41107 | LVRGT_GraphNotSupported | You cannot select a graph as the input appearance for this data type. |
| ‑41106 | LVRGT_OpenFailed | Microsoft Word or Excel did not open. |
| ‑41105 | LVRGT_NoMSGraph | The Microsoft Office installation on the computer does not include Microsoft Graph. You must install the Microsoft Graph component. |
| ‑41104 | LVRGT_ArrayDimTooHigh | You cannot use arrays with more than two dimensions. |
| ‑41103 | LVRGT_UnsupDataType | The LabVIEW Report Generation Toolkit for Microsoft Office does not support the data type you are using. |

<!--NI_TOPIC bundle=lvrgt-api-ref path=functions/ms-office-report-express-vi.html language=enus -->
## TOPIC 00005: MS Office Report Express VI

- bundle_id: `lvrgt-api-ref`
- source_path: `functions/ms-office-report-express-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/functions/ms-office-report-express-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Report Generation VIs Allows you to configure Word and Excel reports using templates. You can use basic templates that the LabVIEW Report Generation Toolkit for Microsoft Office includes, or you can create templates in Word and Excel. Examples Dialog Box OptionsBlock Diagram InputsBl

### MS Office Report Express VI

**Owning Palette:** [Report Generation VIs](/csh?context=lvmnt_rgt_lvoffice_report_generation_vis)

Allows you to configure Word and Excel reports using [templates](/csh?context=lvmnt_rgt_lvrgthelp_using_report_expvis). You can use basic templates that the LabVIEW Report Generation Toolkit for Microsoft Office includes, or you can create templates in Word and Excel.

Examples

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Report Template | Contains the following options: Template—Specifies the type of template you want to use for the report. You can select basic Word or Excel templates or custom templates that you create. Path to Template—Specifies the path to the report template you select. If you want to use a custom template, navigate to the location of the template file. |
| Report Contents | Contains the following options: Named Range in the Selected Template—Lists the named range of cells that the specified Excel template contains. Named Range—Contains the title of the named range selected in Named Range in the Selected Template. Bookmarks in the Selected Template—Lists the bookmarks that the specified Word template contains. Bookmark—Contains the title of the bookmark selected in Bookmarks in the Selected Template. Value Source—Specifies whether the selected Named Range or Bookmark is an input, fixed value, or automatic value. The default is Input, which allows you to set values by wiring data to the Express VI. Fixed Value allows you to enter a specific value. Automatic Value allows you to select an option from a set of values that LabVIEW can determine programmatically, such as date, time, and operator name. Input Appearance in Report—Specifies how data from a specified input appears in the report. The default is Automatic, in which the VI formats the data as a text field or, if it is an array, as a table. If the data is in an array, you also can select the Table or Graph options. This control appears only if you select Input for Value Source. Fixed Value—Contains a value or string you want to associate with the selected named range or bookmark. This control appears only if you select Fixed Value for Value Source. System Defined Value—Specifies a value that LabVIEW determines programmatically and inserts into the selected named range or bookmark. You can select date, time, or username information. |
| Report Destination | Determines whether the report opens in Word or Excel, prints to a printer, or is saved to a file. If you select Open in Microsoft Office, Word or Excel opens in a maximized window size when you run the VI. |
| Configure Save to File Options | Opens the Configure Save to File Options dialog box, which allows you to set the filename, location, and number of files you want to save. The button is active only if you select Save to File in Report Destination. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| Enable | Enables or disables the Express VI. The default is TRUE. |
| error in (no error) | Describes error conditions that occur before this node runs. |
| Printer Settings | Specifies the printer to use and the number of copies of the report to print. This input appears only if you select Print to Printer as the report destination. Printer Name—Contains the name of the printer to use. Number of Copies—Specifies the number of copies of the report to print. |
| Path to Save Report | Specifies the location where you want to save the report. This input appears only if you select Save to File as the report destination. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| Saved Report Path | Returns the path where this Express VI saves the report. |
| error out | Contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the MS Office Report VI:

- Generate Report From Template (Excel) VI: labview\examples\office\Excel Reports.llb
- Generate Report From Template (Word) VI: labview\examples\office\Word Reports.llb

Parent topic:

Report Generation VIs

<!--NI_TOPIC bundle=lvrgt-api-ref path=functions/report-generation-vis.html language=enus -->
## TOPIC 00006: Report Generation VIs

- bundle_id: `lvrgt-api-ref`
- source_path: `functions/report-generation-vis.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/functions/report-generation-vis.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the Report Generation VIs to create and edit reports in Microsoft Word and Microsoft Excel formats. The VIs on this palette can return general LabVIEW error codes,

### Report Generation VIs

This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Report Generation VIs to create and edit [reports](/csh?context=lvmnt_rgt_lvrgthelp_creating_reports) in Microsoft Word and Microsoft Excel formats.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../errors/error-codes.html).

| Palette Object | Description |
| --- | --- |
| MS Office Report | Allows you to configure Word and Excel reports using templates. You can use basic templates that the LabVIEW Report Generation Toolkit for Microsoft Office includes, or you can create templates in Word and Excel. |

| Subpalette | Description |
| --- | --- |
| Advanced Report Generation VIs | Use the Advanced Report Generation VIs to manipulate reports you create in LabVIEW. |
| Excel Specific VIs | Use the Excel Specific VIs to incorporate Microsoft Excel features into LabVIEW reports. |
| HTML Reports Only VIs | Use the HTML Reports Only VIs to manipulate HTML reports you create in LabVIEW. |
| Report Layout VIs | Use the Report Layout VIs to manipulate the layout of reports you create in LabVIEW. |
| VI Documentation VIs | Use the VI Documentation VIs to customize the VI documentation you print or save to a report. VI documentation can include the icon and connector pane, front panel, block diagram, VI hierarchy, revision history, controls and indicators, and so on. |
| Word Specific VIs | Use the Word Specific VIs to incorporate Microsoft Word features into LabVIEW reports. |

2001–2008 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/excel-mnu.html language=enus -->
## TOPIC 00007: Excel Specific

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/excel-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/excel-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Excel Specific VIs to incorporate Microsoft Excel features into LabVIEW reports. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Excel Specific

Use the Excel Specific VIs to incorporate Microsoft Excel features into LabVIEW reports.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='excel-mnu.png']

- [Excel Easy Title VI](../../../../vi-lib/addons/office/excel-llb/excel-easy-title-vi.html) Adds a title to a Microsoft Excel report.
- [Excel Easy Text VI](../../../../vi-lib/addons/office/excel-llb/excel-easy-text-vi.html) Inserts text into a Microsoft Excel report.
- [Excel Easy Table VI](../../../../vi-lib/addons/office/excel-llb/excel-easy-table-vi.html) Inserts and formats a table into a Microsoft Excel report. The data type you wire to the text data input determines the polymorphic instance to use.
- [Excel Easy Graph VI](../../../../vi-lib/addons/office/excel-llb/excel-easy-graph-vi.html) Inserts a graph into a Microsoft Excel report.
- [Excel General](../../../../menus/categories/programming/ni-report/excelgen-mnu.html) Use the Excel General VIs to perform general tasks in Microsoft Excel reports, such as adding and retrieving worksheets, inserting cells, and searching worksheets.
- [Excel Format](../../../../menus/categories/programming/ni-report/excelfrm-mnu.html) Use the Excel Format VIs to format cells in Microsoft Excel reports.
- [Excel Graphs and Pictures](../../../../menus/categories/programming/ni-report/excelpic-mnu.html) Use the Excel Graphs and Pictures VIs to format graphs and images in Microsoft Excel reports. The Excel Graph VIs only manipulate graphs you create using the LabVIEW Report Generation Toolkit for Microsoft Office. The VIs do not manipulate graphs you create in Excel manually.
- [Excel Advanced](../../../../menus/categories/programming/ni-report/exceladv-mnu.html) Use the Excel Advanced VIs to perform complex tasks in Microsoft Excel reports.

Parent topic:

Report Generation VIs

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/exceladv-mnu.html language=enus -->
## TOPIC 00008: Excel Advanced

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/exceladv-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/exceladv-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Excel Advanced VIs to perform complex tasks in Microsoft Excel reports. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Excel Advanced

Use the Excel Advanced VIs to perform complex tasks in Microsoft Excel reports.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='exceladv-mnu.png']

- [Excel Rename Worksheet VI](../../../../vi-lib/addons/office/excel-llb/excel-rename-worksheet-vi.html) Renames the current worksheet.
- [Excel Insert Formula VI](../../../../vi-lib/addons/office/excel-llb/excel-insert-formula-vi.html) Inserts a formula in the cell defined by the start cluster. If you use the name parameter to specify a named range, the VI inserts the formula from the top left cell of the range.
- [Excel Sort Data VI](../../../../vi-lib/addons/office/excel-llb/excel-sort-data-vi.html) Sorts the range of cells specified by the start and end clusters.
- [Excel Insert Object VI](../../../../vi-lib/addons/office/excel-llb/excel-insert-object-vi.html) Inserts an object associated with a file in the cell specified by the position/size cluster.
- [Excel Set Paper Size VI](../../../../vi-lib/addons/office/excel-llb/excel-set-paper-size-vi.html) Sets the paper size you want to associate with a worksheet.
- [Excel Send Workbook VI](../../../../vi-lib/addons/office/excel-llb/excel-send-workbook-vi.html) Sends the current workbook to a list of recipients via email. You can use this VI only if you configure Microsoft Outlook or Outlook Express as the default email application.
- [Excel Get ActiveX References VI](../../../../vi-lib/addons/office/excel-llb/excel-get-activex-references-vi.html) Returns ActiveX references to Microsoft Excel.
- [Excel Get Excel Location VI](../../../../vi-lib/addons/office/excel-llb/excel-get-excel-location-vi.html) Returns the row and column indexes of a cell that you identify by Excel syntax.
- [Excel Set Excel Location VI](../../../../vi-lib/addons/office/excel-llb/excel-set-excel-location-vi.html) Returns the Excel syntax name of a cell that you identify by row and column indexes.
- [Excel Macros](../../../../menus/categories/programming/ni-report/excmacro-mnu.html) Use the Excel Macros VIs to edit and run macros in Microsoft Excel reports.

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/excelfrm-mnu.html language=enus -->
## TOPIC 00009: Excel Format

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/excelfrm-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/excelfrm-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Excel Format VIs to format cells in Microsoft Excel reports. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Excel Format

Use the Excel Format VIs to format cells in Microsoft Excel reports.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='excelfrm-mnu.png']

- [Excel Set Cell Format VI](../../../../vi-lib/addons/office/excel-llb/excel-set-cell-format-vi.html) Sets the number format of the cells specified by the start and end clusters or by a named range.
- [Excel Set Cell Font VI](../../../../vi-lib/addons/office/excel-llb/excel-set-cell-font-vi.html) Sets the font of the cells specified by the start and end clusters or by a named range.
- [Excel Set Cell Alignment VI](../../../../vi-lib/addons/office/excel-llb/excel-set-cell-alignment-vi.html) Sets the alignment of the cells specified by the start and end clusters or by a named range.
- [Excel Set Cell Dimension VI](../../../../vi-lib/addons/office/excel-llb/excel-set-cell-dimension-vi.html) Sets the dimensions of the cells specified by the start and end clusters or by a named range.
- [Excel Set Cell Color and Border VI](../../../../vi-lib/addons/office/excel-llb/excel-set-cell-color-and-border-vi.html) Sets the borders and background color of the cells specified by the start and end clusters or by a named range.
- [Excel Merge Cells VI](../../../../vi-lib/addons/office/excel-llb/excel-merge-cells-vi.html) Merges the range of cells specified by the start and end clusters.

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/excelgen-mnu.html language=enus -->
## TOPIC 00010: Excel General

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/excelgen-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/excelgen-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Excel General VIs to perform general tasks in Microsoft Excel reports, such as adding and retrieving worksheets, inserting cells, and searching worksheets. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation To

### Excel General

Use the Excel General VIs to perform general tasks in Microsoft Excel reports, such as adding and retrieving worksheets, inserting cells, and searching worksheets.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='excelgen-mnu.png']

- [Excel Add Worksheet VI](../../../../vi-lib/addons/office/excel-llb/excel-add-worksheet-vi.html) Adds a new worksheet to the worksheet collection.
- [Excel Get Worksheet VI](../../../../vi-lib/addons/office/excel-llb/excel-get-worksheet-vi.html) Makes a specified worksheet the current worksheet. Use the worksheet index or name parameter to specify the worksheet you want to set as current.
- [Excel Insert Cells VI](../../../../vi-lib/addons/office/excel-llb/excel-insert-cells-vi.html) Inserts a new cell, row, or column into the current worksheet from a position that the row and column indexes specify.
- [Excel Bring to Front VI](../../../../vi-lib/addons/office/excel-llb/excel-bring-to-front-vi.html) Changes the state of a Microsoft Excel window to minimized, maximized, or normal.
- [Excel Find and Replace VI](../../../../vi-lib/addons/office/excel-llb/excel-find-and-replace-vi.html) Searches the occurrences of searched string and replaces them with a new string or numeric value. The data type you wire to the replacement input determines the polymorphic instance to use.
- [Excel Set Page Numbering VI](../../../../vi-lib/addons/office/excel-llb/excel-set-page-numbering-vi.html) Activates the page numbering on the current document.
- [Excel Workbook Properties VI](../../../../vi-lib/addons/office/excel-llb/excel-workbook-properties-vi.html) Sets the properties of the current workbook, such as the author, title, and subject. You also can use this VI to return the number of worksheets in the current workbook.
- [Excel Get Data VI](../../../../vi-lib/addons/office/excel-llb/excel-get-data-vi.html) Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use.
- [Excel Get Last Row VI](../../../../vi-lib/addons/office/excel-llb/excel-get-last-row-vi.html) Retrieves the coordinates of the last row in an Excel worksheet. Use the MS Office parameters input to append the contents of the row to a report.

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/excelpic-mnu.html language=enus -->
## TOPIC 00011: Excel Graphs and Pictures

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/excelpic-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/excelpic-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Excel Graphs and Pictures VIs to format graphs and images in Microsoft Excel reports. The Excel Graph VIs only manipulate graphs you create using the LabVIEW Report Generation Toolkit for Microsoft Office. The VIs do not manipulate graphs you create in Excel manually. If you create a graph t

### Excel Graphs and Pictures

Use the Excel Graphs and Pictures VIs to format graphs and images in Microsoft Excel reports. The Excel Graph VIs only manipulate graphs you create using the LabVIEW Report Generation Toolkit for Microsoft Office. The VIs do not manipulate graphs you create in Excel manually.

Note

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='excelpic-mnu.png']

- [Excel Insert Graph VI](../../../../vi-lib/addons/office/excel-llb/excel-insert-graph-vi.html) Inserts a new graph into the current worksheet and fills the graph with numeric data.
- [Excel Update Graph VI](../../../../vi-lib/addons/office/excel-llb/excel-update-graph-vi.html) Updates the data of an existing graph.
- [Excel Set Graph Colors VI](../../../../vi-lib/addons/office/excel-llb/excel-set-graph-colors-vi.html) Sets the color attributes, marker style, and plot line weight in an existing graph.
- [Excel Set Graph Font VI](../../../../vi-lib/addons/office/excel-llb/excel-set-graph-font-vi.html) Sets the title text and the title font of the x- and y-axes.
- [Excel Set Graph Scale VI](../../../../vi-lib/addons/office/excel-llb/excel-set-graph-scale-vi.html) Sets the scale parameters of the x- and y-axes and formats the graph gridlines.
- [Excel Quit Graph VI](../../../../vi-lib/addons/office/excel-llb/excel-quit-graph-vi.html) Closes all ActiveX references related to a graph. Use this VI after you insert, update, or format a graph using Excel.
- [Excel Format Image VI](../../../../vi-lib/addons/office/excel-llb/excel-format-image-vi.html) Formats the image specified by picture index . You can resize the image or modify its color type .

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/excmacro-mnu.html language=enus -->
## TOPIC 00012: Excel Macros

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/excmacro-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/excmacro-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Excel Macros VIs to edit and run macros in Microsoft Excel reports. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Excel Macros

Use the Excel Macros VIs to edit and run macros in Microsoft Excel reports.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='excmacro-mnu.png']

- [Excel Add Reference to VBproj VI](../../../../vi-lib/addons/office/excel-llb/excel-add-reference-to-vbproj-vi.html) Adds a reference to a type library in the Microsoft Visual Basic project associated with the current workbook.
- [Excel Import Module VI](../../../../vi-lib/addons/office/excel-llb/excel-import-module-vi.html) Imports an external module (*.bas) in the Microsoft Visual Basic project associated with the current workbook.
- [Excel Run Macro VI](../../../../vi-lib/addons/office/excel-llb/excel-run-macro-vi.html) Runs a macro on the current Excel workbook. You must define the macro in the Microsoft Visual Basic project associated with the workbook.
- [Excel Remove Module VI](../../../../vi-lib/addons/office/excel-llb/excel-remove-module-vi.html) Removes an external module from the Microsoft Visual Basic project associated with the current workbook.

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/wdconst-mnu.html language=enus -->
## TOPIC 00013: Word Constants

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/wdconst-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/wdconst-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Word Constants to define specific formatting attributes in Microsoft Word reports. icon

### Word Constants

Use Word Constants to define specific formatting attributes in Microsoft Word reports.

[IMAGE alt='icon' src='wdconst-mnu.png']

- [Borders and Shading Constant (Table)](../../../../vi-lib/addons/office/word-llb/borders-and-shading-constant-table-shell-vi.html) Defines the borders and shading attributes of a table in Word.
- [Borders and Shading Constant](../../../../vi-lib/addons/office/word-llb/borders-and-shading-constant-shell-vi.html) Defines the borders and shading attributes of a document.
- [Indent and Spacing Constant](../../../../vi-lib/addons/office/word-llb/indent-and-spacing-constant-shell-vi.html) Defines the indent and spacing attributes for a specified range within a Word document.
- [Line and Page Break Constant](../../../../vi-lib/addons/office/word-llb/line-and-page-break-constant-shell-vi.html) Defines line and page break attributes of a specified range within a document.

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/word-mnu.html language=enus -->
## TOPIC 00014: Word Specific

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/word-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/word-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Word Specific VIs to incorporate Microsoft Word features into LabVIEW reports. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Word Specific

Use the Word Specific VIs to incorporate Microsoft Word features into LabVIEW reports.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='word-mnu.png']

- [Word Easy Title VI](../../../../vi-lib/addons/office/word-llb/word-easy-title-vi.html) Adds a title to a Microsoft Word report.
- [Word Easy Text VI](../../../../vi-lib/addons/office/word-llb/word-easy-text-vi.html) Adds text to a Microsoft Word report.
- [Word Easy Table VI](../../../../vi-lib/addons/office/word-llb/word-easy-table-vi.html) Inserts and formats a table into a Microsoft Word report. The data type you wire to the data input determines the polymorphic instance to use.
- [Word Easy Graph VI](../../../../vi-lib/addons/office/word-llb/word-easy-graph-vi.html) Inserts a graph into a Microsoft Word report.
- [Word General](../../../../menus/categories/programming/ni-report/wordgen-mnu.html) Use Word General VIs to perform tasks in Microsoft Word reports, such as adding and retrieving Word documents, setting page numbering, and searching documents.
- [Word Tables](../../../../menus/categories/programming/ni-report/wordtab-mnu.html) Use the Word Tables VIs to edit and format tables in Microsoft Word reports.
- [Word Graphs and Pictures](../../../../menus/categories/programming/ni-report/wordpict-mnu.html) Use the Word Graphs and Pictures VIs to edit and format graphs and images in Microsoft Word reports.
- [Word Advanced](../../../../menus/categories/programming/ni-report/wordadv-mnu.html) Use Word Advanced VIs to perform complex tasks in Microsoft Word reports.

Parent topic:

Report Generation VIs

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/wordadv-mnu.html language=enus -->
## TOPIC 00015: Word Advanced

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/wordadv-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/wordadv-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Word Advanced VIs to perform complex tasks in Microsoft Word reports. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Word Advanced

Use Word Advanced VIs to perform complex tasks in Microsoft Word reports.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='wordadv-mnu.png']

- [Word Format Text VI](../../../../vi-lib/addons/office/word-llb/word-format-text-vi.html) Sets the font attributes of a document range specified by the start and end indexes.
- [Word Format Borders (adv) VI](../../../../vi-lib/addons/office/word-llb/word-format-borders-adv-vi.html) Sets border and shading attributes of a Word table or part of a table that the start and end inputs specify.
- [Word Format Paragraph (adv) VI](../../../../vi-lib/addons/office/word-llb/word-format-paragraph-adv-vi.html) Sets the indent and spacing attributes of a document range specified by the start and end indexes.
- [Word Insert Object VI](../../../../vi-lib/addons/office/word-llb/word-insert-object-vi.html) Inserts an object associated with a file into the current document.
- [Word Insert Field VI](../../../../vi-lib/addons/office/word-llb/word-insert-field-vi.html) Inserts a field at the end of the current document or in a document bookmark.
- [Word Set Paper Size VI](../../../../vi-lib/addons/office/word-llb/word-set-paper-size-vi.html) Sets the paper size associated with the current document.
- [Word Send Document VI](../../../../vi-lib/addons/office/word-llb/word-send-document-vi.html) Sends the current document to a list of recipients via email. You can use this VI only if you configure Microsoft Outlook or Outlook Express as the default email application.
- [Word Get ActiveX References VI](../../../../vi-lib/addons/office/word-llb/word-get-activex-references-vi.html) Returns ActiveX references to Microsoft Word.
- [Word Constants](../../../../menus/categories/programming/ni-report/wdconst-mnu.html) Use Word Constants to define specific formatting attributes in Microsoft Word reports.
- [Word Macros](../../../../menus/categories/programming/ni-report/wordmcr-mnu.html) Use the Word Macros VIs to edit and run macros in Microsoft Word reports.

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/wordgen-mnu.html language=enus -->
## TOPIC 00016: Word General

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/wordgen-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/wordgen-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Word General VIs to perform tasks in Microsoft Word reports, such as adding and retrieving Word documents, setting page numbering, and searching documents. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolki

### Word General

Use Word General VIs to perform tasks in Microsoft Word reports, such as adding and retrieving Word documents, setting page numbering, and searching documents.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='wordgen-mnu.png']

- [Word Add New Document VI](../../../../vi-lib/addons/office/word-llb/word-add-new-document-vi.html) Adds a new document to the document collection.
- [Word Get Document VI](../../../../vi-lib/addons/office/word-llb/word-get-document-vi.html) Sets the document defined in the document index parameter as the current document.
- [Word Bring to Front VI](../../../../vi-lib/addons/office/word-llb/word-bring-to-front-vi.html) Changes the state of a Word window to minimized, maximized, or normal.
- [Word Find & Replace VI](../../../../vi-lib/addons/office/word-llb/word-find-replace-vi.html) Finds and replaces a text segment. The data type you wire to the replace with input determines the polymorphic instance to use.
- [Word Set Page Numbering VI](../../../../vi-lib/addons/office/word-llb/word-set-page-numbering-vi.html) Activates the page numbering on the current document.
- [Word Document Properties VI](../../../../vi-lib/addons/office/word-llb/word-document-properties-vi.html) Sets the properties of the current document, such as the title, subject, and author.

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/wordmcr-mnu.html language=enus -->
## TOPIC 00017: Word Macros

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/wordmcr-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/wordmcr-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Word Macros VIs to edit and run macros in Microsoft Word reports. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Word Macros

Use the Word Macros VIs to edit and run macros in Microsoft Word reports.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='wordmcr-mnu.png']

- [Word Add Reference to VBproj VI](../../../../vi-lib/addons/office/word-llb/word-add-reference-to-vbproj-vi.html) Adds an external reference to the Microsoft Visual Basic project associated with the current document. This is the equivalent to selecting Tools>>References in the Microsoft Visual Basic editor.
- [Word Import Module VI](../../../../vi-lib/addons/office/word-llb/word-import-module-vi.html) Imports an external module (*.bas) in the Microsoft Visual Basic project associated with the current document.
- [Word Run Macro VI](../../../../vi-lib/addons/office/word-llb/word-run-macro-vi.html) Runs a macro on the current document.
- [Word Remove Module VI](../../../../vi-lib/addons/office/word-llb/word-remove-module-vi.html) Removes an external module from the Microsoft Visual Basic project associated with the current document.

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/wordpict-mnu.html language=enus -->
## TOPIC 00018: Word Graphs and Pictures

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/wordpict-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/wordpict-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Word Graphs and Pictures VIs to edit and format graphs and images in Microsoft Word reports. If you create a graph that includes more than 3,999 points per plot, Microsoft Office causes an error to occur. The VIs on this palette can return general LabVIEW error codes, specific report generat

### Word Graphs and Pictures

Use the Word Graphs and Pictures VIs to edit and format graphs and images in Microsoft Word reports.

Note

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='wordpict-mnu.png']

- [Word Insert Graph VI](../../../../vi-lib/addons/office/word-llb/word-insert-graph-vi.html) Inserts a new graph into the current document.
- [Word Update Graph VI](../../../../vi-lib/addons/office/word-llb/word-update-graph-vi.html) Updates the data of an existing graph.
- [Word Set Graph Colors VI](../../../../vi-lib/addons/office/word-llb/word-set-graph-colors-vi.html) Sets the color attributes, marker style, and plot weight of an existing graph.
- [Word Set Graph Font VI](../../../../vi-lib/addons/office/word-llb/word-set-graph-font-vi.html) Sets the title and font attributes of the graph axis.
- [Word Set Graph Scale VI](../../../../vi-lib/addons/office/word-llb/word-set-graph-scale-vi.html) Sets the scale parameters of the x- and y-axes. The VI also sets the gridlines parameters of the graph.
- [Word Quit Graph VI](../../../../vi-lib/addons/office/word-llb/word-quit-graph-vi.html) Closes all ActiveX references related to a graph. Use this VI after you insert, update, or format a graph using Word.
- [Word Format Picture VI](../../../../vi-lib/addons/office/word-llb/word-format-picture-vi.html) Formats the image specified by picture index . You can resize the image or modify its color type .

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=menus/categories/programming/ni-report/wordtab-mnu.html language=enus -->
## TOPIC 00019: Word Tables

- bundle_id: `lvrgt-api-ref`
- source_path: `menus/categories/programming/ni-report/wordtab-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/menus/categories/programming/ni-report/wordtab-mnu.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Word Tables VIs to edit and format tables in Microsoft Word reports. Word tables support a maximum of 63 columns. The VIs on this palette can return general LabVIEW error codes, specific report generation error codes, or specific Report Generation Toolkit error codes. icon

### Word Tables

Use the Word Tables VIs to edit and format tables in Microsoft Word reports.

Note

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes), [specific report generation error codes](/csh?context=lvcore_lverror_report_gen_error_codes), or [specific Report Generation Toolkit error codes](../../../../errors/error-codes.html).

[IMAGE alt='icon' src='wordtab-mnu.png']

- [Word Format Cell VI](../../../../vi-lib/addons/office/word-llb/word-format-cell-vi.html) Formats the cells specified by the start and end clusters.
- [Word Edit Cell VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-vi.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.
- [Word Set Table Dimensions VI](../../../../vi-lib/addons/office/word-llb/word-set-table-dimensions-vi.html) Sets the column width, the row height, and the left indentation of any table in the document.
- [Word Table Borders and Shading VI](../../../../vi-lib/addons/office/word-llb/word-table-borders-and-shading-vi.html) Sets the border and shading parameters of the cells specified by the start and end clusters.
- [Word Insert Row-Column-Cell VI](../../../../vi-lib/addons/office/word-llb/word-insert-row-column-cell-vi.html) Inserts a row, a column, or a cell into an existing table.
- [Word Merge Cells VI](../../../../vi-lib/addons/office/word-llb/word-merge-cells-vi.html) Merges the cells specified by the start and end clusters into one cell.
- [Word Table Alignment VI](../../../../vi-lib/addons/office/word-llb/word-table-alignment-vi.html) Sets the horizontal and vertical alignment of the cells specified by the start and end controls.

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=rgt_intro.html language=enus -->
## TOPIC 00020: LabVIEW Report Generation Toolkit Programming Reference Manual

- bundle_id: `lvrgt-api-ref`
- source_path: `rgt_intro.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/rgt_intro.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Report Generation Toolkit LabVIEW Release Notes Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.To comment on National Instruments documentation, refer to the National Instruments website.

### LabVIEW Report Generation Toolkit Programming Reference Manual

The LabVIEW Report Generation Toolkit

[LabVIEW Release Notes](https://www.ni.com/en-us/support/documentation/release-notes/product.labview.html) 
Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.

To comment on National Instruments documentation, refer to the National Instruments website.

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-add-reference-to-vbproj-vi.html language=enus -->
## TOPIC 00021: Excel Add Reference to VBproj VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-add-reference-to-vbproj-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-add-reference-to-vbproj-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a reference to a type library in the Microsoft Visual Basic project associated with the current workbook. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW cl

### Excel Add Reference to VBproj VI

Adds a reference to a type library in the Microsoft Visual Basic project associated with the current workbook.

[IMAGE alt='icon' src='excel-add-reference-to-vbproj-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. reference path — reference path is the path of the type library to add to the Microsoft Visual Basic project associated with the report. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-add-worksheet-vi.html language=enus -->
## TOPIC 00022: Excel Add Worksheet VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-add-worksheet-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-add-worksheet-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new worksheet to the worksheet collection. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cerrcodeclst.png error in (no error) error in des

### Excel Add Worksheet VI

Adds a new worksheet to the worksheet collection.

[IMAGE alt='icon' src='excel-add-worksheet-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-bring-to-front-vi.html language=enus -->
## TOPIC 00023: Excel Bring to Front VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-bring-to-front-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-bring-to-front-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the state of a Microsoft Excel window to minimized, maximized, or normal. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cenum.png window

### Excel Bring to Front VI

Changes the state of a Microsoft Excel window to minimized, maximized, or normal.

[IMAGE alt='icon' src='excel-bring-to-front-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. window state (maximized) — window state sets the state of the Excel window. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-easy-graph-vi.html language=enus -->
## TOPIC 00024: Excel Easy Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-easy-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-easy-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a graph into a Microsoft Excel report. icon Inputs/Outputs cstr.png worksheet ("") worksheet specifies the name of the worksheet where the VI inserts the graph. Microsoft Excel uses default names such as Sheet1, Sheet2, and Sheet3. You can use the Excel Rename Worksheet VI to customize works

### Excel Easy Graph VI

Inserts a graph into a Microsoft Excel report.

[IMAGE alt='icon' src='excel-easy-graph-vi.png']

#### Inputs/Outputs

| worksheet ("") — worksheet specifies the name of the worksheet where the VI inserts the graph. Microsoft Excel uses default names such as Sheet1, Sheet2, and Sheet3. You can use the Excel Rename Worksheet VI to customize worksheet names. If you do not specify a name, the VI inserts the graph in the current worksheet. graph title ("") — graph title contains the title of the graph. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. graph type (col clustered) — graph type sets the type of graph the VI creates. The default is a column graph. You can select one of 65 types of graphs, including XY (scatter), line, bar, three-dimensional surface, pie, and area graphs. start (0, 0) — start specifies the row and column indexes of the cell where the VI inserts the graph. row — row represents the row index. column — column represents the column index. data — data contains the data written into the graph. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies a named range from which the VI inserts the graph. The top left corner of the graph appears in the top left corner of the named range. row headers — row headers contains the row headings. Leave this parameter unwired if you want to create an XY graph. column headers — column headers contains the column headings. Leave this parameter unwired if you want to create an XY graph. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-easy-table-num-vi.html language=enus -->
## TOPIC 00025: Excel Easy Table (num) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-easy-table-num-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-easy-table-num-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts and formats a table into a Microsoft Excel report. The data type you wire to the text data input determines the polymorphic instance to use. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. ccclst.png font fon

### Excel Easy Table (num) VI

Inserts and formats a table into a Microsoft Excel report. The data type you wire to the **text data** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-easy-table-num-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. font — font sets the font attributes that the VI uses when formatting. font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. iteration — Iteration specifies the loop iteration count if you are adding data to an Excel worksheet within a loop. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. auto format (none) — auto format sets the table format using Excel preset table styles. The default is no formatting. start (0, 0) — start represents the position of the top left corner of the range of cells in which the table appears. row — row represents the row index. column — column represents the column index. text data — text data contains the data for the table. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name specifies a named range from which the VI performs the insertion. row headers — row headers contains the row headings. column headers — column headers contains the column headings. report out — report out is a reference to the report whose appearance, data, and printing you want to control. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. next cell bottom-left — next cell bottom-left returns the position of the cell located next to the bottom left corner of the range that the start and end clusters define. row — row represents the row index of the cell. column — column represents the column index of the cell. next cell top-right — next cell top-right returns the position of the cell located next to the top right corner of the range that the start and end clusters define. row — row represents the row index of the cell. column — column represents the column index of the cell. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| row — row represents the row index. column — column represents the column index. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |

Parent topic:

Excel Easy Table VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-easy-table-str-vi.html language=enus -->
## TOPIC 00026: Excel Easy Table (str) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-easy-table-str-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-easy-table-str-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts and formats a table into a Microsoft Excel report. The data type you wire to the text data input determines the polymorphic instance to use. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. ccclst.png font fon

### Excel Easy Table (str) VI

Inserts and formats a table into a Microsoft Excel report. The data type you wire to the **text data** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-easy-table-str-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. font — font sets the font attributes that the VI uses when formatting. font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. iteration — Iteration specifies the loop iteration count if you are adding data to an Excel worksheet within a loop. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. auto format (none) — auto format sets the table format using Excel preset table styles. The default is no formatting. start (0, 0) — start represents the position of the top left corner of the range of cells in which the table appears. row — row represents the row index. column — column represents the column index. text data — text data contains the data for the table. Note LabVIEW limits each element of the text data array to 912 characters. If an element exceeds 912 characters, LabVIEW returns an error. Refer to the KnowledgeBase for more information about a workaround for this limitation. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name specifies a named range from which the VI performs the insertion. row headers — row headers contains the row headings. column headers — column headers contains the column headings. report out — report out is a reference to the report whose appearance, data, and printing you want to control. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. next cell bottom-left — next cell bottom-left returns the position of the cell located next to the bottom left corner of the range that the start and end clusters define. row — row represents the row index of the cell. column — column represents the column index of the cell. next cell top-right — next cell top-right returns the position of the cell located next to the top right corner of the range that the start and end clusters define. row — row represents the row index of the cell. column — column represents the column index of the cell. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| row — row represents the row index. column — column represents the column index. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |

Parent topic:

Excel Easy Table VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-easy-table-vi.html language=enus -->
## TOPIC 00027: Excel Easy Table VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-easy-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-easy-table-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts and formats a table into a Microsoft Excel report. The data type you wire to the text data input determines the polymorphic instance to use. icon

### Excel Easy Table VI

Inserts and formats a table into a Microsoft Excel report. The data type you wire to the **text data** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-easy-table-vi.png']

- [Excel Easy Table (str) VI](../../../../vi-lib/addons/office/excel-llb/excel-easy-table-str-vi.html) Inserts and formats a table into a Microsoft Excel report. The data type you wire to the text data input determines the polymorphic instance to use.
- [Excel Easy Table (num) VI](../../../../vi-lib/addons/office/excel-llb/excel-easy-table-num-vi.html) Inserts and formats a table into a Microsoft Excel report. The data type you wire to the text data input determines the polymorphic instance to use.

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-easy-text-vi.html language=enus -->
## TOPIC 00028: Excel Easy Text VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-easy-text-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-easy-text-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts text into a Microsoft Excel report. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. ccclst.png font font sets the font attributes that the VI uses when

### Excel Easy Text VI

Inserts text into a Microsoft Excel report.

[IMAGE alt='icon' src='excel-easy-text-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. font — font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. border? (F) — border? determines whether a border encloses the text. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. text — text contains the text to insert into the worksheet. start (-1, -1) — start represents the position of the top left corner of the range of cells that the VI merges before inserting the text. row — row represents the row index of the cell. column — column represents the column index of the cell. end (-1, -1) — end represents the position of the bottom right corner of the range of cells that the VI merges before inserting the text. row — row represents the row index of the cell. column — column represents the column index of the cell. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name describes the named range from which the VI retrieves data. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. next cell bottom-left — next cell bottom-left returns the position of the cell located next to the bottom left corner of the range that the start and end clusters define. You can insert the output values in the start input of the Excel Easy Text, Excel Easy Table, or Excel Easy Graph VIs to append new elements below. row — row represents the row index of the cell. column — column represents the column index of the cell. next cell top-right — next cell top-right returns the position of the cell located next to the top right corner of the range that the start and end clusters define. You can insert the output values in the start input of the Excel Easy Text, Excel Easy Table, or Excel Easy Graph VIs to append new elements on the left side. row — row represents the row index of the cell. column — column represents the column index of the cell. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |
| row — row represents the row index of the cell. column — column represents the column index of the cell. |

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-easy-title-vi.html language=enus -->
## TOPIC 00029: Excel Easy Title VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-easy-title-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-easy-title-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a title to a Microsoft Excel report. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. cNI__reportlvclass.png report in report in is a reference to the repo

### Excel Easy Title VI

Adds a title to a Microsoft Excel report.

[IMAGE alt='icon' src='excel-easy-title-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. title — title contains the text you want to use as the report title. start (0, 0) — start represents the position of the cell where the VI places the title. The default is the top left cell in the current worksheet. row — row represents the row index. column — column represents the column index. font — font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies a named range from which the VI performs the insertion. If the named range covers multiple cells, the insertion appears in the top left corner of the range. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the row index. column — column represents the column index. |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |

Parent topic:

Excel Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-find-and-replace-num-vi.html language=enus -->
## TOPIC 00030: Excel Find and Replace (num) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-find-and-replace-num-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-find-and-replace-num-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the occurrences of searched string and replaces them with a new string or numeric value. The data type you wire to the replacement input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and

### Excel Find and Replace (num) VI

Searches the occurrences of **searched string** and replaces them with a new string or numeric value. The data type you wire to the **replacement** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-find-and-replace-num-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. searched string — searched string describes the string to search for and replace. replacement — replacement is the number that replaces instances of searched string. format string (%.3f) — format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string when you wire numeric data to the replacement input. error in (no error) — error in describes error conditions that occur before this VI or function runs. — report out is a reference to the report whose appearance, data, and printing you want to control. found? — found? returns TRUE if the VI finds at least one occurrence of the searched string. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

Excel Find and Replace VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-find-and-replace-str-vi.html language=enus -->
## TOPIC 00031: Excel Find and Replace (str) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-find-and-replace-str-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-find-and-replace-str-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the occurrences of searched string and replaces them with a new string or numeric value. The data type you wire to the replacement input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and

### Excel Find and Replace (str) VI

Searches the occurrences of **searched string** and replaces them with a new string or numeric value. The data type you wire to the **replacement** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-find-and-replace-str-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. searched string — searched string describes the string to search for and replace. replacement — replacement is the string that replaces instances of searched string. error in (no error) — error in describes error conditions that occur before this VI or function runs. — report out is a reference to the report whose appearance, data, and printing you want to control. found? — found? returns TRUE if the VI finds at least one occurrence of the searched string. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

Excel Find and Replace VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-find-and-replace-vi.html language=enus -->
## TOPIC 00032: Excel Find and Replace VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-find-and-replace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-find-and-replace-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the occurrences of searched string and replaces them with a new string or numeric value. The data type you wire to the replacement input determines the polymorphic instance to use. icon

### Excel Find and Replace VI

Searches the occurrences of **searched string** and replaces them with a new string or numeric value. The data type you wire to the **replacement** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-find-and-replace-vi.png']

- [Excel Find and Replace (num) VI](../../../../vi-lib/addons/office/excel-llb/excel-find-and-replace-num-vi.html) Searches the occurrences of searched string and replaces them with a new string or numeric value. The data type you wire to the replacement input determines the polymorphic instance to use.
- [Excel Find and Replace (str) VI](../../../../vi-lib/addons/office/excel-llb/excel-find-and-replace-str-vi.html) Searches the occurrences of searched string and replaces them with a new string or numeric value. The data type you wire to the replacement input determines the polymorphic instance to use.

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-format-image-vi.html language=enus -->
## TOPIC 00033: Excel Format Image VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-format-image-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-format-image-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Formats the image specified by picture index. You can resize the image or modify its color type. icon Inputs/Outputs cu16.png measurement system (US) measurement system determines the system that the VI uses to measure size. csgl.png scale factor (1) scale factor sets the scaling factor the VI uses

### Excel Format Image VI

Formats the image specified by **picture index**. You can resize the image or modify its **color type**.

[IMAGE alt='icon' src='excel-format-image-vi.png']

#### Inputs/Outputs

| measurement system (US) — measurement system determines the system that the VI uses to measure size. scale factor (1) — scale factor sets the scaling factor the VI uses to resize the picture. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. picture index (-1) — picture index specifies the index of the image to format. The default is -1, in which the VI modifies the last image in the current document or worksheet. Note Graphs, images, ActiveX controls, and OLE objects form a collection for each document or worksheet. Each object has an index value based on the order of the objects. Index values begin at 0. For example, if you insert two images into a document before you insert a graph, the index value for the graph is 2. height (-1) — height sets the height of the image in the units of measurement system. The default is –1, which does not change the image height. width (-1) — width sets the width of the picture in the units of measurement system. The default is –1, which does not change the image width. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. color type (auto) — color type sets the type of color transformation the VI applies to the image, such as grayscale or black-and-white. The default setting is automatic. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-activex-references-vi.html language=enus -->
## TOPIC 00034: Excel Get ActiveX References VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-activex-references-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-activex-references-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns ActiveX references to Microsoft Excel. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cerrcodeclst.png error in (no error) error in descri

### Excel Get ActiveX References VI

Returns ActiveX references to Microsoft Excel.

[IMAGE alt='icon' src='excel-get-activex-references-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Excel._Application — Excel._Application is a reference to the application Microsoft Excel. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. Excel._Workbook — Excel._Workbook is a reference to the active workbook. Excel._Worksheet — Excel._Worksheet is a reference to the active worksheet. Excel.Sheets — Excel.Sheets is a reference to all the worksheets in the active workbook. error out — error out contains error information. This output provides standard error out functionality. Excel.Shapes — Excel.Shapes is a reference to graphics in the active worksheet. |
| --- |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi-2.html language=enus -->
## TOPIC 00035: Excel Get Data ([dbl]) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi-2.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi-2.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to ge

### Excel Get Data ([dbl]) VI

Retrieves data from the current worksheet. The data type you wire to the **data type** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-get-data-dbl-vi-2.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. data type — data type sets the type of data the VI returns. start (-1, -1) — start defines the beginning of the range of cells returned. row — row represents the row index. column — column represents the column index. end (-1, -1) — end defines the end of the range of cells returned. row — row represents the row index. column — column represents the column index. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name describes the named range from which the VI retrieves data. — report out is a reference to the report whose appearance, data, and printing you want to control. data — data contains the data from the worksheet. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |
| row — row represents the row index. column — column represents the column index. |

#### Excel Get Data Details

To return a numeric value, use the **start** cluster or the **name** input to specify the cell from which you want to return the value. To return an array, wire both the **start** and **end** clusters or the **name** input to specify the range from which you want to return the array. If the **start** and **end** clusters remain unwired, the VI returns the entire used section of the current worksheet.

Note

data type

Parent topic:

Excel Get Data VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi.html language=enus -->
## TOPIC 00036: Excel Get Data (dbl) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to ge

### Excel Get Data (dbl) VI

Retrieves data from the current worksheet. The data type you wire to the **data type** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-get-data-dbl-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. data type — data type sets the type of data the VI returns. start (0, 0) — start defines the beginning of the range of cells the VI returns. start row — start row represents the row index. start column — start column represents the column index. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name describes the named range from which the VI retrieves data. — report out is a reference to the report whose appearance, data, and printing you want to control. data — data contains the data from the worksheet. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| start row — start row represents the row index. start column — start column represents the column index. |

#### Excel Get Data Details

To return a numeric value, use the **start** cluster or the **name** input to specify the cell from which you want to return the value. To return an array, wire both the **start** and **end** clusters or the **name** input to specify the range from which you want to return the array. If the **start** and **end** clusters remain unwired, the VI returns the entire used section of the current worksheet.

Note

data type

Parent topic:

Excel Get Data VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-data-i32-vi-2.html language=enus -->
## TOPIC 00037: Excel Get Data ([i32]) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-data-i32-vi-2.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-data-i32-vi-2.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to ge

### Excel Get Data ([i32]) VI

Retrieves data from the current worksheet. The data type you wire to the **data type** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-get-data-i32-vi-2.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. data type — data type sets the type of data the VI returns. start (-1, -1) — start defines the beginning of the range of cells returned. row — row represents the row index. column — column represents the column index. end (-1, -1) — end defines the end of the range of cells returned. row — row represents the row index. column — column represents the column index. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name describes the named range from which the VI retrieves data. — report out is a reference to the report whose appearance, data, and printing you want to control. data — data represents the data the worksheet returns. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |
| row — row represents the row index. column — column represents the column index. |

#### Excel Get Data Details

To return a numeric value, use the **start** cluster or the **name** input to specify the cell from which you want to return the value. To return an array, wire both the **start** and **end** clusters or the **name** input to specify the range from which you want to return the array. If the **start** and **end** clusters remain unwired, the VI returns the entire used section of the current worksheet.

Note

data type

Parent topic:

Excel Get Data VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-data-i32-vi.html language=enus -->
## TOPIC 00038: Excel Get Data (i32) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-data-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-data-i32-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to ge

### Excel Get Data (i32) VI

Retrieves data from the current worksheet. The data type you wire to the **data type** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-get-data-i32-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. data type — data type sets the type of data the VI returns. start (0, 0) — start defines the beginning of the range of cells the VI returns. start row — start row represents the row index. start column — start column represents the column index. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name describes the named range from which the VI retrieves data. — report out is a reference to the report whose appearance, data, and printing you want to control. data — data contains the data from the worksheet. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| start row — start row represents the row index. start column — start column represents the column index. |

#### Excel Get Data Details

To return a numeric value, use the **start** cluster or the **name** input to specify the cell from which you want to return the value. To return an array, wire both the **start** and **end** clusters or the **name** input to specify the range from which you want to return the array. If the **start** and **end** clusters remain unwired, the VI returns the entire used section of the current worksheet.

Note

data type

Parent topic:

Excel Get Data VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-data-str-vi-2.html language=enus -->
## TOPIC 00039: Excel Get Data ([str]) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-data-str-vi-2.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-data-str-vi-2.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to ge

### Excel Get Data ([str]) VI

Retrieves data from the current worksheet. The data type you wire to the **data type** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-get-data-str-vi-2.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. data type — data type sets the type of data the VI returns. start (-1, -1) — start defines the beginning of the range of cells returned. row — row represents the row index. column — column represents the column index. end (-1, -1) — end defines the end of the range of cells returned. row — row represents the row index. column — column represents the column index. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name describes the named range from which the VI retrieves data. — report out is a reference to the report whose appearance, data, and printing you want to control. data — data contains the data from the worksheet. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |
| row — row represents the row index. column — column represents the column index. |

#### Excel Get Data Details

To return a numeric value, use the **start** cluster or the **name** input to specify the cell from which you want to return the value. To return an array, wire both the **start** and **end** clusters or the **name** input to specify the range from which you want to return the array. If the **start** and **end** clusters remain unwired, the VI returns the entire used section of the current worksheet.

Note

data type

Parent topic:

Excel Get Data VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-data-str-vi.html language=enus -->
## TOPIC 00040: Excel Get Data (str) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-data-str-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-data-str-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to ge

### Excel Get Data (str) VI

Retrieves data from the current worksheet. The data type you wire to the **data type** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-get-data-str-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. data type — data type sets the type of data the VI returns. start (0, 0) — start defines the beginning of the range of cells the VI returns. start row — start row represents the row index. start column — start column represents the column index. error in (no error) — error in describes error conditions that occur before this VI or function runs. name ("") — name describes the named range from which the VI retrieves data. — report out is a reference to the report whose appearance, data, and printing you want to control. data — data contains the data from the worksheet. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| start row — start row represents the row index. start column — start column represents the column index. |

#### Excel Get Data Details

To return a numeric value, use the **start** cluster or the **name** input to specify the cell from which you want to return the value. To return an array, wire both the **start** and **end** clusters or the **name** input to specify the range from which you want to return the array. If the **start** and **end** clusters remain unwired, the VI returns the entire used section of the current worksheet.

Note

data type

Parent topic:

Excel Get Data VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-data-vi.html language=enus -->
## TOPIC 00041: Excel Get Data VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-data-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use. icon Excel Get Data Details To return a numeric value, use the start cluster or the name input to specify the cell from which you want to return the value. To return a

### Excel Get Data VI

Retrieves data from the current worksheet. The data type you wire to the **data type** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='excel-get-data-vi.png']

#### Excel Get Data Details

To return a numeric value, use the **start** cluster or the **name** input to specify the cell from which you want to return the value. To return an array, wire both the **start** and **end** clusters or the **name** input to specify the range from which you want to return the array. If the **start** and **end** clusters remain unwired, the VI returns the entire used section of the current worksheet.

Note

data type

- [Excel Get Data (str) VI](../../../../vi-lib/addons/office/excel-llb/excel-get-data-str-vi.html) Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use.
- [Excel Get Data (dbl) VI](../../../../vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi.html) Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use.
- [Excel Get Data ([str]) VI](../../../../vi-lib/addons/office/excel-llb/excel-get-data-str-vi-2.html) Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use.
- [Excel Get Data ([dbl]) VI](../../../../vi-lib/addons/office/excel-llb/excel-get-data-dbl-vi-2.html) Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use.
- [Excel Get Data (i32) VI](../../../../vi-lib/addons/office/excel-llb/excel-get-data-i32-vi.html) Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use.
- [Excel Get Data ([i32]) VI](../../../../vi-lib/addons/office/excel-llb/excel-get-data-i32-vi-2.html) Retrieves data from the current worksheet. The data type you wire to the data type input determines the polymorphic instance to use.

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-excel-location-vi.html language=enus -->
## TOPIC 00042: Excel Get Excel Location VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-excel-location-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-excel-location-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the row and column indexes of a cell that you identify by Excel syntax. icon Inputs/Outputs cstr.png cell's name cell's name represents the name of the cell in Excel syntax, such as G6. ii32.png row row represents the row index of the cell. ii32.png column column represents the column index

### Excel Get Excel Location VI

Returns the row and column indexes of a cell that you identify by Excel syntax.

[IMAGE alt='icon' src='excel-get-excel-location-vi.png']

#### Inputs/Outputs

| cell's name — cell's name represents the name of the cell in Excel syntax, such as G6. row — row represents the row index of the cell. column — column represents the column index of the cell. |
| --- |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-last-row-vi.html language=enus -->
## TOPIC 00043: Excel Get Last Row VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-last-row-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-last-row-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the coordinates of the last row in an Excel worksheet. Use the MS Office parameters input to append the contents of the row to a report. icon Inputs/Outputs cNI__reportlvclass.png report in report in is a reference to the report whose appearance, data, and printing you want to control. Use

### Excel Get Last Row VI

Retrieves the coordinates of the last row in an Excel worksheet. Use the **MS Office parameters** input to append the contents of the row to a report.

[IMAGE alt='icon' src='excel-get-last-row-vi.png']

#### Inputs/Outputs

| report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. offset — offset specifies the number of rows by which you want to offset the output in MS Office parameters. The default is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MS Office parameters — MS Office parameters specifies the point in a Microsoft Word or Excel report where you want an insertion to occur. The VI ignores this input for HTML and standard reports. You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the report type to Word but do not specify a bookmark, the insertion occurs at the end of the document. position (excel) — position contains the row and column coordinates of the point in an Excel worksheet from which the insertion occurs. Row and column values in Excel are zero-based, so the row and column coordinates of (0,0) correspond to cell A1. row — row represents the row index. column — column represents the column index. name (excel) — name contains the name of the cell in a Microsoft Excel worksheet from which the insertion occurs. bookmark (word) — bookmark contains the name of the bookmark in a Word document from which the insertion occurs. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. MS Office parameters out — MS Office parameters out contains the MS Office parameters input values and the contents of the row. position (excel) — position (Excel) contains the row and column coordinates of the point in an Excel worksheet from which the insertion occurred. Row and column values in Excel are zero-based, so the row and column coordinates of (0,0) correspond to cell A1. row — row returns the row index. column — column returns the column index. name (excel) — name (Excel) contains the name of the cell in an Excel worksheet from which the insertion occurred. bookmark (word) — bookmark (Word) contains the name of the bookmark in a Word document from which the insertion occurred. |
| --- |
| position (excel) — position contains the row and column coordinates of the point in an Excel worksheet from which the insertion occurs. Row and column values in Excel are zero-based, so the row and column coordinates of (0,0) correspond to cell A1. row — row represents the row index. column — column represents the column index. name (excel) — name contains the name of the cell in a Microsoft Excel worksheet from which the insertion occurs. bookmark (word) — bookmark contains the name of the bookmark in a Word document from which the insertion occurs. |
| row — row represents the row index. column — column represents the column index. |
| position (excel) — position (Excel) contains the row and column coordinates of the point in an Excel worksheet from which the insertion occurred. Row and column values in Excel are zero-based, so the row and column coordinates of (0,0) correspond to cell A1. row — row returns the row index. column — column returns the column index. name (excel) — name (Excel) contains the name of the cell in an Excel worksheet from which the insertion occurred. bookmark (word) — bookmark (Word) contains the name of the bookmark in a Word document from which the insertion occurred. |
| row — row returns the row index. column — column returns the column index. |

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-get-worksheet-vi.html language=enus -->
## TOPIC 00044: Excel Get Worksheet VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-get-worksheet-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-get-worksheet-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Makes a specified worksheet the current worksheet. Use the worksheet index or name parameter to specify the worksheet you want to set as current. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Re

### Excel Get Worksheet VI

Makes a specified worksheet the current worksheet. Use the **worksheet index** or **name** parameter to specify the worksheet you want to set as current.

[IMAGE alt='icon' src='excel-get-worksheet-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. worksheet index (0) — worksheet index represents the index of the new current worksheet. The worksheet index numbers start from zero, the default. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name represents the name of the new current worksheet. If this parameter is empty, the VI uses the worksheet index input. Microsoft Excel uses default names such as Sheet1, Sheet2, and Sheet3. You can use the Excel Rename Worksheet VI to customize worksheet names. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-import-module-vi.html language=enus -->
## TOPIC 00045: Excel Import Module VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-import-module-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-import-module-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports an external module (*.bas) in the Microsoft Visual Basic project associated with the current workbook. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW cl

### Excel Import Module VI

Imports an external module (*.bas) in the Microsoft Visual Basic project associated with the current workbook.

[IMAGE alt='icon' src='excel-import-module-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. module path — module path is the path of the external Microsoft Visual Basic module to import into the Visual Basic project associated with the report. If you do not wire this input, the VI imports the code specified in module code. module code ("") — module code contains the source code of the module to import into the Microsoft Visual Basic project. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. module reference — module reference provides a reference to the imported module. You can use this output value with the Excel Remove Module VI to remove the module after the macro executes. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-insert-cells-vi.html language=enus -->
## TOPIC 00046: Excel Insert Cells VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-insert-cells-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-insert-cells-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a new cell, row, or column into the current worksheet from a position that the row and column indexes specify. If you use the name parameter to specify a named range, the VI inserts the object from the top left cell of the range. The position of the named range from which the VI performs the

### Excel Insert Cells VI

Inserts a new cell, row, or column into the current worksheet from a position that the **row** and **column** indexes specify.

If you use the **name** parameter to specify a named range, the VI inserts the object from the top left cell of the range.

Note

[IMAGE alt='icon' src='excel-insert-cells-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. mode (entire row) — mode sets the insertion mode. start (0, 0) — start specifies the position of the cell from which the VI performs the insertion. row — row represents the row index. column — column represents the column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies a named range from which the VI performs the insertion. If the named range covers multiple cells, the insertion appears in the top left corner of the range. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-insert-formula-vi.html language=enus -->
## TOPIC 00047: Excel Insert Formula VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-insert-formula-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-insert-formula-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a formula in the cell defined by the start cluster. If you use the name parameter to specify a named range, the VI inserts the formula from the top left cell of the range. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing y

### Excel Insert Formula VI

Inserts a formula in the cell defined by the **start** cluster. If you use the **name** parameter to specify a named range, the VI inserts the formula from the top left cell of the range.

[IMAGE alt='icon' src='excel-insert-formula-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. formula — formula specifies the formula to insert in the specified cell. start (0, 0) — start contains the row and column indexes of the cell in which the VI inserts the formula. row — row represents the row index. column — column represents the column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies a named range from which the VI performs the insertion. If the named range covers multiple cells, the insertion appears in the top left corner of the range. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-insert-graph-vi.html language=enus -->
## TOPIC 00048: Excel Insert Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-insert-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-insert-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a new graph into the current worksheet and fills the graph with numeric data. icon Inputs/Outputs cbool.png has legend? (F) has legend? shows or hides the graph legend. The default is FALSE, in which the VI does not display the graph legend. cu16.png measurement system (US) measurement syste

### Excel Insert Graph VI

Inserts a new graph into the current worksheet and fills the graph with numeric data.

[IMAGE alt='icon' src='excel-insert-graph-vi.png']

#### Inputs/Outputs

| has legend? (F) — has legend? shows or hides the graph legend. The default is FALSE, in which the VI does not display the graph legend. measurement system (US) — measurement system determines the system that the VI uses to measure size. graph type (col clustered) — graph type sets the type of graph the VI creates. The default is a column graph. You can select one of 65 types of graphs, including XY (scatter), line, bar, three-dimensional surface, pie, and area graphs. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. column headers — column headers specifies the text of the column labels on the graph. Leave this parameter unwired if you want to create an XY graph. row headers — row headers specifies the text of the row labels on the graph. Leave this parameter unwired if you want to create an XY graph. data — data contains numerical data that the VI uses to create the graph. Microsoft Office returns an error if you plot more than 3,999 points per row or column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies a named range from which the VI inserts the graph. The top left corner of the graph appears in the top left corner of the named range. graph title ("") — graph title contains the title of the graph. position/size — position/size sets the position and size of the graph into the current worksheet. The position represents the row and column indexes of the cell from which the VI inserts the graph. left — left is the column index of the cell from which the VI inserts the graph. top — top is the row index of the cell from which the VI inserts the graph. height — height is the graph height in the units of the measurement system. width — width is the graph width in the units of the measurement system. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| left — left is the column index of the cell from which the VI inserts the graph. top — top is the row index of the cell from which the VI inserts the graph. height — height is the graph height in the units of the measurement system. width — width is the graph width in the units of the measurement system. |

Parent topic:

Excel Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-insert-object-vi.html language=enus -->
## TOPIC 00049: Excel Insert Object VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-insert-object-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-insert-object-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts an object associated with a file in the cell specified by the position/size cluster. icon Inputs/Outputs cu16.png measurement system (US) measurement system determines the system that the VI uses to measure size. cNI__reportlvclass.png report in is a reference to the report whose appearance,

### Excel Insert Object VI

Inserts an object associated with a file in the cell specified by the **position/size** cluster.

[IMAGE alt='icon' src='excel-insert-object-vi.png']

#### Inputs/Outputs

| measurement system (US) — measurement system determines the system that the VI uses to measure size. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. file path — file path is the path of the object to insert into the document. position/size — position/size sets the position and size of the object into the current worksheet. The position represents the row and column indexes of the cell from which the object is inserted. The VI uses size if the object is embedded into the document. row — row is the row index of the cell from which the VI inserts the object. column — column is the column index of the cell from which the VI inserts the object. width — width is the object width in the units of the measurement system. height — height is the object height in the units of measurement system. linked to file? (F) — linked to file? specifies whether the VI links the object to the original file associated with it. The default is FALSE, which links the object to an independent copy of the file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies a named range from which the VI performs the insertion. If the named range covers multiple cells, the insertion appears in the top left corner of the range. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row is the row index of the cell from which the VI inserts the object. column — column is the column index of the cell from which the VI inserts the object. width — width is the object width in the units of the measurement system. height — height is the object height in the units of measurement system. |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-merge-cells-vi.html language=enus -->
## TOPIC 00050: Excel Merge Cells VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-merge-cells-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-merge-cells-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges the range of cells specified by the start and end clusters. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cnclst.png start (-1, -1) start

### Excel Merge Cells VI

Merges the range of cells specified by the **start** and **end** clusters.

[IMAGE alt='icon' src='excel-merge-cells-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. start (-1, -1) — start sets the beginning of the range of cells to merge together. row — row represents the first row index of the range to merge together. column — column represents the first column index of the range to merge together. end (-1, -1) — end sets the end of the range of cells to merge together. row — row represents the last row index of the range to merge together. column — column represents the last column index of the range to merge together. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies a named range from which the VI performs the merge. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the first row index of the range to merge together. column — column represents the first column index of the range to merge together. |
| row — row represents the last row index of the range to merge together. column — column represents the last column index of the range to merge together. |

Parent topic:

Excel Format

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-quit-graph-vi.html language=enus -->
## TOPIC 00051: Excel Quit Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-quit-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-quit-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes all ActiveX references related to a graph. Use this VI after you insert, update, or format a graph using Excel. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this La

### Excel Quit Graph VI

Closes all ActiveX references related to a graph. Use this VI after you insert, update, or format a graph using Excel.

[IMAGE alt='icon' src='excel-quit-graph-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current worksheet. Note Graphs, images, ActiveX controls, and OLE objects form a collection for each worksheet. Each object has an index value based on the order of the objects in the worksheet. Index values begin at 0. For example, if you insert two images into the worksheet before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-remove-module-vi.html language=enus -->
## TOPIC 00052: Excel Remove Module VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-remove-module-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-remove-module-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes an external module from the Microsoft Visual Basic project associated with the current workbook. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class ob

### Excel Remove Module VI

Removes an external module from the Microsoft Visual Basic project associated with the current workbook.

[IMAGE alt='icon' src='excel-remove-module-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. module reference — module reference provides a reference to the external module to remove from the Microsoft Visual Basic project. You can obtain this reference from the output of the Excel Import Module VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-rename-worksheet-vi.html language=enus -->
## TOPIC 00053: Excel Rename Worksheet VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-rename-worksheet-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-rename-worksheet-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Renames the current worksheet. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cstr.png worksheet name ("") worksheet name specifies the new name f

### Excel Rename Worksheet VI

Renames the current worksheet.

[IMAGE alt='icon' src='excel-rename-worksheet-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. worksheet name ("") — worksheet name specifies the new name for the current worksheet. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-run-macro-vi.html language=enus -->
## TOPIC 00054: Excel Run Macro VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-run-macro-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-run-macro-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs a macro on the current Excel workbook. You must define the macro in the Microsoft Visual Basic project associated with the workbook. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI

### Excel Run Macro VI

Runs a macro on the current Excel workbook. You must define the macro in the Microsoft Visual Basic project associated with the workbook.

[IMAGE alt='icon' src='excel-run-macro-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. macro name — macro name specifies the name of the macro to run from LabVIEW. parameters — parameters contains the input parameters of the macro. You cannot send more than nine parameters. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. return value — return value sets the value returned by the macro. The value is a variant. You must convert the value to LabVIEW data if you want to use the value in LabVIEW. Use the Variant to Data VI from the Communication»ActiveX subpalette to convert the return value to LabVIEW data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-send-workbook-vi.html language=enus -->
## TOPIC 00055: Excel Send Workbook VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-send-workbook-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-send-workbook-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the current workbook to a list of recipients via email. You can use this VI only if you configure Microsoft Outlook or Outlook Express as the default email application. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you wa

### Excel Send Workbook VI

Sends the current workbook to a list of recipients via email. You can use this VI only if you configure Microsoft Outlook or Outlook Express as the default email application.

[IMAGE alt='icon' src='excel-send-workbook-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. recipients — recipients contains the list of email addresses the VI uses to send the report. subject ("") — subject contains the subject line of the message. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-cell-alignment-vi.html language=enus -->
## TOPIC 00056: Excel Set Cell Alignment VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-cell-alignment-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-cell-alignment-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the alignment of the cells specified by the start and end clusters or by a named range. icon Inputs/Outputs ci32.png horizontal alignment (left) horizontal alignment sets the horizontal alignment of text in the specified cells. The default setting aligns text along the left side of the cells. c

### Excel Set Cell Alignment VI

Sets the alignment of the cells specified by the **start** and **end** clusters or by a named range.

[IMAGE alt='icon' src='excel-set-cell-alignment-vi.png']

#### Inputs/Outputs

| horizontal alignment (left) — horizontal alignment sets the horizontal alignment of text in the specified cells. The default setting aligns text along the left side of the cells. vertical alignment (top) — vertical alignment sets the vertical alignment of text in the specified cells. The default setting aligns text to the top of each cell. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. wrap text? (F) — wrap text? must be set to TRUE to wrap text into the cells. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the last row index. column — column represents the last column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies the named range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. |
| row — row represents the last row index. column — column represents the last column index. |

Parent topic:

Excel Format

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-cell-color-and-border-vi.html language=enus -->
## TOPIC 00057: Excel Set Cell Color and Border VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-cell-color-and-border-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-cell-color-and-border-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the borders and background color of the cells specified by the start and end clusters or by a named range. icon Inputs/Outputs ccclst.png outside border outside border sets the outside border parameters of the specified cells. cbool.png on/off on/off displays or hides the border. ci32.png weigh

### Excel Set Cell Color and Border VI

Sets the borders and background color of the cells specified by the **start** and **end** clusters or by a named range.

[IMAGE alt='icon' src='excel-set-cell-color-and-border-vi.png']

#### Inputs/Outputs

| outside border — outside border sets the outside border parameters of the specified cells. on/off — on/off displays or hides the border. weight — weight sets the border thickness. color — color sets the border color. inside border — inside border sets the inside border parameters of the specified cells. on/off — on/off displays or hides the border. weight — weight sets the border thickness. color — color sets the border color. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. background color (w) — background color sets the cell background color. The default is a white background. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the last row index. column — column represents the last column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies the named range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| on/off — on/off displays or hides the border. weight — weight sets the border thickness. color — color sets the border color. |
| on/off — on/off displays or hides the border. weight — weight sets the border thickness. color — color sets the border color. |
| row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. |
| row — row represents the last row index. column — column represents the last column index. |

Parent topic:

Excel Format

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-cell-dimension-vi.html language=enus -->
## TOPIC 00058: Excel Set Cell Dimension VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-cell-dimension-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-cell-dimension-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the dimensions of the cells specified by the start and end clusters or by a named range. icon Inputs/Outputs cdbl.png height (-1) height sets the height of the specified cells in the units of measurement system. cdbl.png width (-1) width sets the width of the specified cells in the units of mea

### Excel Set Cell Dimension VI

Sets the dimensions of the cells specified by the **start** and **end** clusters or by a named range.

[IMAGE alt='icon' src='excel-set-cell-dimension-vi.png']

#### Inputs/Outputs

| height (-1) — height sets the height of the specified cells in the units of measurement system. width (-1) — width sets the width of the specified cells in the units of measurement system. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. measurement system (US) — measurement system determines the system that the VI uses to measure size. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the last row index. column — column represents the last column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies the named range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. |
| row — row represents the last row index. column — column represents the last column index. |

Parent topic:

Excel Format

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-cell-font-vi.html language=enus -->
## TOPIC 00059: Excel Set Cell Font VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-cell-font-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-cell-font-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the font of the cells specified by the start and end clusters or by a named range. icon Inputs/Outputs ci32.png auto format auto format sets the cell format using Excel preset table styles. The default is no formatting. In Excel, select Format»AutoFormat to view examples of Excel table styles.

### Excel Set Cell Font VI

Sets the font of the cells specified by the **start** and **end** clusters or by a named range.

[IMAGE alt='icon' src='excel-set-cell-font-vi.png']

#### Inputs/Outputs

| auto format — auto format sets the cell format using Excel preset table styles. The default is no formatting. In Excel, select Format»AutoFormat to view examples of Excel table styles. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. font — font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the last row index. column — column represents the last column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies the named range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. |
| row — row represents the last row index. column — column represents the last column index. |

Parent topic:

Excel Format

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-cell-format-vi.html language=enus -->
## TOPIC 00060: Excel Set Cell Format VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-cell-format-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-cell-format-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number format of the cells specified by the start and end clusters or by a named range. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cs

### Excel Set Cell Format VI

Sets the number format of the cells specified by the **start** and **end** clusters or by a named range.

[IMAGE alt='icon' src='excel-set-cell-format-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. number format — number format describes the format to apply to the specified cells. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the used section of the worksheet. If start is wired but end is unwired, the VI formats the unique cell specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. row — row represents the last row index. column — column represents the last column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. name ("") — name specifies the named range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the index of the first row of the range to format. column — column represents the index of the first column of the range to format. |
| row — row represents the last row index. column — column represents the last column index. |

Parent topic:

Excel Format

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-excel-location-vi.html language=enus -->
## TOPIC 00061: Excel Set Excel Location VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-excel-location-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-excel-location-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Excel syntax name of a cell that you identify by row and column indexes. icon Inputs/Outputs ci32.png row row represents the row index. ci32.png column column represents the column index. istr.png cell's name cell's name represents the name of the cell in Excel syntax, such as G6.

### Excel Set Excel Location VI

Returns the Excel syntax name of a cell that you identify by row and column indexes.

[IMAGE alt='icon' src='excel-set-excel-location-vi.png']

#### Inputs/Outputs

| row — row represents the row index. column — column represents the column index. cell's name — cell's name represents the name of the cell in Excel syntax, such as G6. |
| --- |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-graph-colors-vi.html language=enus -->
## TOPIC 00062: Excel Set Graph Colors VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-graph-colors-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-graph-colors-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the color attributes, marker style, and plot line weight in an existing graph. By default, the VI applies to the last graph you insert in the current worksheet. Use the graph index input if you want to format a specific graph in the current worksheet. The Excel Set Graph Colors VI only sets the

### Excel Set Graph Colors VI

Sets the color attributes, marker style, and plot line weight in an existing graph.

graph index

Note

[IMAGE alt='icon' src='excel-set-graph-colors-vi.png']

#### Inputs/Outputs

| weight (1) — weight sets the thickness of the plot lines. marker style (none) — marker style specifies the type of markers that appear on the graph plots. The default setting displays no markers on the plot lines. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. graph area color (w) — graph area color sets the background color for the region of the graph that includes the graph title, graph legend, and axis tick labels. The default is white. You can wire a color box constant to this input. plot area color (w) — plot area color sets the background color for the region of the graph that contains the plots. The default is white. You can wire a color box constant to this input. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current worksheet. Note Graphs, images, ActiveX controls, and OLE objects form a collection for each worksheet. Each object has an index value based on the order of the objects in the worksheet. Index values begin at 0. For example, if you insert two images into the worksheet before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. plot colors — plot colors sets the color of the plot lines. You can wire an array of color box constants to this input. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-graph-font-vi.html language=enus -->
## TOPIC 00063: Excel Set Graph Font VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-graph-font-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-graph-font-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the title text and the title font of the x- and y-axes. By default, the VI applies to the last graph you insert in the current worksheet. Use the graph index input to format a specific graph in the worksheet. The Excel Set Graph Font VI only sets the font on graphs you create using the LabVIEW

### Excel Set Graph Font VI

Sets the title text and the title font of the x- and y-axes.

graph index

Note

[IMAGE alt='icon' src='excel-set-graph-font-vi.png']

#### Inputs/Outputs

| number format (general) — number format describes the format to apply to the axis of the graph. Refer to the Microsoft Excel documentation for more information about number formatting. axis font — axis font sets the font attributes of the axis tick labels and legend. font style — font style specifies a specific Microsoft Word style to apply to the text. bold — bold specifies whether the text is in bold. italic — italic specifies whether the text is in italics. underline — underline specifies whether the text is underlined. size — size specifies the point size of the font. color — color specifies the text color. The default is black. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. axis type (xlCategory) — axis type specifies the type of axis to format. The default is xlCategory, which generally represents the X axis. You also can select xlValue, which generally represents the Y axis. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current worksheet. Note Graphs, images, ActiveX controls, and OLE objects form a collection for each worksheet. Each object has an index value based on the order of the objects in the worksheet. Index values begin at 0. For example, if you insert two images into the worksheet before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. title ("") — title contains the axis title. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font style — font style specifies a specific Microsoft Word style to apply to the text. bold — bold specifies whether the text is in bold. italic — italic specifies whether the text is in italics. underline — underline specifies whether the text is underlined. size — size specifies the point size of the font. color — color specifies the text color. The default is black. |

Parent topic:

Excel Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-graph-scale-vi.html language=enus -->
## TOPIC 00064: Excel Set Graph Scale VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-graph-scale-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-graph-scale-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the scale parameters of the x- and y-axes and formats the graph gridlines. By default, the VI applies to the last graph you insert in the current worksheet. Use the graph index input to format a specific graph in the current worksheet. The Excel Set Graph Scale VI only sets the scale on graphs

### Excel Set Graph Scale VI

Sets the scale parameters of the x- and y-axes and formats the graph gridlines.

graph index

Note

[IMAGE alt='icon' src='excel-set-graph-scale-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. axis type (xlCategory) — axis type specifies the type of axis to format. The default is xlCategory, which generally represents the X axis. You also can select xlValue, which generally represents the Y axis. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current worksheet. Note Graphs, images, ActiveX controls, and OLE objects form a collection for each worksheet. Each object has an index value based on the order of the objects in the worksheet. Index values begin at 0. For example, if you insert two images into the worksheet before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. axis config — axis config specifies the ways in which the VI scales the axis. autoscale — autoscale determines whether the VI scales the axis automatically. The default is TRUE, which enables autoscaling. min — min specifies the minimum scale value if you set autoscale to FALSE. max — max specifies the maximum scale value if you set autoscale to FALSE. scale type — scale type determines whether you want a logarithmic or linear scale. The default is linear. gridlines — gridlines sets the gridlines parameters. has major gridlines? — has major gridlines? determines whether the graph includes major gridlines. The default is FALSE, in which the graph does not include major gridlines. has minor gridlines? — has minor gridlines? determines whether the graph includes minor gridlines. The default is FALSE, in which the graph does not include minor gridlines. major gridlines color — major gridlines color sets the color of the major gridlines in the graph. The default is black. You can wire a color box constant to this input. minor gridlines color — minor gridlines color sets the color of the minor gridlines in the graph. The default is black. You can wire a color box constant to this input. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| autoscale — autoscale determines whether the VI scales the axis automatically. The default is TRUE, which enables autoscaling. min — min specifies the minimum scale value if you set autoscale to FALSE. max — max specifies the maximum scale value if you set autoscale to FALSE. scale type — scale type determines whether you want a logarithmic or linear scale. The default is linear. |
| has major gridlines? — has major gridlines? determines whether the graph includes major gridlines. The default is FALSE, in which the graph does not include major gridlines. has minor gridlines? — has minor gridlines? determines whether the graph includes minor gridlines. The default is FALSE, in which the graph does not include minor gridlines. major gridlines color — major gridlines color sets the color of the major gridlines in the graph. The default is black. You can wire a color box constant to this input. minor gridlines color — minor gridlines color sets the color of the minor gridlines in the graph. The default is black. You can wire a color box constant to this input. |

Parent topic:

Excel Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-page-numbering-vi.html language=enus -->
## TOPIC 00065: Excel Set Page Numbering VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-page-numbering-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-page-numbering-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Activates the page numbering on the current document. icon Inputs/Outputs cbool.png include page x of n include page x of n determines whether the page numbering format includes the text x of n where x is the current page number and n is the total page count of the report. Note (Word 2007) The forma

### Excel Set Page Numbering VI

Activates the page numbering on the current document.

[IMAGE alt='icon' src='excel-set-page-numbering-vi.png']

#### Inputs/Outputs

| include page x of n — include page x of n determines whether the page numbering format includes the text x of n where x is the current page number and n is the total page count of the report. Note (Word 2007) The format for page numbering is x/n. include page x of n determines whether the page numbering format includes the text x of n where x is the current page number and n is the total page count of the report. Note (Word 2007) The format for page numbering is x/n. The default is FALSE, which sets the page numbering format to include only the current page number. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. position (footers) — position sets the position of the page numbers in report headers or footers. By default, page numbers appear in the footers. alignment (right) — alignment sets the alignment of the page numbers. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-set-paper-size-vi.html language=enus -->
## TOPIC 00066: Excel Set Paper Size VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-set-paper-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-set-paper-size-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the paper size you want to associate with a worksheet. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. ci32.png paper size (letter) paper size

### Excel Set Paper Size VI

Sets the paper size you want to associate with a worksheet.

[IMAGE alt='icon' src='excel-set-paper-size-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. paper size (letter) — paper size sets the paper size you want to associate with the worksheet. The default is letter size. You can select one of 42 paper sizes, including envelope, A4, and legal size. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-sort-data-vi.html language=enus -->
## TOPIC 00067: Excel Sort Data VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-sort-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-sort-data-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sorts the range of cells specified by the start and end clusters. icon Inputs/Outputs ci32.png order (ascend) order specifies the order in which the VI sorts data. cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Repo

### Excel Sort Data VI

Sorts the range of cells specified by the **start** and **end** clusters.

[IMAGE alt='icon' src='excel-sort-data-vi.png']

#### Inputs/Outputs

| order (ascend) — order specifies the order in which the VI sorts data. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. from (0, 0) — from specifies the cell from which the VI sorts data. The position of this cell is relative to the top left corner of the current worksheet. row — row represents the row index. column — column represents the column index. start (0, 0) — start sets the beginning of the range of cells to sort. row — row represents the row index. column — column represents the column index. end (0, 0) — end sets the end of the range of cells to sort. row — row represents the last row index. column — column represents the last column index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. orientation (rows) — orientation specifies the order in which the data sorts. If you use xlSortRows, the VI sorts data by row, from top to bottom. If you use xlSortColumns, the VI sorts data by column, from left to right. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the row index. column — column represents the column index. |
| row — row represents the row index. column — column represents the column index. |
| row — row represents the last row index. column — column represents the last column index. |

Parent topic:

Excel Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-update-graph-vi.html language=enus -->
## TOPIC 00068: Excel Update Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-update-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-update-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the data of an existing graph. By default, the VI applies to the last graph you insert in the current worksheet. Use the graph index input to modify a specific graph in the current worksheet. The Excel Update Graph VI only updates graphs you create using the LabVIEW Report Generation Toolkit

### Excel Update Graph VI

Updates the data of an existing graph.

graph index

Note

[IMAGE alt='icon' src='excel-update-graph-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. row header — row header specifies a new row header to write into the graph. Leave this parameter unwired if you are updating an XY graph. column header — column header specifies a new column header to write into the graph. Leave this parameter unwired if you are updating an XY graph. graph data — graph data contains new data that the VI uses to update the graph. Microsoft Office returns an error if you plot more than 3,999 points per row or column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current worksheet. Note Graphs, images, ActiveX controls, and OLE objects form a collection for each worksheet. Each object has an index value based on the order of the objects in the worksheet. Index values begin at 0. For example, if you insert two images into the worksheet before you insert a graph, the index value for the graph is 2. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/excel-llb/excel-workbook-properties-vi.html language=enus -->
## TOPIC 00069: Excel Workbook Properties VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/excel-llb/excel-workbook-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/excel-llb/excel-workbook-properties-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the properties of the current workbook, such as the author, title, and subject. You also can use this VI to return the number of worksheets in the current workbook. icon Inputs/Outputs cstr.png title ("") title sets the document title. cNI__reportlvclass.png report in report in is a reference t

### Excel Workbook Properties VI

Sets the properties of the current workbook, such as the author, title, and subject. You also can use this VI to return the number of worksheets in the current workbook.

[IMAGE alt='icon' src='excel-workbook-properties-vi.png']

#### Inputs/Outputs

| title ("") — title sets the document title. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. subject ("") — subject sets the document subject. author ("") — author sets the document author. comments ("") — comments sets the document comments. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. worksheets count — worksheets count returns the number of worksheets in the workbook. current worksheet name — current worksheet name returns the name of the worksheet in which the VI set properties. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Excel General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/borders-and-shading-constant-shell-vi.html language=enus -->
## TOPIC 00070: Borders and Shading Constant

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/borders-and-shading-constant-shell-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/borders-and-shading-constant-shell-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the borders and shading attributes of a document. icon

### Borders and Shading Constant

Defines the borders and shading attributes of a document.

[IMAGE alt='icon' src='borders-and-shading-constant-shell-vi.png']

Parent topic:

Word Constants

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/borders-and-shading-constant-table-shell-vi.html language=enus -->
## TOPIC 00071: Borders and Shading Constant (Table)

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/borders-and-shading-constant-table-shell-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/borders-and-shading-constant-table-shell-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the borders and shading attributes of a table in Word. icon

### Borders and Shading Constant (Table)

Defines the borders and shading attributes of a table in Word.

[IMAGE alt='icon' src='borders-and-shading-constant-table-shell-vi.png']

Parent topic:

Word Constants

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/indent-and-spacing-constant-shell-vi.html language=enus -->
## TOPIC 00072: Indent and Spacing Constant

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/indent-and-spacing-constant-shell-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/indent-and-spacing-constant-shell-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the indent and spacing attributes for a specified range within a Word document. icon

### Indent and Spacing Constant

Defines the indent and spacing attributes for a specified range within a Word document.

[IMAGE alt='icon' src='indent-and-spacing-constant-shell-vi.png']

Parent topic:

Word Constants

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/line-and-page-break-constant-shell-vi.html language=enus -->
## TOPIC 00073: Line and Page Break Constant

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/line-and-page-break-constant-shell-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/line-and-page-break-constant-shell-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines line and page break attributes of a specified range within a document. icon

### Line and Page Break Constant

Defines line and page break attributes of a specified range within a document.

[IMAGE alt='icon' src='line-and-page-break-constant-shell-vi.png']

Parent topic:

Word Constants

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-add-new-document-vi.html language=enus -->
## TOPIC 00074: Word Add New Document VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-add-new-document-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-add-new-document-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new document to the document collection. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cpath.png document path (not a path) document path

### Word Add New Document VI

Adds a new document to the document collection.

[IMAGE alt='icon' src='word-add-new-document-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. document path (not a path) — document path refers to the path of the existing document that you want to set as the current document. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-add-reference-to-vbproj-vi.html language=enus -->
## TOPIC 00075: Word Add Reference to VBproj VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-add-reference-to-vbproj-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-add-reference-to-vbproj-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an external reference to the Microsoft Visual Basic project associated with the current document. This is the equivalent to selecting Tools>>References in the Microsoft Visual Basic editor. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data,

### Word Add Reference to VBproj VI

Adds an external reference to the Microsoft Visual Basic project associated with the current document. This is the equivalent to selecting **Tools>>References** in the Microsoft Visual Basic editor.

[IMAGE alt='icon' src='word-add-reference-to-vbproj-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. reference path — reference path is the path of the reference to add to the Visual Basic project associated with the current document. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-bring-to-front-vi.html language=enus -->
## TOPIC 00076: Word Bring to Front VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-bring-to-front-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-bring-to-front-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the state of a Word window to minimized, maximized, or normal. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cenum.png window state (maxi

### Word Bring to Front VI

Changes the state of a Word window to minimized, maximized, or normal.

[IMAGE alt='icon' src='word-bring-to-front-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. window state (maximized) — window state sets the Word window size. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-document-properties-vi.html language=enus -->
## TOPIC 00077: Word Document Properties VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-document-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-document-properties-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the properties of the current document, such as the title, subject, and author. icon Inputs/Outputs cstr.png title ("") title sets the document title. cNI__reportlvclass.png report in report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Re

### Word Document Properties VI

Sets the properties of the current document, such as the title, subject, and author.

[IMAGE alt='icon' src='word-document-properties-vi.png']

#### Inputs/Outputs

| title ("") — title sets the document title. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. subject ("") — subject sets the document subject. author ("") — author sets the document author. comments ("") — comments sets the document comments. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. table count — table count returns the number of tables in the current document. shape count — shape count returns the number of objects in the current document. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-easy-graph-vi.html language=enus -->
## TOPIC 00078: Word Easy Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-easy-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-easy-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a graph into a Microsoft Word report. icon Inputs/Outputs cenum.png graph type (col clustered) graph type sets the type of graph the VI creates. The default is a column graph. You can select one of 65 types of graphs, including XY (scatter), line, bar, three-dimensional surface, pie, and are

### Word Easy Graph VI

Inserts a graph into a Microsoft Word report.

[IMAGE alt='icon' src='word-easy-graph-vi.png']

#### Inputs/Outputs

| graph type (col clustered) — graph type sets the type of graph the VI creates. The default is a column graph. You can select one of 65 types of graphs, including XY (scatter), line, bar, three-dimensional surface, pie, and area graphs. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. row headers — row headers contains the row headings. Leave this parameter unwired if you want to create an XY graph. column headers — column headers contains the column headings. Leave this parameter unwired if you want to create an XY graph. data — data contains the data written into the graph. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. graph title ("") — graph title contains the title of the graph. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-easy-table-num-vi.html language=enus -->
## TOPIC 00079: Word Easy Table (num) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-easy-table-num-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-easy-table-num-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts and formats a table into a Microsoft Word report. The data type you wire to the data input determines the polymorphic instance to use. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. ci32.png auto format (non

### Word Easy Table (num) VI

Inserts and formats a table into a Microsoft Word report. The data type you wire to the **data** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-easy-table-num-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. auto format (none) — auto format sets the table format using Word preset table styles. The default is no formatting. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. row headers — row headers contains the row headers of the table inserted into the report. column headers — column headers contains the column headers of the table inserted into the report. text data — text data contains the data for the table. error in (no error) — error in describes error conditions that occur before this VI or function runs. font — font sets the font attributes that the VI uses when formatting. font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. format string (%.3f) — format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string when you wire numeric data to the text data input. report out — report out is a reference to the report whose appearance, data, and printing you want to control. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |

Parent topic:

Word Easy Table VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-easy-table-str-vi.html language=enus -->
## TOPIC 00080: Word Easy Table (str) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-easy-table-str-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-easy-table-str-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts and formats a table into a Microsoft Word report. The data type you wire to the data input determines the polymorphic instance to use. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. ci32.png auto format (non

### Word Easy Table (str) VI

Inserts and formats a table into a Microsoft Word report. The data type you wire to the **data** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-easy-table-str-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. auto format (none) — auto format sets the table format using Word preset table styles. The default is no formatting. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. row headers — row headers contains the row headers of the table inserted into the report. column headers — column headers contains the column headers of the table inserted into the report. data — data contains the data of the table inserted into the report. error in (no error) — error in describes error conditions that occur before this VI or function runs. font — font sets the font attributes that the VI uses when formatting. font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. report out — report out is a reference to the report whose appearance, data, and printing you want to control. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |

Parent topic:

Word Easy Table VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-easy-table-vi.html language=enus -->
## TOPIC 00081: Word Easy Table VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-easy-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-easy-table-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts and formats a table into a Microsoft Word report. The data type you wire to the data input determines the polymorphic instance to use. icon

### Word Easy Table VI

Inserts and formats a table into a Microsoft Word report. The data type you wire to the **data** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-easy-table-vi.png']

- [Word Easy Table (str) VI](../../../../vi-lib/addons/office/word-llb/word-easy-table-str-vi.html) Inserts and formats a table into a Microsoft Word report. The data type you wire to the data input determines the polymorphic instance to use.
- [Word Easy Table (num) VI](../../../../vi-lib/addons/office/word-llb/word-easy-table-num-vi.html) Inserts and formats a table into a Microsoft Word report. The data type you wire to the data input determines the polymorphic instance to use.

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-easy-text-vi.html language=enus -->
## TOPIC 00082: Word Easy Text VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-easy-text-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-easy-text-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds text to a Microsoft Word report. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. cstr.png style ("") style specifies the name of a Microsoft Word style to

### Word Easy Text VI

Adds text to a Microsoft Word report.

[IMAGE alt='icon' src='word-easy-text-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. style ("") — style specifies the name of a Microsoft Word style to apply to the text. You can create and edit styles in Word. background pattern color (w) — background pattern color sets the color that will be used for the background of the report. The default is white. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. text — text contains the text to enter into the document. alignment (left) — alignment aligns the text to the right, left, or center. The default is left alignment. font — font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. outside line style (none) — outside line style sets the style for lines outside the text. The default is for no lines. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-easy-title-vi.html language=enus -->
## TOPIC 00083: Word Easy Title VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-easy-title-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-easy-title-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a title to a Microsoft Word report. icon Inputs/Outputs cu16.png font settings source font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. cNI__reportlvclass.png report in report in is a reference to the repor

### Word Easy Title VI

Adds a title to a Microsoft Word report.

[IMAGE alt='icon' src='word-easy-title-vi.png']

#### Inputs/Outputs

| font settings source — font settings source specifies the way in which you want to select font settings. The VI ignores this input for HTML and standard reports. report in — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. title — title contains the text you want to use as the report title. font — font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. report out — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. font out — font out contains the font settings the VI uses for formatting, which you can use in other VIs. The values are valid for all report types. font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| font name — font name indicates the name of the font used, such as Times New Roman. font size — font size indicates the size at which the font appears, in points. bold — bold indicates whether the text is in bold. italic — italic indicates whether the text is in italics. underline — underline indicates whether the text is underlined. strike through — strike through indicates whether the text is struck through. font color — font color indicates the color of the text. |

Parent topic:

Word Specific

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi-2.html language=enus -->
## TOPIC 00084: Word Edit Cell ([dbl]) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi-2.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi-2.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon Inputs/Outputs cstr.png format string (%.3f) format string specifies the number formatting to use when LabVIEW converts the numbers t

### Word Edit Cell ([dbl]) VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-dbl-vi-2.png']

#### Inputs/Outputs

| format string (%.3f) — format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string when you wire numeric data to the value input. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. value — value specifies the array of numbers to write into the table cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. start (0, 0) — start defines the position of the edited cell. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Edit Cell VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi.html language=enus -->
## TOPIC 00085: Word Edit Cell (dbl) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon Inputs/Outputs cstr.png format string (%.3f) format string specifies the number formatting to use when LabVIEW converts the numbers t

### Word Edit Cell (dbl) VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-dbl-vi.png']

#### Inputs/Outputs

| format string (%.3f) — format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string when you wire numeric data to the value input. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. value — value specifies the numeric value to write into the table cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. start (0, 0) — start defines the position of the edited cell. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Edit Cell VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-i32-vi-2.html language=enus -->
## TOPIC 00086: Word Edit Cell (i32) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-i32-vi-2.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-i32-vi-2.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon Inputs/Outputs cstr.png format string (%.3f) format string specifies the number formatting to use when LabVIEW converts the numbers t

### Word Edit Cell (i32) VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-i32-vi-2.png']

#### Inputs/Outputs

| format string (%.3f) — format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string when you wire numeric data to the value input. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. value — value specifies the numeric value to write into the table cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. start (0, 0) — start defines the position of the edited cell. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Edit Cell VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-i32-vi.html language=enus -->
## TOPIC 00087: Word Edit Cell ([i32]) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-i32-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon Inputs/Outputs cstr.png format string (%.3f) format string specifies the number formatting to use when LabVIEW converts the numbers t

### Word Edit Cell ([i32]) VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-i32-vi.png']

#### Inputs/Outputs

| format string (%.3f) — format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string when you wire numeric data to the value input. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. value — value specifies the array of numbers to write into the table cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. start (0, 0) — start defines the position of the edited cell. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Edit Cell VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-path-vi.html language=enus -->
## TOPIC 00088: Word Edit Cell (path) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-path-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control

### Word Edit Cell (path) VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-path-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. value — value specifies the path of the file to insert in the cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. start (0, 0) — start defines the position of the edited cell. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Edit Cell VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-str-vi-2.html language=enus -->
## TOPIC 00089: Word Edit Cell (str) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-str-vi-2.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-str-vi-2.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control

### Word Edit Cell (str) VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-str-vi-2.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. value — value specifies the string value to write into the table cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. start (0, 0) — start defines the position of the edited cell. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Edit Cell VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-str-vi.html language=enus -->
## TOPIC 00090: Word Edit Cell ([str]) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-str-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-str-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control

### Word Edit Cell ([str]) VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-str-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. value — value contains an array of strings to insert into the table cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. start (0, 0) — start defines the position of the edited cell. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Edit Cell VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-edit-cell-vi.html language=enus -->
## TOPIC 00091: Word Edit Cell VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-edit-cell-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-edit-cell-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use. icon

### Word Edit Cell VI

Edits the cell specified by the **row** and **column** elements of the **start** input. The data type you wire to the **value** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-edit-cell-vi.png']

- [Word Edit Cell ([str]) VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-str-vi.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.
- [Word Edit Cell (path) VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-path-vi.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.
- [Word Edit Cell (str) VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-str-vi-2.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.
- [Word Edit Cell ([i32]) VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-i32-vi.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.
- [Word Edit Cell (i32) VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-i32-vi-2.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.
- [Word Edit Cell (dbl) VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.
- [Word Edit Cell ([dbl]) VI](../../../../vi-lib/addons/office/word-llb/word-edit-cell-dbl-vi-2.html) Edits the cell specified by the row and column elements of the start input. The data type you wire to the value input determines the polymorphic instance to use.

Parent topic:

Word Tables

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-find-replace-num-vi.html language=enus -->
## TOPIC 00092: Word Find & Replace (num) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-find-replace-num-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-find-replace-num-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finds and replaces a text segment. The data type you wire to the replace with input determines the polymorphic instance to use. icon Inputs/Outputs cstr.png format string (%.3f) format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string wh

### Word Find & Replace (num) VI

Finds and replaces a text segment. The data type you wire to the **replace with** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-find-replace-num-vi.png']

#### Inputs/Outputs

| format string (%.3f) — format string specifies the number formatting to use when LabVIEW converts the numbers to characters. Use format string when you wire numeric data to the replace with input. search range (entire doc) — search range specifies whether the VI performs the search on the entire document, from a specific starting point, or on a custom range. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. find what? — find what? describes the text segment for which the VI will search. replace with — replace with contains the number that replaces the text segment. search scope (first occurrence) — search scope specifies whether the VI replaces all occurrences of the text segment or only the first occurrence. The default replaces only the first occurrence. error in (no error) — error in describes error conditions that occur before this VI or function runs. start — start specifies the beginning of the document or the starting point for the search. end — end specifies the end of the document. — report out is a reference to the report whose appearance, data, and printing you want to control. found? — found? returns TRUE if the VI finds at least one occurrence of the searched string. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

Word Find & Replace VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-find-replace-str-vi.html language=enus -->
## TOPIC 00093: Word Find & Replace (str) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-find-replace-str-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-find-replace-str-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finds and replaces a text segment. The data type you wire to the replace with input determines the polymorphic instance to use. icon Inputs/Outputs cu16.png search range (entire doc) search range specifies whether the VI performs the search on the entire document, from a specific starting point, or

### Word Find & Replace (str) VI

Finds and replaces a text segment. The data type you wire to the **replace with** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-find-replace-str-vi.png']

#### Inputs/Outputs

| search range (entire doc) — search range specifies whether the VI performs the search on the entire document, from a specific starting point, or on a custom range. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. find what? — find what? describes the text segment for which the VI will search. replace with — replace with contains the string that replaces the found text segment search scope (first occurrence) — search scope specifies whether the VI replaces all occurrences of the text segment or only the first occurrence. The default replaces only the first occurrence. error in (no error) — error in describes error conditions that occur before this VI or function runs. start — start specifies the beginning of the document or the starting point for the search. end — end specifies the end of the document. — report out is a reference to the report whose appearance, data, and printing you want to control. found? — found? returns TRUE if the VI finds at least one occurrence of the searched string. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |

Parent topic:

Word Find & Replace VI

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-find-replace-vi.html language=enus -->
## TOPIC 00094: Word Find & Replace VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-find-replace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-find-replace-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finds and replaces a text segment. The data type you wire to the replace with input determines the polymorphic instance to use. icon

### Word Find & Replace VI

Finds and replaces a text segment. The data type you wire to the **replace with** input determines the polymorphic instance to use.

[IMAGE alt='icon' src='word-find-replace-vi.png']

- [Word Find & Replace (str) VI](../../../../vi-lib/addons/office/word-llb/word-find-replace-str-vi.html) Finds and replaces a text segment. The data type you wire to the replace with input determines the polymorphic instance to use.
- [Word Find & Replace (num) VI](../../../../vi-lib/addons/office/word-llb/word-find-replace-num-vi.html) Finds and replaces a text segment. The data type you wire to the replace with input determines the polymorphic instance to use.

Parent topic:

Word General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-format-borders-adv-vi.html language=enus -->
## TOPIC 00095: Word Format Borders (adv) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-format-borders-adv-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-format-borders-adv-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets border and shading attributes of a Word table or part of a table that the start and end inputs specify. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW clas

### Word Format Borders (adv) VI

Sets border and shading attributes of a Word table or part of a table that the **start** and **end** inputs specify.

[IMAGE alt='icon' src='word-format-borders-adv-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. borders and shading — borders and shading sets the line style, width, and color for table borders and the background color and pattern for table cells. outside line style — outside line style sets the type of line for the outside border of the table cells. outside color index — outside color index sets the color for the outside border of the table cells. The default is black. outside line width — outside line width sets the thickness of the border around the table cells. background pattern color — background pattern color sets the background color of the table cells. start (-1) — start sets the beginning of the custom range. The default is -1, which formats the entire document. end (-1) — end sets the end of the custom range. The default is -1, which formats the entire document. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| outside line style — outside line style sets the type of line for the outside border of the table cells. outside color index — outside color index sets the color for the outside border of the table cells. The default is black. outside line width — outside line width sets the thickness of the border around the table cells. background pattern color — background pattern color sets the background color of the table cells. |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-format-cell-vi.html language=enus -->
## TOPIC 00096: Word Format Cell VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-format-cell-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-format-cell-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Formats the cells specified by the start and end clusters. icon Inputs/Outputs ccclst.png font font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. cstr.png font name font name specifies the name of the font you want to use, such

### Word Format Cell VI

Formats the cells specified by the **start** and **end** clusters.

[IMAGE alt='icon' src='word-format-cell-vi.png']

#### Inputs/Outputs

| font — font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. autoformat (-1: none) — autoformat sets the cell format using Word preset table styles. The default is no formatting. In Word, select Table»Table AutoFormat to view examples of Word table styles. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the entire table. If start is wired but end is unwired, the VI formats the unique cell, row, or column specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. start row — start row represents the row index. start column — start column represents the column index. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the entire table. If start is wired but end is unwired, the VI formats the unique cell, row, or column specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. end row — end row represents the last row index of the range to format. end column — end column represents the last column index of the range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |
| start row — start row represents the row index. start column — start column represents the column index. |
| end row — end row represents the last row index of the range to format. end column — end column represents the last column index of the range to format. |

Parent topic:

Word Tables

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-format-paragraph-adv-vi.html language=enus -->
## TOPIC 00097: Word Format Paragraph (adv) VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-format-paragraph-adv-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-format-paragraph-adv-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the indent and spacing attributes of a document range specified by the start and end indexes. icon Inputs/Outputs cnclst.png indent and spacing indent and spacing sets the paragraph alignment, indentation, and line spacing. cenum.png alignment alignment aligns the text in the paragraph to the r

### Word Format Paragraph (adv) VI

Sets the indent and spacing attributes of a document range specified by the **start** and **end** indexes.

[IMAGE alt='icon' src='word-format-paragraph-adv-vi.png']

#### Inputs/Outputs

| indent and spacing — indent and spacing sets the paragraph alignment, indentation, and line spacing. alignment — alignment aligns the text in the paragraph to the right, left, or center. The default is left alignment. left — left determines the indentation for the paragraph relative to the left margin. right — right determines the indentation for the paragraph relative to the right margin. special — special applies particular types of paragraph indentation, such as a hanging indent or indention of only the first line in the paragraph. by — by determines the amount of indentation if you specify a type of indent in special. before — before determines the amount of space before the paragraph. after — after determines the amount of space after the paragraph. line spacing — line spacing determines the amount of spacing between the lines of text in the paragraph. The default is multiple lines. at — at sets line spacing by pixel. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. measurement system (US) — measurement system determines the system that the VI uses to measure size. start (-1) — start sets the beginning of the custom range. The default is -1, which formats the entire document. end (-1) — end sets the end of the custom range. The default is -1, which formats the entire document. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. line and page breaks — line and page breaks specifies the formatting and placement of lines in the paragraph and paragraphs on the page. widow/orphan ctrl — widow/orphan ctrl determines whether to allow lines with a single word in the last line, or pages with a single line at the top. Keeps lines together — Keeps lines together determines whether to keep all the lines in a paragraph on one page. keep with next — keep with next determines whether to put the paragraph on the same page as the following paragraph. page break before — page break before determines whether to insert a page break before the paragraph. suppress line numbers — suppress line numbers determines whether to display numbers that mark each line in a paragraph. don't hyphenate — don't hyphenate determines whether to split a word with a hyphen at the end of a line or to start the word on the following line. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| alignment — alignment aligns the text in the paragraph to the right, left, or center. The default is left alignment. left — left determines the indentation for the paragraph relative to the left margin. right — right determines the indentation for the paragraph relative to the right margin. special — special applies particular types of paragraph indentation, such as a hanging indent or indention of only the first line in the paragraph. by — by determines the amount of indentation if you specify a type of indent in special. before — before determines the amount of space before the paragraph. after — after determines the amount of space after the paragraph. line spacing — line spacing determines the amount of spacing between the lines of text in the paragraph. The default is multiple lines. at — at sets line spacing by pixel. |
| widow/orphan ctrl — widow/orphan ctrl determines whether to allow lines with a single word in the last line, or pages with a single line at the top. Keeps lines together — Keeps lines together determines whether to keep all the lines in a paragraph on one page. keep with next — keep with next determines whether to put the paragraph on the same page as the following paragraph. page break before — page break before determines whether to insert a page break before the paragraph. suppress line numbers — suppress line numbers determines whether to display numbers that mark each line in a paragraph. don't hyphenate — don't hyphenate determines whether to split a word with a hyphen at the end of a line or to start the word on the following line. |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-format-picture-vi.html language=enus -->
## TOPIC 00098: Word Format Picture VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-format-picture-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-format-picture-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Formats the image specified by picture index. You can resize the image or modify its color type. icon Inputs/Outputs cu16.png measurement system (US) measurement system determines the system that the VI uses to measure size. csgl.png scale factor (1) scale factor sets the scaling factor used to resi

### Word Format Picture VI

Formats the image specified by **picture index**. You can resize the image or modify its **color type**.

[IMAGE alt='icon' src='word-format-picture-vi.png']

#### Inputs/Outputs

| measurement system (US) — measurement system determines the system that the VI uses to measure size. scale factor (1) — scale factor sets the scaling factor used to resize the image. Set height and width to –1 if you want to use this control. The default is 1, which does not change the image size. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. height (-1) — height sets the height of the image in the units of measurement system. The default is –1, which does not change the image height. width (-1) — width sets the width of the picture in the units of measurement system. The default is –1, which does not change the image width. picture index (-1) — picture index specifies the index of the image to format. The default is -1, in which the VI modifies the last image in the current document or worksheet. Note Graphs, images, ActiveX controls, and OLE objects form a collection for each document or worksheet. Each object has an index value based on the order of the objects. Index values begin at 0. For example, if you insert two images into a document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. color type (auto) — color type sets the type of color transformation the VI applies to the image, such as grayscale or black-and-white. The default setting is automatic. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-format-text-vi.html language=enus -->
## TOPIC 00099: Word Format Text VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-format-text-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-format-text-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the font attributes of a document range specified by the start and end indexes. icon Inputs/Outputs cstr.png style ("") style specifies a predefined style in Word to apply to the document or document range. ccclst.png font font sets the font attributes that the VI uses when formatting. The VI i

### Word Format Text VI

Sets the font attributes of a document range specified by the **start** and **end** indexes.

[IMAGE alt='icon' src='word-format-text-vi.png']

#### Inputs/Outputs

| style ("") — style specifies a predefined style in Word to apply to the document or document range. font — font sets the font attributes that the VI uses when formatting. The VI ignores this input if you wire the autoformat input. font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. start (-1) — start sets the beginning of the custom range. The default is -1, which formats the entire document. end (-1) — end sets the end of the custom range. The default is -1, which formats the entire document. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font name — font name specifies the name of the font you want to use, such as Times New Roman. If you misspell the font name or specify a font that is not installed on the computer, the operating system selects a font. font size — font size specifies the size at which you want the font to appear, in points. bold — bold specifies whether the text is in bold. The default is bolded text. italic — italic specifies whether the text is in italics. By default, the control does not change the text settings. underline — underline specifies whether the text is underlined. By default, the control does not change the text settings. strike through — strike through specifies whether the text contains a strikethrough line. By default, the control does not change the text settings. font color — font color allows you to select the color of the font from a color table. The default is transparency. |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-get-activex-references-vi.html language=enus -->
## TOPIC 00100: Word Get ActiveX References VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-get-activex-references-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-get-activex-references-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns ActiveX references to Microsoft Word. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cerrcodeclst.png error in (no error) error in describ

### Word Get ActiveX References VI

Returns ActiveX references to Microsoft Word.

[IMAGE alt='icon' src='word-get-activex-references-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Word._Application — Word._Application is a reference to the application Microsoft Word. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. Word.Documents — Word.Documents is a reference to all the open documents in Microsoft Word. Word._Document — Word._Document is a reference to the active document. Word.Tables — Word.Tables is a reference to all the tables in the active document. error out — error out contains error information. This output provides standard error out functionality. Word.InlineShapes — Word.InlineShapes is a reference to graphics in the active document. |
| --- |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-get-document-vi.html language=enus -->
## TOPIC 00101: Word Get Document VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-get-document-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-get-document-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the document defined in the document index parameter as the current document. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. ci32.png documen

### Word Get Document VI

Sets the document defined in the **document index** parameter as the current document.

[IMAGE alt='icon' src='word-get-document-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. document index (0) — document index specifies the index of the document that the VI sets as the new current document. close current document? (T) — close current document? determines whether the VI closes the current document before setting another document as current. The default is TRUE, which closes the document. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-import-module-vi.html language=enus -->
## TOPIC 00102: Word Import Module VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-import-module-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-import-module-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports an external module (*.bas) in the Microsoft Visual Basic project associated with the current document. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW cl

### Word Import Module VI

Imports an external module (*.bas) in the Microsoft Visual Basic project associated with the current document.

[IMAGE alt='icon' src='word-import-module-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. module path (not a path) — module path specifies the path of the external Microsoft Visual Basic module to import into the current document. module code ("") — module code contains the source code of the module to import into the Microsoft Visual Basic project. This parameter is only necessary if you do not specify a path in the module path parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. module reference — module reference provides a reference to the imported module. You can send this output to the Word Remove Module VI to remove the module after the macro runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-insert-field-vi.html language=enus -->
## TOPIC 00103: Word Insert Field VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-insert-field-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-insert-field-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a field at the end of the current document or in a document bookmark. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. ci32.png type type de

### Word Insert Field VI

Inserts a field at the end of the current document or in a document bookmark.

[IMAGE alt='icon' src='word-insert-field-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. type — type describes the type of field to insert in the current document. The default is an empty field. You can select from more than 80 types of fields. Refer to the specific version of Word that you are using for a complete list of available field types. bookmark ("") — bookmark specifies a bookmark where you want to insert the object or field. If you do not specify a bookmark, the VI inserts the object or field at the end of the document. text ("") — text contains text you want to associate with the field. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-insert-graph-vi.html language=enus -->
## TOPIC 00104: Word Insert Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-insert-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-insert-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a new graph into the current document. icon Inputs/Outputs cbool.png has legend? (F) has legend? shows or hides the graph legend. The default is FALSE, in which the VI does not display the graph legend. cu16.png measurement system (US) measurement system determines the system that the VI use

### Word Insert Graph VI

Inserts a new graph into the current document.

[IMAGE alt='icon' src='word-insert-graph-vi.png']

#### Inputs/Outputs

| has legend? (F) — has legend? shows or hides the graph legend. The default is FALSE, in which the VI does not display the graph legend. measurement system (US) — measurement system determines the system that the VI uses to measure size. bookmark name ("") — bookmark name can be used to specify the bookmark from which the graph is inserted. If no bookmark is specified, this VI inserts the graph at the end of the document. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. column headers — column headers specifies the text of the column labels on the graph. Leave this parameter unwired if you want to create an XY graph. row headers — row headers specifies the text of the row labels on the graph. Leave this parameter unwired if you want to create an XY graph. data — data contains numerical data that the VI uses to create the graph. Microsoft Office returns an error if you plot more than 3,999 points per row or column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. graph type (col clustered) — graph type sets the type of graph the VI creates. The default is a column graph. You can select one of 65 types of graphs, including XY (scatter), line, bar, three-dimensional surface, pie, and area graphs. graph title ("") — graph title contains the title of the graph. graph size (5, 5) — graph size sets the graph size in the units of the measurement system. height — height is the graph height in the units of the measurement system. width — width is the graph width in the units of the measurement system. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. start — start represents the index of the character preceding the graph. end — end represents the index of the character following the graph. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| height — height is the graph height in the units of the measurement system. width — width is the graph width in the units of the measurement system. |

Parent topic:

Word Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-insert-object-vi.html language=enus -->
## TOPIC 00105: Word Insert Object VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-insert-object-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-insert-object-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts an object associated with a file into the current document. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cpath.png file path file path i

### Word Insert Object VI

Inserts an object associated with a file into the current document.

[IMAGE alt='icon' src='word-insert-object-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. file path — file path is the path of the object to insert into the document. bookmark ("") — bookmark specifies a bookmark where you want to insert the object or field. If you do not specify a bookmark, the VI inserts the object or field at the end of the document. link to file? (F) — link to file? specifies whether the object is linked to the original file or to a copy of the file. The default is FALSE, in which the VI links to a copy of the file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-insert-row-column-cell-vi.html language=enus -->
## TOPIC 00106: Word Insert Row-Column-Cell VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-insert-row-column-cell-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-insert-row-column-cell-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a row, a column, or a cell into an existing table. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cu16.png mode (entire column) mode speci

### Word Insert Row-Column-Cell VI

Inserts a row, a column, or a cell into an existing table.

[IMAGE alt='icon' src='word-insert-row-column-cell-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. mode (entire column) — mode specifies the type of insertion the VI performs on the table. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. start (0, 0) — start specifies the position of the cell from which the VI performs the insertion. row — row represents the row index. column — column represents the column index. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| row — row represents the row index. column — column represents the column index. |

Parent topic:

Word Tables

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-merge-cells-vi.html language=enus -->
## TOPIC 00107: Word Merge Cells VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-merge-cells-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-merge-cells-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges the cells specified by the start and end clusters into one cell. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. ci16.png table index (-1) t

### Word Merge Cells VI

Merges the cells specified by the **start** and **end** clusters into one cell.

[IMAGE alt='icon' src='word-merge-cells-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. start (0, 0) — start specifies the first cell of the range to merge. start row — start row represents the row index. start column — start column represents the column index. end — end specifies the last cell of the range to merge. end row — end row represents the last row index of the range to merge. end column — end column represents the last column index of the range to merge. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| start row — start row represents the row index. start column — start column represents the column index. |
| end row — end row represents the last row index of the range to merge. end column — end column represents the last column index of the range to merge. |

Parent topic:

Word Tables

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-quit-graph-vi.html language=enus -->
## TOPIC 00108: Word Quit Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-quit-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-quit-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes all ActiveX references related to a graph. Use this VI after you insert, update, or format a graph using Word. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this Lab

### Word Quit Graph VI

Closes all ActiveX references related to a graph. Use this VI after you insert, update, or format a graph using Word.

[IMAGE alt='icon' src='word-quit-graph-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-remove-module-vi.html language=enus -->
## TOPIC 00109: Word Remove Module VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-remove-module-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-remove-module-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes an external module from the Microsoft Visual Basic project associated with the current document. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class ob

### Word Remove Module VI

Removes an external module from the Microsoft Visual Basic project associated with the current document.

[IMAGE alt='icon' src='word-remove-module-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. module reference — module reference represents the reference to the external module to remove from the document. You can obtain the reference from the output of the Word Import Module VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-run-macro-vi.html language=enus -->
## TOPIC 00110: Word Run Macro VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-run-macro-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-run-macro-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs a macro on the current document. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. cstr.png macro name macro name specifies the name of the macr

### Word Run Macro VI

Runs a macro on the current document.

[IMAGE alt='icon' src='word-run-macro-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. macro name — macro name specifies the name of the macro to run from LabVIEW. parameters — parameters contains the input parameters of the macro. You cannot send more than nine parameters. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. return value — return value can be used to retrieve the macro input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Macros

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-send-document-vi.html language=enus -->
## TOPIC 00111: Word Send Document VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-send-document-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-send-document-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the current document to a list of recipients via email. You can use this VI only if you configure Microsoft Outlook or Outlook Express as the default email application. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you wa

### Word Send Document VI

Sends the current document to a list of recipients via email. You can use this VI only if you configure Microsoft Outlook or Outlook Express as the default email application.

[IMAGE alt='icon' src='word-send-document-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. recipients — recipients contains the list of email addresses the VI uses to send the report. subject ("") — subject contains the subject line of the message. message ("") — message contains the text of the email message to which the VI attaches the report. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-set-graph-colors-vi.html language=enus -->
## TOPIC 00112: Word Set Graph Colors VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-set-graph-colors-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-set-graph-colors-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the color attributes, marker style, and plot weight of an existing graph. icon Inputs/Outputs ci16.png weight (1) weight sets the thickness of the plot lines. ci32.png marker style (none) marker style specifies the type of markers that appear on the graph plots. The default setting displays no

### Word Set Graph Colors VI

Sets the color attributes, marker style, and plot weight of an existing graph.

[IMAGE alt='icon' src='word-set-graph-colors-vi.png']

#### Inputs/Outputs

| weight (1) — weight sets the thickness of the plot lines. marker style (none) — marker style specifies the type of markers that appear on the graph plots. The default setting displays no markers on the plot lines. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. plot area color (w) — plot area color sets the background color for the region of the graph that contains the plots. The default is white. You can wire a color box constant to this input. graph area color (w) — graph area color sets the background color for the region of the graph that includes the graph title, graph legend, and axis tick labels. The default is white. You can wire a color box constant to this input. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. plot colors — plot colors sets the color of the plot lines. You can wire an array of color box constants to this input. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-set-graph-font-vi.html language=enus -->
## TOPIC 00113: Word Set Graph Font VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-set-graph-font-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-set-graph-font-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the title and font attributes of the graph axis. icon Inputs/Outputs cstr.png number format (general) number format describes the format to apply to the axis of the graph. Refer to the Microsoft Word documentation for more information about number formatting. ccclst.png axis font axis font sets

### Word Set Graph Font VI

Sets the title and font attributes of the graph axis.

[IMAGE alt='icon' src='word-set-graph-font-vi.png']

#### Inputs/Outputs

| number format (general) — number format describes the format to apply to the axis of the graph. Refer to the Microsoft Word documentation for more information about number formatting. axis font — axis font sets the font attributes of the axis tick labels and legend. font style — font style specifies a specific Microsoft Word style to apply to the text. bold — bold specifies whether the text is in bold. italic — italic specifies whether the text is in italics. underline — underline specifies whether the text is underlined. size — size specifies the point size of the font. color — color specifies the text color. The default is black. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. axis type (category) — axis type specifies the type of axis to format. The default is xlCategory, which generally represents the X axis. You also can select xlValue, which generally represents the Y axis. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. title ("") — title contains the axis title. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| font style — font style specifies a specific Microsoft Word style to apply to the text. bold — bold specifies whether the text is in bold. italic — italic specifies whether the text is in italics. underline — underline specifies whether the text is underlined. size — size specifies the point size of the font. color — color specifies the text color. The default is black. |

Parent topic:

Word Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-set-graph-scale-vi.html language=enus -->
## TOPIC 00114: Word Set Graph Scale VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-set-graph-scale-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-set-graph-scale-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the scale parameters of the x- and y-axes. The VI also sets the gridlines parameters of the graph. icon Inputs/Outputs ccclst.png gridlines gridlines sets the gridlines parameters. cbool.png has major gridlines? has major gridlines? determines whether the graph includes major gridlines. The def

### Word Set Graph Scale VI

Sets the scale parameters of the x- and y-axes. The VI also sets the gridlines parameters of the graph.

[IMAGE alt='icon' src='word-set-graph-scale-vi.png']

#### Inputs/Outputs

| gridlines — gridlines sets the gridlines parameters. has major gridlines? — has major gridlines? determines whether the graph includes major gridlines. The default is FALSE, in which the graph does not include major gridlines. has minor gridlines? — has minor gridlines? determines whether the graph includes minor gridlines. The default is FALSE, in which the graph does not include minor gridlines. major gridlines color — major gridlines color sets the color of the major gridlines in the graph. The default is black. minor gridlines color — minor gridlines color sets the color of the minor gridlines in the graph. The default is black. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. axis type (xlCategory) — axis type specifies the type of axis to format. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current document. error in (no error) — error in describes error conditions that occur before this VI or function runs. axis config — axis config specifies the ways in which the VI scales the axis. autoscale — autoscale determines whether the VI scales the axis automatically. The default is TRUE, which enables autoscaling. min — min specifies the minimum scale value if you set autoscale to FALSE. max — max specifies the maximum scale value if you set autoscale to FALSE. scale type — scale type determines whether you want a logarithmic or linear scale. The default is linear. — report out is a reference to the report whose appearance, data, and printing you want to control. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| has major gridlines? — has major gridlines? determines whether the graph includes major gridlines. The default is FALSE, in which the graph does not include major gridlines. has minor gridlines? — has minor gridlines? determines whether the graph includes minor gridlines. The default is FALSE, in which the graph does not include minor gridlines. major gridlines color — major gridlines color sets the color of the major gridlines in the graph. The default is black. minor gridlines color — minor gridlines color sets the color of the minor gridlines in the graph. The default is black. |
| autoscale — autoscale determines whether the VI scales the axis automatically. The default is TRUE, which enables autoscaling. min — min specifies the minimum scale value if you set autoscale to FALSE. max — max specifies the maximum scale value if you set autoscale to FALSE. scale type — scale type determines whether you want a logarithmic or linear scale. The default is linear. |

Parent topic:

Word Graphs and Pictures

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-set-page-numbering-vi.html language=enus -->
## TOPIC 00115: Word Set Page Numbering VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-set-page-numbering-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-set-page-numbering-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Activates the page numbering on the current document. icon Inputs/Outputs cbool.png include page x of n include page x of n determines whether the page numbering format includes the text x of n where x is the current page number and n is the total page count of the report. Note (Word 2007) The forma

### Word Set Page Numbering VI

Activates the page numbering on the current document.

[IMAGE alt='icon' src='word-set-page-numbering-vi.png']

#### Inputs/Outputs

| include page x of n — include page x of n determines whether the page numbering format includes the text x of n where x is the current page number and n is the total page count of the report. Note (Word 2007) The format for page numbering is x/n. include page x of n determines whether the page numbering format includes the text x of n where x is the current page number and n is the total page count of the report. Note (Word 2007) The format for page numbering is x/n. The default is FALSE, which sets the page numbering format to include only the current page number. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. position (footers) — position sets the position of the page numbers in report headers or footers. By default, page numbers appear in the footers. alignment (right) — alignment sets the alignment of the page numbers. number style (arabic) — number style sets the style of the page numbers. By default, page numbers appear in Arabic style. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word General

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-set-paper-size-vi.html language=enus -->
## TOPIC 00116: Word Set Paper Size VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-set-paper-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-set-paper-size-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the paper size associated with the current document. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. ci32.png paper size (letter) paper size i

### Word Set Paper Size VI

Sets the paper size associated with the current document.

[IMAGE alt='icon' src='word-set-paper-size-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. paper size (letter) — paper size is the size of the page in the current document. The default is letter size. You can select from more than 40 paper sizes. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Advanced

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-set-table-dimensions-vi.html language=enus -->
## TOPIC 00117: Word Set Table Dimensions VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-set-table-dimensions-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-set-table-dimensions-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the column width, the row height, and the left indentation of any table in the document. icon Inputs/Outputs cu16.png measurement system (US) measurement system determines the system that the VI uses to measure size. c1dsgl.png table column widths table column widths sets the width of the table

### Word Set Table Dimensions VI

Sets the column width, the row height, and the left indentation of any table in the document.

[IMAGE alt='icon' src='word-set-table-dimensions-vi.png']

#### Inputs/Outputs

| measurement system (US) — measurement system determines the system that the VI uses to measure size. table column widths — table column widths sets the width of the table columns. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. left indent (0) — left indent sets the left indentation of the table. The left indentation represents the distance between the left page margin and the left edge of the table. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. table row heights — table row heights sets the height of the rows. fit to page width? (F) — fit to page width? automatically adjusts the table width to the page dimension if set to TRUE. The default is FALSE. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Tables

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-table-alignment-vi.html language=enus -->
## TOPIC 00118: Word Table Alignment VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-table-alignment-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-table-alignment-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the horizontal and vertical alignment of the cells specified by the start and end controls. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. ci

### Word Table Alignment VI

Sets the horizontal and vertical alignment of the cells specified by the **start** and **end** controls.

[IMAGE alt='icon' src='word-table-alignment-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. horizontal alignment (left) — horizontal alignment sets the horizontal alignment of text in the specified cells. The default setting aligns text along the left side of the cells. vertical alignment (top) — vertical alignment sets the vertical alignment of text in the specified cells. The default setting aligns text to the top of each cell. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the entire table. If start is wired but end is unwired, the VI formats the unique cell, row, or column specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. start row — start row represents the row index. start column — start column represents the column index. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the entire table. If start is wired but end is unwired, the VI formats the unique cell, row, or column specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. end row — end row represents the last row index of the range to format. end column — end column represents the last column index of the range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| start row — start row represents the row index. start column — start column represents the column index. |
| end row — end row represents the last row index of the range to format. end column — end column represents the last column index of the range to format. |

Parent topic:

Word Tables

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-table-borders-and-shading-vi.html language=enus -->
## TOPIC 00119: Word Table Borders and Shading VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-table-borders-and-shading-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-table-borders-and-shading-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the border and shading parameters of the cells specified by the start and end clusters. icon Inputs/Outputs cnclst.png borders and shading borders and shading sets the line style, width, and color for table borders and the background color and pattern for table cells. ci32.png outside line styl

### Word Table Borders and Shading VI

Sets the border and shading parameters of the cells specified by the **start** and **end** clusters.

[IMAGE alt='icon' src='word-table-borders-and-shading-vi.png']

#### Inputs/Outputs

| borders and shading — borders and shading sets the line style, width, and color for table borders and the background color and pattern for table cells. outside line style — outside line style sets the type of line for the outside border of the table cells. outside color — outside color sets the color for the outside border of the table cells. The default is black. outside line width — outside line width sets the thickness of the border around the table cells. inside line style — inside line style sets the type of line for the inside border of the table cells. inside color — inside color sets the color for the inside border of the table cells. The default is black. inside line width — inside line width sets the thickness of the inside border of the table cells. background pattern color — background pattern color sets the background color of the table cells. — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. table index (-1) — table index specifies the index of the table to edit. The default is -1, in which the VI modifies the last table in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. start (-1, -1) — start determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the entire table. If start is wired but end is unwired, the VI formats the unique cell, row, or column specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. start row — start row represents the row index. start column — start column represents the column index. end (-1, -1) — end determines the range of cells that the VI will format. If neither start nor end are wired, the VI formats the entire table. If start is wired but end is unwired, the VI formats the unique cell, row, or column specified by start. If neither row nor column are equal to –1, the VI formats the corresponding cell. If row is equal to –1, the VI formats the entire column. If column is equal to –1, the VI formats the entire row. If both start and end are wired, the VI formats the range of cells between start and end. end row — end row represents the last row index of the range to format. end column — end column represents the last column index of the range to format. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| outside line style — outside line style sets the type of line for the outside border of the table cells. outside color — outside color sets the color for the outside border of the table cells. The default is black. outside line width — outside line width sets the thickness of the border around the table cells. inside line style — inside line style sets the type of line for the inside border of the table cells. inside color — inside color sets the color for the inside border of the table cells. The default is black. inside line width — inside line width sets the thickness of the inside border of the table cells. background pattern color — background pattern color sets the background color of the table cells. |
| start row — start row represents the row index. start column — start column represents the column index. |
| end row — end row represents the last row index of the range to format. end column — end column represents the last column index of the range to format. |

Parent topic:

Word Tables

<!--NI_TOPIC bundle=lvrgt-api-ref path=vi-lib/addons/office/word-llb/word-update-graph-vi.html language=enus -->
## TOPIC 00120: Word Update Graph VI

- bundle_id: `lvrgt-api-ref`
- source_path: `vi-lib/addons/office/word-llb/word-update-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrgt-api-ref/raw/resource/enus/vi-lib/addons/office/word-llb/word-update-graph-vi.html
- document_id: `lvrgt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the data of an existing graph. icon Inputs/Outputs cNI__reportlvclass.png report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. c1dstr.png row header row header specifies a new row header

### Word Update Graph VI

Updates the data of an existing graph.

[IMAGE alt='icon' src='word-update-graph-vi.png']

#### Inputs/Outputs

| — report in is a reference to the report whose appearance, data, and printing you want to control. Use the New Report VI to generate this LabVIEW class object. row header — row header specifies a new row header to write into the graph. Leave this parameter unwired if you are updating an XY graph. column header — column header specifies a new column header to write into the graph. Leave this parameter unwired if you are updating an XY graph. graph data — graph data contains new data that the VI uses to update the graph. Microsoft Office returns an error if you plot more than 3,999 points per row or column. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. graph index (-1) — graph index specifies the index of the graph to modify. The default is -1, in which the VI modifies the last graph in the current document. Note Graphs, tables, images, ActiveX controls, and OLE objects form a collection for each document. Each object has an index value based on the order of the objects in the document. Index values begin at 0. For example, if you insert two images into the document before you insert a graph, the index value for the graph is 2. — report out is a reference to the report whose appearance, data, and printing you want to control. You can wire this output to other Report Generation VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Word Graphs and Pictures
