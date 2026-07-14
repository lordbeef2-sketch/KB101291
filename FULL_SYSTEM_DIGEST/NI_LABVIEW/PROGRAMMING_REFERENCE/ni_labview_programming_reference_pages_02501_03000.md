# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2501 ordinal=2501 -->
## Functions

Functions


   If hidden frames is TRUE, the block diagram image includes all visible subdiagrams of each
  Case, Event, and Stacked Sequence structure, followed by all hidden subdiagrams for each
  structure. If FALSE (default), the image includes only visible subdiagrams.

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•       VI —

  VI is the path to the VI whose image you want to append to the report. The default is the path to
  the VI that contains this VI as a subVI.

•      alignment (default) —

  alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
  Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

  0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
  1 LEFT
  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      ordered (repeat from higher level if nested) —

   If ordered is TRUE, the block diagram image includes all visible subdiagrams of each Case,
  Event, and Stacked Sequence structure, followed by all subdiagrams for each structure in order,
  including visible and hidden subdiagrams. If FALSE (default), the image does not repeat visible
  subdiagrams in the ordered list of subdiagrams.


                                                   © National Instruments 2501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2502 ordinal=2502 -->
## Functions

Functions


                    If Hidden frames is FALSE, the VI ignores this input.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.


2502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2503 ordinal=2503 -->
## Functions

Functions


    You can wire this output to other Report Generation VIs.

   •       VI path out —

     VI path out returns VI unchanged.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI BlockBlock DiagramDiagram toto ReportReport (refnum)(refnum)
VIVI

Creates an image of the block diagram of the VI you specify in VI and appends the
image to a report. Wire data to the VI input to determine the polymorphic instance to
use or manually select the instance.

      Note You cannot include the Append VI Block Diagram to Report VI in a
       stand-alone application.

You also can use the Get Diagram Image Scaled method to return a block diagram
image programmatically.


                                                    © National Instruments 2503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2504 ordinal=2504 -->
## Functions

Functions


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG           1                           (default)
           2          GIF

               •      hidden frames —

                    If hidden frames is TRUE, the block diagram image includes all visible subdiagrams of each
            Case, Event, and Stacked Sequence structure, followed by all hidden subdiagrams for each
              structure. If FALSE (default), the image includes only visible subdiagrams.

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is a reference to the VI whose data you want to append to the report. The default is a reference
             to the VI that contains this VI as a subVI.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT


2504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2505 ordinal=2505 -->
## Functions

Functions


  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      ordered (repeat from higher level if nested) —

   If ordered is TRUE, the block diagram image includes all visible subdiagrams of each Case,
  Event, and Stacked Sequence structure, followed by all subdiagrams for each structure in order,
  including visible and hidden subdiagrams. If FALSE (default), the image does not repeat visible
  subdiagrams in the ordered list of subdiagrams.

   If Hidden frames is FALSE, the VI ignores this input.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.


                                                   © National Instruments 2505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2506 ordinal=2506 -->
## Functions

Functions


                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI out —

             VI out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —


2506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2507 ordinal=2507 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI BlockBlock DiagramDiagram toto ReportReport (string)(string)
VIVI

Creates an image of the block diagram of the VI you specify in VI and appends the
image to a report. Wire data to the VI input to determine the polymorphic instance to
use or manually select the instance.

      Note You cannot include the Append VI Block Diagram to Report VI in a
       stand-alone application.

You also can use the Get Diagram Image Scaled method to return a block diagram
image programmatically.


Inputs/Outputs

   •     image format (jpeg) —

    image format sets the format in which to save the image.

    0        PNG
             JPEG
    1
                  (default)
    2          GIF

   •      hidden frames —

                                                    © National Instruments 2507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2508 ordinal=2508 -->
## Functions

Functions


                    If hidden frames is TRUE, the block diagram image includes all visible subdiagrams of each
            Case, Event, and Stacked Sequence structure, followed by all hidden subdiagrams for each
              structure. If FALSE (default), the image includes only visible subdiagrams.

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is the name of the VI whose data you want to append to the report. The default is the name of
            the VI that contains this VI as a subVI. The VI must be in memory.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM
           9 ABSBOTTOM

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      ordered (repeat from higher level if nested) —

                    If ordered is TRUE, the block diagram image includes all visible subdiagrams of each Case,
             Event, and Stacked Sequence structure, followed by all subdiagrams for each structure in order,
             including visible and hidden subdiagrams. If FALSE (default), the image does not repeat visible
           subdiagrams in the ordered list of subdiagrams.


2508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2509 ordinal=2509 -->
## Functions

Functions


   If Hidden frames is FALSE, the VI ignores this input.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•      report out —

  report out is a reference to the report whose appearance, data, and printing you want to control.


                                                   © National Instruments 2509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2510 ordinal=2510 -->
## Functions

Functions


           You can wire this output to other Report Generation VIs.

               •       VI name out —

             VI name out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     AppendAppend VIVI DescriptionDescription toto ReportReport

      Appends the description of the VI you specify in VI to a report. Wire data to the VI input
       to determine the polymorphic instance to use or manually select the instance.

           Note You cannot include the Append VI Description to Report VI in a stand-
              alone application.


            • Append VI Description to Report (path) VI
            • Append VI Description to Report (refnum) VI
            • Append VI Description to Report (string) VI


2510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2511 ordinal=2511 -->
## Functions

Functions

AppendAppend VIVI DescriptionDescription toto ReportReport (path)(path) VIVI

Appends the description of the VI you specify in VI to a report. Wire data to the VI input
to determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI Description to Report VI in a stand-
       alone application.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —

     VI is the path to the VI whose image you want to append to the report. The default is the path to
    the VI that contains this VI as a subVI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

    You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
    report type to Word but do not specify a bookmark, the insertion occurs at the end of the
    document.


                                                    © National Instruments 2511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2512 ordinal=2512 -->
## Functions

Functions


                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI path out —

             VI path out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

2512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2513 ordinal=2513 -->
## Functions

Functions


    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI DescriptionDescription toto ReportReport (refnum)(refnum) VIVI

Appends the description of the VI you specify in VI to a report. Wire data to the VI input
to determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI Description to Report VI in a stand-
       alone application.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —

     VI is a reference to the VI whose data you want to append to the report. The default is a reference
    to the VI that contains this VI as a subVI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •    MS Office parameters —

                                                    © National Instruments 2513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2514 ordinal=2514 -->
## Functions

Functions


        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI out —


2514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2515 ordinal=2515 -->
## Functions

Functions


     VI out returns VI unchanged.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI DescriptionDescription toto ReportReport (string)(string) VIVI

Appends the description of the VI you specify in VI to a report. Wire data to the VI input
to determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI Description to Report VI in a stand-
       alone application.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —


                                                    © National Instruments 2515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2516 ordinal=2516 -->
## Functions

Functions


             VI is the name of the VI whose data you want to append to the report. The default is the name of
            the VI that contains this VI as a subVI. The VI must be in memory.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the


2516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2517 ordinal=2517 -->
## Functions

Functions


         insertion occurs.


   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       VI name out —

     VI name out returns VI unchanged.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AppendAppend VIVI IconIcon toto ReportReport

Appends the icon of the VI you specify in VI to a report. Wire data to the VI input to
determine the polymorphic instance to use or manually select the instance.

      Note The Append VI Icon to Report VI does not work when you include it in a
       stand-alone application.


                                                    © National Instruments 2517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2518 ordinal=2518 -->
## Functions

Functions

            • Append VI Icon to Report (path) VI
            • Append VI Icon to Report (refnum) VI
            • Append VI Icon to Report (string) VI
   AppendAppend VIVI IconIcon toto ReportReport (path)(path) VIVI

      Appends the icon of the VI you specify in VI to a report. Wire data to the VI input to
      determine the polymorphic instance to use or manually select the instance.

           Note The Append VI Icon to Report VI does not work when you include it in a
              stand-alone application.


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG
           1
                           (default)
           2          GIF

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is the path to the VI whose image you want to append to the report. The default is the path to


2518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2519 ordinal=2519 -->
## Functions

Functions


  the VI that contains this VI as a subVI.

•      alignment (default) —

  alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
  Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

  0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
  1 LEFT
  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•      caption or alternative string —

  caption or alternative string is the text to display instead of the image if you view the report in a
  Web browser set to display only text.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from


                                                   © National Instruments 2519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2520 ordinal=2520 -->
## Functions

Functions


               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI path out —

             VI path out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —


2520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2521 ordinal=2521 -->
## Functions

Functions


    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI IconIcon toto ReportReport (refnum)(refnum) VIVI

Appends the icon of the VI you specify in VI to a report. Wire data to the VI input to
determine the polymorphic instance to use or manually select the instance.

      Note The Append VI Icon to Report VI does not work when you include it in a
       stand-alone application.


Inputs/Outputs

   •     image format (jpeg) —

    image format sets the format in which to save the image.

    0        PNG
             JPEG
    1
                  (default)
    2          GIF

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.


                                                    © National Instruments 2521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2522 ordinal=2522 -->
## Functions

Functions


           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is a reference to the VI whose data you want to append to the report. The default is a reference
             to the VI that contains this VI as a subVI.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM
           9 ABSBOTTOM

               •      caption or alternative string —

            caption or alternative string is the text to display instead of the image if you view the report in a
         Web browser set to display only text.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.


2522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2523 ordinal=2523 -->
## Functions

Functions


      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•      report out —

  report out is a reference to the report whose appearance, data, and printing you want to control.

  You can wire this output to other Report Generation VIs.

•       VI out —

  VI out returns VI unchanged.

•       start out (Word) —

  start out (Report Generation Toolkit) represents the index of the character at the beginning of
  the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

•     end out (Word) —

                                                   © National Instruments 2523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2524 ordinal=2524 -->
## Functions

Functions


          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   AppendAppend VIVI IconIcon toto ReportReport (string)(string) VIVI

      Appends the icon of the VI you specify in VI to a report. Wire data to the VI input to
      determine the polymorphic instance to use or manually select the instance.

           Note The Append VI Icon to Report VI does not work when you include it in a
              stand-alone application.


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG
           1
                           (default)
           2          GIF

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.


2524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2525 ordinal=2525 -->
## Functions

Functions


  Use the Create Report VI to generate this LabVIEW class object.

•       VI —

  VI is the name of the VI whose data you want to append to the report. The default is the name of
  the VI that contains this VI as a subVI. The VI must be in memory.

•      alignment (default) —

  alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
  Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

  0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
  1 LEFT
  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•      caption or alternative string —

  caption or alternative string is the text to display instead of the image if you view the report in a
  Web browser set to display only text.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.


                                                   © National Instruments 2525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2526 ordinal=2526 -->
## Functions

Functions


                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI name out —

             VI name out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

2526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2527 ordinal=2527 -->
## Functions

Functions


    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AppendAppend VIVI HierarchyHierarchy toto ReportReport

Appends the hierarchy of the VI you specify in VI to a report. Wire data to the VI input to
determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI Hierarchy to Report VI in a stand-
       alone application.


  • Append VI Hierarchy to Report (path) VI
  • Append VI Hierarchy to Report (refnum) VI
  • Append VI Hierarchy to Report (string) VI
AppendAppend VIVI HierarchyHierarchy toto ReportReport (path)(path) VIVI

Appends the hierarchy of the VI you specify in VI to a report. Wire data to the VI input to
determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI Hierarchy to Report VI in a stand-
       alone application.


                                                    © National Instruments 2527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2528 ordinal=2528 -->
## Functions

Functions


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG           1                           (default)
           2          GIF

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is the path to the VI whose image you want to append to the report. The default is the path to
            the VI that contains this VI as a subVI.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM


2528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2529 ordinal=2529 -->
## Functions

Functions


  9 ABSBOTTOM

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the


                                                   © National Instruments 2529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2530 ordinal=2530 -->
## Functions

Functions


                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI path out —

             VI path out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   AppendAppend VIVI HierarchyHierarchy toto ReportReport (refnum)(refnum) VIVI

      Appends the hierarchy of the VI you specify in VI to a report. Wire data to the VI input to
      determine the polymorphic instance to use or manually select the instance.

           Note You cannot include the Append VI Hierarchy to Report VI in a stand-
              alone application.


2530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2531 ordinal=2531 -->
## Functions

Functions


Inputs/Outputs

   •     image format (jpeg) —

    image format sets the format in which to save the image.

    0        PNG
             JPEG    1                  (default)
    2          GIF

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —

     VI is a reference to the VI whose data you want to append to the report. The default is a reference
    to the VI that contains this VI as a subVI.

   •      alignment (default) —

    alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
   Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

    0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
    1 LEFT
    2 RIGHT
    3 TOP
    4 TEXTTOP
    5 MIDDLE
    6 ABSMIDDLE
    7 BASELINE
    8 BOTTOM


                                                    © National Instruments 2531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2532 ordinal=2532 -->
## Functions

Functions


           9 ABSBOTTOM

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the


2532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2533 ordinal=2533 -->
## Functions

Functions


         insertion occurs.


   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       VI out —

     VI out returns VI unchanged.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI HierarchyHierarchy toto ReportReport (string)(string) VIVI

Appends the hierarchy of the VI you specify in VI to a report. Wire data to the VI input to
determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI Hierarchy to Report VI in a stand-
       alone application.


                                                    © National Instruments 2533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2534 ordinal=2534 -->
## Functions

Functions


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG           1                           (default)
           2          GIF

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is the name of the VI whose data you want to append to the report. The default is the name of
            the VI that contains this VI as a subVI. The VI must be in memory.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM


2534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2535 ordinal=2535 -->
## Functions

Functions


  9 ABSBOTTOM

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the


                                                   © National Instruments 2535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2536 ordinal=2536 -->
## Functions

Functions


                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI name out —

             VI name out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     AppendAppend VIVI HistoryHistory toto ReportReport

      Appends the revision history of the VI you specify in VI to a report. Wire data to the VI
       input to determine the polymorphic instance to use or manually select the instance.

           Note You cannot include the Append VI History to Report VI in a stand-alone
                application.


2536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2537 ordinal=2537 -->
## Functions

Functions

  • Append VI History to Report (path) VI
  • Append VI History to Report (refnum) VI
  • Append VI History to Report (string) VI
AppendAppend VIVI HistoryHistory toto ReportReport (path)(path) VIVI

Appends the revision history of the VI you specify in VI to a report. Wire data to the VI
input to determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI History to Report VI in a stand-alone
        application.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —

     VI is the path to the VI whose image you want to append to the report. The default is the path to
    the VI that contains this VI as a subVI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.


                                                    © National Instruments 2537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2538 ordinal=2538 -->
## Functions

Functions


           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI path out —

             VI path out returns VI unchanged.

               •       start out (Word) —


2538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2539 ordinal=2539 -->
## Functions

Functions


     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI HistoryHistory toto ReportReport (refnum)(refnum) VIVI

Appends the revision history of the VI you specify in VI to a report. Wire data to the VI
input to determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI History to Report VI in a stand-alone
        application.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —

     VI is a reference to the VI whose data you want to append to the report. The default is a reference
    to the VI that contains this VI as a subVI.

   •       error in (no error) —

                                                    © National Instruments 2539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2540 ordinal=2540 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.


2540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2541 ordinal=2541 -->
## Functions

Functions


    You can wire this output to other Report Generation VIs.

   •       VI out —

     VI out returns VI unchanged.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI HistoryHistory toto ReportReport (string)(string) VIVI

Appends the revision history of the VI you specify in VI to a report. Wire data to the VI
input to determine the polymorphic instance to use or manually select the instance.

      Note You cannot include the Append VI History to Report VI in a stand-alone
        application.


Inputs/Outputs

   •      report in —


                                                    © National Instruments 2541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2542 ordinal=2542 -->
## Functions

Functions


            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is the name of the VI whose data you want to append to the report. The default is the name of
            the VI that contains this VI as a subVI. The VI must be in memory.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion


2542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2543 ordinal=2543 -->
## Functions

Functions


         occurs.

         •     bookmark (Word) —

       bookmark contains the name of the bookmark in a Word document from which the
         insertion occurs.


   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       VI name out —

     VI name out returns VI unchanged.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AppendAppend VIVI ListList ofof ControlsControls toto ReportReport

Appends a list of controls and indicators of the VI you specify in VI to a report. Wire
data to the VI input to determine the polymorphic instance to use or manually select
the instance.

      Note You cannot include the Append VI List of Controls to Report VI in a


                                                    © National Instruments 2543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2544 ordinal=2544 -->
## Functions

Functions


              stand-alone application.


            • Append VI List of Controls to Report (path) VI
            • Append VI List of Controls to Report (refnum) VI
            • Append VI List of Controls to Report (string) VI
   AppendAppend VIVI ListList ofof ControlsControls toto ReportReport (path)(path) VIVI

      Appends a list of controls and indicators of the VI you specify in VI to a report. Wire
       data to the VI input to determine the polymorphic instance to use or manually select
       the instance.

           Note You cannot include the Append VI List of Controls to Report VI in a
              stand-alone application.


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
           1         JPEG


2544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2545 ordinal=2545 -->
## Functions

Functions


                (default)
  2          GIF

•      include only controls in con pane? —

   If include only controls in con pane? is TRUE, the report includes only connected controls and
  indicators. If FALSE (default), the report includes all controls and indicators.

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•       VI —

  VI is the path to the VI whose image you want to append to the report. The default is the path to
  the VI that contains this VI as a subVI.

•      alignment (default) —

  alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
  Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

  0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
  1 LEFT
  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      include control descriptions? —


                                                   © National Instruments 2545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2546 ordinal=2546 -->
## Functions

Functions


                    If include control descriptions? is TRUE, the report includes control and indicator descriptions.
          The default is FALSE.

               •      include control data types? —

                    If include control data types? is TRUE, the report includes control and indicator data types. The
             default is FALSE.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the


2546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2547 ordinal=2547 -->
## Functions

Functions


         insertion occurs.


   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       VI path out —

     VI path out returns VI unchanged.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI ListList ofof ControlsControls toto ReportReport (refnum)(refnum)
VIVI

Appends a list of controls and indicators of the VI you specify in VI to a report. Wire
data to the VI input to determine the polymorphic instance to use or manually select
the instance.

      Note You cannot include the Append VI List of Controls to Report VI in a
       stand-alone application.


                                                    © National Instruments 2547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2548 ordinal=2548 -->
## Functions

Functions


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG           1
                           (default)
           2          GIF

               •      include only controls in con pane? —

                    If include only controls in con pane? is TRUE, the report includes only connected controls and
              indicators. If FALSE (default), the report includes all controls and indicators.

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is a reference to the VI whose data you want to append to the report. The default is a reference
             to the VI that contains this VI as a subVI.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT


2548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2549 ordinal=2549 -->
## Functions

Functions


  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      include control descriptions? —

   If include control descriptions? is TRUE, the report includes control and indicator descriptions.
  The default is FALSE.

•      include control data types? —

   If include control data types? is TRUE, the report includes control and indicator data types. The
  default is FALSE.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.


                                                   © National Instruments 2549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2550 ordinal=2550 -->
## Functions

Functions


                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI out —

             VI out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —


2550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2551 ordinal=2551 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI ListList ofof ControlsControls toto ReportReport (string)(string)
VIVI

Appends a list of controls and indicators of the VI you specify in VI to a report. Wire
data to the VI input to determine the polymorphic instance to use or manually select
the instance.

      Note You cannot include the Append VI List of Controls to Report VI in a
       stand-alone application.


Inputs/Outputs

   •     image format (jpeg) —

    image format sets the format in which to save the image.

    0        PNG
             JPEG
    1
                  (default)
    2          GIF

   •      include only controls in con pane? —

       If include only controls in con pane? is TRUE, the report includes only connected controls and


                                                    © National Instruments 2551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2552 ordinal=2552 -->
## Functions

Functions


              indicators. If FALSE (default), the report includes all controls and indicators.

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is the name of the VI whose data you want to append to the report. The default is the name of
            the VI that contains this VI as a subVI. The VI must be in memory.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM
           9 ABSBOTTOM

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      include control descriptions? —

                    If include control descriptions? is TRUE, the report includes control and indicator descriptions.
          The default is FALSE.

               •      include control data types? —

                    If include control data types? is TRUE, the report includes control and indicator data types. The
             default is FALSE.


2552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2553 ordinal=2553 -->
## Functions

Functions

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•      report out —

  report out is a reference to the report whose appearance, data, and printing you want to control.

  You can wire this output to other Report Generation VIs.

•       VI name out —


                                                   © National Instruments 2553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2554 ordinal=2554 -->
## Functions

Functions


             VI name out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     AppendAppend VIVI ListList ofof SubVIsSubVIs toto ReportReport

      Appends a list of subVIs of the VI you specify in VI to a report. The list includes subVI
        icons, names, and paths. Wire data to the VI input to determine the polymorphic
       instance to use or manually select the instance.

           Note You cannot include the Append VI List of SubVIs to Report VI in a stand-
              alone application.


            • Append VI List of SubVIs to Report (path) VI
            • Append VI List of SubVIs to Report (refnum) VI
            • Append VI List of SubVIs to Report (string) VI
   AppendAppend VIVI ListList ofof SubVIsSubVIs toto ReportReport (path)(path) VIVI

      Appends a list of subVIs of the VI you specify in VI to a report. The list includes subVI
        icons, names, and paths. Wire data to the VI input to determine the polymorphic


2554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2555 ordinal=2555 -->
## Functions

Functions

instance to use or manually select the instance.

      Note You cannot include the Append VI List of SubVIs to Report VI in a stand-
       alone application.


Inputs/Outputs

   •     image format (jpeg) —

    image format sets the format in which to save the image.

    0        PNG
             JPEG    1                  (default)
    2          GIF

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —

     VI is the path to the VI whose image you want to append to the report. The default is the path to
    the VI that contains this VI as a subVI.

   •      alignment (default) —

    alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
   Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

    0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.


                                                    © National Instruments 2555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2556 ordinal=2556 -->
## Functions

Functions


           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM
           9 ABSBOTTOM

               •      include Express VI configuration information (F) —

            include Express VI configuration information specifies whether the report includes
             configuration information for any Express VIs on the block diagram. The default is FALSE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —


2556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2557 ordinal=2557 -->
## Functions

Functions


         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•      report out —

  report out is a reference to the report whose appearance, data, and printing you want to control.

  You can wire this output to other Report Generation VIs.

•       VI path out —

  VI path out returns VI unchanged.

•       start out (Word) —

  start out (Report Generation Toolkit) represents the index of the character at the beginning of
  the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

•     end out (Word) —

  end out (Report Generation Toolkit) represents the index of the character at the end of the text
  inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2558 ordinal=2558 -->
## Functions

Functions

   AppendAppend VIVI ListList ofof SubVIsSubVIs toto ReportReport (refnum)(refnum)
    VIVI

      Appends a list of subVIs of the VI you specify in VI to a report. The list includes subVI
        icons, names, and paths. Wire data to the VI input to determine the polymorphic
       instance to use or manually select the instance.

           Note You cannot include the Append VI List of SubVIs to Report VI in a stand-
              alone application.


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG
           1
                           (default)
           2          GIF

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       VI —

             VI is a reference to the VI whose data you want to append to the report. The default is a reference
             to the VI that contains this VI as a subVI.


2558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2559 ordinal=2559 -->
## Functions

Functions

•      alignment (default) —

  alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
  Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

  0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
  1 LEFT
  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•      include Express VI configuration information (F) —

  include Express VI configuration information specifies whether the report includes
  configuration information for any Express VIs on the block diagram. The default is FALSE.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)


                                                   © National Instruments 2559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2560 ordinal=2560 -->
## Functions

Functions


               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       VI out —

             VI out returns VI unchanged.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

2560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2561 ordinal=2561 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

AppendAppend VIVI ListList ofof SubVIsSubVIs toto ReportReport (string)(string) VIVI

Appends a list of subVIs of the VI you specify in VI to a report. The list includes subVI
icons, names, and paths. Wire data to the VI input to determine the polymorphic
instance to use or manually select the instance.

      Note You cannot include the Append VI List of SubVIs to Report VI in a stand-
       alone application.


Inputs/Outputs

   •     image format (jpeg) —

    image format sets the format in which to save the image.

    0        PNG
             JPEG
    1
                  (default)
    2          GIF

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       VI —


                                                    © National Instruments 2561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2562 ordinal=2562 -->
## Functions

Functions


             VI is the name of the VI whose data you want to append to the report. The default is the name of
            the VI that contains this VI as a subVI. The VI must be in memory.

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM
           9 ABSBOTTOM

               •      include Express VI configuration information (F) —

            include Express VI configuration information specifies whether the report includes
             configuration information for any Express VIs on the block diagram. The default is FALSE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —


2562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2563 ordinal=2563 -->
## Functions

Functions


       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•      report out —

  report out is a reference to the report whose appearance, data, and printing you want to control.

  You can wire this output to other Report Generation VIs.

•       VI name out —

  VI name out returns VI unchanged.

•       start out (Word) —

  start out (Report Generation Toolkit) represents the index of the character at the beginning of
  the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

•     end out (Word) —


                                                   © National Instruments 2563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2564 ordinal=2564 -->
## Functions

Functions


          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      CreateCreate ReportReport

       Creates a new report.

           If you do not use the Create Easy Text Report VI, to create a report, you must use this VI.


      Inputs/Outputs

               •     window state (normal) —

          window state (Report Generation Toolkit) sets the Microsoft Word or Excel window to display as
            normal, minimized, or maximized. The VI ignores this input for HTML reports.

           0       maximized
           1        minimized
                   normal
           2
                         (default)
           3       no change

               •      display alerts? (F) —

            display alerts? (Report Generation Toolkit) determines whether prompts and alerts appear in
             Microsoft Word or Excel. The default is FALSE, which disables alerts. The VI ignores this input for
         HTML reports.

               •      report type —

2564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2565 ordinal=2565 -->
## Functions

Functions


  report type is the type of report you want to create.

   HTML
  0 —Creates an HTML report and returns a reference to it in report out so you can use other
   Report Generation VIs to customize, save, or print the report.
   Word
  1 (Report Generation Toolkit)—Creates a report in Word and returns a reference to it in report
   out so you can use other Report Generation VIs to customize, save, or print the report.
    Excel
  2 (Report Generation Toolkit)—Creates a report in Excel and returns a reference to it in report out
   so you can use other Report Generation VIs to customize, save, or print the report.

•      template (empty) —

  template (Report Generation Toolkit) specifies a path to a Word document or Excel worksheet
  that acts as a report template. Enter the path to an existing Word document or Excel worksheet
  to open and edit an existing report for a template.

  The VI ignores this input for HTML reports.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     machine name (empty) —

  machine name (Report Generation Toolkit) specifies a computer from which Microsoft Word or
  Excel runs remotely. The VI ignores this input for HTML reports.

•      report out —

  report out is a reference to the report whose appearance, data, and printing you want to control.

  You can wire this output to other Report Generation VIs.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2566 ordinal=2566 -->
## Functions

Functions

      PrintPrint ReportReport

       Prints a report to a designated printer or to the default printer on the computer.

           If you use this VI to print an HTML report, the computer printing the report must have
       Internet Explorer installed.

           Note If you use this VI to print a Microsoft Word report and you assign a
                printer to the printer name input other than the default system printer,
               Microsoft Word resets the default system printer to the printer you assigned
               to the printer name input.


      Inputs/Outputs

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       printer name (default) —

             printer name is the name of the printer to which you want to print the report.

                    If you wire a printer name, that printer must be configured for use with the computer from which
           you want to print the report. If you do not wire a printer name, the VI uses the default printer for
            the computer. The computer from which you want to print must have a default printer.

                    If you print an HTML report, the VI ignores this input and uses the default printer for Internet
             Explorer.

               •     number of copies (1) —

          number of copies specifies how many copies of the report you want to print.

                    If you do not specify a number, LabVIEW prints one copy.


2566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2567 ordinal=2567 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SaveSave ReportReport toto FileFile

Saves an HTML report to the file specified in report file path.

This VI also saves Microsoft Word and Excel reports.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •      report file path —

    report file path specifies the path where you want to save the report and the name of the report.

       If the path is empty or invalid, the VI returns an error.

   •     prompt to replace? (F) —


                                                    © National Instruments 2567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2568 ordinal=2568 -->
## Functions

Functions


          prompt to replace? determines whether the VI displays a dialog box if you specify an existing
            filename in report file path. The default is FALSE, which overwrites existing files without
            prompting.

             This input applies only for HTML reports.

               •      password ("") —

           password (Report Generation Toolkit) creates a read-only report with password protection. You
          must enter the password to modify the report.

          The VI ignores this input for HTML reports.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     DisposeDispose ReportReport

       Closes the report and releases its interface, which saves memory.

        After the VI runs, you cannot perform further operations on the report. The Dispose
      Report VI should be the last VI you use when you create a report.


2568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2569 ordinal=2569 -->
## Functions

Functions

Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •      wait until printing completed? (T) —

    wait until printing completed? (Report Generation Toolkit) specifies whether the VI closes the
    report if printing is still in progress. The default is TRUE, which specifies to wait to close the
    report until the report prints.

    The VI ignores this input for HTML, standard, and Excel reports.

   •      save changes? (F) —

    save changes? (Report Generation Toolkit) specifies whether the VI saves changes to the report.
    The default is FALSE, which specifies to close the report without saving any changes.

    The VI ignores this input if the Close Report input is FALSE. The VI ignores this input for HTML
     reports.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      close report? (T) —

    close report? (Report Generation Toolkit) specifies whether the VI closes the report. The default
      is TRUE, which specifies to close the report file. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

HTMLHTML ReportsReports OnlyOnly

Use the HTML Reports Only VIs to manipulate HTML reports you create in LabVIEW.

The VIs on this palette can return report generation error codes.


                                                    © National Instruments 2569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2570 ordinal=2570 -->
## Functions

Functions


         Palette Object      Description

       Append Horizontal                            Creates a horizontal rule in an HTML report.         Line to Report

       Append Hypertext
         Link Anchor to      Creates and adds a hypertext link anchor to a HTML report.
        Report

       Append User
        Formatted HTML    Inserts text that is not preformatted by LabVIEW in the HTML report.
         to Report

                             Displays an HTML report in the default Web browser. Wire data to the report in       Open HTML Report                            input to determine the polymorphic instance to use or manually select the          in Browser
                              instance.


     AppendAppend HorizontalHorizontal LineLine toto ReportReport

       Creates a horizontal rule in an HTML report.

       This VI also creates a horizontal rule in a Microsoft Word or Excel report.


      Inputs/Outputs

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or


2570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2571 ordinal=2571 -->
## Functions

Functions


  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•       size (default) —

  size sets the height of the horizontal rule.

  The default is 1.

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.


                                                   © National Instruments 2571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2572 ordinal=2572 -->
## Functions

Functions


           Use the Create Report VI to generate this LabVIEW class object.

               •       align (default) —

             align aligns the rule on the report.

           0 (default)—The VI does not add an ALIGN attribute to the <HR> tag.
           1 LEFT
           2 CENTER
           3 RIGHT

               •      width (100=default) —

           width sets the width of the horizontal rule, either in pixels or as a percentage of the page,
           depending on the value you wire to width units.

          The default is 100.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      width units —

           width units determines whether the width you specify is in pixels or a percentage of the page.

           0         Pixels
                     Percentage           1                        (default)

               •     noshade (F) —

          noshade indicates whether to create a solid (TRUE) or three-dimensional (FALSE) horizontal
              rule.

                    If TRUE, the VI adds the noshade attribute to the horizontal rule tag. The default is FALSE.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.


2572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2573 ordinal=2573 -->
## Functions

Functions


    You can wire this output to other Report Generation VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Report Generation\HTML Reports\HTML
   Report.vi

AppendAppend HypertextHypertext LinkLink AnchorAnchor toto ReportReport

Creates and adds a hypertext link anchor to a HTML report.

This VI also creates and adds a hypertext link anchor to a Microsoft Word or Excel
report.


Inputs/Outputs

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

    You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
    report type to Word but do not specify a bookmark, the insertion occurs at the end of the
    document.

         •      position (excel) —


                                                    © National Instruments 2573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2574 ordinal=2574 -->
## Functions

Functions


                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •     URL of link - href —

         URL of link - href is the URL of the website or document that you want to link to from the HTML
             report.

           Use forward slashes (/) to separate directory and filenames in URLs. For example, if you want to
              link to report.html in the factory directory on the website www.mycompany.com, use a
          URL of http://www.mycompany.com/factory/report.html.

                    If you link to documents or sites on a local computer, the links might not work if you post the
             report on the Web. If you use relative paths in the links and the documents or sites move, the


2574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2575 ordinal=2575 -->
## Functions

Functions


     links do not work.

   •       link text —

     link text is the text you want to appear as a link in the report.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AppendAppend UserUser FormattedFormatted HTMLHTML toto ReportReport

Inserts text that is not preformatted by LabVIEW in the HTML report.

Use this VI to insert tags not currently supplied by the Report Generation VIs.


                                                    © National Instruments 2575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2576 ordinal=2576 -->
## Functions

Functions

      Inputs/Outputs

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •     HTML text —

         HTML text is the text LabVIEW adds to the HTML document without extra tags. This input allows
            the use of tags not currently supplied by the Report Generation VIs.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     OpenOpen HTMLHTML ReportReport inin BrowserBrowser

       Displays an HTML report in the default Web browser. Wire data to the report in input to
      determine the polymorphic instance to use or manually select the instance.

           If you wire a URL or path that contains a space character to this VI, the VI encodes the
      space as %20 before displaying the URL or HTML file in the Web browser.


            • Open HTML Report in Browser (Refnum) VI
            • Open HTML Report in Browser (Path) VI
            • Open HTML Report in Browser (String) VI

2576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2577 ordinal=2577 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Report Generation\HTML Reports\HTML
   Report.vi
OpenOpen HTMLHTML ReportReport inin BrowserBrowser (Refnum)(Refnum) VIVI

Displays an HTML report in the default Web browser. Wire data to the report in input to
determine the polymorphic instance to use or manually select the instance.

If you wire a URL or path that contains a space character to this VI, the VI encodes the
space as %20 before displaying the URL or HTML file in the Web browser.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •      temporary HTML file created —

    temporary HTML file created is the path in which the VI saved the temporary HTML file


                                                    © National Instruments 2577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2578 ordinal=2578 -->
## Functions

Functions


            containing the report before displaying the HTML file in the Web browser.

              After the VI runs, you can delete the temporary HTML file to free disk space.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Report Generation\HTML Reports\HTML
        Report.vi
   OpenOpen HTMLHTML ReportReport inin BrowserBrowser (Path)(Path) VIVI

       Displays an HTML report in the default Web browser. Wire data to the report in input to
      determine the polymorphic instance to use or manually select the instance.

           If you wire a URL or path that contains a space character to this VI, the VI encodes the
      space as %20 before displaying the URL or HTML file in the Web browser.


      Inputs/Outputs

               •      path —

           path is the path to the HTML file you want to display in the default Web browser.

                    If the path is relative, the VI interprets the path as relative to the application directory, such as
            the labview directory or the directory containing the stand-alone application.

               •       error in (no error) —


2578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2579 ordinal=2579 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      path out —

    path out returns path unchanged.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Report Generation\HTML Reports\HTML
   Report.vi
OpenOpen HTMLHTML ReportReport inin BrowserBrowser (String)(String) VIVI

Displays an HTML report in the default Web browser. Wire data to the report in input to
determine the polymorphic instance to use or manually select the instance.

If you wire a URL or path that contains a space character to this VI, the VI encodes the
space as %20 before displaying the URL or HTML file in the Web browser.


Inputs/Outputs

   •     URL —

   URL is the URL you want to display in the default Web browser.

    For example, wire http://www.site.com/report.html to this input to display the HTML
      file report.html on the Web Server www.site.com in the browser.


                                                    © National Instruments 2579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2580 ordinal=2580 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     URL out —

         URL out is the URL displayed in the Web browser.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Report Generation\HTML Reports\HTML
        Report.vi

      SetSet ReportReport FontFont

       Sets the font properties of the report, including those in the headers and footers.


      Inputs/Outputs

               •      font settings source (VI Inputs) —

            font settings source (Report Generation Toolkit) specifies the way in which you want to select
             font settings.

          The VI ignores this input for HTML reports.


2580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2581 ordinal=2581 -->
## Functions

Functions


    VI Inputs (default)—The VI uses the values you set in the font settings input. If you do not wire  0
    font settings, the VI uses the default font settings of the report class.
  1 Font Dialog Box—A dialog box appears that you can use to select font settings.

•       text color (unchanged) —

  text color is the color of the text in the report.

  You can wire a color box constant to this input. The default is T, which leaves the text
  unchanged.

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•       text options —

  text options specifies how the text appears in the report.

      •        Italic —

        Italic determines whether subsequent text appears in italics in the report. The default is
     Italic Unchanged.

      0       Italic Unchanged
      1       Italic On
      2       Italic Off

      •       Strike Through —

       Strike Through determines whether subsequent text appears with a strikethrough effect in
      the report. The default is Strike Through Unchanged.

      0   Strike Through Unchanged
      1   Strike Through On
      2   Strike Through Off

      •      Underline —


                                                   © National Instruments 2581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2582 ordinal=2582 -->
## Functions

Functions


                Underline determines whether subsequent text appears underlined in the report. The
                 default is Underline Unchanged.

               0    Underline Unchanged
               1    Underline On
               2    Underline Off

                     •      Bold —

               Bold determines whether subsequent text appears bold in the report. The default is Bold
             Unchanged.

               0     Bold Unchanged
               1     Bold On
               2     Bold Off


               •      font settings —

            font settings indicates the font settings a report uses.

                     •      Charset (-1) —

                charset is the character set to use for report text. The default is -1.

                     •      Weight (-1) —

               weight is the thickness of the font. The default is -1.

                     •     Name —

            name is the font name.

                     •       Size —

                  size is the font size.


               •       error in (no error) —


2582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2583 ordinal=2583 -->
## Functions

Functions


  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      report out —

  report out is a reference to the report whose appearance, data, and printing you want to control.

  You can wire this output to other Report Generation VIs.

•      font out —

  font out (Report Generation Toolkit) contains the font settings the VI uses for formatting, which
  you can use in other VIs. The values are valid for Microsoft Office reports only.

      •      font name —

      font name indicates the name of the font used, such as Times New Roman.

      •      font size —

      font size indicates the size at which the font appears, in points.

      •      bold —

      bold indicates whether the text is in bold.

      •        italic —

        italic indicates whether the text is in italics.

      •      underline —

      underline indicates whether the text is underlined.

      •       strike through —

       strike through indicates whether the text is struck through.

      •      font color —

      font color indicates the color of the text.


•       error out —


                                                   © National Instruments 2583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2584 ordinal=2584 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      The available properties include italic, bold, strikethrough, underline, color, font
      name, font size, character set, and weight. The font you specify in the VI becomes the
       default font for the report.

           If you use the Set Report Font VI to set a font in an HTML report, the <font> tag is used
       to set the font. This tag remains valid until the end of the file. There is no </font> used.

      The table generated by the Append Table to Report VI does not use the font defined by
       the Set Report Font VI. The header and body texts of the table have different default
        fonts. You can use HTML tags to configure the text font for each cell of the table. Refer
       to the example at ni.com for more information about how to generate tables with
        different fonts.

     AppendAppend ReportReport TextText

      Appends text to the selected report. Wire data to the text input to determine the
      polymorphic instance to use or manually select the instance.

      The selected report is the one you wire to report in. You can append the text to the
       current position of the cursor in the report or on a new line.


            • Append Report Text (str wrap) VI
            • Append Report Text (num wrap) VI

     AppendAppend ReportReport TextText (str(str wrap)wrap) VIVI

      Appends text to the selected report. Wire data to the text input to determine the
      polymorphic instance to use or manually select the instance.

      The selected report is the one you wire to report in. You can append the text to the
       current position of the cursor in the report or on a new line.

2584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2585 ordinal=2585 -->
## Functions

Functions


Inputs/Outputs

   •      format string (%.3f) —

    format string specifies the number formatting to use when LabVIEW converts the numbers to
     characters. Use format string when you wire numeric data to the text input.

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

    You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
    report type to Word but do not specify a bookmark, the insertion occurs at the end of the
    document.

         •      position (excel) —

         position contains the row and column coordinates of the point in an Excel worksheet from
        which the insertion occurs.

      Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
        correspond to cell A1.

                •     row —

           rows specifies the row index.

                •     column —

           columns specifies the column index.


         •     name (excel) —


                                                    © National Instruments 2585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2586 ordinal=2586 -->
## Functions

Functions


            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       text —

             text is the information you want to include in the report.

               •     append on new line? (F) —

          append on new line? appends the information on a new line in the report when set to TRUE.

          The default is FALSE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text


2586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2587 ordinal=2587 -->
## Functions

Functions


    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AppendAppend ReportReport TextText (num(num wrap)wrap) VIVI

Appends text to the selected report. Wire data to the text input to determine the
polymorphic instance to use or manually select the instance.

The selected report is the one you wire to report in. You can append the text to the
current position of the cursor in the report or on a new line.


Inputs/Outputs

   •      format string (%.3f) —

    format string specifies the number formatting to use when LabVIEW converts the numbers to
     characters. Use format string when you wire numeric data to the text input.

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

    You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
    report type to Word but do not specify a bookmark, the insertion occurs at the end of the
    document.

         •      position (excel) —


                                                    © National Instruments 2587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2588 ordinal=2588 -->
## Functions

Functions


                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       text —

             text is the information you want to include in the report. Use the format string input to format
            the numeric data.

               •     append on new line? (F) —

          append on new line? appends the information on a new line in the report when set to TRUE.

          The default is FALSE.

               •       error in (no error) —

2588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2589 ordinal=2589 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       start out (Word) —

     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AppendAppend TableTable toto ReportReport

Appends a 2D array to a report as a table with the given column width. Wire data to the
text data input to determine the polymorphic instance to use or manually select the
instance.


  • Append Text Table to Report (wrap) VI
  • Append Numeric Table to Report (wrap) VI

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 2589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2590 ordinal=2590 -->
## Functions

Functions

            • labview\examples\reports\TextReportExample.llb\Text
        Report Example.vi

     AppendAppend TextText TableTable toto ReportReport (wrap)(wrap) VIVI

      Appends a 2D array to a report as a table with the given column width. Wire data to the
       text data input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

                     •      position (excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (excel) —


2590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2591 ordinal=2591 -->
## Functions

Functions


     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•     measurement system for column width (Default) —

  measurement system for column width determines whether the value you enter in column
  width is in inches or centimeters.

•     column width (1) —

  column width defines the width of each column in the report table.

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•     column headers —

  column headers determines how each column is labeled in the table.

•     row headers —

  row headers determines how each row is labeled in the table.

•       text data —

  text data is the information you want to be printed in tabular form.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      separate page? (NO) —

  separate page? specifies whether to place the table on a new page of the report. The default is


                                                   © National Instruments 2591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2592 ordinal=2592 -->
## Functions

Functions


            FALSE.

               •     show grid lines (YES) —

          show grid lines specifies whether to display the grid lines of the table. The default is TRUE.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

               •      range (wd) - start (xl) —

           range (wd) - start (xl) (Report Generation Toolkit) indicates the place where the VI inserts the
              table.

                     •       start (wd) - row (xl) —

                  start (wd) - row (xl) is the point where the table begins.

                     •     end (wd) - col (xl) —

              end (wd) - col (xl) is the point where the table ends.


               •     end (xl) —

          end (xl) (Report Generation Toolkit) indicates the last cell in the Excel worksheet where the VI
              inserts the table.

                     •     row (xl) —

             row (xl) is the row number where the table ends.

                     •       col (xl) —

                  col (xl) is the column number where the table ends.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


2592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2593 ordinal=2593 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\reports\TextReportExample.llb\Text
   Report Example.vi

AppendAppend NumericNumeric TableTable toto ReportReport (wrap)(wrap) VIVI

Appends a 2D array to a report as a table with the given column width. Wire data to the
text data input to determine the polymorphic instance to use or manually select the
instance.


Inputs/Outputs

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

    You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
    report type to Word but do not specify a bookmark, the insertion occurs at the end of the
    document.

         •      position (excel) —

         position contains the row and column coordinates of the point in an Excel worksheet from
        which the insertion occurs.


                                                    © National Instruments 2593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2594 ordinal=2594 -->
## Functions

Functions


            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •     measurement system for column width (Default) —

          measurement system for column width determines whether the value you enter in column
           width is in inches or centimeters.

          The VI ignores this parameter for HTML reports.

           0 US—Sets the column width in inches.
           1 Metric—Sets the column width in centimeters.
           2 Default (default)—Sets the column width in the measurement system set up on the computer.

               •     column width (1) —

          column width defines the width of each column in the report table.

          The value you enter must be in inches or centimeters, depending on the settings you enter in
          measurement system for column width. The default is 1. For HTML reports, the VI multiplies the
            value by 100 to set the column width in pixels.


2594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2595 ordinal=2595 -->
## Functions

Functions


        Note If you set column width to a large value and send several columns of data to
           the VI, the VI automatically resizes the column width to fit the width of the report on a
            single page. If you are using a template and do not want the column width to vary,
          use the value -1.

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•     column headers —

  column headers determines how each column is labeled in the table.

•     row headers —

  row headers determines how each row is labeled in the table.

•      numerical data —

  numerical data is the numerical information included in the table.

  The information must be a 2D array.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      format string (%.3f) —

  format string specifies the number formatting to use when converting the numbers to
  characters. The default is %.3f.

  Use the format string syntax.

•      separate page? —

  separate page? specifies whether to place the table on a new page of the report. The default is
  FALSE.

•     show grid lines —


                                                   © National Instruments 2595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2596 ordinal=2596 -->
## Functions

Functions


          show grid lines specifies whether to display the grid lines of the table. The default is TRUE.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •      range (wd) - start (xl) —

           range (wd) - start (xl) (Report Generation Toolkit) indicates the place where the VI inserts the
              table.

                     •       start (wd) - row (xl) —

                  start (wd) - row (xl) is the point where the table begins.

                     •     end (wd) - col (xl) —

              end (wd) - col (xl) is the point where the table ends.


               •     end (xl) —

          end (xl) (Report Generation Toolkit) indicates the last cell in the Excel worksheet where the VI
              inserts the table.

                     •     row (xl) —

             row (xl) is the row number where the table ends.

                     •       col (xl) —

                  col (xl) is the column number where the table ends.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


2596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2597 ordinal=2597 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\reports\TextReportExample.llb\Text
   Report Example.vi

AppendAppend ListList toto ReportReport

Adds a list of elements to the report.


Inputs/Outputs

   •      unordered item type (default) —

    unordered item type determines the symbol used to denote a list item in an unordered list. You
    can specify a symbol only if the report is HTML-based. The default for HTML-based reports is a
     bullet.

    0            (default)
    1           disc
    2          square
    3             circle

   •      ordered item type (default) —

    ordered item type determines how the ordered list appears, numerical or alphabetical. The
     default is arabic numerals.

    0      (default)
    1      arabic numerals


                                                    © National Instruments 2597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2598 ordinal=2598 -->
## Functions

Functions


           2     lower alpha
           3     upper alpha

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •         list elements —

                 list elements are the items you want to include in the list.

               •         list type (ordered) —

                 list type specifies whether the list appears ordered or unordered in the report.

           0 ordered (default)—Presents the list as numerical or alphabetical.
            unordered—If the report is HTML-based and you select unordered, you can choose an item           1
               indicator.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      ordered start (1) —

           ordered start determines the number or letter the list starts with. Enter the number or the letter
             that corresponds to the number with which you want to start. For example, A equals 1, B equals
               2, or a equals 1, b equals 2. The default is 1.

               •     bookmark (Word) —

          bookmark (Report Generation Toolkit) contains the name of the bookmark in a Microsoft Word
          document from which the insertion occurs. The VI ignores this input for HTML reports.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       start out (Word) —


2598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2599 ordinal=2599 -->
## Functions

Functions


     start out (Report Generation Toolkit) represents the index of the character at the beginning of
    the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •     end out (Word) —

    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReportReport LayoutLayout

Use the Report Layout VIs to manipulate the layout of reports you create in LabVIEW.

The VIs on this palette can return report generation error codes.


 Palette Object         Description

 Set Report Margins     Sets the margins of the specified report.


 Set Report            Determines whether the report is printed in landscape or portrait
 Orientation             orientation.


 New Report Page      Creates a page break within the report.


 New Report Line        Starts a new line in the report.


 Set Report Header
                       Sets the text of the report header.
 Text


                                                    © National Instruments 2599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2600 ordinal=2600 -->
## Functions

Functions


         Palette Object         Description

         Set Report Footer Text  Sets the text of the report footer.


      SetSet ReportReport MarginsMargins

       Sets the margins of the specified report.


      Inputs/Outputs

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •      margins (1.00) —

           margins sets the size of the page margins. The default is 1.00 for each margin.

                    If the margins are smaller than the minimum margins for the printer, the VI returns an error.

                     •      top —

               top sets the distance in inches or centimeters between the top of the page and the top of
                the content on the page.

                     •        left —

                     left sets the distance in inches or centimeters between the left edge of the page and the left
               edge of the content on the page.

                     •       right —

                  right sets the distance in inches or centimeters between the right edge of the page and the


2600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2601 ordinal=2601 -->
## Functions

Functions


          right edge of the content on the page.

         •     bottom —

       bottom sets the distance in inches or centimeters between the bottom of the page and the
       bottom of the content on the page.


   •     measurement system (default) —

    measurement system sets the units of measurement for the margins.

    0 Default—Sets the margins in the measurement system configured on the computer.
    1 US—Sets the margins in inches.
    2 Metric—Sets the margins in centimeters.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •      page width (Word) —

    page width (Report Generation Toolkit) reports the width of the page after the VI has set the
    margins. The VI sets the margins in the units of measurement specified in measurement system.
    The VI ignores this input for HTML, standard, or Excel reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SetSet ReportReport OrientationOrientation

Determines whether the report is printed in landscape or portrait orientation.


                                                    © National Instruments 2601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2602 ordinal=2602 -->
## Functions

Functions

      You cannot use this VI with HTML reports.


      Inputs/Outputs

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       orientation (portrait) —

             orientation (Windows) specifies how the report appears when it prints.

           0 Portrait (default)—Prints the report so the short edge of the paper is the top of the page.
           1 Landscape—Prints the report so the long edge of the paper is the top of the page.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     NewNew ReportReport PagePage

       Creates a page break within the report.


2602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2603 ordinal=2603 -->
## Functions

Functions


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

    You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
    report type to Word but do not specify a bookmark, the insertion occurs at the end of the
    document.

         •      position (Excel) —

         position contains the row and column coordinates of the point in an Excel worksheet from
        which the insertion occurs.

      Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
        correspond to cell A1.

                •     row —

           rows specifies the row index.

                •     column —

           columns specifies the column index.


         •     name (Excel) —

      name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
         occurs.

         •     bookmark (Word) —


                                                    © National Instruments 2603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2604 ordinal=2604 -->
## Functions

Functions


             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     NewNew ReportReport LineLine

        Starts a new line in the report.

       This VI has no affect on Excel reports.


      Inputs/Outputs

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •     number of lines (1) —

          number of lines specifies how many lines the VI adds to the report. The default is 1.


2604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2605 ordinal=2605 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SetSet ReportReport HeaderHeader TextText

Sets the text of the report header.

Header text for Microsoft Excel reports appears only when you print the report.

Use tokens with this VI to generate information in the headers. For example, you can
insert a time stamp in the headers of the report.

You cannot use tokens with Microsoft Word and Excel reports.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •        left header text —

                                                    © National Instruments 2605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2606 ordinal=2606 -->
## Functions

Functions


               left header text is the information you want to appear in the left side of the header.

               •      center header text —

            center header text is the information you want to appear in the center portion of the header.

               •       right header text —

             right header text is the information you want to appear in the right side of the header.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     HTML header size —

         HTML header size is the HTML heading tag to use for the header. Use this parameter only for
         HTML reports.

           0     <H1>
           1     <H2>
           2     <H3> (default)
           3     <H4>
           4     <H5>
           5     <H6>
           6     <H7>

               •      header placement —

           header placement specifies the location of the header.

               Note If you insert a header in a Microsoft Word report, the header is added to all
                   pages regardless of the placement specified.


             Top of Document
           0
                 (default)
            Append to Body
           1
                (the header is added to the top of each page)

               •      report out —

2606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2607 ordinal=2607 -->
## Functions

Functions


    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SetSet ReportReport FooterFooter TextText

Sets the text of the report footer.

Use tokens with this VI to generate information in the footers. For example, you can
insert a time stamp in the footers of the report.

You cannot use tokens with Microsoft Word and Excel reports.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •        left footer text —

     left footer text is the information you want to appear in the left side of the footer.

   •      center footer text —

    center footer text is the information you want to appear in the center portion of the footer.

   •       right footer text —


                                                    © National Instruments 2607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2608 ordinal=2608 -->
## Functions

Functions


             right footer text is the information you want to appear in the right side of the footer.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     HTML footer size —

         HTML footer size is the HTML heading tag to use for the footer. Use this parameter only for HTML
             reports.

           0     <H1>
           1     <H2>
           2     <H3> (default)
           3     <H4>
           4     <H5>
           5     <H6>
           6     <H7>

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     AppendAppend FrontFront PanelPanel ImageImage toto ReportReport

       Creates an image of the front panel of the VI you specify in VI and appends it to a
       report. Wire data to the VI input to determine the polymorphic instance to use or
      manually select the instance.

      The VI also includes an instance whose connector pane is compatible with versions of
       the VI in LabVIEW 6.1 and earlier.


2608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2609 ordinal=2609 -->
## Functions

Functions


  • Append Front Panel Image to Report (path) VI
  • Append Front Panel Image to Report (refnum) VI
  • Append Front Panel Image to Report (string) VI

For an HTML report, the VI saves the image file to the temporary directory and adds a
link to the image file in the report.

If a front panel is not visible, LabVIEW does not update the values in the objects on the
front panel. If you call a VI whose front panel is not visible and you use the Append
Front Panel Image to Report VI to create an image of the front panel, the image does
not reflect any value changes that occurred when you ran the VI.

If you want the image to reflect value changes, make sure the front panel is open
before any values change. If you do not want to display the front panel but want the
image to reflect value changes, create a Property Node from any front panel terminal
on the block diagram of the VI for which you want to create a front panel image.

      Note If you set Image Format to GIF, the VI does not work when you
        include it in a stand-alone application.

You also can use the following methods to return a front panel image
programmatically:

  • Front Panel: Get Image
  • Front Panel: Get Image Scaled

AppendAppend ControlControl ImageImage toto ReportReport

Creates an image of the front panel object specified in ctrl reference and appends it to
a report.


                                                    © National Instruments 2609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2610 ordinal=2610 -->
## Functions

Functions


      Inputs/Outputs

               •     image file type (.jpg) —

          image file type indicates the format of the image.

           0     .jpg (default)
           1     .png

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM
           9 ABSBOTTOM

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •     image depth —

          image depth specifies the color depth of the image, which is the number of bits to use to
            describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per pixel.


2610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2611 ordinal=2611 -->
## Functions

Functions


  image depth affects how LabVIEW interprets the values of image and colors.

•        ctrl reference —

   ctrl reference is a reference to the control whose image you want to append to the report.

•      description —

  description is the description of the graphic to display if you open the HTML report in a Web
  browser set to display text only.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —


                                                   © National Instruments 2611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2612 ordinal=2612 -->
## Functions

Functions


            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the
                  insertion occurs.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       For an HTML report, the VI saves the image file to the temporary directory and adds a
        link to the image file in the report.

           If a front panel is not visible, LabVIEW does not update the values in the objects on the
       front panel. If you call a VI whose front panel is not visible and you use the Append
       Control Image to Report VI to create an image of a front panel object, the image does
       not reflect any value changes that occurred when you ran the VI.

           If you want the image to reflect value changes, make sure the front panel is open
       before any values change. If you do not want to display the front panel but want the
      image to reflect value changes, create a Property Node from any front panel terminal

2612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2613 ordinal=2613 -->
## Functions

Functions

on the block diagram of the VI for which you want to create a control image.

You also can use the Get Image method to return an image of a front panel object.

AppendAppend ImageImage toto ReportReport

For an HTML report, the VI embeds a link to an image into the report.

You can wire either a path to the image or a string that contains the image URL to this
polymorphic VI. Wire data to the path or URL of image input to determine the
polymorphic instance to use or manually select the instance.

      Note When you append an image to an HTML report, using a file that cannot
      be interpreted by the Web browser could make the image unreadable.


  • Append Image to Report (path wrap) VI
  • Append Image to Report (string wrap) VI

AppendAppend ImageImage toto ReportReport (path(path wrap)wrap) VIVI

For an HTML report, the VI embeds a link to an image into the report.

You can wire either a path to the image or a string that contains the image URL to this
polymorphic VI. Wire data to the path or URL of image input to determine the
polymorphic instance to use or manually select the instance.

      Note When you append an image to an HTML report, using a file that cannot
      be interpreted by the Web browser could make the image unreadable.


                                                    © National Instruments 2613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2614 ordinal=2614 -->
## Functions

Functions


      Inputs/Outputs

               •    MS Office parameters —

        MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
             Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

           You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
             report type to Word but do not specify a bookmark, the insertion occurs at the end of the
           document.

                     •      position (Excel) —

                 position contains the row and column coordinates of the point in an Excel worksheet from
               which the insertion occurs.

            Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
               correspond to cell A1.

                           •     row —

                  rows specifies the row index.

                           •     column —

                  columns specifies the column index.


                     •     name (Excel) —

            name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
                 occurs.

                     •     bookmark (Word) —

             bookmark contains the name of the bookmark in a Word document from which the


2614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2615 ordinal=2615 -->
## Functions

Functions


       insertion occurs.


•      alignment (default) —

  alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
  Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

  0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
  1 LEFT
  2 RIGHT
  3 TOP
  4 TEXTTOP
  5 MIDDLE
  6 ABSMIDDLE
  7 BASELINE
  8 BOTTOM
  9 ABSBOTTOM

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•      path or URL of image —

  path or URL of image designates the path to the linked image. If you move the image, you must
  update the path.

•      caption or alternative string —

  caption or alternative string is the text to display instead of the image if you view the report in a
  Web browser set to display only text.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      report out —


                                                   © National Instruments 2615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2616 ordinal=2616 -->
## Functions

Functions


            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     AppendAppend ImageImage toto ReportReport (string(string wrap)wrap) VIVI

       For an HTML report, the VI embeds a link to an image into the report.

      You can wire either a path to the image or a string that contains the image URL to this
      polymorphic VI. Wire data to the path or URL of image input to determine the
      polymorphic instance to use or manually select the instance.

           Note When you append an image to an HTML report, using a file that cannot
            be interpreted by the Web browser could make the image unreadable.


      Inputs/Outputs

               •    MS Office parameters —


2616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2617 ordinal=2617 -->
## Functions

Functions


  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.

      •      position (Excel) —

       position contains the row and column coordinates of the point in an Excel worksheet from
      which the insertion occurs.

     Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
      correspond to cell A1.

             •     row —

         rows specifies the row index.

             •     column —

         columns specifies the column index.


      •     name (Excel) —

     name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
       occurs.

      •     bookmark (Word) —

     bookmark contains the name of the bookmark in a Word document from which the
       insertion occurs.


•      alignment (default) —

  alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
  Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

  0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
  1 LEFT


                                                   © National Instruments 2617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2618 ordinal=2618 -->
## Functions

Functions


           2 RIGHT
           3 TOP
           4 TEXTTOP
           5 MIDDLE
           6 ABSMIDDLE
           7 BASELINE
           8 BOTTOM
           9 ABSBOTTOM

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •      path or URL of image —

           path or URL of image designates the URL of the linked image. If you intend to post this page to
            the World Wide Web, use forward slashes (/) in paths. If the images are on your local computer or
          on a network, use backslashes (\) in the paths. If you move the images, you must update the
               links.

               •      caption or alternative string —

            caption or alternative string is the text to display instead of the image if you view the report in a
         Web browser set to display only text.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —


2618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2619 ordinal=2619 -->
## Functions

Functions


    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AdvancedAdvanced ReportReport GenerationGeneration

Use the Advanced Report Generation VIs to manipulate reports you create in LabVIEW.

The VIs on this palette can return report generation error codes.


 Palette Object   Description

 Report Type     Returns the report type, such as HTML, of a specified report.


 Get Report
                  Retrieves information about the current font and text settings of a given report. Settings

 Append File to               Appends the text from a text file into the current report. Report


 Clear Report     Clears all text, headers, footers, and formatting information from the report.


 Clear Report     Clears the text and related formatting information from the report. This VI does
 Text            not affect header and footer information.


 Query Available  Lists the printers available on the computer, including the default printer in
 Printers        LabVIEW.


                                                    © National Instruments 2619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2620 ordinal=2620 -->
## Functions

Functions

      ReportReport TypeType

       Returns the report type, such as HTML, of a specified report.

       This VI also returns Microsoft Word or Excel report types.


      Inputs/Outputs

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •      report type —

            report type indicates the report type.

           0  HTML
             Word
           1
                (Report Generation Toolkit)
                 Excel
           2
                (Report Generation Toolkit)

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2621 ordinal=2621 -->
## Functions

Functions

GetGet ReportReport SettingsSettings

Retrieves information about the current font and text settings of a given report.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       text options —

     text options indicates how the text appears in the report.

         •        Italic —

           Italic indicates whether text appears in italics in the report.

         •      StrikeThrough —

        StrikeThrough indicates whether text appears with a strikethrough effect in the report.

         •      Underline —


                                                    © National Instruments 2621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2622 ordinal=2622 -->
## Functions

Functions


                Underline indicates whether text appears underlined in the report.

                     •      Bold —

               Bold indicates whether text appears bold in the report.


               •      font settings —

            font settings indicates what font settings currently are used in a report.

                     •      charset —

                charset is the character set to use for report text. The default is -1.

                     •     name —

            name is the font name.

                     •      weight —

               weight is the thickness of the font.

                     •       size —

                  size is the font size.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       text color —

             text color indicates the color of the text in the report.


     AppendAppend FileFile toto ReportReport

      Appends the text from a text file into the current report.

      The VI appends the text within the report.

2622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2623 ordinal=2623 -->
## Functions

Functions


Inputs/Outputs

   •    MS Office parameters —

   MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
     Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

    You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
    report type to Word but do not specify a bookmark, the insertion occurs at the end of the
    document.

         •      position (Excel) —

         position contains the row and column coordinates of the point in an Excel worksheet from
        which the insertion occurs.

      Row and column values in Excel are zero-based, so the row and column coordinates of (0,0)
        correspond to cell A1.

                •     row —

           rows specifies the row index.

                •     column —

           columns specifies the column index.


         •     name (Excel) —

      name contains the name of the cell in a Microsoft Excel worksheet from which the insertion
         occurs.

         •     bookmark (Word) —

       bookmark contains the name of the bookmark in a Word document from which the


                                                    © National Instruments 2623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2624 ordinal=2624 -->
## Functions

Functions


                  insertion occurs.


               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •        file path —

                file path is the path of the text file from which you want to pull information into your report.

                    If the path is empty or invalid, the VI returns an error.

               •        is spreadsheet file? (Excel) —

                is spreadsheet file? (Report Generation Toolkit) embeds a spreadsheet file into the Microsoft
             Excel worksheet as a table when set to TRUE. The VI ignores this input for HTML and Word
             reports.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       start out (Word) —

              start out (Report Generation Toolkit) represents the index of the character at the beginning of
            the text inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •     end out (Word) —

          end out (Report Generation Toolkit) represents the index of the character at the end of the text
             inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

               •       error out —


2624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2625 ordinal=2625 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


ClearClear ReportReport

Clears all text, headers, footers, and formatting information from the report.


Inputs/Outputs

   •      report in —

    report in is a reference to the report whose appearance, data, and printing you want to control.
    Use the Create Report VI to generate this LabVIEW class object.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ClearClear ReportReport TextText

Clears the text and related formatting information from the report. This VI does not
affect header and footer information.

You cannot use this VI with Microsoft Word and Excel reports.


                                                    © National Instruments 2625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2626 ordinal=2626 -->
## Functions

Functions


      Inputs/Outputs

               •      report in —

            report in is a reference to the report whose appearance, data, and printing you want to control.
           Use the Create Report VI to generate this LabVIEW class object.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      QueryQuery AvailableAvailable PrintersPrinters

        Lists the printers available on the computer, including the default printer in LabVIEW.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      system configured printers —

2626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2627 ordinal=2627 -->
## Functions

Functions


    system configured printers contains the names of printers available on the computer.

    The VI returns the printer names in an array in alphabetical order.

    You also can use the Printing:Available Printers property to obtain a list of printer names
    programmatically.

   •       default printer —

    default printer is the name of the default printer in LabVIEW.

   When you start LabVIEW, the default printer in LabVIEW is the same as the system default printer.
    However, any time you print in LabVIEW, the printer you use becomes the default printer in
    LabVIEW. LabVIEW no longer recognizes changes to the system default printer until you restart
    LabVIEW.

    You can use the Printing:Default Printer property to set the default printer in LabVIEW
    programmatically.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReportReport

Generates a preformatted report that contains VI documentation, data the VI returns,
and report properties, such as the author, company, and number of pages.


Dialog Box Options

 Option      Description

 Report
             Contains the following options:
 Information


                                                    © National Instruments 2627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2628 ordinal=2628 -->
## Functions

Functions


        Option      Description

                                   • Report title—

                            Specifies the title of the report.

                                   • Author name—

                            Specifies the author of the report.

                                   • Company name—

                            Specifies the name of the company.

                                   • Operator name—

                            Specifies the name of the operator who generated the data for the report.

                                   • Report print date—

                          Includes the date of the report.

                                   • Report print time—

                          Includes the time of the report.

                                   • Page number—

                          Includes the current page number of the report.

                                   •  Total pages—

                          Includes the total number of pages of the report.

                           This option prints the total number of pages in the following formats:
            ◦ (Word 2000, XP, and 2003) Page xof n
            ◦ (Word 2007) x/n
                                   •  VI documentation (appendix)—

                          Includes the VI documentation in an appendix.

                                   • Comments—


2628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2629 ordinal=2629 -->
## Functions

Functions


Option      Description

                 Includes comments to append to the report information.

             Contains the following options:

                      • Title—

                   Specifies the title for the data.

                      • Include graph (data input 1)—

Data Input        Specifies whether to include a graph with the data.
1
                      •  Y-axis label—

                   Specifies the label for the y-axis.

                      • Include table—

                   Specifies whether to include a table with the data.

             Contains the following options:

                      • Include graph (data input 2)—

                   Specifies whether to include a graph with the data.

                      • Title—

Data Input        Specifies the title for the data.
2
                      •  Y-axis label—

                   Specifies the label for the y-axis.

                      • Include table—

                   Specifies whether to include a table with the data.


Destination  Specifies where to send the report. You can export the report to a Microsoft Word


                                                    © National Instruments 2629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2630 ordinal=2630 -->
## Functions

Functions


        Option      Description

                  document or a Microsoft Excel worksheet, print to a printer, or save the report in
                HTML format for use on a Web page.


        Path to                     Path where you want to save the report.        save report

      Inputs/Outputs

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Additional Comments —

            Includes additional comments to append to the report information.

               •      Signal 1 —

             Specifies the input signal or signals for Data Input 1.

               •      Signal 2 —

             Specifies the input signal or signals for Data Input 2.

               •      Enabled? —

            Enables or disables the Express VI. The default is TRUE.

               •     Saved Report Path —

            Returns the path where this Express VI saves the report.

               •       error out —

            Contains error information. This output provides standard error out functionality.


     Components

       Specifies the name of the operator who generated the data for the report.

2630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2631 ordinal=2631 -->
## Functions

Functions

Specifies whether to include a table with the data.

Specifies whether to include a graph with the data.

Specifies the label for the y-axis.

Specifies the title for the data.

Specifies whether to include a table with the data.

Specifies whether to include a graph with the data.

Specifies the label for the y-axis.

Specifies the title for the data.

Path where you want to save the report.

Specifies where to send the report. You can export the report to a Microsoft Word
document or a Microsoft Excel worksheet, print to a printer, or save the report in HTML
format for use on a Web page.

Includes comments to append to the report information.

Specifies the name of the company.

Specifies the author of the report.

Includes the VI documentation in an appendix.

Specifies the title of the report.

Specifies the name of the company.

Specifies the author of the report.

Includes the total number of pages of the report.

Includes the current page number of the report.


                                                    © National Instruments 2631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2632 ordinal=2632 -->
## Functions

Functions

       Specifies the title of the report.

       Includes the time of the report.

       Includes the date of the report.

    MeasurementMeasurement I/OI/O

      Use the Measurement I/O VIs and functions to interface with NI-DAQmx and other data
       acquisition devices. This palette displays the VIs and functions for the hardware drivers
      you install.

           If driver VIs you expected to find on this palette are missing, you must install support
        for the driver in the current version of LabVIEW.

           Note If you installed a driver with a previous version of LabVIEW, you must
                 reinstall that driver with the current version of LabVIEW. You can search for
              National Instrument drivers at NI Drivers and Updates on the National
              Instruments Web site or install them using the installation media that
             shipped with your purchase.


         Palette Object      Description

         NI Scan Engine     Use the NI Scan Engine VIs to interface with the NI Scan Engine.

     NINI ScanScan EngineEngine

      Use the NI Scan Engine VIs to interface with the NI Scan Engine.


2632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2633 ordinal=2633 -->
## Functions

Functions


Palette              Description
Object

Synchronize   Synchronizes execution timing to the scan period of the NI Scan Engine. This VI
to Scan        waits for each scan to complete and triggers subsequent code to execute once the
Engine       scan engine has updated all values.

Get Scan
Engine        Returns the scan period of the NI Scan Engine on the target.
Period

Set Scan
Engine        Sets the scan period of the NI Scan Engine on the target.
Period

Get Scan              Returns the operating mode of the NI Scan Engine on the target.Engine Mode

Set Scan               Sets the operating mode of the NI Scan Engine on the target.
Engine Mode


               Discovers new I/O modules on any local or networked target. If a local I/O module isRefresh              detected in a slot that was not previously deployed from a LabVIEW project, this VIModules
               creates new I/O variables for the I/O module.


            Use the Forcing VIs to force and unforce I/O variables programmatically.
Forcing
            The VIs on this palette can return general LabVIEW error codes.


            Use the Faults VIs to view, set, and clear NI Scan Engine faults programmatically.
Faults
            The VIs on this palette can return general LabVIEW error codes.


Fault        Use the Fault Configuration VIs to view and configure the level and triggering
Configuration behavior of system faults.


                                                    © National Instruments 2633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2634 ordinal=2634 -->
## Functions

Functions

     SynchronizeSynchronize toto ScanScan EngineEngine

       Synchronizes execution timing to the scan period of the NI Scan Engine. This VI waits
        for each scan to complete and triggers subsequent code to execute once the scan
      engine has updated all values.

      Use the Scan Engine page to configure the scan period. You also can use the Set Scan
      Engine Period VI to set the scan period programmatically.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      scans since last call —

           scans since last call returns the number of times the scan engine has completed a scan since the
               last call of this VI. You can use this information to identify missed scan iterations and determine
           whether the synchronized code consistently finishes executing on time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use this VI for code running outside of a timed structure. For most NI Scan Engine use
       cases, NI recommends using a timed structure with the Synchronize to Scan Engine
       timing source.

       This VI must run on a target with the NI Scan Engine installed.

     Examples

       Refer to the following example files included with LabVIEW.


2634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2635 ordinal=2635 -->
## Functions

Functions

  • labview\examples\Scan Engine\Scan Engine.lvproj

GetGet ScanScan EngineEngine PeriodPeriod

Returns the scan period of the NI Scan Engine on the target.


Inputs/Outputs

   •       target address (localhost) —

    target address specifies the IP address or DNS name of the target.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      scan period (uSec) —

    scan period (uSec) returns the period of the scan engine running on the target.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet ScanScan EngineEngine PeriodPeriod

Sets the scan period of the NI Scan Engine on the target.


Inputs/Outputs

   •       target address (localhost) —

                                                    © National Instruments 2635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2636 ordinal=2636 -->
## Functions

Functions


             target address specifies the IP address or DNS name of the target.

               •      scan period (uSec) —

           scan period (uSec) specifies the period for the scan engine running on the target.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Changing the scan period while the scan engine is running can take a significant
      amount of time, and might cause the scan engine to run late, resulting in a major fault.
           If changing the scan period results in a fault, you can safely clear the fault after the new
      scan period takes effect.

           Note If the target includes an expansion I/O driver, you can set the scan
              period only when the NI Scan Engine is in Configuration Mode. You can use
              the Set Scan Engine Mode VI before this VI to put the NI Scan Engine on the
                target into Configuration Mode.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Scan Engine\Scan Engine.lvproj

     GetGet ScanScan EngineEngine ModeMode

       Returns the operating mode of the NI Scan Engine on the target.


2636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2637 ordinal=2637 -->
## Functions

Functions

Inputs/Outputs

   •       target address (localhost) —

    target address specifies the IP address or DNS name of the target.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     mode —

   mode returns the operating mode of the NI Scan Engine.

    0 Initialization Mode—Occurs only briefly during startup.
    1 Configuration Mode—The required mode when configuring scan engine settings.
    2 Active Mode—The mode in which the scan engine runs and updates values.
    3 Fault Mode—The mode triggered when a major or unrecoverable fault occurs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet ScanScan EngineEngine ModeMode

Sets the operating mode of the NI Scan Engine on the target.


Inputs/Outputs

   •       target address (localhost) —

    target address specifies the IP address or DNS name of the target.

   •     mode (Active Mode) —


                                                    © National Instruments 2637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2638 ordinal=2638 -->
## Functions

Functions


         mode specifies the operating mode of the scan engine running on the target.

           0 Configuration Mode—The required mode when configuring scan engine settings.
           1 Active Mode (default)—The mode in which the scan engine runs and updates values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      RefreshRefresh ModulesModules

       Discovers new I/O modules on any local or networked target. If a local I/O module is
       detected in a slot that was not previously deployed from a LabVIEW project, this VI
       creates new I/O variables for the I/O module.

      These automatically-created I/O variables use the default I/O variable settings. This VI
      does not add the new I/O variables to a LabVIEW project, and the new I/O variables do
       not persist when the target restarts.


      Inputs/Outputs

               •       target address (localhost) —

             target address specifies the IP address or DNS name of the target.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

2638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2639 ordinal=2639 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


If you physically change an I/O module deployed from a LabVIEW project, this VI
cannot overwrite the deployed configuration until you undeploy the I/O module in the
LabVIEW project. However, if you physically change an I/O module that was
automatically detected by this VI or the corresponding Refresh Local Modules button
in the NI Distributed System Manager, this VI adds and deletes automatically-created
I/O variables to match the new physical configuration.

ForcingForcing

Use the Forcing VIs to force and unforce I/O variables programmatically.

The VIs on this palette can return general LabVIEW error codes.


 Palette
              Description Object

 Enable
 Variable      Enables forcing for I/O variables and I/O aliases on the target.
 Forcing

 Disable               Disables forcing for I/O variables and I/O aliases on the target. Unless you clear
 Variable
                forcing, the previous forced values return when you re-enable forcing.
 Forcing

 Clear
 Variable      Unforces all currently forced I/O variables and I/O aliases on the target.
 Forcing

 Force        Forces an I/O variable or I/O alias to assume forced value until you disable forcing,
 Variable      reboot the target, or force the variable to assume a new forced value.


                                                    © National Instruments 2639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2640 ordinal=2640 -->
## Functions

Functions


         Palette                      Description
        Object

        Unforce      Discontinues forcing on an I/O variable or I/O alias and returns control of the I/O
         Variable      value to the NI Scan Engine.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Scan Engine\Programmatic Forcing.lvproj

      EnableEnable VariableVariable ForcingForcing

      Enables forcing for I/O variables and I/O aliases on the target.


      Inputs/Outputs

               •       target address (localhost) —

             target address specifies the IP address or DNS name of the target.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Forcing must be enabled on the target for individual I/O variable or I/O alias forces to
       take effect. This VI affects the equivalent of a master switch for all I/O variable and I/O
        alias forcing on the target.


2640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2641 ordinal=2641 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Scan Engine\Programmatic Forcing.lvproj

DisableDisable VariableVariable ForcingForcing

Disables forcing for I/O variables and I/O aliases on the target. Unless you clear forcing,
the previous forced values return when you re-enable forcing.


Inputs/Outputs

   •       target address (localhost) —

    target address specifies the IP address or DNS name of the target.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Forcing must be enabled on the target for individual I/O variable or I/O alias forces to
take effect. Use the Enable Variable Forcing VI to re-enable forcing on the target.

ClearClear VariableVariable ForcingForcing

Unforces all currently forced I/O variables and I/O aliases on the target.


                                                    © National Instruments 2641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2642 ordinal=2642 -->
## Functions

Functions


      Inputs/Outputs

               •       target address (localhost) —

             target address specifies the IP address or DNS name of the target.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This VI does not disable forcing on the target. Use the Disable Variable Forcing VI to
       prevent I/O variable and I/O alias forcing from taking effect on the target.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Scan Engine\Programmatic Forcing.lvproj

      ForceForce VariableVariable

       Forces an I/O variable or I/O alias to assume forced value until you disable forcing,
       reboot the target, or force the variable to assume a new forced value.


      Inputs/Outputs

               •       variable path (URL) —


2642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2643 ordinal=2643 -->
## Functions

Functions


    variable path (URL) specifies the path to the I/O variable or I/O alias. The path can be absolute
    or relative. The format of the variable path is
   \\<TargetName>\<ModuleName>\<VariableName>. You can view the variable path for
    an I/O variable in the Context Help window when you hover over the I/O variable node on the
    block diagram.

   •      forced value —

    forced value is the value for the I/O variable or I/O alias to assume while forcing is enabled on
    the target and the enable forcing input of this VI is TRUE.

    To ensure data integrity, you must wire a value of the same data type as the I/O variable. To
     verify the data type of an I/O variable, right-click the I/O variable in the Project Explorer window
    and select Properties to display the Shared Variable Properties dialog box.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


To perform batch forcing on a set of I/O variables, disable forcing on the target, force
each I/O variable, then enable forcing on the target.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Scan Engine\Programmatic Forcing.lvproj

UnforceUnforce VariableVariable

Discontinues forcing on an I/O variable or I/O alias and returns control of the I/O value
to the NI Scan Engine.


                                                    © National Instruments 2643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2644 ordinal=2644 -->
## Functions

Functions


      Inputs/Outputs

               •       variable path (URL) —

             variable path (URL) specifies the path to the I/O variable or I/O alias. The path can be absolute
            or relative. The format of the variable path is
         \\<TargetName>\<ModuleName>\<VariableName>. You can view the variable path for
          an I/O variable in the Context Help window when you hover over the I/O variable node on the
            block diagram.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Scan Engine\Programmatic Forcing.lvproj

      FaultsFaults

      Use the Faults VIs to view, set, and clear NI Scan Engine faults programmatically.

      The VIs on this palette can return general LabVIEW error codes.


2644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2645 ordinal=2645 -->
## Functions

Functions


 Palette         Description
 Object

 Get
 Fault   Returns a list of active faults.
 List

 Set     Creates a fault. When the major fault input is TRUE, this VI triggers fault mode. Use the
 Fault   code element of the error in (user fault) input cluster to specify the fault code.


 Clear    Clears NI Scan Engine faults. If the fault you specify using the fault code input is active, this
 Fault    VI clears the fault. If the fault is not active, this VI takes no action and generates no error.

 Clear
 All      Clears all active faults on the target.
 Faults

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Scan Engine\Scan Engine.lvproj

GetGet FaultFault ListList

Returns a list of active faults.


Inputs/Outputs

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       fault list —


                                                    © National Instruments 2645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2646 ordinal=2646 -->
## Functions

Functions


              fault list contains the list of active faults.

                     •      code —

              code is the fault code.

                     •       level —

                  level is the severity level of the fault.

                     •        first reported time —

                      first reported time returns the time the fault first occurred since it was last cleared.

                     •     number reported —

             number reported is the number of times the fault has occurred since it was last cleared.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This VI allocates memory and can affect the determinism of the application. This VI
      must run on a target with the NI Scan Engine installed.

      To obtain the fault list of a remote target from a host computer, you can use the
      DataSocket Read VI to subscribe to the following URL:

     psp:\\<target IP address>\NI_SystemState\ControllerStatus\
     FaultList

      The data type returned by the URL above is identical to that of the fault list output
       terminal of this VI.

      You also can determine whether a fault is present on a remote target from a host
      computer by using the DataSocket Read VI to subscribe to the following URL:

     psp:\\<target IP address>\NI_SystemState\ControllerStatus\
     FaultPresent

2646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2647 ordinal=2647 -->
## Functions

Functions

The data type returned by the URL above is Boolean.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Scan Engine\Scan Engine.lvproj

SetSet FaultFault

Creates a fault. When the major fault input is TRUE, this VI triggers fault mode. Use the
code element of the error in (user fault) input cluster to specify the fault code.


Inputs/Outputs

   •      major fault (F) —

    major fault specifies whether the fault is major (TRUE) or minor (FALSE).

   •       error in (user fault) —

    error in (user fault) specifies the fault code.

       If you do not specify a fault code, the fault code defaults to −66480. This VI triggers a fault based
    on the presence of a non-zero error code, regardless of the value of status. You may optionally
    provide additional information about the fault in source.

   •       error adding fault —

    error adding fault contains error information related to the creation of the fault. Fault creation
    can fail if the NI Scan Engine is not installed on the target or if the target has already reached the
   maximum number of active faults (100). Right-click the error out front panel indicator and select
    Explain Error from the shortcut menu for more information about the error.

   •       error out —

    error out returns error in (user fault).


                                                    © National Instruments 2647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2648 ordinal=2648 -->
## Functions

Functions

       This VI does not allocate memory, so you can use this VI in a time-critical section of an
       application without significantly affecting determinism.

       This VI must run on a target with the NI Scan Engine installed.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Scan Engine\Scan Engine.lvproj

       ClearClear FaultFault

       Clears NI Scan Engine faults. If the fault you specify using the fault code input is active,
        this VI clears the fault. If the fault is not active, this VI takes no action and generates no
        error.


      Inputs/Outputs

               •       target address (localhost) —

             target address specifies the IP address or DNS name of the target.

               •       fault code —

              fault code is the code associated with the fault. The VI ignores this input if clear all? is TRUE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2649 ordinal=2649 -->
## Functions

Functions

This VI does not allocate memory, so you can use this VI in a time-critical section of an
application without significantly affecting determinism.

This VI applies only to targets with the NI Scan Engine installed. You must either run
this VI on a target with the NI Scan Engine installed or use the target address input to
point to a target with the NI Scan Engine installed.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Scan Engine\Scan Engine.lvproj

ClearClear AllAll FaultsFaults

Clears all active faults on the target.


Inputs/Outputs

   •       target address (localhost) —

    target address specifies the IP address or DNS name of the target.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI does not allocate memory, so you can use this VI in a time-critical section of an
application without significantly affecting determinism.

This VI applies only to targets with the NI Scan Engine installed. You must either run

                                                    © National Instruments 2649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2650 ordinal=2650 -->
## Functions

Functions

        this VI on a target with the NI Scan Engine installed or use the target address input to
       point to a target with the NI Scan Engine installed.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Scan Engine\Scan Engine.lvproj

      FaultFault ConfigurationConfiguration

      Use the Fault Configuration VIs to view and configure the level and triggering behavior
       of system faults.


         Palette Object        Description

         Set Fault                              Applies a custom fault configuration for a configurable fault.         Configuration


         Clear Fault            Clears the custom fault configuration for a configurable fault and applies the
         Configuration         default configuration.


        Get All Fault                             Returns a list of custom fault configurations.
         Configurations

      SetSet FaultFault ConfigurationConfiguration

       Applies a custom fault configuration for a configurable fault.

           If the fault code you specify does not correspond to a configurable fault, this VI returns
      an error.


2650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2651 ordinal=2651 -->
## Functions

Functions


Inputs/Outputs

   •       target address (localhost) —

    target address specifies the IP address or DNS name of the target.

   •       fault configuration —

     fault configuration specifies the custom fault configuration to apply.

         •      code —

       code is the fault code of the configurable fault.

         •       level or level before threshold —

         level or level before threshold specifies the level of the specified fault before the
        occurrence threshold is met.

         Ignore—Each occurrence adds to the occurrence counter used to determine whether the        0          occurrence threshold is met but does not trigger the fault.
        1 Minor—Each occurrence triggers the fault as a Minor fault.
        2 Major—Each occurrence triggers the fault as a Major fault.

         •      occurrence threshold —

        occurrence threshold specifies the number of times the selected fault can occur before the
          level of the fault changes.

         •      time window in seconds —

        time window specifies a time limit for the occurrence threshold. When the time window
         expires, LabVIEW resets the internal occurrence counter for the specified fault and restarts
        the time window. The default is 0, which specifies not to use the time window and not to
         reset the occurrence counter until the NI Scan Engine restarts.

         •       level after threshold —


                                                    © National Instruments 2651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2652 ordinal=2652 -->
## Functions

Functions


                  level after threshold specifies the level of the specified fault after the occurrence threshold
                      is met.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       ClearClear FaultFault ConfigurationConfiguration

       Clears the custom fault configuration for a configurable fault and applies the default
       configuration.


      Inputs/Outputs

               •       target address (localhost) —

             target address specifies the IP address or DNS name of the target.

               •      code to clear —

           code to clear is the error code that corresponds to the configurable fault.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —


2652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2653 ordinal=2653 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


GetGet AllAll FaultFault ConfigurationsConfigurations

Returns a list of custom fault configurations.


Inputs/Outputs

   •       target address (localhost) —

    target address specifies the IP address or DNS name of the target.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      configured faults —

    configured faults returns information about custom fault configurations on the target.

       If none of the configurable faults are currently set to use custom configurations, this output
    returns an empty array.

         •      code —

         •       level or level before threshold —

         •      occurrence threshold —

         •      time window in seconds —

         •       level after threshold —


   •       error out —


                                                    © National Instruments 2653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2654 ordinal=2654 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

    InstrumentInstrument I/OI/O

      Use the Instrument I/O VIs and functions to interface with GPIB, serial, modular, PXI,
      and other types of instruments. Use the NI Instrument Driver Finder to search for and
         install instrument drivers. If an instrument driver is not available in the NI Instrument
       Driver Finder, you can use the Create New Instrument Driver Project wizard to create a
     new instrument driver.

           If driver VIs you expected to find on this palette are missing, you must install support
        for the driver in the current version of LabVIEW.

           Note If you installed an instrument driver with a previous version of
             LabVIEW, you must reinstall that instrument driver with the current version of
             LabVIEW.

       Before you begin using the Instrument I/O VIs and functions, make sure you choose the
       appropriate method of instrument control.


         Palette
                     Description
        Object

                  Use Instrument Drivers VIs to configure, control, and retrieve data from GPIB, serial,
                    modular, PXI, and other types of instruments. Use the NI Instrument Driver Finder to
        Instrument
                    search for and install instrument drivers. If an instrument driver is not available, you
         Drivers
                   can use the Create New Instrument Driver Project wizard to create a new instrument
                        driver.


        VISA       Use the VISA VIs and functions to program instruments using VISA.


2654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2655 ordinal=2655 -->
## Functions

Functions


 Palette             Description
 Object

 GPIB      Use the GPIB functions to communicate with GPIB (IEEE-488) devices.


           Use the Serial VIs and functions to access the VISA VIs and functions that communicate
 Serial      with devices connected to a serial port. Additional functions are also available on the
            VISA palette.

InstrumentInstrument DriversDrivers

Use Instrument Drivers VIs to configure, control, and retrieve data from GPIB, serial,
modular, PXI, and other types of instruments. Use the NI Instrument Driver Finder to
search for and install instrument drivers. If an instrument driver is not available, you
can use the Create New Instrument Driver Project wizard to create a new instrument
driver.

The VIs and controls that appear on this palette change depending on the instrument
drivers you install. You can add new VIs and controls to this palette. Before you begin
using the Instrument Driver VIs, make sure you choose the appropriate method of
instrument control.


VISAVISA

Use the VISA VIs and functions to program instruments using VISA.

The VIs and functions on this palette can return VISA error codes.


                                                    © National Instruments 2655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2656 ordinal=2656 -->
## Functions

Functions


         Palette                   Description
        Object

        VISA                    Writes the data from write buffer to the device or interface specified by VISA resource         Write                name.         Function

        VISA                 Reads the specified number of bytes from the device or interface specified by VISA       Read                   resource name and returns the data in read buffer.         Function

        VISA                 Use the VISA Advanced VIs and functions to accomplish advanced VISA tasks.        Advanced

        VISA
         Clear      Clears the input and output buffers of the device.
         Function

        VISA                 Reads a service request status byte byte from the message-based device specified by       Read STB                  VISA resource name.
         Function

        VISA       Asserts a software or hardware trigger, depending on the interface type. For software
         Assert      triggers, Default (0) is the only valid protocol. For VXI hardware triggers, Default (0) is
         Trigger    equivalent to Sync (5). For PXI triggers, PXI: Reserve (6) and PXI: Unreserve (7) are the
         Function  only valid protocols.

     VISAVISA WriteWrite FunctionFunction

       Writes the data from write buffer to the device or interface specified by VISA resource
      name.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.


2656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2657 ordinal=2657 -->
## Functions

Functions

   •      write buffer —

    write buffer contains the data to be written to the device.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      return count —

    return count contains the actual number of bytes written.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Whether the data is transferred synchronously or asynchronously is platform-
dependent. Right-click the node and select Synchronous I/O Mode»Synchronous from
the shortcut menu to write data synchronously.

When you transfer data from or to a hardware driver synchronously, the calling thread
is locked for the duration of the data transfer. Depending on the speed of the transfer,
this can hinder other processes that require the calling thread. However, if an
application requires that the data transfer as quickly as possible, performing the
operation synchronously dedicates the calling thread exclusively to this operation.

      Note In most applications, synchronous calls are slightly faster when you
        are communicating with four or fewer instruments. Asynchronous operations
        result in a significantly faster application when you are communicating with
         five or more instruments. The LabVIEW default is asynchronous I/O.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 2657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2658 ordinal=2658 -->
## Functions

Functions

            • labview\examples\Instrument IO\Serial\Serial.lvproj
            • labview\examples\Instrument IO\GPIB\GPIB with VISA
        functions.vi

     VISAVISA ReadRead FunctionFunction

      Reads the specified number of bytes from the device or interface specified by VISA
       resource name and returns the data in read buffer.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      byte count —

            byte count is the number of bytes to be read.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      read buffer —

           read buffer contains the data read from the device.

               •      return count —

            return count contains the number of bytes actually read.

               •       error out —

2658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2659 ordinal=2659 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


This function might return less than the number of bytes requested if the function
reaches the end of the buffer, reaches a termination character, or if a timeout occurs.
The output error cluster indicates if a timeout has occurred.

Whether the data is read synchronously or asynchronously is platform-dependent.
Right-click the node and select Synchronous I/O Mode»Synchronous from the
shortcut menu to read data synchronously.

When you transfer data from or to a hardware driver synchronously, the calling thread
is locked for the duration of the data transfer. Depending on the speed of the transfer,
this can hinder other processes that require the calling thread. However, if an
application requires that the data transfer as quickly as possible, performing the
operation synchronously dedicates the calling thread exclusively to this operation.

      Note In most applications, synchronous calls are slightly faster when you
        are communicating with 4 or fewer instruments. Asynchronous operations
        result in a significantly faster application when you are communicating with 5
        or more instruments. The LabVIEW default is asynchronous I/O.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Continuous Serial
   Write and Read.vi
  • labview\examples\Instrument IO\VISA\USB\USB RAW - Bulk.vi
  • labview\examples\Instrument IO\GPIB\GPIB with VISA
   functions.vi

VISAVISA AdvancedAdvanced

Use the VISA Advanced VIs and functions to accomplish advanced VISA tasks.


                                                    © National Instruments 2659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2660 ordinal=2660 -->
## Functions

Functions

      The VIs and functions on this palette can return VISA error codes.


         Palette                     Description        Object

        VISA Open  Opens a session to the device specified by VISA resource name and returns a session
         Function     identifier that can be used to call any other operations of that device.

        VISA Close                     Closes a device session or event object specified by VISA resource name.         Function

        VISA Find
        Resource    Queries the system to locate the devices associated with a specified interface.
         Function

        VISA Set                      Sets the Timeout value, in milliseconds, for the VISA session.        Timeout

        VISA                     Gets (reads) and/or sets (writes) properties of a reference. The node operates in the         Property
                 same way as a standard Property Node.       Node

        Bus/                  Use the Bus/Interface Specific functions to program instruments that are interface          Interface
                         specific.          Specific

        VISA Write                    Takes data from the file specified by filename and writes it to the device
       From File
                     synchronously.
         Function

        VISA Read
                   Reads byte count synchronously and stores the transferred data in the file specified
        To File
                   by filename.
         Function

        Event
                  Use the Event Handling VIs and functions to use VISA events with your instruments.
        Handling


        VISA Lock   Asynchronously attempts to establish access to the device or interface specified by
        Async       VISA resource name. Use this function to obtain an exclusive lock that guarantees


2660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2661 ordinal=2661 -->
## Functions

Functions


 Palette             Description
 Object

              sole access to a device or resource.

 VISA
 Unlock      Relinquishes the lock previously obtained using the VISA Lock Async function.
 Function

 Register            Use the Register Access functions to program in an address space at a high level. Access

VISAVISA OpenOpen FunctionFunction

Opens a session to the device specified by VISA resource name and returns a session
identifier that can be used to call any other operations of that device.


Inputs/Outputs

   •      VISA Open timeout (0) —

    VISA Open timeout specifies the maximum time period, in milliseconds, that VISA Open waits
    before returning an error. It does not set the I/O timeout.

    To specify the timeout used for future operations on the VISA session, use VISA Set Timeout.

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      duplicate session (F) —

       If duplicate session is TRUE and there is currently a session opened to the resource, another


                                                    © National Instruments 2661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2662 ordinal=2662 -->
## Functions

Functions


            session is opened to the resource. If duplicate session is set to FALSE and a session is opened to
            the resource, the open session is used.

          A VISA session is a unique logical identifier used by VISA to communicate with a resource. The
            VISA session is maintained by the VISA resource name control and is not seen by the user.

               •      access mode —

            access mode specifies how to access the device.

             This input accepts the following values.

             VISA Defaults (default)—Open session without using an exclusive lock or loading configuration           0              information.
              Exclusive Lock—Acquire an exclusive lock immediately upon opening a session. If a lock           1             cannot be acquired, the session is closed and an error is returned.
            Load Configured Settings—Configure attributes to values specified by an external
              configuration utility, such as the following utilities:
           4   • (Windows) Measurement & Automation Explorer
                       • (Mac OS X) NI-VISA Configuration
                       •  (Linux) visaconf

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is the resource to which a VISA session is opened and its class. The class
           matches that of the VISA resource name input.

             Refer to VISA resource name control for more information.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If you open a significant number of VISA sessions without closing them, you decrease
       the available memory resources. Close the session with the VISA Close function.


2662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2663 ordinal=2663 -->
## Functions

Functions

      Note This function recognizes all resource strings returned by VISA Find
       Resource. However, VISA Find Resource does not necessarily return all strings
        that you pass to this function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\GPIB\GPIB with VISA
   functions.vi

VISAVISA CloseClose FunctionFunction

Closes a device session or event object specified by VISA resource name.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Error I/O operates uniquely in this function. The function closes the device session
regardless of whether an error occurred in a preceding operation. For each VISA

                                                    © National Instruments 2663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2664 ordinal=2664 -->
## Functions

Functions

       session that you open, you should close the session when you are finished with it. This
       function accepts all available classes.

      You also can use the Open VISA Session Monitor VI in the labview\vi.lib\
     Utility\visa.llb to close all open VISA sessions. Alternatively, you could save
      work, exit, and re-enter LabVIEW. Exiting LabVIEW closes all open VISA sessions. You
       also can select the Automatically close VISA sessions option on the Environment
      page of the Options dialog box.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\Serial\Continuous Serial
        Write and Read.vi
            • labview\examples\Instrument IO\VISA\PXI\PXI - Route
        Trigger.vi
            • labview\examples\Instrument IO\GPIB\GPIB with VISA
        functions.vi
            • labview\examples\Instrument IO\VISA\USB\USB RAW -
        Interrupt.vi

      VISAVISA FindFind ResourceResource FunctionFunction

       Queries the system to locate the devices associated with a specified interface.


      Inputs/Outputs

               •      expression ("?*") —

            expression matches the value specified with the devices available for a particular interface.

          The description string specified sets the criteria to search an interface—GPIB, GPIB-VXI, VXI, All
              VXI, Serial, or All—for existing devices. The following table includes valid special characters and


2664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2665 ordinal=2665 -->
## Functions

Functions


operators.

Special
Characters          Meaningand
Operators
?         Matches any one character.
          Makes the character that follows it an ordinary character instead of special
\           character. For example, when a question mark follows a backslash (\?), it matches
           the ? character instead of any one character.
          Matches any one character from the enclosed list. You can use a hyphen to match a
[list]           range of characters.
          Matches any character not in the enclosed list. You can use a hyphen to match a
[^list]           range of characters.
*         Matches 0 or more occurrences of the preceding character or expression.
+         Matches 1 or more occurrences of the preceding character or expression.
          Matches either the preceding or following expression. The or operator | matches the
Exp|exp  entire expression that precedes or follows it and not just the character that precedes
           or follows it. For example, VXI|GPIB means (VXI)|(GPIB), not VX(I|G)PIB.
(exp)    Grouping characters or expressions.

The search criteria specified in the expression parameter has two parts, a regular expression
over a resource string and an optional logical expression over attribute values. The regular
expression is matched against the resource strings of resources known to the VISA Resource
Manager. If the resource string matches the regular expression, the attribute values of the
resource are matched against the expression over attribute values. If the match is successful, the
resource has met the search criteria and is added to the list of resources found. The following
table includes valid regular expressions.

Regular Expression         Sample Matches
                           Matches GPIB0::2::INSTR, GPIB1::1::1::INSTR, and
GPIB?*INSTR
                       GPIB-VXI1::8::INSTR.
                           Matches GPIB0::2::INSTR and GPIB1::1::1::INSTR
GPIB[0-9]*::?*INSTR
                            but not GPIB-VXI1::8::INSTR.
                           Matches GPIB1::1::1::INSTR but not
GPIB[^0]::?*INSTR
                      GPIB0::2::INSTR or GPIB12::8::INSTR.
                           Matches VXI0::1::INSTR but not GPIB-
VXI?*INSTR
                       VXI0::1::INSTR.
                           Matches GPIB-VXI0::1::INSTR but not
GPIB-VXI?*INSTR
                       VXI0::1::INSTR.


                                                 © National Instruments 2665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2666 ordinal=2666 -->
## Functions

Functions


            Regular Expression         Sample Matches
         ?*VXI[0-9]*::?*INSTR   Matches VXI0::1::INSTR and GPIB-VXI0::1::INSTR.
         ASRL[0-9]*::?*INSTR    Matches ASRL1::INSTR but not VXI0::5::INSTR.
                                      Matches ASRL1::INSTR and ASRL11::INSTR but not
         ASRL1+::INSTR
                                 ASRL2::INSTR.
                                      Matches GPIB1::5::INSTR and VXI0::3::INSTR but not
         (GPIB|VXI)?*INSTR
                                 ASRL2::INSTR.
         (GPIB0|VXI0)::1::INSTR Matches GPIB0::1::INSTR and VXI0::1::INSTR.
         ?*INSTR                  Matches all INSTR (device) resources.
         ?*VXI[0-9]*::?*MEMACC Matches VXI0::MEMACC and GPIB-VXI1::MEMACC.
                                      Matches VXI0::1::INSTR, VXI0::2::INSTR, and
         VXI0::?*
                                 VXI0::MEMACC.
         ?*                              (default) Matches all resources.
                                      Matches all resources on the specified remote system. You can
                                             set the hostname as either an IP address (dot-notation) or a
         visa://hostname/?*                                      network machine name. This remote system does not need to
                                    be a configured remote system.
                                      Matches all resources on the local machine. Does not query
         /?*                                          configured remote systems.
                                      Matches all ASRL resources on the local machine and returns
         visa:/ASRL?*INSTR                                  them in URL format, such as visa:/ASRL1::INSTR.

           By using the optional attribute expression, you can construct flexible and powerful expressions
            with the use of logical ANDs (&&), ORs(||), and NOTs (!). You can use equal (==) and unequal (!=)
           comparators to compare attributes of any data type, and other inequality comparators (>, <, >=,
             <=) to compare attributes of numeric data type. Use only global attributes in the attribute
             expression. Local attributes are not allowed in the logical expression part of the expr parameter.
          The following table includes valid expression parameters.

           Expr Parameter                                                Meaning
                                                                                 Find all GPIB
                                                                                    devices that have
         GPIB[0-9]*::?*::?*::INSTR{VI_ATTR_GPIB_SECONDARY_ADDR
                                                                              secondary
         > 0 && VI_ATTR_GPIB_SECONDARY_ADDR < 10}                                                                                addresses from 1
                                                                                      to 9.
                                                                                 Find all serial ports
         ASRL?*INSTR{VI_ATTR_ASRL_BAUD == 9600}                    configured at 9600
                                                                              baud.
         ?*VXI?INSTR{VI_ATTR_MANF_ID == 0xFF6 &&                  Find all VXI
         !(VI_ATTR_VXI_LA ==0 || VI_ATTR_SLOT <= 0)}             instrument


2666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2667 ordinal=2667 -->
## Functions

Functions


  Expr Parameter                                                Meaning
                                                                         resources having
                                                                     manufacturer ID
                                                                  FF6 and which are
                                                                      not logical address
                                                                                        0, slot 0, or external
                                                                                   controllers.

•      search mode (0) —

  search mode determines how the function returns found interfaces in the find list output, either
  by canonical names or aliases. The default is 0.

  This input accepts the following values.

   Canonical Names Only—Search all configured buses. Returns only the resources found that
  0 match the expression string. The format of each returned string is the VISA canonical spec-
   defined resource format.
    Aliases Only—Search all configured buses. Returns only the resources found that match the
   expression string. For each resource, if there is a user-defined alias for that resource, that alias  2     is returned. For the other resources, the returned string is in the VISA canonical spec-defined
   resource format.
   Include Matching Aliases—Do not search any buses. Returns only resources with user-defined  3
    aliases. The only valid expression string is "?*". The format of each returned string is an alias.
   Include All Aliases—Search all configured buses. Returns all found resources that match the
   expression string and all user-defined aliases even if they do not match the expression string.  4   For each resource, the function returns a user-defined alias if there is one for that resource. For
   the other resources, the returned string is in the VISA canonical spec-defined resource format.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       find list —

  find list is an array of strings, each string specifying one interface found by the function.

•      return count —

  return count specifies the number of matches found. The number of matches found is the
  number of strings in the find list array.


                                                   © National Instruments 2667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2668 ordinal=2668 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      LabVIEW lists resources in an I/O control according to the chosen I/O control class type
      and the Filter VISA Names dialog box, so you might not need to call this function.

         All resource strings returned by this function are recognized by VISA Open. However,
        this function does not necessarily return all strings that you pass to the VISA Open
       function. This is especially true for network and TCP/IP resources. If a resource does
       not appear in the list, you can explicitly add the resource in the NI-VISA configuration
         utility, such as (Windows) Measurement & Automation Explorer, (Linux) visaconf, or
      (Mac OS X) NI-VISA Configuration. The configuration utility also has options that
      expand or limit the set of resources that this VI returns.

      VISAVISA SetSet TimeoutTimeout

       Sets the Timeout value, in milliseconds, for the VISA session.

       VISA Set Timeout is a Property Node with a VISA class of Instr.


      Inputs/Outputs

               •      reference —

               •       error in (no error) —

               •      General Settings:Timeout Value —

               •      reference out —

               •       error out —


2668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2669 ordinal=2669 -->
## Functions

Functions

VISAVISA PropertyProperty NodeNode

Gets (reads) and/or sets (writes) properties of a reference. The node operates in the
same way as a standard Property Node.


Inputs/Outputs

   •      reference —
    reference is the refnum associated with the object for which you want to set or get properties.

       If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For
    the Application class, the default is the current application instance. For the VI class, the default
      is the VI containing the Property Node.

    You also can wire a LabVIEW class to the reference input to access the private data of the
    LabVIEW class.

   •       error in (no error) —
    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.
   •      property 2 — property 2..n are examples of properties you want to set (write).
   •      reference out —
    reference out returns reference unchanged.
   •       error out —
    error out contains error information. This output provides standard error out functionality.
   •      property 1 — property 1..n are examples of properties you want to get (read).
   •      Property —


Bus/InterfaceBus/Interface SpecificSpecific

Use the Bus/Interface Specific functions to program instruments that are interface
specific.

The functions on this palette can return VISA error codes.


                                                    © National Instruments 2669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2670 ordinal=2670 -->
## Functions

Functions


         Palette Object   Description

                     Use the Serial VIs and functions to access the VISA VIs and functions that
          Serial         communicate with devices connected to a serial port. Additional functions are
                          also available on the VISA palette.


        VISA USB       Use the VISA USB VI and functions to control USB devices.

        VISA Set I/O                         Sets the size of the I/O buffer. Run the VISA Configure Serial Port VI first if you are
         Buffer Size                           setting the size of a serial port buffer.         Function

        VISA Flush I/O                         Flushes the I/O buffer specified by mask.         Buffer Function

        VISA GPIB
      Command      Writes GPIB command bytes on the bus.
         Function

        VISA GPIB                         Controls the state of the GPIB ATN interface line and, optionally, the active
         Control ATN                           controller state of the local interface.         Function

        VISA GPIB Pass                             Tells the GPIB device at the specified address to become controller-in-charge         Control                             (CIC).
         Function

        VISA GPIB Send
                         Pulses the interface clear line (IFC) for at least 100 microseconds.
         IFC Function

        VISA GPIB
         Control REN     Asserts or deasserts the GPIB REN interface line according to the specified mode.
         Function

        VISA VXI Cmd
                      Sends the device a miscellaneous command or query and/or retrieves the
         or Query
                       response to a previous query.
         Function

        VISA Assert
         Interrupt        Asserts the specified device interrupt or signal.
         Signal Function

2670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2671 ordinal=2671 -->
## Functions

Functions


 Palette Object   Description

 VISA Assert
 Utility Signal    Asserts or deasserts the specified utility bus signal.
 Function

 VISA Map
 Trigger        Maps the specified trigger source line to the specified trigger destination line.
 Function

 VISA Unmap             Unmaps a previous map from the specified trigger source line to the specified Trigger                  trigger destination line. This function unmaps one trigger mapping per call.
 Function

SerialSerial

Use the Serial VIs and functions to access the VISA VIs and functions that communicate
with devices connected to a serial port. Additional functions are also available on the
VISA palette.

The VIs and functions on this palette can return serial error codes.


 Palette
              Description Object

 VISA           Initializes the serial port specified by VISA resource name to the specified settings.
 Configure    Wire data to the VISA resource name input to determine the polymorphic instance to
 Serial Port   use or manually select the instance.

 VISA Write    Writes the data from write buffer to the device or interface specified by VISA
 Function     resource name.

 VISA Read    Reads the specified number of bytes from the device or interface specified by VISA
 Function     resource name and returns the data in read buffer.

 VISA Close
              Closes a device session or event object specified by VISA resource name.
 Function


                                                    © National Instruments 2671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2672 ordinal=2672 -->
## Functions

Functions


         Palette                      Description
        Object

        VISA Bytes
         at Serial      Returns the number of bytes in the input buffer of the specified serial port.
         Port

        VISA Serial   Sends a break on the specified output port. Wire data to the VISA resource name
        Break        input to determine the polymorphic instance to use or manually select the instance.

        VISA Set I/O                      Sets the size of the I/O buffer. Run the VISA Configure Serial Port VI first if you are         Buffer Size                        setting the size of a serial port buffer.         Function

        VISA Flush
         I/O Buffer    Flushes the I/O buffer specified by mask.
         Function

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\Serial\Serial.lvproj
   VISAVISA ConfigureConfigure SerialSerial PortPort

        Initializes the serial port specified by VISA resource name to the specified settings.
       Wire data to the VISA resource name input to determine the polymorphic instance to
      use or manually select the instance.


            • VISA Configure Serial Port (Instr) VI
            • VISA Configure Serial Port (Serial Instr) VI


2672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2673 ordinal=2673 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Serial.lvproj
VISAVISA ConfigureConfigure SerialSerial PortPort (Instr)(Instr) VIVI

Initializes the serial port specified by VISA resource name to the specified settings.
Wire data to the VISA resource name input to determine the polymorphic instance to
use or manually select the instance.


Inputs/Outputs

   •      Enable Termination Char (T) —

    Enable Termination Char prepares the serial device to recognize termination char.

       If TRUE (default), the VI_ATTR_ASRL_END_IN attribute is set to recognize the termination
     character. If FALSE, the VI_ATTR_ASRL_END_IN attribute is set to 0 (None) and the serial device
    does not recognize the termination char.

   •      termination char (0xA = '\n' = LF) —

    termination char calls for termination of the read operation. The read operation terminates
   when the termination char is read from the serial device.

   0xA is the hex equivalent of a linefeed character (\n). Change the termination char to 0xD for
    message strings that terminate with a carriage return (\r).

   •      timeout (10sec) —

                                                    © National Instruments 2673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2674 ordinal=2674 -->
## Functions

Functions


           timeout specifies the time, in milliseconds, for the write and read operations.

          The default is 10000.

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •     baud rate (9600) —

          baud rate is the rate of transmission.

          The default is 9600.

               •      data bits (8) —

           data bits is the number of bits in the incoming data.

          The value of data bits is between five and eight. The default value is 8.

               •       parity (0:none) —

             parity specifies the parity used for every frame to be transmitted or received.

             This input accepts the following values.

                 no parity           0                        (default)
           1      odd parity
           2       even parity
           3      mark parity
           4       space parity

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      stop bits (10: 1 bit) —

            stop bits specifies the number of stop bits used to indicate the end of a frame.


2674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2675 ordinal=2675 -->
## Functions

Functions


  This input accepts the following values.

  10            1 stop bit
  15              1.5 stop bits
  20            2 stop bits

•      flow control (0:none) —

  flow control sets the type of control used by the transfer mechanism.

  This input accepts the following values.

   None (default)—The transfer mechanism does not use flow control. Buffers on both sides of the  0   connection are assumed to be large enough to hold all data transferred.
   XON/XOFF—The transfer mechanism uses the XON and XOFF characters to perform flow
    control. The transfer mechanism controls input flow by sending XOFF when the receive buffer
  1     is nearly full, and it controls the output flow by suspending transmission when XOFF is
    received.
   RTS/CTS—The transfer mechanism uses the RTS output signal and the CTS input signal to
   perform flow control. The transfer mechanism controls input flow by unasserting the RTS
  2    signal when the receive buffer is nearly full, and it controls output flow by suspending the
   transmission when the CTS signal is unasserted.
   XON/XOFF and RTS/CTS—The transfer mechanism uses the XON and XOFF characters and the
   RTS output signal and CTS input signal to perform flow control. The transfer mechanism
  3 controls input flow by sending XOFF and unasserting the RTS signal when the receive buffer is
    nearly full, and it controls the output flow by suspending transmission when XOFF is received
   and the CTS is unasserted.
   DTR/DSR—The transfer mechanism uses the DTR output signal and the DSR input signal to
   perform flow control. The transfer mechanism controls input flow by unasserting the DTR  4
    signal when the receive buffer is nearly full, and it controls output flow by suspending the
   transmission when the DSR signal is unasserted.
   XON/XOFF and DTR/DSR—The transfer mechanism uses the XON and XOFF characters and the
   DTR output signal and DSR input signal to perform flow control. The transfer mechanism
  5 controls input flow by sending XOFF and unasserting the DTR signal when the receive buffer is
    nearly full, and it controls the output flow by suspending transmission when XOFF is received
   and the DSR signal is unasserted.

•      VISA resource name out —

  VISA resource name out is a copy of the VISA resource name that VISA functions return.

•       error out —

                                                   © National Instruments 2675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2676 ordinal=2676 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

   VISAVISA ConfigureConfigure SerialSerial PortPort (Serial(Serial Instr)Instr) VIVI

        Initializes the serial port specified by VISA resource name to the specified settings.
       Wire data to the VISA resource name input to determine the polymorphic instance to
      use or manually select the instance.


      Inputs/Outputs

               •      Enable Termination Char (T) —

           Enable Termination Char prepares the serial device to recognize termination char.

                    If TRUE (default), the VI_ATTR_ASRL_END_IN attribute is set to recognize the termination
             character. If FALSE, the VI_ATTR_ASRL_END_IN attribute is set to 0 (None) and the serial device
           does not recognize the termination char.

               •      termination char (0xA = '\n' = LF) —

            termination char calls for termination of the read operation. The read operation terminates
          when the termination char is read from the serial device.

         0xA is the hex equivalent of a linefeed character (\n). Change the termination char to 0xD for
           message strings that terminate with a carriage return (\r).

               •      timeout (10sec) —

           timeout specifies the time, in milliseconds, for the write and read operations.


2676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2677 ordinal=2677 -->
## Functions

Functions


  The default is 10000.

•      VISA resource name —

  VISA resource name specifies the resource to be opened. The VISA resource name control also
  specifies the session and class.

•     baud rate (9600) —

  baud rate is the rate of transmission.

  The default is 9600.

•      data bits (8) —

  data bits is the number of bits in the incoming data.

  The value of data bits is between five and eight. The default value is 8.

•       parity (0:none) —

  parity specifies the parity used for every frame to be transmitted or received.

  This input accepts the following values.

         no parity  0
            (default)
  1      odd parity
  2       even parity
  3      mark parity
  4       space parity

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      stop bits (10: 1 bit) —

  stop bits specifies the number of stop bits used to indicate the end of a frame.

  This input accepts the following values.


                                                   © National Instruments 2677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2678 ordinal=2678 -->
## Functions

Functions


           10            1 stop bit
           15              1.5 stop bits
           20            2 stop bits

               •      flow control (0:none) —

            flow control sets the type of control used by the transfer mechanism.

             This input accepts the following values.

           None (default)—The transfer mechanism does not use flow control. Buffers on both sides of the           0             connection are assumed to be large enough to hold all data transferred.
           XON/XOFF—The transfer mechanism uses the XON and XOFF characters to perform flow
               control. The transfer mechanism controls input flow by sending XOFF when the receive buffer           1                  is nearly full, and it controls the output flow by suspending transmission when XOFF is
              received.
           RTS/CTS—The transfer mechanism uses the RTS output signal and the CTS input signal to
             perform flow control. The transfer mechanism controls input flow by unasserting the RTS           2               signal when the receive buffer is nearly full, and it controls output flow by suspending the
              transmission when the CTS signal is unasserted.
           XON/XOFF and RTS/CTS—The transfer mechanism uses the XON and XOFF characters and the
           RTS output signal and CTS input signal to perform flow control. The transfer mechanism
           3 controls input flow by sending XOFF and unasserting the RTS signal when the receive buffer is
              nearly full, and it controls the output flow by suspending transmission when XOFF is received
           and the CTS is unasserted.
           DTR/DSR—The transfer mechanism uses the DTR output signal and the DSR input signal to
             perform flow control. The transfer mechanism controls input flow by unasserting the DTR           4               signal when the receive buffer is nearly full, and it controls output flow by suspending the
              transmission when the DSR signal is unasserted.
           XON/XOFF and DTR/DSR—The transfer mechanism uses the XON and XOFF characters and the
           DTR output signal and DSR input signal to perform flow control. The transfer mechanism
           5 controls input flow by sending XOFF and unasserting the DTR signal when the receive buffer is
              nearly full, and it controls the output flow by suspending transmission when XOFF is received
           and the DSR signal is unasserted.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —


2678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2679 ordinal=2679 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

VISAVISA WriteWrite FunctionFunction

Writes the data from write buffer to the device or interface specified by VISA resource
name.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      write buffer —

    write buffer contains the data to be written to the device.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      return count —

    return count contains the actual number of bytes written.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 2679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2680 ordinal=2680 -->
## Functions

Functions

      Whether the data is transferred synchronously or asynchronously is platform-
      dependent. Right-click the node and select Synchronous I/O Mode»Synchronous from
       the shortcut menu to write data synchronously.

     When you transfer data from or to a hardware driver synchronously, the calling thread
         is locked for the duration of the data transfer. Depending on the speed of the transfer,
        this can hinder other processes that require the calling thread. However, if an
       application requires that the data transfer as quickly as possible, performing the
       operation synchronously dedicates the calling thread exclusively to this operation.

           Note In most applications, synchronous calls are slightly faster when you
              are communicating with four or fewer instruments. Asynchronous operations
                result in a significantly faster application when you are communicating with
                 five or more instruments. The LabVIEW default is asynchronous I/O.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\Serial\Serial.lvproj
            • labview\examples\Instrument IO\GPIB\GPIB with VISA
        functions.vi
   VISAVISA ReadRead FunctionFunction

      Reads the specified number of bytes from the device or interface specified by VISA
       resource name and returns the data in read buffer.


      Inputs/Outputs

               •      VISA resource name —


2680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2681 ordinal=2681 -->
## Functions

Functions


    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      byte count —

    byte count is the number of bytes to be read.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      read buffer —

    read buffer contains the data read from the device.

   •      return count —

    return count contains the number of bytes actually read.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This function might return less than the number of bytes requested if the function
reaches the end of the buffer, reaches a termination character, or if a timeout occurs.
The output error cluster indicates if a timeout has occurred.

Whether the data is read synchronously or asynchronously is platform-dependent.
Right-click the node and select Synchronous I/O Mode»Synchronous from the
shortcut menu to read data synchronously.

When you transfer data from or to a hardware driver synchronously, the calling thread
is locked for the duration of the data transfer. Depending on the speed of the transfer,
this can hinder other processes that require the calling thread. However, if an
application requires that the data transfer as quickly as possible, performing the
operation synchronously dedicates the calling thread exclusively to this operation.

                                                    © National Instruments 2681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2682 ordinal=2682 -->
## Functions

Functions

           Note In most applications, synchronous calls are slightly faster when you
              are communicating with 4 or fewer instruments. Asynchronous operations
                result in a significantly faster application when you are communicating with 5
              or more instruments. The LabVIEW default is asynchronous I/O.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\Serial\Continuous Serial
        Write and Read.vi
            • labview\examples\Instrument IO\VISA\USB\USB RAW - Bulk.vi
            • labview\examples\Instrument IO\GPIB\GPIB with VISA
        functions.vi
   VISAVISA CloseClose FunctionFunction

       Closes a device session or event object specified by VISA resource name.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —


2682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2683 ordinal=2683 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Error I/O operates uniquely in this function. The function closes the device session
regardless of whether an error occurred in a preceding operation. For each VISA
session that you open, you should close the session when you are finished with it. This
function accepts all available classes.

You also can use the Open VISA Session Monitor VI in the labview\vi.lib\
Utility\visa.llb to close all open VISA sessions. Alternatively, you could save
work, exit, and re-enter LabVIEW. Exiting LabVIEW closes all open VISA sessions. You
also can select the Automatically close VISA sessions option on the Environment
page of the Options dialog box.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Continuous Serial
   Write and Read.vi
  • labview\examples\Instrument IO\VISA\PXI\PXI - Route
   Trigger.vi
  • labview\examples\Instrument IO\GPIB\GPIB with VISA
   functions.vi
  • labview\examples\Instrument IO\VISA\USB\USB RAW -
   Interrupt.vi
VISAVISA BytesBytes atat SerialSerial PortPort

Returns the number of bytes in the input buffer of the specified serial port.

The Number of Bytes at Serial Port property specifies the number of bytes currently
available at the serial port used by this session.

Visa Bytes at Serial Port is a Property Node with a VISA class of Instr.


                                                    © National Instruments 2683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2684 ordinal=2684 -->
## Functions

Functions


      Inputs/Outputs

               •      reference —

               •       error in (no error) —

               •      reference out —

               •       error out —

               •       Serial Settings:Number of Bytes at Serial Port —

   VISAVISA SerialSerial BreakBreak

      Sends a break on the specified output port. Wire data to the VISA resource name input
       to determine the polymorphic instance to use or manually select the instance.


            • VISA Serial Break (Instr) VI
            • VISA Serial Break (Serial Instr) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\Serial\Set Serial Break
        Event.vi


2684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2685 ordinal=2685 -->
## Functions

Functions

VISAVISA SerialSerial BreakBreak (Instr)(Instr) VIVI

Sends a break on the specified output port. Wire data to the VISA resource name input
to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      Duration (-1 : use default) —

    Duration specifies the length of the break in milliseconds.

    While the VI runs, this value temporarily overrides the current setting of the VISA Serial
    Settings:Break Length property. Afterwards, the VI returns the current setting to its original
     value.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 2685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2686 ordinal=2686 -->
## Functions

Functions

            • labview\examples\Instrument IO\Serial\Set Serial Break
        Event.vi
   VISAVISA SerialSerial BreakBreak (Serial(Serial Instr)Instr) VIVI

      Sends a break on the specified output port. Wire data to the VISA resource name input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      Duration (-1 : use default) —

            Duration specifies the length of the break in milliseconds.

            While the VI runs, this value temporarily overrides the current setting of the VISA Serial
             Settings:Break Length property. Afterwards, the VI returns the current setting to its original
             value.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2687 ordinal=2687 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Set Serial Break
   Event.vi
VISAVISA SetSet I/OI/O BufferBuffer SizeSize FunctionFunction

Sets the size of the I/O buffer. Run the VISA Configure Serial Port VI first if you are
setting the size of a serial port buffer.

      Note Not all serial drivers support user-defined buffer sizes so some
       implementations of VISA might not be able to perform this operation. If an
        application requires a specific buffer size for performance reasons and the
       VISA implementation cannot guarantee that size, use some form of
       handshaking to prevent overflow conditions.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •     mask (16) —

   mask designates which buffer size to set.

    16     I/O Receive Buffer
    32     I/O Transmit Buffer
    48     I/O Receive and Transmit Buffer


                                                    © National Instruments 2687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2688 ordinal=2688 -->
## Functions

Functions

               •       size (4096) —

             size designates the size of the I/O buffer in bytes. Set size slightly higher than the amount of data
           you expect to transmit or receive. If you call this function without specifying a buffer size, this
             function sets the buffer size to 4096 bytes. If you do not call this function, the buffer size depends
          on both VISA and the operating system configuration.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\Serial\Continuous Serial
        Write and Read.vi
   VISAVISA FlushFlush I/OI/O BufferBuffer FunctionFunction

       Flushes the I/O buffer specified by mask.


      Inputs/Outputs

               •      VISA resource name —


2688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2689 ordinal=2689 -->
## Functions

Functions


    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •     mask (16) —

   mask designates the buffer to flush.

    Combine the buffer masks by bit to flush more than one buffer simultaneously. Use logical OR,
    also known as OR-ing or adding, to combine the values. Use only one mask value for the receive
     buffer and only one mask value for the transmit buffer.

    This input accepts the following values.

    Mask    Hex                      Description
    Values   Codes
    16       0x10    Flushes and discards contents of the receive buffer (same as 64).
                      Flushes and discards contents of the transmit buffer by writing all the    32       0x20                      buffered data to the device.
                      Flushes and discards contents of the receive buffer (does not perform any I/O    64       0x40                       to the device).
                      Flushes and discards contents of the transmit buffer (does not perform any    128      0x80                       I/O to the device).

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

VISAVISA USBUSB

Use the VISA USB VI and functions to control USB devices.


                                                    © National Instruments 2689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2690 ordinal=2690 -->
## Functions

Functions

      The VI and functions on this palette can return VISA error codes.


         Palette Object               Description

        VISA USB Control In Function  Performs a USB control pipe transfer from a USB device.

        VISA USB Control Out                                   Performs a USB control pipe transfer to the device.         Function

                                       Retrieves the interrupt data that is stored in a VISA USB interrupt        VISA Get USB Interrupt Data                                       event.

   VISAVISA USBUSB ControlControl InIn FunctionFunction

      Performs a USB control pipe transfer from a USB device.


      Inputs/Outputs

               •      index (0) —

            index passes a parameter to the device. The value you enter here depends on the value you
            entered in request.

          The index is often used in requests to specify an endpoint or an interface.
               •      value (0) —

            value passes a parameter to the device. The value you enter here depends on the value you
            enter in request.


2690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2691 ordinal=2691 -->
## Functions

Functions

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      request type —

    request type is the numeric representation of the request you want to send to the device.

    This parameter is a bitmapped field that identifies the characteristics of the specific request. The
     bit specifying the direction must be set to 1 (device-to-host).
   •      request —

    request specifies the particular request. The request you can enter depends on the value you
    entered in request type.

   •      length (0) —

    length specifies the length of the data transferred during the second phase of the control
     transfer. The direction is device-to-host.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      read buffer —

    read buffer contains the data read from the device.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This function takes the values of the data payload in the setup stage of the control
transfer as parameters. The function reads the optional data buffer read buffer if you
require a data stage for this transfer.


                                                    © National Instruments 2691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2692 ordinal=2692 -->
## Functions

Functions

           Note This function is only intended for users familiar with the USB protocol.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\VISA\USB\USB RAW -
        Control.vi
   VISAVISA USBUSB ControlControl OutOut FunctionFunction

      Performs a USB control pipe transfer to the device.


      Inputs/Outputs

               •      index (0) —

            index passes a parameter to the device. The value you enter here depends on the value you
            entered in request.

          The index is often used in requests to specify an endpoint or an interface.
               •      value (0) —

            value passes a parameter to the device. The value you enter here depends on the value you
            enter in request.

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      request type —


2692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2693 ordinal=2693 -->
## Functions

Functions


    request type is the numeric representation of the request you want to send to the device.

    This parameter is a bitmapped field that identifies the characteristics of the specific request. The
     bit specifying the direction must be set to 0 (host-to-device).
   •      request —

    request specifies the particular request. The request you can enter depends on the value you
    entered in request type.

   •      write buffer (empty) —

    write buffer contains the data to be written to the device.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This function takes the values of the data payload in the setup stage of the control
transfer as parameters. The function sends an optional data buffer write buffer if you
require a data stage for this transfer.

      Note This function is only intended for users familiar with the USB protocol.
VISAVISA GetGet USBUSB InterruptInterrupt DataData

Retrieves the interrupt data that is stored in a VISA USB interrupt event.


                                                    © National Instruments 2693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2694 ordinal=2694 -->
## Functions

Functions


      Inputs/Outputs

               •      VISA USB Intr Event —

           VISA USB Intr Event is a unique logical identifier to a VISA USB Interrupt Event.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA USB Intr Event out —

           VISA USB Intr Event out is a copy of the VISA USB Intr Event that is passed out of the VISA
             functions.

               •      data buffer —

           data buffer is the buffer of USB interrupt data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA SetSet I/OI/O BufferBuffer SizeSize FunctionFunction

       Sets the size of the I/O buffer. Run the VISA Configure Serial Port VI first if you are
        setting the size of a serial port buffer.

           Note Not all serial drivers support user-defined buffer sizes so some
              implementations of VISA might not be able to perform this operation. If an
               application requires a specific buffer size for performance reasons and the
              VISA implementation cannot guarantee that size, use some form of
             handshaking to prevent overflow conditions.


2694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2695 ordinal=2695 -->
## Functions

Functions


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •     mask (16) —

   mask designates which buffer size to set.

    16     I/O Receive Buffer
    32     I/O Transmit Buffer
    48     I/O Receive and Transmit Buffer

   •       size (4096) —

     size designates the size of the I/O buffer in bytes. Set size slightly higher than the amount of data
    you expect to transmit or receive. If you call this function without specifying a buffer size, this
    function sets the buffer size to 4096 bytes. If you do not call this function, the buffer size depends
    on both VISA and the operating system configuration.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 2695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2696 ordinal=2696 -->
## Functions

Functions

            • labview\examples\Instrument IO\Serial\Continuous Serial
        Write and Read.vi
   VISAVISA FlushFlush I/OI/O BufferBuffer FunctionFunction

       Flushes the I/O buffer specified by mask.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •     mask (16) —

         mask designates the buffer to flush.

          Combine the buffer masks by bit to flush more than one buffer simultaneously. Use logical OR,
             also known as OR-ing or adding, to combine the values. Use only one mask value for the receive
             buffer and only one mask value for the transmit buffer.

             This input accepts the following values.

          Mask    Hex
                              Description
            Values   Codes
           16       0x10    Flushes and discards contents of the receive buffer (same as 64).
                             Flushes and discards contents of the transmit buffer by writing all the
           32       0x20
                              buffered data to the device.
                             Flushes and discards contents of the receive buffer (does not perform any I/O
           64       0x40
                               to the device).
                             Flushes and discards contents of the transmit buffer (does not perform any
           128      0x80
                                I/O to the device).

               •       error in (no error) —


2696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2697 ordinal=2697 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

VISAVISA GPIBGPIB CommandCommand FunctionFunction

Writes GPIB command bytes on the bus.

      Note GPIB Command does not accept VISA sessions of class Instr. The VISA
        session must be of class GPIB BoardInterface.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •     command —

   command The command bytes should be valid IEEE 488-defined Multiline Interface Messages.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

                                                    © National Instruments 2697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2698 ordinal=2698 -->
## Functions

Functions


           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      return count —

            return count is the number of bytes actually transferred.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA GPIBGPIB ControlControl ATNATN FunctionFunction

       Controls the state of the GPIB ATN interface line and, optionally, the active controller
        state of the local interface.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •     mode —

         mode specifies the state of the ATN line and optionally the local active controller state.

             This input accepts the following values.

             Deassert ATN—Deassert ATN line. The GPIB interface corresponding to the VISA session goes to
           0
              standby.
              Assert ATN—Assert ATN line and take control synchronously without corrupting transferred
           1
              data. If a data handshake is in progress, ATN is not asserted until the handshake is complete.
             Deassert ATN with Handshake—Deassert ATN line and enter shadow handshake mode. The
           2
               local device participates in data handshakes as an Acceptor without actually reading the data.


2698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2699 ordinal=2699 -->
## Functions

Functions


     The GPIB interface corresponding to the VISA session goes to standby.
      Assert ATN Immediately—Assert ATN line and take control asynchronously and immediately,
    3 without regard for any data transfer currently in progress. Use this mode only under error
      conditions.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Most applications do not require this function. You can use the VISA GPIB Command
function to modify the ATN automatically and the VISA GPIB Pass Control function to
modify the ATN and controller-in-charge (CIC) state automatically.

      Note GPIB Command does not accept VISA sessions of class Instr. The VISA
        session must be of class GPIB BoardInterface.
VISAVISA GPIBGPIB PassPass ControlControl FunctionFunction

Tells the GPIB device at the specified address to become controller-in-charge (CIC).


Inputs/Outputs

   •      VISA resource name —


                                                    © National Instruments 2699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2700 ordinal=2700 -->
## Functions

Functions


           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      primary address —

           primary address is the primary address of the GPIB device to which you want to pass control.

               •      secondary address (none) —

           secondary address is the secondary address of the targeted GPIB device.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This function passes CIC status to the device specified by primary address and
      secondary address and deasserts the ATN line. This function assumes that the
       targeted device has controller capability.

           Note VISA GPIB Pass Control does not accept VISA sessions of class Instr. The
              VISA session must be of class GPIB BoardInterface.
   VISAVISA GPIBGPIB SendSend IFCIFC FunctionFunction

       Pulses the interface clear line (IFC) for at least 100 microseconds.

       This function asserts the IFC line and becomes the controller-in-charge (CIC). The local
       device must be the system controller.


2700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2701 ordinal=2701 -->
## Functions

Functions

      Note VISA GPIB Send IFC does not accept VISA sessions of class Instr. The
       VISA session must be of class GPIB BoardInterface.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

VISAVISA GPIBGPIB ControlControl RENREN FunctionFunction

Asserts or deasserts the GPIB REN interface line according to the specified mode.

mode also can specify the remote/local state of the device.

      Note VISA GPIB Control REN is valid only if the GPIB interface associated
       with the specified session is currently the system controller.


                                                    © National Instruments 2701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2702 ordinal=2702 -->
## Functions

Functions


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •     mode —

         mode specifies the state of the REN line and optionally the device remote/local state.

             This input accepts the following values.

           0 Deassert REN—Deassert REN line.
           1 Assert REN—Assert REN line.
           2 Go To Local; Deassert REN—Send the Go To Local (GTL) command and deassert REN line.
           3 Assert REN; Address Device—Assert REN line and address device.
           4 Local Lockout (Addressed Devices)—Send LLO to any devices that are addressed to listen.
           5 Local Lockout (This Device)—Address this device and send it LLO, putting it in RWLS.
           6 Go To Local—Send the Go To Local command (GTL) to this device.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA VXIVXI CmdCmd oror QueryQuery FunctionFunction

      Sends the device a miscellaneous command or query and/or retrieves the response to


2702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2703 ordinal=2703 -->
## Functions

Functions

a previous query.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •     mode (x200: 16-bit cmd) —

   mode specifies whether to issue a command and/or retrieve a response.

          Note The mode you specify can cause all or part of the command or response
            parameters to be ignored. The possible results of specifying a particular mode are the
              following:
                         •  If mode specifies sending a 16-bit command, the upper half of command is
                    ignored.
                         •  If mode specifies retrieving a response only, command is ignored.
                         •  If mode specifies sending a command only, response is ignored.
                         •  If mode specifies to retrieve a 16-bit value, the upper half of response is set to
                       0.

    This input accepts the following values.

    0x0002      Get 16-bit Response From Previous Query
    0x0004      Get 32-bit Response From Previous Query
    0x0200      Send 16-bit Command
    0x0202      Send 16-bit Query; Get 16-bit Response
    0x0400      Send 32-bit Command
    0x0402      Send 32-bit Query; Get 16-bit Response
    0x0404      Send 32-bit Query; Get 32-bit Response

   •     command —

   command is the miscellaneous command to send.


                                                    © National Instruments 2703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2704 ordinal=2704 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      response —

           response is the response retrieved from the device.

                    If the mode specifies to send a command rather than retrieve a response, you can use VI_NULL
              for this parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA AssertAssert InterruptInterrupt SignalSignal FunctionFunction

       Asserts the specified device interrupt or signal.

        In VXI, for example, this can be done with either a VXI signal or a VXI interrupt. On
       certain bus types, statusID may be ignored.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •     mode —


2704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2705 ordinal=2705 -->
## Functions

Functions


   mode specifies how to assert the interrupt.

    This input accepts the following values.

    –1 VXI Signal—Send the notification using a VXI signal.
    0  Assigned Method—Use the notification method assigned to the local device.
       VXI/VME IRQ1–VXI/VME IRQ7—Send the interrupt through the specified VXI/VME IRQ line.
    1–7 This uses the standard VXI/VME ROAK (release on acknowledge) interrupt mechanism rather
       than the older VME RORA (release on register access) mechanism.

   •       status ID —

    status ID is the status value to be presented during an interrupt acknowledge cycle.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


      Note VISA Assert Interrupt Signal does not accept VISA sessions of class
         Instr. The VISA session must be of class VXI/GPIB-VXI Backplane or VXI
        Servant.
VISAVISA AssertAssert UtilityUtility SignalSignal FunctionFunction

Asserts or deasserts the specified utility bus signal.


                                                    © National Instruments 2705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2706 ordinal=2706 -->
## Functions

Functions

      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      bus signal —

           bus signal specifies the utility bus signal to assert.

             This input accepts the following values.

           1     Assert SYSRESET
           2     Assert SYSFAIL
           3     Deassert SYSFAIL

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This function can assert the SYSFAIL or SYSRESET utility bus interrupts on the VXI
       backplane.

           Note VISA Assert Utility Signal does not accept VISA sessions of class Instr.
            The VISA session must be of class VXI/GPIB-VXI Backplane or VXI Servant.
   VISAVISA MapMap TriggerTrigger FunctionFunction

      Maps the specified trigger source line to the specified trigger destination line.


2706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2707 ordinal=2707 -->
## Functions

Functions


Inputs/Outputs

   •     mode —

   mode is VI_NULL.

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       trigger source —

     trigger source is the source line from which to map.

    This input accepts the following values.

    0–7 VXI/PXI TTL Line 0–VXI/PXI TTL Line 7—Map the specified VXI TTL trigger line.
    27  Front Panel Input—Map the controller's front panel trigger input line.
    28  Front Panel Output—Map the controller's front panel trigger output line.
    8   VXI ECL Line 0—Map the specified VXI ECL trigger line.
    9   VXI ECL Line 1—Map the specified VXI ECL trigger line.

   •       trigger destination —

     trigger destination is the destination line to which to map.

    This input accepts the following values.

    0–7 VXI/PXI TTL Line 0–VXI/PXI TTL Line 7—Map the specified VXI TTL trigger line.
    27  Front Panel Input—Map the controller's front panel trigger input line.
    28  Front Panel Output—Map the controller's front panel trigger output line.
    8   VXI ECL Line 0—Map the specified VXI ECL trigger line.
    9   VXI ECL Line 1—Map the specified VXI ECL trigger line.

   •       error in (no error) —


                                                    © National Instruments 2707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2708 ordinal=2708 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           Note VISA Map Trigger does not accept VISA sessions of class Instr. The VISA
               session must be of class PXI Backplane or VXI/GPIB-VXI Backplane.

           If this function is called multiple times on the same backplane resource with the same
       trigger source line and different trigger destination lines, all of the specified trigger
       destination lines are asserted when the trigger source line is asserted. If this function
         is called multiple times on the same backplane resource with different trigger source
        lines and the same trigger destination line, the trigger destination line is asserted
     when any of the specified trigger source lines are asserted.
   VISAVISA UnmapUnmap TriggerTrigger FunctionFunction

     Unmaps a previous map from the specified trigger source line to the specified trigger
       destination line. This function unmaps one trigger mapping per call.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also


2708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2709 ordinal=2709 -->
## Functions

Functions


     specifies the session and class.

   •       trigger source —

     trigger source is the source line used in the previous map.

    This input accepts the following values.

    0–7 VXI/PXI TTL Line 0–VXI/PXI TTL Line 7—Unmap the specified trigger line.
    27  Front Panel Input—Unmap the controller's front panel trigger input line.
    28  Front Panel Output—Unmap the controller's front panel trigger output line.
    8   VXI ECL Line 0—Unmap the specified VXI ECL trigger line.
    9   VXI ECL Line 1—Unmap the specified VXI ECL trigger line.

   •       trigger destination (all) —

     trigger destination is the destination line used in the previous map.

    This input accepts the following values.

    –2  All Connected Lines—Unmap all trigger lines to which the source is currently connected.
    0–7 VXI/PXI TTL Line 0–VXI/PXI TTL Line 7—Unmap the specified VXI TTL trigger line.
    27 Front Panel Input—Unmap the controller's front panel trigger input line.
    28 Front Panel Output—Unmap the controller's front panel trigger output line.
    8  VXI ECL Line 0—Unmap the specified VXI ECL trigger line.
    9  VXI ECL Line 1—Unmap the specified VXI ECL trigger line.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If VISA Map Trigger was previously called multiple times on the same backplane

                                                    © National Instruments 2709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2710 ordinal=2710 -->
## Functions

Functions

       resource and created multiple mappings for either trigger source or trigger
       destination, trigger mappings that you do not specify in trigger source or trigger
       destination in this function remain in effect when the unmap operation completes.

           Note This function does not accept VISA sessions of class Instr. The VISA
               session must be of class PXI Backplane or VXI/GPIB-VXI Backplane.

      VISAVISA WriteWrite FromFrom FileFile FunctionFunction

      Takes data from the file specified by filename and writes it to the device
       synchronously.

      filename opens in binary mode and the function reads the amount of data specified by
       count. The data is then written to the device. This operation returns only when the
        transfer terminates.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      filename —

            filename is the name of file from which data will be read.

               •      count (entire file) —

           count is the number of bytes to be written.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


2710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2711 ordinal=2711 -->
## Functions

Functions

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      return count —

    return count is the number of bytes actually transferred.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


VISAVISA ReadRead ToTo FileFile FunctionFunction

Reads byte count synchronously and stores the transferred data in the file specified by
filename.

filename opens in binary mode. Any existing contents are destroyed if you set the
Message Based Settings:File Append Enable property to FALSE. The data is then
written to the file. The operation returns only when the transfer terminates.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      filename —

    filename is the name of file to which data will be written.

   •      byte count —

    byte count is the number of bytes to be read.

   •       error in (no error) —

                                                    © National Instruments 2711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2712 ordinal=2712 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      return count —

            return count is the number of bytes actually transferred.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      EventEvent HandlingHandling

      Use the Event Handling VIs and functions to use VISA events with your instruments.

      The VIs and functions on this palette can return VISA error codes.

      You also can access the Select Event Type constant from this palette.


         Palette
                       Description
        Object

        VISA Enable
        Event        Enables notification of a specified event type.
         Function

        VISA Wait on
                    Suspends execution of an application thread and waits for an event type for a time
        Event
                      period not to exceed that specified by timeout.
         Function

        VISA Disable
        Event         Disables servicing of an event.
         Function

        VISA Discard  Discards all pending occurrences of the specified event type and mechanism from

2712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2713 ordinal=2713 -->
## Functions

Functions


 Palette               Description
 Object

 Events              the specified session. Function

              Waits for a service request from a device. Before you call this VI, first enable the
 Wait for RQS  event by calling the VISA Enable Event function and specifying Service Request as
              the event type.

 Select Event             Use this control to select the desired event type. Type VI

VISAVISA EnableEnable EventEvent FunctionFunction

Enables notification of a specified event type.

      Note You must call the VISA Enable Event function for a session before using
       the VISA Wait on Event function.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      event type —

    event type is the logical event identifier.

    You can select from the following VISA event types.


                                                    © National Instruments 2713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2714 ordinal=2714 -->
## Functions

Functions


             Service Request (default)                         0x3FFF200B
             Trigger                                     0xBFFF200A
             Clear                                       0x3FFF200D
             VXI Signal                                   0x3FFF2020
           VXI/VME Interrupt                              0xBFFF2021
           VXI/VME Sysfail                                0x3FFF201D
           VXI/VME Sysreset                              0x3FFF201E
           GPIB CIC                                    0x3FFF2012
           GPIB Talk                                    0x3FFF2013
           GPIB Listen                                  0x3FFF2014
             PXI Interrupt                                  0x3FFF2022
              Serial Break                                  0x3FFF2023
              Serial TermChar                               0x3FFF2024
              Serial CTS                                   0x3FFF2029
              Serial DSR                                   0x3FFF202A
              Serial DCD                                   0x3FFF202C
              Serial RI                                     0x3FFF202E
              Serial Character                               0x3FFF2035
         USB Interrupt                                 0x3FFF2037
                All Enabled                                  0x3FFF7FFF

             Refer to the NI-VISAHelpfor more information about event types.

               •     mechanism (1: VI_QUEUE) —

          mechanism specifies the event handling mechanism to be disabled.

             Currently only accepts VI_QUEUE (1).

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2715 ordinal=2715 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Detect Serial Break
   Event.vi
  • labview\examples\Instrument IO\GPIB\SRQ Event Handling.vi
VISAVISA WaitWait onon EventEvent FunctionFunction

Suspends execution of an application thread and waits for an event type for a time
period not to exceed that specified by timeout.


Inputs/Outputs

   •      timeout (0) —

    timeout specifies the time, in milliseconds, that the function waits for the event.

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •      event type (all enabled) —

    event type is the logical event identifier.

    You can select from the following VISA event types.

    Service Request                            0x3FFF200B
     Trigger                                  0xBFFF200A
    Clear                                   0x3FFF200D


                                                    © National Instruments 2715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2716 ordinal=2716 -->
## Functions

Functions


             VXI Signal                                0x3FFF2020
           VXI/VME Interrupt                           0xBFFF2021
           VXI/VME Sysfail                             0x3FFF201D
           VXI/VME Sysreset                           0x3FFF201E
           GPIB CIC                                 0x3FFF2012
           GPIB Talk                                0x3FFF2013
           GPIB Listen                               0x3FFF2014
             PXI Interrupt                              0x3FFF2022
              Serial Break                               0x3FFF2023
              Serial TermChar                            0x3FFF2024
              Serial CTS                                0x3FFF2029
              Serial DSR                                0x3FFF202A
              Serial DCD                                0x3FFF202C
              Serial RI                                 0x3FFF202E
              Serial Character                            0x3FFF2035
         USB Interrupt                              0x3FFF2037
                All Enabled (default)                         0x3FFF7FFF

             Refer to the NI-VISAHelpfor more information about event types.

               •      event class (Generic Event) —

           event class specifies the class of event for which the function waits. The default is Generic
          Event, meaning the function recognizes any class of event.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      event type out —

           event type out identifies the event type received if the wait was successful.

               •      event —

           event is valid if the wait was successful.


2716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2717 ordinal=2717 -->
## Functions

Functions

    Wire event to a Property Node to get further information about the event. Wire event to the VISA
    Close function when examination of the event is complete.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


You can set this function to perform I/O operations synchronously or asynchronously.
By default, the function handles I/O operations asynchronously. Right-click the
function and select Synchronous I/O Mode»Synchronous from the shortcut menu to
synchronously wait for an occurrence of the specified event.

      Note In most applications, synchronous calls are slightly faster when you
        are communicating with 4 or fewer instruments. Asynchronous operations
        result in a significantly faster application when you are communicating with 5
        or more instruments. The LabVIEW default is asynchronous I/O.

Refer to individual event descriptions for context definitions. If the specified event
type is All Events (0x3FFF7FFF), the operation waits for any event that is enabled for
the given session.

      Note You must call the VISA Enable Event function for a given session before
       using the VISA Wait on Event function.

If a session's event queue becomes full and a new event arrives, the new event is
discarded. The default event queue size per session is 50. If you expect more than 50
unhandled events to arrive, you can use the General Settings:Maximum Queue Length
property to set event queue size programmatically.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Detect Serial Break
   Event.vi


                                                    © National Instruments 2717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2718 ordinal=2718 -->
## Functions

Functions

   VISAVISA DisableDisable EventEvent FunctionFunction

       Disables servicing of an event.

       This operation prevents new event occurrences from being queued. However, event
       occurrences already queued are not lost. Use the VISA Discard Events VI to discard
      queued events.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      event type (all enabled) —

           event type is the logical event identifier.

           You can select from the following VISA event types.

             Service Request                            0x3FFF200B
             Trigger                                  0xBFFF200A
             Clear                                   0x3FFF200D
             VXI Signal                                0x3FFF2020
           VXI/VME Interrupt                           0xBFFF2021
           VXI/VME Sysfail                             0x3FFF201D
           VXI/VME Sysreset                           0x3FFF201E
           GPIB CIC                                 0x3FFF2012
           GPIB Talk                                0x3FFF2013
           GPIB Listen                               0x3FFF2014
             PXI Interrupt                              0x3FFF2022
              Serial Break                               0x3FFF2023
              Serial TermChar                            0x3FFF2024


2718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2719 ordinal=2719 -->
## Functions

Functions


     Serial CTS                                0x3FFF2029
     Serial DSR                                0x3FFF202A
     Serial DCD                                0x3FFF202C
     Serial RI                                 0x3FFF202E
     Serial Character                            0x3FFF2035
   USB Interrupt                              0x3FFF2037
      All Enabled (default)                         0x3FFF7FFF

    Refer to the NI-VISAHelpfor more information about event types.

   •     mechanism (1: VI_QUEUE) —

   mechanism specifies the event handling mechanism to be disabled.

    Currently only accepts VI_QUEUE (1).

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\GPIB\SRQ Event Handling.vi
VISAVISA DiscardDiscard EventsEvents FunctionFunction

Discards all pending occurrences of the specified event type and mechanism from the
specified session.

                                                    © National Instruments 2719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2720 ordinal=2720 -->
## Functions

Functions

       This function discards information about all the event occurrences that have not yet
      been handled. This behavior is useful if you want to remove event occurrences that an
       operation no longer needs. Discarded event occurrences are not available to a session
       at a later time.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      event type (all enabled) —

           event type is the logical event identifier.

           You can select from the following VISA event types.

             Service Request                            0x3FFF200B
             Trigger                                  0xBFFF200A
             Clear                                   0x3FFF200D
             VXI Signal                                0x3FFF2020
           VXI/VME Interrupt                           0xBFFF2021
           VXI/VME Sysfail                             0x3FFF201D
           VXI/VME Sysreset                           0x3FFF201E
           GPIB CIC                                 0x3FFF2012
           GPIB Talk                                0x3FFF2013
           GPIB Listen                               0x3FFF2014
             PXI Interrupt                              0x3FFF2022
              Serial Break                               0x3FFF2023
              Serial TermChar                            0x3FFF2024
              Serial CTS                                0x3FFF2029
              Serial DSR                                0x3FFF202A
              Serial DCD                                0x3FFF202C
              Serial RI                                 0x3FFF202E


2720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2721 ordinal=2721 -->
## Functions

Functions


     Serial Character                            0x3FFF2035
   USB Interrupt                              0x3FFF2037
      All Enabled (default)                         0x3FFF7FFF

    Refer to the NI-VISAHelpfor more information about event types.

   •     mechanism (1: VI_QUEUE) —

   mechanism specifies the event handling mechanism to be disabled.

    Currently only accepts VI_QUEUE (1).

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Detect Serial Break
   Event.vi
WaitWait forfor RQSRQS

Waits for a service request from a device. Before you call this VI, first enable the event
by calling the VISA Enable Event function and specifying Service Request as the event
type.

If the event arrives within the specified timeout period, the status byte of the device is

                                                    © National Instruments 2721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2722 ordinal=2722 -->
## Functions

Functions

       read and returned.


      Inputs/Outputs

               •      timeout (25000 ms) —

           timeout specifies the time, in milliseconds, that the VI waits for the event. The default is 25,000
           ms.

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       status byte —

             status byte is returned if the event arrives within the specified timeout period.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\GPIB\SRQ Event Handling.vi


2722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2723 ordinal=2723 -->
## Functions

Functions

SelectSelect EventEvent TypeType VIVI

Use this control to select the desired event type.


Data type

   •    —


 Service Request                                    3FFF200B

 Trigger                                           BFFF200A

 Clear                                             3FFF200D

 VXI Signal                                           3FFF2020

 VXI/VME Interrupt                                   BFFF2021

 VXI/VME Sysfail                                     3FFF201D

 VXI/VME Sysreset                                    3FFF201E

 GPIB CIC                                            3FFF2012

 GPIB Talk                                           3FFF2013

 GPIB Listen                                         3FFF2014

 PXI Interrupt                                        3FFF2022

 Serial Break                                         3FFF2023

 Serial TermChar                                     3FFF2024

 Serial CTS                                          3FFF2029

 Serial DSR                                          3FFF202A

 Serial DCD                                         3FFF202C

 Serial RI                                            3FFF202E

 Serial Character                                     3FFF2035

 USB Interrupt                                       3FFF2037

                                                    © National Instruments 2723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2724 ordinal=2724 -->
## Functions

Functions


           All Enabled                                         3FFF7FFF

      VISAVISA LockLock AsyncAsync

      Asynchronously attempts to establish access to the device or interface specified by
      VISA resource name. Use this function to obtain an exclusive lock that guarantees sole
       access to a device or resource.


      Inputs/Outputs

               •      lock type (exclusive: 1) —

            lock type specifies the type of lock you want to request for the session. You can specify a value
             of 1 or a 2 to mean an exclusive or shared lock, respectively. The default value is 1.

                    If a session has an exclusive lock, other sessions cannot modify global attributes or invoke
            operations but still can get attributes and set local attributes. If the session has a shared lock,
            other sessions that have shared locks also can modify global attributes and invoke operations.

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      timeout (0) —

           timeout specifies the time, in milliseconds, that the function waits for access to lock.

               •      requested key —

           requested key specifies a unique access key for the shared lock. This parameter is valid only if
           you specify a value of 2 for the lock type parameter.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


2724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2725 ordinal=2725 -->
## Functions

Functions


    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      access key —

    access key returns a unique access key for the lock if this VI runs successfully. You then can share
    the lock by wiring this output to other sessions. access key is valid only if you specify a value of 2
     for the lock type parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


You also can obtain shared locks. The locking mechanism works for all processes and
resources that exist on the same computer. Refer to the NI-VISAHelptopic on the
viLock function for more information about requesting keys and lock sharing.

If a locked VISA session is closed without first being unlocked, VISA automatically
performs a VISA Unlock operation on that session, regardless of the type of lock set on
the session.

VISAVISA UnlockUnlock FunctionFunction

Relinquishes the lock previously obtained using the VISA Lock Async function.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       error in (no error) —

                                                    © National Instruments 2725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2726 ordinal=2726 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\VISA\Locking\VISA
        Locking.vi

       RegisterRegister AccessAccess

      Use the Register Access functions to program in an address space at a high level.

      The functions on this palette can return VISA error codes.


         Palette Object     Description

        VISA In 8 Function Reads an 8-bit block of data from the specified address space and offset.

        VISA In 16
                        Reads a 16-bit block of data from the specified address space and offset.
         Function

        VISA In 32
                        Reads a 32-bit block of data from the specified address space and offset.
         Function

        VISA In 64
                        Reads a 64-bit block of data from the specified address space and offset.
         Function

        VISA Out 8         Writes an 8-bit block of data to the specified address space and offset.


2726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2727 ordinal=2727 -->
## Functions

Functions


Palette Object     Description

Function

VISA Out 16                   Writes a 16-bit block of data to the specified address space and offset.Function

VISA Out 32                   Writes a 32-bit block of data to the specified address space and offset.
Function

VISA Out 64                   Writes a 64-bit block of data to the specified address space and offset.Function

VISA Move In 8               Moves one or more 8-bit units of data from device memory to local memory.
Function

VISA Move In 16               Moves one or more 16-bit units of data from device memory to local memory.Function

VISA Move In 32               Moves one or more 32-bit units of data from device memory to local memory.Function

VISA Move In 64               Moves one or more 64-bit units of data from device memory to local memory.Function

VISA Move Out 8   Moves an array of 8-bit data from local memory to the specified address space
Function        and offset.

VISA Move Out 16  Moves an array of 16-bit data from local memory to the specified address space
Function        and offset.

VISA Move Out 32  Moves an array of 32-bit data from local memory to the specified address space
Function        and offset.

VISA Move Out 64  Moves an array of 64-bit data from local memory to the specified address space
Function        and offset.

VISA Memory
                    Allocates device memory of a specified size and returns the offset that specifies
Allocation
                where the memory is located.
Function

VISA Memory
                    Allocates device memory of a specified size and returns the offset that specifies
Allocation Ex
                where the memory is located.
Function

VISA Memory Free  Frees the memory previously allocated by the VISA Memory Allocation function
Function          or the VISA Memory Allocation Ex function.

VISA Move       Moves length elements of the given source width from the specified source
Function          address space and offset to the specified destination address space and offset.


                                                    © National Instruments 2727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2728 ordinal=2728 -->
## Functions

Functions


         Palette Object     Description

       Low Level        Use the Low Level Register Access functions to program in an address space
         Register Access    with more detail than is provided at a high level.

   VISAVISA InIn 88 FunctionFunction

      Reads an 8-bit block of data from the specified address space and offset.


      Inputs/Outputs

               •      address space (A16: 1) —

           address space specifies the address space without requiring VISA Map Address to be called. The
             following table lists the valid entries for specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)

                                               VXI/VME A24 (2)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A32 (3)

                                               VXI/VME A64 (4)


                                                    PXI Memory Allocations (9)

             PXI                                     PXI Configuration (10)

                                                    PXI BAR0 (11) to PXI BAR5 (16)


               •      VISA resource name —

2728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2729 ordinal=2729 -->
## Functions

Functions


    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset is the offset, in bytes, of the device to read from.

     offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
     offset specifies the offset.
         • INSTR Specific—The offset specified in the VISA In 8, VISA In 16, VISA In 32, and VISA In 64
        operations for an INSTR Resource is the offset address relative to the device's allocated
        address base for the corresponding address space that was specified. For example, if
        address space specifies VXI/VME A16, offset specifies the offset from the logical address
        base address of the specified VXI device. If address space specifies VXI/VME A24, A32, or A64,
         offset specifies the offset from the base address of the VXI device's memory space allocated
       by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
         • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      value —

    value contains the data read from address space.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

VISAVISA InIn 1616 FunctionFunction

Reads a 16-bit block of data from the specified address space and offset.


                                                    © National Instruments 2729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2730 ordinal=2730 -->
## Functions

Functions


      Inputs/Outputs

               •      address space (A16: 1) —

           address space specifies the address space without requiring VISA Map Address to be called. The
             following table lists the valid entries for specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)

                                               VXI/VME A24 (2)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A32 (3)

                                               VXI/VME A64 (4)


                                                    PXI Memory Allocations (9)

             PXI                                     PXI Configuration (10)

                                                    PXI BAR0 (11) to PXI BAR5 (16)


               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       offset (0) —

             offset is the offset, in bytes, of the device to read from.

             offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
             offset specifies the offset.
                     • INSTR Specific—The offset specified in the VISA In 8, VISA In 16, VISA In 32, and VISA In 64
                operations for an INSTR Resource is the offset address relative to the device's allocated
                address base for the corresponding address space that was specified. For example, if
               address space specifies VXI/VME A16, offset specifies the offset from the logical address

2730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2731 ordinal=2731 -->
## Functions

Functions

        base address of the specified VXI device. If address space specifies VXI/VME A24, A32, or A64,
         offset specifies the offset from the base address of the VXI device's memory space allocated
       by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
         • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      value —

    value contains the data read from address space.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

VISAVISA InIn 3232 FunctionFunction

Reads a 32-bit block of data from the specified address space and offset.


Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space without requiring VISA Map Address to be called. The
    following table lists the valid entries for specifying address space.


                                                    © National Instruments 2731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2732 ordinal=2732 -->
## Functions

Functions


            Value                                 Description

                                               VXI/VME A16 (1)

                                               VXI/VME A24 (2)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A32 (3)

                                               VXI/VME A64 (4)


                                                    PXI Memory Allocations (9)

             PXI                                     PXI Configuration (10)

                                                    PXI BAR0 (11) to PXI BAR5 (16)


               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       offset (0) —

             offset is the offset, in bytes, of the device to read from.

             offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
             offset specifies the offset.
                     • INSTR Specific—The offset specified in the VISA In 8, VISA In 16, VISA In 32, and VISA In 64
                operations for an INSTR Resource is the offset address relative to the device's allocated
                address base for the corresponding address space that was specified. For example, if
               address space specifies VXI/VME A16, offset specifies the offset from the logical address
               base address of the specified VXI device. If address space specifies VXI/VME A24, A32, or A64,
                  offset specifies the offset from the base address of the VXI device's memory space allocated
              by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —


2732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2733 ordinal=2733 -->
## Functions

Functions


    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      value —

    value contains the data read from address space.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

VISAVISA InIn 6464 FunctionFunction

Reads a 64-bit block of data from the specified address space and offset.


Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space without requiring VISA Map Address to be called. The
    following table lists the valid entries for specifying address space.

    Value                                 Description

                                        VXI/VME A16 (1)

                                        VXI/VME A24 (2)
     VXI, VME, and GPIB-VXI
                                        VXI/VME A32 (3)

                                        VXI/VME A64 (4)


    PXI                                     PXI Memory Allocations (9)


                                                    © National Instruments 2733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2734 ordinal=2734 -->
## Functions

Functions


            Value                                 Description

                                                    PXI Configuration (10)

                                                    PXI BAR0 (11) to PXI BAR5 (16)


               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       offset (0) —

             offset is the offset, in bytes, of the device to read from.

             offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
             offset specifies the offset.
                     • INSTR Specific—The offset specified in the VISA In 8, VISA In 16, VISA In 32, and VISA In 64
                operations for an INSTR Resource is the offset address relative to the device's allocated
                address base for the corresponding address space that was specified. For example, if
               address space specifies VXI/VME A16, offset specifies the offset from the logical address
               base address of the specified VXI device. If address space specifies VXI/VME A24, A32, or A64,
                  offset specifies the offset from the base address of the VXI device's memory space allocated
              by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.
               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      value —

            value contains the read data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2735 ordinal=2735 -->
## Functions

Functions

VISAVISA OutOut 88 FunctionFunction

Writes an 8-bit block of data to the specified address space and offset.


Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space to map. The following table lists the valid entries for
     specifying address space.

    Value                                 Description

                                        VXI/VME A16 (1)

                                        VXI/VME A24 (2)
     VXI, VME, and GPIB-VXI
                                        VXI/VME A32 (3)

                                        VXI/VME A64 (4)


                                            PXI Memory Allocations (9)

    PXI                                     PXI Configuration (10)

                                            PXI BAR0 (11) to PXI BAR5 (16)


   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —


                                                    © National Instruments 2735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2736 ordinal=2736 -->
## Functions

Functions


             offset is the offset, in bytes, of the device to read from.

             offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
             offset specifies the offset.
                     • INSTR Specific—The offset specified in the VISA Out 8, VISA Out 16, VISA Out 32, and VISA
              Out 64 operations for an INSTR Resource is the offset address relative to the device's
                 allocated address base for the corresponding address space that was specified. For
               example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
                address base address of the specified VXI device. If address space specifies VXI/VME A24,
                A32, or A64, offset specifies the offset from the base address of the VXI device's memory
               space allocated by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.
               •      value (0) —

            value contains the data to write to address space.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA OutOut 1616 FunctionFunction

       Writes a 16-bit block of data to the specified address space and offset.


2736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2737 ordinal=2737 -->
## Functions

Functions

Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space to map. The following table lists the valid entries for
     specifying address space.

    Value                                 Description

                                        VXI/VME A16 (1)

                                        VXI/VME A24 (2)
     VXI, VME, and GPIB-VXI
                                        VXI/VME A32 (3)

                                        VXI/VME A64 (4)


                                            PXI Memory Allocations (9)

    PXI                                     PXI Configuration (10)

                                            PXI BAR0 (11) to PXI BAR5 (16)


   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset is the offset, in bytes, of the device to read from.

     offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
     offset specifies the offset.
         • INSTR Specific—The offset specified in the VISA Out 8, VISA Out 16, VISA Out 32, and VISA
       Out 64 operations for an INSTR Resource is the offset address relative to the device's
         allocated address base for the corresponding address space that was specified. For
        example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
        address base address of the specified VXI device. If address space specifies VXI/VME A24,
        A32, or A64, offset specifies the offset from the base address of the VXI device's memory
        space allocated by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
         • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.


                                                    © National Instruments 2737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2738 ordinal=2738 -->
## Functions

Functions

               •      value (0) —

            value contains the data to write to address space.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA OutOut 3232 FunctionFunction

       Writes a 32-bit block of data to the specified address space and offset.


      Inputs/Outputs

               •      address space (A16: 1) —

           address space specifies the address space to map. The following table lists the valid entries for
             specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A24 (2)


2738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2739 ordinal=2739 -->
## Functions

Functions


  Value                                 Description

                                      VXI/VME A32 (3)

                                      VXI/VME A64 (4)


                                          PXI Memory Allocations (9)

  PXI                                     PXI Configuration (10)

                                          PXI BAR0 (11) to PXI BAR5 (16)


•      VISA resource name —

  VISA resource name specifies the resource to be opened. The VISA resource name control also
  specifies the session and class.

•       offset (0) —

  offset is the offset, in bytes, of the device to read from.

  offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
  offset specifies the offset.
      • INSTR Specific—The offset specified in the VISA Out 8, VISA Out 16, VISA Out 32, and VISA
      Out 64 operations for an INSTR Resource is the offset address relative to the device's
       allocated address base for the corresponding address space that was specified. For
      example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
      address base address of the specified VXI device. If address space specifies VXI/VME A24,
      A32, or A64, offset specifies the offset from the base address of the VXI device's memory
      space allocated by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
      • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.
•      value (0) —

  value contains the data to write to address space.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      VISA resource name out —


                                                   © National Instruments 2739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2740 ordinal=2740 -->
## Functions

Functions


           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA OutOut 6464 FunctionFunction

       Writes a 64-bit block of data to the specified address space and offset.


      Inputs/Outputs

               •      address space (A16: 1) —

           address space specifies the address space to map. The following table lists the valid entries for
             specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)

                                               VXI/VME A24 (2)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A32 (3)

                                               VXI/VME A64 (4)


                                                    PXI Memory Allocations (9)
             PXI
                                                    PXI Configuration (10)


2740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2741 ordinal=2741 -->
## Functions

Functions


  Value                                 Description

                                          PXI BAR0 (11) to PXI BAR5 (16)


•      VISA resource name —

  VISA resource name specifies the resource to be opened. The VISA resource name control also
  specifies the session and class.

•       offset (0) —

  offset is the offset, in bytes, of the device to read from.

  offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
  offset specifies the offset.
      • INSTR Specific—The offset specified in the VISA Out 8, VISA Out 16, VISA Out 32, and VISA
      Out 64 operations for an INSTR Resource is the offset address relative to the device's
       allocated address base for the corresponding address space that was specified. For
      example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
      address base address of the specified VXI device. If address space specifies VXI/VME A24,
      A32, or A64, offset specifies the offset from the base address of the VXI device's memory
      space allocated by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.
      • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.
•      value (0) —

  value contains the value to write.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      VISA resource name out —

  VISA resource name out is a copy of the VISA resource name that VISA functions return.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2742 ordinal=2742 -->
## Functions

Functions

   VISAVISA MoveMove InIn 88 FunctionFunction

      Moves one or more 8-bit units of data from device memory to local memory.

       This function uses the specified address space and offset to read in count 8-bit units of
       data.


      Inputs/Outputs

               •      address space (A16: 1) —

           address space specifies the address space to map. The following table lists the valid entries for
             specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)

                                               VXI/VME A24 (2)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A32 (3)

                                               VXI/VME A64 (4)


                                                    PXI Memory Allocations (9)

             PXI                                     PXI Configuration (10)

                                                    PXI BAR0 (11) to PXI BAR5 (16)


               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also


2742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2743 ordinal=2743 -->
## Functions

Functions


  specifies the session and class.

•       offset (0) —

  offset is the offset, in bytes, of the device to write to. offset accepts a 32- or 64-bit unsigned
  integer as input. The type of resource determines how offset specifies the offset.

      • INSTR Specific—The offset specified in the VISA Move In 8, VISA Move In 16, VISA Move In 32,
     and VISA Move In 64 operations for an INSTR Resource is the offset address relative to the
       device's allocated address base for the corresponding address space that was specified. For
      example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
      address base address of the VXI device specified. If address space specifies VXI/VME A24,
      A32, or A64, offset specifies the offset from the base address of the VXI device's memory
      space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.

     The count specified in the VISA Move In XX operations for an INSTR Resource is the number
       of data items (of the size corresponding to the operation) to move, beginning at the
       specified offset. Therefore, offset + count*size cannot exceed the amount of memory
      exported by the device in the given space.

      • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

     The count specified in the VISA Move In XX operations for a MEMACC Resource is the number
       of data items (of the size corresponding to the operation) to move, beginning at the
       specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
       available in the given space.

•      count —

  count is the number of data items to move.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      VISA resource name out —

  VISA resource name out is a copy of the VISA resource name that VISA functions return.

•      data —

  data is the array of 8 bit data being moved.


                                                   © National Instruments 2743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2744 ordinal=2744 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove InIn 1616 FunctionFunction

      Moves one or more 16-bit units of data from device memory to local memory.

       This function uses the specified address space and offset to read in count 16-bit units
       of data.


      Inputs/Outputs

               •      address space (A16: 1) —

           address space specifies the address space to map. The following table lists the valid entries for
             specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)

                                               VXI/VME A24 (2)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A32 (3)

                                               VXI/VME A64 (4)


                                                    PXI Memory Allocations (9)
             PXI
                                                    PXI Configuration (10)


2744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2745 ordinal=2745 -->
## Functions

Functions


  Value                                 Description

                                          PXI BAR0 (11) to PXI BAR5 (16)


•      VISA resource name —

  VISA resource name specifies the resource to be opened. The VISA resource name control also
  specifies the session and class.

•       offset (0) —

  offset is the offset, in bytes, of the device to write to. offset accepts a 32- or 64-bit unsigned
  integer as input. The type of resource determines how offset specifies the offset.

      • INSTR Specific—The offset specified in the VISA Move In 8, VISA Move In 16, VISA Move In 32,
     and VISA Move In 64 operations for an INSTR Resource is the offset address relative to the
       device's allocated address base for the corresponding address space that was specified. For
      example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
      address base address of the VXI device specified. If address space specifies VXI/VME A24,
      A32, or A64, offset specifies the offset from the base address of the VXI device's memory
      space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.

     The count specified in the VISA Move In XX operations for an INSTR Resource is the number
       of data items (of the size corresponding to the operation) to move, beginning at the
       specified offset. Therefore, offset + count*size cannot exceed the amount of memory
      exported by the device in the given space.

      • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

     The count specified in the VISA Move In XX operations for a MEMACC Resource is the number
       of data items (of the size corresponding to the operation) to move, beginning at the
       specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
       available in the given space.

•      count —

  count is the number of data items to move.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.


                                                   © National Instruments 2745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2746 ordinal=2746 -->
## Functions

Functions

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      data —

           data is the array of 16 bit data being moved.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove InIn 3232 FunctionFunction

      Moves one or more 32-bit units of data from device memory to local memory.

       This function uses the specified address space and offset to read in count 32-bit units
       of data.


      Inputs/Outputs

               •      address space (A16: 1) —

           address space specifies the address space to map. The following table lists the valid entries for
             specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A24 (2)


2746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2747 ordinal=2747 -->
## Functions

Functions


  Value                                 Description

                                      VXI/VME A32 (3)

                                      VXI/VME A64 (4)


                                          PXI Memory Allocations (9)

  PXI                                     PXI Configuration (10)

                                          PXI BAR0 (11) to PXI BAR5 (16)


•      VISA resource name —

  VISA resource name specifies the resource to be opened. The VISA resource name control also
  specifies the session and class.

•       offset (0) —

  offset is the offset, in bytes, of the device to write to.

  offset accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how
  offset specifies the offset.

      • INSTR Specific—The offset specified in the VISA Move In 8, VISA Move In 16, VISA Move In 32,
     and VISA Move In 64 operations for an INSTR Resource is the offset address relative to the
       device's allocated address base for the corresponding address space that was specified. For
      example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
      address base address of the VXI device specified. If address space specifies VXI/VME A24,
      A32, or A64, offset specifies the offset from the base address of the VXI device's memory
      space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.

     The count specified in the VISA Move In XX operations for an INSTR Resource is the number
       of data items (of the size corresponding to the operation) to move, beginning at the
       specified offset. Therefore, offset + count*size cannot exceed the amount of memory
      exported by the device in the given space.

      • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

     The count specified in the VISA Move In XX operations for a MEMACC Resource is the number
       of data items (of the size corresponding to the operation) to move, beginning at the


                                                   © National Instruments 2747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2748 ordinal=2748 -->
## Functions

Functions


                  specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
                  available in the given space.

               •      count —

           count is the number of data items to move.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      data —

           data is the array of 32 bit data being moved.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove InIn 6464 FunctionFunction

      Moves one or more 64-bit units of data from device memory to local memory.

       This function uses the specified address space and offset to read in count 64-bit units
       of data.


      Inputs/Outputs

               •      address space (A16: 1) —

2748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2749 ordinal=2749 -->
## Functions

Functions


  address space specifies the address space to map. The following table lists the valid entries for
  specifying address space.

  Value                                 Description

                                      VXI/VME A16 (1)

                                      VXI/VME A24 (2)
   VXI, VME, and GPIB-VXI
                                      VXI/VME A32 (3)

                                      VXI/VME A64 (4)


                                          PXI Memory Allocations (9)

  PXI                                     PXI Configuration (10)

                                          PXI BAR0 (11) to PXI BAR5 (16)


•      VISA resource name —

  VISA resource name specifies the resource to be opened. The VISA resource name control also
  specifies the session and class.

•       offset (0) —

  offset is the offset, in bytes, of the device to write to. offset accepts a 32- or 64-bit unsigned
  integer as input. The type of resource determines how offset specifies the offset.

      • INSTR Specific—The offset specified in the VISA Move In 8, VISA Move In 16, VISA Move In 32,
     and VISA Move In 64 operations for an INSTR Resource is the offset address relative to the
       device's allocated address base for the corresponding address space that was specified. For
      example, if address space specifies VXI/VME A16, offset specifies the offset from the logical
      address base address of the VXI device specified. If address space specifies VXI/VME A24,
      A32, or A64, offset specifies the offset from the base address of the VXI device's memory
      space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.

     The count specified in the VISA Move In XX operations for an INSTR Resource is the number
       of data items (of the size corresponding to the operation) to move, beginning at the
       specified offset. Therefore, offset + count*size cannot exceed the amount of memory
      exported by the device in the given space.


                                                   © National Instruments 2749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2750 ordinal=2750 -->
## Functions

Functions


                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

              The count specified in the VISA Move In XX operations for a MEMACC Resource is the number
                  of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
                  available in the given space.

               •      count —

           count is the number of data items to move.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      data —

           data is the array of 64-bit data being moved.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove OutOut 88 FunctionFunction

      Moves an array of 8-bit data from local memory to the specified address space and
        offset.


2750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2751 ordinal=2751 -->
## Functions

Functions

Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space to map. The following table lists the valid entries for
     specifying address space.

    Value                                 Description

                                        VXI/VME A16 (1)

                                        VXI/VME A24 (2)
     VXI, VME, and GPIB-VXI
                                        VXI/VME A32 (3)

                                        VXI/VME A64 (4)


                                            PXI Memory Allocations (9)

    PXI                                     PXI Configuration (10)

                                            PXI BAR0 (11) to PXI BAR5 (16)


   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset is the offset (in bytes) of the device to write to. offset accepts a 32- or 64-bit unsigned
     integer as input. The type of resource determines how offset specifies the offset.

         • INSTR Specific—The offset specified in the VISA Move Out 8, VISA Move Out 16, VISA Move
       Out 32, and VISA Move Out 64 operations for an INSTR Resource is the offset address relative
         to the device's allocated address base for the corresponding address space that was
         specified. For example, if address space specifies VXI/VME A16, offset specifies the offset
        from the logical address base address of the VXI device specified. If address space specifies
        VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's
      memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.

       The count specified in the VISA Move Out XX operations for an INSTR Resource is the


                                                    © National Instruments 2751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2752 ordinal=2752 -->
## Functions

Functions


             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the amount of memory
                exported by the device in the given space.

                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

              The count specified in the VISA Move Out XX operations for a MEMACC Resource is the
             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
                  available in the given space.

               •      data —

           data is the data you want to move.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove OutOut 1616 FunctionFunction

      Moves an array of 16-bit data from local memory to the specified address space and
        offset.


2752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2753 ordinal=2753 -->
## Functions

Functions

Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space to map.

    The following table lists the valid entries for specifying address space.

    Value                                 Description

                                        VXI/VME A16 (1)

                                        VXI/VME A24 (2)
     VXI, VME, and GPIB-VXI
                                        VXI/VME A32 (3)

                                        VXI/VME A64 (4)


                                            PXI Memory Allocations (9)

    PXI                                     PXI Configuration (10)

                                            PXI BAR0 (11) to PXI BAR5 (16)


   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset is the offset (in bytes) of the device to write to. offset accepts a 32- or 64-bit unsigned
     integer as input. The type of resource determines how offset specifies the offset.

         • INSTR Specific—The offset specified in the VISA Move Out 8, VISA Move Out 16, VISA Move
       Out 32, and VISA Move Out 64 operations for an INSTR Resource is the offset address relative
         to the device's allocated address base for the corresponding address space that was
         specified. For example, if address space specifies VXI/VME A16, offset specifies the offset
        from the logical address base address of the VXI device specified. If address space specifies
        VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's
      memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.


                                                    © National Instruments 2753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2754 ordinal=2754 -->
## Functions

Functions


              The count specified in the VISA Move Out XX operations for an INSTR Resource is the
             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the amount of memory
                exported by the device in the given space.

                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

              The count specified in the VISA Move Out XX operations for a MEMACC Resource is the
             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
                  available in the given space.

               •      data —

           data is the data you want to move.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove OutOut 3232 FunctionFunction

      Moves an array of 32-bit data from local memory to the specified address space and
        offset.


2754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2755 ordinal=2755 -->
## Functions

Functions

Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space to map. The following table lists the valid entries for
     specifying address space.

    Value                                 Description

                                        VXI/VME A16 (1)

                                        VXI/VME A24 (2)
     VXI, VME, and GPIB-VXI
                                        VXI/VME A32 (3)

                                        VXI/VME A64 (4)


                                            PXI Memory Allocations (9)

    PXI                                     PXI Configuration (10)

                                            PXI BAR0 (11) to PXI BAR5 (16)


   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset is the offset (in bytes) of the device to write to. offset accepts a 32- or 64-bit unsigned
     integer as input. The type of resource determines how offset specifies the offset.

         • INSTR Specific—The offset specified in the VISA Move Out 8, VISA Move Out 16, VISA Move
       Out 32, and VISA Move Out 64 operations for an INSTR Resource is the offset address relative
         to the device's allocated address base for the corresponding address space that was
         specified. For example, if address space specifies VXI/VME A16, offset specifies the offset
        from the logical address base address of the VXI device specified. If address space specifies
        VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's
      memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.

       The count specified in the VISA Move Out XX operations for an INSTR Resource is the


                                                    © National Instruments 2755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2756 ordinal=2756 -->
## Functions

Functions


             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the amount of memory
                exported by the device in the given space.

                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

              The count specified in the VISA Move Out XX operations for a MEMACC Resource is the
             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
                  available in the given space.

               •      data —

           data is the data you want to move.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove OutOut 6464 FunctionFunction

      Moves an array of 64-bit data from local memory to the specified address space and
        offset.


2756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2757 ordinal=2757 -->
## Functions

Functions

Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space to map. The following table lists the valid entries for
     specifying address space.

    Value                                 Description

                                        VXI/VME A16 (1)

                                        VXI/VME A24 (2)
     VXI, VME, and GPIB-VXI
                                        VXI/VME A32 (3)

                                        VXI/VME A64 (4)


                                            PXI Memory Allocations (9)

    PXI                                     PXI Configuration (10)

                                            PXI BAR0 (11) to PXI BAR5 (16)


   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset is the offset (in bytes) of the device to write to. offset accepts a 32- or 64-bit unsigned
     integer as input. The type of resource determines how offset specifies the offset.

         • INSTR Specific—The offset specified in the VISA Move Out 8, VISA Move Out 16, VISA Move
       Out 32, and VISA Move Out 64 operations for an INSTR Resource is the offset address relative
         to the device's allocated address base for the corresponding address space that was
         specified. For example, if address space specifies VXI/VME A16, offset specifies the offset
        from the logical address base address of the VXI device specified. If address space specifies
        VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's
      memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.

       The count specified in the VISA Move Out XX operations for an INSTR Resource is the


                                                    © National Instruments 2757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2758 ordinal=2758 -->
## Functions

Functions


             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the amount of memory
                exported by the device in the given space.

                     • MEMACC Specific—For a MEMACC Resource, offset specifies an absolute address.

              The count specified in the VISA Move Out XX operations for a MEMACC Resource is the
             number of data items (of the size corresponding to the operation) to move, beginning at the
                  specified offset. Therefore, offset + count*size cannot exceed the total amount of memory
                  available in the given space.

               •      data —

           data is the array of 64-bit data being moved.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA MemoryMemory AllocationAllocation FunctionFunction

       Allocates device memory of a specified size and returns the offset that specifies where
       the memory is located.


      Inputs/Outputs

               •      VISA resource name —

2758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2759 ordinal=2759 -->
## Functions

Functions


    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       size —

     size specifies the size of the allocation.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       offset —

     offset is a 32-bit offset which specifies the location of the allocated memory.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The memory can be allocated on either the device itself or on the computer's system
memory. If the device to which the given VISA Session refers is located on the local
interface card, the memory can be allocated either on the device itself or on the
computer's system memory. The memory region referenced by offset that is returned
from this function can be accessed with the high-level functions VISA Move In 8, VISA
Move In 16, VISA Move In 32, VISA Move In 64, VISA Move Out 8, VISA Move Out 16, VISA
Move Out 32, and VISA Move Out 64 or it can be mapped using the VISA Map Address
function.
VISAVISA MemoryMemory AllocationAllocation ExEx FunctionFunction

Allocates device memory of a specified size and returns the offset that specifies where
the memory is located.


                                                    © National Instruments 2759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2760 ordinal=2760 -->
## Functions

Functions


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       size —

             size specifies the size of the allocation.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       offset —

             offset is a 64-bit offset which specifies the location of the allocated memory.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The memory can be allocated on either the device itself or on the computer's system
      memory. If the device to which the given VISA Session refers is located on the local
        interface card, the memory can be allocated either on the device itself or on the
      computer's system memory. The memory region referenced by offset that is returned
      from this function can be accessed with the high-level functions VISA Move In 8, VISA
      Move In 16, VISA Move In 32, VISA Move In 64, VISA Move Out 8, VISA Move Out 16, VISA
      Move Out 32, and VISA Move Out 64 or it can be mapped using the VISA Map Address
       function.


2760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2761 ordinal=2761 -->
## Functions

Functions

      Note The offset of this function could be above the 4 GB boundary. If your
       device cannot access this memory, use the VISA Memory Allocation function
        instead.
VISAVISA MemoryMemory FreeFree FunctionFunction

Frees the memory previously allocated by the VISA Memory Allocation function or the
VISA Memory Allocation Ex function.

If the specified offset has been mapped using the VISA Map Address function, you
must unmap the offset using the VISA Unmap Address function before the memory can
be freed.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset —

     offset specifies the memory previously allocated by the VISA Memory Allocation function or the
    VISA Memory Allocation Ex function.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —


                                                    © National Instruments 2761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2762 ordinal=2762 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

   VISAVISA MoveMove FunctionFunction

      Moves length elements of the given source width from the specified source address
      space and offset to the specified destination address space and offset.


      Inputs/Outputs

               •      source width (16-bit: 2) —

            source width specifies the width of the source data.

             This input accepts the following values.

           1       8-bit
           2       16-bit (default)
           4       32-bit

               •      source space (A16: 1) —

            source space specifies the address space of the data to be moved.

             Refer to the table listed under address space in the VISA In 8 function for more information.

           1       VXI/VME A16
           2       VXI/VME A24
           3       VXI/VME A32


2762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2763 ordinal=2763 -->
## Functions

Functions


  4       VXI/VME A64

•      VISA resource name —

  VISA resource name specifies the resource to be opened. The VISA resource name control also
  specifies the session and class.

•      source offset (0) —

  source offset is the offset (in bytes) of the device to read from.

   It is the offset address relative to the device's allocated address base for the corresponding
  specified address space. For example, if source space specifies VXI/VME A16, source offset
  specifies the offset from the logical address base address of the VXI device specified. If source
  space specifies VXI/VME A24, A32, or A64, source offset specifies the offset from the base address
  of the VXI device's memory space allocated by the VXI Resource Manager within VXI A24 or A32.

•      length —

  length specifies the number of elements to move.

•      dest offset (0) —

  dest offset is the offset, in bytes, of the destination device.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      dest space (A16: 1) —

  dest space specifies the address space of the destination.

  Refer to the table listed under source space for more information.

•      dest width (same as source) —

  dest width specifies the width of the destination data.

   If dest width is not wired, it will be the same as the source width. This input accepts the
  following values.


                                                   © National Instruments 2763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2764 ordinal=2764 -->
## Functions

Functions


           1       8-bit
           2       16-bit (default)
           4       32-bit

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           Note This function does not accept all classes of VISA sessions. Valid VISA
               session classes include GPIB-VXI INSTR, GPIB-VXI MEMACC, VXI INSTR, and VXI
            MEMACC.
   LowLow LevelLevel RegisterRegister AccessAccess

      Use the Low Level Register Access functions to program in an address space with more
        detail than is provided at a high level.

      The functions on this palette can return VISA error codes.


         Palette Object       Description

        VISA Map Address
                       Maps a memory space specified by map base and map size.
         Function

        VISA Unmap       Unmaps the memory space previously mapped by the VISA Map Address
        Address Function    function.

        VISA Peek 8
                          Reads an 8-bit value from the address location specified in offset.
         Function

        VISA Peek 16       Reads a 16-bit value from the address location specified by offset.


2764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2765 ordinal=2765 -->
## Functions

Functions


 Palette Object       Description

 Function

 VISA Peek 32                   Reads a 32-bit value from the address location specified in offset. Function

 VISA Peek 64                   Reads a 64-bit value from the address location specified in offset.
 Function

 VISA Poke 8          Writes an 8-bit value to the specified address and stores the content of the
 Function            value to the address pointed to by offset.

 VISA Poke 16        Writes a 16-bit value to the specified address and stores the content of the
 Function            value to the address pointed to by offset.

 VISA Poke 32        Writes a 32-bit value to the specified address and stores the content of the
 Function            value to the address pointed to by offset.

 VISA Poke 64        Writes a 64-bit value to the specified address and stores the content of the
 Function            value to the address pointed to by offset.

VISAVISA MapMap AddressAddress FunctionFunction

Maps a memory space specified by map base and map size.

The memory space that the function maps depends on the type of interface specified
by VISA resource name and address space. After the window is mapped, VISA keeps
track of the window that is mapped. This dictates that VISA can map only one window
for each VISA session.


Inputs/Outputs

   •      address space (A16: 1) —

    address space specifies the address space to map. The following table lists the valid entries for


                                                    © National Instruments 2765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2766 ordinal=2766 -->
## Functions

Functions


             specifying address space.

            Value                                 Description

                                               VXI/VME A16 (1)

                                               VXI/VME A24 (2)
              VXI, VME, and GPIB-VXI
                                               VXI/VME A32 (3)

                                               VXI/VME A64 (4)


                                                    PXI Memory Allocations (9)

             PXI                                     PXI Configuration (10)

                                                    PXI BAR0 (11) to PXI BAR5 (16)


               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •    map base (0) —

         map base contains the offset (in bytes) of the memory to be mapped.

          The type of resource determines how map base specifies the offset.
                     • INSTR Specific—Notice that map base specified in the VISA Map Address operation for an
               INSTR Resource is the offset address relative to the device's allocated address base for the
                corresponding address space that was specified. For example, if address space specifies
               VXI/VME A16, map base specifies the offset from the logical address base address of the
                  specified VXI device. If address space specifies VXI/VME A24, VXI/VME A32, or VXI/VME A64,
           map base specifies the offset from the base address of the VXI device's memory space
                 allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64 space.
                     • MEMACC Specific—For a MEMACC Resource, map base specifies an absolute address.
               •    map size (0) —

         map size contains the amount of memory to map.

               •       error in (no error) —


2766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2767 ordinal=2767 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      access (False) —

    access is reserved for future use and should be set to FALSE.

    This input is available only if you do not place a checkmark in the Restrict Access checkbox on
    the Configuration page of the Properties dialog box for the variable refnum.
   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

VISAVISA UnmapUnmap AddressAddress FunctionFunction

Unmaps the memory space previously mapped by the VISA Map Address function.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.


                                                    © National Instruments 2767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2768 ordinal=2768 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   VISAVISA PeekPeek 88 FunctionFunction

      Reads an 8-bit value from the address location specified in offset.

      You must use the VISA Map Address function to map the address before you call this
       function. The address must be a valid memory address in the current process.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       offset (0) —

             offset contains the offset, in bytes, from the register location originally mapped in the mapped
         memory space.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      value —

            value contains the read data.

               •       error out —

2768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2769 ordinal=2769 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
function, NI I/O Trace might not log this function.
VISAVISA PeekPeek 1616 FunctionFunction

Reads a 16-bit value from the address location specified by offset.

You must use the VISA Map Address function to map the address before you call this
function. The address must be a valid memory address in the current process.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset contains the offset, in bytes, from the register location originally mapped in the mapped
   memory space.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.


                                                    © National Instruments 2769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2770 ordinal=2770 -->
## Functions

Functions

               •      value —

            value contains the read data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
      appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
       visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
       function, NI I/O Trace might not log this function.
   VISAVISA PeekPeek 3232 FunctionFunction

      Reads a 32-bit value from the address location specified in offset.

      You must use the VISA Map Address function to map the address before you call this
       function. The address must be a valid memory address in the current process.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       offset (0) —

             offset contains the offset, in bytes, from the register location originally mapped in the mapped
         memory space.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


2770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2771 ordinal=2771 -->
## Functions

Functions


    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •      value —

    value contains the read data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
function, NI I/O Trace might not log this function.
VISAVISA PeekPeek 6464 FunctionFunction

Reads a 64-bit value from the address location specified in offset.

You must use the VISA Map Address function to map the address before you call this
function. The address must be a valid memory address in the current process.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —


                                                    © National Instruments 2771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2772 ordinal=2772 -->
## Functions

Functions


             offset contains the offset, in bytes, from the register location originally mapped in the mapped
         memory space.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •      value —

            value contains the read data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
      appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
       visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
       function, NI I/O Trace might not log this function.
   VISAVISA PokePoke 88 FunctionFunction

       Writes an 8-bit value to the specified address and stores the content of the value to the
       address pointed to by offset.

      You must use the VISA Map Address function to map the address before you call this
       function. The address must be a valid memory address in the current process.


2772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2773 ordinal=2773 -->
## Functions

Functions

Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset contains the offset, in bytes, from the register location originally mapped in the mapped
   memory space.

   •      value (0) —

    value contains the value to write.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
function, NI I/O Trace might not log this function.
VISAVISA PokePoke 1616 FunctionFunction

Writes a 16-bit value to the specified address and stores the content of the value to the
address pointed to by offset.

You must use the VISA Map Address function to map the address before you call this
function. The address must be a valid memory address in the current process.

                                                    © National Instruments 2773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2774 ordinal=2774 -->
## Functions

Functions


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       offset (0) —

             offset contains the offset, in bytes, from the register location originally mapped in the mapped
         memory space.

               •      value (0) —

            value contains the value to write.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
      appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
       visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
       function, NI I/O Trace might not log this function.


2774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2775 ordinal=2775 -->
## Functions

Functions

VISAVISA PokePoke 3232 FunctionFunction

Writes a 32-bit value to the specified address and stores the content of the value to the
address pointed to by offset.

You must use the VISA Map Address function to map the address before you call this
function. The address must be a valid memory address in the current process.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       offset (0) —

     offset contains the offset, in bytes, from the register location originally mapped in the mapped
   memory space.

   •      value (0) —

    value contains the value to write.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 2775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2776 ordinal=2776 -->
## Functions

Functions

           If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
      appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
       visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
       function, NI I/O Trace might not log this function.
   VISAVISA PokePoke 6464 FunctionFunction

       Writes a 64-bit value to the specified address and stores the content of the value to the
       address pointed to by offset.

      You must use the VISA Map Address function to map the address before you call this
       function. The address must be a valid memory address in the current process.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       offset (0) —

             offset contains the offset, in bytes, from the register location originally mapped in the mapped
         memory space.

               •      value (0) —

            value contains the value to write.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —


2776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2777 ordinal=2777 -->
## Functions

Functions


    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If you use NI I/O Trace to debug this function, enable the Force peek/poke calls to
appear in NI I/O Trace option in Measurement & Automation Explorer (Windows),
visaconf (Linux), or NI-VISA Configuration (Mac OS X). If you do not enable this
function, NI I/O Trace might not log this function.

VISAVISA ClearClear FunctionFunction

Clears the input and output buffers of the device.


Inputs/Outputs

   •      VISA resource name —

    VISA resource name specifies the resource to be opened. The VISA resource name control also
     specifies the session and class.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      VISA resource name out —

    VISA resource name out is a copy of the VISA resource name that VISA functions return.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 2777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2778 ordinal=2778 -->
## Functions

Functions

      Clear for 488.2 Instruments (GPIB, VXI, TCP/IP, USB)

            • GPIB—VISA sends the Selected Device Clear command.
            • VXI—VISA sends the Word Serial Clear command.
            • USB—VISA sends the INITIATE_CLEAR and CHECK_CLEAR_STATUS commands on
          the control pipe.

      Clear for Non-488.2 Instruments (Serial Instr, TCP/IP Socket, USB Raw)

            • Serial Instr—VISA flushes (discards) the I/O output buffer, sends a break, and then
           flushes the I/O input buffer.
            • TCP/IP Socket—VISA flushes the I/O buffers.
            • USB Raw—VISA resets the endpoints referred to by the USB Settings:Bulk-In Pipe
         and USB Settings:Out Pipe properties.

     VISAVISA ReadRead STBSTB FunctionFunction

      Reads a service request status byte byte from the message-based device specified by
      VISA resource name.


      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.


2778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2779 ordinal=2779 -->
## Functions

Functions

   •       status byte —

    status byte contains the status byte read from the instrument.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Status Bytes for 488.2 Instruments (GPIB, VXI, TCP/IP, USB)

This function reads a service request from a message-based device. The following
details are bus-specific:

  • GPIB—This function reads the status by serial polling the device.
  • VXI—This function sends the Word Serial Read STB query to the device.
  • USB—This function sends the device the Read Status Byte command on the control
    pipe.

Status Bytes for Non-488.2 Instruments (Serial Instr, TCP/IP Socket, USB
Raw)

This function retrieves status information by sending a message in response to a
service request. For a session to a Serial Instr or Ethernet Socket, if the property IO
Protocol is Serial-TCPIP/488 (4), the device is sent the string "*STB?\n" and then the
device status byte is read; otherwise, this operation is not valid.

VISAVISA AssertAssert TriggerTrigger FunctionFunction

Asserts a software or hardware trigger, depending on the interface type. For software
triggers, Default (0) is the only valid protocol. For VXI hardware triggers, Default (0) is
equivalent to Sync (5). For PXI triggers, PXI: Reserve (6) and PXI: Unreserve (7) are the
only valid protocols.


                                                    © National Instruments 2779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2780 ordinal=2780 -->
## Functions

Functions

      Inputs/Outputs

               •      VISA resource name —

           VISA resource name specifies the resource to be opened. The VISA resource name control also
              specifies the session and class.

               •      protocol (default: 0) —

            protocol is the trigger protocol to use during assertion.

             This input accepts the following values.

           0      Default
           1     On
           2       Off
           5      Sync
           6       PXI: Reserve
           7       PXI: Unreserve

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      VISA resource name out —

           VISA resource name out is a copy of the VISA resource name that VISA functions return.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Software Triggers for 488.2 Instruments (GPIB, VXI, TCP/IP, USB)

       This function sends an IEEE-488.2 software trigger to the addressed device, with the
       following bus-specific details:

            • GPIB—VISA addresses the device to listen and sends the GPIB Group Execute
           Trigger (GET) message.
            • VXI—VISA sends the Word Serial Trigger command.

2780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2781 ordinal=2781 -->
## Functions

Functions

  • USB—VISA sends the trigger message ID on the bulk-out pipe.

Software Triggers for Non-488.2 Instruments (Serial Instr, TCP/IP Socket,
USB Raw)

If the property IO Protocol is set to Serial-TCPIP-USB/488 Strings (4), this function
sends the string "*TRG\n" to the device. Otherwise, this operation is not valid.

Hardware Triggers for VXI

For hardware triggers to VXI instruments, you must first set the property Trigger
Identifier to the desired trigger line. This function performs the specified trigger
operation on the line identified by the Trigger Identifier property.

Trigger Reservation for PXI

For PXI instruments, this function reserves or unreserves (releases) a trigger line for
use in external triggering.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\VISA\PXI\PXI - Reserve
   Trigger.vi

GPIBGPIB

Use the GPIB functions to communicate with GPIB (IEEE-488) devices.

The functions on this palette can return specific GPIB error codes.


                                                    © National Instruments 2781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2782 ordinal=2782 -->
## Functions

Functions


         Palette                      Description
        Object

        GPIB Read                   Reads byte count number of bytes from the GPIB device at address string.         Function

        GPIB Write                      Writes data to the GPIB device identified by address string.
         Function

        Wait for
        GPIB RQS    Waits for the device indicated by address string to assert RQS.
         Function

        GPIB Trigger                   Sends GET (Group Execute Trigger) to the device indicated by address string.         Function

        GPIB Clear                   Sends either SDC (Selected Device Clear) or DCL (Device Clear).
         Function

        GPIB Serial
          Poll         Performs a serial poll of the device indicated by address string.
         Function

        GPIB
           Initialization  Configures the GPIB interface at address string.
         Function

                  Shows the present status of the GPIB Controller indicated by address string. Error I/O
        GPIB Status                      operates uniquely in this function. The function gets the status of the GPIB Controller         Function                       regardless of whether an error occurred in a preceding operation.

        GPIB Wait    Waits for the state(s) indicated by wait state vector at the device indicated by
         Function     address string.

        GPIB Misc    Performs the GPIB operation indicated by command string. Use this low-level
         Function     function when the other high-level, traditional GPIB functions are not suitable.

                   Use the GPIB 488.2 functions to exchange data and instructions between VIs and
        GPIB 488.2
                   GPIB 488.2 devices.


      Compatible GPIB Hardware

         All NI-488.2 hardware drivers are compatible with LabVIEW. Refer to the GPIB Driver
       Versions on the National Instruments Web site for information about current driver
       versions for each GPIB controller.

2782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2783 ordinal=2783 -->
## Functions

Functions

GPIBGPIB ReadRead FunctionFunction

Reads byte count number of bytes from the GPIB device at address string.

Right-click the node and select Synchronous I/O Mode»Synchronous from the
shortcut menu to read data synchronously.


Inputs/Outputs

   •      timeout ms (488.2 global) —

    timeout ms specifies the time, in milliseconds, that the function waits before timing out.

    The operation aborts if it does not complete within timeout ms. To disable timeouts, set
    timeout ms to 0.

    To use the 488.2 global timeout, leave timeout ms unwired or set the input to –1. Then use the
    SetTimeOut function to change the default value of timeout ms. The default is 10000.

   •      address string —

    address string contains the address of the GPIB device with which the function communicates.

    You can input both the primary and secondary addresses in address string by using the form
   primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
    and secondaryis 3, address string is 2+3.

       If you do not specify an address, the functions do not perform addressing before they attempt to
    read and write the string. They assume you have either sent these commands another way or
    that another controller is in charge and therefore responsible for the addressing. If the controller
      is supposed to address the device but does not do so before the time limit expires, the functions
    terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
    Charge, do not specify address string.

   When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
    form ID:address (or ID: if no address is necessary) determines the controller that a specific


                                                    © National Instruments 2783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2784 ordinal=2784 -->
## Functions

Functions


             function uses. For example, to set GPIB controller 2 to talk to a device on address 3, use the
              prefix 2:3. If a controller ID is not present, the function defaults to controller (or bus) number 0.

               •      byte count —

            byte count specifies the number of bytes the function reads from the GPIB device.

               •     mode (0) —

         mode specifies conditions, other than reaching byte count, for terminating the read.

          The following table includes valid values and the corresponding EOS characters. Any mode not
              listed in the table indicates the decimal number of the EOS character that you want. Refer to
           >GPIB Multiline Interface Messages for more information about managing GPIB tasks.

          No EOS character. The EOS termination mode is disabled. Read terminated on EOI or byte           0
             count.
           1 EOS character is CR. Read terminated on EOI, byte count, or CR.
           2 EOS character is LF. Read terminated on EOI, byte count, or LF.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data is the data the function read.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active


2784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2785 ordinal=2785 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


When you transfer data from or to a hardware driver synchronously, the calling thread
is locked for the duration of the data transfer. Depending on the speed of the transfer,
this can hinder other processes that require the calling thread. However, if an
application requires that the data transfer as quickly as possible, performing the
operation synchronously dedicates the calling thread exclusively to this operation.

      Note In most applications, synchronous calls are slightly faster when you
        are communicating with 4 or fewer instruments. Asynchronous operations
        result in a significantly faster application when you are communicating with 5
        or more instruments. The LabVIEW default is asynchronous I/O.

The GPIB Read function terminates when it accomplishes one of the following tasks:

  • Reads the number of bytes requested.
  • Detects an error.
  • Exceeds the time limit.
  • Detects the END message (EOI asserted).
  • Detects the EOS character (if this option is enabled by the value supplied to mode).

      Note The function compares all eight bits when it checks for the EOS

                                                    © National Instruments 2785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2786 ordinal=2786 -->
## Functions

Functions


                character.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\GPIB\Simple GPIB.vi

     GPIBGPIB WriteWrite FunctionFunction

       Writes data to the GPIB device identified by address string.

        Right-click the node and select Synchronous I/O Mode»Synchronous from the
       shortcut menu to write data synchronously.


      Inputs/Outputs

               •      timeout ms (488.2 global) —

           timeout ms specifies the time, in milliseconds, that the function waits before timing out.

          The operation aborts if it does not complete within timeout ms. To disable timeouts, set
           timeout ms to 0.

           To use the 488.2 global timeout, leave timeout ms unwired or set the input to –1. Then use the
           SetTimeOut function to change the default value of timeout ms. The default is 10000.

               •      address string —

           address string contains the address of the GPIB device with which the function communicates.

           You can input both the primary and secondary addresses in address string by using the form
          primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
          and secondaryis 3, address string is 2+3.


2786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2787 ordinal=2787 -->
## Functions

Functions


   If you do not specify an address, the functions do not perform addressing before they attempt to
  read and write the string. They assume you have either sent these commands another way or
  that another controller is in charge and therefore responsible for the addressing. If the controller
   is supposed to address the device but does not do so before the time limit expires, the functions
  terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
  Charge, do not specify address string.

  When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
  form ID:address (or ID: if no address is necessary) determines the controller that a specific
  function uses. For example, to set GPIB controller 2 to talk to a device on address 3, use the
  prefix 2:3. If a controller ID is not present, the function defaults to controller (or bus) number 0.

•      data —

  data is the data the function writes to the GPIB device.

•     mode (0) —

  mode indicates how to terminate the GPIB Write.

  This input accepts the following values.

  0 Send EOI with the last character of the string.
  1 Append CR to the string and send EOI with CR.
  2 Append LF to the string and send EOI with LF.
  3 Append CR LF to the string and send EOI with LF.
  4 Append CR to the string but do not send EOI.
  5 Append LF to the string but do not send EOI.
  6 Append CR LF to the string but do not send EOI.
  7 Do not send EOI.

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       status —

  status is a Boolean array in which each bit describes a state of the GPIB Controller.

   If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

  The following table shows the numeric value and symbolic status of each bit in status. This table

                                                   © National Instruments 2787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2788 ordinal=2788 -->
## Functions

Functions

             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When you transfer data from or to a hardware driver synchronously, the calling thread
         is locked for the duration of the data transfer. Depending on the speed of the transfer,
        this can hinder other processes that require the calling thread. However, if an
       application requires that the data transfer as quickly as possible, performing the
       operation synchronously dedicates the calling thread exclusively to this operation.

           Note In most applications, synchronous calls are slightly faster when you
              are communicating with 4 or fewer instruments. Asynchronous operations
                result in a significantly faster application when you are communicating with 5
              or more instruments. The LabVIEW default is asynchronous I/O.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Instrument IO\GPIB\Simple GPIB.vi


2788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2789 ordinal=2789 -->
## Functions

Functions

WaitWait forfor GPIBGPIB RQSRQS FunctionFunction

Waits for the device indicated by address string to assert RQS.

Use the GPIB Wait function to wait for a specified device to assert any state.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      address string —

    address string contains the address of the GPIB device with which the function communicates.

    You can input both the primary and secondary addresses in address string by using the form
   primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
    and secondaryis 3, address string is 2+3.

       If you do not specify an address, the functions do not perform addressing before they attempt to
    read and write the string. They assume you have either sent these commands another way or
    that another controller is in charge and therefore responsible for the addressing. If the controller
      is supposed to address the device but does not do so before the time limit expires, the functions
    terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
    Charge, do not specify address string.

   When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
    form ID:address (or ID: if no address is necessary) determines the controller that a specific
    function uses. For example, to set GPIB controller 2 to talk to a device on address 3, use the
     prefix 2:3. If a controller ID is not present, the function defaults to controller (or bus) number 0.

   •      timeout ms (488.2 global) —

    timeout ms specifies the time, in milliseconds, that the function waits before timing out.

    The operation aborts if it does not complete within timeout ms. To disable timeouts, set
    timeout ms to 0.


                                                    © National Instruments 2789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2790 ordinal=2790 -->
## Functions

Functions


           To use the 488.2 global timeout, leave timeout ms unwired or set the input to –1. Then use the
           SetTimeOut function to change the default value of timeout ms. The default is 10000.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       poll response byte —

             poll response byte returns the serial poll response from the specified device. If SRQI is set, the
             function polls the device at the specified address to see if the device requested service.

         When the specified device requests service (the RQS bit—bit 6 in the device's Status Byte
             Register—is TRUE), the function returns the serial poll response.

                    If the device indicated by address string does not respond within the timeout limit, poll
           response byte is –1.

               Note The bit definitions for the poll response byte vary among instruments.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     GPIBGPIB TriggerTrigger FunctionFunction

      Sends GET (Group Execute Trigger) to the device indicated by address string.


      Inputs/Outputs

               •      address string —

           address string contains the address of the GPIB device with which the function communicates.

           You can input both the primary and secondary addresses in address string by using the form


2790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2791 ordinal=2791 -->
## Functions

Functions


  primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
  and secondaryis 3, address string is 2+3.

   If you do not specify an address, the functions do not perform addressing before they attempt to
  read and write the string. They assume you have either sent these commands another way or
  that another controller is in charge and therefore responsible for the addressing. If the controller
   is supposed to address the device but does not do so before the time limit expires, the functions
  terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
  Charge, do not specify address string.

  When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
  form ID:address (or ID: if no address is necessary) determines the controller that a specific
  function uses. For example, to set GPIB controller 2 to talk to a device on address 3, use the
  prefix 2:3. If a controller ID is not present, the function defaults to controller (or bus) number 0.

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       status —

  status is a Boolean array in which each bit describes a state of the GPIB Controller.

   If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

  The following table shows the numeric value and symbolic status of each bit in status. This table
  also includes a description of each bit.

  Status Bit    Numeric Value      Symbolic Status       Description
  0           1               DCAS                 Device Clear state
  1           2                DTAS                  Device Trigger State
  2           4                 LACS                   Listener Active
  3           8                 TACS                   Talker Active
  4           16               ATN                    Attention Asserted
  5           32                  CIC                     Controller-In-Charge
  6           64              REM                Remote State
  7           128              LOK                  Lockout State
  8           256             CMPL                 Operation Completed
  12          4096              SRQI              SRQ Detected while CIC
  13          8192            END                 EOI or EOS Detected


                                                   © National Instruments 2791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2792 ordinal=2792 -->
## Functions

Functions


            Status Bit    Numeric Value      Symbolic Status       Description
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     GPIBGPIB ClearClear FunctionFunction

      Sends either SDC (Selected Device Clear) or DCL (Device Clear).


      Inputs/Outputs

               •      address string —

           address string contains the address of the GPIB device with which the function communicates.

           You can input both the primary and secondary addresses in address string by using the form
          primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
          and secondaryis 3, address string is 2+3.

                    If you do not specify an address, the functions do not perform addressing before they attempt to
            read and write the string. They assume you have either sent these commands another way or
             that another controller is in charge and therefore responsible for the addressing. If the controller
                is supposed to address the device but does not do so before the time limit expires, the functions
            terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
            Charge, do not specify address string.

         When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
           form ID:address (or ID: if no address is necessary) determines the controller that a specific
             function uses. For example, to set GPIB controller 2 to talk to a device on address 3, use the
              prefix 2:3. If a controller ID is not present, the function defaults to controller (or bus) number 0.

               •       error in —


2792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2793 ordinal=2793 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table
    also includes a description of each bit.

    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GPIBGPIB SerialSerial PollPoll FunctionFunction

Performs a serial poll of the device indicated by address string.


                                                    © National Instruments 2793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2794 ordinal=2794 -->
## Functions

Functions

      Inputs/Outputs

               •      address string —

           address string is the address of the device the function polls.

           address string contains the address of the GPIB device with which the function communicates.
           You can input both the primary and secondary addresses in address string by using the form
          primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
          and secondaryis 3, address string is 2+3.

                    If you do not specify an address, the functions do not perform addressing before they attempt to
            read and write the string. They assume you have either sent these commands another way or
             that another controller is in charge and therefore responsible for the addressing. If the controller
                is supposed to address the device but does not do so before the time limit expires, the functions
            terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
            Charge, do not specify address string.

         When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
           form ID:address (or ID: if no address is necessary) determines the controller that a specific
             function uses. If a controller ID is not present, the function defaults to controller (or bus) number
               0.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       serial poll byte —

              serial poll byte is the response from the device.

                    If the addressed device does not respond within the timeout limit, serial poll byte is -1.
               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2795 ordinal=2795 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GPIBGPIB InitializationInitialization FunctionFunction

Configures the GPIB interface at address string.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      require re-addressing (T) —

       If require re-addressing is TRUE, the function addresses the device before every read or write.


                                                    © National Instruments 2795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2796 ordinal=2796 -->
## Functions

Functions

                    If FALSE, the device must be able to retain addressing from one read or write to the next.
               •       assert REN with IFC (T) —

                    If assert REN with IFC is TRUE, and if this Controller (specified by the ID in address string) is the
           System Controller, the function asserts the Remote Enable line.

               •      system controller (T) —

                    If system controller is TRUE, this Controller acts as the System Controller.

               •      address string —

           address string sets the GPIB address of the GPIB controller itself.

          The default value for address string is the configured address for the primary GPIB controller on
            your system. The configured address is usually 0. You usually do not need to wire this input.

         When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
           form ID:address(or ID: if no address is necessary) determines which controller the function
             uses. If a controller ID is not present, the function defaults to controller (or bus) number 0.

               •      IST bit sense (T) —

                    If IST bit sense is TRUE, the Individual Status bit of the device responds TRUE to a parallel poll; if
            IST bit sense is FALSE, the Individual Status bit of the device responds FALSE to a parallel poll.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      disallow DMA (F) —

                    If disallow DMA is TRUE, this device uses programmed I/O for data transfers.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     GPIBGPIB StatusStatus FunctionFunction

      Shows the present status of the GPIB Controller indicated by address string. Error I/O
       operates uniquely in this function. The function gets the status of the GPIB Controller

2796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2797 ordinal=2797 -->
## Functions

Functions

regardless of whether an error occurred in a preceding operation.


Inputs/Outputs

   •      address string —

    address string contains the address of the GPIB device with which the function communicates.

    You can input both the primary and secondary addresses in address string by using the form
   primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
    and secondaryis 3, address string is 2+3.

       If you do not specify an address, the functions do not perform addressing before they attempt to
    read and write the string. They assume you have either sent these commands another way or
    that another controller is in charge and therefore responsible for the addressing. If the controller
      is supposed to address the device but does not do so before the time limit expires, the functions
    terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
    Charge, do not specify address string.

   When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
    form ID:address (or ID: if no address is necessary) determines the controller that a specific
    function uses. For example, to set GPIB controller 2 to talk to a device on address 3, use the
     prefix 2:3. If a controller ID is not present, the function defaults to controller (or bus) number 0.

   •       error in —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table


                                                    © National Instruments 2797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2798 ordinal=2798 -->
## Functions

Functions


             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •     GPIB error —

          GPIB error contains the most recent error code reported by any of the GPIB functions. Refer to
           GPIB Error Codes for possible values for GPIB error if bit 15 of status is set.

               •      byte count —

            byte count is the number of bytes the previous GPIB operation sent.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     GPIBGPIB WaitWait FunctionFunction

       Waits for the state(s) indicated by wait state vector at the device indicated by address
        string.

      Use the Wait for GPIB RQS function to wait for a device to assert RQS.


2798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2799 ordinal=2799 -->
## Functions

Functions


Inputs/Outputs

   •      timeout ms (488.2 global) —

    timeout ms specifies the time, in milliseconds, that the function waits before timing out.

    The operation aborts if it does not complete within timeout ms. To enable timeouts, set bit 14 in
    the wait state vector input. To disable timeouts, set timeout ms to 0.

    To use the 488.2 global timeout, leave this input unwired. Then use the SetTimeOut function to
    change the default value of timeout ms. The default is 10000.

   •      address string —

    address string contains the address of the GPIB device with which the function communicates.

    You can input both the primary and secondary addresses in address string by using the form
   primary+secondary. Both primaryand secondaryare decimal values, so if primaryis 2
    and secondaryis 3, address string is 2+3.

       If you do not specify an address, the functions do not perform addressing before they attempt to
    read and write the string. They assume you have either sent these commands another way or
    that another controller is in charge and therefore responsible for the addressing. If the controller
      is supposed to address the device but does not do so before the time limit expires, the functions
    terminate with GPIB error 6 (timeout) and set bit 14 in status. If the GPIB is not the Controller-In-
    Charge, do not specify address string.

   When there are multiple GPIB controllers that LabVIEW can use, a prefix to address string in the
    form ID:address (or ID: if no address is necessary) determines the controller that a specific
    function uses. For example, to set GPIB controller 2 to talk to a device on address 3, use the
     prefix 2:3. If a controller ID is not present, the function defaults to controller (or bus) number 0.

   •      wait state vector —

    wait state vector indicates the states for which the function waits.

    Each Boolean element in the array corresponds to a state that the device can wait on. If more
    than one element is set to TRUE, the function terminates when any one of the states exists.


                                                    © National Instruments 2799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2800 ordinal=2800 -->
## Functions

Functions


          The following table defines the states that you can specify in wait state vector. This table also
                 lists the numeric value and description of each element. While these elements are the same as
            those that other GPIB functions return, only the states listed are valid for this function.

           Wait State Vector Bit    Numeric Value   Symbolic Status    Description
           0                     1             DCAS              Device Clear state
           1                     2              DTAS              Device Trigger State
           2                     4              LACS                Listener Active
           3                     8              TACS                Talker Active
           4                     16            ATN                Attention Asserted
           5                     32               CIC                 Controller-In-Charge
           6                     64           REM             Remote State
           7                     128           LOK               Lockout State
           12                    4096            SRQI           SRQ Detected while CIC
           13                    8192          END              EOI or EOS Detected
           14                    16384          TIMO             Timeout

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the GPIB function sets bit 15. GPIB error is valid only if bit 15 of status is set.
             Refer to the GPIB Status function for more information about status bits and GPIB error codes.

                    If you are waiting for multiple states, check status to see which state caused the function to
             terminate.

             This function can run in parallel with other functions because LabVIEW alternately checks for
             status and executes other functions. In addition, multiple calls to this function can execute in
               parallel, so you can wait for different states on different Controllers at the same time or for
            multiple states to exist.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2801 ordinal=2801 -->
## Functions

Functions

GPIBGPIB MiscMisc FunctionFunction

Performs the GPIB operation indicated by command string. Use this low-level function
when the other high-level, traditional GPIB functions are not suitable.


Inputs/Outputs

   •     command string —

   command string is the GPIB operation to perform.

    The following table shows the functions you can specify in command string.

          Note address is the address in the command string.

    Functions          Type      Description
   cac 0/1             Controller Become active controller.
   cmd string         Controller Send IEEE 488 commands.
   dma 0/1             Controller  Set DMA mode or programmed I/O mode.
   gts 0/1             Controller Go from active controller to standby.
   ist 0/1             Controller  Set individual status bit.
   llo                   Controller  Local lockout.
   loc                   Controller  Place controller in local state.
   loc address          Device    Go to local.
   off                   Controller  Take controller offline.
   off address          Device     Take device offline.
   pct address          Device     Pass control.
   ppc byte            Controller  Parallel poll configure (enable or disable).
   ppc byte address   Device      Parallel poll configure (enable or disable).
   ppu                   Controller  Parallel poll unconfigure all devices.
   rpp                   Controller Conduct parallel poll.
   rsc 0/1             Controller  Request or release system control.
   rsv byte            Controller  Request service and/or set the serial poll status byte.
   sic                   Controller Send interface clear and set remote enable (REN).


                                                    © National Instruments 2801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2802 ordinal=2802 -->
## Functions

Functions


            Functions          Type      Description
         sre 0/1             Controller  Set or clear remote enable (REN).

           To specify the GPIB Controller used by this function, use a command string in the form, ID: xxx,
           where ID is the GPIB Controller (bus number) and xxx is the three-character command and its
            corresponding arguments, if any. If you do not specify a Controller ID, LabVIEW assumes 0.

             Refer to GPIB Device and Controller Functions for more information.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      output string —

           output string is the response the function returns when you conduct a parallel poll with the rpp
         command string. Set output string only when you use the rrp command string.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout


2802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2803 ordinal=2803 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GPIBGPIB 488.2488.2

Use the GPIB 488.2 functions to exchange data and instructions between VIs and GPIB
488.2 devices.

The functions on this palette can return GPIB error codes.


 Palette Object  Description

 Send Function  Sends data bytes to a single GPIB device.

 Receive
               Reads data bytes from a GPIB device. Function

 Trigger
                  Triggers a single device. Function

 DevClear
                 Clears a single device.
 Function

 ReadStatus
                   Serial polls a single device to get its status byte.
 Function

 PPollConfig
                Configures a device for parallel polls.
 Function

                Unconfigures devices for parallel polls. PPollUnconfig unconfigures the GPIB
 PPollUnconfig
                 devices whose addresses are contained in the address list array for parallel polls.
 Function
               These devices no longer participate in polls.

 PassControl
                Passes control to another device with Controller capability.
 Function


                                                    © National Instruments 2803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2804 ordinal=2804 -->
## Functions

Functions


         Palette Object  Description

         SendList                     Sends data bytes to multiple GPIB devices.         Function

        FindRQS                       Determines which device is requesting service.         Function

          TriggerList                          Triggers multiple devices simultaneously.         Function

         DevClearList                          Clears multiple devices simultaneously.         Function

          AllSpoll                            Serial polls all devices.         Function

         PPoll Function  Performs a parallel poll.

        EnableRemote                       Enables remote programming of multiple GPIB devices.         Function

        EnableLocal                       Enables local mode for multiple devices.         Function

         FindLstn                        Finds all Listeners on the GPIB.         Function

         TestSys                           Directs multiple devices to conduct IEEE 488.2 self-tests.         Function

        ResetSys       Performs bus initialization, message exchange initialization, and device
         Function         initialization.

        SendIFC                          Clears the GPIB functions with Interface Clear (IFC).         Function

        TestSRQ
                       Determines the current state of the SRQ line.
         Function

        WaitSRQ
                        Waits until a device asserts Service Request.
         Function

       SetRWLS
                         Places particular devices in the Remote With Lockout State.
         Function

       SendLLO
                     Sends the Local Lockout (LLO) message to all devices.
         Function

        SendDataBytes
                     Sends data bytes to previously addressed devices.
         Function

2804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2805 ordinal=2805 -->
## Functions

Functions


 Palette Object  Description

 SendSetup                Prepares particular devices to receive data bytes. Function

 SendCmds              Sends GPIB command bytes. Function

 RcvRespMsg               Reads data bytes from a previously addressed device. Function

 ReceiveSetup   Prepares a device to send data bytes and prepares the GPIB controller to read data
 Function        bytes.

 SetTimeOut              Changes the global timeout period for all GPIB 488.2 functions. Function

              Combines primary address and secondary address in a specially formatted MakeAddr
              packed address for devices that require both a primary and secondary GPIB Function                 address.

SendSend FunctionFunction

Sends data bytes to a single GPIB device.

This function is similar to the SendList function, except that the Send function sends
data to a single GPIB device.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —

    bus The function addresses the interface indicated by bus as a Talker.


                                                    © National Instruments 2805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2806 ordinal=2806 -->
## Functions

Functions


           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0. Refer to the software installation instructions included with your GPIB
             controller for additional GPIB interfaces.

               •      address —

           address addresses the device indicated by address as a Listener.

                    If you do not wire address, the function sends data string with no addressing, thereby sending it
             to all previously addressed Listeners. To send data string to several devices, use the SendList
             function. If a secondary address is required, use the MakeAddr function to format the primary
          and secondary addresses properly.

               •     mode —

         mode describes how to signal the end of the data to the Listener.

             This input accepts the following values.

           0 Do nothing to mark the end of the transfer (default).
           1 Send NL (linefeed) with EOI after the data bytes.
           2 Send EOI with the last data byte in the string.

               •      data string —

           data string contains the data bytes that the function sends to the GPIB device.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2807 ordinal=2807 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •      byte count —

    byte count refers to the number of bytes that pass over the GPIB.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ReceiveReceive FunctionFunction

Reads data bytes from a GPIB device.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —


                                                    © National Instruments 2807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2808 ordinal=2808 -->
## Functions

Functions


           bus The function addresses the interface indicated by bus as a Listener.

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0. Refer to the software installation instructions included with your GPIB
             controller for additional GPIB interfaces.
               •      address —

           address contains the primary address of the GPIB device with which the function
           communicates.

                    If a secondary address is required, use the MakeAddr function to format the primary and
           secondary addresses.
               •     mode —

         mode selects the method that signals the end of the data.

          The default is 0. If mode is a value from decimal 0 through 255, the ASCII character that
            corresponds to it is the termination character, and the function stops the read when it detects
            the character. If mode is not wired, or is decimal 256, the function stops the read when it detects
           END.
               •      count —

           count is the maximum number of data bytes to return from the device in data string.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data string —

           data string contains count data bytes from the GPIB device.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2809 ordinal=2809 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •      byte count —

    byte count refers to the number of bytes that pass over the GPIB.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Receive terminates when the function does one of the following:

  • Reads the number of bytes requested
  • Detects an error
  • Exceeds the time limit
  • Detects the END message (EOI asserted)
  • Detects the EOS character (assuming the value supplied to mode has enabled this
    option)

TriggerTrigger FunctionFunction

Triggers a single device.

Use the TriggerList function to send a single message that triggers several GPIB
devices.


                                                    © National Instruments 2809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2810 ordinal=2810 -->
## Functions

Functions

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •      address —

           address sends the GPIB Group Execute Trigger message to the device at address.

                    If the address terminal is not wired, the function sends the Group Execute Trigger message with
          no addressing, and this triggers all previously addressed Listeners. If a secondary address is
             required, use the MakeAddr function to put the primary and secondary addresses in the proper
            format.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active


2810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2811 ordinal=2811 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


DevClearDevClear FunctionFunction

Clears a single device.

Use the DevClearList function to send the Selected Device Clear (SDC) message to
several GPIB devices.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional


                                                    © National Instruments 2811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2812 ordinal=2812 -->
## Functions

Functions


           GPIB interfaces.

               •      address —

           address sends the GPIB SDC message to the device at address.

                    If the address terminal is not wired, the function sends the Universal Device Clear message to all
            devices on the GPIB. If a secondary address is required, use the MakeAddr function to put the
            primary and secondary addresses in the proper format.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2813 ordinal=2813 -->
## Functions

Functions

ReadStatusReadStatus FunctionFunction

Serial polls a single device to get its status byte.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •      address —

    address contains the primary address of the GPIB device with which the function
    communicates.

       If a secondary address is required, use the MakeAddr function to format the primary and
    secondary addresses.
   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       serial poll response —

     serial poll response is the status byte of the device at address.

    Refer to the documentation supplied with the device to learn how to interpret this byte.
   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.


                                                    © National Instruments 2813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2814 ordinal=2814 -->
## Functions

Functions

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      PPollConfigPPollConfig FunctionFunction

       Configures a device for parallel polls.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —


2814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2815 ordinal=2815 -->
## Functions

Functions


  bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
  default bus number is 0.

  Refer to the software installation instructions included with the GPIB controller for additional
  GPIB interfaces.
•      address —

  address configures the GPIB device at address for parallel polls according to the dataline and
  sense parameters.

   If a secondary address is required, use the MakeAddr function to put the primary and secondary
  addresses in the proper format.
•       dataline —

  dataline is the data line, 1 to 8, on which the device responds to the parallel poll.

•      sense —

  sense indicates the condition under which the data line is asserted or unasserted.

  The device compares the sense value, TRUE or FALSE, to its individual status bit and responds
  accordingly.
•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       status —

  status is a Boolean array in which each bit describes a state of the GPIB Controller.

   If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

  The following table shows the numeric value and symbolic status of each bit in status. This table
  also includes a description of each bit.

  Status Bit    Numeric Value      Symbolic Status       Description
  0           1               DCAS                 Device Clear state
  1           2                DTAS                  Device Trigger State
  2           4                 LACS                   Listener Active
  3           8                 TACS                   Talker Active
  4           16               ATN                    Attention Asserted


                                                   © National Instruments 2815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2816 ordinal=2816 -->
## Functions

Functions


            Status Bit    Numeric Value      Symbolic Status       Description
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      PPollUnconfigPPollUnconfig FunctionFunction

       Unconfigures devices for parallel polls. PPollUnconfig unconfigures the GPIB devices
      whose addresses are contained in the address list array for parallel polls. These
       devices no longer participate in polls.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •      address list —


2816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2817 ordinal=2817 -->
## Functions

Functions


  address list contains a list of all of the instruments to which this function sends the Parallel Poll
  Unconfigure command.

  Each element of this array contains the primary address of a single instrument. If a secondary
  address is required, use the MakeAddr function to format the primary and secondary addresses.
   If you do not wire this input, this function sends the Parallel Poll Unconfigure command to all
  connected GPIB instruments.
•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       status —

  status is a Boolean array in which each bit describes a state of the GPIB Controller.

   If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

  The following table shows the numeric value and symbolic status of each bit in status. This table
  also includes a description of each bit.

  Status Bit    Numeric Value      Symbolic Status       Description
  0           1               DCAS                 Device Clear state
  1           2                DTAS                  Device Trigger State
  2           4                 LACS                   Listener Active
  3           8                 TACS                   Talker Active
  4           16               ATN                    Attention Asserted
  5           32                  CIC                     Controller-In-Charge
  6           64              REM                Remote State
  7           128              LOK                  Lockout State
  8           256             CMPL                 Operation Completed
  12          4096              SRQI              SRQ Detected while CIC
  13          8192            END                 EOI or EOS Detected
  14          16384            TIMO                Timeout
  15           -32768            ERR                    Error Detected

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2818 ordinal=2818 -->
## Functions

Functions

      PassControlPassControl FunctionFunction

       Passes control to another device with Controller capability.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •      address —

           address sends the GPIB Device Take Control message to the device specified by address.

                    If a secondary address is required, use the MakeAddr function to put the primary and secondary
            addresses in the proper format.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2819 ordinal=2819 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SendListSendList FunctionFunction

Sends data bytes to multiple GPIB devices.

This function is similar to the Send function, except that SendList sends data to
multiple listeners with only one transmission.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —


                                                    © National Instruments 2819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2820 ordinal=2820 -->
## Functions

Functions


           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.

               •      address list —

           address list array contains a list of GPIB addresses for devices, which the function addresses as
              Listeners.

                    If a secondary address is required, use the MakeAddr function to put the primary and secondary
            addresses in the proper format.

               •     mode —

         mode describes how to signal the end of the data to the Listener.

             This input accepts the following values.

           0 Do nothing to mark the end of the transfer (default).
           1 Send NL (linefeed) with EOI after the data bytes.
           2 Send EOI with the last data byte in the string.

               •      data string —

           data string contains the data bytes that the function sends to the addressed devices.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2821 ordinal=2821 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •      byte count —

    byte count refers to the number of bytes that pass over the GPIB.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FindRQSFindRQS FunctionFunction

Determines which device is requesting service.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —


                                                    © National Instruments 2821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2822 ordinal=2822 -->
## Functions

Functions


           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •      address list —

           address list serial polls the GPIB devices listed in address list, starting at the beginning of the
           address list array, until the function finds the device asserting SRQ.

                    If a secondary address is required, use the MakeAddr function to put the primary and secondary
            addresses in the proper format.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      requester status byte —

            requester status byte is the status byte for the device asserting SRQ.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected


2822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2823 ordinal=2823 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •      requester index —

    requester index is the index of the address in address list of the device asserting SRQ.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


TriggerListTriggerList FunctionFunction

Triggers multiple devices simultaneously.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •      address list —

    address list simultaneously triggers GPIB devices whose addresses appear in address list.

       If the address list terminal is not wired, the function sends the Group Execute Trigger message
    without addressing, which triggers all previously addressed Listeners. If a secondary address is
    required, use the MakeAddr function to put the primary and secondary addresses in the proper
    format.

                                                    © National Instruments 2823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2824 ordinal=2824 -->
## Functions

Functions

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       DevClearListDevClearList FunctionFunction

       Clears multiple devices simultaneously.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


2824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2825 ordinal=2825 -->
## Functions

Functions


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.

   •      address list —

    address list sends the GPIB Selected Device Clear (SDC) message to the devices listed in address
      list.

       If the address list terminal is not wired, the function sends the Universal Device Clear message
    to all devices on the GPIB. If a secondary address is required, use the MakeAddr function to put
    the primary and secondary addresses in the proper format.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table
    also includes a description of each bit.

    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted


                                                    © National Instruments 2825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2826 ordinal=2826 -->
## Functions

Functions


            Status Bit    Numeric Value      Symbolic Status       Description
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       AllSpollAllSpoll FunctionFunction

        Serial polls all devices.

      Although the AllSpoll function is general enough to serial poll any number of GPIB
       devices, use the ReadStatus function when you serial poll only one GPIB device.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.


2826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2827 ordinal=2827 -->
## Functions

Functions

•      address list —

  address list serial polls GPIB devices whose addresses appear in address list.

   If a secondary address is required, use the MakeAddr function to put the primary and secondary
  addresses in the proper format.

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       serial poll byte list —

  serial poll byte list contains the responses of the devices whose addresses are contained in the
  corresponding elements of address list.

•       status —

  status is a Boolean array in which each bit describes a state of the GPIB Controller.

   If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

  The following table shows the numeric value and symbolic status of each bit instatus. This table
  also includes a description of each bit.

  Status Bit    Numeric Value      Symbolic Status       Description
  0           1               DCAS                 Device Clear state
  1           2                DTAS                  Device Trigger State
  2           4                 LACS                   Listener Active
  3           8                 TACS                   Talker Active
  4           16               ATN                    Attention Asserted
  5           32                  CIC                     Controller-In-Charge
  6           64              REM                Remote State
  7           128              LOK                  Lockout State
  8           256             CMPL                 Operation Completed
  12          4096              SRQI              SRQ Detected while CIC
  13          8192            END                 EOI or EOS Detected
  14          16384            TIMO                Timeout
  15           -32768            ERR                    Error Detected

•      byte count —


                                                   © National Instruments 2827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2828 ordinal=2828 -->
## Functions

Functions


            byte count contains the index of any device that times out instead of responding to the poll.

         On success, byte count returns the number of responses in serial poll byte list. If an error
             occurs, byte count returns the index of address list of the first address that timed out or was
              invalid.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       PPollPPoll FunctionFunction

      Performs a parallel poll.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       parallel poll byte —

             parallel poll byte is the result of the parallel poll.

           Each bit of the poll result returns one bit of status information from each device configured for
              parallel polls. The state of each bit, 0 or 1, and the interpretation of these states are based on the

2828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2829 ordinal=2829 -->
## Functions

Functions

     latest parallel poll configuration sent to the devices and on the individual status of the devices.
   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table
    also includes a description of each bit.

    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


EnableRemoteEnableRemote FunctionFunction

Enables remote programming of multiple GPIB devices.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


                                                    © National Instruments 2829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2830 ordinal=2830 -->
## Functions

Functions

      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •      address list —

           address list sends the GPIB Remote Enable (REN) command to the devices listed in address list.

                    If the address list terminal is not wired, the function performs no addressing, and the Remote
           Enable (REN) line asserts. If a secondary address is required, use the MakeAddr function to put
            the primary and secondary addresses in the proper format.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected


2830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2831 ordinal=2831 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


EnableLocalEnableLocal FunctionFunction

Enables local mode for multiple devices.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •      address list —

    address list sends the GPIB Go To Local (GTL) command to the devices listed in address list.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       status —


                                                    © National Instruments 2831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2832 ordinal=2832 -->
## Functions

Functions


             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FindLstnFindLstn FunctionFunction

       Finds all Listeners on the GPIB.

       FindLstn detects the presence of devices at particular addresses because most GPIB
       devices have the ability to listen. When you detect the devices, you can usually
       interrogate them to determine their identity.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


2832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2833 ordinal=2833 -->
## Functions

Functions


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •      address list —

    address list tests for the presence of a Listener for all devices listed in address list.

       If the function does not detect a listening device at the particular primary address, it tests all the
    secondary addresses associated with that primary address.
   •       limit —

     limit If more Listeners are present on the bus than limit specifies, the function truncates listener
    address list after limit entries.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       listener address list —

     listener address list contains the addresses of all the Listeners the function finds.

   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table
    also includes a description of each bit.


                                                    © National Instruments 2833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2834 ordinal=2834 -->
## Functions

Functions


            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •     number of listeners —

          number of listeners contains the number of addresses placed in listener address list.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      TestSysTestSys FunctionFunction

       Directs multiple devices to conduct IEEE 488.2 self-tests.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —


2834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2835 ordinal=2835 -->
## Functions

Functions


  bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
  default bus number is 0.

  Refer to the software installation instructions included with the GPIB controller for additional
  GPIB interfaces.
•      address list —

  address list contains a list of GPIB devices which receive instructions from the function to
  conduct their self-test procedures.

   If a secondary address is required, use the MakeAddr function to put the primary and secondary
  addresses in the proper format.
•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       result list —

  result list Each device returns an integer code signifying the results of its tests. TestSys returns
  these codes in the corresponding elements of result list.

  A result code of 0 indicates the device passed its tests. Any other value indicates the tests
  resulted in an error.
•       status —

  status is a Boolean array in which each bit describes a state of the GPIB Controller.

   If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

  The following table shows the numeric value and symbolic status of each bit in status. This table
  also includes a description of each bit.

  Status Bit    Numeric Value      Symbolic Status       Description
  0           1               DCAS                 Device Clear state
  1           2                DTAS                  Device Trigger State
  2           4                 LACS                   Listener Active
  3           8                 TACS                   Talker Active
  4           16               ATN                    Attention Asserted
  5           32                  CIC                     Controller-In-Charge
  6           64              REM                Remote State
  7           128              LOK                  Lockout State


                                                   © National Instruments 2835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2836 ordinal=2836 -->
## Functions

Functions


            Status Bit    Numeric Value      Symbolic Status       Description
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       failed devices —

              failed devices contains the number of devices that failed their tests.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      ResetSysResetSys FunctionFunction

      Performs bus initialization, message exchange initialization, and device initialization.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •      address list —

           address list contains the primary address of the GPIB device with which the function
           communicates.


2836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2837 ordinal=2837 -->
## Functions

Functions

       If a secondary address is required, use the MakeAddr function to put the primary and secondary
    addresses in the proper format.
   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table
    also includes a description of each bit.

    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


First, the function asserts Remote Enable (REN), followed by Interface Clear (IFC),
unaddressing all devices and making the GPIB controller (the System Controller) the
Controller-In-Charge.

Second, the function sends the Device Clear (DCL) message to all connected devices.
This ensures that all IEEE 488.2-compatible devices can receive the Reset (RST)

                                                    © National Instruments 2837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2838 ordinal=2838 -->
## Functions

Functions

      message that follows.

       Third, the function sends the *RST message to all devices whose addresses are
       contained in the address list array. This message initializes device-specific functions
       within each device.

      SendIFCSendIFC FunctionFunction

       Clears the GPIB functions with Interface Clear (IFC).

     When you issue the GPIB Device IFC message, the interface functions of all connected
       devices return to their cleared states.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2839 ordinal=2839 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use this function as part of a GPIB initialization. It forces the interface to be Controller
of the GPIB and ensures that the connected devices are all unaddressed and that the
interface functions of the devices are in their idle states.

TestSRQTestSRQ FunctionFunction

Determines the current state of the SRQ line.

This function is similar in format to the WaitSRQ function, except that WaitSRQ
suspends itself while it waits for an occurrence of SRQ, and TestSRQ immediately
returns the current SRQ state.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


                                                    © National Instruments 2839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2840 ordinal=2840 -->
## Functions

Functions

      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     SRQ —

         SRQ is TRUE if the SRQ line is asserted and FALSE if it is not.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —


2840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2841 ordinal=2841 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


WaitSRQWaitSRQ FunctionFunction

Waits until a device asserts Service Request.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     SRQ —

       If the SRQ occurs within the timeout period specified in the GPIB configuration, the function
    returns TRUE in SRQ.

    Otherwise, the function returns FALSE.
   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table
    also includes a description of each bit.

                                                    © National Instruments 2841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2842 ordinal=2842 -->
## Functions

Functions


            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The function suspends execution until a GPIB device connected on the GPIB asserts
       the Service Request (SRQ) line.

      WaitSRQ is similar in format to the TestSRQ function, except that TestSRQ returns the
     SRQ status immediately, whereas WaitSRQ suspends the program for the duration of
       the timeout period, but no longer, waiting for an SRQ to occur.

     SetRWLSSetRWLS FunctionFunction

       Places particular devices in the Remote With Lockout State.


      Inputs/Outputs

               •      bus —


2842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2843 ordinal=2843 -->
## Functions

Functions


  bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
  default bus number is 0.

  Refer to the software installation instructions included with the GPIB controller for additional
  GPIB interfaces.
•      address list —

  address list contains a list of the GPIB devices with which the function communicates.

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       status —

  status is a Boolean array in which each bit describes a state of the GPIB Controller.

   If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

  The following table shows the numeric value and symbolic status of each bit in status. This table
  also includes a description of each bit.

  Status Bit    Numeric Value      Symbolic Status       Description
  0           1               DCAS                 Device Clear state
  1           2                DTAS                  Device Trigger State
  2           4                 LACS                   Listener Active
  3           8                 TACS                   Talker Active
  4           16               ATN                    Attention Asserted
  5           32                  CIC                     Controller-In-Charge
  6           64              REM                Remote State
  7           128              LOK                  Lockout State
  8           256             CMPL                 Operation Completed
  12          4096              SRQI              SRQ Detected while CIC
  13          8192            END                 EOI or EOS Detected
  14          16384            TIMO                Timeout
  15           -32768            ERR                    Error Detected

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2844 ordinal=2844 -->
## Functions

Functions

      The function sends Remote Enable (REN) to the GPIB devices listed in address list. It
       also places all devices in Lockout State, which prevents them from independently
       returning to local programming mode without intervention by the Controller.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.

     SendLLOSendLLO FunctionFunction

      Sends the Local Lockout (LLO) message to all devices.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2845 ordinal=2845 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •       error out —

    error out contains error information. This output provides standard error out functionality.


When the function sends the GPIB Local Lockout message, a device cannot
independently choose the local or remote state. While Local Lockout is in effect, only
the Controller can alter the local or remote state of the devices by sending the
appropriate GPIB messages. Use SendLLO only in unusual local/remote situations,
particularly those in which you must lock all devices into local programming state. Use
the SetRWLS function when you want to place devices in Remote Mode With Lockout
State.

SendDataBytesSendDataBytes FunctionFunction

Sends data bytes to previously addressed devices.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


                                                    © National Instruments 2845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2846 ordinal=2846 -->
## Functions

Functions


      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.

               •     mode —

         mode describes how to signal the end of the data to the Listener.

             This input accepts the following values.

           0 Do nothing to mark the end of the transfer (default).
           1 Send NL (linefeed) with EOI after the data bytes.
           2 Send EOI with the last data byte in the string.

               •      data string —

           data string contains the data bytes the function sends over the GPIB.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.


2846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2847 ordinal=2847 -->
## Functions

Functions


    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State
    7           128              LOK                  Lockout State
    8           256             CMPL                 Operation Completed
    12          4096              SRQI              SRQ Detected while CIC
    13          8192            END                 EOI or EOS Detected
    14          16384            TIMO                Timeout
    15           -32768            ERR                    Error Detected

   •      byte count —

    byte count refers to the number of bytes that pass over the GPIB.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SendSetupSendSetup FunctionFunction

Prepares particular devices to receive data bytes.

You normally follow a call to this function with a call to a function such as
SendDataBytes to actually transfer the data to the Listeners. This sequence eliminates
the need to readdress the devices between blocks of sends.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


                                                    © National Instruments 2847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2848 ordinal=2848 -->
## Functions

Functions

      Inputs/Outputs

               •      bus —

           bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
             default bus number is 0.

             Refer to the software installation instructions included with the GPIB controller for additional
           GPIB interfaces.
               •      address list —

           address list addresses GPIB devices whose addresses appear in address list as Listeners.

                    If a secondary address is required, use the MakeAddr function to put the primary and secondary
            addresses in the proper format.
               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected


2848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2849 ordinal=2849 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SendCmdsSendCmds FunctionFunction

Sends GPIB command bytes.

You normally do not need to use SendCmds for GPIB operation. Use it when
specialized command sequences, not provided for in other functions, must be sent
over the GPIB.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.

Refer to GPIB Multiline Interface Messages for more information about available
commands.


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •     command string —

   command string contains the command bytes the function sends over the GPIB.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 2849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2850 ordinal=2850 -->
## Functions

Functions

               •       status —

             status is a Boolean array in which each bit describes a state of the GPIB Controller.

                    If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •      byte count —

            byte count refers to the number of bytes that pass over the GPIB.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      RcvRespMsgRcvRespMsg FunctionFunction

      Reads data bytes from a previously addressed device.

      RcvRespMsg assumes that another function, such as ReceiveSetup, Receive, or
      SendCmds, has already addressed the GPIB Talkers and Listeners. You use RcvRespMsg
        specifically to skip the addressing step of GPIB management. Use the Receive function
       to perform the entire sequence of addressing and then to receive the data bytes.


2850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2851 ordinal=2851 -->
## Functions

Functions

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •     mode —

   mode determines the data termination method.

    The default is 0. If mode is from 0 through decimal 255, the ASCII character that corresponds to it
      is the termination character, and the function stops the read when it detects the character. If
   mode is not wired or is decimal 256, the read stops when the function detects the END message
     (EOI).
   •      count —

    count is the maximum number of data bytes to read from the GPIB.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data string —

    data string contains the bytes read from the GPIB.

   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.


                                                    © National Instruments 2851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2852 ordinal=2852 -->
## Functions

Functions

          The following table shows the numeric value and symbolic status of each bit in status. This table
             also includes a description of each bit.

            Status Bit    Numeric Value      Symbolic Status       Description
           0           1               DCAS                 Device Clear state
           1           2                DTAS                  Device Trigger State
           2           4                 LACS                   Listener Active
           3           8                 TACS                   Talker Active
           4           16               ATN                    Attention Asserted
           5           32                  CIC                     Controller-In-Charge
           6           64              REM                Remote State
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •      byte count —

            byte count refers to the number of bytes that pass over the GPIB.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      ReceiveSetupReceiveSetup FunctionFunction

       Prepares a device to send data bytes and prepares the GPIB controller to read data
       bytes.

        After you call this function, you can use a function such as RcvRespMsg to transfer the
       data from the Talker. In this way, you eliminate the need to readdress the devices
      between blocks of reads.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


2852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2853 ordinal=2853 -->
## Functions

Functions


Inputs/Outputs

   •      bus —

    bus refers to the GPIB bus number. If you have only one GPIB interface in your computer, the
     default bus number is 0.

    Refer to the software installation instructions included with the GPIB controller for additional
    GPIB interfaces.
   •      address —

    address prepares a device to send data bytes by addressing the device as a Talker and prepares
    the GPIB controller to receive transmitted data bytes.

    address contains the primary address of the GPIB device with which the function
    communicates. If a secondary address is required, use the MakeAddr function to format the
    primary and secondary addresses.
   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       status —

    status is a Boolean array in which each bit describes a state of the GPIB Controller.

       If an error occurs, the function sets bit 15. GPIB error is valid only if bit 15 of status is set.

    The following table shows the numeric value and symbolic status of each bit in status. This table
    also includes a description of each bit.

    Status Bit    Numeric Value      Symbolic Status       Description
    0           1               DCAS                 Device Clear state
    1           2                DTAS                  Device Trigger State
    2           4                 LACS                   Listener Active
    3           8                 TACS                   Talker Active
    4           16               ATN                    Attention Asserted
    5           32                  CIC                     Controller-In-Charge
    6           64              REM                Remote State


                                                    © National Instruments 2853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2854 ordinal=2854 -->
## Functions

Functions


            Status Bit    Numeric Value      Symbolic Status       Description
           7           128              LOK                  Lockout State
           8           256             CMPL                 Operation Completed
           12          4096              SRQI              SRQ Detected while CIC
           13          8192            END                 EOI or EOS Detected
           14          16384            TIMO                Timeout
           15           -32768            ERR                    Error Detected

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      SetTimeOutSetTimeOut FunctionFunction

      Changes the global timeout period for all GPIB 488.2 functions.

       This function also sets the default timeout period for all GPIB functions. This function
       defaults to the next higher ibtmo value.

       Refer to GPIB Function Defaults for more information about the timeout and address
        defaults.


      Inputs/Outputs

               •     new timeout (10000) —

         new timeout defaults to 10,000 ms.

               •      previous timeout —

            previous timeout is the previous timeout period for all GPIB 488.2 functions.


      The following table lists some sample input values and their resulting timeout values.


2854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2855 ordinal=2855 -->
## Functions

Functions


 Input Value                                   Resulting Timeout

 0-1ms                               1ms

 1ms                                3ms

 4-10ms                               10ms

 11-30ms                              30ms

 31-100ms                              100ms

 101-300ms                             300ms

 301-1000ms                                  1s

 1001-3000ms                                 3s

 3001-10000ms                               10s

 10001-30000ms                              30s

 30001-100000ms                            100s

 100001-300000ms                           300s

 300001+ ms                                1000s

MakeAddrMakeAddr FunctionFunction

Combines primary address and secondary address in a specially formatted packed
address for devices that require both a primary and secondary GPIB address.

Refer to GPIB Function Defaults for more information about the timeout and address
defaults.


Inputs/Outputs

   •      primary address —

    primary address is placed in the lower byte of the packed address by MakeAddr.

   •      secondary address —

                                                    © National Instruments 2855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2856 ordinal=2856 -->
## Functions

Functions


           secondary address is placed in the upper byte of the packed address by MakeAddr.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      packed address —

           packed address contains primary address in its lower byte and secondary address in its upper
             byte. You can use packed address as the address input to the GPIB 488.2 Functions.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    GPIBGPIB DeviceDevice andand ControllerController FunctionsFunctions

      The GPIB Device and Controller functions listed in the GPIB Misc function description
       are described here. Notice that there are both device and controller versions of the ppc
      and loc commands. The syntax and use of the commands are slightly different for each
       version.

      You can use these functions with all GPIB Controllers accessible by LabVIEW unless
       stated otherwise in the function description. An ECMD error (17) results when you
       execute a function for a GPIB Controller without the specified capability. The function
       syntax is strict. Each function recognizes only lowercase characters and allows only
      one space between the function name and the arguments.

      ControllerController FunctionsFunctions

      The controller functions configure the controller or send IEEE 488 commands to which
         all instruments respond.

     cac—Become Active Controller

     cmd—Send IEEE 488 Commands


2856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2857 ordinal=2857 -->
## Functions

Functions

dma—Set DMA Mode or Programmed I/O Mode

gts—Go from Active Controller to Standby

ist—Set Individual Status Bit

llo—Local Lockout

loc—Place Controller in Local State

off—Take Controller Offline

ppc—Parallel Poll Configure (Enable and Disable)

ppu—Parallel Poll Unconfigure

rpp—Conduct Parallel Poll

rsc—Release or Request System Control

rsv—Request Service and/or Set the Serial Poll Status Byte

sic—Send Interface Clear

sre—Unassert or Assert Remote Enable

cac—Become Active Controller

 syntax           cac 0 (take control synchronously)

                 cac 1 (take control immediately)

cac takes control either synchronously or immediately, and in some cases
asynchronously. You generally do not need to use the cac function because other
functions, such as cmd and rpp, take control automatically.

If you try to take control synchronously when a data handshake is in progress, the
function postpones the take control action until the handshake is complete. If a
handshake is not in progress, the function executes the take control action

                                                    © National Instruments 2857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2858 ordinal=2858 -->
## Functions

Functions

       immediately. Taking control synchronously is not guaranteed if a read or write
       operation completes with a timeout or other error.

      You should take control asynchronously when it is impossible to gain control
       synchronously, for example, after a timeout error.

      The ECIC error results if the GPIB controller is not CIC.

    cmd—Send IEEE 488 Commands

         syntax                      cmd string

     cmd sends GPIB command messages. These command messages include device talk
      and listen addresses, secondary addresses, serial and parallel poll configuration
      messages, and device clear and trigger messages.

      You do not use cmd to transmit programming instructions to devices. The GPIB Read
      and GPIB Write functions transmit programming instructions and other device-
      dependent information.

        string contains the command bytes the controller sends. ASCII characters represent
       these bytes in cmd string. If you must send characters that cannot be displayed, you
      can enable backslash codes on the string control or string constant, or you can use a
       format function to list the commands in hexadecimal.

     dma—Set DMA Mode or Programmed I/O Mode

         syntax          dma 0 (use programmed I/O)

                    dma 1 (use DMA)

     dma indicates whether data transfers use DMA.

     Some GPIB controllers do not have DMA capability. If you try to execute dma 1, the
       function returns GPIB error 11 to indicate no capability.


2858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2859 ordinal=2859 -->
## Functions

Functions

gts—Go from Active Controller to Standby

 syntax             gts 0 (no shadow handshaking)

                    gts 1 (shadow handshaking)

gts sets the GPIB controller to the controller standby state and unasserts the ATN
signal if it is the active controller. Normally, the GPIB controller is involved in the data
transfer. gts permits GPIB devices to transfer data without involving the GPIB
controller.

If shadow handshaking is active, the GPIB controller participates in the GPIB transfer
as a listener but does not accept any data. When it detects the END message, the GPIB
controller asserts the Not Ready For Data (NRFD) to create a handshake holdoff state.

If shadow handshaking is not active, the GPIB controller performs neither shadow
handshaking nor a handshake holdoff.

If you enable the shadow handshake option, the GPIB controller participates in a data
handshake as a listener without actually reading the data. It monitors the transfer for
the END message and stops subsequent transfers. This mechanism allows the GPIB
controller to take control synchronously on subsequent operations such as cmd or
rpp.

After you send the gts command, wait for END before you initiate another GPIB
command. You can do this with the GPIB Wait function.

The ECIC error results if the GPIB controller is not CIC.

ist—Set Individual Status Bit

 syntax         ist 0 (individual status bit is cleared)

                  ist 1 (individual status bit is set)

                  ist sets the sense of the individual status (ist) bit.

Use ist when the GPIB controller is not the CIC but participates in a parallel poll
conducted by a device that is the active controller. The CIC conducts a parallel poll by

                                                    © National Instruments 2859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2860 ordinal=2860 -->
## Functions

Functions

       asserting the EOI and ATN signals, which send the Identify (IDY) message. While this
      message is active, each device that you configured to participate in the poll responds
      by asserting a predetermined GPIB data line either TRUE or FALSE, depending on the
       value of its local ist bit. For example, you can assign the GPIB controller to drive the
      DIO3 data line TRUE if ist is 1 and FALSE if ist is 0. Conversely, you can assign it to drive
      DIO3 TRUE if ist is 0 and FALSE if ist is 1.

      The Parallel Poll Enable (PPE) message in effect for each device determines the
       relationship among the value of ist, the line that is driven, and the sense at which the
        line is driven. The GPIB controller is capable of receiving this message either locally
       using ppc or remotely through a command from the CIC. After the PPE message
       executes, ist changes the sense at which the GPIB controller drives the line during the
        parallel poll, and the GPIB controller can convey a one-bit, device-dependent message
       to the controller.

      llo—Local Lockout

         syntax                                                                    llo

        llo places all devices in local lockout state. This action usually inhibits recognition of
       inputs from the front panel of the device.

        llo sends the Local Lockout (LLO) command.

      loc—Place Controller in Local State

         syntax                                                        loc

       loc places the GPIB controller in a local state by sending the local message Return To
       Local (RTL) if it is not locked in remote mode (indicated by the LOK bit of status). You
      use loc to simulate a front panel RTL switch when you use a computer to simulate an
       instrument.

      off—Take Controller Offline

         syntax                                                               off


2860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2861 ordinal=2861 -->
## Functions

Functions

off takes the controller offline. This is only needed when sharing the controller with
another application which is using the NI-488 Library.

ppc—Parallel Poll Configure (Enable and Disable)

 syntax                              ppc byte

ppc configures the GPIB Controller to participate in a parallel poll by setting its Local
Poll Enable (LPE) message to the value of byte. If the value of byte is 0, the GPIB
controller unconfigures itself.

Each of the 16 Parallel Poll Enable (PPE) messages selects the GPIB data line (DIO1
through DIO8) and sense (1 or 0) that the device must use when responding to the
Identify (IDY) message during a parallel poll. The device interprets the assigned
message and the current value of the individual status (ist) bit to determine if the
selected line is driven TRUE or FALSE. For example, if PPE=0x64, DIO5 is driven TRUE if
ist is 0 and FALSE if ist is 1. If PPE=0x68, DIO1 PPE message is in effect. You must know
which PPE and PPD messages are sent and determine what the responses indicate.

ppu—Parallel Poll Unconfigure

 syntax                                       ppu

ppu disables all devices from responding to parallel polls.

ppu sends the Parallel Poll Unconfigure (PPU) command.

rpp—Conduct Parallel Poll

 syntax                                              rpp

rpp conducts a parallel poll of previously configured devices by asserting the ATN and
EOI signals, which sends the IDY message.

rpp places the parallel poll response in the output string as ASCII characters.


                                                    © National Instruments 2861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2862 ordinal=2862 -->
## Functions

Functions

      rsc—Release or Request System Control

         syntax              rsc 0 (release system control)

                              rsc 1 (request system control)

       rsc releases or requests the capability of the GPIB controller to send the Interface Clear
        (IFC) and Remote Enable (REN) messages to GPIB devices using the sic and sre
       functions. For the GPIB controller to respond to IFC sent by another controller, the
      GPIB controller must not be the system controller.

        In most applications, the GPIB controller is always the system controller. You use rsc
       only if the computer is not the system controller for the duration of the program
       execution.

     rsv—Request Service and/or Set the Serial Poll Status Byte

         syntax                                      rsv byte

       rsv sets the serial poll status byte of the GPIB controller to byte. If the 0x40 bit is set in
       byte, the GPIB controller also requests service from the controller by asserting the
      GPIB RQS line. For example, if you want to assert the GPIB RQS line, send the ASCII
       character @, in which the 0x40 bit is set.

      You use rsv to request service from the controller using the Service Request (SRQ)
       signal and to provide a system-dependent status byte when the controller serial polls
       the GPIB port.

     sic—Send Interface Clear

         syntax                                                                sic

        sic causes the controller to assert the IFC signal for at least 100 ms if the controller has
      system controller authority. This action initializes the GPIB and makes the Controller
       port CIC. You generally use sic when you want a device to become CIC or to clear a bus
        fault condition.


2862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2863 ordinal=2863 -->
## Functions

Functions

The IFC signal resets only the GPIB functions of bus devices; it does not reset internal
device functions. The Device Clear (DCL) and Selected Device Clear (SDC) commands
reset the device functions. Consult the instrument documentation to determine the
effect of these messages.

sre—Unassert or Assert Remote Enable

 syntax             sre 0 (unassert Remote Enable)

                    sre 1 (assert Remote Enable)

sre unasserts or asserts the GPIB REN line. Devices monitor REN when they select
between local and remote modes of operation. A device does not actually enter
remote mode until it receives its listen address.

The ESAC error occurs if the controller is not system controller.

DeviceDevice FunctionsFunctions

The device functions send configuration information to a specific instrument or device.

loc—Go to local

off—Take device offline

pct—Pass control

ppc—Parallel poll configure

loc—Go to local

 syntax                               loc address

loc temporarily moves devices from a remote program mode to a local mode.

address is the GPIB address of the device. This argument indicates both primary and
secondary addresses if you use the form primary+secondary, where primary and
secondary are the decimal values of the primary and secondary addresses. For

                                                    © National Instruments 2863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2864 ordinal=2864 -->
## Functions

Functions

      example, if primary is 2 and secondary is 3, address is 2+3.

       loc sends the GTL (Go To Local) message to the GPIB device.

      off—Take device offline

         syntax                                   off address

        off takes the device at the specified GPIB address offline. This is only needed when
       sharing a device with another application which is using the NI-488 GPIB Library.

       address is the GPIB address of the device. This argument indicates both primary and
      secondary addresses if you use the form primary+secondary, where primary and
      secondary are the decimal values of the primary and secondary addresses. For
      example, if primary is 2 and secondary is 3, address is 2+3.

     pct—Pass control

         syntax                             pct address

       pct passes Controller-In-Charge (CIC) authority to the device at the specified address.
      The GPIB Controller becomes idle automatically. The function assumes that the device
       to which pct passes control has Controller capability.

       address is the GPIB address of the device. This argument indicates both primary and
      secondary addresses if you use the form primary+secondary, where primary and
      secondary are the decimal values of the primary and secondary addresses. For
      example, if primary is 2 and secondary is 3, address is 2+3.

       pct sends the following command sequence:

         1. Talk address of the device
         2. Secondary address of the device, if applicable
         3. Take Control (TCT)


2864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2865 ordinal=2865 -->
## Functions

Functions

ppc—Parallel poll configure

 syntax                   ppc byte address

ppc enables the instrument to respond to parallel polls.

byte is 0 or a valid parallel poll enable (PPE) command. If byte is 0, the parallel poll
disable (PPD) byte 0x70 is sent to disable the device from responding to a parallel poll.
Each of the 16 PPE messages selects a GPIB data line (DIO1 through DIO8) and sense (1
or 0) that the device must use when it responds to the Identify (IDY) message during a
parallel poll. The device compares the ist sense and drives the indicated DIO line TRUE
or FALSE.

address is the GPIB address of the device. This argument indicates both primary and
secondary addresses if you use the form primary+secondary, where primary and
secondary are the decimal values of the primary and secondary addresses. For
example, if primary is 2 and secondary is 3, address is 2+3.

GPIBGPIB FunctionFunction DefaultsDefaults

When using GPIB functions, the default primary address of the GPIB controller is 0,
with no secondary address. It is designated as System Controller. The default timeout
value for GPIB functions is 10 seconds. If you want to set the primary address or
change the default timeout value, use the configuration utility included with the GPIB
controller.

You also can use the GPIB Initialization and SetTimeOut functions to set the primary
address and to change the default timeout value at run time, but these functions affect
the interface only when you use it with LabVIEW. Refer to the documentation supplied
with the hardware interface for more information.

GPIBGPIB MultilineMultiline InterfaceInterface MessagesMessages

Multiline Interface Messages are commands that IEEE 488 defines. Multiline interface
messages manage GPIB by performing tasks such as initializing the bus, addressing
and unaddressing devices, and setting device modes for local or remote programming.
These multiline interface messages are sent and received with ATN TRUE.

                                                    © National Instruments 2865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2866 ordinal=2866 -->
## Functions

Functions

      The GPIB Multiline Interface Messages can return the following message codes.


       Mnemonic                     Definition

       DCL                          Device Clear

       GET                       Group Execute Trigger

       GTL                    Go To Local

       LLO                           Local Lockout

       MLA                    My Listen Address

       MSA                    My Secondary Address

       MTA                    My Talk Address

       PPC                              Parallel Poll Configure

       PPD                              Parallel Poll Disable

       PPE                              Parallel Poll Enable

       PPU                              Parallel Poll Unconfigure

       SDC                          Selected Device Clear

       SPD                              Serial Poll Disable

       SPE                              Serial Poll Enable

       TCT                         Take Control

       UNL                           Unlisten

      UNT                         Untalk

       Refer to the ANSI/IEEE Standard 488.1-1987, IEEE Standard Digital Interface for
      Programmable Instrumentation, for more information about these messages.

       Refer to ASCII Codes for a list of ASCII codes.

     ConfiguringConfiguring SerialSerial andand ParallelParallel PortsPorts withwith VISAVISA

       NI-VISA automatically detects ports. You can view the list of ports with a VISA resource
     name control on the front panel or with the VISA Find Resource function. The
     maximum number of serial ports that NI-VISA supports on any platform is 256. The

2866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2867 ordinal=2867 -->
## Functions

Functions

default numbering of serial ports is system dependent.

(Windows) NI-VISA supports interaction with parallel ports as well as with serial ports
on your computer. You can use the VISA properties to communicate with parallel ports
in the same way you communicate with serial ports.

      Note You may receive unexpected errors while attempting to write to a
         parallel port if you leave floating pins. Unlike the serial ports, parallel ports
       have pins that, if left floating, cause the port driver to assume that the
       attached device is busy (pin 11) or out of paper (pin 12). Ground pins 11 and
       12 on the port to ensure that you can write successfully to the port.

VISAVISA ResourceResource NameName ControlControl

Use the VISA resource name control to specify the resource to which a VISA session
will be opened and to maintain the session and class. A VISA session is a unique logical
identifier used by VISA to communicate with a resource. The VISA session is
maintained by the VISA resource name control and is not seen by the user. VISA
resource name out is a copy of the resource name that is passed out of the VISA
functions. By passing the resource name in and out of functions and VIs, you can
simplify dataflow programming by chaining functions and VIs together. This is similar
to the file refnum outputs used by the File I/O functions.

The following table shows the syntax for the VISA resource name string. Optional
parameters are shown in square brackets ([ ]).


 Interface      Syntax                                                     Classes

                                                                                              Instr;

                                                                             VXI/GPIB-VXI MBD
 VXI INSTR       VXI[board]::VXI logical address[::INSTR]                             Instr;

                                                                         VXI/GPIB-VXI/VME
                                                         RBD Instr

 VXI MEMACC   VXI[board]::MEMACC                                        VXI/GPIB-VXI/VME


                                                    © National Instruments 2867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2868 ordinal=2868 -->
## Functions

Functions


         Interface      Syntax                                                     Classes

                                                                MemAcc

         VXI                                                                         VXI/GPIB-VXI                          VXI[board][::VXI logical address]::BACKPLANE       BACKPLANE                                                          Backplane

         VXI SERVANT   VXI[board]::SERVANT                                          VXI Servant

                                                                                     VXI/GPIB-VXI MBD
                                                                                                        Instr;         GPIB-VXI                         GPIB-VXI[board]::VXI logical address[::INSTR]
        INSTR                                                                                 VXI/GPIB-VXI/VME
                                                               RBD Instr

         GPIB-VXI                                                                 VXI/GPIB-VXI/VME                       GPIB-VXI[board]::MEMACC      MEMACC                                                   MemAcc

         GPIB-VXI                                                                    VXI/GPIB-VXI                         GPIB-VXI[board][::VXI logical address]::BACKPLANE       BACKPLANE                                                          Backplane

                        GPIB[board]::primary address[::GPIB secondary        GPIB INSTR                                                         GPIB Instr                         address][::INSTR]

                                                                          GPIB        GPIB INTFC    GPIB[board]::INTFC                                                                                     BoardInterface

        GPIB                      GPIB[board]::SERVANT                                   N/A
       SERVANT

         PXI INSTR       PXI[bus]::device[::function][::INSTR]                           PXI Instr

         PXI INSTR       PXI[interface]::[bus-]device[.function][::INSTR]                 PXI Instr

         PXI MEMACC   PXI[interface]::MEMACC                                       PXI MemAcc

          Serial INSTR    ASRL[board][::INSTR]                                             Serial Instr

        TCPIP INSTR   TCPIP[board]::host address[::LAN device name][::INSTR]        TCP/IP Instr

        TCPIP
                        TCPIP[board]::host address::port::SOCKET                    TCP/IP Socket
       SOCKET

                       USB[board]::manufacturer ID::model code::serial
       USB INSTR                                                  USB Instr
                      number[::USB interface number][::INSTR]

                       USB[board]::manufacturer ID::model code::serial
       USB RAW                                                   USB Raw
                      number[::USB interface number]::RAW


2868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2869 ordinal=2869 -->
## Functions

Functions

The VXI keyword is used for VXI instruments through either embedded or MXIbus
controllers. The GPIB keyword is used to establish communication with a GPIB device.
The GPIB-VXI keyword is used for a GPIB-VXI controller. The ASRL keyword is used to
establish communication with an asynchronous serial (such as RS232) device.

The INSTR keyword specifies a VISA resource of the type INSTR.

The following table shows the default value for optional string segments.


 Optional String Segment                Default Value

 board                               0

 GPIB secondary address              None

 LAN device name                          inst0

 PXI function                         0

 USB interface number                   lowest numbered relevant interface

The following table shows examples of address strings.


 Address String                   Description

 VXI0::1::INSTR                 A VXI device at logical address 1 in VXI interface VXI0.

                            A VXI device at logical address 9 in a GPIB-VXI controlled
 GPIB-VXI::9::INSTR                                 system.

                            A GPIB device at primary address 1 and secondary address 0 in
 GPIB::1::0::INSTR
                              GPIB interface 0.

 ASRL1::INSTR                 A serial device attached to interface ASRL1.

 VXI::MEMACC                      Board-level register access to the VXI interface.

 GPIB-VXI1::MEMACC               Board-level register access to GPIB-VXI interface number 1.

 GPIB2::INTFC                       Interface or raw resource for GPIB interface 2.

                               Mainframe resource for chassis 1 on the default VXI system,
 VXI::1::BACKPLANE
                              which is interface 0.

 GPIB-VXI2::BACKPLANE          Mainframe resource for default chassis on GPIB-VXI interface 2.

 GPIB1::SERVANT                  Servant/device-side resource for GPIB interface 1.


                                                    © National Instruments 2869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2870 ordinal=2870 -->
## Functions

Functions


        Address String                   Description

        VXI0::SERVANT                    Servant/device-side resource for VXI interface 0.

         TCPIP0::1.2.3.4::999::SOCKET     Raw TCP/IP access to port 999 at the specified IP address.

                                   A TCP/IP device using VXI-11 located at the specified address.        TCPIP::dev.company.com::INSTR                                           This uses the default LAN Device Name of inst0.

         PXI::15::INSTR                     PXI device number 15 on bus 0.

         PXI0::2-12.1::INSTR                PXI bus number 2, device 12 with function 1.

        PXI0::MEMACC                    PXI MEMACC session.

                                    The resource on the specified remote system. The hostname
                                      can be represented as either an IP address (dot-notation) or         visa://hostname/resource                                      network machine name. This remote system need not be
                                                  explicitly configured on the client system.

                                   A USB Test & Measurement class device with manufacturer ID
                                         0x1234, model code 125, and serial number A22-5. This uses the         USB::0x1234::125::A22-5::INSTR
                                                          first available USBTMC interface of the device. This is usually
                                  number 0.

                                   A raw USB nonclass device with manufacturer ID 0x5678, model
         USB::0x5678::0x33::SN999::1::RAW code 0x33, and serial number SN999. This uses the device
                                              interface number 1.

      By default, the VISA resource name control is set to the Instr class, which also
      corresponds to the class of the session to be opened. You can change the class type by
        right-clicking the control in edit mode and selecting a different class from the shortcut
      menu.

       VISA functions vary in the class of VISA resource name that can be wired to them. The
        valid classes for each function are listed in the NI-VISA Help. For example, the functions
      on the Register Access and Low Level Register Access palettes do not accept VISA
       sessions of class GPIB Instr or Serial Instr.

           If you wire the VISA resource name control to a function that does not accept the class
       of the session, or if you wire two resource names of differing classes together, the
       block diagram will not run and a Class Conflict error is reported.


2870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2871 ordinal=2871 -->
## Functions

Functions

      Note You can wire resource names set to the Event classes only to the VISA
       Close function and a Property Node.

If you wire the VISA resource name control to a function that does not accept the class
of the session, or if you wire two resource names of differing classes together, the
block diagram will not run and a Class Conflict error is reported.

      Note VISA name controls and constants are available on all platforms.
       However, if you try to run a VI with a name control that contains a resource
         string for a device that your platform does not support, you will receive an
         error.

VISAVISA EventsEvents

The VIs and functions on the Event Handling palette handle VISA events. To handle
VISA events, you must enable event queuing with the VISA Enable Event function.
Queues work per session and per event type, so you must enable queuing on every
session for which you want to handle events.

Use the VISA Wait on Event function to retrieve events from a queue. If an event of the
specified type already has occurred, calling VISA Wait on Event returns that event
immediately, regardless of the value you set for the timeout parameter.

You also can use VISA Wait on Event to wait for events that currently do not exist in the
queue. Execution stops until an event of the specified type arrives or until the VISA
Wait on Event function times out. Set a reasonable timeout value to wait for events
that currently do not exist in the queue.

      Tip To check if the queue contains any events of the type you specified, set
       timeout on the VISA Wait on Event function to 0 (immediate).

When the VISA Wait on Event function returns an event, the event no longer exists in
the queue for the session on which you invoked the wait operation. However, if event
queuing is enabled on any other VISA session, the event remains in the queue for that
session until it is retrieved.

                                                    © National Instruments 2871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2872 ordinal=2872 -->
## Functions

Functions

      Use the VISA Disable Event function to disable event queuing on a specific VISA
       session. When you call this function, no additional events are added to the queue for
       the session. However, the queue retains any events that already existed in the queue.
      You can either retrieve or discard these events. To retrieve the events, use the VISA
       Wait on Event function. To discard the events, use the VISA Discard Events function.

      The default length of VISA event queues is 50. If the queue is full and a new event
        arrives, the new event is discarded. Event queues in VISA do not grow dynamically, but
      you can use the General Settings:Maximum Queue Length property to change the size
       of an event queue programmatically. If you change the queue length on a given
       session, you must do so before VISA Enable Event is called for the first time.

      The following table lists the events you can handle with these VIs and functions. This
       table includes a description of each event along with its supported resource classes,
      such as GPIB, PXI etc.

           Note The serial events are valid only on Windows and platforms on which
              National Instruments supports its ENET-Serial products.


        Event                                                                   Resource
                   Description      Name                                                                         Classes

                      Notifies the application that a service request was received from the     GPIB INSTR,
                   device or interface associated with the given session.                 GPIB INTFC,
                                                                                       GPIB-VXI         Service
                                                                                     INSTR, TCPIP
        Request         Note When you receive this event on an instrument session,                                                                                     INSTR, USB
                         you must call VISA Read STB to guarantee delivery of future                                                                                     INSTR, VXI
                              service request events on the given session.                                                                              INSTR

                                                                             GPIB INTFC,
                      Notifies the application that a trigger interrupt was received from the
                                                                                            VXI INSTR, VXI
         Trigger    device. This may be either a hardware or software trigger, depending on
                                                                          BACKPLANE,
                   the interface and the current session settings.
                                                                                            VXI SERVANT

                      Notifies the application that a device clear message was sent to the      GPIB INTFC,
         Clear
                      local controller.                                                        VXI SERVANT

                      Notifies the application that a VXIbus signal or VXIbus interrupt was
         VXI Signal                                                                         VXI INSTR
                    received from the device associated with the given session.

2872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2873 ordinal=2873 -->
## Functions

Functions


Event                                                                   Resource           Description
Name                                                                         Classes

VXI/VME   Notifies the application that a VXIbus interrupt was received from the                                                                                  VXI INSTRInterrupt  device associated with the given session.

VXI/VME                                                                           VXI            Notifies the application that the VXI/VME SYSFAIL* line was asserted.
Sysfail                                                          BACKPLANE

                                                                                  VXIVXI/VME            Notifies the application that the VXI/VME SYSRESET* line was asserted.   BACKPLANE,Sysreset                                                                                  VXI SERVANT

            Notifies the application that the GPIB controller has gained or lost CICGPIB CIC                                                               GPIB INTFC            (controller-in-charge) status.

GPIB Talk  Notifies the application that the GPIB controller was addressed to talk.   GPIB INTFC

GPIB       Notifies the application that the GPIB controller has been addressed to                                                                      GPIB INTFCListen      listen.

PXI            Notifies the application that a PXI interrupt occurred.                    PXI INSTRInterrupt

USB                                                          USB INSTR,            Notifies the application that a USB interrupt has occurred.Interrupt                                                      USB RAW

Serial            Notifies the application that a break signal was received.                  Serial INSTRBreak

            Notifies the application that the termination character was received.
         The actual termination character is specified by setting the Message
Serial         Based Settings:Termination Character Enable property prior to enabling  Serial INSTRTermChar            this event. For this event, the setting of the Message Based
           Settings:Termination Character Enable property is ignored.

            Notifies the application that the Clear To Send (CTS) line changed state.
Serial
                 If the CTS line changes state quickly several times in succession, not all    Serial INSTR
CTS
            line state changes necessarily result in event notifications.

            Notifies the applications that the Data Set Ready (DSR) line changed
Serial
             state. If the DSR line changes state quickly several times in succession,    Serial INSTR
DSR
          not all line state changes necessarily result in event notifications.

            Notifies the application that the Data Carrier Detect (DCD) line changed
Serial
             state. If the DCD line changes state quickly several times in succession,    Serial INSTR
DCD
          not all line state changes necessarily result in event notifications.

Serial RI   Notifies the application that the Ring Indicator (RI) input signal was       Serial INSTR


                                                    © National Instruments 2873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2874 ordinal=2874 -->
## Functions

Functions


        Event                                                                   Resource                   Description
      Name                                                                         Classes

                     asserted.

                      Notifies the application that at least one data byte has been received.
                 Each data character does not necessarily result in an event notification.
          Serial      In other words, if multiple data bytes arrive at once, you may get only                                                                                                   Serial INSTR         Character one event. After receiving this event, use the Serial Settings:Number of
                   Bytes at Serial Port property to query the serial port for the number of
                   bytes available.

      SerialSerial

      Use the Serial VIs and functions to access the VISA VIs and functions that communicate
       with devices connected to a serial port. Additional functions are also available on the
       VISA palette.

      The VIs and functions on this palette can return serial error codes.


         Palette
                      Description        Object

        VISA           Initializes the serial port specified by VISA resource name to the specified settings.
         Configure    Wire data to the VISA resource name input to determine the polymorphic instance to
          Serial Port   use or manually select the instance.

        VISA Write    Writes the data from write buffer to the device or interface specified by VISA
         Function     resource name.

        VISA Read    Reads the specified number of bytes from the device or interface specified by VISA
         Function     resource name and returns the data in read buffer.

        VISA Close
                      Closes a device session or event object specified by VISA resource name.
         Function

        VISA Bytes
                     Returns the number of bytes in the input buffer of the specified serial port.
         at Serial

2874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2875 ordinal=2875 -->
## Functions

Functions


 Palette              Description
 Object

 Port

 VISA Serial   Sends a break on the specified output port. Wire data to the VISA resource name
 Break        input to determine the polymorphic instance to use or manually select the instance.

 VISA Set I/O
              Sets the size of the I/O buffer. Run the VISA Configure Serial Port VI first if you are Buffer Size               setting the size of a serial port buffer. Function

 VISA Flush
 I/O Buffer    Flushes the I/O buffer specified by mask.
 Function

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Serial.lvproj

VisionVision andand MotionMotion

Refer to the NI Vision, NI Vision Acquisition Software, NI-Motion, and NI SoftMotion
help files, which you can access from the Help menu, for more information about
those VIs. If NI Vision Acquisition Software, NI-Motion, and NI SoftMotion are not
installed, you cannot access the help files. Install these additional packages from the
media included with LabVIEW.


MathematicsMathematics

Use the Mathematics VIs to perform many different kinds of mathematical analysis.
You also can interface real-world measurements to the mathematical algorithms in
order to obtain practical solutions.


                                                    © National Instruments 2875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2876 ordinal=2876 -->
## Functions

Functions

      The Mathematics VIs support only explicit multiplication syntax. For example, to
       multiply the variable xby 5, enter 5*xrather than 5x.

           Note Many Mathematics VIs are available only in the LabVIEW Full and
               Professional Development Systems. If you have the LabVIEW Base
             Development System, you do not have the full set of the Mathematics VIs
              described in this help file. A subset of the Mathematics VIs is available in the
            LabVIEW Base Development System.


         Palette Object  Description

                     Use the Numeric VIs and functions to create and perform arithmetic and complex
                      mathematical operations on numbers and to convert numbers from one data type
        Numeric                         to another. Use the VIs and functions on the Elementary and Special Functions and
                           VIs palette to perform trigonometric and logarithmic functions.


        Elementary &
                     Use the Elementary & Special Functions and VIs to evaluate common mathematical         Special                          functions.         Functions


         Linear Algebra Use the Linear Algebra VIs to perform matrix-related computations and analysis.


          Fitting        Use the Fitting VIs to perform curve fitting analysis or regression.


         Interpolation
                     Use the Interpolation & Extrapolation VIs to perform 1D and 2D interpolation,
      &
                       piecewise interpolation, polynomial interpolation, and Fourier interpolation.
         Extrapolation


         Integration &   Use the Integration & Differentiation VIs to perform integration and differentiation
          Differentiation  procedures.


2876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2877 ordinal=2877 -->
## Functions

Functions


 Palette Object  Description

 Probability &   Use the Probability and Statistics VIs to perform probability, descriptive statistics,
 Statistics       analysis of variance, and interpolation functions.


              Use the Optimization VIs to determine local minima and maxima of real 1D or
 Optimization              n-dimension functions.


 Differential              Use the Differential Equations VIs to solve differential equations.
 Equations


 Geometry     Use the Geometry VIs to manipulate coordinates and angles.


 Polynomial    Use the Polynomial VIs to perform calculations and evaluations with polynomials.


 Scripts &      Use the Scripts & Formulas VIs to evaluate mathematical formulae and expressions
 Formulas     on the block diagram.

NumericNumeric

Use the Numeric VIs and functions to create and perform arithmetic and complex
mathematical operations on numbers and to convert numbers from one data type to
another. Use the VIs and functions on the Elementary and Special Functions and VIs
palette to perform trigonometric and logarithmic functions.

You also can access the following constants from this palette:

  • positive infinity
  • negative infinity
  • machine epsilon
  • not a number


                                                    © National Instruments 2877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2878 ordinal=2878 -->
## Functions

Functions


         Palette                       Description
        Object

       Add                   Computes the sum of the inputs.         Function

         Subtract                   Computes the difference of the inputs.
         Function

         Multiply                      Returns the product of the inputs.         Function

         Divide                   Computes the quotient of the inputs.
         Function

        Quotient &                   Computes the integer quotient and the remainder of the inputs. This function        Remainder                     rounds floor(x/y) to the nearest integer towards -inf.
         Function

        Conversion   Use the Conversion VIs and functions to convert data types.

        Increment                    Adds 1 to the input value.         Function

        Decrement                       Subtracts 1 from the input value.         Function

       Add Array
        Elements     Returns the sum of all the elements in numeric array.
         Function

         Multiply
                      Returns the product of all the elements in numeric array. If numeric array is an
         Array
                   empty array, the function returns a value of 1. If numeric array contains only one
        Elements
                      element, the function returns that element.
         Function

                     Performs arithmetic on one or more numeric, array, cluster, or Boolean inputs. To
                         select the operation (Add, Multiply, AND, OR, or XOR), right-click the function and
       Compound
                         select Change Mode from the shortcut menu. When you select this function from the
         Arithmetic
                    Numeric palette, the default mode is Add. When you select this function from the
                     Boolean palette, the default mode is OR.


2878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2879 ordinal=2879 -->
## Functions

Functions


Palette              Description
Object

Data            Use the Data Manipulation functions to modify the data types used in LabVIEW.Manipulation

Absolute
Value         Returns the absolute value of the input.
Function

Round To            Rounds the input to the nearest integer. If the value of the input is midway betweenNearest            two integers, the function returns the nearest even integer.Function

Round
Toward              Truncates the input to the next lowest integer.-Infinity
Function

Round
Toward            Rounds the input to the next highest integer.+Infinity
Function

Scale By
Power Of 2    Multiplies x by 2 raised to the power of n.
Function

            Use the Complex functions to create complex numbers from two values given in
Complex      rectangular or polar and to break a complex number into its rectangular or polar
            components.

Square Root
            Computes the square root of the input value.
Function

Square
            Computes the square of the input value.
Function

Negate
             Negates the input value.
Function

Reciprocal
              Divides 1 by the input value.
Function

Sign
             Returns the sign of number.
Function

                                                    © National Instruments 2879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2880 ordinal=2880 -->
## Functions

Functions


         Palette                       Description
        Object

         Scaling      Use the Scaling VIs to convert voltage readings to other temperature or strain units.

        Numeric     Use the numeric constant to pass a numeric value to the block diagram. Set this
        Constant     value by clicking inside the constant with the Operating tool and typing a value.

      Enum       Use the enumerated constant to create a list of string labels with corresponding
        Constant      integer values you can select on the block diagram.

        Ring        Use the ring constant to create a list of value pairs you can select on the block
        Constant     diagram. Each value pair consists of a numeric value and corresponding string label.

       Random
                     Produces a double-precision, floating-point number between 0 and 1. The number
       Number (0-1)                      generated is greater than or equal to 0, but less than 1. The distribution is uniform.         Function

       Random      Generates a random value from a specified range. Wire data to the upper bound or
       Number      lower bound input to determine the polymorphic instance to use or manually select
         (Range)       the instance.


                    Use the Fixed-Point functions to manipulate the overflow status of a fixed-point         Fixed-Point                    number.


                    Use the DBL numeric constant to pass a double-precision, floating-point numeric       DBL Numeric                       value to the block diagram. Set this value by clicking inside the constant with the        Constant
                      Operating tool and typing a value.

          Positive                      Returns the value Inf (infinity).           Infinity

         Negative                      Returns the value -Inf (negative infinity).           Infinity

                      Represents the round-off error for a floating-point number with a given precision.
        Machine
                    Use the machine epsilon constant to compare whether two floating-point numbers
         Epsilon
                       are equivalent.

        Not A                      Returns the value NaN (not a number).       Number

2880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2881 ordinal=2881 -->
## Functions

Functions


 Palette               Description
 Object

 Constant

 Math &
 Scientific     Use the Math & Scientific Constants to create LabVIEW applications.
 Constants

 Range Limits              Returns the maximum and minimum values of the input data type. for Type

             Use the Expression Node to calculate expressions that contain a single variable. The
               following built-in functions are allowed in formulas: abs, acos, acosh, asin, asinh, Expression                atan, atanh, ceil, cos, cosh, cot, csc, exp, expm1, floor, getexp, getman, int, intrz, ln,
 Node                lnp1, log, log2, max, min, mod, rand, rem, sec, sign, sin, sinc, sinh, sizeOfDim, sqrt,
                tan, tanh.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

ElementaryElementary && SpecialSpecial FunctionsFunctions

Use the Elementary & Special Functions and VIs to evaluate common mathematical
functions.

The VIs on this palette can return mathematics error codes.


 Palette Object     Description

 Trigonometric    Use this class of elementary functions to compute trigonometric functions and
 Functions          their inverses.


                                                    © National Instruments 2881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2882 ordinal=2882 -->
## Functions

Functions


         Palette Object     Description

         Exponential      Use this class of elementary functions to compute exponential and logarithmic
         Functions          functions.


         Hyperbolic       Use this class of elementary functions to compute hyperbolic functions and
         Functions          their inverses.


                       Use this class of elementary functions to compute common periodic waves at         Gating Functions
                           given points.


                       Use this class of elementary functions to compute discrete math functions for         Discrete Math                           areas such as combinatorics and number theory.


         Bessel Functions  Use this class of special functions to compute Bessel-related functions.


      Gamma                       Use this class of special functions to compute Gamma-related functions.         Functions


        Hypergeometric   Use this class of special functions to compute functions based on the
         Functions         hypergeometric differential equation.


                       Use this class of special functions to compute complete and incomplete elliptic
           Elliptic Integrals
                               integrals.


         Exponential
                       Use this class of special functions to compute exponential integrals.
          Integrals


         Error Functions   Use this class of special functions to compute Error-related functions.


2882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2883 ordinal=2883 -->
## Functions

Functions


 Palette Object     Description

 Elliptic &                Use this class of special functions to compute specific forms of elliptic integrals
 Parabolic                   or Weber functions. Functions

TrigonometricTrigonometric FunctionsFunctions

Use this class of elementary functions to compute trigonometric functions and their
inverses.

The VIs on this palette can return mathematics error codes.


 Palette Object         Description

 Sine Function        Computes the sine of x, where x is in radians.

 Cosine Function      Computes the cosine of x, where x is in radians.

 Tangent Function     Computes the tangent of x, where x is in radians.

                   Computes the secant of x, where x is in radians. Secant is the reciprocal of Secant Function                         cosine.

                   Computes the cosecant of x, where x is in radians. Cosecant is the Cosecant Function                         reciprocal of sine.

                   Computes the cotangent of x, where x is in radians. Cotangent is the
 Cotangent Function
                         reciprocal of tangent.

 Inverse Sine Function  Computes the arcsine of x.

 Inverse Cosine
                   Computes the arccosine of x.
 Function

 Inverse Tangent
                   Computes the arctangent of x.
 Function

 Inverse Secant
                   Computes the inverse secant of x.
 Function

 Inverse Cosecant      Computes the inverse cosecant of x.

                                                    © National Instruments 2883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2884 ordinal=2884 -->
## Functions

Functions


         Palette Object         Description

         Function

         Inverse Cotangent                          Computes the inverse cotangent of x.         Function

         Sine & Cosine        Computes both the sine and cosine of x, where x is in radians. Use this
         Function               function only when you need both results.

         Sinc Function        Computes the sine of x divided by x, where x is in radians.

         Inverse Tangent (2                          Computes the arctangent of y/x.         Input) Function

      SineSine FunctionFunction

      Computes the sine of x, where x is in radians.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       sin(x) —

              sin(x) is of the same numeric representation as x.

         When x is of the form x = a + bi, that is, when x is complex, the following equation defines sin(x):
              sin(x) = sin(a) * cosh(b) + i(cos(a) * sinh(b))

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special

2884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2885 ordinal=2885 -->
## Functions

Functions

   Functions\Trigonometric Functions\Sine.vi

CosineCosine FunctionFunction

Computes the cosine of x, where x is in radians.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       cos(x) —

    cos(x) is of the same numeric representation as x.

   When x is of the form x = a + bi, that is, when x is complex, the following equation defines cos(x):

    cos(x) = cos(a) * cosh(b) + i(-sin(a) * sinh(b))


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

TangentTangent FunctionFunction

Computes the tangent of x, where x is in radians.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 2885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2886 ordinal=2886 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       tan(x) —

             tan(x) is of the same numeric representation as x.

         When x is of the form x = a + bi, that is, when x is complex, the following equation defines tan(x):


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

      SecantSecant FunctionFunction

      Computes the secant of x, where x is in radians. Secant is the reciprocal of cosine.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       1/cos(x) —


2886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2887 ordinal=2887 -->
## Functions

Functions


    1/cos(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

CosecantCosecant FunctionFunction

Computes the cosecant of x, where x is in radians. Cosecant is the reciprocal of sine.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       1/sin(x) —

     1/sin(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi


                                                    © National Instruments 2887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2888 ordinal=2888 -->
## Functions

Functions

      CotangentCotangent FunctionFunction

      Computes the cotangent of x, where x is in radians. Cotangent is the reciprocal of
       tangent.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       1/tan(x) —

             1/tan(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

       InverseInverse SineSine FunctionFunction

      Computes the arcsine of x.

           If x is not complex and is less than –1 or greater than 1, the result is NaN. The
       connector pane displays the default data types for this polymorphic function.


2888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2889 ordinal=2889 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       arcsin(x) —

     arcsin(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is,
   when x is complex, the following equation defines arcsin(x):


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

InverseInverse CosineCosine FunctionFunction

Computes the arccosine of x.

If x is not complex and is less than –1 or greater than 1, the result is NaN. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       arccos(x) —

    arccos(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is,


                                                    © National Instruments 2889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2890 ordinal=2890 -->
## Functions

Functions


          when x is complex, the following equation defines arccos(x):


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

       InverseInverse TangentTangent FunctionFunction

      Computes the arctangent of x.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       arctan(x) —

             arctan(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is,
          when x is complex, the following equation defines arctan(x):


             arctan(x) ranges from -pi/2 to pi/2.


2890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2891 ordinal=2891 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

InverseInverse SecantSecant FunctionFunction

Computes the inverse secant of x.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       arcsec(x) —

    arcsec(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

InverseInverse CosecantCosecant FunctionFunction

Computes the inverse cosecant of x.

The connector pane displays the default data types for this polymorphic function.

                                                    © National Instruments 2891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2892 ordinal=2892 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       arccsc(x) —

             arccsc(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

       InverseInverse CotangentCotangent FunctionFunction

      Computes the inverse cotangent of x.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       arccot(x) —

             arccot(x) is of the same numeric representation as x.


2892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2893 ordinal=2893 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

SineSine && CosineCosine FunctionFunction

Computes both the sine and cosine of x, where x is in radians. Use this function only
when you need both results.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       sin(x) —

     sin(x) is of the same numeric representation as x.

   When x is of the form x = a + bi, that is, when x is complex, the following equation defines sin(x):
     sin(x) = sin(a) * cosh(b) + i(cos(a) * sinh(b))
   •       cos(x) —

    cos(x) is of the same numeric representation as x.

   When x is of the form x = a + bi, that is, when x is complex, the following equation defines cos(x):
    cos(x) = cos(a) * cosh(b) + i(-sin(a) * sinh(b))

SincSinc FunctionFunction

Computes the sine of x divided by x, where x is in radians.


                                                    © National Instruments 2893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2894 ordinal=2894 -->
## Functions

Functions

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       sin(x)/x —

              sin(x)/x is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

       InverseInverse TangentTangent (2(2 Input)Input) FunctionFunction

      Computes the arctangent of y/x.

       This function can compute the arctangent for angles in any of the four quadrants of the
        x-y plane, whereas the Inverse Tangent function computes the arctangent in only two
       quadrants. The connector pane displays the default data types for this polymorphic
       function.


      Inputs/Outputs

               •      y —


2894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2895 ordinal=2895 -->
## Functions

Functions


    y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       atan2(y,x) —

    atan2(y,x) is the arctangent of y and x, in radians. atan2(y,x) falls in the range [-pi, pi]. When x or
    y are complex, the following equation defines atan2(y,x):


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

ExponentialExponential FunctionsFunctions

Use this class of elementary functions to compute exponential and logarithmic
functions.

The VIs on this palette can return mathematics error codes.


 Palette Object     Description

 Exponential
                Computes the value of e raised to the x power, or the exponential of x.
 Function

 Exponential (Arg)
                Computes 1 less than the value of e raised to the x power.
 -1 Function


                                                    © National Instruments 2895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2896 ordinal=2896 -->
## Functions

Functions


         Palette Object     Description

       Power Of 10                       Computes 10 raised to the x power.         Function

       Power Of 2                       Computes 2 raised to the x power.         Function

       Power Of X                       Computes x raised to the y power.         Function

          Y-th Root of X      Returns the yth root of the input value x. If x is not complex, x must be greater
         Function          than or equal to zero unless y is an integer. Otherwise, the result is NaN.

         Natural Logarithm                       Computes the base e natural logarithm of x.         Function

         Natural Logarithm                       Computes the natural logarithm of (x + 1).
         (Arg +1) Function

        Logarithm Base                       Computes the base 10 logarithm of x.
        10 Function

        Logarithm Base 2                       Computes the base 2 logarithm of x.
         Function

        Logarithm Base X
                       Computes the base x logarithm of y.         Function

      ExponentialExponential FunctionFunction

      Computes the value of e raised to the x power, or the exponential of x.

           Note For very small values of x, the Exponential (Arg) -1 function is more
              accurate than using this function then subtracting 1 from the output.

      The connector pane displays the default data types for this polymorphic function.


2896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2897 ordinal=2897 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      exp(x) —

    exp(x) is of the same numeric representation as x. The following equation defines the
    exponential exp(x):

    exp(a+bi) = exp(a)(cos(b)+i sin(b))

   when x is of the form x = a + bi, that is, when x is complex.


If x is a matrix, this function computes the exponential of x. When you wire matrix data
as an input to this function, a VI that includes subVIs that work with the matrix data
type replaces the function. The resulting VI has the same icon but contains a matrix-
specific algorithm. The node remains a VI if you disconnect the matrix from the
input(s). Wire other data types as inputs to restore the original function. If you wire a
data type to a function and that data type causes a basic math operation to fail, the
function returns an empty matrix or NaN.

Refer to the Matrix Exp VI for more information.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Exponential Functions\Exponential.vi

ExponentialExponential (Arg)(Arg) -1-1 FunctionFunction

Computes 1 less than the value of e raised to the x power.

When x is very small, this function is more accurate than using the Exponential
function then subtracting 1 from the output. The connector pane displays the default
data types for this polymorphic function.


                                                    © National Instruments 2897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2898 ordinal=2898 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      exp(x) -1 —

             exp(x)-1 is of the same numeric representation as x.

         When x is of the form x = a + bi, that is, when x is complex, the following equation defines
             exp(x)-1:exp(x)-1 = (exp(a) * (cos(b)+i sin(b))) – 1

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Exponential Functions\Exponential.vi

     PowerPower OfOf 1010 FunctionFunction

      Computes 10 raised to the x power.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      10^x —


2898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2899 ordinal=2899 -->
## Functions

Functions


    10^x is of the same numeric representation as x.

   When x is of the form x = a + bi, that is, when x is complex, the following equation defines
    10^x:10^x = 10^a * 10^(bi) = 10^a * (cos(b * ln(10)) + i sin (b * ln(10)))

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Exponential Functions\Exponential.vi

PowerPower OfOf 22 FunctionFunction

Computes 2 raised to the x power.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      2^x —

    2^x is of the same numeric representation as x.

   When x is of the form x = a + bi, that is, when x is complex, the following equation defines 2^x:
    2^x = 2^a * 2^(bi) = 2^a * (cos(b * ln(2)) + i sin(b * ln(2)))

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special

                                                    © National Instruments 2899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2900 ordinal=2900 -->
## Functions

Functions

        Functions\Exponential Functions\Exponential.vi

     PowerPower OfOf XX FunctionFunction

      Computes x raised to the y power.

           If x is not complex, it must be greater than zero unless y is an integer value. Otherwise,
       the result is NaN. If y is 0, x^y is 1 for all values of x, including 0. The connector pane
       displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      y —

           y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      x^y —

           x^y is x to the power of y.

         When x and y are complex, the following equation defines x^y: x^y = exp(y * ln(x)) Refer to the
            Exponential function and the Natural Logarithm function for more information.

     When you wire matrix data as an input to this function, a VI that includes subVIs that
      work with the matrix data type replaces the function. The resulting VI has the same
       icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
       the matrix from the input(s). Wire other data types as inputs to restore the original
       function. If you wire a data type to a function and that data type causes a basic math
       operation to fail, the function returns an empty matrix or NaN.

       Refer to the Matrix Power VI for more information.


2900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2901 ordinal=2901 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Exponential Functions\Exponential.vi

Y-thY-th RootRoot ofof XX FunctionFunction

Returns the yth root of the input value x. If x is not complex, x must be greater than or
equal to zero unless y is an integer. Otherwise, the result is NaN.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      y —

    y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       y-th root(x) —

    y-th root(x) returns the yth root of x.

   When x and y are complex, the following equation defines y-th root(x): y-th root(x) = exp((1/y) *
     ln(x)) Refer to the Natural Logarithm function and the Exponential function for more
    information.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special

                                                    © National Instruments 2901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2902 ordinal=2902 -->
## Functions

Functions

        Functions\Exponential Functions\Exponential.vi

      NaturalNatural LogarithmLogarithm FunctionFunction

      Computes the base e natural logarithm of x.

           If x is 0, ln(x) is –∞. If x is not complex and is less than 0, ln(x) is NaN.

           Note For very small values of x, the Natural Logarithm (Arg +1) function is
            more accurate than adding 1 to x then using this function.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       ln(x) —

              ln(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is, when x is
            complex, the following equation defines the natural logarithm ln(x): ln(x) = ln(|x|) + i arg(x)where
              arg(x) is the phase of x over the interval                       . In other words, LabVIEW uses the
             following equation:


     When you wire matrix data as an input to this function, a VI that includes subVIs that
      work with the matrix data type replaces the function. The resulting VI has the same
       icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
       the matrix from the input(s). Wire other data types as inputs to restore the original
       function. If you wire a data type to a function and that data type causes a basic math
       operation to fail, the function returns an empty matrix or NaN.

       Refer to the Matrix Logarithm VI for more information.


2902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2903 ordinal=2903 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Exponential Functions\Exponential.vi

NaturalNatural LogarithmLogarithm (Arg(Arg +1)+1) FunctionFunction

Computes the natural logarithm of (x + 1).

When x is near 0, this function is more accurate than adding 1 to x then using the
Natural Logarithm function. If x is equal to –1, the result is –∞. If x is not complex and is
less than –1, the result is NaN. The connector pane displays the default data types for
this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       ln(x+1) —

    ln(x+1) is of the same numeric representation as x. When x is of the form x = a + bi, that is, when
    x is complex, the following equation defines ln(x+1): ln(x+1) = ln(|x + 1|) + i arctan2(b, a + 1)


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Exponential Functions\Exponential.vi


                                                    © National Instruments 2903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2904 ordinal=2904 -->
## Functions

Functions

      LogarithmLogarithm BaseBase 1010 FunctionFunction

      Computes the base 10 logarithm of x.

           If x is 0, log(x) is negative infinity. If x is not complex and is less than 0, log(x) is NaN.
      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       log(x) —

             log(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is, when x
                is complex, the following equation defines log(x):


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Exponential Functions\Exponential.vi

      LogarithmLogarithm BaseBase 22 FunctionFunction

      Computes the base 2 logarithm of x.

           If x is 0, log2(x) is negative infinity. If x is not complex and is less than 0, log2(x) is NaN.
      The connector pane displays the default data types for this polymorphic function.


2904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2905 ordinal=2905 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       log2(x) —

    log2(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is, when
    x is complex, the following equation defines log2(x):


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Exponential Functions\Exponential.vi

LogarithmLogarithm BaseBase XX FunctionFunction

Computes the base x logarithm of y.

(x>0, y>0). If y is 0, the output is –∞. When x and y are both non-complex and x is less
than or equal to 0, or y is less than 0, the output is NaN. The connector pane displays
the default data types for this polymorphic function.


Inputs/Outputs

   •      y —

    y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.


                                                    © National Instruments 2905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2906 ordinal=2906 -->
## Functions

Functions

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       logx(y) —

             logx(y) is the logarithm of y to the base x. When x and y are complex, the following equation
             defines logx(y):

             logx(y) = ln(y)/ln(x)

             Refer to the Natural Logarithm function for more information.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Exponential Functions\Exponential.vi

     HyperbolicHyperbolic FunctionsFunctions

      Use this class of elementary functions to compute hyperbolic functions and their
       inverses.

      The VIs on this palette can return mathematics error codes.


         Palette Object                             Description

         Hyperbolic Sine Function                Computes the hyperbolic sine of x.

         Hyperbolic Cosine Function              Computes the hyperbolic cosine of x.

         Hyperbolic Tangent Function             Computes the hyperbolic tangent of x.

         Hyperbolic Secant Function              Computes the hyperbolic secant of x.

         Hyperbolic Cosecant Function            Computes the hyperbolic cosecant of x.


2906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2907 ordinal=2907 -->
## Functions

Functions


 Palette Object                             Description

 Hyperbolic Cotangent Function           Computes the hyperbolic cotangent of x.

 Inverse Hyperbolic Sine Function          Computes the inverse hyperbolic sine of x.

 Inverse Hyperbolic Cosine Function        Computes the inverse hyperbolic cosine of x.

 Inverse Hyperbolic Tangent Function       Computes the inverse hyperbolic tangent of x.

 Inverse Hyperbolic Secant Function        Computes the inverse hyperbolic secant of x.

 Inverse Hyperbolic Cosecant Function      Computes the inverse hyperbolic cosecant of x.

 Inverse Hyperbolic Cotangent Function     Computes the inverse hyperbolic cotangent of x.

HyperbolicHyperbolic SineSine FunctionFunction

Computes the hyperbolic sine of x.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       sinh(x) —

     sinh(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi


                                                    © National Instruments 2907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2908 ordinal=2908 -->
## Functions

Functions

      HyperbolicHyperbolic CosineCosine FunctionFunction

      Computes the hyperbolic cosine of x.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      cosh(x) —

            cosh(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

      HyperbolicHyperbolic TangentTangent FunctionFunction

      Computes the hyperbolic tangent of x.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

2908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2909 ordinal=2909 -->
## Functions

Functions


    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      tanh(x) —

    tanh(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

HyperbolicHyperbolic SecantSecant FunctionFunction

Computes the hyperbolic secant of x.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       sech(x) —

    sech(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special

                                                    © National Instruments 2909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2910 ordinal=2910 -->
## Functions

Functions

        Functions\Trigonometric Functions\Sine.vi

      HyperbolicHyperbolic CosecantCosecant FunctionFunction

      Computes the hyperbolic cosecant of x.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       csch(x) —

             csch(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

      HyperbolicHyperbolic CotangentCotangent FunctionFunction

      Computes the hyperbolic cotangent of x.

      The connector pane displays the default data types for this polymorphic function.


2910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2911 ordinal=2911 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       coth(x) —

    coth(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

InverseInverse HyperbolicHyperbolic SineSine FunctionFunction

Computes the inverse hyperbolic sine of x.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       argsinh(x) —

    argsinh(x) is of the same numeric representation as x.


                                                    © National Instruments 2911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2912 ordinal=2912 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

       InverseInverse HyperbolicHyperbolic CosineCosine FunctionFunction

      Computes the inverse hyperbolic cosine of x.

           If x is not complex and is less than 1, the result is NaN. The connector pane displays the
       default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      argcosh(x) —

            argcosh(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

       InverseInverse HyperbolicHyperbolic TangentTangent FunctionFunction

      Computes the inverse hyperbolic tangent of x.


2912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2913 ordinal=2913 -->
## Functions

Functions

If x is not complex and is less than –1 or greater than 1, the result is NaN. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      argtanh(x) —

    argtanh(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

InverseInverse HyperbolicHyperbolic SecantSecant FunctionFunction

Computes the inverse hyperbolic secant of x.

If x is not complex and is less than 0 or greater than 1, the result is NaN. The connector
pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.


                                                    © National Instruments 2913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2914 ordinal=2914 -->
## Functions

Functions

               •      argsech(x) —

            argsech(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi

       InverseInverse HyperbolicHyperbolic CosecantCosecant FunctionFunction

      Computes the inverse hyperbolic cosecant of x.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      argcsch(x) —

            argcsch(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi


2914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2915 ordinal=2915 -->
## Functions

Functions

InverseInverse HyperbolicHyperbolic CotangentCotangent FunctionFunction

Computes the inverse hyperbolic cotangent of x.

If x is not complex and is greater than –1 and less than 1, the result is NaN. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       argcoth(x) —

    argcoth(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

GatingGating FunctionsFunctions

Use this class of elementary functions to compute common periodic waves at given
points.

The VIs on this palette can return mathematics error codes.


                                                    © National Instruments 2915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2916 ordinal=2916 -->
## Functions

Functions


         Palette Object            Description

        Spike Function VI         Generates the spike function for any real number x.


        Square Function VI        Generates the square function for any real number x.


        Step Function VI          Generates the step function for any real number x.


      SpikeSpike FunctionFunction VIVI

       Generates the spike function for any real number x.


      Inputs/Outputs

               •      x —

           x is any real number.

               •       spike(x) —

             spike(x) is the value of spike(x) for the given value of x.


      The following equation defines the spike function:

       spike(x) = 1, if 0 ≤ x < 1 and 0 elsewhere.

           Note You can define more complex functions by varying and combining the
              Step Function, Spike Function, and Square Function VIs, respectively.

      The following illustration shows the graph for spike(x) – spike(–x) in the interval (–4.0,
         4.0).

2916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2917 ordinal=2917 -->
## Functions

Functions


SquareSquare FunctionFunction VIVI

Generates the square function for any real number x.


Inputs/Outputs

   •      x —

    x is any real number.

   •      square(x) —

    square(x) is the value of square(x) for the given value of x.


The following equation defines the square function.

square(x) = 1, if 2n≤ x < 2n+ 1 and 0 elsewhere,where nis an integer.

      Note You can define more complex functions by varying and combining the
       Step Function, Spike Function, and Square Function VIs, respectively.

The following illustration shows the graph for square(x) * square(x – 0.8) in the interval
(–4.0, 4.0).


                                                    © National Instruments 2917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2918 ordinal=2918 -->
## Functions

Functions


      StepStep FunctionFunction VIVI

       Generates the step function for any real number x.


      Inputs/Outputs

               •      x —

           x is any real number.

               •       step(x) —

             step(x) is the value of step(x) for the given value of x.


      The following equation defines the step function.

       step(x) = 0 if x < 0 and 1 elsewhere

           Note You can define more complex functions by varying and combining the
              Step Function, Spike Function, and Square Function VIs, respectively.

      The following illustration shows the graph for step(x) + spike(x) in the interval (–4.0,
        4.0)


2918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2919 ordinal=2919 -->
## Functions

Functions


DiscreteDiscrete MathMath

Use this class of elementary functions to compute discrete math functions for areas
such as combinatorics and number theory.

The VIs on this palette can return mathematics error codes.


 Palette Object      Description

 Gcd             Computes the greatest common divisor of the input values.


 Lcm             Computes the least common multiple of the input values.


 Factorial          Computes the factorial of n.


 Prime Factor       Computes the prime factorization of an integer.


 Check Prime       Checks whether a number is a prime number.


                                                    © National Instruments 2919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2920 ordinal=2920 -->
## Functions

Functions


         Palette Object      Description

                        Computes the number of ways to obtain an ordered subset of k elements from
        Permute                         a set of n elements.


        Binomial                             Calculates the binomial coefficient for nonnegative integer values of n and k.          Coefficient VI


        Continued Fraction  Evaluates the continued fraction of two sequences (a[0], a[1], …, a[n]) and
          VI                      (b[0], b[1], …, b[n]).


        (Riemann) Zeta
                        Computes the zeta function.         Function

     GcdGcd

      Computes the greatest common divisor of the input values.


      Inputs/Outputs

               •      x —

           x is an integer.

               •      y —

           y is an integer.

               •       gcd(x,y) —

             gcd(x,y) returns the greatest common divisor of x and y.


       gcd(x,y) is the largest divisor common to x and y.


2920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2921 ordinal=2921 -->
## Functions

Functions

To compute gcd(x,y), consider the prime factorizations of x and y:

x = Πipiai y = Πipibi

where pi are all the prime factors of x and y. If pi does not occur in a factorization, the
corresponding exponent is 0. gcd(x,y) then is given by:

                                          , bi)gcd(x,y) = Πipimin(ai

For example, the prime factorizations of 12 and 30 are given by:

12 = 2² × 31 × 50 30 = 21 × 31 × 51

so

gcd(12, 30) = 21 × 31 × 50 = 6
LcmLcm

Computes the least common multiple of the input values.


Inputs/Outputs

   •      x —

    x is an integer.

   •      y —

    y is an integer.

   •       lcm(x,y) —

    lcm(x,y) returns the least common multiple of x and y.


                                                    © National Instruments 2921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2922 ordinal=2922 -->
## Functions

Functions

       lcm(x,y) is the smallest integer mfor which there exist integers cand dsuch that

      x × c= y × d= m

      To compute lcm(x,y), consider the prime factorizations of x and y:

      x = Πipiai y = Πipibi

      where pi are all the prime factors of x and y. If pi does not occur in a factorization, the
       corresponding exponent is 0. lcm(x,y) then is given by:

                                   bi)       lcm(x,y) = Πipimax(ai,

       For example, the prime factorizations of 12 and 30 are given by:

      12 = 2² × 31 × 50 30 = 21 × 31 × 51

      so

       lcm(12,30) = 2² × 31 × 51 = 60
       FactorialFactorial

      Computes the factorial of n.


      Inputs/Outputs

               •     n —

          n is the input argument.

               •       n! —

             n! returns the factorial of n.


2922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2923 ordinal=2923 -->
## Functions

Functions

The following equation defines the factorial function.


PrimePrime FactorFactor

Computes the prime factorization of an integer.


Inputs/Outputs

   •     n —

   n is an integer the VI factorizes. If n is negative, the VI factorizes the absolute value of n.

   •      Prime Factors —

    Prime Factors returns an array of prime numbers whose product equals n.


CheckCheck PrimePrime

Checks whether a number is a prime number.


Inputs/Outputs

   •     n —

   n specifies an integer.

   •      prime? —

    prime? returns TRUE if n is a prime number.


                                                    © National Instruments 2923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2924 ordinal=2924 -->
## Functions

Functions

      PermutePermute

      Computes the number of ways to obtain an ordered subset of k elements from a set of
     n elements.


      Inputs/Outputs

               •     n —

          n is an unsigned integer.

               •     k —

           k is an unsigned integer.

               •     nPk —

          nPk returns the number of ordered subsets of k elements that you can obtain from a set of n
            elements.


      BinomialBinomial CoefficientCoefficient VIVI

       Calculates the binomial coefficient for nonnegative integer values of n and k.


      Inputs/Outputs

               •     n —

          n is any nonnegative integer.

               •     k —

           k is any nonnegative integer.


2924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2925 ordinal=2925 -->
## Functions

Functions

   •      binomial coefficient (n,k) —

    binomial coefficient (n,k) is the result of the calculation of the binomial coefficient for the given
    values of n and k.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the binomial coefficient.


Binomial coefficients can have many digits, even in the case of relatively small
numbers n and k. The data type most suited for the binomial coefficient is a double
real. You can directly calculate the factorial functions, n!, k!, and (n – k)!, with the
(Incomplete) Gamma Function VI.

ContinuedContinued FractionFraction VIVI

Evaluates the continued fraction of two sequences (a[0], a[1], …, a[n]) and (b[0], b[1],
…, b[n]).


Inputs/Outputs

   •     A —

   A is the 1D array of the numerator part of the continued fraction.

   •     B —

   B is the 1D array of the denominator part of the continued fraction.

   •       result —


                                                    © National Instruments 2925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2926 ordinal=2926 -->
## Functions

Functions


             result is a real value representing the result of the continued fraction.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the evaluated sequences.


      Continued fractions are valuable tools for calculating special functions.

      (Riemann)(Riemann) ZetaZeta FunctionFunction

      Computes the zeta function.


      Inputs/Outputs

               •      x —

           x is the input argument.

               •       z(x) —

              z(x) returns the value of the zeta function.


      The following formula defines the Riemann zeta function ζ(x).


2926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2927 ordinal=2927 -->
## Functions

Functions

BesselBessel FunctionsFunctions

Use this class of special functions to compute Bessel-related functions.

The VIs on this palette can return mathematics error codes.


 Palette Object       Description

 Bessel Function Jv   Computes the Bessel function of the first kind.


                  Computes the Bessel function of the second kind, also known as the Bessel Function Yv                Neumann function.


                  Computes the Hankel function, which is also known as the Bessel function of Hankel Function Hv                     the third kind.


 Modified Bessel
                  Computes the modified Bessel function of the first kind. Function Iv

 Modified Bessel                  Computes the modified Bessel function of the second kind. Function Kn

 Spherical Bessel
                      Calculates the spherical Bessel function of the first kind.
 Function jn

 Spherical Bessel
                      Calculates the spherical Bessel function of the second kind.
 Function yn


 Spherical Hankel    Computes the spherical Hankel function, which is also known as the
 Function hn          spherical Bessel function of the third kind.


                                                    © National Instruments 2927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2928 ordinal=2928 -->
## Functions

Functions


         Palette Object       Description

          Airy Functions      Computes the Airy functions Ai(x) and Bi(x).


         Struve Function     Computes the Struve function.


         Kelvin Functions be  Computes the complex Kelvin function of the first kind.


         Kelvin Functions ke  Computes the complex Kelvin function of the second kind.


      BesselBessel FunctionFunction JvJv

      Computes the Bessel function of the first kind.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •      v —

           v specifies the order of the Bessel function.

               •       Jv(x) —

             Jv(x) returns the value of the Bessel function of the first kind.


      The Bessel function of the first kind of order v, Jv, is a solution of the following
        differential equation.


2928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2929 ordinal=2929 -->
## Functions

Functions


The function is defined according to the following intervals for the input values.


LabVIEW supports the entire domain of this function that produces real-valued results.
For any integer value of order v, the function is defined for all real values of x.
Otherwise, the function is defined for nonnegative real values of x.

BesselBessel FunctionFunction YvYv

Computes the Bessel function of the second kind, also known as the Neumann
function.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      v —

    v specifies the order of the Bessel function.

   •       Yv(x) —

     Yv(x) returns the value of the Bessel function of the second kind.


The Bessel function of the second kind of order v, Yv, is a solution of the following
differential equation.


The function is defined according to the following intervals for the input values.

                                                    © National Instruments 2929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2930 ordinal=2930 -->
## Functions

Functions


      LabVIEW supports the entire domain of this function that produces real-valued results.
       For any real value of order v, the function is defined for positive real values of x.

      HankelHankel FunctionFunction HvHv

      Computes the Hankel function, which is also known as the Bessel function of the third
       kind.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •      v —

           v specifies the order of the Hankel function.

               •      type —

           type specifies the type of the Hankel function.

           0 First Kind—Computes the Hankel function of the first kind.
           1 Second Kind—Computes the Hankel function of the second kind.

               •      Hv(x) —

            Hv(x) returns the value of the Hankel function.


      The following equation defines the Hankel function of the first kind of order v.


2930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2931 ordinal=2931 -->
## Functions

Functions

The following equation defines the Hankel function of the second kind of order v.


where Jv is a Bessel function of the first kind and Yv is a Bessel function of the second
kind.

The following intervals for the input values of the VI define the Hankel function.


For any real value of order v, LabVIEW supports positive real values of x.

ModifiedModified BesselBessel FunctionFunction IvIv

Computes the modified Bessel function of the first kind.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      v —

    v specifies the order of the Bessel function.

   •        Iv(x) —

     Iv(x) returns the value of the modified Bessel function of the first kind.


The modified Bessel function of the first kind of order v, Iv, also known as the
hyperbolic Bessel function of the first kind, is a solution of the following differential
equation.


                                                    © National Instruments 2931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2932 ordinal=2932 -->
## Functions

Functions


      The function is defined according to the following intervals for the input values.


      LabVIEW supports the entire domain of this function that produces real-valued results.
       For any integer value of order v, the function is defined for all real values of x. For any
       noninteger value of order v, the function is defined for nonnegative real values of x.

      ModifiedModified BesselBessel FunctionFunction KnKn

      Computes the modified Bessel function of the second kind.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •     n —

          n specifies the order of the modified Bessel function.

               •      Kn(x) —

            Kn(x) returns the value of the modified Bessel function of the second kind.


      The modified Bessel function of the second kind of order n, Kn, also known as the
       hyperbolic Bessel function of the second kind, is a solution of the following differential
       equation.


      The function is defined according to the following intervals for the input values.

2932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2933 ordinal=2933 -->
## Functions

Functions


LabVIEW supports the entire domain of this function that produces real-valued results.
For any integer value of order n, the function is defined for nonnegative real values of
x.

SphericalSpherical BesselBessel FunctionFunction jnjn

Calculates the spherical Bessel function of the first kind.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •     n —

   n specifies the order of the spherical Bessel function.

   •       jn(x) —

     jn(x) returns the value of the spherical Bessel function of the first kind.


The spherical Bessel function of the first kind of order n, jnis a solution to the
following differential equation.


The following equation shows the relationship of the spherical Bessel function of the
first kind to the Bessel function of the first kind.


The function is defined according to the following intervals for the input values.

                                                    © National Instruments 2933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2934 ordinal=2934 -->
## Functions

Functions


      LabVIEW supports the entire domain of this function that produces real-valued results.
       For any integer value of order n, the function is defined for nonnegative real values of
        x.

       SphericalSpherical BesselBessel FunctionFunction ynyn

       Calculates the spherical Bessel function of the second kind.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •     n —

          n specifies the order of the spherical Bessel function.

               •       yn(x) —

             yn(x) returns the value of the spherical Bessel function of the second kind.


      The spherical Bessel function of the second kind of order n, ynis a solution to the
       following differential equation.


      The following equation shows the relationship of the spherical Bessel function of the
      second kind to the Bessel function of the second kind.


      The function is defined according to the following intervals for the input values.

2934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2935 ordinal=2935 -->
## Functions

Functions


LabVIEW supports the entire domain of this function that produces real-valued results.
For any integer value of order n, the function is defined for nonnegative real values of
x.

SphericalSpherical HankelHankel FunctionFunction hnhn

Computes the spherical Hankel function, which is also known as the spherical Bessel
function of the third kind.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •     n —

   n specifies the order of the spherical Hankel function.

   •      type —

    type specifies the type of the spherical Hankel function.

    0 First Kind—Computes the spherical Hankel function of the first kind.
    1 Second Kind—Computes the spherical Hankel function of the second kind.

   •      hn(x) —

    hn(x) returns the value of the spherical Hankel function.


The following equation defines the spherical Hankel function of the first kind of order
n.


                                                    © National Instruments 2935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2936 ordinal=2936 -->
## Functions

Functions


      The following equation defines the spherical Hankel function of the second kind of
       order n.


      where jn is a spherical Bessel function of the first kind and yn is a spherical Bessel
       function of the second kind.

      The following intervals for the input values of the VI define the spherical Hankel
       function.


       For any integer value of order n, LabVIEW supports nonnegative real values of x.

       AiryAiry FunctionsFunctions

      Computes the Airy functions Ai(x) and Bi(x).


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •       Ai(x) —

              Ai(x) returns the value of the Airy function Ai.

               •       Bi(x) —

              Bi(x) returns the value of the Airy function Bi.


2936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2937 ordinal=2937 -->
## Functions

Functions

The Airy functions Ai and Bi are solutions to the Airy differential equation, which is
given by the following equation.


StruveStruve FunctionFunction

Computes the Struve function.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      v —

    v is the index parameter.

   •      Hv(x) —

    Hv(x) returns the value of the Struve function.


The Struve function of order v, Hv(x) is a solution of the following differential
equation.


The function is defined according to the following intervals for the input values.


LabVIEW supports the entire domain of this function that produces real-valued results.
For any integer value of order v, the function is defined for all real values of x.
Otherwise, the function is defined for nonnegative real values of x.

                                                    © National Instruments 2937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2938 ordinal=2938 -->
## Functions

Functions

       KelvinKelvin FunctionsFunctions bebe

      Computes the complex Kelvin function of the first kind.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •     n —

          n specifies the order of the Kelvin function.

               •       ber(x) + bei(x)i —

             ber(x) + bei(x)i returns the complex value of the Kelvin function of the first kind.


      The complex-valued Kelvin function of the first kind of order vis a solution of the
       following complex-valued differential equation.


      The real and imaginary parts of the Kelvin function of the first kind of order vare
       solutions of the following differential equation.


      The function is defined according to the following intervals for the input values.


       For any integer value of order n, the function is defined for all real values of x.


2938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2939 ordinal=2939 -->
## Functions

Functions

KelvinKelvin FunctionsFunctions keke

Computes the complex Kelvin function of the second kind.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •     n —

   n specifies the order of the Kelvin function.

   •       ker(x) + kei(x)i —

     ker(x) + kei(x)i returns the complex value of the Kelvin function of the second kind.


The complex-valued Kelvin function of the second kind of order vis a solution of the
following complex-valued differential equation.


The real and imaginary parts of the Kelvin function of the second kind of order vare
solutions of the following differential equation.


The function is defined according to the following intervals for the input values.


For any integer value of order n, the function is defined for positive real values of x.


                                                    © National Instruments 2939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2940 ordinal=2940 -->
## Functions

Functions

    GammaGamma FunctionsFunctions

      Use this class of special functions to compute Gamma-related functions.

      The VIs on this palette can return mathematics error codes.


         Palette Object          Description

          Factorial            Computes the factorial of n.


                                Evaluates the gamma function and regularized incomplete gamma         (Incomplete) Gamma                                  function. You must manually select the polymorphic instance you want to
         Function                                 use.


           Stirling's Formula      Computes the Stirling approximation to the gamma function.


         (Incomplete) Beta      Evaluates the beta function and regularized incomplete beta function. You
         Function             must manually select the polymorphic instance you want to use.


        Logarithm of Factorial  Computes the natural logarithm of a factorial.


        Logarithm of Complete
                           Computes the natural logarithm of the complete gamma function.
      Gamma Function

        Complementary
        Incomplete Gamma    Computes the regularized complementary incomplete gamma function.
         Function

          Psi (Digamma)
                           Computes the psi, or digamma, function.
         Function


2940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2941 ordinal=2941 -->
## Functions

Functions

FactorialFactorial

Computes the factorial of n.


Inputs/Outputs

   •     n —

   n is the input argument.

   •       n! —

    n! returns the factorial of n.


The following equation defines the factorial function.


(Incomplete)(Incomplete) GammaGamma FunctionFunction

Evaluates the gamma function and regularized incomplete gamma function. You must
manually select the polymorphic instance you want to use.


  • Gamma Function VI
  • Incomplete Gamma Function VI

Gamma Function

The following equation defines the gamma function.


                                                    © National Instruments 2941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2942 ordinal=2942 -->
## Functions

Functions


      The gamma function is related to the factorial function by the identity gamma(n+ 1) =
      n! for integer n.

      Incomplete Gamma Function

      The following equation defines the regularized incomplete gamma function.


      The following intervals for the input values define the function.


      The following illustration shows the regularized incomplete gamma functions with a =
        1, 2, 3, and 4 from top to bottom.


  GammaGamma FunctionFunction VIVI

       Evaluates the gamma function and regularized incomplete gamma function. You must
      manually select the polymorphic instance you want to use.


2942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2943 ordinal=2943 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x is the real input of the gamma function.

   •       g(x) —

     g(x) is the result of the gamma function for the given value of x.


Gamma Function

The following equation defines the gamma function.


The gamma function is related to the factorial function by the identity gamma(n+ 1) =
n! for integer n.

Incomplete Gamma Function

The following equation defines the regularized incomplete gamma function.


The following intervals for the input values define the function.


The following illustration shows the regularized incomplete gamma functions with a =
1, 2, 3, and 4 from top to bottom.


                                                    © National Instruments 2943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2944 ordinal=2944 -->
## Functions

Functions


   IncompleteIncomplete GammaGamma FunctionFunction VIVI

       Evaluates the gamma function and regularized incomplete gamma function. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      x —

           x is the real input of the incomplete gamma function. x must be nonnegative.

               •      a —

           a is the upper limit of the regularized incomplete gamma function. The default value is Inf.

               •       g(x, a) —

              g(x, a) is the result of the regularized incomplete gamma function for the given values of x and a.


     Gamma Function

      The following equation defines the gamma function.


2944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2945 ordinal=2945 -->
## Functions

Functions

The gamma function is related to the factorial function by the identity gamma(n+ 1) =
n! for integer n.

Incomplete Gamma Function

The following equation defines the regularized incomplete gamma function.


The following intervals for the input values define the function.


The following illustration shows the regularized incomplete gamma functions with a =
1, 2, 3, and 4 from top to bottom.


Stirling'sStirling's FormulaFormula

Computes the Stirling approximation to the gamma function.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.


                                                    © National Instruments 2945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2946 ordinal=2946 -->
## Functions

Functions

               •       Stirling(x) —

              Stirling(x) returns the value of the Stirling function.


      The following approximation defines the Stirling approximation to the gamma
       function.


      The function is defined according to the following interval for the input value.


      LabVIEW supports the entire domain of this function that produces real-valued results.
      The function is defined for nonnegative real values of x.

      (Incomplete)(Incomplete) BetaBeta FunctionFunction

       Evaluates the beta function and regularized incomplete beta function. You must
      manually select the polymorphic instance you want to use.


            • Beta Function VI
            • Incomplete Beta Function VI

      Beta Function

      The following equation defines the beta function.


      The following intervals for the input values define the function.


2946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2947 ordinal=2947 -->
## Functions

Functions

Incomplete Beta Function

The following equation defines the regularized incomplete beta function.


The following intervals for the input values define the function.


For any real nonnegative value of upper limit a ≤ 1, the function is defined for all real
nonnegative values of x and y.
BetaBeta FunctionFunction VIVI

Evaluates the beta function and regularized incomplete beta function. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      x —

    x is the first argument of the beta function. x must be nonnegative.

   •      y —

    y is the second argument of the beta function. y must be nonnegative.

   •       b(x, y) —

     b(x, y) is the result of the beta function for the given values of x and y.


Beta Function


                                                    © National Instruments 2947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2948 ordinal=2948 -->
## Functions

Functions

      The following equation defines the beta function.


      The following intervals for the input values define the function.


      Incomplete Beta Function

      The following equation defines the regularized incomplete beta function.


      The following intervals for the input values define the function.


       For any real nonnegative value of upper limit a ≤ 1, the function is defined for all real
      nonnegative values of x and y.
   IncompleteIncomplete BetaBeta FunctionFunction VIVI

       Evaluates the beta function and regularized incomplete beta function. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      x —

           x is the first argument of the beta function. x must be nonnegative.


2948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2949 ordinal=2949 -->
## Functions

Functions

   •      y —

    y is the second argument of the beta function. y must be nonnegative.

   •      a —

    a is the upper limit of the regularized incomplete beta integral and is a real number between 0
    and 1. The default value is 1.

   •       b(x, y, a) —

     b(x, y, a) is the result of the regularized incomplete beta function for the given values of x, y, and
     a.


Beta Function

The following equation defines the beta function.


The following intervals for the input values define the function.


Incomplete Beta Function

The following equation defines the regularized incomplete beta function.


The following intervals for the input values define the function.


For any real nonnegative value of upper limit a ≤ 1, the function is defined for all real
nonnegative values of x and y.


                                                    © National Instruments 2949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2950 ordinal=2950 -->
## Functions

Functions

      LogarithmLogarithm ofof FactorialFactorial

      Computes the natural logarithm of a factorial.


      Inputs/Outputs

               •     n —

          n is the input argument.

               •       ln(n!) —

              ln(n!) returns the natural log of the factorial.


      LogarithmLogarithm ofof CompleteComplete GammaGamma FunctionFunction

      Computes the natural logarithm of the complete gamma function.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •       ln(g(x)) —

              ln(g(x)) returns the natural logarithm of the complete gamma function.


     ComplementaryComplementary IncompleteIncomplete GammaGamma FunctionFunction

      Computes the regularized complementary incomplete gamma function.


2950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2951 ordinal=2951 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      a —

    a is the lower limit of the regularized complementary incomplete gamma integral.

   •      1 - g(x, a) —

    1 - g(x, a) returns the value of the regularized complementary incomplete gamma function.


The following equation defines the complement of the regularized incomplete gamma
function.


The complement of the regularized incomplete gamma function is related to the
regularized incomplete gamma function by the following identity.


The regularized incomplete gamma function is defined according to the following
intervals for the input values.


For any positive real value of lower limit a, the regularized incomplete gamma function
is defined for nonnegative real values of x.

PsiPsi (Digamma)(Digamma) FunctionFunction

Computes the psi, or digamma, function.

                                                    © National Instruments 2951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2952 ordinal=2952 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •       y(x) —

              y(x) returns the value of the psi function.


      The following equation defines the psi function.


     HypergeometricHypergeometric FunctionsFunctions

      Use this class of special functions to compute functions based on the hypergeometric
        differential equation.

      The VIs on this palette can return mathematics error codes.


         Palette
                      Description
        Object

        Gauss      Computes the Gauss hypergeometric function F(x, a, b, c) according to the input
         Function    argument and parameters you specify.


       Kummer
                  Computes the Kummer, or confluent hypergeometric, function.
         Function


2952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2953 ordinal=2953 -->
## Functions

Functions


 Palette              Description
 Object

 Tricomi            Computes the Tricomi, or associated confluent hypergeometric, function. Function

GaussGauss FunctionFunction

Computes the Gauss hypergeometric function F(x, a, b, c) according to the input
argument and parameters you specify.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      a —

    a is the first parameter of the Gauss hypergeometric function.

   •     b —

   b is the second parameter of the Gauss hypergeometric function.

   •      c —

    c is the third parameter of the Gauss hypergeometric function.

   •       F(x, a, b, c) —

     F(x, a, b, c) returns the value of the Gauss hypergeometric function.


The Gauss hypergeometric function F(x, a, b, c) is a solution of the following
differential equation:


                                                    © National Instruments 2953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2954 ordinal=2954 -->
## Functions

Functions


      The function is defined according to the following intervals for the input values.


      LabVIEW supports the entire domain of this function that produces real-valued results.
       For any real value of a, b, and c, the function is defined for real values of x < 1. For real
       values of a, b, and c, such that c > a + b, the domain of x is extended to include 1.

     KummerKummer FunctionFunction

      Computes the Kummer, or confluent hypergeometric, function.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •      a —

           a is the first parameter of the Kummer function.

               •     b —

          b is the second parameter of the Kummer function.

               •      M(x, a, b) —

            M(x, a, b) returns the value of the Kummer function.


      The Kummer function is a solution of the following differential equation.


2954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2955 ordinal=2955 -->
## Functions

Functions

The function is defined according to the following intervals for the input values.


LabVIEW supports the entire domain of this function that produces real-valued results.
For any real value of a and any real value of b except nonpositive integers, the function
is defined for all real values of x.

TricomiTricomi FunctionFunction

Computes the Tricomi, or associated confluent hypergeometric, function.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      a —

    a is the first parameter of the Tricomi function.

   •     b —

   b is the second parameter of the Tricomi function.

   •       U(x, a, b) —

    U(x, a, b) returns the value of the Tricomi function.


The Tricomi function U(x, a, b) is a solution of the following differential equation:


                                                    © National Instruments 2955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2956 ordinal=2956 -->
## Functions

Functions

       EllipticElliptic IntegralsIntegrals

      Use this class of special functions to compute complete and incomplete elliptic
        integrals.

      The VIs on this palette can return mathematics error codes.


         Palette Object     Description

           Elliptic Integral of  Computes the Legendre elliptic integral of the first kind. You must manually
         the 1st kind         select the polymorphic instance you want to use.


           Elliptic Integral of  Computes the Legendre elliptic integral of the second kind. You must manually
         the 2nd kind        select the polymorphic instance you want to use.


        EllipticElliptic IntegralIntegral ofof thethe 1st1st kindkind

      Computes the Legendre elliptic integral of the first kind. You must manually select the
      polymorphic instance you want to use.


            • Complete Elliptic Integral K VI
            • Incomplete Elliptic Integral F VI

      Complete Elliptic Integral K

      The following equation defines the complete elliptic integral of the first kind.


2956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2957 ordinal=2957 -->
## Functions

Functions

where k is the square of the elliptic modulus.

Incomplete Elliptic Integral F

The following equation defines the incomplete elliptic integral of the first kind.


where k is the square of the elliptic modulus and a is the upper limit, or amplitude, of
the integral.

The following intervals for the input values define the function.


LabVIEW supports the entire domain of this function that produces real-valued results.
For a real value of upper limit a, the function is defined for all real values of k in the
unit interval.
CompleteComplete EllipticElliptic IntegralIntegral KK VIVI

Computes the Legendre elliptic integral of the first kind. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •     k —

    k is the square of the elliptic modulus. k is a real number between 0 and 1.

   •      K(k) —

    K(k) is the value of the complete elliptic integral of the first kind.


                                                    © National Instruments 2957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2958 ordinal=2958 -->
## Functions

Functions

      Complete Elliptic Integral K

      The following equation defines the complete elliptic integral of the first kind.


      where k is the square of the elliptic modulus.

      Incomplete Elliptic Integral F

      The following equation defines the incomplete elliptic integral of the first kind.


      where k is the square of the elliptic modulus and a is the upper limit, or amplitude, of
       the integral.

      The following intervals for the input values define the function.


      LabVIEW supports the entire domain of this function that produces real-valued results.
       For a real value of upper limit a, the function is defined for all real values of k in the
       unit interval.
   IncompleteIncomplete EllipticElliptic IntegralIntegral FF VIVI

      Computes the Legendre elliptic integral of the first kind. You must manually select the
      polymorphic instance you want to use.


2958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2959 ordinal=2959 -->
## Functions

Functions

Inputs/Outputs

   •     k —

    k is the square of the elliptic modulus. k is a real number between 0 and 1.

   •      a —

    a is the amplitude of the function, which is the upper limit of the integral. The default value is Pi/
     2.

   •       F(k, a) —

     F(k, a) is the value of the incomplete elliptic integral of the first kind.


Complete Elliptic Integral K

The following equation defines the complete elliptic integral of the first kind.


where k is the square of the elliptic modulus.

Incomplete Elliptic Integral F

The following equation defines the incomplete elliptic integral of the first kind.


where k is the square of the elliptic modulus and a is the upper limit, or amplitude, of
the integral.

The following intervals for the input values define the function.


LabVIEW supports the entire domain of this function that produces real-valued results.

                                                    © National Instruments 2959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2960 ordinal=2960 -->
## Functions

Functions

       For a real value of upper limit a, the function is defined for all real values of k in the
       unit interval.

        EllipticElliptic IntegralIntegral ofof thethe 2nd2nd kindkind

      Computes the Legendre elliptic integral of the second kind. You must manually select
       the polymorphic instance you want to use.


            • Complete Elliptic Integral E VI
            • Incomplete Elliptic Integral E VI

      Complete Elliptic Integral E

      The following equation defines the complete elliptic integral of the second kind.


      where k is the square of the elliptic modulus.

      Incomplete Elliptic Integral E

      The following equation defines the incomplete elliptic integral of the second kind.


      where k is the square of the elliptic modulus and a is the upper limit, or amplitude, of
       the integral.

      The following intervals for the input values define the function.


2960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2961 ordinal=2961 -->
## Functions

Functions

LabVIEW supports the entire domain of this function that produces real-valued results.
For any real value of upper limit a, the function is defined for all real values of k in the
unit interval.
CompleteComplete EllipticElliptic IntegralIntegral EE VIVI

Computes the Legendre elliptic integral of the second kind. You must manually select
the polymorphic instance you want to use.


Inputs/Outputs

   •     k —

    k is the square of the elliptic modulus. k is a real number between 0 and 1.

   •       E(k) —

    E(k) is the value of the complete elliptic integral of the second kind.


Complete Elliptic Integral E

The following equation defines the complete elliptic integral of the second kind.


where k is the square of the elliptic modulus.

Incomplete Elliptic Integral E

The following equation defines the incomplete elliptic integral of the second kind.


                                                    © National Instruments 2961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2962 ordinal=2962 -->
## Functions

Functions


      where k is the square of the elliptic modulus and a is the upper limit, or amplitude, of
       the integral.

      The following intervals for the input values define the function.


      LabVIEW supports the entire domain of this function that produces real-valued results.
       For any real value of upper limit a, the function is defined for all real values of k in the
       unit interval.
   IncompleteIncomplete EllipticElliptic IntegralIntegral EE VIVI

      Computes the Legendre elliptic integral of the second kind. You must manually select
       the polymorphic instance you want to use.


      Inputs/Outputs

               •     k —

           k is the square of the elliptic modulus. k is a real number between 0 and 1.

               •      a —

           a is the amplitude of the function, which is the upper limit of the integral. The default value is Pi/
               2.

               •       E(k, a) —

             E(k, a) is the value of the incomplete elliptic integral of the second kind.


      Complete Elliptic Integral E

2962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2963 ordinal=2963 -->
## Functions

Functions

The following equation defines the complete elliptic integral of the second kind.


where k is the square of the elliptic modulus.

Incomplete Elliptic Integral E

The following equation defines the incomplete elliptic integral of the second kind.


where k is the square of the elliptic modulus and a is the upper limit, or amplitude, of
the integral.

The following intervals for the input values define the function.


LabVIEW supports the entire domain of this function that produces real-valued results.
For any real value of upper limit a, the function is defined for all real values of k in the
unit interval.

ExponentialExponential IntegralsIntegrals

Use this class of special functions to compute exponential integrals.

The VIs on this palette can return mathematics error codes.


                                                    © National Instruments 2963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2964 ordinal=2964 -->
## Functions

Functions


         Palette Object               Description

         Exponential Integral        Computes the exponential integral function.


         Sine Integral                 Evaluates the sine integral for any real number x.


        Cosine Integral              Evaluates the cosine integral for any real nonnegative number x.


         Dilogarithm              Computes the dilogarithm function, or Spence's Integral.


         Hyperbolic Sine Integral     Computes the hyperbolic sine integral function.


         Hyperbolic Cosine Integral   Computes the hyperbolic cosine integral function.


      ExponentialExponential IntegralIntegral

      Computes the exponential integral function.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •     n —

          n is the exponent parameter.

               •      En(x) —


2964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2965 ordinal=2965 -->
## Functions

Functions


    En(x) returns the value of the exponential integral function.


The following equation defines the exponential integral function.


The following intervals for the input values define the exponential integral function.


LabVIEW supports the entire domain of this function that produces real-valued results.
For any nonnegative integer value of order n, the function is defined for nonnegative
real values of x.

SineSine IntegralIntegral

Evaluates the sine integral for any real number x.


Inputs/Outputs

   •      x —

    x is any real number.

   •       Si(x) —

     Si(x) is the result of the calculation of the sine integral for the given value of x.


The following equation defines the sine integral.


                                                    © National Instruments 2965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2966 ordinal=2966 -->
## Functions

Functions

      where Siis the sine integral.

      The following illustration shows the graph of the sine integral in the interval (0, 15).


      CosineCosine IntegralIntegral

       Evaluates the cosine integral for any real nonnegative number x.


      Inputs/Outputs

               •      x —

           x is any real nonnegative number. If x is negative, the VI uses the absolute value of x.

               •       Ci(x) —

              Ci(x) is the result of the calculation of the cosine integral for the given value of x.


      The following equation defines the cosine integral.


      where Ciis the cosine integral and γ is the Euler constant.


2966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2967 ordinal=2967 -->
## Functions

Functions

The following illustration shows the graph of the cosine integral in the interval (0, 15).


DilogarithmDilogarithm

Computes the dilogarithm function, or Spence's Integral.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •       diln(x) —

     diln(x) returns the value of the dilogarithm function.


The following equation defines the dilogarithm and the Spence's Integral.


where F(x) is the Spence's Integral and diln(x) is the dilogarithm.

The following intervals for the input values define the dilogarithm function.


                                                    © National Instruments 2967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2968 ordinal=2968 -->
## Functions

Functions


      The function is defined for nonnegative real values of x.

      HyperbolicHyperbolic SineSine IntegralIntegral

      Computes the hyperbolic sine integral function.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •       Shi(x) —

             Shi(x) returns the value of the hyperbolic sine integral.


      The following equation defines the hyperbolic sine integral function.


      HyperbolicHyperbolic CosineCosine IntegralIntegral

      Computes the hyperbolic cosine integral function.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.


2968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2969 ordinal=2969 -->
## Functions

Functions

   •       Chi(x) —

     Chi(x) returns the value of the hyperbolic cosine integral.


The following equation defines the hyperbolic cosine integral function.


where γ is Euler's constant.

ErrorError FunctionsFunctions

Use this class of special functions to compute Error-related functions.

The VIs on this palette can return mathematics error codes.


 Palette Object            Description

 Error Function          Computes the error function.


 Error Function
                      Computes the error function complement.
 Complement


 Scaled Error Function     Computes the scaled complementary error function associated with a
 Complement            normal distribution.


                      Computes the inverse of the error function associated with a normal
 Inverse Error Function
                              distribution.


                                                    © National Instruments 2969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2970 ordinal=2970 -->
## Functions

Functions


         Palette Object            Description

         Inverse Error Function    Computes the inverse of the complementary error function associated
       Complement             with a normal distribution.


         Fresnel Integrals         Computes the Fresnel cosine and sine integral functions.


        Dawson's Integral        Computes the Dawson integral.


       ErrorError FunctionFunction

      Computes the error function.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •       erf(x) —

              erf(x) returns the value of the error function.


      The following equation defines the error function.


       ErrorError FunctionFunction ComplementComplement

      Computes the error function complement.


2970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2971 ordinal=2971 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      1 - erf(x) —

    1 - erf(x) returns the value of the error function complement.


The following equation defines the error function complement.


ScaledScaled ErrorError FunctionFunction ComplementComplement

Computes the scaled complementary error function associated with a normal
distribution.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •      scaled erfc(x) —

    scaled erfc(x) returns the value of the scaled error function complement.


The following equation defines the scaled error function complement.


                                                    © National Instruments 2971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2972 ordinal=2972 -->
## Functions

Functions


       InverseInverse ErrorError FunctionFunction

      Computes the inverse of the error function associated with a normal distribution.

       This VI calculates the Error Function VI in reverse.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •       inverf(x) —

              inverf(x) returns the value of the inverse error function.


       InverseInverse ErrorError FunctionFunction ComplementComplement

      Computes the inverse of the complementary error function associated with a normal
        distribution.

       This VI calculates the Error Function Complement VI in reverse.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •       inverfc(x) —


2972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2973 ordinal=2973 -->
## Functions

Functions


     inverfc(x) returns the value of the inverse error function complement.


FresnelFresnel IntegralsIntegrals

Computes the Fresnel cosine and sine integral functions.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •       C(x) —

    C(x) returns the value of the Fresnel cosine integral.

   •       S(x) —

     S(x) returns the value of the Fresnel sine integral.


The following equation defines the Fresnel cosine integral.


The following equation defines the Fresnel sine integral.


Dawson'sDawson's IntegralIntegral

Computes the Dawson integral.


                                                    © National Instruments 2973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2974 ordinal=2974 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •      daw(x) —

           daw(x) returns the value of the Dawson integral.


      The following formula defines Dawson's integral function.


       EllipticElliptic && ParabolicParabolic FunctionsFunctions

      Use this class of special functions to compute specific forms of elliptic integrals or
      Weber functions.

      The VIs on this palette can return mathematics error codes.


         Palette Object                  Description

        Jacobian Elliptic Functions      Determines the Jacobian elliptic functions cn, dn, and sn.


         Parabolic Cylinder Function     Computes the parabolic cylinder, or Weber, function.


2974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2975 ordinal=2975 -->
## Functions

Functions

JacobianJacobian EllipticElliptic FunctionsFunctions

Determines the Jacobian elliptic functions cn, dn, and sn.


Inputs/Outputs

   •      x —

    x is the input argument. If x is negative, the VI uses the absolute value of x.

   •     k —

    k is the integrand parameter.

   •      cn —

    cn returns the value of the Jacobi elliptic function cn.

   •     dn —

   dn returns the Jacobi elliptic function dn.

   •      sn —

    sn returns the value of the Jacobi elliptic function sn.

   •      phi —

    phi is the upper limit of the integral defining the function.


The following equations define the three Jacobian elliptic functions.

cn(x, k) = cos(ϕ) sn(x, k) = sin(ϕ)

where


                                                    © National Instruments 2975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2976 ordinal=2976 -->
## Functions

Functions


      The function is defined according to the following intervals for the input values.


       For any real value of integrand parameter k in the unit interval, the function is defined
        for all real values of x.

       ParabolicParabolic CylinderCylinder FunctionFunction

      Computes the parabolic cylinder, or Weber, function.


      Inputs/Outputs

               •      x —

           x is the input argument. If x is negative, the VI uses the absolute value of x.

               •      v —

           v specifies the order of the parabolic cylinder function.

               •      Dv(x) —

            Dv(x) returns the value of the parabolic cylinder function.


      The parabolic cylinder function, Dv(x), is a solution of the following differential
       equation:


2976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2977 ordinal=2977 -->
## Functions

Functions

LinearLinear AlgebraAlgebra

Use the Linear Algebra VIs to perform matrix-related computations and analysis.

      Note Many Linear Algebra VIs are available only in the LabVIEW Full and
        Professional Development Systems. If you have the LabVIEW Base
       Development System, you do not have the full set of the Linear Algebra VIs
       described in this help file. A subset of the Linear Algebra VIs is available in the
       LabVIEW Base Development System.

The VIs on this palette can return mathematics error codes.


 Palette Object  Description

                Generates a special matrix based on matrix type. The data types you wire to the
 Create Special                Input Vector2 and Input Vector1 inputs determine the polymorphic instance to Matrix                 use.

 Create Real
 Matrix From    Generates a real matrix from Eigenvalues.
 Eigenvalues

              Use the Matrix functions to manipulate the elements, diagonals, and submatrices
 Matrix           of a matrix or 2D numeric array. Many of these functions complement existing
                 array operations but offer functionality for math algorithms based on matrices.


 Solve Linear    Solves a linear system AX = Y. The data types you wire to the Input Matrix and
 Equations     Known Vector inputs determine the polymorphic instance to use.


              Computes the dot product of X Vector and Y Vector. The data types you wire to the
 Dot Product
              X Vector and Y Vector inputs determine the polymorphic instance to use.


                                                    © National Instruments 2977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2978 ordinal=2978 -->
## Functions

Functions


         Palette Object  Description

                    Computes the outer product of X Vector and Y Vector. The data types you wire to
        Outer Product                        the X Vector and Y Vector inputs determine the polymorphic instance to use.


                       Performs the multiplication of two input matrices or an input matrix and an input
       A x B             vector. The data types you wire to the A and B inputs determine the polymorphic
                         instance to use.


        Kronecker      Calculates the Kronecker product of the input matrices A and B. The data types
        Product       you wire to the A and B inputs determine the polymorphic instance to use.


        Subspaces                    Computes the angle between column spaces of two matrices.        Angle


                    Computes the determinant of Input Matrix. Wire data to the Input Matrix input to
        Determinant                       determine the polymorphic instance to use or manually select the instance.


                    Computes the norm of Input Vector. Wire data to the Input Vector input to
         Vector Norm                       determine the polymorphic instance to use or manually select the instance.


                    Computes the norm of Input Matrix. Wire data to the Input Matrix input to         Matrix Norm                       determine the polymorphic instance to use or manually select the instance.


                    Computes the rank of Input Matrix. Wire data to the Input Matrix input to
         Matrix Rank
                       determine the polymorphic instance to use or manually select the instance.


                        Finds the trace of Input Matrix. Wire data to the Input Matrix input to determine
         Trace
                        the polymorphic instance to use or manually select the instance.


         Test Matrix
                          Tests whether Input Matrix is a matrix of special type. Wire data to the Input
        Type


2978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2979 ordinal=2979 -->
## Functions

Functions


Palette Object  Description

                Matrix input to determine the polymorphic instance to use or manually select the
                 instance.


Matrix        Computes the condition number of Input Matrix. Wire data to the Input Matrix
Condition       input to determine the polymorphic instance to use or manually select the
Number         instance.


                Finds Inverse Matrix, if it exists, of Input Matrix. Wire data to the Input Matrix
Inverse Matrix   input to determine the polymorphic instance to use or manually select the
                 instance.


                Finds the PseudoInverse Matrix of Input Matrix. Wire data to the Input MatrixPseudoInverse                input to determine the polymorphic instance to use or manually select theMatrix
                 instance.


               Transposes Input Matrix. If Input Matrix is a complex matrix, the VI performsTranspose               conjugate transposition. Wire data to the Input Matrix input to determine the
Matrix               polymorphic instance to use or manually select the instance.


Matrix Square  Computes the square root of Input Matrix. Wire data to the Input Matrix input to
Root           determine the polymorphic instance to use or manually select the instance.


             Computes the exponential of a square Input Matrix. Wire data to the Input Matrix
Matrix Exp      input to determine the polymorphic instance to use or manually select the
                 instance.


             Computes the nth power of Input Matrix. Wire data to the Input Matrix input toMatrix Power
               determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 2979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2980 ordinal=2980 -->
## Functions

Functions


         Palette Object  Description

                    Computes the natural logarithm of a square Input Matrix. Wire data to the Input
         Matrix                        Matrix input to determine the polymorphic instance to use or manually select the        Logarithm                          instance.


       LU            Performs the LU factorization of A so that PA = LU. Wire data to the A input to
         Factorization   determine the polymorphic instance to use or manually select the instance.


                       Performs Cholesky factorization on a symmetric or Hermitian positive definite        Cholesky                          matrix. Wire data to the A input to determine the polymorphic instance to use or         Factorization                      manually select the instance.


        Cholesky       Performs Cholesky factorization on the rank-1 updated Cholesky matrix. The VI
         Factorization   performs Cholesky factorization directly on the known factored matrix instead of
        Rank-1 Update  the updated matrix.


                       Performs the QR decomposition of A with or without column pivoting. Wire data to      QR                        the A input to determine the polymorphic instance to use or manually select the
        Decomposition                          instance.


                    Computes the singular value decomposition (SVD) of the m× nmatrix A. Wire data       SVD
                         to the A input to determine the polymorphic instance to use or manually select the        Decomposition
                          instance.

         Generalized    Computes the generalized singular value decomposition (GSVD) of a matrix pair
       SVD              (A,B). The data types you wire to the A and B inputs determine the polymorphic
        Decomposition  instance to use.

                       Performs the Schur decomposition of a square matrix. Wire data to the Input
        Schur
                        Matrix input to determine the polymorphic instance to use or manually select the
        Decomposition
                          instance.


2980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2981 ordinal=2981 -->
## Functions

Functions


Palette Object  Description

               Performs the Hessenberg decomposition of Input Matrix. Wire data to the Input
Hessenberg                Matrix input to determine the polymorphic instance to use or manually select theDecomposition                 instance.


QZ            Performs the QZ decomposition of a pair of square matrices. The data types you
Decomposition  wire to the A and B inputs determine the polymorphic instance to use.


Sylvester       Solves the Sylvester matrix equation. The data types you wire to the A, B, and C
Equations      inputs determine the polymorphic instance to use.


Lyapunov       Solves the Lyapunov matrix equation. The data types you wire to the A and B
Equations      inputs determine the polymorphic instance to use.


                Finds the eigenvalues and right eigenvectors of the square Input Matrix. Wire dataEigenvalues                to the Input Matrix input to determine the polymorphic instance to use or
and Vectors              manually select the instance.


Generalized    Computes the generalized right eigenvalues and eigenvectors of the matrix pair A
Eigenvalues    and B. The data types you wire to the A and B inputs determine the polymorphic
and Vectors     instance to use.


               Balances the general matrix Input Matrix to improve the accuracy of computed
Matrix Balance  eigenvalues and eigenvectors. Wire data to the Input Matrix input to determine
               the polymorphic instance to use or manually select the instance.


Back           Transforms the eigenvectors of a balanced matrix to those of the original matrix.
Transform      Wire data to the Eigenvectors input to determine the polymorphic instance to use
Eigenvectors    or manually select the instance.


                                                    © National Instruments 2981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2982 ordinal=2982 -->
## Functions

Functions


         Palette Object  Description

         Matrix        Computes the characteristic polynomial of Input Matrix. Wire data to the Input
          Characteristic   Matrix input to determine the polymorphic instance to use or manually select the
        Polynomial      instance.


         Basic Linear                     Use the Basic Linear Algebra Subroutines VIs to perform standard functions for         Algebra                         basic vector and matrix operations.
        Subroutines

      CreateCreate SpecialSpecial MatrixMatrix

       Generates a special matrix based on matrix type. The data types you wire to the Input
       Vector2 and Input Vector1 inputs determine the polymorphic instance to use.


            • Create Special Real Matrix VI
            • Create Special Complex Matrix VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Matrix to a
        Power.vi

      CreateCreate SpecialSpecial RealReal MatrixMatrix VIVI

       Generates a special matrix based on matrix type. The data types you wire to the Input
       Vector2 and Input Vector1 inputs determine the polymorphic instance to use.


2982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2983 ordinal=2983 -->
## Functions

Functions


Inputs/Outputs

   •      Input Vector2 —

    Input Vector2 used as the input to construct a special matrix in some options.

   •      matrix type —

    matrix type specifies the type of special matrix that this VI uses to generate as the Special Matrix
    output.

    Let nrepresent matrix size, X represent Input Vector1, nxrepresent the size of X, and Y
    represent Input Vector2, nyrepresent the size of Y, and B represent the output Special Matrix.

    0 Identity—Generates an n-by-nidentity matrix.
      Diagonal—Generates an nx-by-nxdiagonal matrix whose diagonal elements are the    1
      elements of X.
      Toeplitz—Generates an nx-by-nyToeplitz matrix, which has X as its first column and Y as its    2
         first row. If the first element of X and Y are different, the first element of X is used.

      Vandermonde—Generates an nx-by-nxVandermonde matrix whose columns are powers of
       the elements of X. The elements of a Vandermonde matrix are:

    3                  – j– 1       bi,j = xinx

      where i,j= 0…nx– 1.


      Companion—Generates an nx-1-by-nx-1 companion matrix. If vector X is a vector of a
      polynomial coefficient, the first element of X is the coefficient of the highest order, the last
      element of X is the constant term in the polynomial, the corresponding companion matrix is
       constructed as follows: the first row is
    4


       the rest of B from the second row is an identity matrix.


                                                    © National Instruments 2983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2984 ordinal=2984 -->
## Functions

Functions


             The eigenvalues of a companion matrix contain the roots of the corresponding polynomial.

             Hankel—Generates an nx-by-nyHankel matrix, where X is the first column and Y is the last
           5 row of the matrix. If the first element of Y and last element of X are different, this VI uses the
                  last element of X.
            Hadamard—Generates an n-by-nHadamard matrix, whose elements are 1 and –1. All
           6 columns or rows are orthogonal to each other. matrix size must be a power of 2, a power of 2
               multiplied by 12, or a power of 2 multiplied by 20. If nis 1, this VI returns an empty matrix.
           7 Wilkinson—Generates an n-by-nWilkinson matrix whose eigenvalues are ill-conditioned.

              Hilbert—Generates an n-by-nHilbert matrix, which has elements according to the following
               equation.

           8


             where i,j= 0,1,…n– 1

           9 Inverse Hilbert—Generates the inverse of an n-by-nHilbert matrix.
           10 Rosser—Generates an 8-by-8 Rosser matrix whose eigenvalues are ill-conditioned.

              Pascal—Generates an n-by-nsymmetric Pascal matrix, which has elements according to the
               following equation.

           11


             where i,j= 0,1,…n– 1


               •      matrix size —

            matrix size determines the dimension size of the output Special Matrix.

               •      Input Vector1 —

            Input Vector1 used as the input to construct a special matrix in some options.

               •      Special Matrix —

            Special Matrix is the generated matrix.


2984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2985 ordinal=2985 -->
## Functions

Functions

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Matrix to a
   Power.vi

CreateCreate SpecialSpecial ComplexComplex MatrixMatrix VIVI

Generates a special matrix based on matrix type. The data types you wire to the Input
Vector2 and Input Vector1 inputs determine the polymorphic instance to use.


Inputs/Outputs

   •      Input Vector2 —

    Input Vector2 used as the input to construct a special matrix in some options.

   •      matrix type —

    matrix type specifies the type of special matrix that this VI uses to generate as the Special Matrix
    output.

    Let nrepresent matrix size, X represent Input Vector1, nxrepresent the size of X, and Y
    represent Input Vector2, nyrepresent the size of Y, and B represent the output Special Matrix.

    0 Identity—Generates an n-by-nidentity matrix.
    1 Diagonal—Generates an nx-by-nxdiagonal matrix whose diagonal elements are the


                                                    © National Instruments 2985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2986 ordinal=2986 -->
## Functions

Functions


              elements of X.
              Toeplitz—Generates an nx-by-nyToeplitz matrix, which has X as its first column and Y as its           2
                    first row. If the first element of X and Y are different, the first element of X is used.

            Vandermonde—Generates an nx-by-nxVandermonde matrix whose columns are powers of
              the elements of X. The elements of a Vandermonde matrix are:

           3                           – j– 1               bi,j = xinx

             where i,j= 0…nx– 1.


             Companion—Generates an nx-1-by-nx-1 companion matrix. If vector X is a vector of a
              polynomial coefficient, the first element of X is the coefficient of the highest order, the last
             element of X is the constant term in the polynomial, the corresponding companion matrix is
               constructed as follows: the first row is

           4


              the rest of B from the second row is an identity matrix.

             The eigenvalues of a companion matrix contain the roots of the corresponding polynomial.

             Hankel—Generates an nx-by-nyHankel matrix, where X is the first column and Y is the last
           5 row of the matrix. If the first element of Y and last element of X are different, this VI uses the
                  last element of X.
            Hadamard—Generates an n-by-nHadamard matrix, whose elements are 1 and –1. All
           6 columns or rows are orthogonal to each other. matrix size must be a power of 2, a power of 2
               multiplied by 12, or a power of 2 multiplied by 20. If nis 1, this VI returns an empty matrix.
           7 Wilkinson—Generates an n-by-nWilkinson matrix whose eigenvalues are ill-conditioned.

              Hilbert—Generates an n-by-nHilbert matrix, which has elements according to the following
               equation.

           8


             where i,j= 0,1,…n– 1

           9 Inverse Hilbert—Generates the inverse of an n-by-nHilbert matrix.


2986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2987 ordinal=2987 -->
## Functions

Functions


    10 Rosser—Generates an 8-by-8 Rosser matrix whose eigenvalues are ill-conditioned.

      Pascal—Generates an n-by-nsymmetric Pascal matrix, which has elements according to the
       following equation.

    11


      where i,j= 0,1,…n– 1


   •      matrix size —

    matrix size determines the dimension size of the output Special Matrix.

   •      Input Vector1 —

    Input Vector1 used as the input to construct a special matrix in some options.

   •      Special Matrix —

    Special Matrix is the generated matrix.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Matrix to a
   Power.vi

CreateCreate RealReal MatrixMatrix FromFrom EigenvaluesEigenvalues

Generates a real matrix from Eigenvalues.


                                                    © National Instruments 2987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2988 ordinal=2988 -->
## Functions

Functions


      Inputs/Outputs

               •      Eigenvalues —

            Eigenvalues contains the eigenvalues from which you want to create Matrix. Eigenvalues must
          be real or conjugate pairs.

               •      Matrix —

            Matrix returns the real matrix whose eigenvalues are specified by Eigenvalues.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI generates the Matrix in the following form:


      where nis the length of Eigenvalues and a0, a1, …, an– 1 are the coefficients of the
      polynomial P(x).

      The following equation defines P(x):

      P(x) = (x– λ0)(x– λ1)···(x– λn– 1) = a0 + a1x+ a2x² + … + an– 1xn– 1 + xn

      where λ0, λ1, …, λn– 1 are the elements in Eigenvalues.

     SolveSolve LinearLinear EquationsEquations

       Solves a linear system AX = Y. The data types you wire to the Input Matrix and Known


2988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2989 ordinal=2989 -->
## Functions

Functions

Vector inputs determine the polymorphic instance to use.


   • Solve Linear Equations (single right hand) VI
   • Solve Linear Equations (multiple right hand) VI
   • Solve Complex Linear Equations (single right hand) VI
   • Solve Complex Linear Equations (multiple right hand) VI

Let A be an m-by-nmatrix that represents the Input Matrix, Y be the set of m
coefficients in Known Vector, and X be the set of nelements in Solution Vector that
solves the system

AX = Y

When m> n, the system has more equations than unknowns, so it is an over-
determined system. The solution that satisfies AX = Y might not exist, so the VI finds the
least-square solution X, which minimizes ||AX – Y||.

When m< n, the system has more unknowns than equations, so it is an under-
determined system. It may have infinite solutions that satisfy AX = Y. The VI finds one of
these solutions.

In the case of m= n, if A is a nonsingular matrix—no row or column is a linear
combination of any other row or column, respectively—then you can solve the system
for X by decomposing the input matrix A into its lower and upper triangular matrices, L
and U, such that

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.


                                                    © National Instruments 2989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2990 ordinal=2990 -->
## Functions

Functions

       Triangular systems are easy to solve using recursive techniques. Consequently, when
      you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
      from the UX = Z system.

        In the case of m≠ n, A can be decomposed to an orthogonal matrix Q and an upper
       triangular matrix R, so that A = QR. The linear system then can be represented by QRX =
          Y. You then can solve RX = QTY.

      You can easily solve this triangular system to get x using recursive techniques.

           Note You cannot always determine beforehand whether the matrix is
                singular, especially with large systems. The Solve Linear Equations VI detects
               singular matrices and returns an error, so you do not need to verify whether
            you have a valid system before using this VI.

      The numerical implementation of the matrix inversion is numerically intensive and,
      because of its recursive nature, is also highly sensitive to round-off error introduced by
       the floating-point numeric coprocessor. Although the computations use the maximum
       possible accuracy, the VI cannot always solve the system.

      Solve Complex Linear Equations

       Let A represent the m-by-nInput Matrix, Y represent the set of melements in the
     Known Vector, and X represent the set of nelements in the Solution Vector that solves
        for the system

      AX = Y

     When m> n, the system has more equations than unknowns, so it is an over-
      determined system. Since the solution that satisfies AX = Y may not exist, the VI finds
       the least-square solution X, which minimizes ||AX – Y||.

     When m< n, the system has more unknowns than equations, so it is an under-
      determined system. It might have infinite solutions that satisfy AX = Y. The VI then
        selects one of these solutions.


2990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2991 ordinal=2991 -->
## Functions

Functions

When m= n, if A is a nonsingular matrix—no row or column is a linear combination of
any other row or column, respectively—then you can solve the system for X by
decomposing the Input Matrix A into its lower and upper triangular matrices, L and U,
such that

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

When m≠ n, A can be decomposed to an orthogonal matrix Q, and an upper triangular
matrix R, so that A = QR, and the linear system can be represented by QRX = Y. You then
can solve RX = QHY. You can easily solve this triangular system to get X using recursive
techniques.

      Note The numerical implementation of the matrix inversion is numerically
        intensive and, because of its recursive nature, is also highly sensitive to
        round-off error introduced by the floating-point numeric coprocessor.
       Although the computations use the maximum possible accuracy, the VI
       cannot always solve for the system.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi


                                                    © National Instruments 2991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2992 ordinal=2992 -->
## Functions

Functions

      SolveSolve LinearLinear EquationsEquations (single(single rightright hand)hand) VIVI

       Solves a linear system AX = Y. The data types you wire to the Input Matrix and Known
       Vector inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is a square or rectangular, real matrix. The number of elements in the Known
            Vector must be equal to the rows of the Input Matrix. If the number of elements in the Known
            Vector does not match the rows of the Input Matrix, the VI sets the Solution Vector to an empty
             array and returns an error.

         When Input Matrix is singular, if the matrix type is General, the Solve Linear Equations VI finds
            the least-square solution. Otherwise, the VI returns an error.

               •     Known Vector —

         Known Vector is an array of known, dependent-variable values. The number of elements in the
         Known Vector must be equal to the rows of the Input Matrix. If the number of elements in the
         Known Vector does not match the rows of the Input Matrix, the VI sets the Solution Vector to an
          empty array and returns an error.

               •      matrix type —

            matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
           computation of the Solution Vector and can help you to avoid unnecessary computation, which
            could introduce numerical inaccuracy.

                  General
           0
                     (default)
           1      Positive definite
           2     Lower triangular
           3     Upper triangular

               •      Solution Vector —


2992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2993 ordinal=2993 -->
## Functions

Functions


    Solution Vector is the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let A be an m-by-nmatrix that represents the Input Matrix, Y be the set of m
coefficients in Known Vector, and X be the set of nelements in Solution Vector that
solves the system

AX = Y

When m> n, the system has more equations than unknowns, so it is an over-
determined system. The solution that satisfies AX = Y might not exist, so the VI finds the
least-square solution X, which minimizes ||AX – Y||.

When m< n, the system has more unknowns than equations, so it is an under-
determined system. It may have infinite solutions that satisfy AX = Y. The VI finds one of
these solutions.

In the case of m= n, if A is a nonsingular matrix—no row or column is a linear
combination of any other row or column, respectively—then you can solve the system
for X by decomposing the input matrix A into its lower and upper triangular matrices, L
and U, such that

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X

                                                    © National Instruments 2993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2994 ordinal=2994 -->
## Functions

Functions

      from the UX = Z system.

        In the case of m≠ n, A can be decomposed to an orthogonal matrix Q and an upper
       triangular matrix R, so that A = QR. The linear system then can be represented by QRX =
          Y. You then can solve RX = QTY.

      You can easily solve this triangular system to get x using recursive techniques.

           Note You cannot always determine beforehand whether the matrix is
                singular, especially with large systems. The Solve Linear Equations VI detects
               singular matrices and returns an error, so you do not need to verify whether
            you have a valid system before using this VI.

      The numerical implementation of the matrix inversion is numerically intensive and,
      because of its recursive nature, is also highly sensitive to round-off error introduced by
       the floating-point numeric coprocessor. Although the computations use the maximum
       possible accuracy, the VI cannot always solve the system.

      Solve Complex Linear Equations

       Let A represent the m-by-nInput Matrix, Y represent the set of melements in the
     Known Vector, and X represent the set of nelements in the Solution Vector that solves
        for the system

      AX = Y

     When m> n, the system has more equations than unknowns, so it is an over-
      determined system. Since the solution that satisfies AX = Y may not exist, the VI finds
       the least-square solution X, which minimizes ||AX – Y||.

     When m< n, the system has more unknowns than equations, so it is an under-
      determined system. It might have infinite solutions that satisfy AX = Y. The VI then
        selects one of these solutions.

     When m= n, if A is a nonsingular matrix—no row or column is a linear combination of
      any other row or column, respectively—then you can solve the system for X by


2994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2995 ordinal=2995 -->
## Functions

Functions

decomposing the Input Matrix A into its lower and upper triangular matrices, L and U,
such that

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

When m≠ n, A can be decomposed to an orthogonal matrix Q, and an upper triangular
matrix R, so that A = QR, and the linear system can be represented by QRX = Y. You then
can solve RX = QHY. You can easily solve this triangular system to get X using recursive
techniques.

      Note The numerical implementation of the matrix inversion is numerically
        intensive and, because of its recursive nature, is also highly sensitive to
        round-off error introduced by the floating-point numeric coprocessor.
       Although the computations use the maximum possible accuracy, the VI
       cannot always solve for the system.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

SolveSolve LinearLinear EquationsEquations (multiple(multiple rightright hand)hand) VIVI

Solves a linear system AX = Y. The data types you wire to the Input Matrix and Known

                                                    © National Instruments 2995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2996 ordinal=2996 -->
## Functions

Functions

       Vector inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is a square or rectangular, real matrix. The number of rows in the Known Matrix
          must be equal to the rows of the Input Matrix. If the number of rows in the Known Matrix does
            not match the rows of the Input Matrix, the VI sets the Solution Matrix to an empty matrix and
             returns an error.

         When Input Matrix is singular, if the matrix type is General, the VI finds the least-square solution.
            Otherwise, the VI returns an error.

               •     Known Matrix —

         Known Matrix is a matrix of known, dependent-variable values. Known Matrix must have the
          same number of rows as Input Matrix. If the number of rows in Known Matrix and Input Matrix
            are not equal, the VI sets Solution Matrix to an empty matrix and returns an error.

               •      matrix type —

            matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
           computation of the Solution Matrix and can help you to avoid unnecessary computation, which
            could introduce numerical inaccuracy.

                  General
           0
                     (default)
           1      Positive definite
           2     Lower triangular
           3     Upper triangular

               •      Solution Matrix —

            Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known
             Matrix.

               •       error —


2996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2997 ordinal=2997 -->
## Functions

Functions


     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let A be an m-by-nmatrix that represents the Input Matrix, Y be the set of m
coefficients in Known Vector, and X be the set of nelements in Solution Vector that
solves the system

AX = Y

When m> n, the system has more equations than unknowns, so it is an over-
determined system. The solution that satisfies AX = Y might not exist, so the VI finds the
least-square solution X, which minimizes ||AX – Y||.

When m< n, the system has more unknowns than equations, so it is an under-
determined system. It may have infinite solutions that satisfy AX = Y. The VI finds one of
these solutions.

In the case of m= n, if A is a nonsingular matrix—no row or column is a linear
combination of any other row or column, respectively—then you can solve the system
for X by decomposing the input matrix A into its lower and upper triangular matrices, L
and U, such that

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

In the case of m≠ n, A can be decomposed to an orthogonal matrix Q and an upper

                                                    © National Instruments 2997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2998 ordinal=2998 -->
## Functions

Functions

       triangular matrix R, so that A = QR. The linear system then can be represented by QRX =
          Y. You then can solve RX = QTY.

      You can easily solve this triangular system to get x using recursive techniques.

           Note You cannot always determine beforehand whether the matrix is
                singular, especially with large systems. The Solve Linear Equations VI detects
               singular matrices and returns an error, so you do not need to verify whether
            you have a valid system before using this VI.

      The numerical implementation of the matrix inversion is numerically intensive and,
      because of its recursive nature, is also highly sensitive to round-off error introduced by
       the floating-point numeric coprocessor. Although the computations use the maximum
       possible accuracy, the VI cannot always solve the system.

      Solve Complex Linear Equations

       Let A represent the m-by-nInput Matrix, Y represent the set of melements in the
     Known Vector, and X represent the set of nelements in the Solution Vector that solves
        for the system

      AX = Y

     When m> n, the system has more equations than unknowns, so it is an over-
      determined system. Since the solution that satisfies AX = Y may not exist, the VI finds
       the least-square solution X, which minimizes ||AX – Y||.

     When m< n, the system has more unknowns than equations, so it is an under-
      determined system. It might have infinite solutions that satisfy AX = Y. The VI then
        selects one of these solutions.

     When m= n, if A is a nonsingular matrix—no row or column is a linear combination of
      any other row or column, respectively—then you can solve the system for X by
      decomposing the Input Matrix A into its lower and upper triangular matrices, L and U,
      such that


2998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2999 ordinal=2999 -->
## Functions

Functions

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

When m≠ n, A can be decomposed to an orthogonal matrix Q, and an upper triangular
matrix R, so that A = QR, and the linear system can be represented by QRX = Y. You then
can solve RX = QHY. You can easily solve this triangular system to get X using recursive
techniques.

      Note The numerical implementation of the matrix inversion is numerically
        intensive and, because of its recursive nature, is also highly sensitive to
        round-off error introduced by the floating-point numeric coprocessor.
       Although the computations use the maximum possible accuracy, the VI
       cannot always solve for the system.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

SolveSolve ComplexComplex LinearLinear EquationsEquations (single(single rightright hand)hand) VIVI

Solves a linear system AX = Y. The data types you wire to the Input Matrix and Known
Vector inputs determine the polymorphic instance to use.


                                                    © National Instruments 2999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3000 ordinal=3000 -->
## Functions

Functions


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix must be a nonsingular, square or rectangular, complex matrix. A nonsingular matrix
                is a matrix in which no row or column contains a linear combination of any other row or column,
              respectively. You cannot always determine beforehand whether the matrix is singular, especially
            with large systems.

         When Input Matrix is singular, if the matrix type is General, the VI finds the least-square solution.
            Otherwise, the VI returns an error.

               •     Known Vector —

         Known Vector is an array of known, dependent-variable values. The number of elements in
         Known Vector must match the row size of the Input Matrix. If the number of elements in Known
            Vector does not match the row size of Input Matrix, the VI sets Solution Vector to an empty array
          and returns an error.

               •      matrix type —

            matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
           computation of the Solution Vector and can help you to avoid unnecessary computation, which
            could introduce numerical inaccuracy.

                  General           0
                     (default)
           1      Positive definite
           2     Lower triangular
           3     Upper triangular

               •      Solution Vector —

            Solution Vector is the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3000 -->

